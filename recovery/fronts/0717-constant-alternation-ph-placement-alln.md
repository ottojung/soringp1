# constant-alternation-ph-placement-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

49LbKREpjKqFGTD8U5Z8sv-learning

## exit_state

clearexit

## question

SORT-BOUND-U is decided by the sorter-versus-adversary game G(n,k) using k=Theta(N) alternating rounds, which yields PSPACE via APTIME=PSPACE. Does SORT-BOUND-U belong to a fixed level of the polynomial hierarchy, i.e. can G(n,k) be replaced for all n by an equivalent decision procedure using only O(1) alternations, giving a Sigma_i^p or Pi_i^p characterization for some constant i?

## basis

research-certificates-barriers Claim A (APTIME=PSPACE via Theta(k) alternations) and docs/problem.md established unary PSPACE membership; the repository contains no PH placement analysis. The tally/sparse structure (Mahaney, Ogiwara-Watanabe) constrains hardness but does not settle constant-alternation membership, so this is an open complexity question about the exact language of S(n).

## falsifier

Show that for every constant i there are unary inputs forcing more than i alternations in any correct game-style decision procedure, for instance via a PH-collapse consequence such as SORT-BOUND-U not in PH unless PH collapses; or exhibit an O(1)-alternation formulation that refutes the apparent need for Theta(N) alternations.

## implication

A constant-alternation characterization would be a genuine new upper bound strictly below PSPACE, a PH placement tightening the game/Alternation characterization of the unary threshold; a collapse-based no-go would be a new barrier theorem about the minimax game and the limits of local alternating certificates for S(n).

## finding_unverified

=12 case (`S(12)=30>29`) refutes the simpler "defect-zero" local certificate family. This is precisely the repo's documented soundness/completeness gap; no completeness theorem exists.

### Why the suggested collapse-based falsifier is not viable `[deduction]`
- Unconditional `SORT-BOUND-U ∉ PH` would imply `PSPACE ≠ PH` (language is in PSPACE by Claim A) — a major open separation; and `PSPACE = PH` itself collapses PH to a finite level (a PSPACE-complete set would lie in some Σᵢ, closed under many-one reductions).
- A conditional "∈ PH ⇒ collapse" needs PH-level hardness; sparsity blocks NP-hardness (Berman/Mahaney ⇒ P=NP) and higher sparse completeness already yields collapses (Ogiwara–Watanabe). No such hardness is established.
- General-poset hardness (Hyafil–Rivest, Laber–Nogueira) and network verification (Parberry) do not transfer to the fixed antichain-root adaptive game.

**Honest limits:** PH-U stands open. The proof covers only explicitly represented local strategies; a succinct circuit strategy escapes the Θ(N/log N) bound, and ruling that out is PH-separation territory. Process here produced one checkable theorem about the *game formulation* and a precise map of the obstruction — not a theorem about the language's PH membership.
I'll audit the actual persisted state before doing anything else. No new posts, commits, or writes during this check.
## Recovery audit — no new external actions taken

I inspected state only; I did **not** post, commit, push, or modify any record.

**What actually persisted from the previous turn:**

| Effect | Status | Evidence |
|---|---|---|
| Board #301 post | **Happened exactly once**, full body intact | Digest shows 1 match, author `SoringP1 frontier: constant-alternation-ph-placement-alln`, timestamp `2026-11-23T13:26:01.342Z`; the closing phrase of the intended body is present; pages 1–3 contain no second copy |
| Git / commits / branches | **No change** | `git status` clean, HEAD still `6a96398`, reflog shows only the original clone, only `billy-dev` |
| Repo / Lean / tests / CI | **No change** | No files written outside `/tmp/opencode` (`ph_placement_report.txt`, post result/err logs) |
| Ledger | **Unchanged** | Entry `constant-alternation-ph-placement-alln` still `status: running`, `result: null`, `finished_at: null` |

**Backend failure impact:** none observable. The single post persisted in full and the board is currently readable. No duplication risk remains — I will not re-post.

**Unfinished work:** none on my side. The mathematical report was delivered and the sole intended side effect (one #301 post) is confirmed. The "no repository/Lean/test/CI/ledger change" claim in that post is accurate.

**Flagged for review, not guessed at:** the ledger entry for this front is still `running` even though the research turn completed. I left it alone deliberately: (a) my earlier report explicitly declared no ledger change, (b) the keeper owns `running → investigated/blocked` transitions on process exit, and (c) across all 717 ledger entries **none** has a populated `result` field, while 680 are `investigated` and 3 other fronts from the same batch (started within ~2 s of ours) are also still `running`. So `running` with null result is consistent with current convention, not evidence of a lost effect. If the operator expects an explicit `investigated` transition for this front, that is a judgment call for the keeper/operator rather than something I should write into the ledger during recovery.

## Other metadata

```json
{
  "finished_at": 1795440479.9293957,
  "started_at": 1795440049.31795
}
```
