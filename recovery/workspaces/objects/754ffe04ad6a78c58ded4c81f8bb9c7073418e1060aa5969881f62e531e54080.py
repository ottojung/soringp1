from functools import lru_cache


def enum_posets(n, qmax):
    """Enumerate fixed-natural-extension posets whose incomparability graph is a tree."""
    Q = []

    def rec(k, q):
        if q > qmax:
            return
        if k == n:
            if q == n - 1:
                yield tuple(Q)
            return

        for S in range(1 << k):
            s = S.bit_count()
            if q + s > qmax:
                continue

            # Transitivity: if i || k and i < j in the fixed extension,
            # then j || k, or else i < j < k would force i < k.
            valid = True
            for i in range(k):
                if (S >> i) & 1:
                    for j in range(i + 1, k):
                        if not ((Q[j] >> i) & 1) and not ((S >> j) & 1):
                            valid = False
                            break
                    if not valid:
                        break
            if not valid:
                continue

            # A tree cannot acquire a cycle. Rebuild the processed-prefix
            # components and reject S if it joins vertices already connected.
            parent = list(range(n))

            def find(x):
                while parent[x] != x:
                    x = parent[x]
                return x

            for v in range(k):
                for i in range(v):
                    if (Q[v] >> i) & 1:
                        a, b = find(i), find(v)
                        if a != b:
                            parent[a] = b
            cycle = False
            bits = S
            while bits:
                bit = bits & -bits
                i = bit.bit_length() - 1
                bits -= bit
                a, b = find(i), find(k)
                if a == b:
                    cycle = True
                    break
                parent[a] = b
            if cycle:
                continue

            Q.append(S)
            yield from rec(k + 1, q + s)
            Q.pop()

    yield from rec(0, 0)


def extensions(Q, n):
    pred = [0] * n
    for hi in range(n):
        for lo in range(hi):
            if not ((Q[hi] >> lo) & 1):
                pred[hi] |= 1 << lo
    full = (1 << n) - 1
    out = []

    def go(done, word):
        if done == full:
            out.append(tuple(word))
            return
        for x in range(n):
            if not ((done >> x) & 1) and not (pred[x] & ~done):
                go(done | (1 << x), word + [x])

    go(0, [])
    return out


def width(Q, n):
    best = 0
    for subset in range(1, 1 << n):
        if subset.bit_count() <= best:
            continue
        if all(
            not ((subset >> i) & 1 and (subset >> j) & 1)
            or ((Q[j] >> i) & 1)
            for i in range(n)
            for j in range(i + 1, n)
        ):
            best = subset.bit_count()
    return best


def minimax(ext, n):
    e = len(ext)
    split_masks = []
    for i in range(n):
        for j in range(i + 1, n):
            mask = sum(1 << k for k, p in enumerate(ext) if p.index(i) < p.index(j))
            if mask and mask != (1 << e) - 1:
                split_masks.append(mask)

    @lru_cache(None)
    def f(states):
        if states & (states - 1) == 0:
            return 0
        return 1 + min(
            max(f(states & m), f(states & ~m))
            for m in split_masks
            if states & m and states & ~m
        )

    return f((1 << e) - 1)


if __name__ == "__main__":
    n = 12
    total = 0
    e12_width_le3 = []
    for q in enum_posets(n, n - 1):
        total += 1
        ext = extensions(q, n)
        if len(ext) == 12 and width(q, n) <= 3:
            e12_width_le3.append((q, minimax(ext, n)))
    print(
        "n=12 incomparability trees:", total,
        "e=12,width<=3:", len(e12_width_le3),
        "F histogram:", {v: sum(f == v for _, f in e12_width_le3)
                           for v in sorted({f for _, f in e12_width_le3})},
    )
