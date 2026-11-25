# transitive-closure-subquadratic-alln-barrier

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Ss4zu9L8gdxwMyvLeHP673-planning

## exit_state

clearexit

## question

For every uniform exact evaluator of S(n) that maintains dynamic transitive closure over all adversarial comparison outcomes from the antichain, must the total update+query cost be Omega(n^2 / log^c n) per comparison on some infinite family of instances for all sufficiently large n?

## basis

Transitive-closure update cost is a known bottleneck for the budgeted/DP approach; no all-n unconditional barrier for this exact game structure appears in investigated fronts.

## falsifier

Exhibit a uniform data structure achieving o(n^2 / log^c n) amortized exact transitive-closure maintenance for all legal comparison sequences arising in G(n,k) and integrate it into a correct exact evaluator with no loss of precision.

## implication

A proved all-n subquadratic barrier would rule out a broad class of efficient exact evaluators and explain the apparent gap between naive reachability and practical performance without claiming P!=PSPACE.

## finding_unverified

**Mathematical finding (disproof of the front claim):** The alleged all-`n` barrier is false in the standard RAM/uniform model. For incremental transitive closure (the only updates that occur here: edge insertions when we learn a comparison result, never deletions) Italiano’s algorithm maintains exact reachability in **O(n) amortized time per edge insertion** for directed graphs (and hence for the partial-order DAGs produced by adversarial comparison sequences from the antichain). Each sorting comparison is exactly such an insertion; queries (comparability) are O(1) if using a reachability matrix. Consequently **O(n) per comparison** is achievable with no loss of precision, which is `o(n^2 / log^c n)` for any fixed `c`. The “bottleneck” is therefore not inherent to TC maintenance over comparison outcomes, but to **naive recomputation** (e.g. BFS/DFS from scratch per update/query).

**Distinctions:** This is a **general-poset/incremental-graph** algorithmic fact (Italiano 1986), not a fact special to `S(n)`’s numeric values except the incrementality and partial-order structure (both of which are *easier* than arbitrary incremental graphs). We do **not** conflate certificate **soundness** (the TC is exact) with **completeness** of any proposed NP certificate for `SORT-BOUND-U` (the latter remains a separate question). The claim would need to hold for “every uniform exact evaluator”, but a standard method already violates the Ω(n²/log^c n) per-comparison lower bound; to salvage the front one would need to restrict the model (e.g. pointer machine without the structures used, or some other resource model) in a way that is not stated and that is not the usual model for “uniform exact evaluator” of a function/decision problem.

**Primary literature (relevant):**
- G. F. Italiano, “Amortized efficiency of a path retrieval data structure”, *Theor. Comput. Sci.* 48 (1986) 273–281 (incremental transitive closure).
- Wikipedia page on “Dynamic transitive closure” states Italiano’s incremental algorithm runs in O(n) amortized per insertion.

**Honest limits:** 
- I did not implement/integrate this into a full `S(n)` evaluator here (the user asks for study/attack/disproof argument, not repo changes). The integration is straightforward in principle (replace naive TC with an incremental structure) but the true cost of computing exact `S(n)` is dominated by the **exponentially many partial-order states** in the game tree/DP, not by O(n) per comparison. 
- If the front assumes a model where TC must be maintained in a particular representation or charges differently, it needs to be made explicit; as stated it is refuted by known results. 
- No all-`n` unconditional class separation follows from this (and AGENTS.md correctly warns against expecting P≠PSPACE from TC costs alone). 

**Concrete failed/obstructed angle:** No obstruction found to O(n) per comparison; the obstruction would be to find a model where Italiano-style incremental maintenance is impossible. None is apparent from the stated front.


## Other metadata

```json
{
  "finished_at": 1793767542.7592652,
  "started_at": 1793767227.2295861
}
```
