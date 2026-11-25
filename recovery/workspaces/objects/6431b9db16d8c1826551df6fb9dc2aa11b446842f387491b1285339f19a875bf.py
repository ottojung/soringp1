#!/usr/bin/env python3
"""Independent targeted completeness audit for the n=12 T(4) residual.

Enumerate only fixed-natural-extension prefixes with at most 12 linear
extensions. Exact prefix extensions are updated by inserting the new largest
label into every legal position. Since extension counts never decrease, a
prefix exceeding 12 cannot lead to an e=12 target. The final q=11 acyclic
incomparability graph on 12 vertices is automatically a tree (and connected).
"""

import json
from functools import lru_cache
from pathlib import Path


N = 12
Q_MAX = 11
ROOT = Path(__file__).resolve().parents[2]


def transitive_column(Q, k, incomparable):
    """Check all new transitivity triples whose largest label is k."""
    for i in range(k):
        if not ((incomparable >> i) & 1):
            continue
        for j in range(i + 1, k):
            if not ((Q[j] >> i) & 1) and not ((incomparable >> j) & 1):
                return False
    return True


def acyclic_after_column(Q, k, incomparable):
    """Check that adding this incomparability column creates no graph cycle."""
    parent = list(range(k + 1))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    for v in range(k):
        bits = Q[v]
        while bits:
            bit = bits & -bits
            bits -= bit
            i = bit.bit_length() - 1
            a, b = find(i), find(v)
            if a != b:
                parent[a] = b

    bits = incomparable
    while bits:
        bit = bits & -bits
        bits -= bit
        i = bit.bit_length() - 1
        a, b = find(i), find(k)
        if a == b:
            return False
        parent[a] = b
    return True


def insert_new_largest(extensions, k, incomparable):
    """Exactly extend the prefix's linear extensions by label k."""
    predecessors = [i for i in range(k) if not ((incomparable >> i) & 1)]
    result = []
    for word in extensions:
        # The new label must be inserted after every predecessor. Inserting
        # after the last such predecessor is sufficient; all other positions
        # from there through the end are legal.
        first_legal = max((word.index(i) + 1 for i in predecessors), default=0)
        for position in range(first_legal, k + 1):
            result.append(word[:position] + (k,) + word[position:])
            if len(result) > 12:
                return None
    return result


def enumerate_targets():
    nodes = [0] * (N + 1)
    extension_prunes = [0] * (N + 1)
    targets = {}

    def visit(k, q, Q, extensions):
        nodes[k] += 1
        if k == N:
            if q == Q_MAX and len(extensions) == 12:
                targets[tuple(Q)] = tuple(extensions)
            return

        for column in range(1 << k):
            edge_count = column.bit_count()
            if q + edge_count > Q_MAX:
                continue
            if not transitive_column(Q, k, column):
                continue
            if not acyclic_after_column(Q, k, column):
                continue

            next_extensions = insert_new_largest(extensions, k, column)
            if next_extensions is None:
                extension_prunes[k + 1] += 1
                continue
            visit(k + 1, q + edge_count, Q + [column], next_extensions)

    visit(0, 0, [], [()])
    return targets, nodes, extension_prunes


def minimax(extensions):
    e = len(extensions)
    full = (1 << e) - 1
    splits = []
    n = len(extensions[0])
    for i in range(n):
        for j in range(i + 1, n):
            mask = sum(
                1 << r
                for r, word in enumerate(extensions)
                if word.index(i) < word.index(j)
            )
            if mask and mask != full:
                splits.append(mask)

    @lru_cache(None)
    def depth(states):
        if states & (states - 1) == 0:
            return 0
        return 1 + min(
            max(depth(states & mask), depth(states & ~mask))
            for mask in splits
            if states & mask and states & ~mask
        )

    return depth(full)


def main():
    targets, nodes, extension_prunes = enumerate_targets()
    saved = json.loads((ROOT / "data" / "t4-threshold-candidates.json").read_text())
    saved12 = {tuple(row["Q"]): row for row in saved if row["n"] == N}

    assert len(targets) == 12, len(targets)
    assert set(targets) == set(saved12), "n=12 fixed-extension candidate sets differ"
    for Q, extensions in targets.items():
        row = saved12[Q]
        assert set(extensions) == {tuple(word) for word in row["ext"]}, Q
        assert minimax(extensions) == row["F"] == 4, Q

    print("prefix nodes by depth:", nodes)
    print("extension-count prunes by next depth:", extension_prunes)
    print("target n=12 representations:", len(targets))
    print("saved n=12 representations:", len(saved12))
    print("complete Q sets and extension sets match; every F(P)=4")


if __name__ == "__main__":
    main()
