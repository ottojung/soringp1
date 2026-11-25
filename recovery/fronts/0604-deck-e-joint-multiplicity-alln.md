# deck-e-joint-multiplicity-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

wxK2zNyDzvK5XvBAEU3n6U-cirsoid

## exit_state

clearexit

## question

For all sufficiently large n, is the number of poset states lying on a common height-S(n) optimal play from the n-antichain that share BOTH the same linear-extension count e(P) and the same child extension-count deck D(P) bounded by a polynomial in n? Earlier fronts closed e alone and e-plus-width/height as value keys and posed (e,F) state multiplicity, but the joint (e,D) fiber on the optimal-feasible slice is untested.

## basis

Antonina #301 (2026-11-20) posts on optimal-feasible (e,F) and greedy (e,V) state multiplicity and the child-deck soundness fronts all leave the joint (e,D) multiplicity fiber open on S(n)-relevant states; no front in the durable ledger combines the deck with the extension count as a joint state key.

## falsifier

Exhibit, for infinitely many n, superpolynomially many pairwise nonisomorphic optimal-feasible states with identical (e(P),D(P)) but pairwise distinct minimax values F, or prove that every such (e,D) fiber has at most polynomially many states.

## implication

Superpolynomial (e,D) multiplicity would rule out even a deck-refined e-indexed exact evaluator on the states relevant to S(n), strengthening the extension-count collision barrier; a polynomial bound would leave such a deck-keyed evaluator viable.

## finding_unverified

**No theorem or counterexample was established.** The all-\(n\) polynomial bound on the joint \((e(P),D(P))\) fibers over optimal-feasible states remains open.

A precise obstacle is that the child extension-count deck records only local counting data: for each incomparable pair, the two child counts sum to \(e(P)\). But minimax value is determined recursively by the *values* of those children, through \(F(P)=1+\min\max F(P')\). The deck does not supply those values. This observation neither proves that equal \((e,D)\) states can have different \(F\), nor bounds how many such states can occur.

Crucially, a collision among arbitrary posets would not suffice: the states must lie on a height-\(S(n)\) play from the antichain. Likewise, a soundness argument for an evaluator keyed by \((e,D)\) would not establish completeness—that every relevant state can be represented or merged without losing the exact minimax value.

I found no applicable primary-literature result settling this joint fiber question. No repository or Lean changes were made, and I did not post to #301: the board check found no matching post, but this investigation produced no new mathematical result to report there.

## Other metadata

```json
{
  "finished_at": 1795171129.0159879,
  "started_at": 1795170581.1990323
}
```
