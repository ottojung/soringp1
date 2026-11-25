# insertion-number-uniform-complexity-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

XKF2qtBNo5QSzbuXbzHjaK-secretary

## exit_state

clearexit

## question

Is the exact chain-host insertion number I(a,b) = F(C_b disjoint-union A_a) - the minimax comparisons to place a free keys into a known sorted b-chain, which the 2026-11-21T10:20Z board result identifies as the extremal disjoint-union defect envelope max_B delta(A_a,B) - computable by a uniform algorithm in time polynomial in a+b for every a,b >= 1?

## basis

Board #301 10:20Z chain-extremality result: max defect = F(C_b discrete-union A_a)-S(a) <= sum ceil(log2(b+i)), with an explicit limit that no closed form is known; distinct from ledger front two-chain-merge-exact-complexity (two chains) and split-completion-coupling-penalty-alln (a defect bound).

## falsifier

Exhibit an infinite family (a_i,b_i) with a proved superpolynomial or #P-hard lower bound for computing the exact value of F(C_{b_i} disjoint-union A_{a_i}), or a state-space lower bound exceeding (a+b)^{O(1)} for every uniform evaluator.

## implication

A polynomial-time evaluator for I(a,b) would make the insertion upper bound S(n) <= S(b) + I(n-b,b) uniformly computable without minimax search, sharpening the active upper-bound frontier for exact unary S(n); a hardness result would isolate a concrete barrier.

## finding_unverified

ured family without an encoding-preserving reduction, which sparsity obstructs. Turing-hardness remains open.
- **State-space lower bound for "every evaluator":** at `b=1` the natural DP family has `2^{Θ(a log²a)}` states (prior front), but upgrading that to all evaluators is exactly the open `S ∈ FP` question.
- **Soundness vs completeness:** the merge-insertion bound `I ≤ S(a)+Σ⌈log₂(b+i)⌉` and the information bound are sound certificates (a strategy / a leaf count), not proofs that `F` equals them; exact `F` needs minimax.
- **Positive slice (not new):** for fixed `a`, `I(a,b)` is computable in `b^{O(a)}` time — a state is a poset `Q` on the `a` free keys plus each key's chain prefix/suffix (`≤ 2^{a²}(b+2)^{2a}` states) — matching known Hwang-style configuration DPs. It does not extend to growing `a`.

## Bottom line
I neither refuted nor proved the claim: disproving it needs `P≠PSPACE` at `b=1`, proving it resolves `S_unary ∈ FP`. The genuine remaining question is `b≥2` with both coordinates growing; even at `b=2`, `S(a+2)−1 ≤ I(a,2) ≤ S(a+2)`, so a poly evaluator there is essentially an `S`-evaluator. No new bound for `S(n)`, no class membership for `SORT-BOUND-U`; no repository, Lean, test or ledger changes.
I'll follow the recovery protocol: inspect state first, determine what actually happened, and only continue genuinely unfinished work — without duplicating any external action.
Git state is clean (`billy-dev`, `6a96398`) and scratch artifacts from the prior turn are intact. Now let me verify the board post landed exactly once and check for any post-turn activity (e.g., a referee disposition) and the ledger state.
Confirmed: exactly one post from my front (10:40:26Z), no duplicate, no referee disposition pending, ledger still keeper-managed (`running`), worktree clean. Let me verify the full post body was written intact (not truncated) before concluding there is no unfinished work.
## Recovery check complete — no unfinished work, no repeated actions

I inspected the conversation, working directory, Git state, durable ledger, and board #301 before taking any action. The prior turn's effects are all confirmed and complete:

| Item | Verified state |
|---|---|
| Branch / worktree | `billy-dev`, clean at `6a96398` — no commits, no file changes |
| Board #301 post | **Exactly one** comment under `SoringP1 researcher: insertion-number-uniform-complexity-alln`, at `2026-11-21T10:40:26.610Z`, full 3,993-char body intact (ends with the complete honest-limits conclusion) — no duplicate |
| Ledger | Front `insertion-number-uniform-complexity-alln` remains `running` (keeper-managed; I did not alter it) |
| Scratch | `/tmp/opencode/insertion_front/` (evaluator, post draft, response) — scratch only, as declared |
| New activity | No referee disposition after my post; nothing awaiting a response |

**Effects that actually happened in the previous turn:** one independent minimax computation in scratch and one complete board report. Nothing else.

**Conclusion:** the investigation was already delivered — the decisive finding (that `I(a,1)=S(a+1)` collapses the front to the flagship `S_unary ∈ FP` problem, so both falsifier horns require `P≠PSPACE`/a Mahaney-type collapse) was posted with full soundness/completeness caveats and honest limits. There is no unfinished work to continue. I have deliberately **not** re-posted, re-committed, or modified the ledger, in accordance with the recovery instruction. Nothing is uncertain and in need of review.

## Other metadata

```json
{
  "finished_at": 1795257720.82004,
  "started_at": 1795256851.8378074
}
```
