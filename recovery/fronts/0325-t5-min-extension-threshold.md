# t5-min-extension-threshold

## status

investigated

## origin

ai_proposal_unverified

## agent_id

5dUsIStTVvhplHeMqPuDcA-denounce

## exit_state

clearexit

## question

Is the universal tightness threshold T(5) exactly 27, i.e. is every finite poset with at most 27 linear extensions sortable in five comparisons, while the 8-element Merge(2,6) with e=28 and m=6 shows that 28 does not suffice?

## basis

docs/research-obstruction-next.md sections 2 and 6 report T(5)=29 only for n<=6 (first failure e=30); exact minimax on Merge(2,6) gives e=28, m=6, so the n<=6 value cannot hold for all ground-set sizes.

## falsifier

An explicit finite poset P with e(P)<=27 and m(P)>=6, checkable by exact minimax, which would force T(5)<=26.

## implication

Fixes the exact all-size budget-5 leaf base and corrects the n<=6 extrapolation T(5)=29; this is a structural pruning theorem about the minimax game, not a P/NP separation.

## finding_unverified

t ways: memoized minimax over reachable posets, and extension-subset DP. Both give \(e=21,\ m=6\). Hence

\[
T(5)\le 20.
\]

The front’s `Merge(2,6)` witness has \(e=28,\ m=6\), so it only gives \(T(5)\le 27\); it is **not** the sharp failing instance. `Merge(2,5)` has \(e=21,\ m=5\) and is tight, while the staircase \(S_7\) is the actual \(e=21\) failure.

### Exact thresholds

I also computed the full all-size thresholds without assuming the open \(T(4)=12\):

\[
T(4)=12,\qquad T(5)=20.
\]

Method, briefly:

1. Decompose any poset into its unique ordinal sum of ordinally indecomposable factors (the connected components of the incomparability graph). Under ordinal sum, \(e\) multiplies and \(m\) adds; this is already proved in the repository.
2. Exhaustively enumerate every ordinally indecomposable poset with \(e\le 20\) by maximal-element insertion. Completeness holds because every poset has a natural labelling; a new maximal element is inserted after an ideal of predecessors. Pruning at \(e>20\) is safe because \(e\) is nondecreasing. For a connected incomparability graph, \(n\le e\), so depth 20 covers all cores.
3. Compute exact minimax for every core. The maximum exact \(m\) by \(e=1,\dots,20\) is
   \[
   0,1,2,2,3,3,3,4,4,4,4,4,5,5,5,5,5,5,5,5.
   \]
   No core with \(e\le20\) has \(m>5\). Counts at \(e=18,19,20\) are \(324,304,305\); the \(e=11,12\) counts and \(n\)-distribution match the independent T(4) audit’s 144 saved records exactly, and all 144 recompute to \(F=4\).
4. The minimal extension counts for depth \(d\) are \(s(1)=2,s(2)=3,s(3)=5,s(4)=8,s(5)=13\). If a poset with \(e\le12\) had factor depths summing to at least 5, the extension product would be at least \(3\cdot5=15>12\), contradiction: \(T(4)=12\). If a poset with \(e\le20\) had factor depths summing to at least 6, the product would be at least \(3\cdot8=24>20\): \(T(5)=20\).

The extremal family is the staircase \(S_n\) with \(\mathrm{pred}[i]=(1\ll(i-1))-1\). It satisfies \(e(S_n)=F_{n+1}\) and \(m(S_n)=n-1\) for all \(n\) (the all-\(n\) portion is an elementary adversary argument: only adjacent pairs are informative, and every adjacent pair must be queried). Hence

\[
T(r)\le F_{r+3}-1
\]

for every \(r\), with equality verified for \(r=2,3,4,5\):

\[
T(2)=4,\quad T(3)=7,\quad T(4)=12,\quad T(5)=20.
\]

The all-\(r\) equality \(T(r)=F_{r+3}-1\) (equivalently a Fibonacci splitting induction) remains a conjecture; only the upper bound is proved for all \(r\).

## Honest limits

- This is an **exhaustive finite computation plus paper deductions**, not Lean and not kernel-checked. Its correctness rests on the stated completeness of the insertion enumeration and the \(n\le e\) spanning-tree bound.
- It is a **general-poset local-threshold theorem**, not a certificate-completeness or NP-membership result. It does not give a polynomial-size certificate for `SORT-BOUND-U`, and it does not improve the uniform complexity of computing \(S(n)\).
- \(T(5)\) is a local pruning base, not a statement about \(S(5)\); the relevant root threshold is \(T(S(n))\).
- The all-\(r\) Fibonacci equality remains open.

## Effects and records

- One new board #301 comment posted at `2026-11-07T20:26:12Z`; no duplicate of the earlier conditional \(T(5)=20\) post.
- Durable note and reproducible sources: `~/.local/state/soringp1/t5-exact-threshold-20261107.md` and `~/.local/state/soringp1/t5verify/` (`enum_t5.go` SHA-256 `d71b1d58…`).
- No repository changes; the worktree remains clean.

## Other metadata

```json
{
  "finished_at": 1794083362.996252,
  "started_at": 1794081340.0438242
}
```
