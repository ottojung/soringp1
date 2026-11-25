# sergeev-effective-pruning-completeness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

01FZnUAlr9i5O8vBfiHVKk-pregnancy

## exit_state

clearexit

## question

For all sufficiently large n, does there exist an explicit uniform polynomial-time (in n) procedure that certifies S(n) >= C(n) + f(n) with f(n)=omega(log n) using only effectively computable constants from Sergeev's asymptotic, or is non-effectivity unavoidable for any such all-n certificate?

## basis

docs/research-sergeev-asymptotic.md notes non-effectivity blocks concrete (n,k) pruning; sergeev-effective-finite-bound is blocked with no extracted finite form.

## falsifier

Prove that no Turing machine using only Sergeev's published O(·) parameters can produce an effective all-n lower certificate of the form above, or construct an explicit effective all-n procedure achieving f(n)=omega(log n).

## implication

An effective finite form would yield a uniform pruning test for SORT-BOUND-U and tighten the search window; a proven obstruction to effectivity would be a barrier limiting asymptotic bounds to non-constructive guidance.

## finding_unverified

nly published $O(\cdot)$ parameters”. 

3) **Soundness vs completeness / general posets.** Any candidate must be careful: results about arbitrary partial orders do not transfer to the antichain root without reduction (AGENTS/model fidelity). The winning frontier is a poset-state counting phenomenon (enumeration barrier) — relevant to search, not obviously to constructing a uniform polynomial-time *lower certificate* from Sergeev’s asymptotic parameters. Also certificate *soundness* (does it actually prove $S(n)\ge g(n)$ for all large $n$ given only those parameters?) vs *completeness* must be distinguished.

4) **What’s feasible vs blocked.** Constructing an *explicit effective all-n procedure* achieving $f(n)=\omega(\log n)$ would require a new worst-case lower-bound argument (not just quoting Sergeev’s upper bound) that is effective and uses only his published parameters. I know of no such argument in the repo/literature cited; extracting finite constants from the constructive proof is nontrivial and not present. Conversely, proving non-effectivity is a meta/complexity-of-description obstruction: if the only information is the asymptotic form with unspecified constants, no TM can compute a uniform effective constant/threshold function from “published $O(\cdot)$ parameters” alone to guarantee the inequality for all large $n$ — but one must be precise about what “using only effectively computable constants from Sergeev’s published $O(\cdot)$ parameters” means (the theorem statement vs the full proof). 

### Concrete conclusion
- **Most plausible answer:** non-effectivity is unavoidable under the restriction “using only Sergeev’s published $O(\cdot)$ parameters”. The published form provides an asymptotic upper bound on $S(n)$ but no explicit finite constants/function; turning $O(n/(\log n)^{1/5})=o(n)$ into an effective all-n lower certificate $S(n)\ge C(n)+\omega(\log n)$ is not possible from those parameters alone without extracting a finite effective bound from the constructive proof (a separate task not done). The entropy expectation bound is not a worst-case certificate. 
- **Failed/blocked approach identified:** trying to read off a lower bound on excess from Sergeev’s $o(n)$ excess upper bound is the wrong direction; trying to use only the $O(\cdot)$ form (no constants) cannot yield a uniform polynomial-time testable certificate for all large $n$. 
- **No new theorem/counterexample produced here.** I did not construct the explicit procedure and did not formalize a full non-effectivity proof — the obstruction is the stated effectivity gap in the docs. Any rigorous resolution would need either (a) an explicit finite form extracted from Sergeev’s proof (with constants) enabling such a certificate, or (b) a theorem showing that asymptotic $O(\cdot)$ alone is insufficient (meta-theoretic) under that restriction. 
- **Complexity implication (as stated):** effective finite form would help uniform pruning for $SORT\!-\!BOUND\!-\!U$; proven non-effectivity limits asymptotic bounds to non-constructive guidance (consistent with $SORT\!-\!BOUND\!-\!U\in PSPACE$ frontier).

**Honest limit:** this is a known blocker in the repo, not resolved by this analysis. No repository changes made. The question remains open; the cleanest falsifier is (b) a precise non-effectivity argument about the information content of “published $O(\cdot)$ parameters” vs extracting constructive constants, but that requires care to distinguish the theorem from its proof.

## Other metadata

```json
{
  "finished_at": 1793339015.383565,
  "started_at": 1793338829.6041162
}
```
