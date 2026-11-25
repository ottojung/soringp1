# antonina-4rCohgIIUW0rikPm8V2ntn-complain

Session: ses_e012063c1ffe0oO9o7kyEx3XW3
Workspace: /home/lubko/soring-fronts/curator
Created: 1795277429831; updated: 1795278194194

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fedf9c6a0016udoy2sbxCQi7H)

I'll start by orienting myself: checking the git branch, reading the key docs, and finding how to access board #301.

## Output 29 (msg_1fedfc63b001kyQuutx6w3VSrQ)

The branch is `main`; the user's "billy-dev" likely refers to the execution host. Let me verify and gather the board digest, literature, and existing frontier definitions.

## Output 48 (msg_1fedfe48c001G3WML9xWz5VgV3)

Host confirmed as `billy-dev`. Let me gather more board context and understand the 645-front ledger to avoid duplication.

## Output 76 (msg_1fee014c1001RFlcVHrLJlecg0)

Now I understand the active frontier. Let me survey all 645 front IDs/questions and read the key theory notes to find genuinely new angles.

## Output 91 (msg_1fee078240013CAgX3enrt1OCH)

Let me see the rest of the fronts and search for keywords related to promising new angles.

## Output 106 (msg_1fee097ab001yrew7567haJVfA)

Let me inspect the newest fronts (tail) and their statuses, plus check for any board posts newer than 16:07Z.

## Output 121 (msg_1fee11155001ekJ48KkQpX88lf)

I've mapped the frontier. Let me verify a concrete mathematical claim computationally and check novelty of my candidate angles against all 645 fronts.

## Output 145 (msg_1fee2518d001ZF6K1tjeYZG8UK)

I have a concrete mathematical finding (the defect-superadditivity DP matches S through n=6, first fails at n=7, gap Θ(n log n)) and three distinct, non-duplicate angles. Let me write and validate the JSON.

## Output 163 (msg_1fee327a8001FQ08LJgcWzQ7Kx)

Schema validates. Let me do a quick primary-literature check on whether the antichain superadditivity bound is already classical, since that affects the novelty claim.

## Output 183 (msg_1fee360a3001D3622N1WHtP9v1)

Done. Deliverable is at `/home/lubko/soring-fronts/curator/frontier-candidates.json` (validated JSON, 3 fronts, all field-length constraints met).

## What I did

- Confirmed host `billy-dev` (the git branch is `main`; "billy-dev" is the execution host per `docs/operations.md`).
- Read `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, `docs/research-plan.md`; read the 20 newest `#301` posts (through 16:07Z) and all 645 ledger fronts (623 investigated, 22 blocked) to screen for duplicates.
- Checked primary values against OEIS A036604: `S(1..22) = 0,1,3,5,7,10,13,16,19,22,26,30,34,38,42,46,50,54,58,62,66,71`.

## Claim I attacked and the outcome

**Claim (falsifiable, all-n):** the polynomial-time defect-superadditivity DP
`L(1)=0, L(n)=max_{a+b=n}[L(a)+L(b)+min(a,b)+1]` computes `S(n)` exactly for all `n`.

**DISPROVED** by scratch computation: `L(n)=S(n)` holds for `n≤6`, first fails at `n=7` (`L(7)=12 < S(7)=13`), and the gap grows to `13` at `n=22`. Paper argument: balanced splitting solves the recurrence to `0.5·n·log₂n + O(n)`, while `S(n) = log₂(n!) + o(n) ~ n log₂ n`, so `S(n)−L(n) = Θ(n log n)`.

**Honest limits:** this says nothing about whether the defect inequality `D` itself is true — `D` could hold and still yield this weak recursion. It is a general-poset/superadditivity obstruction, not a lower bound for computing `S(n)`; no P/NP/PSPACE separation follows. Soundness of a lower-bound recurrence is not completeness of an evaluator. Web search was cancelled in this session; I relied on the repo literature baseline plus a direct OEIS fetch, so novelty against the outside literature is not fully certified.

## The three proposed fronts

1. `antichain-superadditivity-minplusone-alln` — isolate the **antichain-only** defect inequality, the sole case needed for `S(n)`.
2. `antichain-defect-sufficiency-vs-general-alln` — does the antichain case imply the general disjoint-union defect inequality, or is the general statement strictly stronger than anything needed for `S(n)`? (draws the general-poset vs. antichain line).
3. `superadditivity-tight-split-finiteness-alln` — is the set of `n` with a defect-tight split finite (largest `6`) or infinite?

No Lean, tests, commits, ledger edits, or board posts were made; the only repository change is the requested JSON file.

## Output 215 (msg_1feeb19b1001SLEedHG0vkk0Kk)

## Recovery inspection

- **Working directory / repo:** `/home/lubko/soring-fronts/curator` on `billy-dev`, branch `main`, HEAD `f89f6d0 Add research note: FO(TC) strategy programs for exact optimal sorting`.
- **Git state:** clean except for one untracked file: `?? frontier-candidates.json`. No staged changes, no tracked-file diffs, no new commits.
- **Durable deliverable:** `/home/lubko/soring-fronts/curator/frontier-candidates.json` exists (3109 bytes, valid JSON). It contains exactly the requested `fronts` array with 3 entries; each has `id` (6–63 lowercase slug), `question` (>=75), `falsifier` (>=40), `implication` (>=40), `basis` (>=35).
- **External side effects:** none detected beyond creating that local file and scratch `/tmp/opencode/*` artifacts. I did **not** post to Antonina #301, did **not** edit the frontier ledger, did **not** commit/push, and made **no** Lean/test/CI/repo-content changes.

## Status

The requested task is already complete; no unfinished work remains. I did not repeat any external action. If you want, I can also review the three proposed fronts for novelty/defensibility against the board before they are imported, but I will not post or commit anything without explicit instruction.
