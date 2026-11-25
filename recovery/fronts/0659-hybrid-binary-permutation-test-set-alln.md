# hybrid-binary-permutation-test-set-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

MczkdzlAuKYrOu2yGiETtH-riotous

## exit_state

clearexit

## question

Since binary orders alone apparently cannot certify the exact sorting number (B(n) < S(n) on the computed range), let h(n) be the least number of distinct-key permutations which, together with all 2^n binary orders, force every height-below-S(n) comparison program to fail. Is h(n) bounded by a polynomial in n for all n, or must h(n) grow superpolynomially?

## basis

The 21:43Z zero-one result leaves this regime open; the universal-order-hitting-set front refuted polynomial test sets only at budget binom(n,2), not at S(n); the separation-tree lemma; computed B(n) < S(n).

## falsifier

Exhibit, for each n, a polynomial-size permutation set P_n such that any program sorting all binary orders and P_n has height at least S(n); or derive a 2^{Omega(n)} lower bound on h(n) by an adversarial restriction argument on optimal trees.

## implication

A polynomial h(n), combined with a polynomial-size optimal program, would open a sample-based NP-style verification route; a superpolynomial h(n) would close the hybrid binary-plus-permutation test route. Neither outcome separates complexity classes.

## finding_unverified

Let me push the n=5 search to size 3 with the faster decision routine.
Let me sanity-check my routines and gather the final evidence before reporting.
My witness verification had a representation bug — the search returns rank-vectors, but I re-applied `make_rank`. Let me correct.
Sanity checks pass. Let me find the exact board-post command used previously (so I post exactly once, correctly).
I have a solid finding. Let me write and post the report to #301 exactly once (no prior post for my front exists).
Let me verify the post landed exactly once.
Post confirmed exactly once (22:33:01Z). Let me do a final clean-state check.
## Report — front `hybrid-binary-permutation-test-set-alln`

**Recovery audit first.** Host `billy-dev`, tree clean (branch `billy-dev`, HEAD `6a96398`, empty stash, reflog = clone only). My front's ledger entry was `running` (launched ~22:15:34Z), and board searches for `hybrid` / `permutation test` / `h(n)` returned **0 matches** before I acted. The interrupted turn left **no external side effects** to repeat. I posted exactly one #301 result (22:33:01Z, verified present once) and made **no repository/Lean/test/ledger changes**; all computation is in `/tmp/opencode/`.

**What I did.** Studied AGENTS.md, problem.md, literature.md, the 21:43Z zero-one result + separation-tree lemma, and the `minimax-witness-family` / `universal-order-hitting-set` / `binary-test-universe` fronts. Built a from-scratch minimax solver `h(H)` = min height to sort a family H (verified against known S(n)=1,3,5,7 and B(n)=1,3,4,6).

**Mathematical finding (not a theorem completion).**

- *Rigorous lower bound [deduction]:* **h(n) ≥ S(n) − B(n)** via the leaf-extension lemma (adding one permutation raises min height by at most 1). With B(n)=O(n) (B(7)=9 computed), this is only Ω(n log n) — polynomial.
- *New exact data [experiment, exhaustive]:* h(3)=0; **h(4)=2** (witness P={(1,0,3,2),(1,3,0,2)}); **h(5)≥4** (all |P|≤3 checked, 129,766 size-3 sets). Notably h(4)=2 > S(4)−B(4)=1, so the trivial bound is not tight.
- *Exact obstruction [deduction]:* the front's dichotomy is **equivalent to the open defect problem** D(n)=max_H(h(H)−log₂|H|): (a) D(n)=O(n) ⟹ h(n) ≥ 2^{S(n)−O(n)} = 2^{Ω(n log n)} (superpolynomial); (b) h(n)=n^{O(1)} ⟹ D(n)=Θ(n log n) (maximal, since always D(n)≤S(n)−log₂S(n)). Sergeev's o(n) surplus bounds only the full family S_n, not arbitrary H. Known witness families are a constant fraction of n! (τ(4)=12/24, τ(5)≤49/120, defect o(n)), which *supports* superpolynomial h(n) but does not prove it.

**Concrete failed approach.** Leaf-extension only certifies Ω(n log n); the greedy "each added input increments h" route (which would give h(n)≤S(n)−B(n)) is **refuted** by h(4)=2>1. Adversarial restriction on optimal trees fails because binary orders are routable shallow (h(B)≈n).

**Honest limits.** I could not decide polynomial vs superpolynomial — it reduces to settling D(n)=O(n) vs Θ(n log n) (equivalently τ(n) exponential vs a poly-size S(n)-complete witness family), both open. No new S(n) value, no class separation. General-poset hardness and certificate soundness were kept distinct from completeness throughout. `S(n)` and `SORT-BOUND-U` remain open.

## Other metadata

```json
{
  "finished_at": 1795300438.0207405,
  "started_at": 1795299334.0329187
}
```
