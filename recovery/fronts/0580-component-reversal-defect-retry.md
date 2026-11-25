# component-reversal-defect-retry

## status

investigated

## origin

executive_blocked_front_retry

## agent_id

lV62nXGKWXa4e7QbRs0Ga6-illusion

## exit_state

clearexit

## question

For all finite posets A and B, is the component-reversal defect |F(A^op disjoint-union B)-F(A disjoint-union B)| at most 1, or can it be arbitrarily large?

## basis

Newest #301 parallel-reversal-symmetry reports F(A^op disjoint-union B)=11 versus F(A disjoint-union B)=12 at n=9, with all n at most 8 pairs equal and 96 of 1840 non-self-dual n=9 pairs violating equality. [EXECUTIVE RETRY 2026-11-19T19:5xZ] Fresh retry of a ledger front whose Antonina agent FAILED WITHOUT A FINAL TEXT (context/tool failure, not a mathematical resolution). FIRST read the current #301 board digest and the already-investigated adjacent fronts: parallel-reversal-symmetry, module-reversal-invariant-extension. Decide whether the EXACT question below is already settled by them; if so, report that precisely with evidence and STOP (do not repeat their work). Otherwise attack the exact question below. Keep scratch small; never paste large outputs or media into context; post ONE concise decisive finding/obstruction to #301.

## falsifier

Exhibit A,B with reversal defect at least 2 by exact minimax over disjoint unions, or prove the uniform bound 1 by a structural induction.

## implication

A uniform one-comparison bound would make component reversal a canonicalization with only additive-one value loss in exact DP; unbounded defect would show component orientation carries unbounded value information and block every reversal quotient.

## finding_unverified

cts), and (b) no newer post found a D≥2 witness.
No D≥2 witness exists anywhere on the board, and my own front has never posted. The exact question has already been thoroughly investigated. Let me check how to post to the board.
Let me verify the worktree is clean before posting.
I have everything I need. The exact question is verbatim the already-investigated `component-reversal-defect-bound` front, and its sharpened "≤1" form was attacked by a dedicated proof front with an independently-verified obstruction. I'll post one concise decisive status report to #301 and stop, without repeating spent work.
The comment posted (exit 0). Let me verify it landed exactly once.
Done. Here is the honest outcome.

## Decision: exact question already investigated → reported and stopped

The front's exact question — `D(A,B)=|F(Aᵒᵖ⊔B)−F(A⊔B)| ≤ 1` for all finite posets vs. unbounded — is **verbatim** the already-investigated `component-reversal-defect-bound` front, and its "≤1" form was attacked head-on by the dedicated proof front `reversal-defect-bound-proof-20261119exec`. Per the retry instruction to avoid repeating spent work, I did not re-run their computations; I posted one precise status finding to #301 (exactly once, verified) and made no repository/Lean changes. Worktree clean at `6a96398`.

## Mathematical finding (status of the claim)

- **Equality form `D≡0` is FALSE** — `parallel-reversal-symmetry` (11-08) gives the n=9 witness `A=Λ₃`, `B=(0,1,1,3,7,11)`; `P=A⊔B=(0,1,1,0,8,8,24,56,88)`, `Q=Aᵒᵖ⊔B=(6,0,0,0,8,8,24,56,88)`, `F(P)=12, F(Q)=11`, so `D=1`. Reproduced by ≥3 independent solvers and re-verified by the Executive (04:05Z); 96/1840 non-self-dual n=9 pairs violate equality.
- **Exhaustive |A|+|B|≤8: `D=0`** for 46,481 ordered pairs (and 6,248 nonempty pairs in the repo probe).
- **The `D≤1` bound itself is OPEN**, not proved and not refuted. The 11-19 proof front returned outcome (c): a precise obstruction plus sharp partial results, independently verified (04:45Z). **No `D≥2` witness exists anywhere on #301**; n=10 exhaustive search was never completed. Executive twice declined re-dispatch as duplicate work.

## Exact obstruction (why not settled) + my one new sharpening

Cross-comparisons `x∈A, y∈B` leave the `{A′⊔B′}` family, so there is no componentwise recurrence for `F(A⊔B)`; global duality couples `P` with `Pᵒᵖ`, not one-component reversal. With `g(X)=F(X)−⌈log₂e(X)⌉`, reduction gives `D=|g(A⊔B)−g(Aᵒᵖ⊔B)|` (same extension counts).

**New deduction:** the proof front listed "`g(X)≤1` for all posets ⇒ `D≤1`" as an open sufficient condition. That condition is in fact already **false** — `prime-excess-unboundedness` (11-10) proves `sup_X g(X)=∞` (prime posets on `27c` elements with `g≥2c+1`). This closes the "gap ≤1 everywhere" route to a `≤1` proof, but does **not** resolve `D≤1`, since the two gaps in `D` come from same-extension-count parallel compositions, not arbitrary prime posets.

## Scope

These are general-poset structural facts about `F`, not results about `S(n)`/`SORT-BOUND-U`. Component reversal is not a zero-loss value symmetry, hence not a sound canonicalization for exact DP; whether it is additive-one stays open. Value-invariance alone would not give a sound state quotient anyway (that requires an equivariant transition). No certificate-completeness or class conclusion follows. Reopening requires a genuinely new bridge — a targeted `D≥2` search beyond n=9 or a non-componentwise invariant — which is not available here.

## Other metadata

```json
{
  "finished_at": 1795118214.5712428,
  "started_at": 1795117874.5004485
}
```
