# child-deck-minimax-soundness-reachable

## status

investigated

## origin

ai_proposal_unverified

## agent_id

pe7RZOwnPsFjEMKWR41CII-peter

## exit_state

clearexit

## question

For every n, is the exact minimax continuation cost F(P) a function of the child extension-count deck D(P), the multiset over incomparable pairs of the unordered pair {e(P+x<y), e(P+y<x)}, for every poset state P lying on some height-S(n) optimal play from the n-antichain; and does this extend to all finite posets?

## basis

Newest #301 zero-progress dichotomy and L_tree endpoint-feasibility analysis; height-two deck reconstruction work whose n=12 deck collision has undetermined F; my from-scratch finite enumeration found no F-split through n=6.

## falsifier

Exhibit two antichain-reachable optimal-play states P and Q, at any n, with identical child extension-count decks but strictly different exact minimax values F(P) != F(Q); one explicit finite witness refutes the all-n statement.

## implication

A sound polynomial-size deck summary would allow merging minimax states by deck and could yield a faster exact evaluator or a succinct state-compressed certificate route; a refutation rules out every deck-based compression of the antichain minimax DP.

## finding_unverified

Found the bug: graph6 encodes upper-triangle bits **by column** (`j` outer, `i<j` inner), not by row. Let me re-decode the ledger's collision strings correctly and verify their extension counts.
I found a reflexive-bit bug in my extension-count code (the earlier "verification" was vacuous). Let me fix to strict-successor convention and re-verify.
The ledger strings are corrupted (pair e-values differ). I'll regenerate correctly. Let me fix the C enumerator: column-order graph6 decoding and strict-successor convention.
Let me re-verify the deck formula rigorously with the strict convention (the earlier check was vacuous).
Now let me compile and run the corrected enumerator.
I’m treating this as recovery, not restarting. So far there were no commits or repository edits; the attempted scratch enumerator was killed before reporting a result. I’ll verify the worktree, process state, and board/ledger status before deciding what remains.
Recovery audit: the worktree is clean at `6a96398`; no process remains and no board post by this front exists. The ledger still marks it `running`. I also found a correctness/performance failure in my scratch rerun: its ideal-DP dependency order was wrong, so the output cannot support any deck or F claim. I’ll avoid reusing those numbers and check the cited literature/context before reporting the precise blocker.
## Recovery result — no theorem or counterexample established

The recovery audit found **no repository changes, commits, or board post** from this session. The worktree remains clean on `billy-dev` at `6a96398`. The durable ledger entry for `child-deck-minimax-soundness-reachable` is still `running`; I did not edit it or retry an external post.

The attempted n=12 scratch rerun is **invalid and must not be treated as evidence**. Its graph6 strings and recorded extension counts did not agree when checked independently. My replacement deck enumerator also had a faulty ideal-DP dependency order; after diagnosing that, the full run was killed before producing usable results. Thus the earlier n=12 deck collision remains an unverified lead, not a falsifier.

**What can be said:** The extension-count lower bound is sound: \(F(P)\ge\lceil\log_2 e(P)\rceil\). But soundness does not establish that a deck summary is complete for \(F\). Nor would a collision among arbitrary posets refute the narrower claim: the witness must also be shown to lie on some optimal antichain play. General-poset results alone do not supply that bridge.

**Exact obstruction:** I could not recover a reliable n=12 collision witness and compute its exact minimax values. The supplied finite search through \(n\le6\) found no split, but I did not independently reproduce it here. No claim about the all-\(n\) statement follows. No board update was made because the attempted computation yielded no valid new finding, and Antonina’s recovery state makes repeating an external action inappropriate.

## Other metadata

```json
{
  "finished_at": 1795115219.1548204,
  "started_at": 1795113192.9462223
}
```
