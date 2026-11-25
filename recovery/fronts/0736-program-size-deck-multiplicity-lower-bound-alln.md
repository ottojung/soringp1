# program-size-deck-multiplicity-lower-bound-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

XRvtrGPNCcU4lTmX7PO2af-kochubey

## exit_state

clearexit

## question

For all sufficiently large n, must every fixed-interpreter FO(TC) strategy program that sorts the n-antichain within S(n) comparisons have text size Omega(D(n)), where D(n) is the number of distinct child extension-count decks over states reachable on height-S(n) optimal play, or can transitive-closure queries compress arbitrary deck-indexed move choices into poly(n) program size despite superpolynomial deck multiplicity?

## basis

docs/research-fo-tc-strategy-programs.md sections 4-6 (newest repo note, committed Nov 2026) conjectures poly-size optimal sorters and names branch asymmetry as a refutation route; board #301 deck-multiplicity findings in reachable-depth-two-profile-f-completeness-alln and the deck-class/superpoly-collision fronts supply the reachable-state quantity. This connects two previously separate programs rather than repeating either; it is descriptive-complexity/general-poset in evidence, with the antichain bridge left explicit and unproved.

## falsifier

Give an all-n family of optimal sorters whose FO(TC) program text is o(D(n)) while the reachable optimal-play deck count D(n) is superpolynomial, exhibiting genuine compression; alternatively prove a lower bound forcing program size to track deck multiplicity on that reachable set.

## implication

If program size must grow with deck multiplicity and D(n) is superpolynomial, the FO(TC)/Sigma_2^P route to a succinct certificate for SORT-BOUND-U fails for all large n, refuting the completeness conjecture of the FO(TC) note; a poly-size program would instead support such a certificate. Soundness of any executing program is immediate; completeness is the open crux, and no antichain reduction or complexity-class placement is asserted.

## finding_unverified

teness question is whether some poly-size FO(TC) family selects optimal moves for all large n. A superpolynomial `D(n)` would rule out only programs that *essentially enumerate deck classes by reading D_e*. It would **not** rule out programs that compute an optimal move by an FO(TC)-expressible invariant different from D_e, nor programs that exploit structure of reachable states. The small-n max-min-e optimality suggests the *information* may compress to a simple split rule, but that rule itself needs e and so is not FO(TC)-implementable.

### 5. Why this does not settle the front

- I did **not** produce an all-n family of poly-size optimal FO(TC) programs (that would be Conjecture C / a major completeness result).
- I did **not** prove `D(n)` is superpolynomial. The deck-class board result is only finite evidence through n=7 / height-two proxies.
- I did **not** prove an unconditional Omega(D(n)) lower bound, nor rule it out. I identified a model mismatch in the *mechanism* suggested by the front: literal deck-indexed branching is not FO(TC)-realizable because D_e is #P-hard to compute.
- I did **not** give an antichain reduction or any complexity-class placement for SORT-BOUND-U. A barrier to one certificate route is not NP/completeness/EXPTIME separation.

### 6. Sharpened falsifiable question (proposed)

Replace "deck-indexed move choices" by an **FO(TC)-distinguishable** invariant: let `I_k(P)` be the FO(TC)_k-type / bounded-rank invariant of the labelled poset structure P (or another poly-time computable invariant). Ask: for reachable optimal-play states, does any poly-time-computable invariant I with poly(n)-many values determine an optimal move, or is there an all-n family requiring superpolynomially many I-classes? This separates *information content* (D_e, #P-hard) from *interpreter-accessible information* (FO(TC)/poly-time), which is the actual completeness bottleneck per note §§2,4,6.

## Concrete failed / limited approaches

1. **Direct D_e-indexed lower bound**: fails as stated because D_e is not readable by a poly-time/FO(TC) interpreter (Brightwell-Winkler #P-completeness). Not a refutation of all lower bounds, only of this mechanism.
2. **Max-min-e split as compression witness**: optimal on R(5),R(6) by probe, but uses e(P) — #P-hard, so not an FO(TC) program rule. Cannot be promoted to the front's falsifier.
3. **All-posets balance probe**: attempted exhaustive/random test; script had bugs then was killed by timeout/resource limits. No result obtained; not needed for the reported obstruction.
4. **Web search**: unavailable/cancelled in this environment; relied on local note, local literature.md, and Wikipedia summary for Brightwell-Winkler identification.

## Honest limits

- **No new theorem/counterexample establishing the front either way.** The reported obstruction is a model-mismatch/expressiveness observation grounded in standard complexity facts; it does not close the FO(TC) completeness conjecture.
- **#P-completeness is a complexity assumption boundary**: "FO(TC)/poly-time cannot compute e" is conditional on standard separations (NL != P#P, FP != #P); I did not prove an unconditional separation.
- **Small-n data n<=6 only** for the new probes; board already had up to n<=7/9 in related fronts. No extrapolation.
- **No repo/Lean/board changes made.** Per AGENTS, nothing here crosses the publication gate as a substantive new theorem/counterexample; it is a precise obstruction to report back to the frontier/board.

## Other metadata

```json
{
  "finished_at": 1795475414.9916012,
  "started_at": 1795473472.8713255
}
```
