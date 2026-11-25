#!/usr/bin/env python3
"""Independent reverse-label audit of the finite T(4) residual.

This review implementation does not import the candidate generator or either
candidate validator. It adds the smallest label first (reverse of the package's
column order), enumerates every legal incomparable-neighbor set under a fixed
natural extension, and directly evaluates the resulting extension-set game.
"""

import json
from functools import lru_cache
from itertools import combinations, permutations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SAVED = json.loads((ROOT / "data/t4-threshold-candidates.json").read_text())


def extensions(incomparables, n, cap=13):
    predecessors = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if not ((incomparables[i] >> j) & 1):
                predecessors[j] |= 1 << i
    full = (1 << n) - 1
    output = []

    def visit(done, word):
        if len(output) >= cap:
            return
        if done == full:
            output.append(tuple(word))
            return
        for x in range(n):
            if not ((done >> x) & 1) and not (predecessors[x] & ~done):
                visit(done | (1 << x), word + [x])

    visit(0, [])
    return output


def connected(incomparables, n):
    reached, todo = 1, [0]
    while todo:
        i = todo.pop()
        for j in range(n):
            if i == j:
                continue
            edge = (
                (incomparables[i] >> j) & 1
                if i < j
                else (incomparables[j] >> i) & 1
            )
            if edge and not ((reached >> j) & 1):
                reached |= 1 << j
                todo.append(j)
    return reached == (1 << n) - 1


def width(incomparables, n):
    best = 0
    for subset in range(1, 1 << n):
        size = subset.bit_count()
        if size <= best:
            continue
        if all(
            not ((subset >> i) & 1 and (subset >> j) & 1)
            or ((incomparables[i] >> j) & 1)
            for i in range(n)
            for j in range(i + 1, n)
        ):
            best = size
    return best


def minimax(extension_set, n):
    e = len(extension_set)
    full = (1 << e) - 1
    splits = []
    for i in range(n):
        for j in range(i + 1, n):
            mask = sum(
                1 << r
                for r, word in enumerate(extension_set)
                if word.index(i) < word.index(j)
            )
            if mask and mask != full:
                splits.append(mask)

    @lru_cache(None)
    def value(states):
        if states & (states - 1) == 0:
            return 0
        return 1 + min(
            max(value(states & mask), value(states & ~mask))
            for mask in splits
            if states & mask and states & ~mask
        )

    return value(full)


def edge_subset_audit_t3():
    """Separate exhaustive check of the connected e<=7 base."""
    examined = 0
    count = 0
    histogram = {}
    for n in range(2, 8):
        pairs = list(combinations(range(n), 2))
        for q in range(n - 1, min(6, len(pairs)) + 1):
            for chosen in combinations(pairs, q):
                examined += 1
                edges = set(chosen)
                # Connectedness of the incomparability graph.
                reached, todo = {0}, [0]
                while todo:
                    i = todo.pop()
                    for j in range(n):
                        if j not in reached and (min(i, j), max(i, j)) in edges:
                            reached.add(j)
                            todo.append(j)
                if len(reached) != n:
                    continue

                # The natural-order complement must be transitive.
                if any(
                    (i, j) not in edges
                    and (j, k) not in edges
                    and (i, k) in edges
                    for i in range(n)
                    for j in range(i + 1, n)
                    for k in range(j + 1, n)
                ):
                    continue

                predecessors = [0] * n
                for j in range(n):
                    for i in range(j):
                        if (i, j) not in edges:
                            predecessors[j] |= 1 << i
                full = (1 << n) - 1
                ext = []

                def generate(done, word):
                    if len(ext) >= 8:
                        return
                    if done == full:
                        ext.append(tuple(word))
                        return
                    for x in range(n):
                        if not ((done >> x) & 1) and not (predecessors[x] & ~done):
                            generate(done | (1 << x), word + [x])

                generate(0, [])
                if len(ext) > 7:
                    continue
                depth = minimax(ext, n)
                assert depth <= 3
                count += 1
                histogram[(len(ext), depth)] = histogram.get((len(ext), depth), 0) + 1

    assert examined == 62991 and count == 49
    return count, histogram


def audit_sharpness_witness():
    """Recheck the six-element e=13, F=5 boundary witness."""
    successors = (20, 16, 0, 23, 0, 22)
    n = len(successors)
    ext = []
    for word in permutations(range(n)):
        rank = [0] * n
        for position, element in enumerate(word):
            rank[element] = position
        if all(
            not ((successors[i] >> j) & 1) or rank[i] < rank[j]
            for i in range(n)
            for j in range(n)
        ):
            ext.append(word)
    assert len(ext) == 13 and minimax(ext, n) == 5
    return len(ext), minimax(ext, n)


def audit_t3_sharpness_witness():
    successors = (0, 0, 1, 3, 7)
    n = len(successors)
    ext = []
    for word in permutations(range(n)):
        rank = [0] * n
        for position, element in enumerate(word):
            rank[element] = position
        if all(
            not ((successors[i] >> j) & 1) or rank[i] < rank[j]
            for i in range(n)
            for j in range(n)
        ):
            ext.append(word)
    assert len(ext) == 8 and minimax(ext, n) == 4
    return len(ext), minimax(ext, n)


def encode(incomparables, n):
    # Candidate Q[j] stores earlier incomparable labels in bits of j.
    return tuple(
        sum(1 << i for i in range(j) if (incomparables[i] >> j) & 1)
        for j in range(n)
    )


def enumerate_residual(n, qmax):
    incomparables = [0] * n
    found = set()
    visited = 0

    def visit(k, q):
        nonlocal visited
        visited += 1
        if q > qmax:
            return
        if k < 0:
            if q < n - 1 or not connected(incomparables, n):
                return
            ext = extensions(incomparables, n)
            if (
                len(ext) not in (11, 12)
                or q > len(ext) - 1
                or width(incomparables, n) > 3
            ):
                return
            assert minimax(ext, n) == 4
            found.add(encode(incomparables, n))
            return

        # Every remaining edge has smaller endpoint at most k.
        if q + (k + 1) * (2 * n - k - 2) // 2 < n - 1:
            return

        # Choose incomparable neighbors of the new smallest label k.
        for mask in range(1 << (n - k - 1)):
            q_next = q + mask.bit_count()
            if q_next > qmax:
                continue

            # If k<j and j<l, transitivity requires k<l.
            valid = True
            for j in range(k + 1, n):
                if (mask >> (j - k - 1)) & 1:
                    continue
                for ell in range(j + 1, n):
                    j_ell_incomparable = (incomparables[j] >> ell) & 1
                    k_ell_incomparable = (mask >> (ell - k - 1)) & 1
                    if not j_ell_incomparable and k_ell_incomparable:
                        valid = False
                        break
                if not valid:
                    break
            if not valid:
                continue

            incomparables[k] = sum(
                1 << j
                for j in range(k + 1, n)
                if (mask >> (j - k - 1)) & 1
            )
            # Adding an element cannot decrease the extension count; prune
            # only when even the exact truncated count already exceeds 12.
            if len(extensions(incomparables, n)) <= 12:
                visit(k - 1, q_next)
            incomparables[k] = 0

    visit(n - 1, 0)
    return found, visited


def main():
    count_t3, hist_t3 = edge_subset_audit_t3()
    print(f"T(3) base: {count_t3} connected posets; histogram={dict(sorted(hist_t3.items()))}")
    print(f"T(3) sharpness witness (e,F)={audit_t3_sharpness_witness()}")
    print(f"sharpness witness (e,F)={audit_sharpness_witness()}")

    saved_small = {
        (row["n"], tuple(row["Q"])) for row in SAVED if row["n"] <= 11
    }
    saved_12 = {tuple(row["Q"]) for row in SAVED if row["n"] == 12}

    actual_small = set()
    for n in range(2, 12):
        found, visited = enumerate_residual(n, qmax=11)
        actual_small.update((n, q) for q in found)
        print(f"n={n}: residual={len(found)} nodes={visited}")
    assert actual_small == saved_small, (
        len(actual_small), len(saved_small), len(saved_small - actual_small),
        len(actual_small - saved_small)
    )

    found_12, visited_12 = enumerate_residual(12, qmax=11)
    # For a connected 12-vertex graph with 11 edges, the incomparability graph
    # is a tree; this is exactly the residual required for e=12.
    assert len(found_12) == 12 and found_12 == saved_12
    print(
        f"n=12: residual={len(found_12)} nodes={visited_12}; "
        "exact candidate sets match"
    )
    print("All independently enumerated residual states have minimax depth 4.")


if __name__ == "__main__":
    main()
