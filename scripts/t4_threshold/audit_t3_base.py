#!/usr/bin/env python3
"""Independent finite audit of the all-finite T(3) = 7 base.

Enumerate connected incomparability graphs as edge subsets in a fixed natural
linear extension, rather than using the column-recursive T(4) generator.
"""

from collections import Counter
from functools import lru_cache
from itertools import combinations


def connected(n, edges):
    adjacency = [0] * n
    for i, j in edges:
        adjacency[i] |= 1 << j
        adjacency[j] |= 1 << i
    seen = 1
    todo = [0]
    while todo:
        i = todo.pop()
        new = adjacency[i] & ~seen
        while new:
            bit = new & -new
            new -= bit
            j = bit.bit_length() - 1
            seen |= 1 << j
            todo.append(j)
    return seen == (1 << n) - 1


def predecessors_from_incomparabilities(n, edges):
    """Return None unless the natural-order encoding is transitive."""
    incomparable = [[False] * n for _ in range(n)]
    for i, j in edges:
        incomparable[i][j] = incomparable[j][i] = True

    # In the fixed natural extension, comparabilities point from smaller to
    # larger labels. Reject exactly the forbidden transitivity triple i<j<k.
    for i in range(n):
        for j in range(i + 1, n):
            if incomparable[i][j]:
                continue
            for k in range(j + 1, n):
                if not incomparable[j][k] and incomparable[i][k]:
                    return None

    predecessors = [0] * n
    for hi in range(n):
        for lo in range(hi):
            if not incomparable[lo][hi]:
                predecessors[hi] |= 1 << lo
    return predecessors


def linear_extensions(predecessors, n, cutoff=8):
    """Enumerate extensions, stopping at 8 because only e<=7 is retained."""
    full = (1 << n) - 1
    result = []

    def visit(done, word):
        if len(result) >= cutoff:
            return
        if done == full:
            result.append(tuple(word))
            return
        for v in range(n):
            if not ((done >> v) & 1) and not (predecessors[v] & ~done):
                visit(done | (1 << v), word + [v])
                if len(result) >= cutoff:
                    return

    visit(0, [])
    return result


def minimax_depth(extensions, n):
    count = len(extensions)
    full = (1 << count) - 1
    splits = []
    for i in range(n):
        for j in range(i + 1, n):
            mask = sum(
                1 << k
                for k, extension in enumerate(extensions)
                if extension.index(i) < extension.index(j)
            )
            if mask and mask != full:
                splits.append(mask)

    @lru_cache(None)
    def depth(states):
        if states & (states - 1) == 0:
            return 0
        return 1 + min(
            max(depth(states & split), depth(states & ~split))
            for split in splits
            if states & split and states & ~split
        )

    return depth(full)


def witness_extensions(successors):
    n = len(successors)
    for i in range(n):
        for j in range(n):
            if (successors[i] >> j) & 1:
                for k in range(n):
                    if (successors[j] >> k) & 1:
                        assert (successors[i] >> k) & 1
    predecessors = [0] * n
    for lower, greater_mask in enumerate(successors):
        for higher in range(n):
            if (greater_mask >> higher) & 1:
                predecessors[higher] |= 1 << lower
    return linear_extensions(predecessors, n, cutoff=9)


def main():
    examined = 0
    connected_count = 0
    histogram = Counter()
    connected_small_e = 0
    bad = []

    for n in range(2, 8):
        pairs = list(combinations(range(n), 2))
        for edge_count in range(n - 1, min(6, len(pairs)) + 1):
            for edges in combinations(pairs, edge_count):
                examined += 1
                if not connected(n, edges):
                    continue
                connected_count += 1
                predecessors = predecessors_from_incomparabilities(n, edges)
                if predecessors is None:
                    continue
                extensions = linear_extensions(predecessors, n)
                if len(extensions) > 7:
                    continue
                connected_small_e += 1
                depth = minimax_depth(extensions, n)
                histogram[(len(extensions), depth)] += 1
                if depth > 3:
                    bad.append((n, edges, len(extensions), depth))

    # Independent sharpness witness from the project's successor-mask record.
    witness = witness_extensions((0, 0, 1, 3, 7))
    witness_depth = minimax_depth(witness, 5)
    assert len(witness) == 8 and witness_depth == 4
    assert not bad, bad[:1]
    print("edge subsets examined:", examined)
    print("connected edge subsets:", connected_count)
    print("connected posets with e<=7:", connected_small_e)
    print("(e,F) histogram:", dict(sorted(histogram.items())))
    print("e=8 sharpness witness: e=8, F=", witness_depth)


if __name__ == "__main__":
    main()
