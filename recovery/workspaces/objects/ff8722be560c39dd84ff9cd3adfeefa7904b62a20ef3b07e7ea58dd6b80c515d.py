#!/usr/bin/env python3
"""Model funding instrument of the Ministry of Economy (Act 29).

Antonina tries the models in ~/.config/antonina/config.json in order. The Town's
reliable funding is therefore the ORDER of that list: free models first, so the
Town keeps running at no cost; paid models last, as a fallback of last resort.

This script is the deterministic half of the Ministry. It discovers what exists
(`opencode models`), verifies that candidate free models actually answer, and
rewrites the Antonina list so that the tier order can never be violated, whatever
the Ministry's agent proposes. The agent supplies judgment (what to exclude, what
to prefer within a tier, which sources to read) through
state/economy/model-policy.json; it does not hand-edit the config.

Tiers, best first (a model's tier is decided by this table, not by the agent):
  0 free         id carries a "-free" component (opencode/beam-free, ...). Only
                 added to the list after a probe succeeds; probes are free.
  1 contributor  "-contributor" models of opencode-go: included with the
                 contributor plan. Never auto-added, only kept.
  2 paid         every other model. Never auto-added, only kept.
  3 luna         any "luna" model (openai/gpt-6-luna, ...): paid, and kept at the
                 very bottom, after every other paid model.

Commands
  refresh [--probe-limit N] [--no-apply]   catalogue + probes + plan + apply + report
  plan                                      print the planned order, change nothing
  check                                     exit 1 if the live config breaks the tier order
  report                                    print the latest report

Environment
  VICHE_ANTONINA_CONFIG   config path (default ~/.config/antonina/config.json)
  VICHE_OPENCODE_MODELS   file with `opencode models` output (tests)
  VICHE_STATE_ROOT        state root; files live under economy/
"""
import argparse
import datetime
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time

STATE = pathlib.Path(os.environ.get("VICHE_STATE_ROOT", "/var/lib/lubko/wd/viche-state"))
ROOT = STATE / "economy"
HOME = pathlib.Path(os.environ.get("HOME", "/home/lubko"))
CONFIG = pathlib.Path(os.environ.get(
    "VICHE_ANTONINA_CONFIG",
    str(pathlib.Path(os.environ.get("XDG_CONFIG_HOME", HOME / ".config")) / "antonina" / "config.json")))
COOLDOWNS = pathlib.Path(os.environ.get(
    "VICHE_ANTONINA_COOLDOWNS",
    str(pathlib.Path(os.environ.get("XDG_STATE_HOME", HOME / ".local" / "state")) / "antonina" / "model-cooldowns")))
MAX_MODELS = int(os.environ.get("VICHE_ECONOMY_MAX_MODELS", "14"))
PROBE_FRESH_SECONDS = 14 * 86400
PROBE_TIMEOUT = int(os.environ.get("VICHE_ECONOMY_PROBE_TIMEOUT", "120"))
TIER_NAMES = ["free", "contributor", "paid", "luna"]


def now():
    return int(os.environ.get("VICHE_ECONOMY_NOW", time.time()))


def tier_of(model):
    """The tier table. Luna wins over every other rule: it always sorts last."""
    name = model.lower()
    if "luna" in name:
        return 3
    if re.search(r"(^|[-/])free($|[-/])", name):
        return 0
    if "contributor" in name:
        return 1
    return 2


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


def read_config():
    data = load(CONFIG, None)
    if not isinstance(data, dict) or not isinstance(data.get("models"), list):
        raise SystemExit("Antonina config unreadable or has no models list: %s" % CONFIG)
    return data


def entry_model(entry):
    return entry if isinstance(entry, str) else entry.get("model", "")


def fetch_catalogue():
    override = os.environ.get("VICHE_OPENCODE_MODELS")
    if override:
        text = pathlib.Path(override).read_text()
    else:
        done = subprocess.run(["opencode", "models"], capture_output=True, text=True, timeout=90)
        if done.returncode != 0:
            raise RuntimeError("opencode models failed: " + done.stderr.strip()[:200])
        text = done.stdout
    ids = [line.strip() for line in text.splitlines() if re.match(r"^[A-Za-z0-9._-]+/[A-Za-z0-9._#:-]+$", line.strip())]
    if len(ids) < 10:
        raise RuntimeError("model catalogue implausibly small (%d); refusing to act on it" % len(ids))
    return sorted(set(ids))


def update_catalogue(ids, current):
    store = load(ROOT / "catalogue.json", {"models": {}})
    models = store.get("models", {})
    stamp = datetime.datetime.fromtimestamp(current, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    new_free = []
    for model in ids:
        entry = models.setdefault(model, {"first_seen": stamp})
        entry["last_seen"] = stamp
        entry["tier"] = TIER_NAMES[tier_of(model)]
        if entry["first_seen"] == stamp and store.get("models") and tier_of(model) == 0 and "fetched_at" in store:
            new_free.append(model)
    gone = sorted(m for m in models if m not in ids)
    store = {"fetched_at": stamp, "models": models, "gone": gone}
    atomic_write(ROOT / "catalogue.json", json.dumps(store, sort_keys=True, indent=1) + "\n")
    return models, new_free, gone


def probe(model):
    prompt = "Reply with the single word OK and nothing else."
    try:
        done = subprocess.run(["opencode", "run", "-m", model, "--format", "json", prompt],
                              capture_output=True, text=True, timeout=PROBE_TIMEOUT, cwd="/tmp")
    except subprocess.TimeoutExpired:
        return False, "timeout after %ds" % PROBE_TIMEOUT
    out = done.stdout
    if done.returncode != 0:
        return False, ("exit %d: %s" % (done.returncode, done.stderr.strip()[:160]))
    if '"type":"error"' in out:
        return False, "provider error event"
    texts = []
    for line in out.splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        part = event.get("part", {})
        if event.get("type") == "text" and isinstance(part.get("text"), str):
            texts.append(part["text"])
    if any("OK" in t.upper() for t in texts):
        return True, "answered OK"
    return False, "no usable answer"


def run_probes(candidates, limit, current):
    probes = load(ROOT / "probes.json", {})
    stale = [m for m in candidates
             if m not in probes or current - probes[m].get("at", 0) > PROBE_FRESH_SECONDS]
    stale.sort(key=lambda m: probes.get(m, {}).get("at", 0))
    ran = []
    for model in stale[:limit]:
        ok, detail = probe(model)
        probes[model] = {"ok": ok, "at": current, "detail": detail}
        ran.append(model)
    atomic_write(ROOT / "probes.json", json.dumps(probes, sort_keys=True, indent=1) + "\n")
    return probes, ran


def policy():
    data = load(ROOT / "model-policy.json", {})
    exclude = {}
    for item in data.get("exclude", []):
        if isinstance(item, dict) and item.get("model"):
            if int(item.get("until", 0)) > now():
                exclude[item["model"]] = item
    return {"exclude": exclude, "prefer": [m for m in data.get("prefer", []) if isinstance(m, str)]}


def plan_order(cfg, catalogue_ids, probes, pol, current):
    configured = [entry_model(e) for e in cfg["models"] if entry_model(e)]
    in_catalogue = set(catalogue_ids)
    wanted = {0: [], 1: [], 2: [], 3: []}
    dropped = []
    seen = set()

    def consider(model, grandfathered):
        if model in seen:
            return
        seen.add(model)
        tier = tier_of(model)
        if model not in in_catalogue:
            dropped.append((model, "not in catalogue"))
            return
        if model in pol["exclude"]:
            dropped.append((model, "excluded by policy: " + str(pol["exclude"][model].get("reason", ""))))
            return
        if tier == 0:
            result = probes.get(model)
            if result is not None and not result.get("ok") and current - result.get("at", 0) < PROBE_FRESH_SECONDS:
                dropped.append((model, "probe failed: " + str(result.get("detail", ""))))
                return
            if result is None and not grandfathered:
                return  # unprobed newcomers wait for their probe
        elif not grandfathered:
            return  # contributor/paid/luna models are only ever kept, never auto-added
        wanted[tier].append(model)

    for model in configured:
        consider(model, True)
    for model in catalogue_ids:
        if tier_of(model) == 0:
            consider(model, False)

    def rank(model):
        prefer = pol["prefer"]
        p = prefer.index(model) if model in prefer else len(prefer)
        c = configured.index(model) if model in configured else len(configured)
        return (p, c, model)

    final = []
    for tier in range(4):
        final.extend(sorted(wanted[tier], key=rank))
    final = final[:MAX_MODELS]
    if not final:
        raise SystemExit("plan would leave Antonina with no models; refusing")
    return configured, final, dropped


def violations(models):
    tiers = [tier_of(m) for m in models]
    return [(models[i], models[i + 1]) for i in range(len(models) - 1) if tiers[i] > tiers[i + 1]]


def apply_order(cfg, final, probes, dropped, current):
    existing = {entry_model(e): e for e in cfg["models"]}
    stamp = datetime.datetime.fromtimestamp(current, datetime.timezone.utc).strftime("%Y-%m-%d")
    new_entries = []
    for model in final:
        entry = existing.get(model)
        if entry is None:
            entry = {"model": model, "comment": "Ministry of Economy %s: free model, probe answered OK." % stamp}
        elif isinstance(entry, str):
            entry = {"model": entry}
        new_entries.append(entry)
    updated = dict(cfg)
    updated["models"] = new_entries
    backup = CONFIG.with_name(CONFIG.name + ".bak-" + str(current))
    shutil.copy2(CONFIG, backup)
    atomic_write(CONFIG, json.dumps(updated, indent=2) + "\n")
    os.chmod(CONFIG, 0o600)
    try:
        listed = subprocess.run(["antonina", "agent", "model", "select"], capture_output=True, text=True, timeout=60)
        ok = listed.returncode == 0 and final[0] in listed.stdout
    except (OSError, subprocess.TimeoutExpired):
        ok = os.environ.get("VICHE_ECONOMY_SKIP_VALIDATE") == "1"
    if not ok and os.environ.get("VICHE_ECONOMY_SKIP_VALIDATE") != "1":
        shutil.copy2(backup, CONFIG)
        raise SystemExit("Antonina rejected the new model list; previous config restored from " + str(backup))
    return str(backup)


def cooldown_state(models, current):
    out = {}
    if COOLDOWNS.is_dir():
        for path in COOLDOWNS.glob("*.json"):
            data = load(path, {})
            until = data.get("until", 0)
            if data.get("model") in models and until > current:
                out[data["model"]] = {"reason": data.get("reason"), "until": int(until)}
    return out


def build_report(final, cfg_before, dropped, new_free, ran, changed, backup, current):
    cooling = cooldown_state(set(final), current)
    free = [m for m in final if tier_of(m) == 0]
    free_available = [m for m in free if m not in cooling]
    returns = sorted(v["until"] for m, v in cooling.items() if m in free)
    return {
        "at": datetime.datetime.fromtimestamp(current, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "order": [{"model": m, "tier": TIER_NAMES[tier_of(m)]} for m in final],
        "free_models": len(free),
        "free_available_now": len(free_available),
        "next_free_returns_at": returns[0] if (returns and not free_available) else None,
        "cooling": cooling,
        "changed": changed,
        "previous_order": cfg_before,
        "dropped": [{"model": m, "why": why} for m, why in dropped],
        "new_free_models_seen": new_free,
        "probes_run": ran,
        "backup": backup,
        "paid_before_free_violations": [list(v) for v in violations(final)],
        "funding_risk": "none" if len(free_available) >= 2 else ("high" if not free_available else "elevated"),
    }


def refresh(args):
    current = now()
    ROOT.mkdir(parents=True, exist_ok=True)
    cfg = read_config()
    try:
        ids = fetch_catalogue()
    except (RuntimeError, OSError, subprocess.TimeoutExpired) as error:
        atomic_write(ROOT / "report.json", json.dumps({"at": current, "error": str(error),
                     "note": "catalogue unavailable; model list left untouched"}, sort_keys=True) + "\n")
        print("economy: " + str(error), file=sys.stderr)
        return 1
    models, new_free, gone = update_catalogue(ids, current)
    pol = policy()
    free_candidates = [m for m in ids if tier_of(m) == 0 and m not in pol["exclude"]]
    probes, ran = run_probes(free_candidates, args.probe_limit, current)
    before, final, dropped = plan_order(cfg, ids, probes, pol, current)
    changed = before != final
    backup = None
    if changed and not args.no_apply:
        backup = apply_order(cfg, final, probes, dropped, current)
    report = build_report(final, before, dropped, new_free, ran, changed and not args.no_apply, backup, current)
    atomic_write(ROOT / "report.json", json.dumps(report, sort_keys=True, indent=1) + "\n")
    print(json.dumps({"changed": report["changed"], "free_available_now": report["free_available_now"],
                      "funding_risk": report["funding_risk"]}, sort_keys=True))
    return 0


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    refresh_p = sub.add_parser("refresh")
    refresh_p.add_argument("--probe-limit", type=int, default=3)
    refresh_p.add_argument("--no-apply", action="store_true")
    sub.add_parser("plan")
    sub.add_parser("check")
    sub.add_parser("report")
    args = parser.parse_args(argv)
    if args.command == "refresh":
        return refresh(args)
    if args.command == "check":
        bad = violations([entry_model(e) for e in read_config()["models"]])
        for first, second in bad:
            print("tier violation: %s (%s) is ahead of %s (%s)" % (
                first, TIER_NAMES[tier_of(first)], second, TIER_NAMES[tier_of(second)]))
        return 1 if bad else 0
    if args.command == "plan":
        cfg = read_config()
        ids = fetch_catalogue()
        before, final, dropped = plan_order(cfg, ids, load(ROOT / "probes.json", {}), policy(), now())
        print(json.dumps({"before": before, "after": final,
                          "dropped": [{"model": m, "why": w} for m, w in dropped]}, indent=1))
        return 0
    if args.command == "report":
        print(json.dumps(load(ROOT / "report.json", {}), indent=1, sort_keys=True))
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
