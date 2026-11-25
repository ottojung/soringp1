# admissible-split-closure-obstruction

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ahLv5Y90qwvA89e3As4zdY-shoving

## exit_state

clearexit

## question

Let A be the closure under transitive composition of all (e(P'),e(P'')) split ratios achievable by a single comparison in some poset P reachable from the antichain. For all sufficiently large n, does every factorization of n! into factors from A that forms a full comparison tree of height <= C(n)+o(n) violate some global consistency condition (not local Kraft/divisibility) forcing excess >= Omega(n/polylog n)?

## basis

Exact-reset shows divisibility blocks exact splits (research-exact-reset-realizability), winning frontier shows many states exist, but global consistency of the split graph (admissible comparison cuts) is not fully characterized beyond local rules.

## falsifier

Exhibit an infinite family with heights log2(n!)+o(n) whose split ratios all lie in A and satisfy a complete set of local/global consistency constraints realizable by some actual comparison tree structure.

## implication

A general obstruction on the split monoid would constrain how close to the information bound any exact comparison tree can get regardless of certificate compression, complementing Sergeev's upper bound with a necessary condition.

## finding_unverified

ctorization of n! into factors from A that forms a full comparison tree of height <= C(n)+o(n) violate some global consistency condition (not local Kraft/divisibility) forcing excess >= Omega(n/polylog n)?  
> FALSIFIER: Exhibit an infinite family with heights log2(n!)+o(n) whose split ratios all lie in A and satisfy a complete set of local/global consistency constraints realizable by some actual comparison tree structure.  
> COMPLEXITY IMPLICATION: A general obstruction on the split monoid would constrain how close to the information bound any exact comparison tree can get regardless of certificate compression, complementing Sergeev's upper bound with a necessary condition."

If Sergeev's algorithm produces comparison trees of height log2(n!)+o(n) with valid comparison splits, then the falsifier is satisfied - and that would mean the front's obstruction claim is false. That would be a clean disproof. But is this considered "established" in the repo? The repo says "Sergeev's sublinear excess bound" with S(n)=log2(n!)+O(n/(log n)^(1/5)), so this is treated as literature fact. That would directly answer the front in the negative.

Let us start by examining the full picture and then report.

Let us think through this carefully.

Let us examine the evidence and provide a report.

Let us examine the evidence and produce a report.

**Finding (disproof of the front):**  
Sergeev’s group-insertion algorithm gives a deterministic adaptive comparison tree for every $n$ with worst-case height  
$$
S(n) \le \log_2(n!) + O\!\left(\frac{n}{(\log n)^{1/5}}\right)=C(n)+o(n).
$$  
(IGOR S. SERGEEV, *On the asymptotic complexity of sorting*, ECCC TR20-096, Thm. 3; DOI 10.1134/S0965542521020111.) Each node is a comparison on some poset reachable from the antichain, so every split is of the form $(e(P'),e(P''))$ with $P',P''$ children of some reachable $P$ — i.e. in the closure $A$ (and realizable by an actual comparison tree). The factorization down any root-to-leaf path is consistent with a complete sorting tree. This is exactly the infinite family demanded by the falsifier.

**Why this matters:** The front’s conjectured global obstruction forcing excess $\Omega(n/\mathrm{polylog}n)$ is false as stated; near-information $(C(n)+o(n))$ worst-case exact sorting trees are realizable. The repo’s entropy identity is consistent (only $o(n)$ comparisons need significant bias in expectation), but that is not a worst-case obstruction. The complexity implication claimed does not follow from a general split-monoid obstruction.

**Caveats / limits:** (1) Sergeev’s $o(n)$ is asymptotic with unspecified effective constants from the published form (the repo notes extracting finite bounds is separate) — the all-$n$ existence of *some* tree of height $C(n)+o(n)$ is the claim used here. (2) This is a worst-case height bound on comparisons, not an algorithmic time/space bound for *computing* $S(n)$ or for the tree itself; the “computation complexity” of the threshold is a different question (and the front’s complexity implication must be read accordingly). (3) Local divisibility/admissibility constraints remain real (exact-reset shows some transitions impossible), but they do not force $\Omega(n/\mathrm{polylog}n)$ excess for all large $n$ given an actual realizable tree family.

**No repo changes made.** This is a literature-based disproof (paper proof) of the front’s universal obstruction claim; I tried to refute it and the primary literature (Sergeev) does so directly.


## Other metadata

```json
{
  "finished_at": 1793679861.879259,
  "started_at": 1793678329.2470617
}
```
