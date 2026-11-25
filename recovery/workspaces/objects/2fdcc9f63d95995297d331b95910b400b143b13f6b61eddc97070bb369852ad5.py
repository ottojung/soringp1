#!/usr/bin/env python3
"""Resource-availability instrument of the Ministry of Economy (Act 29 section 6).

Model funding is only one scarce resource. This script measures the others the
Town can run out of on its box (disk space, inodes, memory headroom, load), keeps
a short history so it can forecast *time to full* rather than only react to a
percentage, and ACTS early through the Janitor's own pipeline (Act 12) instead of
waiting for the Janitor's alert thresholds. It makes no model call.

It never deletes anything itself. Every reclamation step is a Janitor mode
(`janitor.sh inventory|classify|scratch-quarantine|quarantine|reclaim-idle-caches|
reclaim|reclaim-quarantined`), so the Janitor's invariants stay in force: evidence
before action (12.4), nothing under records/, government/, credentials or live
processes (12.5), quarantine before removal and `reclaim_enabled` (12.7).

Status per resource, worst first: critical > short > watch > ok.

  refresh [--no-act] [--dry-run]   measure, record, forecast, act, write the report
  measure                           print the measurement, change nothing
  report                            print the latest report
  needs                             print the NEEDS-FOUNDER lines of the latest report

Policy: state/economy/resource-policy.json (the Ministry may tune thresholds with
evidence; the defaults below are used for anything absent).

Environment
  VICHE_TOWN_ROOT, VICHE_SEATS_ROOT, VICHE_STATE_ROOT   as elsewhere
  VICHE_ECONOMY_NOW           epoch override (tests)
  VICHE_ECONOMY_FS_OVERRIDE   JSON {label:{total,avail,files,ffree}} (tests)
  VICHE_ECONOMY_LOAD_OVERRIDE JSON {load1,load5,load15,cpus?} load override (tests; keeps
                              the smoke suite hermetic under host load spikes)
  VICHE_ECONOMY_CGROUP        cgroup directory (default /sys/fs/cgroup)
  VICHE_ECONOMY_JANITOR       janitor script path (default $TOWN/government/janitor.sh)
"""
import argparse
import datetime
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import time

TOWN = pathlib.Path(os.environ.get("VICHE_TOWN_ROOT", "/var/lib/lubko/wd/viche"))
SEATS = pathlib.Path(os.environ.get("VICHE_SEATS_ROOT", "/var/lib/lubko/wd/viche-seats"))
STATE = pathlib.Path(os.environ.get("VICHE_STATE_ROOT", "/var/lib/lubko/wd/viche-state"))
ROOT = STATE / "economy"
HOME = pathlib.Path(os.environ.get("HOME", "/home/lubko"))
CGROUP = pathlib.Path(os.environ.get("VICHE_ECONOMY_CGROUP", "/sys/fs/cgroup"))
JANITOR = pathlib.Path(os.environ.get("VICHE_ECONOMY_JANITOR", str(TOWN / "government" / "janitor.sh")))
RANKS = ["ok", "watch", "short", "critical"]
GIB = 1024 ** 3
HISTORY_KEEP = 14 * 86400
SAMPLE_EVERY = 600

DEFAULT_POLICY = {
    "disk_used_pct": [70, 80, 90],          # watch, short, critical
    "disk_hours_to_full": [168, 72, 24],    # watch, short, critical (shorter is worse)
    "inode_used_pct": [80, 90, 95],
    "memory_headroom_bytes": [3 * GIB, 2 * GIB, 1 * GIB],   # Act 13 floor is 2 GiB, critical 1 GiB
    "load_per_cpu": [1.5, 3.0, 6.0],
    "min_free_bytes_critical": 5 * GIB,
    "action_interval_seconds": 21600,
}


def now():
    return int(os.environ.get("VICHE_ECONOMY_NOW", time.time()))


def stamp(epoch):
    return datetime.datetime.fromtimestamp(epoch, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def atomic_write(path, text):
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".tmp.", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w") as handle:
            handle.write(text)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def load(path, default):
    try:
        return json.loads(pathlib.Path(path).read_text())
    except (OSError, ValueError):
        return default


def policy():
    merged = dict(DEFAULT_POLICY)
    custom = load(ROOT / "resource-policy.json", {})
    if isinstance(custom, dict):
        for key, value in custom.items():
            if key in merged and type(value) == type(merged[key]):
                if isinstance(value, list) and len(value) != len(merged[key]):
                    continue
                merged[key] = value
    return merged


def rank_up(value, limits):
    """Rank of a 'higher is worse' value against [watch, short, critical]."""
    return sum(1 for limit in limits if value >= limit)


def rank_down(value, limits):
    """Rank of a 'lower is worse' value against [watch, short, critical]."""
    return sum(1 for limit in limits if value <= limit)


def worst(*ranks):
    return max(ranks) if ranks else 0


# ---- measurement ------------------------------------------------------------

def filesystems():
    override = os.environ.get("VICHE_ECONOMY_FS_OVERRIDE")
    if override:
        data = load(override, {})
        return {label: dict(values, mount=label) for label, values in data.items()}
    out = {}
    seen = {}
    for label, path in (("state", STATE), ("seats", SEATS), ("town", TOWN), ("home", HOME), ("tmp", pathlib.Path("/tmp"))):
        try:
            dev = os.stat(path).st_dev
            vfs = os.statvfs(path)
        except OSError:
            continue
        if dev in seen:
            out[seen[dev]].setdefault("also", []).append(label)
            continue
        seen[dev] = label
        used = (vfs.f_blocks - vfs.f_bfree) * vfs.f_frsize
        avail = vfs.f_bavail * vfs.f_frsize
        out[label] = {"mount": str(path), "total": vfs.f_blocks * vfs.f_frsize, "used": used, "avail": avail,
                      "files": vfs.f_files, "ffree": vfs.f_ffree}
    return out


def memory():
    try:
        maximum = (CGROUP / "memory.max").read_text().strip()
        if maximum == "max" or not maximum.isdigit():
            return {"status": "unknown", "note": "no cgroup memory limit"}
        stat = {}
        for line in (CGROUP / "memory.stat").read_text().splitlines():
            key, _, value = line.partition(" ")
            stat[key] = int(value) if value.strip().isdigit() else 0
        unreclaimable = sum(stat.get(k, 0) for k in ("anon", "slab", "kernel_stack", "sock"))
        events = {}
        try:
            for line in (CGROUP / "memory.events").read_text().splitlines():
                key, _, value = line.partition(" ")
                events[key] = int(value) if value.strip().isdigit() else 0
        except OSError:
            pass
        return {"max": int(maximum), "unreclaimable": unreclaimable, "headroom": int(maximum) - unreclaimable,
                "oom_kill": events.get("oom_kill", 0), "max_hits": events.get("max", 0)}
    except (OSError, ValueError):
        return {"status": "unknown", "note": "cgroup memory unreadable"}


def load_average():
    override = os.environ.get("VICHE_ECONOMY_LOAD_OVERRIDE")
    if override:
        try:
            data = json.loads(override)
            one, five, fifteen = (float(data[k]) for k in ("load1", "load5", "load15"))
        except (ValueError, TypeError, KeyError, json.JSONDecodeError):
            return {"status": "unknown"}
        cpus = int(data.get("cpus", os.cpu_count() or 1))
    else:
        try:
            one, five, fifteen = os.getloadavg()
        except OSError:
            return {"status": "unknown"}
        cpus = os.cpu_count() or 1
    return {"load1": round(one, 2), "load5": round(five, 2), "load15": round(fifteen, 2), "cpus": cpus,
            "per_cpu": round(five / cpus, 2)}


def growth_sizes(current, urgent):
    """Sizes of the Town-owned top-level directories, cached; du is slow on a big box."""
    cache = load(ROOT / "sizes.json", {})
    age = current - int(cache.get("at", 0))
    if age < (3600 if urgent else 21600) and cache.get("dirs"):
        return cache
    dirs = []
    budget_end = time.time() + 150
    for base in (STATE, SEATS):
        if not base.is_dir():
            continue
        try:
            children = sorted(p for p in base.iterdir() if p.is_dir() and not p.is_symlink())
        except OSError:
            continue
        for child in children:
            if time.time() > budget_end:
                break
            try:
                done = subprocess.run(["du", "-sk", str(child)], capture_output=True, text=True, timeout=60)
                kb = int(done.stdout.split()[0])
            except (OSError, ValueError, IndexError, subprocess.TimeoutExpired):
                continue
            dirs.append({"path": str(child), "kb": kb})
    dirs.sort(key=lambda d: -d["kb"])
    result = {"at": current, "dirs": dirs[:12], "total_kb": sum(d["kb"] for d in dirs)}
    atomic_write(ROOT / "sizes.json", json.dumps(result, sort_keys=True) + "\n")
    return result


# ---- history and forecast ---------------------------------------------------

def read_history(current):
    path = ROOT / "resource-history.jsonl"
    rows = []
    try:
        for line in path.read_text().splitlines():
            try:
                row = json.loads(line)
            except ValueError:
                continue
            if isinstance(row, dict) and current - int(row.get("at", 0)) <= HISTORY_KEEP:
                rows.append(row)
    except OSError:
        pass
    return rows


def record_sample(rows, fs, mem, current):
    if rows and current - int(rows[-1].get("at", 0)) < SAMPLE_EVERY:
        return rows
    row = {"at": current, "fs": {label: {"avail": v["avail"]} for label, v in fs.items() if "avail" in v}}
    if "headroom" in mem:
        row["mem_headroom"] = mem["headroom"]
    rows = rows + [row]
    atomic_write(ROOT / "resource-history.jsonl", "".join(json.dumps(r, sort_keys=True) + "\n" for r in rows))
    return rows


def forecast_hours(rows, label, avail_now, current):
    """Hours until the filesystem is full at the rate observed over the last day (None: not shrinking)."""
    window = [r for r in rows if 7200 <= current - int(r.get("at", 0)) <= 86400 and label in r.get("fs", {})]
    if not window:
        window = [r for r in rows if 3600 <= current - int(r.get("at", 0)) <= 7200 and label in r.get("fs", {})]
    if not window:
        return None
    then = min(window, key=lambda r: r["at"])
    hours = (current - then["at"]) / 3600.0
    lost = then["fs"][label]["avail"] - avail_now
    if hours <= 0 or lost <= 0:
        return None
    rate = lost / hours
    return round(avail_now / rate, 1)


# ---- evaluation -------------------------------------------------------------

def evaluate(pol, fs, mem, load_avg, funding, rows, current):
    resources = {}
    for label, v in fs.items():
        if "total" not in v:
            continue
        used = v.get("used")
        if used is None:
            used = v["total"] - v["avail"]
        pct = round(100.0 * used / max(used + v["avail"], 1), 1)
        hours = forecast_hours(rows, label, v["avail"], current)
        rank = rank_up(pct, pol["disk_used_pct"])
        if hours is not None:
            rank = worst(rank, rank_down(hours, pol["disk_hours_to_full"]))
        if v["avail"] < pol["min_free_bytes_critical"]:
            rank = 3
        inode_pct = None
        if v.get("files"):
            inode_pct = round(100.0 * (v["files"] - v.get("ffree", 0)) / v["files"], 1)
            rank = worst(rank, rank_up(inode_pct, pol["inode_used_pct"]))
        resources["disk:" + label] = {
            "status": RANKS[rank], "used_pct": pct, "avail_gib": round(v["avail"] / GIB, 1),
            "total_gib": round(v["total"] / GIB, 1), "inode_used_pct": inode_pct,
            "hours_to_full": hours, "mount": v.get("mount"), "also": v.get("also", [])}
    if "headroom" in mem:
        rank = rank_down(mem["headroom"], pol["memory_headroom_bytes"])
        resources["memory"] = {"status": RANKS[rank], "headroom_gib": round(mem["headroom"] / GIB, 2),
                               "oom_kills": mem["oom_kill"], "max_hits": mem["max_hits"]}
    else:
        resources["memory"] = {"status": "ok", "note": mem.get("note", "unmeasured")}
    if "per_cpu" in load_avg:
        resources["load"] = dict(load_avg, status=RANKS[rank_up(load_avg["per_cpu"], pol["load_per_cpu"])])
    risk = funding.get("funding_risk") if isinstance(funding, dict) else None
    resources["model_funding"] = {"status": {"none": "ok", "elevated": "watch", "high": "critical"}.get(risk, "ok"),
                                  "funding_risk": risk or "unknown",
                                  "free_available_now": (funding or {}).get("free_available_now")}
    return resources


def overall(resources):
    return max((RANKS.index(r["status"]) for r in resources.values()), default=0)


# ---- action -----------------------------------------------------------------

def janitor(mode, dry_run):
    if not JANITOR.is_file():
        return {"mode": mode, "ok": False, "detail": "janitor.sh not found"}
    command = ["/bin/sh", str(JANITOR), mode] + (["--dry-run"] if dry_run else [])
    try:
        done = subprocess.run(command, capture_output=True, text=True, timeout=900)
    except subprocess.TimeoutExpired:
        return {"mode": mode, "ok": False, "detail": "timeout"}
    last = (done.stdout.strip().splitlines() or [""])[-1][:200]
    return {"mode": mode, "ok": done.returncode == 0, "detail": last or done.stderr.strip()[:200]}


def disk_level(resources):
    return max((RANKS.index(r["status"]) for k, r in resources.items() if k.startswith("disk:")), default=0)


def act(pol, resources, current, dry_run):
    """Janitor steps by severity. Returns the actions taken (possibly none)."""
    state_path = ROOT / "action-state.json"
    state = load(state_path, {})
    taken = []
    level = disk_level(resources)
    if level >= 1 and current - int(state.get("last_disk_action", 0)) >= pol["action_interval_seconds"] - (
            pol["action_interval_seconds"] // 2 if level >= 3 else 0):
        steps = ["inventory", "classify"]
        if level >= 2:
            steps += ["scratch-quarantine", "quarantine", "reclaim-idle-caches", "reclaim", "reclaim-quarantined"]
        for mode in steps:
            result = janitor(mode, dry_run)
            result["at"] = stamp(current)
            result["level"] = RANKS[level]
            taken.append(result)
        if not dry_run:
            state["last_disk_action"] = current
            state["last_disk_level"] = RANKS[level]
    if not dry_run:
        atomic_write(state_path, json.dumps(state, sort_keys=True) + "\n")
        if taken:
            with open(ROOT / "actions.log", "a") as log:
                for item in taken:
                    log.write(json.dumps(item, sort_keys=True) + "\n")
    return taken


def needs_founder(resources, taken, previous):
    """One line per resource that is still short or critical after acting; the Founder is told what to do."""
    lines = []
    for key, r in sorted(resources.items()):
        if RANKS.index(r["status"]) < 2:
            continue
        if key.startswith("disk:"):
            persisted = previous.get(key, {}).get("status") in ("short", "critical")
            if r["status"] == "critical" or persisted:
                lines.append("NEEDS-FOUNDER: disk %s is %s (%.1f%% used, %.1f GiB free%s) after the Janitor pipeline ran; "
                             "free space on this box or approve removing a named directory."
                             % (key.split(":", 1)[1], r["status"], r["used_pct"], r["avail_gib"],
                                "" if r["hours_to_full"] is None else ", full in about %.0f h" % r["hours_to_full"]))
        elif key == "memory" and r["status"] == "critical":
            lines.append("NEEDS-FOUNDER: memory headroom is %.2f GiB (critical, Act 13); more memory or fewer concurrent seats."
                         % r["headroom_gib"])
        elif key == "model_funding" and r["status"] == "critical":
            lines.append("NEEDS-FOUNDER: no free model is available now; the Town would fall back to paid models.")
    return lines


# ---- commands ---------------------------------------------------------------

def measure(current, record=True):
    pol = policy()
    fs = filesystems()
    mem = memory()
    load_avg = load_average()
    funding = load(ROOT / "report.json", {})
    rows = read_history(current)
    if record:
        rows = record_sample(rows, fs, mem, current)
    resources = evaluate(pol, fs, mem, load_avg, funding, rows, current)
    return pol, resources


def refresh(args):
    current = now()
    ROOT.mkdir(parents=True, exist_ok=True)
    previous = load(ROOT / "resources.json", {}).get("resources", {})
    pol, resources = measure(current)
    taken = []
    if not args.no_act:
        taken = act(pol, resources, current, args.dry_run)
        if taken and not args.dry_run:
            # Re-measure: reclaiming may already have moved the numbers.
            pol, resources = measure(current)
    level = overall(resources)
    sizes = growth_sizes(current, level >= 2) if not os.environ.get("VICHE_ECONOMY_NO_DU") else {}
    report = {
        "at": stamp(current), "epoch": current, "overall": RANKS[level], "resources": resources,
        "actions_this_pass": taken, "needs_founder": needs_founder(resources, taken, previous),
        "town_owned_largest": sizes.get("dirs", [])[:8], "town_owned_total_kb": sizes.get("total_kb"),
        "policy": pol,
    }
    atomic_write(ROOT / "resources.json", json.dumps(report, sort_keys=True, indent=1) + "\n")
    summary = {"overall": report["overall"], "actions": len(taken), "needs_founder": len(report["needs_founder"])}
    print(json.dumps(summary, sort_keys=True))
    return 0


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    refresh_p = sub.add_parser("refresh")
    refresh_p.add_argument("--no-act", action="store_true")
    refresh_p.add_argument("--dry-run", action="store_true")
    sub.add_parser("measure")
    sub.add_parser("report")
    sub.add_parser("needs")
    args = parser.parse_args(argv)
    if args.command == "refresh":
        return refresh(args)
    if args.command == "measure":
        pol, resources = measure(now(), record=False)
        print(json.dumps({"overall": RANKS[overall(resources)], "resources": resources}, indent=1, sort_keys=True))
        return 0
    if args.command == "report":
        print(json.dumps(load(ROOT / "resources.json", {}), indent=1, sort_keys=True))
        return 0
    if args.command == "needs":
        for line in load(ROOT / "resources.json", {}).get("needs_founder", []):
            print(line)
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
