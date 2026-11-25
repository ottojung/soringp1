# antonina-QXNz587yZ3lWsLw4WuaROO-game

Session: ses_e402592aeffeQd8UAreLeQuJtp
Workspace: /home/lubko/soring-fronts/connected-comparability-orientation-invariance
Created: 1794220125816; updated: 1794221125868

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 331 (msg_1bfe898180010DoR7yE6eP1QbV)

## Recovery audit

- Worktree was clean at `6a96398`; no uncommitted files, branches, or commits from the interrupted turn.
- Board search across all 52 pages found no prior post for this front. No external action was duplicated.
- The connectedness of the underlying `n=7` module-reversal witness is already implicit in `docs/research-orientation-modules.md` / `docs/research-compression-next.md` and the PR #12 review, so I did not claim a new poset pair.

## Mathematical finding

The front’s all-`n` claim is **false already at `n=7`**, and it fails for every `n ≥ 7`. There is a connected same-comparability-graph pair with different exact minimax values. A restricted positive theorem survives for prime comparability graphs.

### Explicit counterexample

On labels `0..6`, with successor bitmasks:

```
A = (0, 0,   1, 3, 5,  5, 37)
Q = (0, 0, 113, 3, 1, 65,  1)
```

`S = {2,4,5,6}` is a module of `A`; `Q` is the reversal of the internal order on `S`, keeping all cross relations. Hence `A` and `Q` have the **same comparability graph on the same labels**, and both graphs are connected.

Exact values, reproduced by two independent minimax implementations:

| poset | `e` | `F` |
|---|---:|---:|
| `A` | 60 | **6** |
| `Q` | 60 | **7** |

The lower bound `F(Q) ≥ 7` has a short paper-checkable certificate: every first comparison in `Q` leaves a child with at least `34` extensions (best split `(1,6)` gives `34/26`), while a height-`6` tree has only `2^5 = 32` leaves below a root child. For `A`, `(1,2)` splits `30/30`, and the exact DP verifies a height-`6` policy; the information bound gives `F(A) ≥ 6`.

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

## Output 363 (msg_1bfe958c90017HGVKVA1y4YDlM)

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
