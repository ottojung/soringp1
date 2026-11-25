#!/usr/bin/env python3
"""Replay/check oracle-aided refuter (adversary) or sorter traces for G(n,k).

Trace format (JSON):
{
  "kind": "refuter"|"sorter",
  "n": int, "k": int,
  "root": node_id,
  "nodes": {
    id: {
      "state": [succ_bitmask_int, ...],   # transitive closure successor bitmasks
      "budget": int,                       # refuter: remaining comparisons; sorter: same
      "type": "internal"|"leaf"|"oracle",
      # internal refuter: "rule": { "i,j": {"answer":"lt"|"gt", "next":id}, ... } covers ALL Inc(state)
      # internal sorter: "compare":[i,j], "lt":{"next":id}, "gt":{"next":id}
      # leaf refuter: adversary wins here -> state non-total and budget==0 (or explicit)
      # leaf sorter: state total
      # oracle: "oracle": {"name":str, "constraints":[...], "params":{...}}
    }
  }
}
Constraints checked mechanically (no raw search output trusted):
- {"type":"root_antichain"}
- {"type":"budget_eq","value":int}
- {"type":"state_tc"}  # verifies transitive closure/antisymmetry
- {"type":"non_total"}
- {"type":"total"}
- {"type":"budget_zero"}
- {"type":"tc_edge","move":[i,j],"answer":"lt|gt","child":id}
- {"type":"covers_all_incomparable"} (refuter internal)
- {"type":"budget_decrements","child":id}
- {"type":"exhaustive_can_sort","value":bool,"node_cap":int}  # runs budgeted_dfs.can_sort
- {"type":"exhaustive_cannot_sort","value":bool,"node_cap":int}
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from budgeted_dfs import can_sort, extend, incomparable_pairs, is_total as is_total_succ


def to_succ(state):
    return tuple(int(x) for x in state)


def tc_ok(succ, n):
    # antisymmetry and transitivity
    for i in range(n):
        if succ[i] >> i & 1:
            return False, f"self-loop at {i}"
        for j in range(n):
            if succ[i] >> j & 1:
                if succ[j] >> i & 1:
                    return False, f"cycle {i},{j}"
                for k in range(n):
                    if (succ[j] >> k & 1) and not (succ[i] >> k & 1):
                        return False, f"not transitive {i}->{j}->{k}"
    return True, "ok"


def is_total(state, n):
    s = to_succ(state)
    for i in range(n):
        for j in range(i + 1, n):
            if not (s[i] >> j & 1) and not (s[j] >> i & 1):
                return False
    return True


def check_constraints(doc, nid, node):
    n, k = doc["n"], doc["k"]
    oracle = node.get("oracle", {})
    constraints = oracle.get("constraints", [])
    state = node["state"]
    succ = to_succ(state)
    budget = int(node["budget"])
    nodes = doc["nodes"]
    for c in constraints:
        t = c["type"]
        if t == "root_antichain":
            if nid != doc["root"] or any(x != 0 for x in succ):
                return False, f"{nid}: root_antichain"
        elif t == "budget_eq":
            if budget != c["value"]:
                return False, f"{nid}: budget_eq {budget}!={c['value']}"
        elif t == "state_tc":
            ok, msg = tc_ok(succ, n)
            if not ok:
                return False, f"{nid}: state_tc {msg}"
        elif t == "non_total":
            if is_total(state, n):
                return False, f"{nid}: expected non_total"
        elif t == "total":
            if not is_total(state, n):
                return False, f"{nid}: expected total"
        elif t == "budget_zero":
            if budget != 0:
                return False, f"{nid}: expected budget_zero"
        elif t == "tc_edge":
            i, j = c["move"]
            ans = c["answer"]
            child = nodes[c["child"]]
            s2 = extend(succ, i, j) if ans == "lt" else extend(succ, j, i)
            if to_succ(child["state"]) != s2:
                return False, f"{nid}: tc_edge mismatch to {c['child']}"
            if int(child["budget"]) != budget - 1:
                return False, f"{nid}: child budget mismatch"
        elif t == "covers_all_incomparable":
            rule = node.get("rule", {})
            inc = {(min(i, j), max(i, j)) for i, j in incomparable_pairs(succ, n)}
            keys = set()
            for key in rule:
                a, b = (int(x) for x in key.split(","))
                keys.add((min(a, b), max(a, b)))
            if keys != inc:
                return False, f"{nid}: covers_all_incomparable missing={inc-keys} extra={keys-inc}"
        elif t == "budget_decrements":
            child = nodes[c["child"]]
            if int(child["budget"]) != budget - 1:
                return False, f"{nid}: budget_decrements"
        elif t == "exhaustive_can_sort":
            res, cap = can_sort(succ, n, budget, [0], c.get("node_cap"))
            if cap:
                return False, f"{nid}: exhaustive_can_sort hit node_cap"
            if res != c["value"]:
                return False, f"{nid}: exhaustive_can_sort got {res} expected {c['value']}"
        elif t == "exhaustive_cannot_sort":
            res, cap = can_sort(succ, n, budget, [0], c.get("node_cap"))
            if cap:
                return False, f"{nid}: exhaustive_cannot_sort hit node_cap"
            if res != c["value"]:
                return False, f"{nid}: exhaustive_cannot_sort got {res} expected {c['value']}"
        else:
            return False, f"{nid}: unknown constraint {t}"
    return True, "ok"


def check_refuter(doc):
    nodes = doc["nodes"]
    for nid, node in nodes.items():
        n = doc["n"]
        state = node["state"]
        succ = to_succ(state)
        budget = int(node["budget"])
        typ = node["type"]
        ok, msg = tc_ok(succ, n)
        if not ok:
            return False, f"{nid}: {msg}"
        if typ == "oracle":
            ok, msg = check_constraints(doc, nid, node)
            if not ok:
                return False, msg
            continue
        if typ == "leaf":
            if is_total(state, n):
                return False, f"{nid}: refuter leaf must be non-total (or be explicit win)"
            if budget != 0:
                return False, f"{nid}: refuter non-total leaf needs budget 0"
            continue
        if typ == "internal":
            rule = node["rule"]
            inc = list(incomparable_pairs(succ, n))
            if not inc:
                return False, f"{nid}: internal but total"
            seen = set()
            for i, j in inc:
                key = f"{i},{j}"
                if key not in rule:
                    return False, f"{nid}: missing move {key}"
                seen.add(key)
                entry = rule[key]
                ans = entry["answer"]
                child = nodes[entry["next"]]
                s2 = extend(succ, i, j) if ans == "lt" else extend(succ, j, i)
                if to_succ(child["state"]) != s2:
                    return False, f"{nid}: bad tc for {key}->{entry['next']}"
                if int(child["budget"]) != budget - 1:
                    return False, f"{nid}: bad budget for child {entry['next']}"
            for key in rule:
                if key not in seen:
                    return False, f"{nid}: rule has comparable/non-canonical move {key}"
            continue
        return False, f"{nid}: unknown type {typ}"
    return True, f"ACCEPT refuter n={doc['n']} k={doc['k']} nodes={len(nodes)}"


def check_sorter(doc):
    # minimal: root state, internal has compare+lt+gt with tc edges and budget-1, leaves total
    nodes = doc["nodes"]
    n = doc["n"]
    for nid, node in nodes.items():
        succ = to_succ(node["state"])
        budget = int(node["budget"])
        typ = node["type"]
        ok, msg = tc_ok(succ, n)
        if not ok:
            return False, f"{nid}: {msg}"
        if typ == "oracle":
            ok, msg = check_constraints(doc, nid, node)
            if not ok:
                return False, msg
            continue
        if typ == "leaf":
            if not is_total(node["state"], n):
                return False, f"{nid}: sorter leaf must be total"
            continue
        if typ == "internal":
            i, j = node["compare"]
            if (succ[i] >> j & 1) or (succ[j] >> i & 1):
                return False, f"{nid}: comparing comparable pair"
            for ans in ("lt", "gt"):
                child = nodes[node[ans]["next"]]
                s2 = extend(succ, i, j) if ans == "lt" else extend(succ, j, i)
                if to_succ(child["state"]) != s2:
                    return False, f"{nid}: bad {ans} child"
                if int(child["budget"]) != budget - 1:
                    return False, f"{nid}: bad child budget"
            continue
        return False, f"{nid}: unknown type {typ}"
    return True, f"ACCEPT sorter n={doc['n']} k={doc['k']} nodes={len(nodes)}"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("file")
    args = ap.parse_args()
    doc = json.loads(Path(args.file).read_text())
    if doc["kind"] == "refuter":
        ok, msg = check_refuter(doc)
    elif doc["kind"] == "sorter":
        ok, msg = check_sorter(doc)
    else:
        ok, msg = False, f"unknown kind {doc.get('kind')}"
    print(("ACCEPT: " if ok else "REJECT: ") + msg)
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
