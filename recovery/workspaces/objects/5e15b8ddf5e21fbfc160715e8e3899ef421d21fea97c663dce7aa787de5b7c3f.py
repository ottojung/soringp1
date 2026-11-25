#!/usr/bin/env python3
"""Core census behind the finite comparison thresholds ``T(r)``.

Status: **experiment**, with a paper proof for the structural part (see
``docs/research-core-threshold.md``). This is not a Lean file and not a
complexity-class result.

Definitions (``docs/problem.md``): ``e(P)`` is the number of linear extensions
of a finite poset ``P`` and ``m(P)`` the exact number of further comparisons
needed to sort every linear extension. ``T(r)`` is the largest ``E`` such that
every poset with ``e(P) <= E`` has ``m(P) <= r``.

Two structural facts make a finite census of *cores* sufficient:

* deleting an element comparable with every other element does not change
  ``e`` or ``m``, so every poset reduces to a **core** (no element comparable
  with all others) with the same ``(e, m)``;
* every core is built from the 2-antichain by (i) adjoining a new maximal
  element above a proper ideal and (ii) ordinal sums, and every core has
  ``e(P) >= |P|``.

Hence cores with ``e <= E`` have at most ``E`` elements and can be generated
level by level. Correctness of the generator is argued in the note, not here.

Usage::

    python3 scripts/core_threshold_census.py --E 33 --h 6

Exit status is 0 when every generated core is sorted within ``h`` comparisons.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
from itertools import permutations

# ---------------------------------------------------------------------------
# Poset representation: up[i] is the bitmask of elements strictly above i.
# The relation is transitively closed and irreflexive.
# ---------------------------------------------------------------------------

FIB = [0, 1, 1]
while len(FIB) < 24:
    FIB.append(FIB[-1] + FIB[-2])


def predecessors(up):
    n = len(up)
    pre = [0] * n
    for a in range(n):
        q = up[a]
        while q:
            bit = q & -q
            q -= bit
            pre[bit.bit_length() - 1] |= 1 << a
    return pre


def is_core(up):
    """True when no element is comparable with every other element."""
    n = len(up)
    pre = predecessors(up)
    for a in range(n):
        if pre[a].bit_count() + up[a].bit_count() == n - 1:
            return False
    return True


def _refine(up, colors):
    n = len(up)
    pre = predecessors(up)
    while True:
        sig = []
        for a in range(n):
            counts = {}
            for b in range(n):
                if a == b:
                    continue
                if (up[a] >> b) & 1:
                    rel = 1
                elif (pre[a] >> b) & 1:
                    rel = 2
                else:
                    rel = 0
                key = (rel, colors[b])
                counts[key] = counts.get(key, 0) + 1
            sig.append((colors[a], tuple(sorted(counts.items()))))
        labels = {v: i for i, v in enumerate(sorted(set(sig)))}
        new = tuple(labels[x] for x in sig)
        if new == colors:
            return new
        colors = new


def _canon(up, colors):
    n = len(up)
    colors = _refine(up, colors)
    cells = {}
    for v, c in enumerate(colors):
        cells.setdefault(c, []).append(v)
    branch = next((cells[c] for c in sorted(cells) if len(cells[c]) > 1), None)
    if branch is None:
        order = [v for c in sorted(cells) for v in cells[c]]
        inv = [0] * n
        for i, v in enumerate(order):
            inv[v] = i
        out = [0] * n
        for i, v in enumerate(order):
            q = up[v]
            while q:
                bit = q & -q
                q -= bit
                out[i] |= 1 << inv[bit.bit_length() - 1]
        return tuple(out)
    best = None
    new_color = max(colors) + 1
    for v in branch:
        trial = list(colors)
        trial[v] = new_color
        got = _canon(up, tuple(trial))
        if best is None or got < best:
            best = got
    return best


@lru_cache(maxsize=None)
def canonical(up):
    """Isomorphism-canonical relabelling of ``up`` (validated on n <= 9)."""
    return _canon(up, tuple([0] * len(up)))


def ideals(up, order):
    """All ideals (down-sets) of ``up``, enumerated along one linear extension."""
    pre = predecessors(up)
    n = len(up)
    out = []

    def rec(i, mask):
        if i == n:
            out.append(mask)
            return
        rec(i + 1, mask)  # leave out
        x = order[i]
        if pre[x] & ~mask == 0:
            rec(i + 1, mask | (1 << x))

    rec(0, 0)
    return out


# ---------------------------------------------------------------------------
# Core generation.  A core is carried as (up, extensions); extensions are
# tuples of bytes, one permutation of the labels per linear extension.  They
# are always derived structurally, never by enumerating n! permutations, so
# large sparse cores stay cheap.
# ---------------------------------------------------------------------------


def antichain2():
    return (0, 0), (b"\x00\x01", b"\x01\x00")


def antichain3():
    perms = tuple(bytes(p) for p in permutations(range(3)))
    return (0, 0, 0), perms


def add_maximal(up, exts, ideal):
    """Adjoin a new maximal element above ``ideal``; return (up, exts)."""
    n = len(up)
    up2 = list(up)
    up2.append(0)
    m = ideal
    while m:
        bit = m & -m
        m -= bit
        up2[bit.bit_length() - 1] |= 1 << n
    new_exts = []
    for ext in exts:
        start = -1
        m = ideal
        while m:
            bit = m & -m
            m -= bit
            pos = ext.index(bit.bit_length() - 1)
            if pos > start:
                start = pos
        for slot in range(start + 1, n + 1):
            new_exts.append(ext[:slot] + bytes([n]) + ext[slot:])
    return tuple(up2), tuple(new_exts)


def ordinal_sum(left, right):
    up_a, ex_a = left
    up_b, ex_b = right
    a = len(up_a)
    b = len(up_b)
    shift = (1 << b) - 1
    up = [up_a[i] | (shift << a) for i in range(a)]
    up += [(up_b[j] << a) for j in range(b)]
    exts = tuple(la + bytes(x + a for x in lb) for la in ex_a for lb in ex_b)
    return tuple(up), exts


def enumerate_cores(E):
    """All core isomorphism classes with e <= E, keyed by level."""
    levels = {2: {canonical(antichain2()[0]): antichain2()},
              3: {canonical(antichain3()[0]): antichain3()}}
    for ideal in ideals(antichain2()[0], (0, 1))[:-1]:
        up, exts = add_maximal(*antichain2(), ideal)
        levels[3][canonical(up)] = (up, exts)
    for n in range(4, E + 1):
        current = {}
        for up, exts in levels[n - 1].values():
            order = tuple(exts[0])
            full = (1 << (n - 1)) - 1
            for ideal in ideals(up, order):
                if ideal == full:
                    continue
                get = add_maximal(up, exts, ideal)
                if len(get[1]) > E or canonical(get[0]) in current:
                    continue
                current[canonical(get[0])] = get
        for p in range(2, n - 1):
            for left in levels[p].values():
                for right in levels[n - p].values():
                    if len(left[1]) * len(right[1]) > E:
                        continue
                    up, exts = ordinal_sum(left, right)
                    current.setdefault(canonical(up), (up, exts))
        levels[n] = current
    return {n: v for n, v in levels.items() if v}


# ---------------------------------------------------------------------------
# Exact bounded minimax decision on the comparison game.
# ---------------------------------------------------------------------------


@lru_cache(maxsize=None)
def sortable(exts, budget):
    """Can every permutation in ``exts`` be sorted with ``budget`` comparisons?

    A state is its surviving linear extensions; a comparison splits them into
    two states; an outcome is legal only when both sides are nonempty.
    """
    if len(exts) <= 1:
        return True
    if budget <= 0 or (len(exts) - 1).bit_length() > budget:
        return False
    n = len(exts[0])
    ranks = [[0] * n for _ in exts]
    for r, ext in enumerate(exts):
        for pos, x in enumerate(ext):
            ranks[r][x] = pos
    for a in range(n - 1):
        for b in range(a + 1, n):
            left, right = [], []
            for r, ext in enumerate(exts):
                (left if ranks[r][a] < ranks[r][b] else right).append(ext)
            if not left or not right:
                continue
            if max(len(left), len(right)) > (1 << (budget - 1)):
                continue
            if sortable(tuple(left), budget - 1) and sortable(tuple(right), budget - 1):
                return True
    return False


def staircase(n):
    """Staircase poset with e = F(n+1) and m = n-1 (the threshold witness)."""
    return tuple(0 if i == 0 else (1 << (i - 1)) - 1 for i in range(n))


def extensions_by_permutation(up):
    n = len(up)
    pre = predecessors(up)
    out = []
    for perm in permutations(range(n)):
        pos = [0] * n
        for i, x in enumerate(perm):
            pos[x] = i
        ok = True
        for a in range(n):
            q = pre[a]
            while q:
                bit = q & -q
                q -= bit
                if pos[bit.bit_length() - 1] > pos[a]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(bytes(perm))
    return tuple(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--E", type=int, default=33, help="extension budget")
    ap.add_argument("--h", type=int, default=6, help="comparison budget to test")
    ap.add_argument("--levels", action="store_true", help="print per-level counts")
    args = ap.parse_args()

    levels = enumerate_cores(args.E)
    total = 0
    failures = []
    for n in sorted(levels):
        classes = levels[n]
        total += len(classes)
        if args.levels:
            print("n=%2d cores=%5d" % (n, len(classes)))
        for up, exts in classes.values():
            assert len(exts) <= args.E
            assert is_core(up), (n, len(exts))
            if not sortable(tuple(sorted(exts)), args.h):
                failures.append((n, len(exts), up))
    print("E=%d h=%d cores=%d failures=%d" % (args.E, args.h, total, len(failures)))
    for n, e, _ in failures[:10]:
        print("  FAILS n=%d e=%d" % (n, e))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
