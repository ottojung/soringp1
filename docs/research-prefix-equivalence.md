# The disjoint-pair-prefix identity is exactly Ford–Johnson optimality

**Status:** elementary paper proof plus small-`n` computational corroboration.
Not Lean-checked. This note is a *negative* result for a research front: it
shows that the "all-`n` disjoint-pair prefix" question is not an independent
route to `S(n)`, because it is logically equivalent to the classical (and
known-false) statement that merge-insertion is optimal for every `n`.

Model: adaptive comparison sorting of `n` distinct labelled keys; `S(n)` is
the minimum worst-case comparison count; `F(P)` is the minimax comparison
depth of a finite poset `P` (see `docs/problem.md`).

## Objects

- `A_m` — the antichain on `m` elements (no known comparisons).
- `tC_2` — the disjoint union of `t` two-element chains `a_i < b_i`.
- `P_{n,t} = tC_2 ⊔ A_{n-2t}`, defined for `0 <= t <= floor(n/2)`.

`P_{n,t}` is the state of a sorter that has performed `t` comparisons, namely
`s` pairwise comparisons of disjoint pairs and nothing else.

- `M(n) = sum_{j=1..n} ceil(log_2(3j/4))` — the exact worst-case comparison
  count of the Ford–Johnson / merge-insertion algorithm on `n` keys
  (Knuth, TAOCP vol. 3, §5.3.1). `M` is `0,1,3,5,7,10,13,16,19,22,26,30,...`
  for `n = 1,2,3,...`.

## Lemma 1 (upper bound)

For every `n >= 1` and `0 <= t <= floor(n/2)`,

    F(P_{n,t}) <= M(n) - t.

*Proof.* Merge-insertion on `n` keys begins with a fixed initial phase of
`floor(n/2)` comparisons that pair up the keys in a matching (Knuth §5.3.1);
these are the first comparisons the algorithm makes and they depend on no
outcome. Any matching of size `t` extends to a matching of size `floor(n/2)`,
so relabel the keys such that the first `t` of those initial comparisons are
exactly the `t` pairs of `P_{n,t}`.

Now fix any linear order `L` compatible with `P_{n,t}` and run merge-insertion
with `L` as the oracle. Whenever the algorithm asks about one of the `t`
already-known pairs, the answer is determined by `P_{n,t}` and is not charged;
the remaining queries are genuine comparisons of keys whose relation is not
yet known. Because merge-insertion uses at most `M(n)` comparisons in total on
any input, and the `t` skipped queries are part of that total, this
outcome-corrected execution costs at most `M(n) - t` charged comparisons and
sorts every compatible order. Hence `F(P_{n,t}) <= M(n) - t`. ∎

The relevant point is that the *worst case* is preserved: for each compatible
`L` the total is at most `M(n)`, so the maximum over compatible `L` of the
charged count is at most `M(n) - t`.

## Lemma 2 (lower bound)

For every `n >= 1` and `0 <= t <= floor(n/2)`,

    F(P_{n,t}) >= S(n) - t.

*Proof.* Take an optimal strategy for `P_{n,t}` using `F(P_{n,t})` comparisons
in the worst case. Prepend the `t` comparisons of the pairs: this uses
`t + F(P_{n,t})` comparisons in the worst case and sorts `A_n` (the `t` pair
answers are exactly what the strategy expects). Hence
`S(n) <= t + F(P_{n,t})`. ∎

## Theorem (equivalence)

For every `n >= 1`:

    S(n) - t <= F(P_{n,t}) <= M(n) - t   for all 0 <= t <= floor(n/2),

and the following are equivalent:

1. `S(n) = M(n)` (merge-insertion is optimal on `n` keys);
2. `F(P_{n,t}) = S(n) - t` for every `t`;
3. `F(P_{n,t}) = S(n) - t` for at least one `t`.

*Proof.* Combine Lemmas 1 and 2. Both bounds coincide exactly when
`S(n) = M(n)`. If equality holds for a single `t`, then
`S(n) - t = F(P_{n,t}) <= M(n) - t`, so `S(n) >= M(n)`, and `S(n) <= M(n)`
always holds, giving `S(n) = M(n)`. ∎

## Consequences

**The all-`n` disjoint-pair-prefix conjecture is false.** Merge-insertion is
not optimal for every `n`: Manacher (JACM 26(3), 1979) proved `F(n) > S(n)`
for infinitely many `n`, and Schulte Mönting (TCS 14(1), 1981) proved
non-optimality at `n = 47`. Stober–Weiß (ALENEX 2023, arXiv:2206.05597, §1)
state exactly: "it has been shown that the Ford–Johnson algorithm is not
optimal for `n = 47`; it is not known whether there is any `n < 47` for which
`F(n) > S(n)`."

By the theorem, at any such `n` the identity fails for **every** `t`:
`S(n) < M(n)` gives `F(P_{n,t}) < M(n) - t` strictly. In particular, for
`n = 47` and every `0 <= t <= 23`,

    F(P_{47,t}) <= M(47) - t - 1,

and the conjectured equality `F(P_{47,t}) = S(47) - t` is refuted without
knowing `S(47)`.

**The identity holds exactly on the known optimality range.** Since
`S(n) = M(n)` is established for `1 <= n <= 22` (Wells; Kasai–Sawato–Iwata;
Peczarski; Stober–Weiß), the identity `F(P_{n,t}) = S(n) - t` holds for all
`0 <= t <= floor(n/2)` throughout `1 <= n <= 22`. For `23 <= n <= 46` the
identity is *equivalent* to the open question whether merge-insertion is
optimal there (no `n < 47` with `F(n) > S(n)` is known), and for `n = 47` and
infinitely many larger `n` it is false. The pattern observed for `n <= 12` was
therefore a verification of merge-insertion optimality, not evidence for a new
all-`n` phenomenon.

**No all-`n` conclusion about `S(n)` can be extracted from this front.** The
prefix identity carries exactly the information "merge-insertion is optimal
here", and nothing more: it is implied by, and implies, that statement. A
refutation at `n = 47` is therefore not a defect of a certificate format; it
is the classical `n = 47` phenomenon reappearing.

## Computational corroboration

`scripts/prefix_equivalence_check.py` (in this worktree) computes `F(P_{n,t})`
exactly with the repository's transcript DFS (`scripts/transcript_dfs.py`) for
all `0 <= t <= floor(n/2)` and prints `F(P_{n,t})`, `M(n) - t` and
`S(n) - t`. For `2 <= n <= 8` every value satisfies
`F(P_{n,t}) = M(n) - t = S(n) - t`, as the theorem requires on the optimality
range. This is a finite read-out of the two lemmas, not a proof of either;
the proof above is the general argument.

## What would be new

The theorem does not touch the actual open questions. To make progress on
`S(n)` one still needs either (i) lower bounds beyond merge-insertion's `M(n)`
for specific `n` (e.g. `n = 23`), or (ii) a genuinely different certificate or
program format. Any proposal phrased as "the optimal sorter begins with `t`
disjoint comparisons" reduces to (i) by the argument above and should be
rejected as an independent front.
