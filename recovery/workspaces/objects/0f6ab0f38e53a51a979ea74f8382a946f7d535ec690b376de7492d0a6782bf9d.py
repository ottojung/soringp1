#!/usr/bin/env python3
"""Transcript-only budgeted DFS for S(n): a space-accounted reference.

This is the implementation behind the *space* refinement proved in
``docs/research-budgeted-dfs.md`` (section 5.2).  The DFS state is the
comparison **transcript** -- a list of ordered pairs ``(a, b)`` meaning
``a < b`` -- instead of an ``n x n`` transitive-closure bitmatrix.  Two
labelled keys are comparable exactly when one is reachable from the other in
the transcript's digraph, so a frame stores only its own comparison and a loop
cursor (``O(log n)`` bits) and comparability is recomputed on demand by
reachability (``O(n log n)`` bits of workspace).  No ``n x n`` closure matrix
is kept per frame, so the peak space is ``O((d+n) log(n+2))`` bits for a budget
``d`` -- the ``n log n`` reachability term is present even at ``d = 0`` and is
not absorbed into ``O(d log n)``; with ``d <= U(n) = O(n log n)`` this is
``O(n log^2 n)`` bits.

To realise that bound faithfully this reference uses a **single shared mutable
transcript list**: the recursion appends one comparison before a child and pops
it afterwards, so the full transcript is never copied per frame and no
``n^2``-sized incomparable-pair list is ever materialised.  The nested
``for i / for j`` loop tests comparability directly before recursing.
Reachability allocates its adjacency list and visited vector inside a
non-recursive helper and releases them before any child call.  The public
``can_sort`` wrapper copies the caller's transcript **once** and then runs the
mutating private helper.

The correctness argument and the exact bit accounting are in the doc; this
program is a small reference/experiment and is deliberately not optimised.
It uses no external libraries.  The companion regression test exercises only
``n <= 5``.
"""

import argparse
import time

# --------------------------------------------------------------------------
# Transcript = list of ordered pairs (a, b), a != b, meaning "a < b".
# Comparability is reachability in the digraph of these edges.
# --------------------------------------------------------------------------


def reachable(transcript, n, src):
    """Boolean list: which vertices are reachable from ``src`` (incl. src).

    Non-recursive: the adjacency list and visited vector are local to this call
    and released on return, so no reachability workspace is retained across a
    recursive descent.
    """
    adj = [[] for _ in range(n)]
    for a, b in transcript:
        adj[a].append(b)
    seen = [False] * n
    seen[src] = True
    stack = [src]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if not seen[v]:
                seen[v] = True
                stack.append(v)
    return seen


def comparable(transcript, n, i, j):
    """True iff i and j are comparable in the transitive closure of transcript."""
    return reachable(transcript, n, i)[j] or reachable(transcript, n, j)[i]


def is_total(transcript, n):
    """True iff every pair of distinct keys is comparable."""
    for i in range(n):
        for j in range(i + 1, n):
            if not comparable(transcript, n, i, j):
                return False
    return True


def _search(transcript, n, d, depth, stats):
    """Recursive helper; mutates the shared ``transcript`` list in place.

    Appends one comparison, recurses, then pops it, so the transcript is never
    copied.  The nested pair loop tests comparability directly before recursing
    and materialises no incomparable-pair list.
    """
    if stats is not None:
        stats["max_depth"] = max(stats.get("max_depth", 0), depth)
        stats["max_edges"] = max(stats.get("max_edges", 0), len(transcript))
    if is_total(transcript, n):
        return True
    if d == 0:
        return False
    for i in range(n):
        for j in range(i + 1, n):
            if not comparable(transcript, n, i, j):
                transcript.append((i, j))          # sorter picks {i,j}
                if _search(transcript, n, d - 1, depth + 1, stats):
                    transcript[-1] = (j, i)        # adversary answers j<i
                    if _search(transcript, n, d - 1, depth + 1, stats):
                        transcript.pop()
                        return True
                transcript.pop()
    return False


def can_sort(transcript, n, d, stats=None):
    """Decide "the sorter wins within budget ``d``" from the given transcript.

    ``transcript`` may be any sequence of ordered pairs (typically a tuple or
    list); it is copied **once** here and the caller's object is never mutated.
    ``stats`` (optional dict) records the maximum recursion depth and the
    maximum transcript length reached, i.e. the size of the stored path; both
    are bounded by ``d``.
    """
    return _search(list(transcript), n, d, 0, stats)


def ceil_log2(x):
    """Exact integer ceil(log2(x)) for x >= 1, no floating point."""
    if x <= 1:
        return 0
    return (x - 1).bit_length()


def merge_sort_upper_bound(n):
    """U(n) = n * ceil(log2(max(2, n))); a valid merge-sort upper bound."""
    if n <= 1:
        return 0
    return n * ceil_log2(max(2, n))


def compute_s(n, stats=None):
    """Exact S(n) by binary search on the transcript DFS, or None if n <= 1.

    Returns ``(value, seconds)``.  For n >= 2 the value is the least ``k`` in
    ``[0, U(n)]`` with ``can_sort((), n, k)`` true; monotonicity in ``k`` is
    used.  This is exact for every ``n`` the caller can afford; the doc's
    tests stay at ``n <= 5``.
    """
    if n <= 1:
        return 0, 0.0
    lo, hi = 0, merge_sort_upper_bound(n)
    t0 = time.perf_counter()
    while lo < hi:
        mid = (lo + hi) // 2
        if can_sort((), n, mid, stats):
            hi = mid
        else:
            lo = mid + 1
    return lo, time.perf_counter() - t0


def space_accounting(n, d):
    """Accounted peak bits for the transcript DFS at budget ``d``.

    ``stack`` counts the stored path: one ordered pair (2 labels, each
    ``ceil_log2(n+1)`` bits) plus a loop cursor (``ceil_log2(binom(n,2)+1)``
    bits) per frame, over at most ``d + 1`` frames.  ``reach`` counts the
    on-demand reachability workspace (a visited bit-vector of ``n`` bits and a
    stack of at most ``n`` labels).  ``matrix`` is the older bound that keeps
    one ``n x n`` bitmatrix per frame.  This is a bookkeeping helper, not a
    claim that the transcript bound is tight.
    """
    if n <= 1:
        return {"stack_bits": 0, "reach_bits": 0, "total_bits": 0, "matrix_bits": 0}
    label_bits = (n + 1 - 1).bit_length()  # ceil(log2(n+1))
    pairs = n * (n - 1) // 2
    cursor_bits = pairs.bit_length()  # ceil(log2(pairs+1)) for pairs>=1
    frames = d + 1
    stack_bits = frames * (2 * label_bits + cursor_bits)
    reach_bits = n + n * label_bits
    matrix_bits = frames * (n * n)
    return {
        "stack_bits": stack_bits,
        "reach_bits": reach_bits,
        "total_bits": stack_bits + reach_bits,
        "matrix_bits": matrix_bits,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-n", type=int, default=5,
                    help="largest n for the value table (keep small)")
    args = ap.parse_args()

    print("Transcript-only budgeted DFS: exact S(n) for small n")
    print("n | U(n) | S(n) | depth | edges | stack bits | total bits | matrix bits")
    stats = {}
    for n in range(0, args.max_n + 1):
        value, _dt = compute_s(n, stats)
        acc = space_accounting(n, value)
        print(f"{n} | {merge_sort_upper_bound(n)} | {value} | "
              f"{stats.get('max_depth', 0)} | {stats.get('max_edges', 0)} | "
              f"{acc['stack_bits']} | {acc['total_bits']} | {acc['matrix_bits']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
