#!/usr/bin/env python3
"""Reproducible O1/O2 tests for framed PGF joins at the hard case (n,k)=(12,30).

Runs the existing checker logic from check_framed_strategy.py on:
1) an accepted frame-normalized join fragment;
2) a rejected O1 fragment where a meet loses disjunctive 0v1 knowledge;
3) a rejected O1 fragment instantiated at n=12, budget 30.

Also reports finite exhaustive results for tiny exact poset-minimax (sanity)
and global labelled-poset reachability collisions (illustrating that O2 is a
single-policy property, not global reachability). No claim is made that these
results extend to n=12 or prove nonexistence of an exact-height-30 PGF.
"""
from __future__ import annotations

import json
import sys
from functools import lru_cache
from itertools import permutations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_framed_strategy import check_certificate, InvalidCertificate

ID3 = [0, 1, 2]
SW01 = [1, 0, 2]
ID12 = list(range(12))

ACCEPTED_JOIN_N3 = {
    "n": 3,
    "budget": 3,
    "comment": "Accepted: frame normalization joins first-comparison histories into identical {0<1}.",
    "nodes": [
        {"compare": [0, 1], "lt": {"next": 1, "perm": ID3}, "gt": {"next": 1, "perm": SW01}},
        {"compare": [1, 2], "lt": {"next": 2, "perm": ID3}, "gt": {"next": 3, "perm": ID3}},
        {"leaf": True},
        {"compare": [0, 2], "lt": {"next": 4, "perm": ID3}, "gt": {"next": 5, "perm": ID3}},
        {"leaf": True},
        {"leaf": True},
    ],
}

O1_REJECT_N3 = {
    "n": 3,
    "budget": 3,
    "comment": "Rejected O1: join meets {0<1,...} with {1<0,...}, losing 0v1.",
    "nodes": [
        {"compare": [0, 1], "lt": {"next": 1, "perm": ID3}, "gt": {"next": 2, "perm": ID3}},
        {"compare": [1, 2], "lt": {"next": 3, "perm": ID3}, "gt": {"next": 4, "perm": ID3}},
        {"compare": [1, 2], "lt": {"next": 3, "perm": ID3}, "gt": {"next": 4, "perm": ID3}},
        {"leaf": True},
        {"compare": [0, 2], "lt": {"next": 5, "perm": ID3}, "gt": {"next": 6, "perm": ID3}},
        {"leaf": True},
        {"leaf": True},
    ],
}

O1_REJECT_N12 = {
    "n": 12,
    "budget": 30,
    "comment": (
        "Rejected O1 fragment at (n,k)=(12,30): opposite 0v1 facts joined; meet={2<3} "
        "cannot sort 0,1. Local mechanism only; not a global exact-height nonexistence proof."
    ),
    "nodes": [
        {"compare": [0, 1], "lt": {"next": 1, "perm": ID12}, "gt": {"next": 2, "perm": ID12}},
        {"compare": [2, 3], "lt": {"next": 3, "perm": ID12}, "gt": {"next": 4, "perm": ID12}},
        {"compare": [2, 3], "lt": {"next": 3, "perm": ID12}, "gt": {"next": 4, "perm": ID12}},
        {"leaf": True},
        {"leaf": True},
    ],
}


def is_total(pos, n):
    for i in range(n):
        for j in range(i + 1, n):
            if not (pos[i] & (1 << j) or pos[j] & (1 << i)):
                return False
    return True


def close(less, n):
    less = list(less)
    for k in range(n):
        b = 1 << k
        for a in range(n):
            if less[a] & b:
                less[a] |= less[k]
    return tuple(less)


def can_sort_poset_game(n, budget):
    @lru_cache(None)
    def solve(pos):
        if is_total(pos, n):
            return 0
        best = None
        for i in range(n):
            for j in range(i + 1, n):
                if pos[i] & (1 << j) or pos[j] & (1 << i):
                    continue
                def child(x, y):
                    t = list(pos)
                    t[x] |= 1 << y
                    return close(t, n)
                v = 1 + max(solve(child(i, j)), solve(child(j, i)))
                if best is None or v < best:
                    best = v
                if best == 1:
                    return 1
        return best if best is not None else 0
    return solve(tuple([0] * n))


def global_labelled_collisions(n, max_depth):
    from collections import deque
    root = tuple([0] * n)
    seen = {root}
    q = deque([(root, 0)])
    collisions = 0
    while q:
        pos, d = q.popleft()
        if is_total(pos, n) or d >= max_depth:
            continue
        for i in range(n):
            for j in range(i + 1, n):
                if pos[i] & (1 << j) or pos[j] & (1 << i):
                    continue
                for res in (True, False):
                    t = list(pos)
                    if res:
                        t[i] |= 1 << j
                    else:
                        t[j] |= 1 << i
                    c = close(t, n)
                    if c in seen:
                        collisions += 1
                    else:
                        seen.add(c)
                        q.append((c, d + 1))
    return collisions, len(seen)


def run_checker_case(name, cert, should_accept):
    try:
        depth = check_certificate(cert)
        ok = should_accept
        return ok, f"ACCEPT depth={depth} nodes={len(cert['nodes'])}"
    except InvalidCertificate as exc:
        ok = not should_accept
        return ok, f"REJECT {exc}"


def main():
    cases = [
        ("accepted_join_n3", ACCEPTED_JOIN_N3, True),
        ("o1_reject_n3", O1_REJECT_N3, False),
        ("o1_reject_n12_budget30", O1_REJECT_N12, False),
    ]
    all_ok = True
    for name, cert, should in cases:
        ok, msg = run_checker_case(name, cert, should)
        print(f"{name}: {msg} {'PASS' if ok else 'FAIL'}")
        all_ok &= ok

    print("\nFinite exact poset minimax sanity (tiny n only):")
    for n, s in [(3, 3), (4, 5)]:
        print(f"  n={n} S(n)={can_sort_poset_game(n, 99)}; height {s}={can_sort_poset_game(n, s)}; height {s-1}={can_sort_poset_game(n, s-1)}")
    print("\nGlobal labelled-poset reachability collisions (all feasible comparisons/outcomes):")
    for n in (2, 3, 4):
        coll, states = global_labelled_collisions(n, 99)
        print(f"  n={n} states={states} collision-events={coll} (O2 concerns a single deterministic policy tree, not global reachability)")
    print("\nALL PASS" if all_ok else "\nSOME FAIL")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
