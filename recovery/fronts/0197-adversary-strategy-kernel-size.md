# adversary-strategy-kernel-size

## status

investigated

## origin

ai_proposal_unverified

## agent_id

iwyo1lwIz9dGFVdAclEPVn-unwell

## exit_state

clearexit

## question

For the universal (adversary) player in the minimax game for S(n), is there an all-n family of reachable states where every optimal adversary strategy requires a description of size exponential in n, while some suboptimal adversary strategy is polynomially describable?

## basis

Winning frontier gives many winning states but adversary-optimal paths differ; adversary strategy compression fronts looked at related issues without isolating this exact kernel-size question.

## falsifier

Prove that optimal adversary strategies admit a polynomial-size canonical representation for all n, or construct an explicit polynomial-size optimal adversary strategy for all reachable states.

## implication

Exponential adversary-strategy size would strengthen alternation-based arguments about certificate nontriviality; polynomial representation would suggest the game is more compressible than the winning frontier alone indicates.

## finding_unverified

 optimal adversary strategy must pick a max-$F$ direction on every state; if different states in the same class require different optimal moves and moves are not locally inferable from a small class label while preserving optimality for some root-optimal play, then no $\mathrm{poly}(n)$-size class-based (canonical quotient) representation of *any* root-optimal adversary strategy exists. The description cannot be compressed below listing behavior on an exponential antichain of “move-incompatible” winning states.

**Failed/suspect approaches to disprove (falsifier):**
- **Minimax recurrence as “polynomial description”:** Writing $g(P,(i,j))=\argmax_d F(P\cup d)$ is a short mathematical rule, but if “description size” means the *strategy object* size this is circular; more directly, you can’t just cite $F$ unless $F$ itself is represented compactly. The question targets the strategy’s description complexity.
- **Fixed total order / balancing by $e(P)$:** These are polynomially describable rules but **suboptimal** when $S(n)>\lceil \log_2 n!\rceil$ (the $n\ge12$ gap). Balancing by linear extension counts is also hard to evaluate exactly but the *rule* is short; however exact optimality fails in the gap regime. The front requires optimal (not just suboptimal) strategies to need exponential description.
- **Global invariants:** No scalar invariant ($e, width, \#min,\#max$) is sufficient ([research-obstruction-next.md](docs/research-obstruction-next.md)); merge/poset structure gives unbounded local gaps. This suggests invariants don’t compress the move function.

**Exact obstruction / honest limits:**
- **No full proof of exponential strategy size exists yet.** The move-disjointness/incompatibility for the explicit independent-edge winning frontier under *all* coarser quotients preserving optimality is a natural conjecture but not rigorously established here. Also certificates need not be quotient-based (non-quotient compact representations are not ruled out).
- **Distinction is crucial:** The frontier is about *state counts* (enumeration barrier) — that’s stronger in some forms but different from “strategy description size”. The link is plausible but not identical.
- **Model note:** “Optimal adversary strategy” means achieving the minimax value $F(P)$ (forcing $S(n)$). The fixed-π strategy is not optimal as an adversary in the standard adaptive sense; the relevant suboptimal polynomial strategy is e.g. an $e(P)$-balancing (information-theoretic) rule or any simple invariant-based rule that is exact only when tight.

**Conclusion:** The FRONT is a coherent barrier hypothesis consistent with the winning frontier + quotient obstructions. I found no explicit polynomial-size canonical representation for all-$n$ optimal adversary strategies, and natural compressions fail on move-incompatible winning states; however I cannot produce a rigorous all-$n$ proof of exponential description size or a counterexample construction today. The clean falsifier would be either (a) an explicit all-$n$ polynomial strategy defined via a non-quotient canonical invariant computable in $\mathrm{poly}(n)$ that achieves $F(P)$ on all reachable states, or (b) a general theorem showing minimax strategies compress for this poset game. Neither is evident from current literature; the move-incompatibility argument is the strongest concrete obstruction but remains to be formalized for the exact winning frontier family. No repository/Lean changes are warranted by this analysis.


## Other metadata

```json
{
  "finished_at": 1793639000.1555066,
  "started_at": 1793635988.6968656
}
```
