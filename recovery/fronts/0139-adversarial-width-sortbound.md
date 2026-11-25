# adversarial-width-sortbound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

lMdyzMg8d5idhtfSsMaMge-banquet

## exit_state

clearexit

## question

Is the pathwidth or the adversarial antichain width of the minimax game tree on n elements unbounded as Omega(n / log n) in the worst case over all optimal strategies, and does this force alternation of that depth?

## basis

Sorting game is an alternating minimax process; no investigated front isolates the adversarial width/pathwidth of states as a forcing parameter for alternation depth.

## falsifier

Show that for every n there is some strategy whose state graph has bounded pathwidth independent in effect or whose adversarial width is O(1), or prove width Omega(n/log n) forces the ATM alternation count to be linear in n.

## implication

A width-based obstruction could link the unbounded alternation of the PSPACE ATM simulation to a concrete combinatorial parameter of the sorting game without reducing from arbitrary PSPACE instances.

## finding_unverified

Let us look at the frontier ledger and current literature/research docs.

**Finding (disproof): the premise is false by tree structure.**

- **Model:** A deterministic adaptive sorting strategy is a comparison decision tree (game tree for G(n,k)) whose nodes are sorter/adversary states over partial orders; states reached under the strategy form a **tree** (not a general DAG requiring path decomposition across different branches except the tree itself). The graph-theoretic pathwidth (and treewidth) of any finite tree is ≤ 1, bounded independently of n.
- **Application:** This holds for *every* strategy, including those achieving S(n) (optimal). The “adversarial antichain width” interpretation as graph width is not standard; if meant as poset width, poset width can be large but that is a different parameter (Dilworth) not the graph pathwidth of the strategy tree. The question’s graph-width phrasing is refuted directly by the tree structure.
- **Alternation:** The ATM alternation depth from Claim A in `docs/research-certificates-barriers.md` is equal to the game depth k = height of the strategy tree (alternating sorter/adversary moves), i.e. Θ(S(n)) = Θ(n log n) as function of n. Bounded tree/pathwidth does **not** force large alternation here — alternation is forced by game depth; conversely bounded width is trivial. No width→alternation forcing relation follows from the standard ATM simulation.

**Failed approaches / limits:**
- If “adversarial antichain width” means max poset width under adversary play (Dilworth width), that can be unbounded in general for bad strategies but the question states “of the minimax game tree on n elements” (graph of the tree). Also even if poset width is large, it doesn’t create unbounded graph pathwidth of the strategy tree.
- No known reduction shows graph width forces alternation depth beyond game depth for this comparison game; the direct simulation already uses depth = game depth.
- General-poset hardness doesn’t transfer (AGENTS §Model fidelity). Soundness vs completeness: this is a structural graph property, not a certificate completeness claim.

**Conclusion:** The claim as stated is false. There is no unbounded pathwidth over optimal strategies (all have pathwidth ≤ 1); any alternation depth is the game depth, not forced by an unbounded width parameter. No repository changes needed; this is a clean structural disproof.


## Other metadata

```json
{
  "finished_at": 1793524876.1295922,
  "started_at": 1793524448.2540917
}
```
