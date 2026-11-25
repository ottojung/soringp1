# antonina-0qtyC04N8DKrCoSQhjKVZ8-grants

Session: ses_e46332986fferwdzLTUAdtCmon
Workspace: /home/lubko/soring-fronts/curator
Created: 1794118571668; updated: 1794119995054

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b9ccd6e9001EldlPlMggRs50N)

I'll start by understanding the current state: reading the contract, problem docs, board #301, and the existing candidate file.

## Output 369 (msg_1b9de70f6001wJX2wM5yYU11Ge)

I'll verify the key cover-count facts computationally before committing to a frontier claim.

## Output 407 (msg_1b9e18cc2001LAL4ffStDyc5dh)

Studied `AGENTS.md`, `docs/problem.md`, the live board #301 (newest posts), the research ledger, and the current literature notes on billy-dev.

**Falsification attempt (concrete finding).** I attacked the newest all-\(n\) reachability claim: states reachable in \(k\) comparisons are exactly posets with \(|cov(P)|\le k\).

- The lemma’s *statement* survived: an exhaustive check over all labelled posets for \(n\le 5\) (4,231 states at \(n=5\)) found zero discrepancies between BFS distance and \(|cov(P)|\).
- However, the posted proof contains a false intermediate claim: “a cover of \(P\) remains a cover of \(Q\).” Counterexample: \(P=\{0<1,\ 0<2\}\), compare \(1\) vs \(2\) with outcome \(1<2\); then \((0,2)\) is a cover of \(P\) but not of \(Q\). Comparisons can destroy several covers at once.
- The lemma is still repairable: each comparison adds exactly one new cover, and all current covers lie among the covers ever added, giving \(|cov(P)|\le k\); sufficiency follows because distinct target covers remain covers when other target covers are added. So this is a proof-step erratum, not a counterexample to the lemma.

Honest limits: no counterexample to the lemma was found, no board post was made, and no Lean or repository changes were made beyond the required candidates file (worktree otherwise clean).

**Curator output.** Wrote two non-duplicate fronts to `/home/lubko/soring-fronts/curator/frontier-candidates.json`:

1. `pp-hardness-transfer-antichain` — tests whether the board’s new PP-hardness of the general-poset Fibonacci threshold transfers to exact unary `SORT-BOUND-U`, explicitly separating sound general-poset hardness from antichain completeness.
2. `cover-destruction-lower-bound` — uses the reachability lemma’s cover-count structure to ask whether a destruction potential can prove infinitely many non-tight \(n\).

Both are all-\(n\), falsifiable, and schema-validated; neither claims a proof or verification.

## Output 468 (msg_1b9e262b7001JxiSAYC1yT114A)

Recovery inspection complete; no duplicate external actions taken.

**Effects that actually happened**
- `/home/lubko/soring-fronts/curator/frontier-candidates.json` exists, is valid JSON, and contains exactly two fronts: `pp-hardness-transfer-antichain` and `cover-destruction-lower-bound`.
- No commits were made; `git status` shows only the untracked candidates file.
- No board #301 post was made by this curator (latest board entries are from other agents/Executive, none matching this work).
- No Lean, docs, test, or repository edits.

**Durable records**
- The frontier ledger still holds the older `curator` entry (`0qtyC04N8DKrCoSQhjKVZ8-grants`) and does **not** yet contain the two proposed IDs. Importing them is the deterministic keeper’s job, not this curator’s; I did not force it or write to the ledger.
- The candidates file passed schema/length/slug validation and its IDs do not collide with the 348 existing ledger fronts.

**Unfinished work**
- None on the curator deliverable. The JSON was already written and validated before the interruption.
- One item for review, not action: the earlier mathematical pass found that the board’s 05:56Z reachability *proof* contains a false intermediate sentence (“a cover of \(P\) remains a cover of \(Q\)”), though the lemma’s statement itself survived exhaustive checks through \(n=5\). No board erratum was posted.

I will not re-run the prompt or rewrite the file.
