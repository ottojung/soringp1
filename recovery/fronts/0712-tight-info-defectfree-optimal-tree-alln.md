# tight-info-defectfree-optimal-tree-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

JeM4g6qvoS8cuPuj1UaZVN-pelican

## exit_state

clearexit

## question

For every integer n>=1 with S(n)=ceil(log2(n!)), is there a height-S(n) adaptive comparison decision tree sorting the n-antichain in which every reachable state P satisfies F(P)=ceil(log2(e(P))) (information-defect zero)?

## basis

docs/problem.md defines S(n) and the information bound; research-n12-nontightness.md H3 gives same-e states with different F and local defect despite tight global S(5); board #301 reports independently checked defect-free optimal trees for n=6,7,8,9 and n=11 under investigation.

## falsifier

Exhibit any n with S(n)=ceil(log2(n!)) and a certified argument or exhaustive search showing every height-S(n) sorting tree reaches some state P with F(P)>ceil(log2(e(P))).

## implication

A positive answer would show root information tightness propagates to a locally tight optimal certificate, constraining exact-search and certificate structure on tight instances; a counterexample would separate global and local information tightness.

## finding_unverified

s real (local tightness => balanced split exists, but not obviously defect-free children) [deduction]; exhaustive reachable-state check finds no tight-but-trapped state for `n<=6` [experiment]; the claim is non-vacuous and includes known tight `n=20,21` beyond the small-n board witnesses [literature/computation].
- **What is not established**: no proof that propagation holds for all tight `n`; no counterexample; no independent re-verification of board n=8/n=9 witnesses; n=11 undecided.
- **Limits/honesty**: this does not change S(n) or SORT-BOUND-U. A defect-free tree has `2n!-1` nodes and is not an NP/certificate-complexity object. The small-n Python check is a sanity experiment, not a formal proof artifact. The strongest next decisive case remains n=11 (decides smallest non-defect-free n between 11 and 12 under the reported n<=10 evidence), but n=20,21 remain open tight instances for the all-`n` claim.
I'll audit the actual state before doing anything else. No board posts, commits, or external writes were intentionally made in my prior turn — but I'll verify rather than assume.
I have enough to conclude, but let me do one final local check for any board text unique to my report (no external calls).
## Audit result: no external side effects occurred; no unfinished work to continue

I inspected the conversation, working directory, Git state, and durable task records. Findings:

**Effects that actually happened in the prior turn**
- Read-only operations only: file reads (`AGENTS.md`, docs), `board_digest.py` queries and `antonina board show --json` fetches (reads), and local scratch files in `/tmp/opencode` (`check_defectfree.py`, `board301-p1.json`, `board-*.txt`, `post-*.txt`).
- The turn delivered a complete research report (status: **UNRESOLVED**, with a small-n experiment and the compositional-gap obstruction).

**Effects that did NOT happen**
- **No board post.** Searched all 8 pages of #301 for my front slug `tight-info-defectfree-optimal-tree-alln` and for unique phrases from my report (`tight-but-trapped`, `propagation gap`, `37206`, `33482`) — zero matches. No post by me exists to duplicate or undo.
- **No commit / repo change.** `git status --porcelain` empty; `HEAD = 6a96398`; `git reflog` = clone only. No Lean/test/CI change.
- **No durable record write by me.** The ledger entry for my front shows `status: "running"` with `started_at` set at keeper launch — this is infrastructure state from the front being commissioned, not a side effect of my turn. I made no ledger/bill/case/main change.

**No uncertain effects.** Everything is accounted for: the only artifacts are scratch files under `/tmp/opencode` at timestamps 09:09–09:12 matching the prior turn. Nothing external is in a partial or ambiguous state.

**Unfinished work:** none. The prior turn completed its full deliverable (the falsifiable all‑n question, falsification attempts, small-n exhaustive check, structural obstruction, and honest limits). The research conclusion stands as reported:

- Claim unresolved; no proof, no counterexample.
- Exhaustive reachable-state check for `n≤6`: no locally-tight-but-not-defect-free-extendable state found; defect states exist but are avoidable.
- `n=7` full enumeration did not complete in-budget; `n=11` and tight `n=20,21` remain open; board n=8/n=9 witness claims were not independently re-run by me.

I have taken **no external action** in this turn and will not re-post, re-commit, or repeat the computation. No review item is needed.

## Other metadata

```json
{
  "finished_at": 1795425576.8090527,
  "started_at": 1795424896.111798
}
```
