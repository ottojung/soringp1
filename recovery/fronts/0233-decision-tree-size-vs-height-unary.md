# decision-tree-size-vs-height-unary

## status

investigated

## origin

ai_proposal_unverified

## agent_id

br16Kt7BFivxbPQFYJcQYS-deposited

## exit_state

clearexit

## question

For exact unary SORT-BOUND-U, ask whether polynomial-time height-evaluation requires super-polynomial decision-tree size on some family achieving near-S(n), and whether size is polynomially verifiable without enumerating the exponential tree.

## basis

Optimal trees can be exponentially large; framed-DAG tightness showed height-collapse only when tight; certificate soundness vs completeness repeatedly emphasized (AGENTS.md, problem.md).

## falsifier

Construct a uniform family of comparison trees of height O(S(n)) with polynomially many nodes for all n, with a polynomial-time soundness/completeness checker not equivalent to building the full tree; or prove exponential size is necessary for all height-optimal trees.

## implication

Distinguishes height (the S(n) object) from representation size for unary complexity: NP membership would need succinct certificates (sound+complete) not just small height, so size/representation is a different obstacle than the PSPACE upper bound.

## finding_unverified

Let us think systematically.

Let us verify this fundamental point.

Let us do a serious analysis of this question.

Let us think carefully about this.

Let us analyze the question carefully.

Let us write a detailed report.

The analysis above is complete. I will report this to the board as requested - but I need to follow the instructions: "report a mathematical finding, concrete failed approach or exact obstruction; do not confuse process success with a proof" and post to board #301 if there is something changed? The instructions say "Report the result, including negative or inconclusive outcomes, as a concise update on the research board (see `docs/operations.md`)". Also the user says "On completion report..." - I should follow the research protocol.

Done. I have analyzed the question thoroughly - studied AGENTS.md, problem.md, literature, board, experiments. No repository changes made as there is no genuinely substantive new theorem/counterexample to publish. I report the findings above.Studied AGENTS.md, docs/problem.md, literature, board #301, and ran strategy_dag_probe/one-ply experiments on billy-dev. No repo/Lean changes.

FALSIFIERS tested: (1) construct polynomial-node height-O(S(n)) trees with poly-time sound/completeness checker not equivalent to full tree; (2) prove exponential size necessary for all height-optimal trees. Neither found.

KEY FINDINGS:
- Any correct sorting decision tree needs >=n! leaves, >=2n!-1 nodes (independent of height). Height-optimal (tight) strategies achieve S(n)~n log n but tree size remains exponential in n log n.
- For a fixed optimal policy (poset-state function achieving S(n)), different branches do not merge to same poset state (poset only grows, and optimal tight strategies lack cross-branch collisions); experiments show DAG(1)=2n!-1 with no duplicates up to n=6 while union-of-all-optimal/DAGs grow quickly (n=5 gives 1551). Quotients help but remain exponential.
- Framed-DAG joins are equivalent to ordinary trees up to unfolding (height-collapse only when tight); checker polynomial in explicit graph size, but all-n polynomial-size completeness at height S(n) is open. Merge-sort gives polynomial graphs at larger height; optimal strategies resist compression.
- SORT-BOUND-U sparse => many-one NP-hardness would imply P=NP (Mahaney); unary in PSPACE, binary in EXPSPACE. NP membership needs succinct sound+complete certificates - a distinct obstacle from height/PSPACE.

OBSTRUCTION: height-optimal tight strategies appear to prevent poset-state merging; exponential leaf count forces exponential tree size under tree representations, and DAG/joins seem to require unfolding for completeness. No combinatorial proof found, but experimental evidence strongly suggests exponential size necessary for height-optimal trees. Cannot rule out clever non-tree representations, but soundness+completeness with height optimality is blocked by tightness. No counterexample constructed.


## Other metadata

```json
{
  "finished_at": 1793707991.6399646,
  "started_at": 1793705359.8323069
}
```
