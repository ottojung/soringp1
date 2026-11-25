#!/usr/bin/env python3
"""Small exact checks for the disjoint-oriented-pair minimal-basis family."""
from itertools import combinations, product
from math import factorial


def family(n, t):
    """Enumerate unordered matchings of size t."""
    for vertices in combinations(range(n), 2 * t):
        def pairings(rest):
            if not rest:
                yield ()
                return
            a = rest[0]
            for k in range(1, len(rest)):
                b = rest[k]
                tail = rest[1:k] + rest[k + 1:]
                for p in pairings(tail):
                    yield ((a, b),) + p
        for pairs in pairings(vertices):
            yield pairs


def oriented_relation_masks(n, t):
    """Generate the strict relations of every oriented matching of size t."""
    for pairs in family(n, t):
        for directions in product((0, 1), repeat=t):
            rel = 0
            for (a, b), d in zip(pairs, directions):
                i, j = (a, b) if d == 0 else (b, a)
                # Ordered-pair index in the n-by-n strict relation matrix.
                rel |= 1 << (i * n + j)
            yield rel


def count_formula(n, t):
    return factorial(n) // (factorial(n - 2 * t) * factorial(t))


def check(n, t):
    rels = list(oriented_relation_masks(n, t))
    assert len(rels) == count_formula(n, t)
    assert len(set(rels)) == len(rels)
    assert all(r.bit_count() == t for r in rels)
    # Equal-size distinct bitsets are pairwise incomparable by subset.
    assert all((a & b) != a for i, a in enumerate(rels) for b in rels[i + 1:])
    return len(rels)


if __name__ == "__main__":
    for n in (4, 8):
        t = n // 4
        print(f"n={n} t={t}: {check(n, t)} oriented matchings")
