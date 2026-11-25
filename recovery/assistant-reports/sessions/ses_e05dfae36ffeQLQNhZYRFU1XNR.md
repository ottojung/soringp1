# antonina-qZZvbx8LwTO6aNSq6tBvBN-connect

Session: ses_e05dfae36ffeQLQNhZYRFU1XNR
Workspace: /home/lubko/soring-fronts/kraft-converse-reachable-20261120
Created: 1795197784663; updated: 1795199500840

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fa2055de001OPvPwUXlxT5O4P)

I'll start with the recovery and authority phase: reading the required documents and board posts before doing any research.

## Output 25 (msg_1fa207077001yQYK29RKfRUyaE)

Now let me read the operations doc, source the profile, and check the literature and git state.

## Output 44 (msg_1fa209d13001rRTAiW68ZZHELR)

Git HEAD matches the expected commit and worktree is clean. Now let me read the #301 board, paginating carefully.

## Output 118 (msg_1fa2163440011O4WoOd2vOKosa)

Let me check the Peczarski A/B/C conditions and Sergeev references in the repo, plus the related notes on this exact front.

## Output 264 (msg_1fa22f10e001QuVbvKDCJXY0rH)

I've completed the recovery/authority phase. Now let me set up an independent computation scratch script (no repo changes) and validate the approach on known small cases first.

## Output 320 (msg_1fa295238001EUt6XF0gA6MgNz)

This is a significant finding — let me verify it very carefully with independent implementations before believing it. First, let me reconstruct explicit paths and analyze the violating states in detail.

## Output 356 (msg_1fa2fd41a001puTvEb2XqUUFLX)

The violations are independently confirmed. Let me now trace the precise mechanism (why G exceeds eps) and check reachability via strict adversary paths too.

## Output 374 (msg_1fa32b99c001tUvuu46lVl33Z7)

The mechanism is now clear. Let me verify the strict adversary-path reachability question and double-check the pi bound with brute-force counts.

## Output 392 (msg_1fa360b370010GBLl2VrmOrnHk)

All 13 violations are reachable even via strict adversary-only paths, and max adversary π = 2 through n=8. Let me check the Antonina posting interface.

## Output 426 (msg_1fa38f9c7001Kdi4MagwpN3ltp)

I have a fully verified result. Let me write the finding and post it once to #301 (the single allowed external write).

## Output 444 (msg_1fa397d45001ifU0mEMVyNLJoe)

The post is confirmed on #301 (id `sha256:2cgwjV3TM...`, 18:30:29Z). Now let me perform the final recovery/side-effect audit.

## Output 455 (msg_1fa39aa3f001Vm5In4f1FNKaxI)

## Research summary

I completed the recovery/authority phase, then ran an independent finite computation. The result is a **counterexample to the reachable-state converse `G(P) ≤ eps(P)` at n=8**, independently verified.

### What I did first (authority)
Read `AGENTS.md`, `docs/problem.md`, `docs/research-plan.md`, `docs/operations.md`, `docs/literature.md`; paginated all of #301 (`board show --json`, pages 1–10, no parser failures) and read the four specified 2026-11-20 posts. Verified Sergeev's `S(n)=log₂(n!)+o(n)` directly at ECCC TR20-096, and examined Peczarski 2012 (no literally labelled "A/B/C conditions" in that text; recorded honestly).

### Result (all claims labelled)
- **[experiment]** Independent scratch implementation: transitive-closed successor masks; `e` by subset DP, cross-checked by brute-force over all 8! permutations; canonical form by 1-WL refinement, validated because the F-memo visits exactly the unlabelled-poset counts (318/2045/16999 for n=6/7/8) and `F(A_n)=S(n)` for n≤8. A **second implementation** (labelled, no canonicalisation) reproduced `e, F, G` at every witness.
- **n=5,6,7 [experiment]:** `G(A_n)=D(n)=0`; no reachable `P` with `G>eps` (19/134/802 reachable states).
- **n=8 [experiment]:** `G(A₈)=D(8)=0`, 5102 reachable states (all also reachable via adversary-only paths). **13 states have `G(P)>eps(P)`**: ten with `eps=0, G=1`, three with `(eps,G)=(1,2)`.
- **Explicit witness [experiment, re-checked]:** poset with successor masks `(62,48,8,0,32,0,140,12)`, reached by the adversary-only optimal path `(0,1),(2,3),(0,2),(1,4),(1,5),(2,6),(2,7),(4,5),(6,7)`, π = `1,1,1,2,0,2,0,1,1`. Brute-force `e=65`, `b=7`, `F=7`, `eps=0`, independent `G=1 > 0`.
- **[deduction] Precise obstruction:** `eps` is a signed sum of `(1−π_i)` losses; `G` counts nonclean steps unsigned. Here all optimal comparisons at P are clean, but the adversary takes a clean π=2 step (loss −1) to a child where the optimal comparison is nonclean (loss +1). The negative subsidy is invisible to `G`, so `G(P)>eps(P)` even at an information-tight state — the exact signed-sum/negative-subsidy point flagged at 16:51Z, now realised.
- **[experiment] Question (2):** max adversary-path π is 1 (n≤5), 2 (n=6,7,8); **no π≥3 through n=8** (non-adversary slack children reach π up to 5).
- **[deduction] Limits:** refutes only "G(P)≤eps(P) for all reachable P". Does **not** affect `G(A_n)=D(n)=0`, the clean-split sufficient lemma, known `S(n)` values, or SORT-BOUND-U. No theorem claim. n=9 not attempted (≈183k states; n=8 already settles it).

### Delivery / side-effect audit
- **External effects:** exactly one — a single finding posted to Antonina #301, author `SoringP1 independent researcher: kraft-converse-reachable-20261120`, id `sha256:2cgwjV3TMX_elNN3aPFrWzmeMvb8B5qbgXtfgJ0qL5M`, 18:30:29Z. No other writes.
- **Worktree:** clean, HEAD `6cddeaa2453d4da2ae0e918e50ba61c71a7da85f`. No repo, Lean, test, workflow, ledger, or canonical-main changes; no commits.
- **Scratch paths (only):** `/tmp/opencode/soring301/` (board JSON pages, `minimax_scratch.py`, `verify_violations.py`, `mechanism.py`, `adv_reach.py`, `adv_path.py`, `post_body.txt`, outputs, and `pec2012.pdf/.txt`).

## Output 493 (msg_1fa3a4c7e001ej7h3251s76gcl)

## Recovery inspection (post-interruption)

Inspected the existing conversation, working directory/Git state, scratch artifacts, and the durable board record. I did **not** re-run the research prompt or repeat any external action.

## Effects that actually happened

- **Board post (confirmed, single, not duplicated):** `antonina board comment --id 301` succeeded. Live board page 1 now contains exactly one matching message:
  - author: `SoringP1 independent researcher: kraft-converse-reachable-20261120`
  - id: `sha256:2cgwjV3TMX_elNN3aPFrWzmeMvb8B5qbgXtfgJ0qL5M`
  - createdAt: `2026-11-20T18:30:29.639Z`
  - content: the n≤8 `G(P)≤eps(P)` counterexample/π-bound finding (witness at n=8, adversary-only path, independently re-checked). This matches `/tmp/opencode/soring301/post_result.json` and `post_body.txt`.
- **Scratch-only local files (no external effect):** `/tmp/opencode/soring301/` contains computation scripts and outputs used for the result (e.g. `minimax_scratch.py`, `verify_violations.py`, `mechanism.py`, `adv_reach.py`, `adv_path.py`, `n8_out.txt`, `verify_out.txt`, `post_body.txt`, `post_result.json`, board snapshots/Peczarski text).
- **No other external effects:** no commits, no repo/Lean/test/workflow/ledger/canonical-main changes, no PRs, no purchases, no additional posts.

## Git / worktree state

- HEAD: `6cddeaa2453d4da2ae0e918e50ba61c71a7da85f` (unchanged)
- `git status --short`: clean

## Unfinished work

**None.** The assigned questions were completed: definitive, independently re-checked finite computation for n≤8 (counterexample to the converse at n=8; adversary-path max π = 1 for n≤5 and 2 for n=6,7,8, no π≥3 through n=8) with a precise signed-sum obstruction, and the single allowed evidence-bearing finding posted to #301.

## Uncertainties

**None material.** The post’s presence and uniqueness are directly confirmed on the live board; all other effects are local/scratch and auditable. No effect remains uncertain, so nothing requires review-as-uncertain action.
