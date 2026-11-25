# framed-dag-completeness-alln

## status

investigated

## origin

executive_proposed

## agent_id

jffm97iXXBZOgxQp0ruXG5-gravel

## exit_state

clearexit

## question

For every n and every optimal (or height-S(n)) adaptive comparison strategy, does there exist a polynomial-size permutation-framed DAG strategy equivalent on all input orders, with a polynomial-time uniform construction, making SORT-BOUND-U in NP under some polynomial encoding? Or is there an all-n obstruction to uniform polynomial completeness?

## basis

Framed DAG checker exists (scripts/check_framed_strategy.py); docs/research-framed-certificate-frontier.md states optimal-size completeness is open; NP/coNP membership is a genuine upper-bound question distinct from hardness.

## falsifier

Prove for all-n that some infinite family of optimal strategies requires superpolynomial framed-DAG size under every uniform framed encoding, or show the proposed completeness is false for large n despite soundness of the local checker.

## implication

All-n polynomial completeness would establish membership of SORT-BOUND-U in NP (a major upper-bound result); an obstruction would rule out a natural compressed-certificate route without claiming class separations.

## finding_unverified

generic-poset construction; it is not proved to be forced along any optimal root sorting strategy." 

So up to permutation/symmetry, many different histories collapse. That suggests compression is possible if you use the frame structure well. The question is whether it's possible for *every optimal strategy*.

Let us think systematically about the claim.

Let us analyze the question carefully.

Let us look up more about this specific construction and whether it's realizable by an optimal strategy.

**Finding (deduction + literature): no all-n proof of polynomial completeness; a natural obstruction is the winning frontier, but it does not force superpolynomial size for *every* optimal strategy under the framed (intersection+permutation) model.**

**Distinction:** certificate *soundness* (checker accepts only correct height-k strategies) is established; *completeness* (every optimal/height-S(n) strategy has some polynomial-size framed-DAG representation, uniform) is open. NP membership of `SORT-BOUND-U` would follow from all-n polynomial completeness + sound polynomial checker; failure of completeness rules out that route without implying class separations.

**Why completeness is nontrivial:** for a single optimal policy the labelled-poset tree has no hash-consing possible (distinct nodes => distinct labelled poset states; Theorem 2.6 in `research-strategy-certificates.md`). Quotienting by label symmetries can compress but counts grow quickly for `n≤6` and appear super-polynomial in trend; the framed model adds *intersection of guaranteed relations at joins* and *permutations* (forgetting information) which is strictly more powerful than identical-poset sharing.

**Obstruction candidate:** the winning frontier (`research-winning-frontier-barrier.md`) shows there are `2^((1/4-o(1))n (log n)^2)` nonisomorphic reachable winning states at the same depth (even at exact `S(n)`). If some infinite family of optimal strategies were forced to traverse states that remain distinguishable under every possible intersection+permutation merge (and cannot be identified without losing correctness/equivalence), that would force superpolynomial framed-DAG size. However:
- The frontier is an enumeration barrier for *methods that list states*, not a proof that *every* strategy must list them.
- Framed DAGs can merge via intersection (forgetting details) while remaining correct; the `e(P)`-counting/forgetting analysis in `research-framed-certificate-frontier.md` shows exponential classes can collapse with tiny information loss in structured cases.
- No theorem shows forced distinguishability for all optimal strategies; conversely no all-n polynomial completeness theorem exists.

**Concrete failed/blocked route:** trying to derive a general all-n compression is blocked by the lack of a canonical state invariant preserved by joins+permutations for arbitrary optimal strategies, and by the tension between the tree's information-carrying history and the intersection's forgetting. The falsifier is not obviously discharged - the frontier is suggestive but not decisive against the framed representation.

**Honest limits:** I cannot produce a proof of obstruction or a proof of completeness from the reviewed material. The decisive question is: is there some infinite family of optimal strategies that is *incompressible* under guaranteed-relation intersection+permutations? Without a formal equivalence/merge condition, this remains open. No repository/Lean changes proposed.

## Other metadata

```json
{
  "finished_at": 1793517973.594253,
  "started_at": 1793516994.9979768
}
```
