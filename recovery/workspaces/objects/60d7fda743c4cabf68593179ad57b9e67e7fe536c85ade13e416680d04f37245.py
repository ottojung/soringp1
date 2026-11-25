#!/usr/bin/env python3
"""Probes for the linear-extension-count-obstruction front.

Model: docs/problem.md / scripts/state_compression.py.
  State = strictly transitively closed poset, successor bitmasks.
  F(P) = 0 if total, else 1 + min_{x,y incomp} max(F(P+x<y), F(P+y<x)).
  e(P) = number of linear extensions (memoized via e(P)=e(P+x<y)+e(P+y<x)).

Probe 1: BFS from the n-antichain; assert min-depth(P) = |cov(P)| for all
reachable states, n <= 6.
Probe 2: over all posets on <= 6 labelled elements: for each F-value, the
max spread of e among states sharing it; pairs with equal e but different F.
Probe 3: sensitivity: for all P and incomparable (x,y): drop of F when the
best relation is NOT taken, i.e. max over relations of F(P) - F(child);
also d = F(P) - max(F(P+x<y), F(P+y<x)) for forced (x,y).
Probe 4: height-2 locus: count states with height <= 2 and the (F, e)
relation there (the #P-complete description class for e).
"""
import sys, time
from collections import deque

def extend(succ, i, j, n):
    out = list(succ)
    new_greater = succ[j] | (1 << j)
    for x in range(n):
        if x == i or (succ[x] & (1 << i)):
            out[x] |= new_greater
    return tuple(out)

def incomparable(succ, n):
    return [(i, j) for i in range(n) for j in range(i+1, n)
            if not (succ[i] & (1 << j)) and not (succ[j] & (1 << i))]

def covers(succ, n):
    """Cover pairs of the poset."""
    cov = []
    for i in range(n):
        for j in range(n):
            if succ[i] & (1 << j):
                # j covers i iff no intermediate k: i < k < j
                if not any((succ[i] & (1 << k)) and (succ[k] & (1 << j)) for k in range(n)):
                    cov.append((i, j))
    return cov

def solve_all(n):
    """Minimax F and count e for every labelled poset on n elements.
    Returns (F: dict, e: dict, parents accessible via memo)."""
    F = {}
    E = {}
    def solveF(succ):
        v = F.get(succ)
        if v is not None:
            return v
        pairs = incomparable(succ, n)
        if not pairs:
            F[succ] = 0
        else:
            best = None
            for i, j in pairs:
                c1 = solveF(extend(succ, i, j, n))
                c2 = solveF(extend(succ, j, i, n))
                m = c1 if c1 > c2 else c2
                if best is None or m < best:
                    best = m
            F[succ] = 1 + best
        return F[succ]
    def solveE(succ):
        v = E.get(succ)
        if v is not None:
            return v
        pairs = incomparable(succ, n)
        if not pairs:
            E[succ] = 1
        else:
            i, j = pairs[0]
            E[succ] = solveE(extend(succ, i, j, n)) + solveE(extend(succ, j, i, n))
        return E[succ]
    root = (0,) * n
    solveF(root)
    for s in list(F.keys()):
        solveE(s)
    return F, E

def bfs_depths(n):
    """min number of comparisons from antichain to each state."""
    root = (0,) * n
    depth = {root: 0}
    q = deque([root])
    bad = []
    while q:
        s = q.popleft()
        d = depth[s]
        for i, j in incomparable(s, n):
            for c in (extend(s, i, j, n), extend(s, j, i, n)):
                if c not in depth:
                    depth[c] = d + 1
                    q.append(c)
    for s, d in depth.items():
        if d != len(covers(s, n)):
            bad.append((s, d, len(covers(s, n))))
    return len(depth), bad

def main():
    for n in (2, 3, 4, 5, 6):
        t0 = time.perf_counter()
        cnt, bad = bfs_depths(n)
        print(f"n={n}: reachable labelled states={cnt}, "
              f"min-depth != |cov| violations: {len(bad)} "
              f"({time.perf_counter()-t0:.1f}s)")
        if bad[:3]:
            print("  examples:", bad[:3])
    # F/e stats over n<=6. Build the union state space across n. Note a state
    # of size n relates to elements 0..n-1 only; compute per n separately.
    for n in (5, 6):
        t0 = time.perf_counter()
        F, E = solve_all(n)
        # group by F value: spread of e
        per_F = {}
        per_e = {}
        for s, f in F.items():
            per_F.setdefault(f, set()).add(E[s])
            per_e.setdefault(E[s], set()).add(f)
        max_spread = max(max(v) - min(v) for v in per_F.values())
        max_mult_f = 0
        for f, es in per_F.items():
            pass
        # multiplicities: count states per (f, e)
        mult_fe = {}
        for s, f in F.items():
            mult_fe.setdefault((f, E[s]), 0)
            mult_fe[(f, E[s])] += 1
        # max number of distinct e sharing one F, and distinct F sharing one e
        spread_per_F = {f: (min(es), max(es), len(es)) for f, es in per_F.items()}
        fs_per_e = {e: len(fs) for e, fs in per_e.items()}
        max_fs_per_e = max(fs_per_e.values())
        # sensitivity probe: for every state and every move, how much can F
        # drop if the adversary forces that move? d = F(P) - max(children)
        max_forced_drop = 0
        n_forced_ge2 = 0
        for s, f in F.items():
            if f == 0:
                continue
            for i, j in incomparable(s, n):
                c1 = F[extend(s, i, j, n)]
                c2 = F[extend(s, j, i, n)]
                m = c1 if c1 > c2 else c2
                d = f - m
                if d > max_forced_drop:
                    max_forced_drop = d
                if d >= 2:
                    n_forced_ge2 += 1
        # height-2 states (longest chain <= 2): all relations are covers,
        # F and e stats there
        h2 = [(s, f, E[s]) for s, f in F.items()
              if all(not ((s[i] & (1 << k)) and (s[k] & (1 << j)))
                     for i in range(n) for j in range(n) if s[i] & (1 << j)
                     for k in range(n))]
        h2_Fspread = {}
        for s, f, e in h2:
            h2_Fspread.setdefault(f, set()).add(e)
        h2_spread = max((max(es) - min(es) for es in h2_Fspread.values()), default=0)
        print(f"n={n}: F in [{min(F.values())},{max(F.values())}], "
              f"distinct F={len(per_F)}")
        print(f"   max spread of e over one F-value: {max_spread}")
        print(f"   max #distinct-F for a single e: {max_fs_per_e}")
        print(f"   max forced-drop F(P)-max(children): {max_forced_drop} "
              f"(#moves with drop>=2: {n_forced_ge2})")
        print(f"   height<=2 states: {len(h2)}, max e-spread within one F "
              f"among height-2 states: {h2_spread}")
        # sandwich check: F vs log2 e
        import math
        worst_hi = 0.0
        worst_lo = 1.0
        for s, f in F.items():
            e = E[s]
            if e <= 1:
                continue
            r = f / math.log2(e)
            worst_hi = max(worst_hi, r)
            worst_lo = min(worst_lo, r)
        print(f"   F/log2(e) range over states: [{worst_lo:.3f}, {worst_hi:.3f}]")
        print(f"   ({time.perf_counter()-t0:.1f}s)")

if __name__ == "__main__":
    main()
