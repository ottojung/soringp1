# single-deletion-eta-characterization

## status

investigated

## origin

ai_proposal_unverified

## agent_id

GEPPaI3rpnMnF9kzgwl3sn-treading

## exit_state

clearexit

## question

For all integers a,b >= 2, is the exact minimax value of the single-deletion prime poset P=(A_a (+) A_b) - {(a0,b0)} equal to S(a)+S(b) when min(a,b) >= 3 and to S(a)+S(b)+1 when min(a,b)=2?

## basis

Newest board #301 prime-excess-unbounded (02:00Z) proves F(P) is in {S(a)+S(b), S(a)+S(b)+1} and leaves the exact value open; independent exact minimax computation here for a,b <= 6 gives eta=1 for min=2 and eta=0 for min>=3.

## falsifier

Exhibit a,b >= 3 with F(P) = S(a)+S(b)+1, or a,b with min(a,b)=2 and F(P) = S(a)+S(b), by exact minimax computation.

## implication

A positive answer would fix the exact excess of the prime single-deletion family as E(a)+E(b)+d+eta, resolve the n=27 base ambiguity, and give a precise structural theorem about the minimax game on a family built from S(n).

## finding_unverified

he excess `η = F − S(a) − S(b)` is `1` for `(2,2),(2,5),(5,5)` and `0` for the others. The excess `d = F − ⌈log₂ e⌉` is `0` for all these except `(5,5)`, where it is `1`. So the exact value is **not** determined by `min(a,b)`, nor by the maximum of the two lower bounds.

## Soundness vs completeness, and scope

- The lower bounds `F ≥ S(a)+S(b)` and `F ≥ ⌈log₂ e⌉` remain **sound**.
- The front’s proposed **completeness** rule is false: the two lower bounds do not determine `F`.
- These are results about a specific prime poset family, not general-poset hardness. No complexity-class consequence for `S(n)` or `SORT-BOUND-U` follows.
- The `n=27` base ambiguity `F(P₁) ∈ {72,73}` remains open; the exact all-`n` characterization is a new open problem.

## Limits

The `(5,5)` value is an exact game search, not a paper adversary argument. The decomposition’s correctness is supported by cross-checks on smaller cases and a second independent implementation, not a formal proof. I made no repository or Lean changes; the worktree is clean at `6a96398`. A concise report was posted to Antonina issue #301 at 07:27Z.
**Recovery inspection (no external actions taken)**

- **Conversation/work state:** The prior turn’s checkpoint indicates the `single-deletion-eta-characterization` front was fully investigated and reported (claim refuted by exact counterexamples), with “Next move: none.”
- **Working directory / Git:** `/home/lubko/soring-fronts/single-deletion-eta-characterization` on `billy-dev`, `HEAD 6a96398` (`Merge commit '6859bc2'...`), `git status` clean (no uncommitted changes).
- **Durable scratch records:** `/tmp/opencode/singdel/` present with reported artifacts including `post.md`, `post_result.json`, `post_err.txt`, and computation scripts/logs (e.g. `full.py`, `full_5_5.log`, `decomp.py`, `decomp_5_5.log`, `decomp_4_6.log`, `verify.py`, `values.py`, `mm.py`, `budget.py`).
- **Board (Antonina #301):** `board_digest.py --contains "single-deletion-eta-characterization"` shows the finding comment present once: `2026-11-10T07:27:22.885Z` by `SoringP1 frontier: single-deletion-eta-characterization` (“…proposed all-n claim is FALSE. Two exact counterexamples…”), consistent with the prior post. No repost attempted.
- **Frontier ledger:** `~/.local/state/soringp1/frontier-ledger.json` exists (not modified). I did not update keeper-managed state.

**Determination of external effects**
- **Occurred (confirmed):** 1 Antonina board comment on issue #301 at `2026-11-10T07:27:22.885Z` for `single-deletion-eta-characterization` (present once on board; local post artifacts exist in `/tmp/opencode/singdel/`).
- **Did not occur:** No commits, pushes, PRs, repository/Lean edits, or other external actions observed (`git` clean/same HEAD).

**Unfinished work / actions continued**
- None. All substantive work for this front was already completed and reported; I did not repeat or duplicate the interrupted prompt or any external side effect.

**Uncertainty for review**
- Minor: I did not fully parse the ledger entry structure in this pass beyond confirming the ledger file exists (structure differed from expectation), and I did not re-run/independently re-verify the earlier `(5,5)` exact-search results now; the prior checkpoint already records them as exact game-search evidence with cross-checks and stated limits. If desired, follow-up would be independent verification/paper argument for the `(5,5)`/larger cases or keeper-managed ledger status adjustment (separately).

## Other metadata

```json
{
  "finished_at": 1794295875.1621916,
  "started_at": 1794289509.9526944
}
```
