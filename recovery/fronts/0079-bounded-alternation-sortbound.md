# bounded-alternation-sortbound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

FC2scXp6sNS7FIgvAHDVwu-reminding

## exit_state

clearexit

## question

For SORT-BOUND-U modeled as the bounded-depth alternating game G(n,k), is there a fixed constant d>=1 with SORT-BOUND-U in Σ_d^P union Π_d^P for the relevant encodings, or does the antichain-root game require unbounded alternation depth under any polynomial-time reduction?

## basis

Claim A in docs/research-certificates-barriers.md uses APSPACE=PSPACE with polynomial alternations; AGENTS.md notes alternation game structure is central to minimax.

## falsifier

Show unbounded alternation is necessary via a reduction preserving the game alternation structure, or conversely exhibit a fixed-level alternating algorithm for G(n,k) with polynomial time in unary N.

## implication

A fixed-level collapse would place unary S(n)-evaluation much lower than full PSPACE; unbounded necessity would clarify the alternation/PSPACE boundary for this sparse language.

## finding_unverified

 is there any reason to think SORT-BOUND-U would be in some fixed level of PH?

Alternatively, looking up the structure again. The game is essentially a "game tree" where players alternate - it's similar to an "AND-OR tree". The "value" is determined by minimax. For general AND-OR trees of polynomial depth, the evaluation is in P. But if the tree is given implicitly and we need to see if there's a winning strategy of depth k...

Another way: this is exactly like the "strategy problem" in a game. For a game of bounded length with alternating moves, the set of winning positions is computable by alternating quantification. But can we "buy down" alternations by noting the structure?

Or think of it as a kind of "path constraint" satisfaction. Alternatively, notice that sorting is a very symmetric structure. Also the "comparison matrix" gives a total order iff it's a transitive tournament.

Alternatively, is there a known result that the "minimum comparison sorting" decision problem is in Σ_2^P or some fixed level? Or is it PSPACE-complete?

Another common result is that the "graph bandwidth problem" is NP-complete, "optimal linear arrangement" is NP-complete. Also "minimum feedback arc set" in tournaments is NP-hard. But those are different problems. Or perhaps the "matrix bandwidth"? Not obviously the same as sorting number S(n).

Or another possibility - the "coin weighing problem" or "identification via membership queries" - some of these are in PSPACE. But I need to recall or derive.

Alternatively, consider that to guarantee sorting within k comparisons starting from empty order (antichain), the sorter needs a strategy. The adversary is adaptive. This is similar to the "Ulam's game with comparison queries"? Or more directly it's equivalent to a "coin identification" or to the concept of a "coin weighing strategy" with a spring scale? No. Or it's exactly a comparison search (identification) problem - finding which permutation by pairwise comparisons, adversarial answers. The minimum worst-case number of comparisons is S(n). The decision problem is whether identification is possible within k queries.

Also in terms of combinatorial group testing / coin identification, these are often in NP for some models, but with adaptive queries and adversarial answers... Or perhaps related to "graph property testing"? Unclear. But Hyafil-Rivest showed that for arbitrary tests (not necessarily pairwise), the minimum height decision tree is NP-complete. Here the tests ARE pairwise comparisons (a very restricted set). So restriction makes it easier in some cases? Or same complexity? But the docs say Hyafil-Rivest doesn't transfer. And with sparsity barriers making NP-hardness unlikely for unary case, maybe it's lower in the hierarchy than general case.
Let us look up more about the game and alternation structure.

Let us start by exploring the game structure more deeply and looking for known results.

Let us start by analyzing the alternation structure carefully.

Let us think more systematically and also look up the actual ATM behavior.

Let us prepare a report to post to the board.

Reported alternation/strategy-size argument for unbounded alternation depth of the antichain-root game (adaptive dependencies + exponential strategy witnesses preclude fixed-level Σ_d^P with poly verification); distinguished general-poset results from certificate soundness/completeness. No repo changes made; noted limits (not a PH lower bound or PSPACE-completeness proof).

## Other metadata

```json
{
  "finished_at": 1793399745.2945032,
  "started_at": 1793394616.1432967
}
```
