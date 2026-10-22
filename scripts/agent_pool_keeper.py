#!/usr/bin/env python3
"""Keep a minimum of five *running* SoringP1 research agents on billy-dev.

Reuses existing agent IDs and worktrees, respects a no-maximum rule, and
never treats idle agents or unrelated Viche agents as research capacity.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import time

A = "/home/lubko/.local/bin/antonina"
REQUIRED_RUNNING = 5
TARGET_RUNNING = 8  # Buffer above the hard minimum for normal completions.
INTERVAL = 10
MIN_RESEARCH_RESTART_SECONDS = 240  # Avoid fast repeats of completed investigations.
STALLED_OUTPUT_SECONDS = 30 * 60  # A silent managed agent is not productive capacity.
PREFERRED_MODEL_QUIET_SECONDS = 5 * 60  # Resume preferred model after genuine quota reset.
MAX_STALLED_STEERS_PER_TICK = 1  # Recover gradually without losing the agent floor.
AGENTS_DIR = Path("/home/lubko/.local/state/antonina/agents")
MODELS_CONFIG = Path("/home/lubko/.config/antonina/config.json")
STATE = Path("/home/lubko/.local/state/soringp1/agent-pool.json")
CURSORS = STATE.parent / "packet-cursors.json"
PACKETS = Path(__file__).resolve().parent.parent / "docs/research-packets.json"
ROSTER = [
    ('sYIEgoMgv7GpA2M8IF6N55-race', 'soring301-new-optimal-policy-fj-20261022', 'Constructive YES certificate frontier; Ford-Johnson state quot'),
    ('uocSY7i9UxaE71ujhhxl5t-strict', 'soring301-new-global-slack-20261022', 'Global vs local minimax quotient DAG theorem'),
    ('kK0hfvyCDUbSg5chSWjR9H-friant', 'soring301-new-root-no-cert-20261022', 'Root-specific polynomial coNO certificate proof system'),
    ('z8FIxKzTS8NklpFKEez6hS-equality', 'soring301-new-avgdepth-obstruction-20261022', 'External-path/average-depth obstruction to exact sorting'),
    ('naVVa2aiGjj9EeQlYbAOTs-removing', 'soring301-new-surplus-parameter-20261022', 'Parameterised exact root threshold by information surplus'),
    ('so7oeYESYOuat2aZ6bP0CY-hideous', 'soring301-new-alternation-witness-20261022', 'NP strategy witnesses and uniform verifier completeness'),
    ('HS5LZJ7PvDr441nyS0bkje-dearest', 'soring301-new-partial-info-20261022', 'Exact consequences of 2025 partial-information sorting'),
    ('grhT1CGQzErpmZ1DOIhoZY-mined', 'soring301-new-independent-referee-20261022', 'Mathematical referee and literature counterexample audit'),
]

def execute(args, timeout=20):
    return subprocess.run(args, capture_output=True, text=True, timeout=timeout)

def running():
    result = execute([A, "agent", "list", "--running", "--page", "1", "--limit", "100", "--json"])
    if result.returncode:
        raise RuntimeError(result.stderr.strip())
    agents = json.loads(result.stdout)["agents"]
    return {v["id"] for v in agents if v.get("state") == "running"
            and (v.get("title", "").startswith("SoringP1")
                 or v.get("cwd", "").startswith("/home/lubko/soring301"))}

def load_packet_plan():
    """Source-controlled research packets can be changed without modifying the keeper."""
    plan = json.loads(PACKETS.read_text())
    if plan.get("version") != 2 or not isinstance(plan.get("common"), str):
        raise ValueError("invalid research packet plan")
    if not isinstance(plan.get("agents"), dict):
        raise ValueError("missing per-agent research packets")
    for agent_id, _, _ in ROSTER:
        entries = plan["agents"].get(agent_id)
        if (not isinstance(entries, list) or len(entries) < 2 or
                any(not isinstance(q, str) or len(q.strip()) < 60 for q in entries) or
                len(set(entries)) != len(entries)):
            raise ValueError(f"missing or duplicate research packets for {agent_id}")
    return plan


def select_packet(agent_id, fallback, cursors, plan):
    entries = plan["agents"].get(agent_id, [fallback])
    seq = int(cursors.get(agent_id, 0))
    if seq < len(entries):
        current = entries[seq]
    else:
        # Do not loop over already exhausted research packets indefinitely.
        # Under the binding five-agent floor, instead task this role with
        # developing a FRESH explicit conjecture after reading its history.
        current = ("All curated packets for your track have been tried. "
                   "Do not repeat any prior result or re-audit the same theorem. "
                   "Find a distinct falsifiable all-n question by comparing "
                   "original literature with specific open failures in #301; "
                   "then investigate it. If no new information is established, "
                   "end WITHOUT a board comment and report that your track "
                   "requires new operator curation.")
    return (f"Research packet {seq + 1}. New clean role; avoid repeating past work. "
            "Make a substantive effort to prove or DISPROVE the given all-n conjecture "
            "before ending.\n\n" + current + "\n\n" + plan["common"])


def agent_declares_cwd(agent_id, expected_cwd):
    """Reuse a managed agent only in the directory it was created for.

    Antonina deliberately rejects --cwd when an existing front owns work.
    Read the durable declaration instead, and omit --cwd on resume/relaunch.
    """
    try:
        data = json.loads((AGENTS_DIR / agent_id / "meta.json").read_text())
        return data.get("id") == agent_id and data.get("cwd") == expected_cwd
    except (OSError, ValueError, TypeError):
        return False


def last_observed_output(agent_id, expected_cwd):
    """Return recent output/start timestamp, not a mere running flag.

    Last_activity_at can remain at invocation start while a model streams
    substantive output; consult the managed log modification time as well.
    Never steer a record whose declared worktree changed underneath us.
    """
    base = AGENTS_DIR / agent_id
    try:
        meta = json.loads((base / "meta.json").read_text())
        if meta.get("state") != "running" or meta.get("cwd") != expected_cwd:
            return None
        observed = float(meta.get("started_at") or 0)
        log = base / "output.log"
        if log.exists():
            observed = max(observed, log.stat().st_mtime)
        return observed if observed > 0 else None
    except (OSError, ValueError, TypeError):
        return None


def save_history(history, cursors):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(history))
    pending = CURSORS.with_suffix(".tmp")
    pending.write_text(json.dumps(cursors, sort_keys=True))
    pending.replace(CURSORS)


def restored_preferred_model(agent_id, expected_cwd, now):
    """The first configured model is eligible again after its prior cooldown.

    Read only the local operator-configured model order. No model discovery,
    provider probe or broad process kill. Never preempt fresh model output.
    """
    try:
        meta = json.loads((AGENTS_DIR / agent_id / "meta.json").read_text())
        config = json.loads(MODELS_CONFIG.read_text())
        choices = config.get("models")
        if not isinstance(choices, list) or not choices:
            return False
        preferred = choices[0].get("model")
        if not isinstance(preferred, str) or not preferred:
            return False
        if meta.get("state") != "running" or meta.get("cwd") != expected_cwd:
            return False
        failover = meta.get("model_failover") or {}
        if failover.get("selected_model") in (None, preferred):
            return False
        cooldowns = failover.get("cooldowns") or []
        # Only undo a *recorded* exclusion when it has expired.
        matching = [c for c in cooldowns if c.get("model") == preferred]
        return bool(matching and all(float(c["until"]) <= now for c in matching))
    except (OSError, ValueError, TypeError, KeyError, AttributeError):
        return False


def recover_stalled(live, history, cursors, plan, now):
    """Steer in place without temporarily lowering the agent count.

    A running OpenCode child can wait indefinitely after provider rate limits.
    On Billy, steering with --cwd while a front exists is refused, so steer
    reuses the already-validated declared directory.
    """
    count = 0
    for agent_id, wd, fallback in ROSTER:
        if agent_id not in live or count >= MAX_STALLED_STEERS_PER_TICK:
            continue
        last = last_observed_output(agent_id, "/home/lubko/" + wd)
        if last is None:
            continue
        quiet_for = now - max(last, history.get(agent_id, 0))
        returning_primary = (
            quiet_for >= PREFERRED_MODEL_QUIET_SECONDS and
            restored_preferred_model(agent_id, "/home/lubko/" + wd, now)
        )
        if not returning_primary and quiet_for < STALLED_OUTPUT_SECONDS:
            continue
        prompt = select_packet(agent_id, fallback, cursors, plan)
        try:
            p = execute([A, "agent", "run", "--id", agent_id,
                         "--prompt", prompt, "--steer", "--detach", "--json"],
                        timeout=35)
            if p.returncode == 0 and json.loads(p.stdout).get("state") == "running":
                history[agent_id] = now
                cursors[agent_id] = int(cursors.get(agent_id, 0)) + 1
                count += 1
                print("steered", "returned-primary" if returning_primary else "stalled",
                      agent_id, "packet", cursors[agent_id], flush=True)
            else:
                print("stall recovery failed", agent_id, p.stderr[-250:], flush=True)
        except Exception as e:
            print("stall recovery error", agent_id, str(e), flush=True)
    return count


def tick(history, cursors, plan):
    live = running()
    recovered = recover_stalled(live, history, cursors, plan, time.time())
    if len(live) >= TARGET_RUNNING:
        if recovered:
            save_history(history, cursors)
        print(f"{time.strftime('%FT%T')} running={len(live)} minimum met; recovered={recovered}", flush=True)
        return
    print(f"{time.strftime('%FT%T')} running={len(live)} replenishing", flush=True)
    choices = sorted((r for r in ROSTER if r[0] not in live),
                     key=lambda r: history.get(r[0], 0))
    for agent_id, wd, prompt in choices:
        if len(live) >= TARGET_RUNNING:
            break
        # The >=5 directive is hard; refill it immediately. Above the floor,
        # allow an agent time to finish a substantive investigation before
        # reopening its session. Rapid 10-second replays flooded board #301.
        if (len(live) >= REQUIRED_RUNNING and
                time.time() - history.get(agent_id, 0) < MIN_RESEARCH_RESTART_SECONDS):
            continue
        path = "/home/lubko/" + wd
        if not os.path.isdir(path):
            print("missing worktree", path, flush=True)
            continue
        if not agent_declares_cwd(agent_id, path):
            print("refusing agent with missing or unexpected declared worktree", agent_id, flush=True)
            continue
        try:
            next_prompt = select_packet(agent_id, prompt, cursors, plan)
            # Existing agents retain an owned front even in state "failed".
            # --cwd is rejected in that case; their declared path was checked.
            p = execute([A, "agent", "run", "--id", agent_id,
                         "--prompt", next_prompt, "--detach", "--json"], timeout=35)
            if p.returncode == 0 and json.loads(p.stdout).get("state") == "running":
                live.add(agent_id)
                history[agent_id] = time.time()
                cursors[agent_id] = int(cursors.get(agent_id, 0)) + 1
                print("started", agent_id, "packet", cursors[agent_id], flush=True)
            else:
                print("failed", agent_id, p.stderr[-250:], flush=True)
        except Exception as e:
            print("error", agent_id, str(e), flush=True)
    save_history(history, cursors)

def main():
    import fcntl
    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true")
    args = parser.parse_args()
    STATE.parent.mkdir(parents=True, exist_ok=True)
    lock = open(STATE.parent / "agent-pool.lock", "w")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        print("another pool keeper is already running", flush=True)
        return 0
    if os.uname().nodename != "billy-dev":
        raise RuntimeError("refusing to manage research outside billy-dev")
    try:
        history = json.loads(STATE.read_text())
    except (FileNotFoundError, ValueError):
        history = {}
    try:
        cursors = json.loads(CURSORS.read_text())
    except (FileNotFoundError, ValueError):
        cursors = {}
    while True:
        try:
            tick(history, cursors, load_packet_plan())
        except Exception as e:
            print("tick error", repr(e), flush=True)
        if args.once:
            break
        time.sleep(INTERVAL)
    return 0

if __name__ == "__main__":
    sys.exit(main())
