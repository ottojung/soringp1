# optimal-path-prefix-invariant-gap

## status

investigated

## origin

ai_proposal_unverified

## agent_id

PfHJx8UfYJrQIWvjtKnM1l-gompers

## exit_state

clearexit

## question

For all sufficiently large n, does there exist a family of reachable poset states on some minimax-optimal path from the antichain with identical extension-count profiles and identical information bounds yet requiring different worst-case comparison budgets to complete to a total order under optimal play?

## basis

Small-n examples show e(P) alone insufficient; antichain-orbit work is running but focuses on identity/forcing, not this prefix-completion cost gap on optimal paths.

## falsifier

Prove that for every reachable state P on any S(n)-optimal strategy, the pair (e(P), F(P)) together with the root-orbit class determines the exact minimax completion cost C(P) for all n.

## implication

A positive all-n result would identify an unavoidable invariant gap for DP compression on optimal paths and constrain any polynomial-state exact recurrence for S(n).

## finding_unverified

oidable invariant gap for DP compression on optimal paths and constrain any polynomial-state exact recurrence for S(n).  
> EVIDENCE: Small-n examples show e(P) alone insufficient; antichain-orbit work is running but focuses on identity/forcing, not this prefix-completion cost gap on optimal paths."

So "extension-count profiles" - in poset terms, sometimes people mean the profile of how many extensions go to each child under different comparisons (the split profile). "identical information bounds" - maybe L0 = ceil(log2 e(P)) same. "requiring different worst-case comparison budgets to complete to a total order under optimal play" - so different minimax completion costs = different F_minimax(P). "pair (e(P), F(P))" - maybe F(P) here means the information bound or some other function F (like L1 from one_ply_obstruction)? Let us look up one_ply_obstruction again: it defines L0 = ceil(log2 e(P)) (info bound) and L1 = 1 + min over pairs of max(L0 of children). Also calls L1 "one-ply adversarial information bound". Could F(P) in the falsifier refer to L1 or some other function? Or could it refer to the minimax value? Let us look up how the codebase uses notation - in some texts F is minimax, in others people use different letters. Also "completion cost C(P)" - maybe C(P) is the actual minimax cost F_minimax(P). The falsifier says (e(P), F(P)) together with root-orbit class determines C(P). So three things determine C(P)=minimax cost. That means if you know e(P), and you know F(P) (some other function), plus root-orbit class, that determines the true minimax completion cost. That would be a kind of "compression": these invariants suffice. The question is asking if there exists states (on optimal paths) with identical extension-count profiles and identical information bounds but different completion costs - so "extension-count profiles" same as the profile of splits (so all child extension counts same?), "information bounds" same (so all L0 values same?), leading to different completion costs. That would mean the detailed profile doesn't determine cost. And the falsifier is trying to prove the opposite in some strong form.

Alternatively need to interpret precisely. Let us look up existing usage patterns from other fronts - "extension-count profile" might refer to the function/value related to e across the state. Let us look up more of the one_ply_obstruction and n12 notes again.

Let us test systematically.

Let us think: is there any known fact that on optimal paths, (e, L0, root orbit) don't determine minimax cost? Or is there some barrier?

I studied the repo, AGENTS/docs, board context, and the frontier as given. Searched for existing uses of “extension-count profile”, “root-orbit class”, “completion cost C(P)”. Checked literature (n12 non-tightness, winning-frontier barrier, framed certificates) and examined the minimax structure. On minimax-optimal paths from the antichain for n≤6, I looked for states with identical (e, L0=ceil(log2 e), split profiles of child e values, isomorphism/root-orbit classes) but different minimax completion costs F(P); no counterexamples found under these encodings. The falsifier would mean (e, F’, root-orbit) determines minimax cost C(P) — also holds for tested candidates on optimal paths up to n=6. But finite search can’t disprove an “all sufficiently large n” claim, terminology may admit other encodings, and proving/disproving for all n is a structural theorem beyond small enumeration. No repo changes made.

## Other metadata

```json
{
  "finished_at": 1793785627.4832206,
  "started_at": 1793780348.242862
}
```
