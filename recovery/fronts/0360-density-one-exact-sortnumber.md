# density-one-exact-sortnumber

## status

investigated

## origin

ai_proposal_unverified

## agent_id

5IvydrHYQFxPgzAq1gEoUY-term

## exit_state

clearexit

## question

Is there a uniform deterministic polynomial-time algorithm that computes S(n) correctly for all n outside a set of asymptotic density zero, or does every polynomial-time algorithm err on a positive-density set of n?

## basis

docs/problem.md unary encoding and open SORT-BOUND-U in P status; board #301 exact values and Sergeev asymptotics; no density-one or generic-case front in the ledger.

## falsifier

A fully specified polynomial-time algorithm with a proved density-one correctness set, or a proof that every polynomial-time algorithm errs on a positive-density set of n.

## implication

A density-one algorithm would be a new uniform upper bound weaker than P and would show the hard n are sparse; a positive-density error theorem would rule out generic-case evaluation and strengthen the worst-case barrier.

## finding_unverified

ocked polynomial-time machine `M_i` to a positive-density set of blocks, e.g. those `k` with `v₂(k)=i`; this has density `2^{-(i+1)}`. Maintain a counter `c=O(k)`. In a block assigned to `M_i`, let `p=min P_k`; the plateau `[p,2^{k+1})` has length at least `δ|B_k|`. If `M_i` equals `c` on at least half the plateau, set `c:=c+1` (one jump at `p`, a floor-increment position); otherwise keep `c`. Define `D(n)=c` on that plateau and `S'=C+D`. Then `D=O(log n)`, the increment spectrum is preserved, and on every assigned plateau `S'` differs from `M_i` on at least half the plateau. Thus `M_i` errs on a set of density at least `(δ/2)2^{-(i+1)}>0`. The construction is EXP-computable by block scanning and polynomial-time simulation.

**Consequence.** A proof of the positive horn must use finer facts specific to the minimax value `S`; it cannot rely on `C≤S≤F`, monotonicity, the increment spectrum, sublinear excess, or EXP computability. Conversely, the negative horn does not follow either: the construction diagonalizes an artificially chosen sequence and cannot target the fixed minimax sequence `S`. The exact missing step is an `S`-specific infinite-family theorem — either a density-one computable formula, or a proof that `S` differs from every FP sequence on positive upper density.

**Model and literature distinctions.** General-poset minimax/certificate results (Wells–Peczarski–Stober–Weiss exhaustive searches, extension-count pruning) supply sound finite certificates or exact values, not all-`n` density statements about `S`. Sparse-language barriers such as Mahaney concern decision-language reductions, not density-one agreement of functions. Certificate **soundness** is also independent of the **completeness** needed for a density-one evaluator.

**Honest limits.** This is not a disproof of either horn for `S`, and it is not a complexity-class separation. It is an independently checkable barrier theorem plus a precise obstruction. I also note a logical caveat in the front: the literal negation of “errors only on a density-zero set” is “errors not of density zero”; the second horn should say positive **upper** density unless existence of the density is separately proved.

I posted this finding to board **#301**. Host verified `billy-dev`; worktree remains clean at `6a96398`; no Lean or repository changes were made.
Recovery inspection complete. I did not repeat the prompt or create any new external effects.

**Verified state**
- Host: `billy-dev`.
- Working directory: `/home/lubko/soring-fronts/density-one-exact-sortnumber`.
- Git: clean worktree, `HEAD = 6a96398`; no commits, edits, Lean files, or repository changes.
- Board #301: the previous finding **was posted exactly once** at `2026-11-08T10:20:22.255Z` by `SoringP1 frontier: density-one-exact-sortnumber`. I did not post again.
- Durable ledger: `density-one-exact-sortnumber` is still marked `running`, with no finding yet recorded. That is expected until this agent exits; the keeper updates the ledger from the returned result.

**Effect assessment**
- Confirmed side effect: one board #301 comment containing the diagonal-barrier finding.
- No commit, no file change, no duplicate board post.
- No uncertain external effects requiring review.

The mathematical result from the previous turn stands as reported: a rigorous insufficiency/barrier theorem for the density-one front, not a disproof of either horn for the actual minimax sequence `S`. Nothing substantive remains unfinished on my side.

## Other metadata

```json
{
  "finished_at": 1794133310.324097,
  "started_at": 1794132519.3887746
}
```
