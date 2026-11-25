# framed-optimal-height-polysize-existence

## status

investigated

## origin

ai_proposal_unverified

## agent_id

EatO8buxC7479kniyKXkRj-atoms

## exit_state

clearexit

## question

For every integer n>=1, does some sound permutation-framed DAG of node count polynomial in n achieve longest path exactly S(n) for the n-key antichain, beyond known merge-sort and Ford-Johnson surpluses?

## basis

research-framed-certificate-frontier.md reports sound polynomial merge/FJ constructions with known surpluses and states optimal-height completeness is open for all n.

## falsifier

Find an infinite family of n where every sound permutation-framed DAG with polynomially many nodes in n has longest path >= S(n)+1, proved by an invariant or explicit witness argument.

## implication

A uniform affirmative would imply SORT-BOUND-U in NP via checkable framed certificates; a uniform negative would block framed-DAG completeness at exact height and refocus certificate work.

## finding_unverified

 checker's per-node relation can have minimax value exceeding the remaining budget — i.e., whether any local F-value invariant is even necessary.
Let me inspect the certificate's edge structure to document exactly why counting invariants fail, then verify the model-fidelity point about merges.
This reveals the key mechanism: 10 of 18 nodes send both outcomes to the same child — outcomes are encoded in edge permutations, not graph branches. Let me find how to post to board #301.
I have a clear picture now. Let me re-verify the worktree is clean, then write and post the #301 report.
The post succeeded. Let me verify it landed on the board and confirm the worktree is still clean.
## Report: `framed-optimal-height-polysize-existence`

Worked on `billy-dev` (clean worktree at `6a96398`, no repo/Lean/test/ledger changes). One #301 post landed at `02:17Z`.

**Result: the FALSIFIER was NOT established; the FRONT remains open.** I attacked the claim and report a concrete failed approach plus the exact obstruction, not a proof.

**Concrete failed falsifier attempt (level-counting invariant).** I tried to prove that a node on "level S(n)−1" serves at most two longest paths, forcing ≥ (n! − 2^{⌊log₂ n!⌋})/2 ≈ 2^{Ω(n)} nodes — which would disprove the FRONT. This invariant is false. I verified the checker-ACCEPT 19-node, depth-13 certificate for n=7 by simulating all 5040 inputs:

- 5040 distinct root-to-leaf paths funnel into **one** leaf, reached at path positions **10–13**;
- internal node 17 is reached at positions 10, 11, 12 and serves 2688 inputs;
- 10 of 18 comparison nodes route **both** outcomes to the same child;
- 5040 paths are realized by 19 nodes.

So nodes have no unique depth, per-node path multiplicity is unbounded, and leaves/paths are heavily shared — every per-level or path-count invariant collapses.

**Where the information actually lives.** Each input corresponds to a distinct composed permutation frame σ with σ(π)=sorted. With V nodes there are ≤2V edge permutations whose products along paths number up to (2V)^{S(n)} ≫ n!, so there is no counting/group obstruction to encoding all n! inputs in poly size. This is the compression mechanism that defeats the counting approach.

**Soundness ≠ completeness (model fidelity).** The checker never evaluates minimax F at internal nodes; it checks only acyclicity, leaf totality, and max path ≤ budget. Soundness concerns the union of real inputs reaching a node, not LE(R_v). Hence the "lossless merge needs F(P∩Q)=F(P)=F(Q)" condition and its known n=5 non-transitivity constrain only fixed-tree meet-compression — they do **not** lower-bound sound framed DAGs. Likewise 2n!−1 reachable labelled posets (decision trees) and the winning-frontier state count are structural/general-poset results, not framed-DAG bounds.

**Exact obstruction.** A disproof requires showing no poly-size choice of comparisons + edge permutations realizes all n! sorting frames within height S(n) — a succinct-optimal-sorter representation lower bound. All available techniques fail for the reasons above, and such fixed-polynomial lower bounds are unprecedented here. Small-n data (9 nodes at n=4, 19 at n=7, both checker-ACCEPT at exact S(n)) also rule out starting the disproof by small counting. Crucially, even a full disproof would only block this grammar; it would not place SORT-BOUND-U outside NP.

No mathematical theorem or counterexample was produced — the FRONT stays open, consistent with the project's stated barrier.

## Other metadata

```json
{
  "finished_at": 1795054701.5979233,
  "started_at": 1795054149.3212008
}
```
