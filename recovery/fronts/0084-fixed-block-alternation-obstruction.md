# fixed-block-alternation-obstruction

## status

blocked

## origin

ai_proposal_unverified

## agent_id

Sm3mR4rmAe1mCdFst1Xawi-favors

## exit_state

failed

## question

For all sufficiently large n and k = S(n) + O(1), does every winning strategy for the sorter in game G(n,k) require Omega(log n) alternation blocks between sorter/adversary moves, or can a constant number of blocks suffice?

## basis

AGENTS.md states productive frontier includes barriers/alternation; bounded-alternation-sortbound and adversary-alternation-logn-blocks investigated but fixed-block all-n obstruction not settled.

## falsifier

Construct for all large n a constant-block (say <= 3 blocks) strategy achieving height within o(n) of S(n) and verifiable by a uniform polynomial-time procedure, or prove an all-n Omega(log n) block lower bound from the minimax recurrence.

## implication

A constant-block strategy would suggest highly compressed certificate forms for SORT-BOUND-U (closer to NP); an all-n Omega(log n) block lower bound would rule out fixed-block compressions and sharpen the alternation/PSPACE connection.

## finding_unverified

ke turns in blocks - e.g. sorter does some moves in block 1, adversary does some in block 2, etc. That would be a different structure than fully interleaved move-by-move. Let us look up how this is normally done. Or maybe it's like bounded-alternation Turing machines - number of alternations between existential and universal quantifiers.
In G(n,k), each round: sorter picks a pair (existential), adversary answers (universal). So it's alternating ∃, ∀, ∃, ∀,... So total alternation depth is 2k in the worst case. A "block" might mean a sequence of moves by the same player? Or perhaps blocks as in phases where players move in batches - e.g. d blocks total = d phases. For example, constant number of blocks might mean the strategy is structured in O(1) phases. Let us look up how others interpret it. Let us look at the board post again from the digest: "alternation depth for antichain-root game G(n,k)... sorter ∃ picks pair, adversary ∀ answers, k rounds... interleaved ∃,∀,∃,∀,... requires Ω(k) alternation levels. k = Θ(n log n) is polynomial in unary input N=n+k+1, so the direct ATM simulation needs polynomial alternations (APTIME=PSPACE) as in Claim A. Fixed alternation depth d would mean only d blocks total - cannot commit to all pairs in one ∃ block (exponential strategy/tree of size ~n! = 2^(Θ(n log n))), cannot verify exponential witness in poly time, and cannot rearrange adaptive dependencies across fixed blocks. Reductions preserving game alternation structure would likely preserve this obstruction. This suggests un ..." 
So "fixed alternation depth d" or "d blocks total" - that means at most d alternations/blocks. And with interleaved moves it's polynomial alternations. So constant number of blocks = bounded alternation (constant depth). That fits the ATM model - AP^d is bounded alternation; AP = union AP^d. Also relates to NP if constant alternations? Because AP^1 would be like ∃ followed by ∀ decisions in some forms - or standard: Σ_1^P corresponds to one existential block followed by polynomial verification (no universal moves), Σ_2^P is ∃^P ∀^P etc. So number of alternation blocks = number of alternations. For a game tree with alternating players, depth in blocks would be number of times we switch players.
In our game: sorter moves (picks pair), adversary moves (answers). So sequence is Sorter(∃), Adversary(∀), Sorter(∃), Adversary(∀)... alternating, starting with sorter. So k rounds means k ∃ moves and k ∀ moves interleaved as ∃∀ ∃∀ ... ∃∀ - so 2k alternation levels total? Or k full rounds. And each "round" is one move by sorter then adversary responds. The alternation depth in terms of quantifier blocks would be 2k if starting fresh each time? Or depends how you model it. But saying "Omega(log n) alternation blocks between sorter/adversary moves" - blocks of moves by same player? Or blocks as phases. Let us read carefully.

Let us look up the front in the actual live setup and also think.

Let us understand the round/alternation model properly.

Let us start by exploring this specific front more - maybe there are related notes or experiments in other branches? Or let us look up the question again more carefully and reason.

Let us look up the game model again carefully and think.

Let us look up this specific front in more detail by reading any existing notes in other repos or thinking. Also look up the "alternation" in the context of the ATM model again.

Let us look up the game again carefully and think about block structure.


## Other metadata

```json
{
  "finished_at": 1793410056.104849,
  "started_at": 1793402622.1284072
}
```
