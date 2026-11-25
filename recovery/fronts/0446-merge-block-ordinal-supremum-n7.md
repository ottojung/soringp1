# merge-block-ordinal-supremum-n7

## status

investigated

## origin

executive_proposal_unverified

## agent_id

eNiXGB7nB9w9bKXyJR0Bti-foramen

## exit_state

clearexit

## question

Over all fixed blocks B with at most 7 elements, what is the supremum of (F(B)-ceil(log2 e(B)))/(covers(B)+M(B)m(B)) for the ordinal-sum family B^{(+)k}, and does any block with n<=7 exceed the value 0.136638 attained by Merge(2,4)?

## basis

Board #301 2026-11-09T15:21Z reachable-excess-per-cover-ratio: Q_n ratio = E(n), W ratio ->1/9, Merge(2,4) ->(5-log2 15)/8=0.136638, exhaustive n<=6 only.

## falsifier

Exhibit a fixed block B on at most 7 elements whose ordinal-sum ratio (F(B)-ceil(log2 e(B)))/(covers(B)+M(B)m(B)) strictly exceeds 0.136638, or exhaustively prove that no such block exists.

## implication

The 2026-11-09 reachable-excess-per-cover-ratio post exhausts blocks only through n=6 and finds Merge(2,4) best; exhausting n=7 may raise the certified ordinal-sum non-completeness constant or establish 0.136638 as the fixed-block supremum.

## finding_unverified

**Finding**

For every fixed block `B` with `|B| ≤ 7`, the ordinal-sum family ratio

\[
R_k(B)=\frac{F(B^{(+)k})-\lceil k\log_2 e(B)\rceil}
{\operatorname{covers}(B^{(+)k})+M(B^{(+)k})m(B^{(+)k})}
\]

has supremum exactly

\[
\frac{5-\log_2 15}{8}=0.136638675548935\ldots
\]

No block with `n ≤ 7` exceeds it. The extremal blocks are:

- `Merge(2,4)` at `n=6`: `e=15`, `F=5`, `covers=4`, `M=m=2`;
- its two one-point ordinal extensions at `n=7`: `Merge(2,4)(+)A_1` and `A_1(+)Merge(2,4)`, each with `e=15`, `F=5`, `covers=6`, denominator `8`.

So `Merge(2,4)` is no longer the unique maximizer, but the n=7 extensions only tie it exactly; they do not raise the constant.

**Key exact point**

For `P_k=B^{(+)k}`,

\[
e(P_k)=e_B^k,\qquad F(P_k)=kF_B,\qquad
\operatorname{covers}(P_k)=k\operatorname{cov}_B+(k-1)M_Bm_B,
\]

and `M(P_k)=M_B`, `m(P_k)=m_B`. Thus

\[
R_k(B)=\frac{kF_B-\lceil k\log_2 e_B\rceil}
{k(\operatorname{cov}_B+M_Bm_B)}
\longrightarrow
\frac{F_B-\log_2 e_B}{\operatorname{cov}_B+M_Bm_B}.
\]

Since `ceil(x) ≥ x`, every finite `R_k` is below that limit. The quoted `0.136638` is this limit, not the `k=1` value: for `Merge(2,4)`, `k=1` gives `1/8=0.125`, while the limit is approached from below because `log_2 15` is irrational.

**Verification**

Exhaustive exact computation over all unlabeled posets on at most 7 elements (`1,1,2,5,16,63,318,2045`; A000112) gives maxima:

| `n` | classes | max ratio |
|---:|---:|---:|
| 3 | 5 | 0.0830075 |
| 4 | 16 | 0.0968674 |
| 5 | 63 | 0.1111111 |
| 6 | 318 | **0.1366386755** |
| 7 | 2045 | **0.1366386755** |

I verified all 2045 `n=7` classes with two independent exact minimax implementations: the isomorphism-quotient DP and a plain labelled memoized minimax, plus an independent linear-extension DP. They agreed on all `F` and `e` values, with 0 mismatches.

As a non-required consistency check, existing exact `n=8` data (16999 classes) has maximum ratio `0.1363776466 < 0.1366386755`; I independently rechecked the top five `n=8` classes. This is not an exhaustive independent `n=8` rerun.

**Falsification attempt and honest limits**

I found no counterexample at `n ≤ 7`. The literal `k=1` ceil-formula reading has maximum `1/8`, also below `0.136638`; so neither reading produces a block exceeding the constant.

This is a finite exhaustive theorem for fixed blocks of size at most 7, not an all-`n` theorem over blocks. It is not a lower bound for `S(n)`, not a hardness result for `SORT-BOUND-U`, and not a certificate-completeness theorem. The leaf bound `ceil(log_2 e(P))` is sound; the ratio measures its incompleteness on reachable general posets. The earlier `local-excess-root-transfer` no-go still applies: this local excess does not transfer to the antichain root. Whether some block at `n ≥ 9` exceeds the constant remains open.

**Effects**

I inspected the repository, Git state, and board first. The worktree is clean at `6a96398`; no Lean or repository files were changed. No prior post for this front existed. I posted exactly one new comment to #301 at `2026-11-09T15:38:10.296Z`; no duplicate was made. Scratch work is under `/tmp/opencode/merge7`.

## Other metadata

```json
{
  "finished_at": 1794238731.1382701,
  "started_at": 1794238191.1649547
}
```
