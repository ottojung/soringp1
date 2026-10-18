#!/usr/bin/env python3
"""Sound pruning and move reduction for the exact budgeted sorting DFS.

This is an *experiment*, not a proof.  It improves the reference budgeted DFS
of ``scripts/budgeted_dfs.py`` (the ``CanSort`` decision procedure) with three
independently justified, **provably sound** optimizations, and measures their
call-count and wall-clock effect against the unchanged reference.  The reference
``can_sort`` / ``compute_s_dfs`` are **not** modified; they are re-implemented
here (verbatim semantics) as ``can_sort_reference`` and cross-checked.

Model (docs/problem.md, docs/upper-bound.md, docs/research-budgeted-dfs.md):
  * n distinct labelled keys; a state is the transitively closed poset P induced
    by the comparisons made so far (successor bitmasks: bit j of succ[i] iff
    i < j).
  * S(n) = minimum worst-case number of adaptive pairwise comparisons to sort.
  * Game G(n,k): sorter picks an incomparable pair, adversary answers, P becomes
    its transitive closure.  S(n) <= k iff the sorter wins G(n,k).
  * CanSort(P, d) = the sorter can force a total order from P within d
    comparisons.  CanSort(P, d) = True iff F(P) <= d, where F is the exact
    minimax value (adv univ, A24) and S(n) = F(empty).

SPACE COMPLEXITY (flagged explicitly per the coordination note 510a18001004):
  * The reference DFS keeps only the recursion stack: O(d * n^2) bits,
    polynomial space.
  * The poly-space pruning primitive is ``e_exceeds``: a depth-first enumeration
    of linear extensions that stops at cap+1 of them.  It uses an order-ideal DFS
    stack (depth n, O(n) per frame = O(n^2) bits) and a counter, so it is
    polynomial space and never builds a 2^n table.  Every order-ideal prefix
    extends to at least one full linear extension, so there are no dead ends.
  * ``linear_extensions`` (subset/downset DP with an lru_cache) is an EXACT
    cross-check and a fast prototype, but it stores up to 2^n ideal counts, so it
    is O(2^n) space and does NOT preserve the poly-space guarantee.  It is used
    only as ``ext='exact'`` for comparison, never as the recommended method.
  * ``width`` is polynomial-time computable in general (Dilworth / matching); the
    subset scan used here is 2^n *time* but O(n) space.

Three optimizations (each proven sound in docs/research-budget-pruning.md):

  1. EXTENSION-COUNT CUTOFF (information bound, poset level).
     Necessary condition:  F(P) <= d  implies  e(P) <= 2^d,
     where e(P) is the number of linear extensions of P.  Contrapositive:
     e(P) > 2^d  implies  F(P) > d, so CanSort(P, d) = False and the node may be
     pruned.  Deciding "e(P) > 2^d?" is done by the poly-space capped
     enumeration ``e_exceeds(P, n, 2^d)``.  A cheap, strictly WEAKER surrogate is
     ``width(P)!`` (it reproduces a weaker lower bound than exact ceil(log2 e),
     not a new bound; included only to measure how much of the benefit the cheap
     version captures).

  2. HANAMURA-IWATA BASE (acceptance shortcut, poly-space).
     [literature] Hanamura-Iwata (2011): every poset with e(P) <= 7 linear
     extensions is sortable by three comparisons, i.e. F(P) <= 3.  Hence
     CanSort(P, d) = True whenever d >= 3 and e(P) <= 7.  The predicate
     "e(P) <= 7" is decided in polynomial time and space by ``e_at_most(P, 7)``
     (enumerate at most 8 extensions).  No 2^n table is needed.

  3. AUTOMORPHISM MOVE ORBITS (both outcomes retained).
     For phi in Aut(P), the map P -> P is an isomorphism, so the two children of
     {i,j} and of {phi i, phi j} have equal F; hence the decision predicate
     "both children win" is invariant on Aut(P)-orbits of incomparable pairs.
     The existential (OR) may therefore range over one representative per orbit
     only.  BOTH adversary outcomes of the chosen representative are still
     explored (the reverse branch is never dropped; cf. the n=3 dual-branch
     falsification of docs/research-compression-next.md section 6a).

  4. ORDINAL-SUM ALLOCATION (exact value shortcut).
     If P is a genuine ordinal sum A (+) B (every element of A below every
     element of B), then F(P) = F(A) + F(B): all cross pairs are already
     comparable, so every comparison is internal to one block and the blocks are
     independent.  A value-DFS may then return F(A) + F(B) instead of searching
     the full n-element tree.  Additivity is a standard result (verified for
     every poset with n <= 5 here; see also
     docs/research-series-decomposition.md section 2).

Everything is labelled [definition] / [deduction] / [literature] / [experiment]
in docs/research-budget-pruning.md.  No complexity-class claim is made.  The
optimizations never change the boolean answer; soundness is re-verified against
the reference on every run (see --verify and tests/test_budget_pruning.py).
"""

from __future__ import annotations

import argparse
import math
import random
import sys
import time
from functools import lru_cache
from itertools import permutations

sys.setrecursionlimit(100000)

# ---------------------------------------------------------------------------
# Poset machinery (successor bitmasks; re-implemented, self-contained).
# ---------------------------------------------------------------------------


def extend(succ, i, j):
    """Transitive closure after adding i < j to an already closed poset."""
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


def is_total(succ, n):
    return all(
        (succ[i] >> j) & 1 or (succ[j] >> i) & 1
        for i in range(n)
        for j in range(i + 1, n)
    )


def antichain(n):
    return (0,) * n


def factorial(k):
    return math.factorial(k)


# ---------------------------------------------------------------------------
# Linear extensions: poly-space capped enumeration (complexity-correct) and
# exact subset DP (fast prototype, O(2^n) space).
# ---------------------------------------------------------------------------


def e_exceeds(succ, n, cap):
    """True iff e(P) > cap, by DFS enumeration that stops at cap+1 extensions.

    Polynomial space: depth-n recursion, O(n) per frame (an order-ideal stack),
    plus a counter; never builds a 2^n table.  Every order-ideal prefix extends
    to at least one full linear extension, so there are no dead ends and the
    search visits O(min(e, cap+1) * n) nodes.
    """
    state = {"count": 0, "stop": False}

    def dfs(remaining):
        if not remaining:
            state["count"] += 1
            if state["count"] > cap:
                state["stop"] = True
            return
        rem = tuple(remaining)
        for x in rem:
            if state["stop"]:
                return
            # x is minimal in the remaining subposet iff no other y < x.
            if not any(succ[y] & (1 << x) for y in rem if y != x):
                dfs(tuple(y for y in rem if y != x))

    dfs(tuple(range(n)))
    return state["count"] > cap


def e_at_most(succ, n, E):
    """Decide e(P) <= E in polynomial time and space (enumerate <= E+1)."""
    return not e_exceeds(succ, n, E)


def linear_extensions(succ, n):
    """Exact e(P) by the minimal-element order-ideal DP.

    Fast, but the lru_cache stores up to 2^n ideal counts, so this is O(2^n)
    SPACE.  Used only as an exact cross-check and the ext='exact' prototype; the
    recommended poly-space method is e_exceeds / e_at_most.
    """

    @lru_cache(maxsize=None)
    def count(remaining):
        if not remaining:
            return 1
        rem = tuple(remaining)
        return sum(
            count(tuple(y for y in rem if y != x))
            for x in rem
            if not any(succ[y] & (1 << x) for y in rem if y != x)
        )

    return count(tuple(range(n)))


def linear_extensions_bruteforce(succ, n):
    """e(P) by enumerating all n! permutations (independent ground truth)."""
    c = 0
    for p in permutations(range(n)):
        if all(
            not (succ[p[a]] >> p[b] & 1)
            for a in range(n)
            for b in range(a + 1, n)
        ):
            c += 1
    return c


# ---------------------------------------------------------------------------
# Width and the (weaker) width! lower bound on e(P).
# ---------------------------------------------------------------------------


def width(succ, n):
    """Size of a maximum antichain, by exhaustive subset scan (2^n time)."""
    best = 0
    for mask in range(1, 1 << n):
        els = [i for i in range(n) if mask >> i & 1]
        if len(els) <= best:
            continue
        ok = True
        for a in els:
            for b in els:
                if a != b and ((succ[a] >> b & 1) or (succ[b] >> a & 1)):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            best = len(els)
    return best


# ---------------------------------------------------------------------------
# Automorphism orbits of incomparable pairs (sound move reduction).
# ---------------------------------------------------------------------------


def automorphisms(succ, n):
    """All permutations p with succ[p[a]] == image of succ[a] under p."""
    result = []
    for p in permutations(range(n)):
        ok = True
        for a in range(n):
            img = 0
            for b in range(n):
                if succ[a] >> b & 1:
                    img |= 1 << p[b]
            if img != succ[p[a]]:
                ok = False
                break
        if ok:
            result.append(p)
    return result


def orbit_representatives(succ, n):
    """One unordered incomparable pair per Aut(P)-orbit.

    Sound by the isomorphism invariance of F (docs/research-compression-next.md
    Theorem 5).  The antichain (Aut = S_n) has a single orbit.
    """
    if succ == (0,) * n:
        return [(0, 1)] if n >= 2 else []
    aut = automorphisms(succ, n)
    covered = set()
    reps = []
    for (i, j) in incomparable_pairs(succ, n):
        if (i, j) in covered:
            continue
        reps.append((i, j))
        for p in aut:
            a, b = p[i], p[j]
            covered.add((min(a, b), max(a, b)))
    return reps


# ---------------------------------------------------------------------------
# Ordinal-sum (series) structure for the value shortcut.
# ---------------------------------------------------------------------------


def incomparability_components(succ, n):
    """Connected components of the incomparability graph = the unique
    ordinal-sum decomposition into ordinally indecomposable factors
    (Pouzet-Zaguia; Erne-Stege 1995)."""
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in range(n):
        for j in range(i + 1, n):
            if not (succ[i] & (1 << j)) and not (succ[j] & (1 << i)):
                ri, rj = find(i), find(j)
                if ri != rj:
                    parent[ri] = rj
    comps = {}
    for i in range(n):
        comps.setdefault(find(i), []).append(i)
    return list(comps.values())


def ordinal_sum_blocks(succ, n):
    """Ordinal-sum blocks ordered bottom-to-top; None if series-prime or not a
    genuine ordinal sum (blocks not totally ordered by complete cross-block
    comparability)."""
    comps = incomparability_components(succ, n)
    if len(comps) == 1:
        return None

    def below(a, b):
        return all(succ[x] & (1 << y) for x in a for y in b)

    ordered = list(comps)
    for i in range(1, len(ordered)):
        key = ordered[i]
        j = i - 1
        while j >= 0 and below(key, ordered[j]):
            ordered[j + 1] = ordered[j]
            j -= 1
        ordered[j + 1] = key
    for a in range(len(ordered)):
        for b in range(a + 1, len(ordered)):
            if not below(ordered[a], ordered[b]):
                return None
    return ordered


def induced(succ, subset):
    """Induced subposet on subset, relabelled to 0..m-1."""
    index = {e: k for k, e in enumerate(subset)}
    return tuple(
        sum((1 << index[j]) for j in subset if succ[i] & (1 << j))
        for i in subset
    )


# ---------------------------------------------------------------------------
# Reference budgeted DFS (verbatim semantics of scripts/budgeted_dfs.py).
# ---------------------------------------------------------------------------


def can_sort_reference(succ, n, d, counter, node_cap=None):
    """Unmodified reference decision procedure (baseline)."""
    counter[0] += 1
    if node_cap is not None and counter[0] > node_cap:
        return None, True
    if is_total(succ, n):
        return True, False
    if d == 0:
        return False, False
    for i, j in incomparable_pairs(succ, n):
        a, cap = can_sort_reference(extend(succ, i, j), n, d - 1, counter, node_cap)
        if cap:
            return None, True
        if a:
            b, cap = can_sort_reference(extend(succ, j, i), n, d - 1, counter, node_cap)
            if cap:
                return None, True
            if b:
                return True, False
    return False, False


# ---------------------------------------------------------------------------
# Pruned budgeted DFS.
# ---------------------------------------------------------------------------


def can_sort_pruned(
    succ,
    n,
    d,
    counter,
    node_cap=None,
    ext="none",
    hi_base=False,
    orbits=False,
    orbit_max_depth=None,
    depth=0,
):
    """Reference DFS with sound pruning / move reduction.

    ext            : 'none' | 'width' | 'enum' | 'exact'  (extension cutoff).
                     'enum' is the poly-space e_exceeds method (recommended);
                     'exact' is the fast O(2^n)-space subset-DP prototype;
                     'width' is the cheap strictly-weaker width! surrogate.
    hi_base        : Hanamura-Iwata acceptance (d >= 3 and e(P) <= 7 => True),
                     decided in poly-space by e_at_most(P, 7).
    orbits         : restrict the OR to Aut(P)-orbit representatives (both
                     children of each representative are still explored).
    orbit_max_depth: if set, use orbits only at depth <= orbit_max_depth
                     (avoids the O(n!) Aut cost deep in the tree).

    The return value is identical to can_sort_reference; the optimizations only
    ever return True *earlier* (acceptance) or False *earlier* (prune), or skip
    provably-equivalent moves.
    """
    counter[0] += 1
    if node_cap is not None and counter[0] > node_cap:
        return None, True
    if is_total(succ, n):
        return True, False
    if d == 0:
        return False, False
    if hi_base and d >= 3 and e_at_most(succ, n, 7):
        return True, False
    if ext != "none":
        if ext == "width":
            if factorial(width(succ, n)) > (1 << d):
                return False, False
        elif ext == "enum":
            if e_exceeds(succ, n, 1 << d):
                return False, False
        elif ext == "exact":
            if linear_extensions(succ, n) > (1 << d):
                return False, False
        else:
            raise ValueError(ext)
    pairs = incomparable_pairs(succ, n)
    if orbits and (orbit_max_depth is None or depth <= orbit_max_depth):
        pairs = orbit_representatives(succ, n)
    for i, j in pairs:
        a, cap = can_sort_pruned(
            extend(succ, i, j), n, d - 1, counter, node_cap, ext, hi_base,
            orbits, orbit_max_depth, depth + 1,
        )
        if cap:
            return None, True
        if a:
            b, cap = can_sort_pruned(
                extend(succ, j, i), n, d - 1, counter, node_cap, ext, hi_base,
                orbits, orbit_max_depth, depth + 1,
            )
            if cap:
                return None, True
            if b:
                return True, False
    return False, False


# ---------------------------------------------------------------------------
# Value DFS with ordinal-sum allocation (exact F, no memoization).
# ---------------------------------------------------------------------------


def F_value(succ, n, use_ordinal_sum=False, counter=None):
    """Exact F(P) by DFS.  With use_ordinal_sum, a genuine ordinal sum A (+) B
    returns F(A) + F(B) immediately (additivity), skipping the full tree."""
    if counter is not None:
        counter[0] += 1
    if is_total(succ, n):
        return 0
    if use_ordinal_sum:
        blocks = ordinal_sum_blocks(succ, n)
        if blocks is not None:
            return sum(
                F_value(induced(succ, blk), len(blk), True, counter)
                for blk in blocks
            )
    return 1 + min(
        max(
            F_value(extend(succ, i, j), n, use_ordinal_sum, counter),
            F_value(extend(succ, j, i), n, use_ordinal_sum, counter),
        )
        for (i, j) in incomparable_pairs(succ, n)
    )


# ---------------------------------------------------------------------------
# Memoized reference F (from scripts/evaluate.py) for cross-checking.
# ---------------------------------------------------------------------------


def memoized_F(n):
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

    solve((0,) * n)
    return states


# ---------------------------------------------------------------------------
# Search driver: binary search for S(n) under a given decision procedure.
# ---------------------------------------------------------------------------


def merge_sort_upper_bound(n):
    if n <= 1:
        return 0
    return n * (max(2, n) - 1).bit_length()


def compute_s(n, decide, **kw):
    """Binary search for S(n); ``decide`` is a (succ,n,d,counter,node_cap) fn.
    Returns (value, calls, seconds, hit_cap)."""
    if n <= 1:
        return 0, 1, 0.0, False
    lo, hi = 0, merge_sort_upper_bound(n)
    counter = [0]
    t0 = time.perf_counter()
    hit_cap = False
    while lo < hi:
        mid = (lo + hi) // 2
        res, cap = decide((0,) * n, n, mid, counter, **kw)
        if cap:
            hit_cap = True
            break
        if res:
            hi = mid
        else:
            lo = mid + 1
    dt = time.perf_counter() - t0
    return lo, counter[0], dt, hit_cap


# ---------------------------------------------------------------------------
# Verification harness: pruned decisions must equal the reference decisions.
# ---------------------------------------------------------------------------


def all_posets(n):
    seen = {(0,) * n}
    frontier = [(0,) * n]
    while frontier:
        nxt = []
        for s in frontier:
            for i in range(n):
                for j in range(i + 1, n):
                    if not (s[i] & (1 << j)) and not (s[j] & (1 << i)):
                        for t in (extend(s, i, j), extend(s, j, i)):
                            if t not in seen:
                                seen.add(t)
                                nxt.append(t)
        frontier = nxt
    return seen


def random_poset(n, p, rng):
    succ = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < p:
                succ[i] |= 1 << j
    for k in range(n):
        for i in range(n):
            if succ[i] >> k & 1:
                succ[i] |= succ[k]
    return tuple(succ)


def structured_posets(n):
    out = {
        "antichain": antichain(n),
        "chain+iso": chain_plus_isolated(n),
        "2-chains": disjoint_chains(n, 2),
    }
    if n % 2 == 0:
        out["crown"] = crown(n)
    return out


def chain_plus_isolated(n):
    succ = [0] * n
    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            succ[i] |= 1 << j
    return tuple(succ)


def disjoint_chains(n, k):
    succ = [0] * n
    sizes = [n // k + (1 if i < n % k else 0) for i in range(k)]
    idx = 0
    for s in sizes:
        for a in range(idx, idx + s):
            for b in range(a + 1, idx + s):
                succ[a] |= 1 << b
        idx += s
    return tuple(succ)


def crown(n):
    if n % 2 != 0:
        raise ValueError("crown needs even n")
    half = n // 2
    succ = [0] * n
    for i in range(half):
        succ[i] |= 1 << half + i
        succ[i] |= 1 << half + (i - 1) % half
    return tuple(succ)


def _decision_equivalence(P, n, d, node_cap, stats):
    """Reference vs pruned decision for one (P, d). Returns #failures."""
    f = 0
    c_ref = [0]
    r_ref, cap_ref = can_sort_reference(P, n, d, c_ref, node_cap)
    for label, kw in (
        ("ext=width", dict(ext="width")),
        ("ext=enum", dict(ext="enum")),
        ("ext=exact", dict(ext="exact")),
        ("hi_base", dict(hi_base=True)),
        ("ext=enum+hi_base", dict(ext="enum", hi_base=True)),
        ("orbits", dict(orbits=True)),
        ("ext=enum+orbits", dict(ext="enum", orbits=True)),
    ):
        cq = [0]
        rq, cap_q = can_sort_pruned(P, n, d, cq, node_cap, **kw)
        stats["checks"] += 1
        if cap_q or rq != r_ref:
            f += 1
            print(f"  DECISION MISMATCH n={n} d={d} {P} {label}: "
                  f"{rq} (cap={cap_q}) != {r_ref}")
    return f


def verify(n_max=5, node_cap=2_000_000, verbose=True):
    """Exhaustively check soundness.  Two tiers, because the decision DFS is
    expensive deep in the tree:

    * TIER 1 (cheap, exhaustive for every poset with n <= n_max):
        - linear_extensions == linear_extensions_bruteforce (exactness of e);
        - e_exceeds(P, cap) == (linear_extensions(P) > cap) for all caps that
          arise (cap = 2^d, d <= U(n)) and cap = 7 (Hanamura-Iwata);
        - e(P) >= width(P)!                            (width surrogate valid);
        - F_value(., use_ordinal_sum=True) == F[P]    (ordinal-sum additivity);
        - ordinal_sum_blocks is a genuine ordinal sum when it returns blocks.
    * TIER 2 (decision equivalence vs the reference):
        - exhaustive over all posets for n <= min(n_max, 4);
        - for n == 5, structured posets and a fixed random sample (the deep
          n = 5 search is covered by tests/test_budget_pruning.py and the repo
          regression tests/test_budgeted_dfs.py).

    Returns the number of failures (0 = all sound).
    """
    fails = 0
    checks = 0
    rng = random.Random(20261018)
    for n in range(0, n_max + 1):
        U = merge_sort_upper_bound(n)
        F = memoized_F(n) if n >= 2 else {(0,) * n: 0}
        for P in all_posets(n):
            e_exact = linear_extensions(P, n)
            # exactness of the subset-DP against permutation enumeration
            if e_exact != linear_extensions_bruteforce(P, n):
                fails += 1
                checks += 1
                if verbose:
                    print(f"  e mismatch n={n} {P}: dp={e_exact} "
                          f"brute={linear_extensions_bruteforce(P, n)}")
            # poly-space e_exceeds agrees with exact e for every cap that arises
            for d in range(0, U + 1):
                cap = 1 << d
                if e_exceeds(P, n, cap) != (e_exact > cap):
                    fails += 1
                    checks += 1
                    if verbose:
                        print(f"  e_exceeds mismatch n={n} {P} cap={cap}")
            if e_exceeds(P, n, 7) != (e_exact > 7):
                fails += 1
                checks += 1
                if verbose:
                    print(f"  e_exceeds(7) mismatch n={n} {P}")
            checks += 1
            if e_exact < factorial(width(P, n)):
                fails += 1
                if verbose:
                    print(f"  width!>e n={n} {P}: e={e_exact} w!={factorial(width(P,n))}")
            blocks = ordinal_sum_blocks(P, n)
            if blocks is not None:
                checks += 2
                if F_value(P, n, use_ordinal_sum=True) != F[P]:
                    fails += 1
                    if verbose:
                        print(f"  ord-sum F mismatch n={n} {P}")
                if sum(F_value(induced(P, b), len(b)) for b in blocks) != F[P]:
                    fails += 1
                    if verbose:
                        print(f"  ord-sum additivity fails n={n} {P}")
        if verbose:
            print(f"  n={n}: tier-1 checks={checks} failures={fails}")
        # TIER 2: decision equivalence
        if n <= min(n_max, 4):
            targets = list(all_posets(n))
        elif n == 5:
            targets = list(structured_posets(n).values())
            for _ in range(6):
                targets.append(random_poset(n, rng.choice([0.2, 0.4, 0.6]), rng))
        else:
            targets = []
        stats = {"checks": 0}
        for P in targets:
            fval = F[P]
            for d in range(0, min(fval + 2, U + 1)):
                fails += _decision_equivalence(P, n, d, node_cap, stats)
                checks += 1
        if verbose:
            print(f"  n={n}: decision checks={stats['checks']} "
                  f"cumulative failures={fails}")
    return fails


# ---------------------------------------------------------------------------
# Benchmarks: call counts and wall-clock, reference vs pruned.
# ---------------------------------------------------------------------------


CONFIGS = (
    "reference", "ext=width", "ext=enum", "ext=exact", "hi_base",
    "ext=enum+hi_base", "ext=enum+orbits", "ext=enum+orbits@0",
)


def _pruned_kw(cfg):
    kw = {}
    if "ext=width" in cfg:
        kw["ext"] = "width"
    elif "ext=enum" in cfg:
        kw["ext"] = "enum"
    elif "ext=exact" in cfg:
        kw["ext"] = "exact"
    if "hi_base" in cfg:
        kw["hi_base"] = True
    if "orbits" in cfg:
        kw["orbits"] = True
    if "orbits@0" in cfg:
        kw["orbit_max_depth"] = 0
    return kw


def bench_values(max_n=5, node_cap=20_000_000, configs=CONFIGS):
    """Compare S(n) binary-search cost across configurations."""
    known = {0: 0, 1: 0, 2: 1, 3: 3, 4: 5, 5: 7}
    rows = []
    for n in range(0, max_n + 1):
        U = merge_sort_upper_bound(n)
        row = {"n": n, "S": known[n], "U": U}
        for cfg in configs:
            if cfg == "reference":
                val, calls, dt, cap = compute_s(n, can_sort_reference)
            elif cfg == "value+ordsum":
                c = [0]
                t0 = time.perf_counter()
                val = F_value((0,) * n, n, use_ordinal_sum=True, counter=c)
                dt = time.perf_counter() - t0
                row[cfg] = (val, c[0], dt)
                continue
            else:
                val, calls, dt, cap = compute_s(
                    n, can_sort_pruned, node_cap=node_cap, **_pruned_kw(cfg))
            row[cfg] = (val, calls, dt, cap)
        rows.append(row)
    return rows


def print_bench_values(rows, configs):
    print("\n=== S(n) binary search: reference vs pruned (value, calls, seconds) ===")
    hdr = "n | S(n) | " + " | ".join(configs)
    print(hdr)
    print("-" * len(hdr))
    for row in rows:
        cells = [str(row["n"]), str(row["S"])]
        for cfg in configs:
            v, c, dt = row[cfg][0], row[cfg][1], row[cfg][2]
            if cfg == "value+ordsum":
                cells.append(f"{v} ({c}, {dt:.3f}s)")
            else:
                cap = row[cfg][3]
                cells.append(f"{v} ({c}, {dt:.3f}s)" + (" CAP" if cap else ""))
        print(" | ".join(cells))


def bench_adversarial(max_n=5, node_cap=2_000_000, configs=CONFIGS):
    """Worst-case per-(P,d) decision cost on structured posets + budgets near
    the F boundary (d = F-1 and d = F)."""
    print("\n=== Adversarial posets: worst-case decision cost ===")
    for n in range(2, max_n + 1):
        F = memoized_F(n)
        for name, P in structured_posets(n).items():
            fval = F[P]
            for d in sorted({max(0, fval - 1), fval}):
                c_ref = [0]
                t0 = time.perf_counter()
                r_ref, cap_ref = can_sort_reference(P, n, d, c_ref, node_cap)
                dt_ref = time.perf_counter() - t0
                print(f"n={n} {name} F={fval} d={d}: "
                      f"reference calls={c_ref[0]} {dt_ref:.3f}s")
                for cfg in configs:
                    if cfg in ("reference", "value+ordsum"):
                        continue
                    cq = [0]
                    t0 = time.perf_counter()
                    r_q, cap_q = can_sort_pruned(
                        P, n, d, cq, node_cap, **_pruned_kw(cfg))
                    dt_q = time.perf_counter() - t0
                    match = "OK" if (r_q == r_ref and not cap_q and not cap_ref) \
                        else "MISMATCH"
                    print(f"    {cfg:20s} calls={cq[0]:>8} {dt_q:.3f}s  {match}")


def bench_ordinal_sum(max_n=5):
    """Ordinal-sum allocation micro-benchmark.

    For every genuine ordinal-sum poset P = A (+) B with n <= max_n, compare
    F(P) computed (a) by the plain DFS and (b) by the allocation F(A) + F(B).
    Both must agree with the memoized F (additivity cross-check).  The antichain
    root used for S(n) is series-prime, so allocation does NOT apply there; its
    benefit is on ordinal-sum substates.
    """
    print("\n=== Ordinal-sum allocation: F(P) on ordinal-sum posets ===")
    print("n | poset | blocks | F plain (calls) | F alloc (calls) | memoized | match")
    for n in range(2, max_n + 1):
        F = memoized_F(n)
        shown = 0
        for P in all_posets(n):
            blocks = ordinal_sum_blocks(P, n)
            if blocks is None or shown >= 4:
                continue
            shown += 1
            c_plain = [0]
            f_plain = F_value(P, n, use_ordinal_sum=False, counter=c_plain)
            c_alloc = [0]
            f_alloc = F_value(P, n, use_ordinal_sum=True, counter=c_alloc)
            match = (f_plain == f_alloc == F[P])
            print(f"{n} | {P} | {[len(b) for b in blocks]} | "
                  f"{f_plain} ({c_plain[0]}) | {f_alloc} ({c_alloc[0]}) | "
                  f"{F[P]} | {'OK' if match else 'MISMATCH'}")


# ---------------------------------------------------------------------------
# Driver.
# ---------------------------------------------------------------------------


def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("--verify", action="store_true",
                    help="exhaustively verify soundness (n <= 5)")
    ap.add_argument("--max-n", type=int, default=5)
    ap.add_argument("--node-cap", type=int, default=20_000_000)
    ap.add_argument("--configs", type=str, default=",".join(CONFIGS))
    ap.add_argument("--skip-adversarial", action="store_true")
    args = ap.parse_args()
    configs = tuple(c for c in args.configs.split(",") if c)

    if args.verify:
        print("=== Exhaustive soundness verification (n <= %d) ===" % args.max_n)
        fails = verify(args.max_n, args.node_cap)
        print(f"\nTOTAL FAILURES: {fails}  ({'ALL SOUND' if fails == 0 else 'UNSOUND'})")
        if fails:
            return 1

    rows = bench_values(args.max_n, args.node_cap, configs)
    print_bench_values(rows, configs)
    if not args.skip_adversarial:
        bench_adversarial(args.max_n, args.node_cap, configs)
    bench_ordinal_sum(args.max_n)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
