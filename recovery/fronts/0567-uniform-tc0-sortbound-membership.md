# uniform-tc0-sortbound-membership

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Byf8ncGDFPsxRR3PUa2LYb-brood

## exit_state

clearexit

## question

For all n, is the unary threshold language SORT-BOUND-U decidable by a DLOGTIME-uniform TC0 (or ACC0) circuit family, given that the information bound ceil(log2 n!) is itself in uniform TC0 and only the o(n) information excess separates it from the exact sorting number S(n)?

## basis

docs/problem.md records PSPACE membership; docs/research-sergeev-asymptotic.md records S(n)=log2(n!)+o(n); board #301 (2026-11-19 17:13Z) leaves small uniform circuit classes open; iterated multiplication is classically in uniform TC0.

## falsifier

Exhibit a uniform TC0 circuit computing S(n) for every n (upper outcome), or derive a uniform TC0 lower bound for the excess predicate from iterated multiplication or majority (negative outcome).

## implication

A TC0 membership proof would place exact unary sorting-number evaluation far below P; a lower bound would give the first circuit-class separation for the tally sequence and sharpen the known PSPACE/poly baseline.

## finding_unverified

n 1ⁿ`.
- (⇒) Compute I(n), U(n)=n⌈log₂ n⌉ in TC0; evaluate the threshold decider for **all O(n) candidates k in parallel** (poly size, constant depth); take iterated min → E(n) (O(log n) bits).
- (⇐) Compute S(n)=I(n)+E(n) and compare with k; TC0 is closed under composition.
This is the parallel-band refinement of the FP-equivalence in `problem.md`.

## 3. Decisive barrier [deduction from repo Theorem 6.6]

Repo Theorem 6.6 constructs a computable nondecreasing `G` with `I(n)≤G(n)≤I(n)+1` (slack **1**, far stronger than o(n)), satisfying the exact insertion and merge recurrences, with `U_G` in nonuniform depth-two AC0 — yet `U_G ∉ P`. Since uniform TC0 ⊆ uniform ACC0 ⊆ P, also `U_G ∉` uniform TC0/ACC0. **Therefore the whole package the front relies on — info bound in TC0, o(n) (even O(1)) slack, monotonicity, insertion/merge recurrences, computability, tiny nonuniform circuits — provably cannot imply uniform TC0 membership.** Any positive proof needs sorting-specific structure the front does not supply.

## 4. Required distinctions

- **General posets ≠ antichain:** GEN-SORT/Hyafil–Rivest hardness does not transfer to the single symmetric sequence S(n); every root comparison of the n-antichain is a relabeling, so no instance structure can be embedded (consistent with prior repo fronts).
- **Soundness ≠ completeness:** sound framed-DAG/Ford–Johnson certificates verify upper bounds but are not polynomial *complete* certificates for the exact optimum (repo Theorem 5.4; tree may be exponential). Neither NP nor TC0 membership follows.
- **Nonuniform ≠ uniform:** membership in nonuniform depth-two AC0 is trivial for every sparse language.

## 5. Failed upper/lower attempts and exact obstruction

- **Upper (C true):** needs an exact poly-time/TC0 minimax evaluator. Best known: 2^{O(n²)} / PSPACE; the repo's `exact-evaluator-time-exponent` result rules out the canonical memoization family reaching 2^{O(n log n)}. Sergeev is asymptotic with non-explicit constant and no closed form for E(n); the entropy identity needs exponentially precise rationals.
- **Lower (¬C):** no explicit natural tally language is known outside uniform TC0; diagonal tally languages are artificial, counting hardness doesn't apply, and P vs uniform TC0 is open. Sparsity/Mahaney concerns hardness, not membership.
- **Missing ingredient (sharp):** an all-n explicit finite effective evaluation of E(n) (upper), or a new counting-hardness/encoding-preserving reduction from a class strictly above uniform TC0 to the excess predicate (lower). Neither exists.

## Honest limits

This is a **precise obstruction and falsification of the proposed inference**, not a proof of membership or non-membership. The barrier is sorting-agnostic: it kills the *method*, not the specific claim about S(n). Numerical sanity checks (n≤3000; known S values give excess 1 at n=12,16,17,18) are consistent with the picture but prove no formula.

**Side effects:** one board #301 comment (17:24Z), scratch only in `/tmp/opencode/`; worktree clean, no commits, no Lean/CI/ledger changes.
Recovery check complete: the previous turn **already posted** one comment to Antonina board #301 as `SoringP1 frontier: uniform-tc0-sortbound-membership` at **2026-11-19 17:24:14.934Z**. The post was verified on the board, so I did not post again.

Git is clean at `6a96398d937d20977a91b9afa8619cb27feab269`; no repository edits or commits occurred. Scratch material is under `/tmp/opencode/`. No unfinished external action remains.

## Other metadata

```json
{
  "finished_at": 1795109177.7367263,
  "started_at": 1795108714.9764075
}
```
