#!/usr/bin/env python3
"""Independent re-verification of a reported WL counterexample.

Uses ONLY the original labelled recurrence from scripts/oracle.py
(frozenset relations, Floyd-Warshall closure, memo by (n, sorted rel)).
No canonical form, no bitmasks, no code shared with oracle_n8.py.

Input: n and a JSON list of ordered pairs, e.g.
  python3 scripts/verify_counterexample.py 9 '[[0,3],[1,4],...]'
"""
import sys, json
sys.path.insert(0, 'scripts')
import oracle as OLD

def main():
    n = int(sys.argv[1])
    rel = frozenset(tuple(p) for p in json.loads(sys.argv[2]))
    # sanity: relation set must be transitively closed and antisymmetric
    assert all(a != b for a, b in rel)
    cl = OLD.closure(rel, n)
    assert set(cl) == set(rel), 'not transitively closed'
    m = OLD.m_depth(n, rel)
    best = None  # f(P) = MAX over incomparable pairs of min(child depths)
    for (a, b) in OLD.incomparable_pairs(rel, n):
        r1 = OLD.closure(set(rel) | {(a, b)}, n)
        r2 = OLD.closure(set(rel) | {(b, a)}, n)
        d1, d2 = OLD.m_depth(n, r1), OLD.m_depth(n, r2)
        mn = min(d1, d2)
        if best is None or mn > best[0]:
            best = (mn, (a, b), d1, d2, 1 + max(d1, d2) == m)
    ok = (m >= 2 and best[0] < m - 2)
    print(json.dumps({'n': n, 'm': m, 'f': best[0], 'threshold': m - 2,
                      'best_pair': best[1], 'child_depths': [best[2], best[3]],
                      'optimal': best[4], 'is_counterexample': ok}))
    return 0 if ok else 1

if __name__ == '__main__':
    sys.exit(main())
