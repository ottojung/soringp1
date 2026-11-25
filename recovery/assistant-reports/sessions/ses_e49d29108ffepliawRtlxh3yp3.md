# antonina-yDCbVJDshKi8DdiNc1WzKL-shared

Session: ses_e49d29108ffepliawRtlxh3yp3
Workspace: /home/lubko/soring-fronts/exec-fotc-history-eliminate-frame-20261107
Created: 1794057793334; updated: 1794057827470

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 49 (msg_1b62dacdf001W23wM113ZTbuoc)

**Answer: Yes, for this specific candidate, under explicit assumptions.** Nested TC can recover each slot’s original label from the existing cumulative history, without mutable `M` or `AskSlot`. The construction uses the certificate’s static edge permutations and an *actual path whose recorded comparisons are all in `H`*. That path condition resolves joins: different frames may reach the same node, but the current history selects the frame of this execution. It does not require that the frame be unique among all paths to the node.

For clarity, take an augmented domain containing tagged slots, original labels, certificate nodes, and outcomes. Use explicit static relations `Query(q,a,b)`, `Edge(q,o,e,t)`, and `Perm(e,x,w)` (old slot `x` maps to new slot `w`), plus a root marker. Use `H(i,j)` for the accumulated outcome “original label `i` is smaller than `j`.” The annotations below denote distinct variables from one global pool of **9** names; each displayed relation is a separate formula, so names can be reused between formulas.

Define the edge predicate
\[
\begin{aligned}
\operatorname{Step}((u,x,i),(t,w,i')) \equiv {}&
  \operatorname{Query}(u,a,b)\land\operatorname{Edge}(u,o,e,t)
  \land\operatorname{Perm}(e,x,w)\land i'=i\\
 &{}\land\bigl[
 (o=\mathrm{LT}\land ((x=a\land i=a_i)\text{ is not intended}) )
 \bigr].
\end{aligned}
\]
More precisely, to avoid confusing slot names with label variables, the comparison/outcome guard is:
\[
\begin{split}
\operatorname{Guard}(u,x,i,o,a,b)\equiv {}&
 (o=\mathrm{LT}\land ((x=a\land i\text{ is the label at }a)
 \lor(x=b\land i\text{ is the label at }b)))\\
 &{}\lor(o=\mathrm{GT}\land ((x=a\land i\text{ is the label at }a)
 \lor(x=b\land i\text{ is the label at }b)).
\end{split}
\]
That guard, as written, is **not sufficient**: it does not state which labels were compared or that `H` contains the selected outcome. The needed formula must correlate the two slot images with the query’s two labels, then test their outcome in `H`. Concretely it needs, simultaneously, the query’s two slots, their two original labels, and the tracked slot/label, in addition to source and target node/slot/label tuples. Under the draft syntax, the TC endpoint width is already three (`node,slot,label`), so its endpoints consume six names. Even with no outside context, the TC transition formula cannot bind the query slots and both endpoint images within the global pool of nine: the transition requires at least three further distinct bound names. A context assignment for the requested endpoint additionally consumes names.

This is a **specific variable-correlation obstruction** to the direct path-replay TC construction: a transition must verify that one recorded comparison simultaneously identifies both endpoint slot images and its outcome. Repeated queries are harmless only after that correlation is established; cumulative `H` alone does not identify which occurrence supplied the comparison. Permutations being explicit and old-slot→new-slot fixes the direction of frame transport, but does not remove the need to correlate both queried labels.

The draft states no fixed variable bound in advance; the audited candidate chose `v=4` for its primitive-based formulas. For endpoint width three, even the TC syntax condition `a+2m≤v` requires `v≥6`; that necessary condition alone does not prove impossibility at `v=6` or larger. This audit therefore **does not establish a general FO(TC) impossibility**: it rules out the proposed direct replay with the candidate’s four-variable budget, not every encoding or larger fixed pool. Domain augmentation to `N' = Θ(n+k+C+1)` changes neither this variable count nor the correlation requirement.

So the mutable-map elimination requested with an actual formula set and one fixed bound is not obtained here. The frame-store replay remains conditional on its explicit `M`/`AskSlot` primitives; the history-only bridge is still open for a sufficiently larger fixed variable pool or a different encoding. No claim is made about exact-optimal certificate completeness or unrestricted NP/Σ₂P membership.
