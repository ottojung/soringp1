# root-split-divisibility-allposets

## status

investigated

## origin

ai_proposal_unverified

## agent_id

AZYrO81ZD2yA9IRxzCpuhy-parts

## exit_state

clearexit

## question

For which infinite families of posets {F_n} rooted at the n-antichain is there NO exact comparison tree partitioning Ext(F_n) into leaf classes of equal size e(F'_n) up to framing, due to the integer divisibility of branch extension counts induced by every possible first comparison and its recursive splits, beyond the known odd antichain-to-star case?

## basis

Exact-reset realizability proof for odd antichain->star in docs/research-exact-reset-realizability.md; branch-split counts from minimax recurrence in docs/problem.md and docs/research-encoding-consequences.md.

## falsifier

Exhibit either a general theorem classifying all such families, or an explicit infinite family with e(F_n)/e(F'_n) integer but every comparison tree produces some branch of size not divisible by e(F'_n) for large n despite no obvious global obstruction.

## implication

A general branch-divisibility obstruction would rule out broad classes of exact-reset/partition certificates for SORT-BOUND-U regardless of framing, constraining the framed-DAG completeness route without relying solely on state-graph size arguments.

## finding_unverified

Let us think of other families. Consider F'_n being a poset whose e(F'_n) has all prime powers matching in a bad way.

Let us write the analysis.

Let us look up what "rooted at the n-antichain" means and the full context again.

Let us analyze systematically.

Let us write a detailed analysis.

Let us provide a comprehensive mathematical analysis.

I need to report a mathematical finding. Let us be precise and cite what we know.Let us post/report the findings. The instructions say "report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof." Also need to follow the rules - this is on billy-dev in the repo; but the instructions say "do not create Lean or repository changes without a genuinely substantive, independently checkable new theorem or counterexample" - our analysis is mathematical reasoning but we haven't produced a new theorem/counterexample to commit. Just analysis.

I should give a concise report of the mathematical finding as requested.Finding: for F_n=A_n, root branch obstruction is exactly when k_n = e(A_n)/e(F'_n) is odd (gives n!/2 not divisible by n!/k_n). Infinite families with k_n odd for all n in family: (1) disjoint union of a fixed odd k-chain and n-k isolated elements (ratio k odd, all n≥k) — cleaner/general beyond star; (2) star V_n gives ratio n odd iff n odd. Deeper-level obstruction can arise even if root OK, but full "impossible for every tree" is strongest when root already fails. No obvious general classification is standard; the 2-adic/ratio-odd condition is the direct divisibility criterion. No counterexample found to the known odd-star case; proposed fixed-k-chain family is a broader explicit infinite family with the same root obstruction for all its members.


## Other metadata

```json
{
  "finished_at": 1793587630.052028,
  "started_at": 1793585212.8134544
}
```
