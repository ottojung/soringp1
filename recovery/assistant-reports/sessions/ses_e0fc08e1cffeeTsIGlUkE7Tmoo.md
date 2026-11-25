# antonina-hW8x4sT0fbLxLxQcxUl742-guidance

Session: ses_e0fc08e1cffeeTsIGlUkE7Tmoo
Workspace: /home/lubko/soring-fronts/curator
Created: 1795032052208; updated: 1795032268887

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f03f7236001bH9wDyKHxSc7VA)

I'll start by exploring the repository structure and the key documents mentioned, then locate board #301.

## Output 21 (msg_1f03f8a2b0018eP8UggyWe5gTR)

I'm on `main` but the task requires `billy-dev` ONLY. Let me check branches and locate the key documents and board #301.

## Output 40 (msg_1f03f9aea001m5rUlFN3WRIUn1)

`billy-dev` is a host, not a branch. Let me verify the hostname and check the board digest.

## Output 51 (msg_1f03fab6a001mtvJtF983RCXiV)

Hostname confirmed as `billy-dev`. Let me gather the full context: the ledger, existing fronts, current candidates, and more board pages.

## Output 70 (msg_1f03fc083001bYJpafE3AjwIRJ)

Let me extract a compact summary of all ledger fronts and read more board pages plus the research plan.

## Output 85 (msg_1f03fccf8001Cs38mETrrHi7UZ)

This frontier is heavily saturated (540 fronts). Let me read the freshest board #301 posts in full and inspect the digest script options.

## Output 109 (msg_1f03ff8e6001LrxW1TDlh11iGq)

This frontier is extremely saturated (540 fronts investigated/blocked). Before deciding, let me ground myself in the primary literature on the *complexity* of computing sorting numbers, and independently verify the freshest deduction.

## Output 142 (msg_1f0414060001j8EEjBV2RxLHt0)

Let me check the ledger findings for the many related fronts to avoid duplicating their conclusions, and verify a couple of specific "entropy/excess/balance" results.

## Output 162 (msg_1f04185e6001qmGwr62VxXm55h)

I've confirmed the major angles are covered. Let me do one independent computational check of the freshest deduction to ground my decision in checked evidence, using a fresh implementation (no repo oracle import).

## Output 180 (msg_1f041ed0a001M9wo5H2x4IevMG)

My independent check reconfirms known findings (e(P) doesn't determine F at n=5: e=8 yields F∈{3,4}; local excess first appears at n=5 in 120 states) but surfaces nothing novel. Let me verify the repo is clean and write the curator output.

## Output 209 (msg_1f0424b12001BKszdP6J71mHjv)

Done. Here is my honest report.

## What I did (on `billy-dev`, hostname verified)

- Studied `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, `docs/research-plan.md`, the research frontier, and the current Antonina **#301** digest (pages 1+, freshest posts 16:38Z–19:47Z).
- Read the full frontier ledger: **540 fronts (519 investigated, 21 blocked)**, plus the 20-front `PREVIOUS` list.

## Claim attacked and independent check

I attacked a candidate all-`n` claim about exact unary `S(n)`: whether a reachable poset's extension count `e(P)` determines the minimax value `F(P)` well enough to support a local-entropy exact evaluator/pruner. Using a fresh from-scratch implementation (no repo oracle import) I computed reachable posets within budget `S(n)` for `n=4,5`. **Result (experiment):** at `n=5`, `e=8` admits both `F=3` and `F=4` (120 states), and local excess `F−⌈log₂ e⌉` first becomes nonzero at `n=5` (120 states with excess 1) — reconfirming the already-posted finding, not a new theorem. This also independently aligns with the fresh #301 deduction that every sorter has `2n!−1` distinct reachable posets (state-merging cannot compress), and that greedy intersection-merge confluence is refuted.

## Why no new front is defensible

Every angle I could formulate maps to an existing investigated/active front:
- **Reachable-state compression / join-reduced / framed-DAG completeness** → `join-reduced-*`, `framed-dag-*`, `subtree-isomorphism-kernel-polynomial`, `canonical-form-reachable-posets`.
- **Entropy/balance pruning & local-vs-root excess** → `entropy-balance-*`, `local-gap-global-complexity-barrier`, `local-excess-root-transfer`, `cheap-zone-excess-unboundedness`.
- **Exponent / space / certificate class membership** → dozens of dedicated fronts; unary super-polynomial lower bounds remain blocked by known separations (`P≠PSPACE`, `NP≠PSPACE`).
- **The one genuinely live follow-up** (all-`n` budget-tight nontransitivity) is already running as an active front.

The Executive has repeatedly (18:37Z, 19:17Z, 19:28Z) declared the frontier depleted and instructed that further dispatch would be forbidden filler. I found no genuinely novel, non-duplicate, independently grounded all-`n` falsifiable question.

## Honest limits & side effects

No proof, counterexample, or new theorem was produced; nothing is claimed as verified. No Lean, test, workflow, or tracked repository changes were made (fresh scratch code only in `/tmp/opencode`). The only artifact is the required curator output:

`/home/lubko/soring-fronts/curator/frontier-candidates.json` → `{"fronts": []}`

Output is a valid JSON object with a `fronts` array (empty, as permitted when no defensible new direction exists).

## Output 234 (msg_1f04295e4001LAxT4SbzoRvRPj)

**Recovery inspection (no duplicate actions taken)**

- **Conversation/work done:** Previous turn completed the curator task in this session: studied `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, board #301 digest, frontier/ledger context, and ran a fresh scratch check (`/tmp/opencode/curator_check.py`, no repo oracle import). No Antonina board posts, commits, agent launches, purchases, or other external actions were performed.
- **Working directory / Git (`/home/lubko/soring-fronts/curator`, `main`, `billy-dev` host):** clean tracked state; only untracked artifact `frontier-candidates.json` (`-rw-r--r--`, 2026-11-18 20:03, 15 bytes). No staged/committed changes.
- **Durable task record:** `frontier-candidates.json` exists and contains the required output: `{"fronts": []}` (valid JSON, empty list — no defensible non-duplicate all-`n` front identified against the saturated ledger/board).
- **Unfinished work:** none. The requested deliverable is present and correct; nothing remains to continue.

**Uncertain effects:** none identified. If any external side effect was claimed outside this environment (e.g. a board post not visible in local state), I cannot confirm it from local records and it should be reviewed rather than guessed — but I did not initiate such actions. I will not re-run or duplicate anything.
