# upper-inequality-height-two-restriction

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Lx5jEz67574FH2on9GFA3G-penalties

## exit_state

clearexit

## question

Does the (U) inequality alpha(P) <= C(covers(P)+psi(m_P,M_P)) with C=(5-log2 15)/8 hold for every finite poset of height at most two, including the one-comparison state Q_n = C_2 disjoint-union A_{n-2} whose exact value is S(n)-1?

## basis

Newest board #301 02:20Z upper-inequality-structural verifies (U) only for matchings plus isolates and two-chain merges; independent exhaustive checks here over all unlabeled posets at n=7,8 find no counterexample.

## falsifier

Exhibit a height-two poset P with exact alpha(P) > C(covers(P)+psi(m_P,M_P)), computed by exact minimax and exact extension counting.

## implication

A height-two proof would be a tractable first case of (U) and a potential pruning bound on the first-comparison state Q_n; a counterexample would show (U) fails already on height two, with no direct S(n) bound change either way.

## finding_unverified

 is not bounded tightly enough in terms of `E` and `e` to close `(U)`.
- `n=11` is not exhaustive; the dense subset and the top crude candidates are safe.
- This is a structural minimax statement about height-two posets. It is **not** a certificate result: the information bound is sound but not complete, and general-poset results (Fredman, Kahn–Saks) do not transfer.
- No `S(n)`, `SORT-BOUND-U`, P/NP/PSPACE, or certificate-completeness consequence is claimed.

**Board post:** Antonina issue #301, 2026-11-10 08:34Z, author `SoringP1 frontier: upper-inequality-height-two-restriction`. Worktree clean at `6a96398`; no repository or Lean changes. Scratch: `/tmp/opencode` (`filter_h2.cpp`, `h2_roots_*.txt`, `h2_meta_*.txt`, `h2_F_*.txt`, `comps11_*`, merge DP).
**Recovery inspection (no actions taken that duplicate side effects)**

- **Host / repo:** `billy-dev`, `/home/lubko/soring-fronts/upper-inequality-height-two-restriction` on `billy-dev...origin/billy-dev`, worktree clean, HEAD `6a96398` (“Merge commit '6859bc2' into research/exact-reset-tree-realizability-20261027”). No uncommitted changes and no new commits beyond that state.
- **Durable artifacts present (scratch):** `/tmp/opencode/fonly{,.cpp}`, `/tmp/opencode/filter_h2{,.cpp}`, height-two data `h2_roots_{7..11}.txt` (165/558/2224/10767/64957 lines), `h2_meta_{7..11}.txt` (164/557/2223/10766/64956), exact results `h2_F_{7..10}.txt` (164/557/2223/10766), plus `board_post_upper_h2.md` and `board_post_result.json` (all consistent with the prior run).
- **External side effect (board #301) — already performed, not repeated:** `/tmp/opencode/board_post_result.json` records the posted finding for front `upper-inequality-height-two-restriction` with `"state":"open"`, `"updatedAt":"2026-11-10T08:34:52.247Z"` (recordedAt `2026-10-19T03:34:52.169Z` in payload; verdict/record fields present as stored). The stored body matches `board_post_upper_h2.md` (exhaustive height-two `n<=10`: no `(U)` violation, max `alpha/D` 0.098904/0.092353/0.091924/0.087306; `n=11` partial 64,956 classes with top crude candidate shown safe; D-induction/balanced-split obstruction on height two; `(U)` not closed under disjoint union; `a=2` subclass observation; honest limits). **I did not repost.**

**Determination**
- **Completed effects:** computation/enumeration artifacts in `/tmp/opencode` and the Antonina board #301 findings post above. No repository or Lean changes were made (and none are present).
- **Unfinished (research-blocked, not a failed side effect):** no all-`n` proof or counterexample for `(U)`; merge-cost gap in `F <= S(a)+S(b)+M(G)` not tight enough to close it; `n=11` not fully exhaustive (exact minimax on remaining dense/candidate subsets expensive). `a=2` subclass remains a finite observation only.
- **No actions taken now:** nothing safe/necessary to resume without risking duplicate external effects or speculative work; the prior report stated “next move: none required” for that request. Per contract, no Lean/repo changes without a substantive, independently checkable new theorem or counterexample.

**Uncertainties for review (not guessed):** I could not independently re-query Antonina board #301 from this environment beyond the local `board_post_result.json` record; the record indicates the post/update occurred, but if authoritative confirmation is needed it should be verified against the live board before any further posting. No commits, PRs, or other external actions were detected or performed.

## Other metadata

```json
{
  "finished_at": 1794300259.5716252,
  "started_at": 1794294255.049185
}
```
