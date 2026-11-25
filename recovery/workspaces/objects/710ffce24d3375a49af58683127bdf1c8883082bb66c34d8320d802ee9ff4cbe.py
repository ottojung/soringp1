import json
from functools import lru_cache
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[2]
D = json.load(open(ROOT / "data" / "t4-threshold-candidates.json"))


def validate(record):
    n = record["n"]
    Q = record["Q"]
    full = (1 << n) - 1

    # Build strict predecessor masks from the fixed-natural-extension encoding.
    pred = [0] * n
    for hi in range(n):
        assert Q[hi] >= 0 and Q[hi] >> hi == 0
        for lo in range(hi):
            if not ((Q[hi] >> lo) & 1):
                pred[hi] |= 1 << lo

    # Count linear extensions by the ideal-subset recurrence.
    @lru_cache(None)
    def extension_count(done):
        if done == full:
            return 1
        return sum(
            extension_count(done | (1 << v))
            for v in range(n)
            if not ((done >> v) & 1) and not (pred[v] & ~done)
        )

    e = extension_count(0)
    assert e == record["e"], (n, Q, e, record["e"])

    # Validate transitivity in the fixed natural extension.
    for i in range(n):
        for j in range(i + 1, n):
            if (Q[j] >> i) & 1:
                continue
            for k in range(j + 1, n):
                assert (Q[k] >> j) & 1 or not ((Q[k] >> i) & 1), (n, Q, i, j, k)

    # Reconstruct the complete extension set independently. Checking only its
    # cardinality would not detect a duplicate or omitted saved permutation.
    generated = []

    def visit(done, word):
        if done == full:
            generated.append(tuple(word))
            return
        for v in range(n):
            if not ((done >> v) & 1) and not (pred[v] & ~done):
                visit(done | (1 << v), word + [v])

    visit(0, [])
    saved_extensions = [tuple(p) for p in record["ext"]]
    assert (
        len(saved_extensions) == e
        and len(set(saved_extensions)) == e
        and set(saved_extensions) == set(generated)
    ), (n, Q)

    # Exact minimax over the freshly reconstructed extension set.
    pair_splits = []
    for i in range(n):
        for j in range(i + 1, n):
            mask = 0
            for k, permutation in enumerate(generated):
                if permutation.index(i) < permutation.index(j):
                    mask |= 1 << k
            if mask and mask != (1 << e) - 1:
                pair_splits.append(mask)

    @lru_cache(None)
    def F(states):
        if states & (states - 1) == 0:
            return 0
        return 1 + min(
            max(F(states & mask), F(states & ~mask))
            for mask in pair_splits
            if (states & mask) and (states & ~mask)
        )

    f = F((1 << e) - 1)
    assert f == record["F"], (n, Q, f, record["F"])

    # Connected incomparability graph: independent BFS.
    seen = 1
    todo = [0]
    while todo:
        i = todo.pop()
        for j in range(n):
            if seen >> j & 1:
                continue
            lo, hi = sorted((i, j))
            if (Q[hi] >> lo) & 1:
                seen |= 1 << j
                todo.append(j)
    assert seen == full

    q = sum(value.bit_count() for value in Q)
    assert q <= 11 and q == record["q"]
    width = 0
    for subset in range(1, full + 1):
        if subset.bit_count() <= width:
            continue
        is_antichain = all(
            not ((subset >> i) & 1 and (subset >> j) & 1)
            or ((Q[j] >> i) & 1)
            for i in range(n)
            for j in range(i + 1, n)
        )
        if is_antichain:
            width = subset.bit_count()
    assert width == record["w"] and width <= 3
    return extension_count.cache_info().currsize, F.cache_info().currsize


states = 0
fstates = 0
for record in D:
    a, b = validate(record)
    states += a
    fstates += b

print(
    f"Independently verified {len(D)} saved representations: exact e(P), exact "
    f"extension sets, minimax F(P), transitivity, connectedness, width<=3, and "
    f"<=11 incomparable pairs; extension-DP states={states}, "
    f"minimax-subset states={fstates}."
)
print("by n", dict(sorted(Counter(x["n"] for x in D).items())))
print("F histogram", dict(sorted(Counter(x["F"] for x in D).items())))
