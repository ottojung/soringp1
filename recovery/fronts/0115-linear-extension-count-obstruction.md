# linear-extension-count-obstruction

## status

blocked

## origin

ai_proposal_unverified

## agent_id

1WbpOp8gErXCUXaH6KUn1g-brougham

## exit_state

failed

## question

Can the #P-hardness of counting linear extensions be encoded into the minimax height evaluation for some infinite family of partial orders reachable from the antichain, establishing that computing F(P) is #P-hard on the SORT-BOUND-U state graph without reducing arbitrary posets directly?

## basis

Brightwell–Winkler #P-completeness of linear extensions; minimax recurrence for F(P) in problem.md and upper-bound.md; need encoding-preserving reduction on reachable states.

## falsifier

Prove F(P) is computable in polynomial time in the description of any poset P reachable from the n-antichain, or show the reduction is impossible due to structure preserved by comparison learning.

## implication

A positive reduction would link F(P) evaluation to #P, clarifying the computational hardness of the recurrence nodes while respecting the 'no transfer without reduction' constraint for the fixed antichain family.

## finding_unverified

exploit recurrence tree structure). 
- Distinguish `F(P)`-evaluation hardness from `e(P)`-counting hardness and from transferring to `S(n)` (antichain root).
- Consider "comparison learning" structure constraints on reductions.

### Blocked
- No concrete all-n encoding found that makes `F(P)` #P-hard without a direct arbitrary-poset reduction, and no proof of poly-time for all reachable `P`.
- Ambiguity of the exact phrase "structure preserved by comparison learning" / "SORT-BOUND-U state graph" in this phrasing.
- Brightwell–Winkler reduction not yet reconstructed to a form that targets `F` (not `e`) under these constraints.
- No independently checkable new theorem/counterexample produced yet.

## Next Move
1. **Test candidate families for invertibility:** Focus on families where information bound is tight or has structure (e.g. certain series-parallel/disjoint unions, or posets where optimal strategy is forced) and see if `F` can encode `e` of a #P-hard instance without leaking arbitrary-poset encoding.
2. **Examine balanced pairs / optimal splits:** Analyze whether exact computation of `F(P)` via minimax requires finding Kahn–Saks/1/3–2/3 balanced splits (which relate to `e` ratios) and whether that forces #P-oracle queries on a hard subfamily.
3. **Check known obstructions:** Review `docs/research-hardness-boundaries.md` Turing-reduction note carefully and attempt to construct a Turing reduction from `#LINEXT` to `F` on derived posets, or find a structural obstruction (comparison-learning constraints) preventing any such reduction.

## Relevant Files
- `AGENTS.md` - Research contract (unary focus, scope)
- `docs/problem.md` - Definitions: `S(n)`, `F(P)`, encodings, minimax correspondence
- `docs/upper-bound.md` - Minimax recurrence for `F(P)`, state graph description
- `docs/operations.md` - Antonina issue #301, `billy-dev` only, board digest
- `docs/research-hardness-boundaries.md` - e vs S, Turing reduction not ruled out, barriers
- `docs/research-series-decomposition.md` - Reachable-from-antichain, ordinal sum
- `docs/research-winning-frontier-barrier.md` - Winning states reachable from antichain
- `docs/research-one-ply-obstruction.md` - `F` vs `e`/information bound
- `SoringP1/Minimax.lean` - Formal minimax `adv`/`minimaxTree`
- `scripts/one_ply_obstruction.py` - Poset experiments (e,F computation)
- `scripts/hardness_boundaries.py`, `tests/test_hardness_boundaries.py` - Barriers/experiments
The previous request exceeded the provider's size limit due to large media attachments. The conversation was compacted and media files were removed from context. If the user was asking about attached images or files, explain that the attachments were too large to process and suggest they try again with smaller or fewer files.

Continue if you have next steps, or stop and ask for clarification if you are unsure how to proceed.
Investigating whether #P-hardness of counting linear extensions (#LINEXT) can be encoded into computing F(P)=minimax comparisons on posets reachable from the antichain (unary SORT-BOUND-U), without a direct arbitrary-poset reduction. 

Read contract/docs, examined Lean's minimax model, tested families in `scripts/one_ply_obstruction.py` (F vs log2 e), and reviewed barriers (Cardinal et al. is approximation; Hyafil–Rivest/Laber–Nogueira don't transfer to pairwise). 

No concrete encoding or obstruction yet—focused on whether "comparison-learning"/state-graph constraints block a Turing reduction from #LINEXT to F(P).

## Other metadata

```json
{
  "finished_at": 1793493885.8436623,
  "started_at": 1793479716.5079153
}
```
