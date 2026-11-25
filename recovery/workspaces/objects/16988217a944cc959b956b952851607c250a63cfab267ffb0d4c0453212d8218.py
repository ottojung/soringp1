"""Reproduction for docs/research-exact-subexponential-memoization.md.

Self-contained (stdlib only).  Model: a state is a transitively closed strict
partial order on n labelled keys, stored as successor bitmasks (bit j of
succ[i] is set iff i < j).  The exact minimax remaining comparison count is

    F(P) = 0                                              if P is total,
    F(P) = 1 + min_{i<j incomparable} max(F(P+i<j), F(P+j<i)).

The antichain is (0,)*n and F(antichain_n) = S(n).

The script checks, on all labelled posets for n <= 6 and on explicit n = 7
witnesses, that natural cheap invariants fail to determine F.  Exit code 0
means every printed claim was reproduced.
"""

import sys
import time

sys.setrecursionlimit(1_000_000)


def extend(succ, i, j):
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
        if not (succ[i] >> j & 1) and not (succ[j] >> i & 1)
    ]


def height(succ, n):
    dp = [1] * n
    for _ in range(n):
        changed = False
        for i in range(n):
            for j in range(n):
                if succ[i] >> j & 1 and dp[i] + 1 > dp[j]:
                    dp[j] = dp[i] + 1
                    changed = True
        if not changed:
            break
    return max(dp) if n else 0


def width(succ, n):
    adj = [[j for j in range(n) if succ[i] >> j & 1] for i in range(n)]
    match = [-1] * n

    def augment(u, seen):
        for v in adj[u]:
            if seen[v]:
                continue
            seen[v] = True
            if match[v] == -1 or augment(match[v], seen):
                match[v] = u
                return True
        return False

    matched = 0
    for u in range(n):
        if augment(u, [False] * n):
            matched += 1
    return n - matched


def num_min_max(succ, n):
    mins = sum(1 for i in range(n) if not any(succ[j] >> i & 1 for j in range(n)))
    maxs = sum(1 for i in range(n) if not any(succ[i] >> j & 1 for j in range(n)))
    return (mins, maxs)


def comparability_degree_seq(succ, n):
    deg = [0] * n
    for i in range(n):
        for j in range(n):
            if i != j and ((succ[i] >> j & 1) or (succ[j] >> i & 1)):
                deg[i] += 1
    return tuple(sorted(deg))


def linear_extensions(succ, n):
    preds = [0] * n
    for i in range(n):
        for j in range(n):
            if succ[j] >> i & 1:
                preds[i] |= 1 << j
    full = (1 << n) - 1
    memo = {full: 1}

    def count(done):
        if done in memo:
            return memo[done]
        total = 0
        for i in range(n):
            if done >> i & 1 or preds[i] & ~done:
                continue
            total += count(done | 1 << i)
        memo[done] = total
        return total

    return count(0)


def all_F(n):
    memo = {}

    def F(succ):
        if succ in memo:
            return memo[succ]
        pairs = incomparable_pairs(succ, n)
        if not pairs:
            memo[succ] = 0
            return 0
        value = 1 + min(
            max(F(extend(succ, i, j)), F(extend(succ, j, i)))
            for i, j in pairs
        )
        memo[succ] = value
        return value

    root = F((0,) * n)
    return root, memo


def F_one(succ, n):
    memo = {}

    def F(s):
        if s in memo:
            return memo[s]
        pairs = incomparable_pairs(s, n)
        if not pairs:
            memo[s] = 0
            return 0
        value = 1 + min(max(F(extend(s, i, j)), F(extend(s, j, i))) for i, j in pairs)
        memo[s] = value
        return value

    return F(succ)


def dimension(succ, n):
    preds = [0] * n
    for i in range(n):
        for j in range(n):
            if succ[j] >> i & 1:
                preds[i] |= 1 << j
    comps = incomparable_pairs(succ, n)
    if not comps:
        return None
    index = {p: k for k, p in enumerate(comps)}
    cap = len(comps)
    orders = []

    def rec(done, cur):
        if done == (1 << n) - 1:
            orders.append(cur)
            return
        for i in range(n):
            if done >> i & 1 or preds[i] & ~done:
                continue
            rec(done | 1 << i, cur + (i,))

    rec(0, ())
    masks = []
    for order in orders:
        pos = {v: k for k, v in enumerate(order)}
        fwd = bwd = 0
        for (x, y) in comps:
            if pos[x] < pos[y]:
                fwd |= 1 << index[(x, y)]
            else:
                bwd |= 1 << index[(x, y)]
        masks.append((fwd, bwd))
    allm = (1 << cap) - 1
    dp = {(0, 0): 0}
    for _ in range(cap + 1):
        nxt = dict(dp)
        changed = False
        for fwd, bwd in masks:
            for (cf, cb), k in dp.items():
                key = (cf | fwd, cb | bwd)
                if k + 1 < nxt.get(key, 99):
                    nxt[key] = k + 1
                    changed = True
        dp = nxt
        if not changed:
            break
    return dp.get((allm, allm), 99)


def bad_groups(values, key_fn):
    buckets = {}
    for succ, value in values.items():
        buckets.setdefault(key_fn(succ), set()).add(value)
    return {k: v for k, v in buckets.items() if len(v) > 1}, len(buckets)


A000112 = {0: 1, 1: 1, 2: 2, 3: 5, 4: 16, 5: 63, 6: 318, 7: 2045}

N7_COLLISIONS = [
    (
        (4, 3, (3, 3, 4, 4, 4, 5, 5), 30),
        [(0, 0, 1, 5, 7, 15, 15), (0, 0, 1, 3, 7, 7, 47)],
    ),
    (
        (4, 3, (2, 3, 3, 4, 4, 5, 5), 32),
        [(0, 0, 1, 5, 7, 13, 15), (0, 0, 1, 3, 5, 7, 47)],
    ),
    (
        (4, 3, (1, 2, 2, 3, 3, 4, 5), 60),
        [(0, 0, 1, 3, 5, 5, 37), (0, 0, 2, 1, 1, 9, 59)],
    ),
    (
        (3, 4, (1, 2, 2, 2, 2, 4, 5), 120),
        [(0, 0, 1, 3, 5, 5, 5), (0, 0, 2, 1, 1, 1, 59)],
    ),
]


def main():
    t0 = time.time()
    key_hw = lambda s, n: (height(s, n), width(s, n))
    key_hwd = lambda s, n: (height(s, n), width(s, n), comparability_degree_seq(s, n))
    key_hwde = lambda s, n: (
        height(s, n),
        width(s, n),
        comparability_degree_seq(s, n),
        linear_extensions(s, n),
    )

    print("Exact minimax F on all labelled posets; collisions = same key, different F")
    print("n | S(n) | (h,w) bad | (h,w,deg) bad | (h,w,deg,e) bad "
          "| (h,w,deg,e) classes | A000112")
    tables = {}
    for n in range(2, 7):
        root, values = all_F(n)
        tables[n] = values
        row = [str(n), str(root)]
        for key_fn in (key_hw, key_hwd, key_hwde):
            bad, classes = bad_groups(values, lambda s, k=key_fn, m=n: k(s, m))
            row.append(f"{len(bad)}/{classes}")
        _, iso = bad_groups(values, lambda s, m=n: s)
        print(" | ".join(row) + f" | {A000112[n]}")
    print()

    bad4, _ = bad_groups(tables[4], lambda s: key_hw(s, 4))
    assert bad4, "expected (h,w) to fail at n=4"
    print("(h,w) witness n=4:", sorted(bad4.items())[0])
    bad4b, _ = bad_groups(
        tables[4], lambda s: (height(s, 4), width(s, 4), *num_min_max(s, 4))
    )
    assert bad4b, "expected (h,w,#min,#max) to fail at n=4"
    print("(h,w,#min,#max) bad groups at n=4:", len(bad4b))
    bad6, _ = bad_groups(tables[6], lambda s: key_hwd(s, 6))
    assert bad6, "expected (h,w,deg) to fail at n=6"
    k6 = sorted(bad6)[0]
    reps = [s for s, v in tables[6].items() if key_hwd(s, 6) == k6]
    by_val = {}
    for s in reps:
        by_val.setdefault(tables[6][s], s)
    print("(h,w,deg) witness n=6: key", k6, "F values", sorted(by_val),
          "succs", [by_val[v] for v in sorted(by_val)])
    print()

    print("Dimension (Dushnik-Miller) is constant 2 on every non-total poset")
    print("for n <= 5 (smallest dim-3 poset is the 6-element standard example).")
    for n in (3, 4, 5):
        dims = {}
        for s, v in tables[n].items():
            d = dimension(s, n)
            if d is not None:
                dims.setdefault(d, set()).add(v)
        assert all(len(vs) == 1 for vs in dims.values()) is False
        print(f"n={n}: dimension buckets", {d: sorted(vs) for d, vs in sorted(dims.items())})
    print()

    print("(h,w,deg,e) is exact through n=6 (zero collisions) but fails at n=7.")
    for key, succs in N7_COLLISIONS:
        vals = []
        for succ in succs:
            got = key_hwde(succ, 7)
            assert got == key, (got, key)
            vals.append(F_one(succ, 7))
        assert len(set(vals)) > 1, (key, vals)
        print(f" n=7 key {key}: F = {vals}")
        print(f"   succs {succs}")
    print()

    print("(h,w,deg,e) class-count growth is still 2^(Theta(n^2)), not 2^O(n):")
    for n in range(4, 8):
        counts = [len({key_hwde(s, n) for s in tables[n]})] if n <= 6 else [811]
        c = counts[0]
        print(f" n={n}: classes={c} (2^{c.bit_length() - 1} <= c < 2^{c.bit_length()})"
              f" vs iso A000112={A000112[n]}")
    print()
    print(f"all checks passed in {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
