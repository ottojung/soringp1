# excess-two-realization-alln

## status

blocked

## origin

ai_proposal_unverified

## agent_id

eeBtFhnlTrwZ02lsLkaGGn-republic

## exit_state

failed

## question

Does the antichain ever realize excess 2, i.e. is there n >= 23 with D(n) >= 2, and if so is gap-2 slack the generic regime for large n?

## basis

Same known data as excess-gap-two-alln (D(n) <= 1 for all n <= 22, including Wells S(12)=30, Stober-Weiss S(16)=46/17=50/18=54). Smallest certified merge gap is 1 (Merge(2,4), research-structural-lower-bounds.md sec. 4); Merge(6,10) reaches gap 2 as a general-poset result that does not transfer to the antichain root (D(16)=1). Distinct from excess-gap-two-alln (universality) and non-tight-infinitely-often-alln (D >= 1 infinitely often).

## falsifier

Exhibit n >= 23 with D(n) >= 2: exact S(n) >= ceil(log2 n!) + 2, or a gadget family with F(P) = C(n) + 2 at the antichain root.

## implication

If gap 2 is realized, any decision scheme must distinguish true gap-2 states - the width-2 slab cannot be 'all true states are width <= 1' - and a poly certificate must prove D(n)=2 without computing the minimax value itself; if gap 2 never occurs, then D(n) <= 1 on all n >= 23, completing the P1 picture after its open end.

## finding_unverified

I'll start by confirming the environment (host/user), then study the board and docs.
I'm on billy-dev as expected. Now let me study the board and the docs.
Now let me get the board digest (board #301) and read the key docs in parallel.

## Other metadata

```json
{
  "finished_at": 1795397689.8205109,
  "started_at": 1795397626.1403983
}
```
