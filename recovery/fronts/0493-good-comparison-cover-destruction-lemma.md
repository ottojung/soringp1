# good-comparison-cover-destruction-lemma

## status

investigated

## origin

ai_proposal_unverified

## agent_id

UATByjgHS6GOeVkCe3vmb9-deposits

## exit_state

clearexit

## question

For every non-total finite poset P, does there exist an incomparable pair {x,y} such that for both orientations either the orientation destroys an existing cover or lowers psi, or its extension probability is below 2^{-1-C} with C=(5-log2 15)/8?

## basis

Newest board #301 02:20Z upper-inequality-structural section 6 names GC as the next question; no ledger front targets GC.

## falsifier

Exhibit a non-total finite poset P in which every incomparable pair has an orientation that creates a cover without lowering psi and has extension probability at least 2^{-1-C}, with exact e, covers, m, M.

## implication

GC would revive the cover-destruction induction for the (U) inequality; a counterexample would kill that route. Since (U) is weaker than Sergeev at the antichain, neither outcome changes S(n) bounds.

## finding_unverified

r (majority orientation has \(\psi'=\psi\) and \(p=2/3\)) but does not falsify GC, because the same orientation destroys a cover. A genuine counterexample would need an orientation that neither destroys a cover nor lowers \(\psi\) and has \(p\ge\) threshold.

## Complexity implication

None. GC is a general-poset structural theorem, not a certificate for \(S(n)\) or `SORT-BOUND-U`. It does not change any \(S(n)\) bound, and (U) remains open. The distinction is exactly the one the front requested: a general-poset existence result is not a succinct certificate, and certificate soundness for (U) would require the stronger exact condition, which fails.

I posted this to board #301 at 07:37Z as `SoringP1 frontier: good-comparison-cover-destruction-lemma`. No Lean, repository, or ledger changes were made; the worktree is clean at `6a96398`.
## Inspection
- **Conversation/context:** Previous turn completed the full GC task (proof, verification, board post). No interrupted tool call is visible in current context; the recovery instruction appears to be precautionary.
- **Working directory:** `/home/lubko/soring-fronts/good-comparison-cover-destruction-lemma` (git repo, on `billy-dev`, clean worktree at `6a96398`).
- **Git state:** `## billy-dev...origin/billy-dev`, working tree clean (`git status --short` empty). Recent commits unchanged (merge of 6859bc2 etc.). No local branches/commits/PRs created.
- **Durable task records:**
  - Frontier ledger (`~/.local/state/soringp1/frontier-ledger.json`): `good-comparison-cover-destruction-lemma` exists (ai_proposal_unverified), status `running`, agent_id `UATByjgHS6GOeVkCe3vmb9-deposits`, basis/implication/falsifier match the board post. No changes made to ledger.
  - Board #301: confirmed via `board_digest.py --contains "GC is TRUE"` — post by `SoringP1 frontier: good-comparison-cover-destruction-lemma` at `2026-11-10T07:37:38.939Z` with full GC proof, verification (n≤8 + random n≤12), and explanation of why it does not revive (U). Post succeeded (antonina returned JSON, no stderr).
- **Scratch artifacts:** `/tmp/opencode/gcwork/` contains `gcsearch.py`, `gcproof_check.py`, `post.md`, `post_result.json` (and `post_result.err` empty). No files created/modified in repo paths.

## Effects actually performed
- **External post:** One board comment posted to Antonina issue #301 (GC proof + findings). Confirmed present on board; **not duplicated**.
- **No other side effects:** No commits, no PRs, no Lean changes, no repo changes, no purchases, no ledger mutations.

## Unfinished work
**None identified.** The front’s question (is GC true / does it revive the cover-destruction induction for (U)?) was answered completely:
- GC is true for all non-total finite posets (inductive proof with a constructive pair selection rule; verified exhaustively n≤8, randomly n≤12).
- GC does not revive the (U) induction (exact D-balanced condition is strictly stronger; n=3 and n=5 counterexamples to the exact condition remain; n=5 satisfies GC but blocks the exact condition for all C′).
- Complexity implication stated (general-poset theorem, not a certificate for S(n)/SORT-BOUND-U).
- Posted to board #301 with honest limits and falsifier mismatch noted.

If the keeper wants to transition the ledger front from `running` to `investigated` based on this posted finding, that would be a separate ledger update (not performed here), but it’s not required to report the result and there’s nothing unfinished to continue. No actions taken.

## Other metadata

```json
{
  "finished_at": 1794296447.933341,
  "started_at": 1794294249.6354554
}
```
