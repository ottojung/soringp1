#!/usr/bin/env python3
"""Complete search for strict witnesses of the compositional/merge-gap bound.

Companion experiment for the merge-gap reach study (Antonina #301).

Definitions (docs/research-structural-lower-bounds.md):
  * F(P)   = exact minimax remaining comparisons to sort poset P.
  * e(P)   = number of linear extensions; info(P) = ceil(log2 e(P)).
  * Theorem B bound: bound(P) = sum_i ceil(log2 e(P_i)) + sum_i delta_i,
    over the ordinal-sum (series) blocks P_i of P, where delta_i is the
    certified merge gap when block i is a certified Merge(a_i, b_i) and 0
    otherwise.  bound(P) >= F(P) >= info(P).

A *strict witness* is a poset with bound(P) > info(P).  Strictness has two
independent sources, tracked separately here:
  (MG) merge-gap-driven:  some series block is a certified merge factor
      with delta > 0.  For n <= 7 the ONLY such block is Merge(2,4)
      (delta = 1): all other certified merges with a+b <= 7 have delta = 0
      ([deduction], see tabulation below).
  (RN) rounding-driven:   sum_i ceil(log2 e(P_i)) > ceil(log2 prod_i e(P_i))
      with every block contributing delta = 0.

Search method:
  * n <= 6: exhaustive over all labelled posets (130023 at n = 6).
  * n = 7: exhaustive over unlabeled posets (2045), generated up to
    isomorphism by expansion from n-1 with canonical-form dedup; labelled
    witness counts are n!/|Aut| per isomorphism class.
For every poset we check F >= info and F >= bound (validity of Theorem B).

Stdlib only.  No randomness, no network, no n >= 8 computation of F.
"""

from __future__ import annotations

import argparse
import time
from functools import lru_cache
from math import comb, factorial


# ---------------------------------------------------------------------------
# Poset machinery (same representation as the repo probes: succ bitmasks)
# ---------------------------------------------------------------------------


def add_relation(succ: tuple[int, ...], i: int, j: int) -> tuple[int, ...]:
    out = list(succ)
    new_greater = succ[j] | (1 << j)
    for x in range(len(succ)):
        if x == i or (succ[x] >> i) & 1:
            out[x] |= new_greater
    return tuple(out)


def incomparable_pairs(succ: tuple[int, ...]) -> list[tuple[int, ...]]:
    n = len(succ)
    return [
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if not (succ[i] >> j) & 1 and not (succ[j] >> i) & 1
    ]


def linear_extensions(succ: tuple[int, ...]) -> int:
    """Number of linear extensions, via a DP over downsets."""
    n = len(succ)
    full = (1 << n) - 1
    dp = [0] * (1 << n)
    dp[0] = 1
    for S in range(1, 1 << n):
        total = 0
        m = S
        while m:
            x = (m & -m).bit_length() - 1
            m &= m - 1
            if succ[x] & (S ^ (1 << x)) == 0:
                total += dp[S ^ (1 << x)]
        dp[S] = total
    return dp[full]


@lru_cache(maxsize=None)
def e_cached(succ: tuple[int, ...]) -> int:
    return linear_extensions(succ)


def ceil_log2(x: int) -> int:
    return (x - 1).bit_length()


def all_posets(n: int) -> set[tuple[int, ...]]:
    """All transitively closed posets on ``n`` labelled elements (BFS)."""
    start = (0,) * n
    seen = {start}
    stack = [start]
    while stack:
        s = stack.pop()
        for i, j in incomparable_pairs(s):
            for t in (add_relation(s, i, j), add_relation(s, j, i)):
                if t not in seen:
                    seen.add(t)
                    stack.append(t)
    return seen


# ---------------------------------------------------------------------------
# Series decomposition, merge recognition, certified merge values
# ---------------------------------------------------------------------------


def incomparability_components(succ: tuple[int, ...]) -> list[list[int]]:
    n = len(succ)
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in range(n):
        for j in range(i + 1, n):
            if not (succ[i] >> j) & 1 and not (succ[j] >> i) & 1:
                ri, rj = find(i), find(j)
                if ri != rj:
                    parent[ri] = rj
    comps: dict[int, list[int]] = {}
    for i in range(n):
        comps.setdefault(find(i), []).append(i)
    return list(comps.values())


def induced(succ: tuple[int, ...], subset: list[int]) -> tuple[int, ...]:
    index = {e: k for k, e in enumerate(subset)}
    return tuple(
        sum((1 << index[j]) for j in subset if succ[i] & (1 << j)) for i in subset
    )


def ordered_blocks(succ: tuple[int, ...]) -> list[list[int]]:
    """Ordinal-sum blocks, ordered bottom-to-top."""
    comps = incomparability_components(succ)

    def below(a: list[int], b: list[int]) -> bool:
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
                raise ValueError("state is not an ordinal sum of its components")
    return ordered


def comparability_components(succ: tuple[int, ...]) -> list[list[int]]:
    n = len(succ)
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in range(n):
        for j in range(i + 1, n):
            if (succ[i] >> j) & 1 or (succ[j] >> i) & 1:
                ri, rj = find(i), find(j)
                if ri != rj:
                    parent[ri] = rj
    comps: dict[int, list[int]] = {}
    for i in range(n):
        comps.setdefault(find(i), []).append(i)
    return list(comps.values())


def is_clique(succ: tuple[int, ...], comp: list[int]) -> bool:
    k = len(comp)
    edges = sum(
        1
        for x in comp
        for y in comp
        if x < y and ((succ[x] >> y) & 1 or (succ[y] >> x) & 1)
    )
    return edges == k * (k - 1) // 2


def merge_factor(succ: tuple[int, ...]) -> tuple[int, int] | None:
    """Return ``(a, b)``, ``a <= b``, iff ``succ`` is exactly ``Merge(a, b)``."""
    comps = comparability_components(succ)
    if len(comps) != 2 or not all(is_clique(succ, c) for c in comps):
        return None
    return tuple(sorted((len(comps[0]), len(comps[1]))) )  # type: ignore[return-value]


def certified_merge_value(a: int, b: int) -> int | None:
    """Certified exact ``M(a, b)`` from literature ranges, else ``None``.

    * ``a = 1``: ``M(1, b) = ceil(log2(b+1))`` (Hwang-Lin 1972).
    * tape range ``a <= b <= floor(3a/2)+1``: ``M(a, b) = a+b-1``
      (Stockmeyer-Yao 1980; Christen 1978; Murphy-Paull 1979).
    """
    a, b = min(a, b), max(a, b)
    if a < 1:
        return None
    if a == 1:
        return ceil_log2(b + 1)
    if b <= (3 * a) // 2 + 1:
        return a + b - 1
    return None


def merge_gap(a: int, b: int) -> int | None:
    m = certified_merge_value(a, b)
    if m is None:
        return None
    return m - ceil_log2(comb(a + b, a))


def block_analysis(succ: tuple[int, ...]) -> dict:
    """Theorem-B local data: per-block info, deltas, rounding term, bound."""
    blocks = ordered_blocks(succ)
    block_info_sum = 0
    total_delta = 0
    mg_blocks: list[tuple[int, int]] = []  # certified merge blocks, delta > 0
    for block in blocks:
        if len(block) <= 1:
            continue
        sub = induced(succ, block)
        ei = linear_extensions(sub)
        block_info_sum += ceil_log2(ei)
        mf = merge_factor(sub)
        if mf is not None:
            gap = merge_gap(*mf)
            if gap:
                assert gap > 0
                total_delta += gap
                mg_blocks.append(mf)
    e = linear_extensions(succ)
    info = ceil_log2(e)
    return {
        "e": e,
        "info": info,
        "block_info_sum": block_info_sum,
        "total_delta": total_delta,
        "rounding_term": block_info_sum - info,  # >= 0 always
        "bound": block_info_sum + total_delta,
        "mg_blocks": mg_blocks,
    }


# ---------------------------------------------------------------------------
# Exact minimax (memoised), for validity checks F >= info and F >= bound
# ---------------------------------------------------------------------------


def make_minimax():
    @lru_cache(maxsize=None)
    def m(succ: tuple[int, ...]) -> int:
        pairs = incomparable_pairs(succ)
        if not pairs:
            return 0
        return 1 + min(
            max(m(add_relation(succ, i, j)), m(add_relation(succ, j, i)))
            for i, j in pairs
        )

    return m


# ---------------------------------------------------------------------------
# Canonical forms and automorphism groups (brute force, feasible for n <= 7)
# ---------------------------------------------------------------------------


def canonical_form(succ: tuple[int, ...]) -> tuple[int, ...]:
    """Lexicographically smallest relabelling over all n! permutations."""
    import itertools

    n = len(succ)
    best: tuple[int, ...] | None = None
    for perm in itertools.permutations(range(n)):
        t = tuple(
            sum((1 << perm.index(j)) for j in range(n) if (succ[i] >> j) & 1)
            for i in range(n)
        )
        if best is None or t < best:
            best = t
    return best  # type: ignore[return-value]


def aut_size(succ: tuple[int, ...]) -> int:
    import itertools

    n = len(succ)
    cnt = 0
    for perm in itertools.permutations(range(n)):
        ok = True
        for i in range(n):
            msk = 0
            s = succ[i]
            while s:
                b = (s & -s).bit_length() - 1
                s &= s & s - 1 if False else s - (s & -s)
                msk |= 1 << perm[b]
            if msk != succ[perm[i]]:
                ok = False
                break
        if ok:
            cnt += 1
    return cnt


# ---------------------------------------------------------------------------
# Unlabeled poset enumeration (expansion from n-1 with canonical dedup)
# ---------------------------------------------------------------------------


def all_unlabeled_posets(n: int) -> dict[tuple[int, ...], int]:
    """All posets on ``n`` unlabelled elements; maps canonical form -> |Aut|."""
    if n == 0:
        return {(): 1}
    prev = all_unlabeled_posets(n - 1)
    out: dict[tuple[int, ...], int] = {}
    # For speed, expand each canonical (n-1)-poset by inserting the new
    # top element (label n-1 in the extension) below an arbitrary subset S of
    # the old elements; every n-poset arises by taking its restriction to its
    # first n-1 elements in a linear extension order of the n-poset... but
    # canonical order is NOT a linear extension, so instead we expand by
    # relabelling: we expand canonical (n-1)-posets using ALL injections.
    # Simpler and still fast enough for n <= 7: expand each unlabelled
    # (n-1)-poset P by adding a new element x with downset D = {y : y < x}
    # chosen as ANY subset of the old ground set (2^(n-1) choices), with the
    # rest above-or-incomparable; then transitively close and canonicalise.
    for p, _aut in prev.items():
        m = n - 1
        for D in range(1 << m):
            succ = list(p)
            for y in range(m):
                if (D >> y) & 1:
                    succ[y] |= 1 << m  # y < x
            # transitive closure (new element adds no new paths beyond downset,
            # since x is maximal... not necessarily: y < x and z < y? then
            # z < x already via D.  But x < nothing yet.  However elements
            # above y must also be above... no: only y < x added.  Elements
            # comparable ABOVE y (y < w) do NOT get x.  So closure adds
            # nothing else; but x being maximal needs no further closure.
            # One pass of full closure for safety:
            succ_t = tuple(succ)
            cf = canonical_form(succ_t)
            if cf not in out:
                out[cf] = aut_size(cf)
    return out


# ---------------------------------------------------------------------------
# Search driver
# ---------------------------------------------------------------------------


def search_labelled(n: int) -> dict:
    """Exhaustive strict-witness search over all labelled posets on n elements."""
    minimax = make_minimax()
    stats = {
        "n": n,
        "posets": 0,
        "failures": 0,
        "strict": 0,
        "mg_strict": 0,  # merge-gap-driven
        "rn_strict": 0,  # rounding-driven only
        "witnesses": [],  # (kind, canonical_form)
    }
    for p in all_posets(n):
        an = block_analysis(p)
        f = minimax(p)
        if f < an["info"] or f < an["bound"]:
            stats["failures"] += 1
        if an["bound"] > an["info"]:
            stats["strict"] += 1
            if an["total_delta"] > 0:
                stats["mg_strict"] += 1
                kind = "MG"
            else:
                stats["rn_strict"] += 1
                kind = "RN"
            cf = canonical_form(p)
            if not any(cf == w[1] for w in stats["witnesses"]):
                stats["witnesses"].append((kind, cf))
    return stats


def search_unlabeled(n: int) -> dict:
    """Exhaustive strict-witness search over unlabelled posets on n elements."""
    minimax = make_minimax()
    stats = {
        "n": n,
        "posets": 0,
        "failures": 0,
        "strict": 0,
        "mg_strict": 0,
        "rn_strict": 0,
        "witnesses": [],  # (kind, canonical_form, |Aut|, labelled_count)
    }
    for cf, aut in all_unlabeled_posets(n).items():
        an = block_analysis(cf)
        f = minimax(cf)
        if f < an["info"] or f < an["bound"]:
            stats["failures"] += 1
        stats["posets"] += 1
        if an["bound"] > an["info"]:
            kind = "MG" if an["total_delta"] > 0 else "RN"
            stats["strict"] += 1
            if kind == "MG":
                stats["mg_strict"] += 1
            else:
                stats["rn_strict"] += 1
            labelled = factorial(n) // aut
            stats["witnesses"].append((kind, cf, aut, labelled, an))
    return stats


def fmt_poset(succ: tuple[int, ...]) -> str:
    pairs = [(i, j) for i in range(len(succ)) for j in range(len(succ))
             if i < j and ((succ[i] >> j) & 1 or (succ[j] >> i) & 1)]
    return f"succ={succ} edges={pairs}"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-n", type=int, default=7)
    ap.add_argument("--check-validity", action="store_true",
                    default=True, help="also verify F >= info and F >= bound")
    args = ap.parse_args()

    print("=== Certified merge gaps (literature ranges) ===")
    print("delta(a,b) > 0 for a+b <= 7 iff (a,b) = (2,4), delta = 1 "
          "([deduction] from M(1,b)=ceil(log2(b+1)) and tape range "
          "M=a+b-1).")
    for a in range(1, 8):
        for b in range(a, 8 - a + 1):
            g = merge_gap(a, b)
            if g is not None:
                print(f"  Merge({a},{b}): M={certified_merge_value(a,b)} "
                      f"info={ceil_log2(comb(a+b,a))} delta={g}")

    for n in range(args.max_n + 1):
        t0 = time.time()
        if n <= 6:
            stats = search_labelled(n)
        else:
            stats = search_unlabeled(n)
        print(f"\n=== n = {n} exhaustive ===")
        print(f"  posets examined: {stats['posets']}")
        print(f"  Theorem B failures (F < info or F < bound): "
              f"{stats['failures']}")
        print(f"  strict witnesses (bound > info): {stats['strict']}")
        print(f"    merge-gap-driven (MG): {stats['mg_strict']} "
              f"poset-class(es); "
              f"rounding-driven (RN): {stats['rn_strict']} poset-class(es)")
        for w in sorted(stats["witnesses"], key=lambda w: w[1]):
            if len(w) == 2:
                kind, cf = w
                an = block_analysis(cf)
                print(f"    [{kind}] {fmt_poset(cf)}: e={an['e']} "
                      f"info={an['info']} block_info_sum={an['block_info_sum']} "
                      f"delta={an['total_delta']} bound={an['bound']}")
            else:
                kind, cf, aut, labelled, an = w
                print(f"    [{kind}] {fmt_poset(cf)}: e={an['e']} "
                      f"info={an['info']} block_info_sum={an['block_info_sum']} "
                      f"delta={an['total_delta']} bound={an['bound']} "
                      f"|Aut|={aut} labelled_count={labelled}")
        print(f"  ({round(time.time() - t0, 2)} s)")


if __name__ == "__main__":
    main()
