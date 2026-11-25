# pp-hardness-transfer-antichain

## status

investigated

## origin

ai_proposal_unverified

## agent_id

90VdYaKaKhKAjWxfAIgXyP-pushed

## exit_state

clearexit

## question

Does the PP-hardness of the general-poset Fibonacci extension-threshold predicate transfer to the antichain language SORT-BOUND-U under polynomial-time reductions, or is there a provable non-transfer barrier?

## basis

Board #301 fibonacci-threshold PP-hardness post (Las Vegas reduction, L_fib in PP), docs/problem.md sparsity, and ledger entry gen-sort-pspace-reduction-antichain; no PP or counting-hierarchy front for SORT-BOUND-U exists.

## falsifier

Construct an encoding-preserving polynomial-time reduction from the PP-hard predicate e(P)<=T(b) to SORT-BOUND-U, or prove that no such reduction can exist without collapsing PP or the polynomial hierarchy.

## implication

A transfer would make SORT-BOUND-U PP-hard, a new hardness result below PSPACE that bypasses the sparse many-one NP barrier; a non-transfer theorem would isolate general-poset hardness as irrelevant to exact S(n) evaluation.

## finding_unverified

by non-completeness.
4. **Reachable-state transfer.** Fails by the \(\exists\)-state versus root-minimax quantifier mismatch.
5. **Compute \(e(P)\) directly.** This is the only obvious correct reduction, but counting linear extensions is #P-complete (Brightwell–Winkler), so it is not polynomial-time.

## Honest limits

- The non-transfer result is **conditional on PH non-collapse**; it is not an unconditional separation.
- It relies on the board’s Las Vegas PP-hardness of \(L_{\mathrm{fib}}\), which in turn relies on the effective Kravitz–Sah construction (paper deduction, currently unaudited). If that is weakened, the barrier still applies to any PP-hard predicate, but the specific \(L_{\mathrm{fib}}\) transfer is moot.
- Deterministic PP-hardness of \(L_{\mathrm{fib}}\) is open; it would strengthen the collapse to \(\Sigma_2\).
- The binary threshold language is not covered by the sparsity argument; per `AGENTS.md`, it remains outside the active unary workstream.
- No new exact value of \(S(n)\), no Lean theorem, and no repository change. The finding is a complexity barrier and a structural obstruction, not a proof of \(P\neq NP\) or of any unconditional separation.

The board post was recorded at #301 (`2026-11-08T06:54:20Z`, author `SoringP1 frontier: pp-hardness-transfer-antichain`) and verified as the latest message.
## Recovery audit

I inspected the existing conversation, working tree, Git state, board, and durable ledger before doing anything.

**Effects that actually happened**
- **Board #301:** exactly **one** comment by `SoringP1 frontier: pp-hardness-transfer-antichain`, at `2026-11-08T06:54:20.112Z`, `sha256:hyVdNUCHBwPBipYSBfwUuN8G8hboaMmkkzXvHugnWuU`. Page 1 contains one message from this author and one body matching the front title. **No duplicate.**
- **Git:** branch `billy-dev`, HEAD `6a96398`, clean worktree. No commits, edits, or repository files were created.
- **Local artifacts:** only `/tmp/opencode/post.md` and `/tmp/opencode/post_result.json`, outside the repository.
- **No new external action was taken on this recovery turn.** I did not repost, commit, or modify the ledger.

**Durable task record**
The ledger still shows the front as:
- `status: running`
- `finished_at: null`
- `exit_state: null`
- `finding_unverified: null`

So the mathematical investigation and board report are complete, but the **operational ledger status is stale**. Recording the exit/finding is the keeper’s bookkeeping step; I did not edit the ledger manually.

## Mathematical status

The finding is unchanged from the prior completed report: the Fibonacci predicate’s PP-hardness does **not** transfer to `SORT-BOUND-U` under uniform polynomial-time reductions unless the polynomial hierarchy collapses. The target is sparse and in `P/log`, so PP-hardness would put PP in `P/poly` (deterministic case, `PH=Σ₂`) or `coNP/poly` (Las Vegas case, `PH=Σ₃`). This is a conditional non-transfer barrier, not an unconditional separation.

The previously reported concrete separation is also still valid: at `n=4`, two posets with `S(P)=3` have `e(P)=6` and `e(P)=8`; with `T(3)=7`, the Fibonacci predicate differs even though `S(P)` does not. That observation was in the final report but not in the board comment; I did not add it separately to avoid an unnecessary second post.

**Conclusion:** no unfinished mathematical work and no repeated side effects. The only review item is the stale ledger entry, which the keeper should mark `investigated` on agent exit.

## Other metadata

```json
{
  "finished_at": 1794121090.717247,
  "started_at": 1794120029.3466408
}
```
