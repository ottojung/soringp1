# antonina-Byf8ncGDFPsxRR3PUa2LYb-brood

Session: ses_e0b2ec4dbffeb1lFKot4P8ELvv
Workspace: /home/lubko/soring-fronts/uniform-tc0-sortbound-membership
Created: 1795108715376; updated: 1795109173128

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f4d13db2001WHpdafsymYWb2K)

I'll start by understanding the environment and checking which host I'm on, then read the key documents.

## Output 21 (msg_1f4d1514b001D8O93c1RpmbKHt)

I'm on billy-dev as required. Let me read the core documents in parallel.

## Output 44 (msg_1f4d162fc001BXmLnYc1mIoN7H)

Now let me check the board #301 digest, the frontier definition, and recent git history to see if there's prior work to avoid repeating.

## Output 76 (msg_1f4d1a5c5001UetbUfWDDK97lu)

Let me look at the 17:13Z Viche Executive board entry in full and search for prior uniform-circuit discussions.

## Output 113 (msg_1f4d1d6b7001wS4rSZpRqyJEjW)

Let me fetch the full text of the 17:13Z Viche Executive entry that defines this front, sourcing the profile as required.

## Output 124 (msg_1f4d1e5c9001G2j9mNHwyIb40m)

Let me check the frontier ledger for this front and search the board across pages for any prior TC0/uniform-circuit work, while I research the primary literature.

## Output 139 (msg_1f4d342a7001390MdtRKZUguzK)

This is a fresh TC0 front. Let me examine the relevant prior findings on uniformity barriers (the "U_G" tally language / Theorem 6.6) and the AC0 no-go result mentioned in git history.

## Output 154 (msg_1f4d35ebb001V302UVkudEUwSS)

This is highly relevant. Let me read those key sections in detail.

## Output 174 (msg_1f4d38500001k1Iw1jAkP0MVNl)

The repo already has a strong barrier (Theorem 6.6). Let me check whether TC0-equivalence of the threshold language and the exact excess function is already recorded, and research the literature on uniform TC0 / iterated multiplication to ground the premise.

## Output 207 (msg_1f4d4607f001tZghIasT1D0jBj)

I have enough to ground the analysis. Let me do a quick independent numerical sanity check of the numerical ingredients (information-bound increments, band width) and re-verify worktree cleanliness.

## Output 218 (msg_1f4d51831001YRQ6oOTQv1pkmM)

Numerical ingredients confirmed. Let me check the Antonina post command syntax and verify no prior post by my author before posting one board update.

## Output 242 (msg_1f4d6020a001wHd5LWeiowIAOf)

Now I'll post one concise board update documenting the finding and its honest limits.

## Output 260 (msg_1f4d678e2001Ssb3upeOFg2zZj)

Let me verify the comment was actually posted and the worktree is still clean.

## Output 271 (msg_1f4d69035001HcedAicKqMAd5Y)

## Outcome

On `billy-dev` I attacked the front's claim and **try seriously to disprove it**. Result: the claim is **not refuted** (no `∉ TC0` proof exists), but the front's *stated reasoning is refuted as insufficient* by a rigorous barrier already latent in the repo, and the question reduces exactly to computing one O(log n)-bit function. No new theorem met the publication gate, so **no Lean or repository changes were made**; worktree remains clean at `6a96398`. One concise finding was posted to board #301 (17:24Z).

## 1. Premise verified [deduction / literature]

- `I(n)=⌈log₂(n!)⌉ ∈ DLOGTIME-uniform TC0`: iterated multiplication is in uniform TC0 (Hesse–Allender–Barrington 2002; functional basis `FOM`), `n!` has Θ(n log n) output bits = poly in unary input length, and `I(n)=bitlength(n!)` for n≥3. Sergeev gives `S(n)−I(n)=o(n)`.
- **Correction of the falsifier:** majority and iterated multiplication are themselves *in* uniform TC0, so reducing them to/from the excess cannot separate it from TC0. A genuine lower bound needs hardness for a class strictly above TC0; the only explicit tool (permanent ∉ uniform TC0, Allender 1999) is counting/PP-hardness, with no bridge to a single tally sequence.

## 2. Clean equivalence [deduction]

`SORT-BOUND-U ∈ uniform TC0 ⟺ E(n)=S(n)−I(n) computable in uniform TC0 on 1ⁿ`.
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

## Output 290 (msg_1f4d825a4001wmNzL73uGXBpi0)

Recovery check complete: the previous turn **already posted** one comment to Antonina board #301 as `SoringP1 frontier: uniform-tc0-sortbound-membership` at **2026-11-19 17:24:14.934Z**. The post was verified on the board, so I did not post again.

Git is clean at `6a96398d937d20977a91b9afa8619cb27feab269`; no repository edits or commits occurred. Scratch material is under `/tmp/opencode/`. No unfinished external action remains.
