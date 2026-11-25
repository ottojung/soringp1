# excess-one-band-polynomial-decision-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

xD8w6xui28g1KFNvajP0Gs-sanguine

## exit_state

clearexit

## question

For the unary excess-one diagonal BAND_1 = {1^n : S(n) <= ceil(log2(n!)) + 1}, does a uniform polynomial-time decider exist on unary n that settles membership without computing the exact value S(n), or must every correct polynomial-time decider either establish the still-unproved global bound S(n) <= ceil(log2(n!)) + 1 for all n, or supply a polynomial-time lower-bound certificate witnessing excess at least two at some n?

## basis

Board #301 2026-11-22T16:24Z: a uniform poly(n,c) band decider is equivalent to SORT-BOUND-U in P, with fixed-c membership explicitly noted as strictly weaker and left unresolved; Sergeev's o(n) surplus does not rule out D(n)<=1; docs/problem.md and the 17:41Z post record no compact excess certificate. The 696-front ledger contains only the parent band front, so this fixed-excess subquestion is uncovered.

## falsifier

Exhibit an explicit polynomial-time predicate of n (for example a condition on the dyadic expansion of n!) that can be shown to agree with [S(n) <= ceil(log2 n!)+1] on all n, or find two n with the same computable dyadic signature but opposite BAND_1 status; in the other direction show that any correct polynomial-time decider would have to certify excess >= 2 at some n.

## implication

Unlike the uniform band decider of the 16:24Z board finding (equivalent to SORT-BOUND-U in P), a fixed-excess-one decider would be a new polynomial-time upper bound on one bit of S(n) that does not put S_unary in FP, while a lower-bound route would give the first structural non-information-theoretic excess certificate usable by an exact evaluator.

## finding_unverified

ult is honest negative / exact obstruction, not a theorem.** No repository, Lean, test, or ledger changes; worktree is clean at `6a96398`. The finding is posted as the single #301 comment for this front.

### The mathematical finding

Let `C(n)=ceil(log2 n!)`, `D(n)=S(n)−C(n)`, and write **P1** for the open conjecture `D(n)≤1 for all n`:

- **Unconditional deduction:** `P1 ⇒ BAND_1 = {1ⁿ}` ⇒ `BAND_1 ∈ P` via the constant‑accept decider, *without computing S(n)*. Contrapositive: `BAND_1 ∉ P ⇒ sup D ≥ 2` (P1 false). Also `S ∈ FP ⇒ BAND_1 ∈ P`.
- So BAND_1's complexity is **not an independent question**: it is implied by the still‑open conjecture P1, and its hardness would refute P1. The front's dichotomy reduces to a tautology about correctness proofs (a correct decider rejects exactly where `D(n)≥2` and accepts exactly where `D(n)≤1`); it cannot be disproved because it has no content beyond "proving BAND_1 ∈ P requires proving the answers." A minor correction: for a decider with a finite rejection set, **both** fact kinds are needed (infinitely many `D(n)≤1` acceptances plus the rejections), not an either/or.

### Concrete failed approaches

1. **Dyadic predicate (horn 1):** once "signature" only means "poly‑time computable from unary n," this *is* `BAND_1 ∈ P` — no weaker notion exists. Natural surrogates fail even on the D=0/D=1 split: slack `1−frac(log2 n!)` is `0.749507` at n=11 (D=0) and `0.749860` at n=15 (D=1); the cheap‑zone‑count predicate is already false at n=9.
2. **Two n, opposite BAND_1 status (horn 2):** requires an n with `D(n)≥2`; none is known (all n≤22 have D∈{0,1}, S(23) open, C(23)=75). If P1 holds, no such pair exists. Blocked by the very conjecture it would test.
3. **"Every decider must certify excess ≥ 2" (horn 3):** false if P1 holds (constant‑accept is correct). Its truth also hinges on P1.

### Honest limits

No improved bound, algorithm, class placement, separation, falsifier, or new theorem. General‑poset hardness was not invoked (no reduction to the antichain root), certificate *soundness* was not confused with *completeness*, and sparsity/Mahaney was kept in its proper many‑one scope. The exact obstruction is P1: every branch of this front collapses to the open question `S(n) ≤ ceil(log2 n!)+1` for all n, or to the absence of a compact excess‑≥2 certificate (unknown even at n=12).
**Recovery check (no actions repeated).**

- **Git/worktree**: `/home/lubko/soring-fronts/excess-one-band-polynomial-decision-alln`, branch `billy-dev`, `git status` clean, HEAD `6a96398`. No commits or repo files were created by this session.
- **Board #301**: the front’s result is already posted once — `[2026-11-22T18:36:17.597Z] SoringP1 frontier: excess-one-band-polynomial-decision-alln` (honest negative / exact obstruction; no falsifier achieved; no theorem completion). I did **not** repost it.
- **Other side effects**: none detected (no PRs, no ledger edits, no purchases). Scratch files exist only under `/tmp/opencode/`.

**Status**: the requested investigation is complete. The finding was: `P1: D(n)=S(n)-ceil(log2 n!) <= 1 for all n` implies `BAND_1 ∈ P` by constant accept (without computing `S(n)`), and `BAND_1 ∉ P` would refute P1; horn 1 is just `BAND_1 ∈ P` in disguise, horn 2 requires an unknown `D(n)>=2` witness, horn 3 is false under P1. The front’s dichotomy is a tautology about correctness proofs; the exact obstruction is P1 / absence of compact excess-≥2 certificates. No further work is pending from this session.

## Other metadata

```json
{
  "finished_at": 1795372640.5384212,
  "started_at": 1795372308.652485
}
```
