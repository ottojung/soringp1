# antichain-reachable-power2-halving-obstruction

## status

investigated

## origin

ai_proposal_unverified

## agent_id

EhH2eegHH4igoJnQyuzkjs-construct

## exit_state

clearexit

## question

For all n, can a poset with e(P) a power of two and no exact-halving continuation occur as a state on some height-S(n) optimal play from the n-element antichain, or does the reachability restriction imposed by the window covers(P) <= d <= S(n) - max(F(P), pi(P)) always exclude such states? Does the answer depend on whether S(n) equals the information bound?

## basis

The documented e=8 obstruction is not reachable at n=5 because its cover count exceeds the window depth S(5)-F=3, so reachability is the decisive filter. The one-bit-slack recurrence on height-C trees and the corrected realizability-window note supply the necessary tests; the specific power-of-two halving obstruction under that filter is not a ledger front.

## falsifier

Exhibit a genuinely reachable state inside a height-S(n) game from the antichain with e(P)=2^r and exact minimax continuation above r, including the required joint-child sibling budget, or show that the window and one-bit-slack restrictions forbid every such state for all n.

## implication

A positive exclusion result would license a sound tight-subproblem pruning rule in exact unary S(n) evaluators and sharpen the structural theory of optimal play; a counterexample would place the obstruction inside the root game itself. This concerns exact evaluation of S(n), not P, NP or PSPACE membership, and a general-poset obstruction does not transfer without reachability.

## finding_unverified

chability front flagged by the two recent general-poset posts. Let me check the board posting interface.
I have a decisive finding. Let me write the board report and post it to #301.
The post succeeded (visible at 18:47:57Z). Let me confirm the worktree remains clean, as required.
Worktree clean on `billy-dev` at `6a96398`; the only external side effect is one board post to #301 (18:47:57Z). All computation was scratch in `/tmp/opencode/p2halving`.

## Mathematical finding

**The front's "always exclude" hypothesis is false.** A poset with `e(P)` a power of two, no exact-halving continuation, and `F(P) > log2 e(P)` **does** occur on a height-`S(n)` optimal play from the antichain — already at `n = 6`, which is information-tight (`S(6)=C(6)=10`). The reachability window is decisive at `n=5` but is **not** a universal filter.

### Fully verified witness `W6` (n=6)
Successor masks `(0,17,1,19,0,5)`; relations `{(1,0),(1,4),(2,0),(3,0),(3,1),(3,4),(5,0),(5,2)}`.
- `e = 16 = 2^4` (brute force over all 720 permutations), `b=4`.
- `F = 5` (independent memoized minimax with a separate Warshall closure), so `eps = 1 > 0`.
- The 7 incomparable pairs split `e` as `(6,10),(10,6),(4,12),(2,14),(12,4),(9,7),(1,15)` — **no (8,8) split**, hence no exact-halving continuation. (This is exactly the primitive obstruction of the 18:45Z general-poset post, now shown reachable.)
- `covers=5`, `pi=1`.

### Genuine reachability with the joint-child sibling budget
Explicit path from `A_6`: `(0,1) j<i`, `(2,5) j<i`, `(0,2) j<i`, `(1,3) j<i`, `(1,4) i<j`. At depths `0–4` both children fit the remaining budget (`(9,9),(8,8),(7,7),(7,7),(5,5)` vs budgets `9,8,7,7,5`). At depth `5` the state is `W6` with remaining budget `5 = F(W6)`, so the minimax subtree below it is a height-5 strategy.

### Window test
`covers=5 ≤ d=5 ≤ S(6)−max(F,pi)=10−5=5` — the interval is the singleton `{5}` and is satisfied with equality. So the window is necessary but does **not** exclude the obstruction; the positive exclusion route is refuted.

### Mechanism and dependence
The ceiling-loss profile is `pi=1,1,1,1,2` (`b: 10→9→8→7→6→4`); the last step drops `b` by 2 (`e 36→16`), a negative signed-loss subsidy. With `D(6)=0`, `eps(W6)=0−(−1)=1`. So local non-tightness arises at an information-tight root via one steep step — the signed-ceiling-loss phenomenon. **The answer does not depend on `S(n)=C(n)`**: `n=6` is tight and admits the witness. At `n=5` (also tight) the analogous `e=8` obstruction has `covers=5 > S(5)−F=3`, so it is excluded — the filter is size-dependent, not universal.

## Honest limits
- Finite counterexample only (`n=6` fully verified; a second `n=7` witness `Q=(0,1,3,3,7,15,31)` — `e=8, F=4, no halving, covers=8, pi=2` — had its properties independently re-verified, but its reachability path is cited from prior independent work, not re-run here). No all-`n` reachability family is proved (an ordinal-sum embedding `P6 ⊕ C_t` is plausible but needs a separate sibling-budget induction, not attempted).
- This closes the proposed power-of-two tight-subproblem pruning rule and places the obstruction inside the root game. It yields **no** new value of `S(n)`, no speed-up for exact evaluation, and no P/NP/PSPACE consequence (per `docs/problem.md`). The 18:43Z/18:45Z results are general-poset results and do not transfer to `S(n)` without exactly this reachability argument.

I did not create any Lean, note, test, or repository changes — a clean worktree is the correct outcome here.

## Other metadata

```json
{
  "finished_at": 1795200520.7280877,
  "started_at": 1795199573.0349956
}
```
