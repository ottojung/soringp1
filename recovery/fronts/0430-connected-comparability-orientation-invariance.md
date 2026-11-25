# connected-comparability-orientation-invariance

## status

investigated

## origin

ai_proposal_unverified

## agent_id

QXNz587yZ3lWsLw4WuaROO-game

## exit_state

clearexit

## question

For all n and all connected finite posets P and Q on n labelled elements with the same comparability graph, is the exact minimax comparison number F(P) equal to F(Q), or does there exist a connected poset pair with identical comparability graphs but different exact minimax values?

## basis

Board #301 parallel-reversal-symmetry gives P=A disjoint-union B and Q=A^op disjoint-union B with F(P)=12, F(Q)=11 and e(P)=e(Q)=1512; A and A^op share the comparability graph P3, so the known failure is disconnected. A curator-side exhaustive n<=5 and random n=6 search found no connected counterexample.

## falsifier

Exhibit a connected poset pair P,Q with the same comparability graph and rigorously verified F(P) != F(Q), or prove that every connected such pair has equal F.

## implication

If orientation invariance holds on connected posets but fails at the board's 9-element disjoint union, then orientation dependence is created by the disjoint-union/merge operation, so exact S(n) is the extreme merge case and componentwise comparability-graph quotients cannot be complete for it.

## finding_unverified

gives `F(A) ≥ 6`.

### All-`n` family and minimality

For every `m ≥ 0`, take the ordinal sums `A ⊕ C_m` and `Q ⊕ C_m`. These have the same connected comparability graph, and ordinal-sum additivity gives

```
F(A ⊕ C_m) = 6 + m,   F(Q ⊕ C_m) = 7 + m,   e = 60.
```

So counterexamples exist for every `n ≥ 7`, not just at a isolated small size. Exhaustive isomorphism-class checks for all `n ≤ 6` found no comparability-graph bucket with two different `F` values, so `n=7` is minimal.

### Positive boundary

Gallai’s theorem says a **prime** graph has at most two transitive orientations, mutually dual. Since `F(P^op) = F(P)`, orientation invariance holds on connected posets whose comparability graph is prime. Any counterexample must therefore have a nontrivial homogeneous set; the witness above has the module `S={2,4,5,6}`.

## Complexity interpretation

The front’s conditional implication is vacuous: orientation dependence is **not created by disjoint union/merge**, because it already occurs in a connected `7`-element poset. The negative quotient conclusion is strengthened: an exact DP quotienting reachable states by comparability graph is unsound even on connected states. This is a state-compression obstruction, not a lower or upper bound on the uniform complexity of `S(n)`.

On soundness versus completeness: the one-ply extension-count test is a sound non-sortability certificate for `Q` at budget `6`, but it does not lift to a graph-level certificate. `A` and `Q` share the graph and `e=60`, yet `A` is sortable in `6` and `Q` is not.

## Honest limits

- `F(A)=6`, `F(Q)=7` are exact finite computations, not kernel-checked proofs.
- The `Q ≥ 7` certificate is paper-checkable modulo the stated extension counts.
- The all-`n` family uses the established ordinal-sum additivity theorem, not a new formalization.
- Minimality `n ≤ 6` is exhaustive computation, not an all-`n` proof.
- No Lean or repository changes were made.

## External effects

Exactly one board #301 post was created at `2026-11-09T10:44:02Z` under `SoringP1 frontier: connected-comparability-orientation-invariance`, verified landed. No duplicate post, commit, or repository change.
Recovery inspection complete. No external action was repeated.

## State verified

- **Git:** clean worktree at `6a96398`; no new commits, branches, or files.
- **Board #301:** exactly one post from this front exists, at `2026-11-09T10:44:02.761Z`, author `SoringP1 frontier: connected-comparability-orientation-invariance`. No duplicate post was made.
- **Durable ledger:** the entry `connected-comparability-orientation-invariance` is still marked `running` with `finding_unverified: null`. That is the pre-exit state; the keeper records the finding when this session terminates. I did not modify the ledger.

## Status of the work

The previous turn completed the research task and posted the result:

- The all-`n` connected-comparability orientation-invariance claim is **false at `n=7`**.
- Explicit connected same-graph pair: `A=(0,0,1,3,5,5,37)` with `F(A)=6`, and `Q=(0,0,113,3,1,65,1)` with `F(Q)=7`; both have `e=60` and the same labelled comparability graph.
- Infinite family for every `n≥7` via ordinal sums with a chain.
- Exhaustive `n≤6` check finds no counterexample.
- Positive boundary: prime comparability graphs are invariant by Gallai’s two-orientation theorem plus `F(P^op)=F(P)`.

No unfinished external work remains. I am not repeating the board post, commit, or any computation with side effects.

## Other metadata

```json
{
  "finished_at": 1794221140.58332,
  "started_at": 1794220124.5801642
}
```
