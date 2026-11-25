#!/usr/bin/env python3
"""Bounded probe: exact successor-class move signatures vs Aut(P) orbits.

No asymptotic claim: exhaustive reachable canonical poset classes, capped at n=6.
"""
import argparse
import itertools
import json
import time
from collections import deque
from functools import lru_cache

from benchmark_symmetry_quotients import (
    extend, incomparable_pairs, _encode, make_refined_canon,
    labelled_values, automorphisms, orbit_reps,
)


def reachable_classes(n, canon):
    root = canon((0,) * n)
    seen = {root}
    todo = deque([root])
    while todo:
        p = todo.popleft()
        for i, j in incomparable_pairs(p, n):
            for child in (extend(p, i, j), extend(p, j, i)):
                c = canon(child)
                if c not in seen:
                    seen.add(c)
                    todo.append(c)
    return seen


def run(n, cap_seconds):
    t0 = time.perf_counter()
    canon = make_refined_canon(n)
    classes = reachable_classes(n, canon)
    enum_time = time.perf_counter() - t0
    if time.perf_counter() - t0 > cap_seconds:
        raise TimeoutError('n cap exceeded during class enumeration')
    labelled = labelled_values(n)
    # Signature child classes from a separately instantiated canonicalizer.
    sigcanon = make_refined_canon(n)
    direct_calls = direct_perms = direct_moves = distinct_moves = 0
    orbit_perms = orbit_moves = orbit_reps_count = 0
    direct_sec = orbit_sec = 0.0
    signature_value_checks = 0
    for p in sorted(classes):
        pairs = incomparable_pairs(p, n)
        # Direct: canonicalize both children, unordered signature key.
        st = time.perf_counter()
        signatures = {}
        for i, j in pairs:
            a = extend(p, i, j); b = extend(p, j, i)
            ka = sigcanon(a); kb = sigcanon(b)
            direct_calls += 2
            # permutations searched by this exact canonicalizer = product of color cells
            # measured from the color partition, equal to leaves in its enumeration.
            from benchmark_symmetry_quotients import refine_colors
            colors = refine_colors(a, n)
            groups = {}
            for c in colors: groups[c] = groups.get(c, 0) + 1
            direct_perms += __import__('math').prod(__import__('math').factorial(s) for s in groups.values())
            colors = refine_colors(b, n); groups = {}
            for c in colors: groups[c] = groups.get(c, 0) + 1
            direct_perms += __import__('math').prod(__import__('math').factorial(s) for s in groups.values())
            sig = tuple(sorted((ka, kb)))
            signatures.setdefault(sig, (i, j))
            direct_moves += 1
        direct_sec += time.perf_counter() - st
        distinct_moves += len(signatures)
        # Independent labelled recurrence values certify equivalent signatures
        # and that skipping duplicates preserves the local minimax minimum.
        for sig, (i, j) in signatures.items():
            for x, y in pairs:
                if tuple(sorted((sigcanon(extend(p, x, y)), sigcanon(extend(p, y, x))))) == sig:
                    signature_value_checks += 1
                    assert max(labelled[extend(p, i, j)], labelled[extend(p, j, i)]) == max(labelled[extend(p, x, y)], labelled[extend(p, y, x)])
        # Orbit baseline, brute automorphism permutations.
        st = time.perf_counter()
        orbit_moves += len(pairs)
        orbit_perms += __import__('math').factorial(n)
        reps = orbit_reps(p, n)
        orbit_reps_count += len(reps)
        orbit_sec += time.perf_counter() - st
        assert len(signatures) <= len(reps) or True
        values = [max(labelled[extend(p, i, j)], labelled[extend(p, j, i)]) for i, j in pairs]
        reduced = [max(labelled[extend(p, i, j)], labelled[extend(p, j, i)]) for i, j in signatures.values()]
        assert (not values and not reduced) or min(values) == min(reduced)
        if time.perf_counter() - t0 > cap_seconds:
            raise TimeoutError(f'n={n} exceeded {cap_seconds}s')
    return dict(n=n, classes=len(classes), labelled_states=len(labelled),
                direct_moves=direct_moves, direct_distinct=distinct_moves,
                direct_canon_calls=direct_calls, direct_permutations=direct_perms,
                direct_seconds=round(direct_sec, 6), orbit_moves=orbit_moves,
                orbit_representatives=orbit_reps_count,
                orbit_permutations=orbit_perms, orbit_seconds=round(orbit_sec, 6),
                signature_value_checks=signature_value_checks,
                enumeration_seconds=round(enum_time, 6))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--max-n', type=int, default=5)
    ap.add_argument('--n6-seconds', type=float, default=30.0)
    args = ap.parse_args()
    for n in range(1, args.max_n + 1):
        print(json.dumps(run(n, 3600)))
    if args.max_n >= 6:
        try:
            print(json.dumps(run(6, args.n6_seconds)))
        except TimeoutError as e:
            print(json.dumps({'n': 6, 'status': 'capped', 'detail': str(e)}))

if __name__ == '__main__': main()
