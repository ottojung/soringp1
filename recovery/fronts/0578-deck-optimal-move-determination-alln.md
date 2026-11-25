# deck-optimal-move-determination-alln

## status

investigated

## origin

executive_derived_open_lemma

## agent_id

q8GbF4Aaidwp72uQnTDxAJ-endorse

## exit_state

clearexit

## question

Does the child extension-count deck D(P) determine the minimax-optimal incomparable-pair set O(P) = {{x,y}: F(P)=1+max(F(P+x<y),F(P+y<x))}, for all n, both over arbitrary posets and over states reachable from the n-antichain on optimal play? Decide or exhibit an explicit pair P,Q with D(P)=D(Q) but O(P)!=O(Q).

## basis

Board #301 19:30Z deck-child-closure-alln finding (verified 19:33Z) proved child-closure false with an explicit n=4 witness and left open whether a deck method avoiding suboptimal children can accelerate exact S(n); deck soundness (D determines F) verified through n=6 at 19:08Z. No ledger front asks whether D determines O.

## falsifier

Explicit posets P,Q (preferably both reachable) with identical child extension-count decks but different sets of minimax-optimal comparisons; a positive answer requires a uniform all-n argument for arbitrary posets and for reachable states.

## implication

If the deck determines optimal queries, a deck-indexed evaluator can expand only optimal children (whose decks lie in the reachable deck set) and the compression route survives the verified child-closure failure; if not, even among reachable states, that route is fully closed. Either settles the last surviving deck-based approach to compact exact S(n) evaluation.

## finding_unverified

Now let me find whether a genuinely non-isomorphic (not just relabelled) reachable pair can share a deck with different optimal sets.
Let me verify the child-deck signature agreement on the non-isomorphic witness, and check the deck-entry-to-child-deck matching.
All verified. Before posting, I must scan all of #301 for the exact author to avoid duplicates.
No duplicate author found (0 hits across 3030 messages). Let me check the antonina post syntax.
Everything checks out. Let me now compose the single board comment, then post it.
Now I'll post the single comment with the exact required author, redirecting JSON output to a file.
The post appears to have succeeded. Let me verify the saved result and confirm exactly one comment with my author, and that the worktree stayed clean.
Done. Here's a concise report of the completed front.

## Outcome: NO — the deck does not determine the optimal move set

Decided for **both** arbitrary posets and optimal-play-reachable states, with an explicit hand-checkable n=4 falsifier whose two witnesses are both reachable.

**Main falsifier.** P = {1<2, 3<2} on {0,1,2,3} with 0 isolated (e=8, F=3, reachable via A₄ → query{1,2} → query{2,3}). Its only minimax-optimal query is {1,3} (both children F=2), so O(P)={(1,3)} and D(P)=((2,6),(3,5),(3,5),(4,4)). Applying σ=swap(2,3) gives Q={1<3,2<3} (e=8, F=3, reachable) with **D(Q)=D(P)** but **O(Q)={(1,2)}**.

**All-n argument [deduction].** D is invariant under the full Sₙ relabelling action; O is only equivariant. A label-blind multiset cannot determine a labelled argmin set — a type mismatch, not a small-n accident. Distinct from soundness: D does determine F, just not the argmin as labelled pairs. A non-isomorphic reachable collision at n=5 confirms it isn't only relabelling.

**Surviving nuance [experiment, n≤6 only].** Although D can't name the labelled pair, through n=6 it *does* determine |O|, the multiset of child decks, and the multiset of paired child decks per query (0 fiber splits each). That means a pure-deck minimax recursion would be well-defined *if* that fiber-invariance held for all n — left as an explicit open question, not claimed. No complexity gain (decks are already 2^{Θ(n²)}).

## Verification & process
- From-scratch engine (bitmask Warshall closure, one-point-extension generation, subset-DP + independent brute-force n! extension counts, memoized minimax, reachable BFS). Reproduced posets 3/19/219/4231/130023, decks 2/4/11/34/155, S=5/7/10, |R|=181/1551/65551, reachable decks 8/11/61, zero F-mixing fibers — all board matches.
- Sourced `/home/lubko/.profile` before every Antonina call; scanned all 3030 board messages (0 prior posts by the exact author); posted **exactly one** comment with author `SoringP1 frontier: deck-optimal-move-determination-alln` at 19:56:07Z.
- Worktree clean at base `6a96398`; scratch confined to `/tmp/opencode/deckmove`; no repo/Lean/test/workflow/ledger/main changes. No theorem completion, class separation, complexity result or S(n) bound claimed.

## Other metadata

```json
{
  "finished_at": 1795118214.3905122,
  "started_at": 1795117543.7153444
}
```
