#!/usr/bin/env python3
"""State-space compression experiments for the exact sorting number S(n).

Model (see docs/problem.md, docs/upper-bound.md):
  * n distinct labelled keys; a state is the strict partial order (transitive
    closure) induced by the comparisons made so far.
  * Reachable states from the empty poset by adding x<y / y<x are exactly the
    labelled posets on n elements, i.e. OEIS A001035(n), not 2^(n!).
  * F(P) = min remaining worst-case comparisons to finish sorting from P.
    F(total order) = 0; otherwise
        F(P) = 1 + min_{x,y incomparable} max(F(P+x<y), F(P+y<x)).

Experiments:
  1. labelled DP: S(n), reachable-state count, wall-clock.
  2. symmetry quotient: canonicalize posets under relabelling by S_n, run the
     same minimax recurrence on isomorphism classes (OEIS A000112(n) states).
  3. falsification: test coarser invariants (linear-extension count) against F.

This is an experiment, not a proof.  It uses no external libraries.
"""

import argparse
import itertools
import time
from functools import lru_cache


# --------------------------------------------------------------------------
# Labelled partial orders, represented as tuples of successor bitmasks.
# succ[i] has bit j set iff i < j (transitively closed).
# --------------------------------------------------------------------------

def extend(succ, i, j):
    """Add i < j to an already transitively closed poset; return closure."""
    out = list(succ)
    new_greater = succ[j] | (1 << j)
    for x in range(len(succ)):
        if x == i or (succ[x] & (1 << i)):
            out[x] |= new_greater
    return tuple(out)


def incomparable_pairs(succ, n):
    return [
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if not (succ[i] & (1 << j)) and not (succ[j] & (1 << i))
    ]


def labelled_solve(n):
    """Return (S(n), state_count, seconds, value_of_every_poset)."""
    states = {}

    def solve(succ):
        if succ in states:
            return states[succ]
        pairs = incomparable_pairs(succ, n)
        if not pairs:
            states[succ] = 0
            return 0
        best = 1 + min(
            max(solve(extend(succ, i, j)), solve(extend(succ, j, i)))
            for i, j in pairs
        )
        states[succ] = best
        return best

    t0 = time.perf_counter()
    value = solve((0,) * n)
    dt = time.perf_counter() - t0
    return value, len(states), dt, states


# --------------------------------------------------------------------------
# Symmetry quotient: canonical form = lexicographically least successor tuple
# over all n! relabellings of the keys.
# --------------------------------------------------------------------------

def canon(succ, perms):
    best = None
    for perm in perms:
        new = []
        for a in range(len(succ)):
            old = perm[a]
            bits = succ[old]
            m = 0
            for b in range(len(succ)):
                if bits >> perm[b] & 1:
                    m |= 1 << b
            new.append(m)
        t = tuple(new)
        if best is None or t < best:
            best = t
    return best


def refine_colors(succ, n):
    """2-dimensional colour refinement (a valid isomorphism invariant)."""
    color = [bin(succ[i]).count("1") for i in range(n)]
    while True:
        sig = []
        for i in range(n):
            down = tuple(sorted(color[j] for j in range(n) if succ[i] >> j & 1))
            up = tuple(sorted(color[j] for j in range(n) if succ[j] >> i & 1))
            sig.append((color[i], down, up))
        order = {v: k for k, v in enumerate(sorted(set(sig)))}
        comp = [order[v] for v in sig]
        if comp == color:
            return color
        color = comp


def _encode(succ, perm, n):
    new = []
    for a in range(n):
        bits = succ[perm[a]]
        m = 0
        for b in range(n):
            if bits >> perm[b] & 1:
                m |= 1 << b
        new.append(m)
    return tuple(new)


def make_refined_canon(n):
    """Complete isomorphism invariant: min encoding over relabellings that
    respect the colour classes of 2-dimensional colour refinement.  Any
    isomorphism must preserve colours, so the resulting value is invariant and
    distinguishes non-isomorphic posets (equal encodings exhibit an
    isomorphism)."""
    cache = {}

    def canon_refined(succ):
        if succ in cache:
            return cache[succ]
        color = refine_colors(succ, n)
        classes = {}
        for i, c in enumerate(color):
            classes.setdefault(c, []).append(i)
        groups = [classes[c] for c in sorted(classes)]
        best = None
        for combo in itertools.product(*(itertools.permutations(g) for g in groups)):
            perm = [0] * n
            pos = 0
            for p in combo:
                for old in p:
                    perm[pos] = old
                    pos += 1
            enc = _encode(succ, perm, n)
            if best is None or enc < best:
                best = enc
        cache[succ] = best
        return best

    return canon_refined


def quotient_solve(n, refined=True):
    """Minimax on isomorphism classes of posets under S_n relabelling."""
    if refined:
        canon_fn = make_refined_canon(n)
    else:
        perms = list(itertools.permutations(range(n)))
        canon_fn = lambda s: canon(s, perms)
    states = {}
    canon_calls = 0

    def solve(c):
        nonlocal canon_calls
        if c in states:
            return states[c]
        pairs = incomparable_pairs(c, n)
        if not pairs:
            states[c] = 0
            return 0
        best = None
        for i, j in pairs:
            canon_calls += 2
            a = canon_fn(extend(c, i, j))
            b = canon_fn(extend(c, j, i))
            v = 1 + max(solve(a), solve(b))
            if best is None or v < best:
                best = v
        states[c] = best
        return best

    t0 = time.perf_counter()
    value = solve(canon_fn((0,) * n))
    dt = time.perf_counter() - t0
    return value, len(states), dt, canon_calls


# --------------------------------------------------------------------------
# Linear-extension count (coarser invariant) for the falsification test.
# --------------------------------------------------------------------------

def linear_extensions(succ, n):
    """Number of permutations consistent with the poset."""
    count = 0
    for perm in itertools.permutations(range(n)):
        ok = True
        for i in range(n):
            for j in range(n):
                if succ[i] >> j & 1 and perm.index(i) > perm.index(j):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            count += 1
    return count


def falsify_coarse_invariant(n):
    """Find two non-isomorphic posets with equal #linear extensions but F values
    that differ.  Such pairs show the coarser invariant cannot replace the poset
    state without changing the optimum."""
    _, _, _, states = labelled_solve(n)
    perms = list(itertools.permutations(range(n)))
    by_le = {}
    for succ, value in states.items():
        le = linear_extensions(succ, n)
        by_le.setdefault(le, []).append((succ, value))
    witnesses = []
    for le, items in sorted(by_le.items()):
        if len(items) < 2:
            continue
        vals = {v for _, v in items}
        if len(vals) > 1:
            canon_rep = {}
            for succ, v in items:
                canon_rep.setdefault(canon(succ, perms), []).append(v)
            # Only interesting if the differing values survive canonicalization.
            classes = {c: set(vs) for c, vs in canon_rep.items()}
            if len(classes) >= 2:
                reps = sorted(classes.items())
                a_c, a_v = reps[0]
                for b_c, b_v in reps[1:]:
                    if a_v != b_v:
                        witnesses.append((le, a_c, sorted(a_v), b_c, sorted(b_v)))
                        break
                if witnesses:
                    break
    return witnesses


# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-n", type=int, default=6)
    ap.add_argument("--falsify-n", type=int, default=5)
    args = ap.parse_args()

    known = {0: 0, 1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10, 7: 13, 8: 16, 12: 30}
    a001035 = {0: 1, 1: 1, 2: 3, 3: 19, 4: 219, 5: 4231, 6: 130023}
    a000112 = {0: 1, 1: 1, 2: 2, 3: 5, 4: 16, 5: 63, 6: 318}

    print("n | S(n) known | labelled S | states A001035 | time(s) "
          "| quotient S | classes A000112 | time(s) | canon calls")
    for n in range(0, args.max_n + 1):
        val, cnt, dt, _ = labelled_solve(n)
        qval, qcnt, qdt, calls = quotient_solve(n)
        naive = 2 ** len(list(itertools.permutations(range(n))))
        print(f"{n} | {known.get(n, '?')} | {val} | {cnt} "
              f"(ref {a001035.get(n, '?')}) | {dt:.3f} "
              f"| {qval} | {qcnt} (ref {a000112.get(n, '?')}) | {qdt:.3f} "
              f"| {calls}")
        print(f"    naive subsets of permutations 2^(n!) = 2^{len(list(itertools.permutations(range(n))))}"
              f" = {naive:.3e}")

    print()
    print(f"Falsification: posets with equal linear-extension count, "
          f"different F (n={args.falsify_n})")
    wits = falsify_coarse_invariant(args.falsify_n)
    if not wits:
        print("  no witness found")
    for le, ca, va, cb, vb in wits:
        print(f"  #lin.ext={le}: canon {ca} -> F={va}  vs  canon {cb} -> F={vb}")


if __name__ == "__main__":
    main()
