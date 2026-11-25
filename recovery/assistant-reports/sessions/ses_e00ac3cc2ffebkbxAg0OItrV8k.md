# antonina-pL1FHDN3sXwph5kMKnah9R-products

Session: ses_e00ac3cc2ffebkbxAg0OItrV8k
Workspace: /home/lubko/soring-fronts/curator
Created: 1795285041988; updated: 1795285724232

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_1ff5b3444001yZMp7eWI5fqmZi)

I'll start by inspecting the environment, Git state, and the relevant documents before doing anything else.

## Output 28 (msg_1ff5b4bd3001WvmkHx5Dc4OTKH)

I'm on `main`, not `billy-dev`. Let me check the branch situation carefully before proceeding.

## Output 43 (msg_1ff5b643e001j2Wsc2cJAQ0gqL)

There is no `billy-dev` git branch (local or remote) — it must be an agent/execution context label, not a branch. I'll note that. Let me read the key documents and discover how the board is accessed.

## Output 62 (msg_1ff5b7f16001rPnulHfYiuneyf)

Good — `billy-dev` is the execution host (per operations.md), and I'm running there. The git branch is `main` (normal for these worktrees). Now let me check the board digest, the durable ledger, and existing frontier state to understand recovery status and avoid duplicates.

## Output 77 (msg_1ff5ba1c5001NQuFA7dpHvL1at)

Let me get a complete inventory of ledger front IDs/statuses and the fuller recent board content, so I can identify genuinely nonredundant directions.

## Output 144 (msg_1ff5cb84f001DFvKifbC4RqqZY)

Let me check my candidate directions against the full ledger text for redundancy before deciding.

## Output 155 (msg_1ff5d07b3001T5a9pYSZyf5Kko)

Let me inspect the specific existing "faster evaluator" fronts to judge whether a pruning-oracle angle is redundant.

## Output 166 (msg_1ff5d714c001NYbBeZ1Z11ifny)

I've mapped the 651-front ledger, the board's newest (18:03–18:25Z) results, and confirmed no `frontier-candidates.json` exists yet and no prior side effects from me. Let me do a final uniqueness/length check on my candidate IDs, then write the deliverable.

## Output 177 (msg_1ff5ddf5600152dD8Iat8HgQ2z)

All checks pass. Writing the deliverable now.

## Output 195 (msg_1ff5e0f2a0017gjUeEUR0jais0)

Done. Deliverable written and validated at `/home/lubko/soring-fronts/curator/frontier-candidates.json`.

## What I did

**Recovery audit first.** Confirmed `billy-dev` is the *execution host* (per `docs/operations.md`) and I'm running on it; there is no `billy-dev` git branch (these worktrees are on `main`, clean). Checked the durable ledger: all 651 fronts are `investigated`/`blocked` — none pending — so there was no unfinished work to duplicate. No `frontier-candidates.json` existed, and I made no Antonina posts, commits, or other external writes.

**Studied** `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, the full ledger, and the newest board #301 posts (18:03–18:25Z, fetched in full). I attacked candidate claims for redundancy with exact-keyword scans over all 651 front texts.

**Proposed 3 nonredundant fronts** (IDs validated unique; `sawtooth`, `threshold t(n)`, and `pruning oracle` had 0 ledger hits):

1. `fj-threshold-sawtooth-limit-alln` — does the info+FJ threshold ratio `t(n)/n` converge, or oscillate with the FJ sawtooth? (method-scope barrier, from the 18:03Z result + 18:25Z referee corrections)
2. `infofj-band-pruned-exact-evaluator-alln` — can the newly poly-time-computable predicate `P(a,b)` serve as a pruning oracle to beat `2^{O(n log² n)}` for exact `S(n)`? (the complexity/upper-bound front)
3. `refinement-defect-failure-all-a-alln` — does defect-refinement monotonicity fail for *every* a≥1? (the 18:13Z front's stated leftover)

## Honest limits

- **No proof or verification is claimed** in any field; every front is phrased as a question with a falsifier horn.
- Fronts 1 and 3 are **structural / method-scope** and explicitly carry **no complexity consequence** and no transfer to `S(n)` without a reduction. Front 2 is the only complexity-directed one and is speculative — its falsifier horn (barrier) is plausible.
- The newest results themselves are paper-level/experimental with referee corrections; I did not re-derive them here.
- **No repository, Lean, test, CI, ledger, or canonical-main changes.** The only file created is the required JSON deliverable (shown as untracked by `git status`); `S(n)` and `SORT-BOUND-U` remain open.
