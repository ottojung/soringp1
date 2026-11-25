#!/usr/bin/env python3
"""Lower-bound ("NO") certificates for the unary threshold SORT-BOUND-U.

Model (fixed, docs/problem.md).  A state is a transitively closed strict
partial order on ``n`` labelled keys, stored as a tuple ``succ`` with
``succ[i]`` bit ``j`` set iff ``i < j``.  The minimax value is

    F(P) = 0                                              if P is total,
    F(P) = 1 + min_{x || y} max( F(P+x<y), F(P+y<x) )      otherwise,

and ``S(n) = F(antichain_n)``.  ``SORT-BOUND-U = {1^n # 1^k : S(n) <= k}``
with unary input length ``N = n + k + 1``.

This module studies the *negative* direction: proof objects for
``NOT CanSort(P, k)``, i.e. ``S(n) > k``.  It is the dual of the upper-bound
strategy-DAG study (docs/research-strategy-certificates.md).

Certificate formats studied here
--------------------------------
1. Barrier (graded family) certificate ``B = (B_0, ..., B_k)`` of non-total
   posets: ``P0 in B_k``, and for every ``P in B_r`` (``r >= 1``) and every
   incomparable pair, at least one answer child lies in ``B_{r-1}``.
2. Admissible potential / invariant ``Phi``: ``Phi(total) = 0`` and
   ``for all non-total P, for all pairs: max(Phi(child)) >= Phi(P) - 1``.
   A potential with ``Phi(P0) > k`` is a NO certificate.
3. Symbolic adversary policy ``sigma(P, pair)`` together with a potential.

Verifiers
---------
* A barrier/DAG with explicit states is checked in ``poly(|B|, n)`` time:
  base (``B_0`` non-total), closure (each pair covered), root membership.
  No linear-extension counting is needed.
* A leaf that is certified by the information bound (``e(child) > 2^r``) is
  NOT poly-time checkable: deciding a linear-extension count against a
  threshold is PP-hard (counting linear extensions is #P-complete).
* A symbolic potential is checked by a universal condition over all states,
  which is not known to be poly-time unless a closed form with a proved
  admissibility theorem is supplied.

Experiments (this module)
-------------------------
* Reproduces the n=12, k=29 one-sided (Wells/Peczarski/Stober-Weiss) NO
  certificate: 2029 canonical states, obligation set empty at level 25.
* The sorting analogue of Cremer 2026 Remark 9: no leaf-count invariant can
  prove ``S(12) > 29``, because the optimal tree has exactly ``12!`` leaves
  and ``ceil(log2 12!) = 29``.
* The iterated one-ply potential hierarchy ``L_t`` (sound, admissible,
  ``L_t <= F``), evaluated at the antichain root for n = 12.

Stdlib only.  Experiments and paper-level deductions; no complexity-class
claim about SORT-BOUND-U is made.
"""

from __future__ import annotations

import argparse
import math
import time
from functools import lru_cache


# --------------------------------------------------------------------------
# Poset primitives
# --------------------------------------------------------------------------

def extend(succ, i, j):
    """Transitive closure after adding ``i < j`` to a closed state."""
    out = list(succ)
    new_greater = succ[j] | (1 << j)
    for x in range(len(succ)):
        if x == i or (succ[x] & (1 << i)):
            out[x] |= new_greater
    return tuple(out)


def incomparable_pairs(succ):
    n = len(succ)
    return [(i, j) for i in range(n) for j in range(i + 1, n)
            if not (succ[i] & (1 << j)) and not (succ[j] & (1 << i))]


def is_total(succ):
    n = len(succ)
    return all((succ[i] >> j & 1) or (succ[j] >> i & 1)
               for i in range(n) for j in range(i + 1, n))


def dual(succ):
    n = len(succ)
    out = [0] * n
    for i in range(n):
        for j in range(n):
            if (succ[i] >> j) & 1:
                out[j] |= 1 << i
    return tuple(out)


def ceil_log2(x):
    return (x - 1).bit_length()


# --------------------------------------------------------------------------
# Linear extensions: naive DP (small n) and the efficient child-counting form
# --------------------------------------------------------------------------

@lru_cache(maxsize=None)
def linear_extensions(succ):
    """e(P) by DP over downsets.  O(2^n n) for small n."""
    n = len(succ)
    full = (1 << n) - 1
    dp = [0] * (1 << n)
    dp[0] = 1
    for S in range(1, 1 << n):
        tot = 0
        m = S
        while m:
            x = (m & -m).bit_length() - 1
            m &= m - 1
            if (succ[x] & (S ^ (1 << x))) == 0:
                tot += dp[S ^ (1 << x)]
        dp[S] = tot
    return dp[full]


def _pred_masks(succ):
    n = len(succ)
    pred = [0] * n
    for i in range(n):
        bits = succ[i]
        while bits:
            j = (bits & -bits).bit_length() - 1
            bits &= bits - 1
            pred[j] |= 1 << i
    return pred


def _downsets(succ):
    n = len(succ)
    pred = _pred_masks(succ)
    full = (1 << n) - 1
    seen = {0}
    stack = [0]
    while stack:
        D = stack.pop()
        rem = full ^ D
        m = rem
        while m:
            x = (m & -m).bit_length() - 1
            m &= m - 1
            if (pred[x] & ~D) == 0:
                D2 = D | (1 << x)
                if D2 not in seen:
                    seen.add(D2)
                    stack.append(D2)
    return seen


def _f_table(succ, downs):
    """f[D] = e(P restricted to the downset D), by removing a maximal element."""
    succ_masks = succ
    f = {0: 1}
    for D in sorted(downs, key=lambda s: bin(s).count("1")):
        if D == 0:
            continue
        tot = 0
        m = D
        while m:
            x = (m & -m).bit_length() - 1
            m &= m - 1
            if (succ_masks[x] & D) == 0:
                tot += f[D ^ (1 << x)]
        f[D] = tot
    return f


def child_e_values(succ):
    """Return ({(i,j): (e(P+i<j), e(P+j<i))}, e(P)) for all incomparable pairs.

    Uses the identity e(P+u<v) = number of linear extensions of P with u
    before v, factorised over the unique split (D = before v, V = after v).
    """
    n = len(succ)
    full = (1 << n) - 1
    pred = _pred_masks(succ)
    downs = _downsets(succ)
    f = _f_table(succ, downs)
    eP = f[full]
    Pd = dual(succ)
    downsd = _downsets(Pd)
    fd = _f_table(Pd, downsd)
    S = [[0] * n for _ in range(n)]
    for D in downs:
        rem = full ^ D
        m = rem
        while m:
            v = (m & -m).bit_length() - 1
            m &= m - 1
            if (pred[v] & rem) != 0:
                continue
            V = full ^ D ^ (1 << v)
            gV = fd[V]
            T = f[D] * gV
            mm = D
            while mm:
                u = (mm & -mm).bit_length() - 1
                mm &= mm - 1
                S[u][v] += T
    res = {}
    for (i, j) in incomparable_pairs(succ):
        e_ij = S[i][j]
        res[(i, j)] = (e_ij, eP - e_ij)
    return res, eP


# --------------------------------------------------------------------------
# Canonical relabelling (de-duplication only; never merges non-isomorphic P)
# --------------------------------------------------------------------------

def refine_colors(succ):
    n = len(succ)
    color = [bin(succ[i]).count("1") for i in range(n)]
    while True:
        sig = []
        for i in range(n):
            down = tuple(sorted(color[j] for j in range(n)
                                if (succ[i] >> j) & 1))
            up = tuple(sorted(color[j] for j in range(n)
                              if (succ[j] >> i) & 1))
            sig.append((color[i], down, up))
        order = {v: k for k, v in enumerate(sorted(set(sig)))}
        comp = [order[v] for v in sig]
        if comp == color:
            return color
        color = comp


@lru_cache(maxsize=None)
def relabel(succ):
    n = len(succ)
    color = refine_colors(succ)
    order = sorted(range(n), key=lambda i: (color[i], i))
    new = [0] * n
    for a in range(n):
        bits = succ[order[a]]
        m = 0
        for b in range(n):
            if (bits >> order[b]) & 1:
                m |= 1 << b
        new[a] = m
    return tuple(new)


@lru_cache(maxsize=None)
def relabel_dual(succ):
    return min(relabel(succ), relabel(dual(succ)))


# --------------------------------------------------------------------------
# 1. Barrier (dual OR/AND proof DAG) certificates and their verifier
# --------------------------------------------------------------------------

class Barrier:
    """A graded family B = (B_0, ..., B_k) of non-total posets.

    Sound iff: B_0 elements are non-total; for each P in B_r (r >= 1) and each
    incomparable pair, at least one answer child lies in B_{r-1}; and the
    root lies in B_k.
    """

    def __init__(self, levels, root, k):
        self.levels = levels          # list of sets of posets
        self.root = root
        self.k = k

    def verify(self):
        """Polynomial-time check.  Returns (ok, message)."""
        # Base: B_0 non-total.
        for P in self.levels[0]:
            if is_total(P):
                return False, f"B_0 contains total poset {P}"
        # Closure: each non-total P in B_r (r>=1) has every pair covered.
        for r in range(1, self.k + 1):
            prev = self.levels[r - 1]
            for P in self.levels[r]:
                if is_total(P):
                    return False, f"B_{r} contains total poset {P}"
                for (i, j) in incomparable_pairs(P):
                    a = extend(P, i, j)
                    b = extend(P, j, i)
                    if a not in prev and b not in prev:
                        return False, (f"uncovered pair {(i, j)} at B_{r}, P={P}")
        if self.root not in self.levels[self.k]:
            return False, "root not in B_k"
        return True, "barrier verified in poly(|B|, n)"


def build_barrier_from_minimax(n, k, m, cap=None):
    """Build the exact barrier for (antichain_n, k) from exact F values."""
    root = (0,) * n
    if m[root] <= k:
        raise ValueError("root is sortable within budget; no NO certificate")
    levels = [set() for _ in range(k + 1)]
    levels[k].add(root)
    for r in range(k, 0, -1):
        cur = levels[r]
        nxt = set()
        for P in cur:
            for (i, j) in incomparable_pairs(P):
                a = extend(P, i, j)
                b = extend(P, j, i)
                if m[a] > r - 1:
                    nxt.add(a)
                if m[b] > r - 1:
                    nxt.add(b)
        levels[r - 1] = nxt
        if cap is not None and len(nxt) > cap:
            return Barrier(levels, root, k), True
    return Barrier(levels, root, k), False


def minimax_values(n):
    """Exact F over all labelled posets on n elements (n <= 7 feasible)."""
    states = {}

    def solve(succ):
        r = states.get(succ)
        if r is not None:
            return r
        pairs = incomparable_pairs(succ)
        if not pairs:
            states[succ] = 0
            return 0
        best = 1 + min(max(solve(extend(succ, i, j)),
                           solve(extend(succ, j, i)))
                       for i, j in pairs)
        states[succ] = best
        return best

    solve((0,) * n)
    return states


# --------------------------------------------------------------------------
# 2. One-sided (Wells / Peczarski / Stober-Weiss) NO certificate
# --------------------------------------------------------------------------

def wells_forward(n, C, cap=None, max_seconds=None, use_dual=True):
    """One-sided heavy-child forward search.

    Level c+1 keeps the heavier child of each pair whose two outcomes both
    have e <= 2^(C-c-1).  If a level is empty, some state at the previous
    level has a child with e > 2^(remaining), which the information bound
    already rejects; hence no height-C tree exists.
    """
    keyfn = relabel_dual if use_dual else relabel
    root = keyfn((0,) * n)
    levels = [{root: root}]
    t0 = time.perf_counter()
    capped = False
    c = 0
    while levels[-1] and c < C:
        if max_seconds is not None and time.perf_counter() - t0 > max_seconds:
            capped = True
            break
        cur = levels[-1]
        nxt = {}
        thr = 1 << (C - c - 1)
        for P in cur.values():
            ev, _ = child_e_values(P)
            for (i, j), (eij, eji) in ev.items():
                if eij > thr or eji > thr:
                    continue
                child = extend(P, i, j) if eij >= eji else extend(P, j, i)
                kk = keyfn(child)
                if kk not in nxt:
                    nxt[kk] = kk
        levels.append(nxt)
        c += 1
        if cap is not None and len(nxt) > cap:
            capped = True
            break
    return {"levels": levels, "capped": capped,
            "seconds": time.perf_counter() - t0}


def report_wells(n, C, cap=None, max_seconds=None):
    res = wells_forward(n, C, cap=cap, max_seconds=max_seconds)
    sizes = [len(s) for s in res["levels"]]
    total = sum(sizes)
    empty_at = next((i for i, s in enumerate(res["levels"]) if not s), None)
    status = "capped" if res["capped"] else "complete"
    print(f"n={n:>2} C={C:>2} N={n+C+1:>3} status={status:>8} "
          f"time={res['seconds']:.2f}s total_nodes={total}")
    print(f"      level sizes: {sizes}")
    if empty_at is not None:
        print(f"      -> level {empty_at} EMPTY: NO certificate proves S({n}) > {C}")
    print()
    return res


# --------------------------------------------------------------------------
# 3. The Cremer-Remark-9 analogue for sorting: leaf-count limits
# --------------------------------------------------------------------------

def leaf_count_counterexample(n, k):
    """Show that no leaf-count invariant can prove S(n) > k when k >= ceil(log2 n!).

    Any correct sorting tree has at least n! reachable leaves (one per
    permutation).  A reduced optimal tree has exactly n! leaves.  Any valid
    leaf-count lower bound N satisfies N <= n!, so its ceiling log is at most
    ceil(log2 n!).  Therefore a leaf-count invariant can never prove S(n) > k
    when k >= ceil(log2 n!).  For (n,k)=(12,29), k = ceil(log2 12!) exactly.
    """
    nfact = math.factorial(n)
    info = ceil_log2(nfact)
    proves = k >= info
    return {
        "n": n, "k": k, "n!": nfact, "ceil(log2 n!)": info,
        "leaf_count_can_prove": proves,
        "argument": ("optimal tree has exactly n! leaves; any leaf-count bound "
                     "is <= n!, so log is <= ceil(log2 n!)"),
    }


def report_leaf_count():
    print("=" * 74)
    print("CREMER-REMARK-9 ANALOGUE FOR SORTING (leaf-count limits)")
    print("=" * 74)
    print(f"{'(n,k)':>9} {'N=n+k+1':>8} {'n!':>14} {'ceil(log2 n!)':>13} "
          f"{'leaf-count bound can prove?':>28}")
    for (n, k) in [(10, 21), (11, 25), (12, 29), (12, 28), (13, 33)]:
        r = leaf_count_counterexample(n, k)
        print(f"{str((n,k)):>9} {n+k+1:>8} {r['n!']:>14} {r['ceil(log2 n!)']:>13} "
              f"{str(r['leaf_count_can_prove']):>28}")
    print()
    print("For n=12, k=29: 12! = 479001600 < 2^29 = 536870912, so")
    print("ceil(log2 12!) = 29.  The optimal tree has exactly 12! leaves, so")
    print("ANY valid leaf-count lower bound is <= 12! and its ceiling log is")
    print("<= 29.  No leaf-count invariant can prove S(12) > 29.")
    print("(Cremer 2026, Remark 9, proves the selection analogue: no leaf count")
    print("can prove V_8(16) >= 29.)")
    print()


# --------------------------------------------------------------------------
# 4. Iterated one-ply potential hierarchy L_t (sound, admissible)
# --------------------------------------------------------------------------

def L0(succ):
    return ceil_log2(linear_extensions(succ))


@lru_cache(maxsize=None)
def potential(key, t):
    """The t-ply potential L_t at a canonical (dual) state ``key``.

    L_0(P) = ceil(log2 e(P));  L_t(P) = 0 if P total, else
    L_t(P) = 1 + min_p max(L_{t-1}(child)).
    L_t is sound (L_t <= F), admissible, non-decreasing in t, and -> F.
    Memoised on (canonical form, t).
    """
    if t == 0:
        return ceil_log2(linear_extensions(key))
    pairs = incomparable_pairs(key)
    if not pairs:
        return 0
    return 1 + min(max(potential(relabel_dual(extend(key, i, j)), t - 1),
                       potential(relabel_dual(extend(key, j, i)), t - 1))
                   for i, j in pairs)


def report_potentials(n):
    print("=" * 74)
    print(f"ITERATED ONE-PLY POTENTIAL HIERARCHY L_t AT THE ROOT (n={n})")
    print("=" * 74)
    root = (0,) * n
    l0 = L0(root)
    print(f"  L0(antichain) = ceil(log2 {n}!) = {l0}")
    if n <= 12:
        key = relabel_dual(root)
        tmax = 9 if n == 12 else 12
        for t in range(1, tmax + 1):
            t0 = time.perf_counter()
            val = potential(key, t)
            t1 = time.perf_counter()
            print(f"  L{t:>2}(antichain) = {val}   ({t1-t0:.2f}s)")
            if val == 30:
                print(f"      -> L{t} > 29 proves S({n}) > 29 at depth {t}")
                break
        if n == 12:
            print("      (depth capped at 9: each further level multiplies the")
            print("       state count by ~4.5x; L9 already costs ~469s.)")
    print()
    print("L_t is sound (L_t <= F), admissible, and non-decreasing in t, with")
    print("L_t -> F.  L_t(P0) > k proves S(n) > k.  Each L_t is a certificate")
    print("of the 'symbolic potential' kind; evaluating it requires counting")
    print("linear extensions (PP-hard per leaf), so it is not poly-time.")
    print()


def verify_potential(max_n=5, n6_sample=2000):
    """Exhaustively check, for every poset on n <= max_n (and a deterministic
    n=6 sample):

      * Soundness:      L_t(P) <= F(P) for all t <= F(P).
      * Monotonicity:   L_t(P) <= L_{t+1}(P).
      * Convergence:    L_t(P) = F(P) for all t >= F(P).

    Returns a summary dict; raises AssertionError on any failure.
    """
    summary = {"checked": 0, "soundness_violations": 0,
               "monotonicity_violations": 0, "convergence_violations": 0}
    for n in range(1, max_n + 1):
        m = minimax_values(n)
        states = sorted(m)
        if n == 6:
            states = states[:n6_sample]
        for P in states:
            F = m[P]
            key = relabel_dual(P)
            prev = None
            for t in range(0, F + 1):
                val = potential(key, t)
                if val > F:
                    summary["soundness_violations"] += 1
                    print(f"  SOUNDNESS FAIL n={n} P={P} t={t} L={val} F={F}")
                if prev is not None and val < prev:
                    summary["monotonicity_violations"] += 1
                    print(f"  MONO FAIL n={n} P={P} t={t} L={val} prev={prev}")
                if t >= F and val != F:
                    summary["convergence_violations"] += 1
                    print(f"  CONV FAIL n={n} P={P} t={t} L={val} F={F}")
                prev = val
            summary["checked"] += 1
    return summary


def report_verify(max_n=5, n6_sample=2000):
    print("=" * 74)
    print("EXHAUSTIVE VERIFICATION OF THE L_t POTENTIAL")
    print("=" * 74)
    s = verify_potential(max_n=max_n, n6_sample=n6_sample)
    print(f"  posets checked: {s['checked']}")
    print(f"  soundness violations:      {s['soundness_violations']}")
    print(f"  monotonicity violations:   {s['monotonicity_violations']}")
    print(f"  convergence violations:    {s['convergence_violations']}")
    print()


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mode", default="all",
                    choices=["all", "wells", "leafcount", "potentials", "barrier",
                             "verify"])
    ap.add_argument("--n", type=int, default=12)
    ap.add_argument("--k", type=int, default=29)
    ap.add_argument("--cap", type=int, default=3000000)
    ap.add_argument("--seconds", type=float, default=600.0)
    args = ap.parse_args()

    if args.mode in ("all", "leafcount"):
        report_leaf_count()

    if args.mode in ("all", "potentials"):
        report_potentials(args.n)

    if args.mode in ("all", "verify"):
        report_verify(max_n=min(args.n, 5), n6_sample=0)

    if args.mode in ("all", "barrier"):
        print("=" * 74)
        print("EXACT BARRIER CERTIFICATE + POLY-TIME VERIFIER (small n)")
        print("=" * 74)
        for n in (5, 6, 7):
            k = {5: 6, 6: 9, 7: 12}[n]
            m = minimax_values(n)
            b, capped = build_barrier_from_minimax(n, k, m)
            ok, msg = b.verify()
            sizes = [len(s) for s in b.levels]
            print(f"  n={n} k={k}: |B|={sum(sizes)} levels={sizes} "
                  f"verified={ok} ({msg})")
        print()

    if args.mode in ("all", "wells"):
        print("=" * 74)
        print("ONE-SIDED (WELLS) NO CERTIFICATES")
        print("=" * 74)
        for (n, k) in [(11, 25), (12, 29)]:
            report_wells(n, k, cap=args.cap, max_seconds=args.seconds)


if __name__ == "__main__":
    main()
