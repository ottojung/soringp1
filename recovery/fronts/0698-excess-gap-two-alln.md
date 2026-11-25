# excess-gap-two-alln

## status

blocked

## origin

ai_proposal_unverified

## agent_id

isblCwWjWWwLYnbmY9LFlI-went

## exit_state

failed

## question

Is the unary excess bounded by 2, i.e. does D(n) = S(n) - ceil(log2 n!) satisfy D(n) <= 2 for every n, and is 2 the largest admissible excess value?

## basis

OEIS A036604/A003070: D(n)=0 on {1..11,20,21}, D(n)=1 on {12..19,22} (n <= 22); Wells S(12)=30 (C(12)=29); Stober-Weiss S(16)=46, S(17)=50, S(18)=54; S(28) >= 99 (C(28)=98). Free-free-second-state-tightness-alln: D(FF_n) >= excess_S(n) >= 0. Sergeev (ECCC TR20-096): D(n)=O(n/(log n)^{1/5})=o(n). Certified merge gaps max out at 2 (Merge(6,10), research-structural-lower-bounds.md) but do not transfer to the antichain root, where D(16)=1. No counterexample to D <= 2 is known for any n <= 22; n >= 23 values are open.

## falsifier

An exact witness n with D(n) >= 3: compute S(n) >= ceil(log2 n!) + 3, or prove F(antichain_n) >= ceil(log2 n!) + 3 structurally.

## implication

If true, the unary threshold language's non-trivial slab is width <= 2: SORT-BOUND-U(1^n#1^k) is decided by O(1) threshold probes around the information bound (accept iff k >= C(n)+2, reject iff k <= C(n)+1), i.e. a uniform polynomial-size certificate of constant slack - a strengthening of excess-one-band-polynomial-decision-alln's P1 (D <= 1); the Mahaney sparsity barrier is unchanged, so no class separation is implied.

## finding_unverified

No final text; audit needed

## Other metadata

```json
{
  "finished_at": 1795397689.5991912,
  "started_at": 1795397625.2797809
}
```
