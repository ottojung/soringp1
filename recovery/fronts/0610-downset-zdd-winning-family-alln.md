# downset-zdd-winning-family-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

fbs1Zf8sm0Yb7Fzs6HYdxU-foresaw

## exit_state

clearexit

## question

The backward search of Stober and Weiss stores families of down-sets (antichains) of the n-key poset. Can the characteristic family of posets sortable within budget k be represented by a polynomial-size zero-suppressed decision diagram over antichain/down-set variables, uniformly in n and k, or must every such ZDD be superpolynomial under all orderings?

## basis

Board #301 'symbolic-poset-dd-obstacle-20261120' and 's23-bidirectional-feasibility-20261120' posts discuss BDD/ZDD representations and the 3^{n/2}-scale down-set barrier; Stober-Weiss arXiv:2206.05597 section 5.6; docs/problem.md fixes the adaptive comparison model.

## falsifier

Produce a fixed variable ordering yielding polynomial-size ZDDs for all budgets n,k, or establish a superpolynomial ZDD-size lower bound via an antichain or fooling-set argument that is independent of the chosen ordering.

## implication

A uniformly polynomial-size ZDD for the winning family would be a compact exact evaluator and a step toward a smaller-class upper bound; a lower bound would close the decision-diagram compression route that the down-set search suggests.

## finding_unverified

enc_n(F_{n,k})`.
- **Concrete failed/blocked approach (what I attempted in reasoning).** (1) Searched for any existing ZDD/zero-suppressed-DD treatment of `F_{n,k}` or of Stober–Weiss down-set families in this repo: none found. (2) Tried to infer a natural `enc_n` from “antichain/down-set variables”: no standard, unambiguous definition appears; pair-bit encodings were already obstructed on board for BDDs (different variables). (3) Considered the minimax recurrence `m(P)=0` if total else `1+min_{incomp x,y} max(m(P+xy),m(P+yx))`: it suggests game-tree structure but gives no direct polynomial-ZDD guarantee for the characteristic family uniformly over all `n,k`, and no obvious fooling set is isolated without `enc_n`. None of these yielded a theorem or a counterexample.

## Falsifier status (honest)
- “Produce a fixed variable ordering yielding polynomial-size ZDDs for all budgets n,k…” — **not produced.** No candidate `(V_n,enc_n,π_n)` is specified or constructed here.
- “Establish a superpolynomial ZDD-size lower bound via an antichain or fooling-set argument that is independent of the chosen ordering…” — **not established.** Blocked by undefined encoding and absence of a stated Boolean function; no all-order communication/fooling-set argument is derived.

## Complexity implication (from `problem.md`/`AGENTS.md`, conditional)
If one *did* have, for a rigorous encoding, a **uniformly polynomial-size** (in the unary-decision sense relevant to input length conventions for the family description) ZDD representing `F_{n,k}` together with efficient query/operations realizing the minimax threshold test, that would be a concrete compression/evaluator route toward stronger uniform upper bounds for exact `S(n)` evaluation — but this is **conditional** on the encoding and algorithmic details. The opposite (a proven all-order superpolynomial lower bound for the right encoding) would rule out that DD compression route. **Neither is proved here.**

## Conclusion (report)
- **Finding (mathematical/epistemic):** The FRONT states an important compression question, but it is **not yet a well-posed theorem target** without an explicit `enc_n` over an explicit “antichain/down-set variable” universe. The only nearby repo/board evidence is (a) a board obstruction for pair-bit BDDs (no width theorem) and (b) empirical/memory pressure in Stober–Weiss down-set-family search (not a ZDD size theorem). No polynomial-ZDD construction and no all-order superpolynomial ZDD lower bound (antichain/fooling-set, independent of ordering) is obtained.
- **Concrete obstruction:** missing formal encoding + no identified communication/fooling-set witness for any fixed encoding in the reviewed sources.
- **Concrete failed approach:** attempts to treat “antichain/down-set variables” as either (i) the full antichain universe (size non-polynomial, wrong regime) or (ii) an informal substitute for Stober–Weiss stored families (no Boolean `F_{n,k}` ZDD form) fail to produce a checkable claim.
- **Honest limit:** I did not access the full text of arXiv:2206.05597 section 5.6 beyond what appears in repo/docs excerpts and board paraphrases here; if that section states a precise data-structure/variable model, that model must be extracted and then the question re-posed as a precise Boolean/DD problem before a real proof/disproof attempt is possible. No Lean/repo changes were made (and none warranted: no genuinely substantive, independently checkable new theorem/counterexample was produced).

## Other metadata

```json
{
  "finished_at": 1795192050.870008,
  "started_at": 1795191192.6150467
}
```
