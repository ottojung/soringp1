# winning-family-obdd-order-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

jeEythCwoCGToerrrvrOMS-segments

## exit_state

clearexit

## question

Let W_d be the Boolean function that is true exactly on labelled n-key posets sortable within d adaptive comparisons, encoded by the fixed pair-lex ternary relation bits. Does there exist any fixed variable order under which every W_d has a polynomial-width ordered binary decision diagram uniformly in n and d, or is the minimum width over all orders superpolynomial for an infinite family of (n,d)?

## basis

Newest board #301 posts 'fixed-order poset BDD' (2026-11-20T15:05Z) and 'symbolic-poset-dd-obstacle-20261120' raise this exact encoding-specific DD question and report only a precise obstruction, not a width theorem; docs/problem.md fixes the model and docs/operations.md describes the curator role.

## falsifier

Either exhibit one fixed variable order whose OBDD width is polynomial for all W_d, or prove a superpolynomial width lower bound (e.g. via a fooling-set or rank argument) that holds simultaneously for every variable order.

## implication

A uniformly polynomial-width, polynomial-time constructible OBDD for the exact winning family would decide SORT-BOUND-U in polynomial time; an all-order width lower bound would rule out the fixed-order decision-diagram route to a faster exact evaluator.

## finding_unverified

er bound for some family `(n,d(n))` one needs, for **every** variable order `π` on `V_n`, some cut/prefix with superpolynomially many subfunctions of `W_{n,d}` (a fooling-set/rank/1-way-communication obstruction uniform over all `π`). 
- For `TOT_n=W_{n,0}`, the opposite-constraint argument above shows many vertex-split prefixes force distinctions, but a variable order may interleave bits/pairs across vertices; a full all-order theorem would have to account for arbitrary interleaving while transitivity couples non-adjacent pairs globally. I did not obtain (and do not claim) such a theorem.
- For `d ≥ 1`, `W_{n,d}(P) ≡ [∃(u,v)∈Inc(P): W_{n,d-1}(P+u<v) ∧ W_{n,d-1}(P+v<u)]` is an alternating/game value over the same relation bits: the relevant “information” a prefix must retain is not a local visible-pair count but the exact minimax winnability consistent with all completions, against an adaptive adversary/chooser (soundness/completeness of any summary is the issue). Known failures of scalar/leaf-count invariants to determine `F(P)` (e.g. `e(P)` insufficient; `S(12)>⌈log₂ 12!⌉`, per `docs/literature.md`/notes) indicate the value is strictly stronger than information-theoretic counting, but this is an **obstruction to naive summaries**, not an all-order OBDD width lower bound.
- Conversely, route (1) would require a fixed scan order and a polynomial-state invariant computable read-once from pair bits that is complete for `F(P) ≤ d` for all `P,n,d`; no such invariant/order is exhibited, and `F(P)` is not determined by coarse invariants (above).

## Concrete failed approach (this pass)
- **Attempted:** promote the pair-lex `2^{n-1}` subfunction argument (Case I/II/III, proved above for the `n-1` vertex-1 pairs prefix) to an all-order superpolynomial lower bound for `TOT_n` or some `W_{n,d}`, e.g. by finding, in every order, a vertex/star cut or a balanced partition with a large fooling set despite arbitrary interleaving and transitivity. 
- **Outcome:** failed to produce a complete all-order argument. The obstruction is precise: arbitrary `π` can distribute/incur pair bits so that the “vertex-split” opposite constraints are not presented as a single pure prefix of the same simple form, and I lack a reduction showing every induced cut still carries superpolynomial residual dependence for this transitive/game-defined family. Therefore this remains a **precise obstruction**, not a theorem.

## Honest limits / status
- **Not proved:** existence of any fixed polynomial-width (uniform in `n,d`) variable order for all `W_{n,d}`. **Not proved:** a superpolynomial OBDD width lower bound holding simultaneously for every variable order for any infinite family `(n,d)` (the asked all-order falsifier). The front remains **open**.
- **Established here:** a rigorous, independently checkable all-`n` lower bound `width_{π_lex}(W_{n,0}) ≥ 2^{n-1}` (pair-lex order), falsifying that specific natural order; and a clarified separation between (i) this fixed-order obstruction, (ii) the unproved all-order DD question, and (iii) general-poset / certificate-soundness observations (which do not imply completeness or an OBDD width theorem).
- No repository/Lean changes were made (nothing here meets the publication gate as a new theorem/counterexample resolving the front or a necessary model fix). Any further claim would require either an explicit poly-width order+proof (route 1) or a verified all-order fooling-set/rank lower bound for a concrete `(n,d)` family (route 2).

## Other metadata

```json
{
  "finished_at": 1795192114.579113,
  "started_at": 1795191191.6650152
}
```
