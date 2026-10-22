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
STATE = Path("/home/lubko/.local/state/soringp1/agent-pool.json")
CURSORS = STATE.parent / "packet-cursors.json"
PACKETS = Path(__file__).resolve().parent.parent / "docs/research-packets.json"
ROSTER = [
    ("Dd1KMoCc1ghfSN3I0dq0fE-beast", "soring301-strategy-dag-20261021",
     "Seek an all-n polynomial framed optimal sorting strategy DAG certificate; independently test its completeness. Do not repeat finite data or formalize peripheral Lean. Post substantive findings on Antonina 301."),
    ("7Ql7xUk4Yn9io6Eb7hmKvf-ligament", "soring301-antichain-adversary-20261021",
     "Seek a uniform exact root-antichain sorting recurrence, structural normal form, or counterexample to a root exchange theorem. Distinguish all-n conclusions from finite examples. No peripheral Lean. Report to Antonina 301."),
    ("eJdn8EBCvUfWSmpcn8N8qO-reddened", "soring301-no-cert-invariant-20261020",
     "Investigate polynomially checkable root sorting NO certificates beyond leaf counting, including tree-shape and comparison admissibility. Distinguish class membership from finite n12. No peripheral Lean. Report to Antonina 301."),
    ("0KvemFXL8da1UGuKv4Aqsp-hippolyte", "soring301-qbf-interactive-20261021",
     "Seek root-specific alternation compression reducing the known unary PSPACE game to NP or P. Give a formal uniformity bridge; avoid generic hardness and peripheral Lean. Report to Antonina 301."),
    ("VVIiJ6xfC0mW2B8OQLKtWS-channels", "soring301-dual-potential-20261021",
     "Find efficiently verifiable all-n comparison-tree shape lower-bound potentials. Avoid redoing finite n12 leaf count or peripheral Lean. Report to Antonina 301."),
    ("yJYQ3Mb8YfuJWm4rVCUUfI-enemy", "soring301-adjacency-referee-20261020",
     "Independently challenge leading proposed all-n root sorting certificate theorems and seek stronger structural lemmas. Validate logical and frame semantics. No routine Lean. Report to Antonina 301."),
    ("T505bkfsHmYO7nFokDXCkP-scored", "soring301-two-value-increment-20261021",
     "Find an all-n reduction from insertion or partial-order structure to uniform exact root S(n) computation. Test a precise theorem against counterexamples. Avoid isolated finite census and peripheral Lean. Report to Antonina 301."),
    ("kC3bgR9UBfwO95MrxYc2yd-otherwise", "soring301-selfreducibility-20261021",
     "Seek uniform self-reducibility or search-to-decision equivalence for unary S(n), with correct input and witness lengths. Distinguish P/poly from uniform membership. No peripheral Lean. Report to Antonina 301."),
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
    if plan.get("version") != 1 or not isinstance(plan.get("common"), str):
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
    current = entries[seq % len(entries)]
    return (f"Research packet {seq + 1}, track position {seq % len(entries) + 1}/{len(entries)}. "
            "This is NOT the same task as your preceding invocation. "
            "Do not repeat an already posted negative result.\n\n" + current +
            "\n\n" + plan["common"])


def tick(history, cursors, plan):
    live = running()
    if len(live) >= TARGET_RUNNING:
        print(f"{time.strftime('%FT%T')} running={len(live)} minimum met", flush=True)
        return
    print(f"{time.strftime('%FT%T')} running={len(live)} replenishing", flush=True)
    choices = sorted((r for r in ROSTER if r[0] not in live),
                     key=lambda r: history.get(r[0], 0))
    for agent_id, wd, prompt in choices:
        if len(live) >= TARGET_RUNNING:
            break
        path = "/home/lubko/" + wd
        if not os.path.isdir(path):
            print("missing worktree", path, flush=True)
            continue
        try:
            next_prompt = select_packet(agent_id, prompt, cursors, plan)
            p = execute([A, "agent", "run", "--id", agent_id, "--cwd", path,
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
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(history))
    pending = CURSORS.with_suffix(".tmp")
    pending.write_text(json.dumps(cursors, sort_keys=True))
    pending.replace(CURSORS)

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
