# antonina-T7jz6emDaUC9QL10b5I3PE-deceive

Session: ses_e03ef4b90ffe5N5SPO5rOleoZA
Workspace: /home/lubko/soring-fronts/curator
Created: 1795230315637; updated: 1795231158934

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fc10b48d001PMHmnmXvezHV7Z)

I'll start by confirming the branch, reading the key docs, and pulling board #301.

## Output 63 (msg_1fc119f15001jHohIgHE9PDN82)

Now let me read the frontier ledger and get a broader board digest.

## Output 91 (msg_1fc11cf4a001u8KmagSnOu384Z)

Now let me study the primary literature evidence — OEIS sequences for exact S(n) values and the Ford–Johnson bound — plus check the repo for data tables.

## Output 114 (msg_1fc12a17e001LxKZDvBI8d7EA0)

Now let me fetch the OEIS sequence tables (exact S, Ford–Johnson FJ, information bound C) to ground the attack.

## Output 150 (msg_1fc1b88c5001QcITtXTbpqbhW3)

The execute tool lacks `require`; I'll use shell + python3 instead.

## Output 179 (msg_1fc1bf3120013GOEj1NjQVR8UQ)

Data verified. Now let me check the ledger/PREVIOUS for duplicate IDs or questions, and build the new frontier-candidates file with length validation.

## Output 190 (msg_1fc1cb732001s9bRTAhgI1d9OD)

Validation passed. Let me view the draft and write the final file.

## Output 219 (msg_1fc1d091e001XUOjO3WzVUGPOq)

Done. The curator output file is written and validated; no Lean, test, or repository changes were made.

## What I studied

AGENTS.md, docs/problem.md, docs/operations.md, docs/literature.md, board #301 digests, the current frontier ledger, and the certified data (OEIS A036604 = exact `S(n)`, A001768 = Ford–Johnson FJ, A003070 = information bound C).

## Attack — claim studied (all-n, about exact unary `S(n)`)

> **Claim: "For every n ≥ 1, S(n) = FJ(n)."** (The Ford–Johnson count equals the exact optimal sorting number for all n.)

Attempts to **disprove** it:
- Certified data (OEIS tables, fetched and parsed by me): S == FJ at n = 1..22; no counterexample in range. Excess e(n) = S(n) − C(n): e = 1 on {12..19, 22}, e = 0 on {2..11, 20, 21}.
- Literature: Manacher 1979 — FJ(n) > S(n) infinitely often (board #301: first at n = 47); Peczarski 2007 — FF "still unbeaten for less than 47 elements"; SW — S(28) ≥ 99.
- A tighter variant, "S(n+1) − S(n) ≤ ⌈log₂(n+1)⌉ − 1 ∀n ≥ 2", is **refuted by certified data**: increment at n = 2 is 2 > 1 (S(3) − S(2) = 2). The variant "≤ ⌈log₂(n+1)⌉" holds through n = 21.

**Honest result:** not refuted in the certified range; the universal claim is expected false in literature (Manacher's infinite failures) but no small falsifier exists because S(23)–S(25) exact values are open (board: n = 23, 24 exact values uncertified). Soundness note: the excess observations are sound data facts; they do not certify any SORT-BOUND-U certificate. Nothing about this establishes any complexity-class result.

## New, unverified frontier proposals (`frontier-candidates.json`)

5 fresh, falsifiable all-n questions, checked for duplicates against the ledger and PREVIOUS fronts:
1. `s24-s25-gap-cert-alln` — is S(24) = C(24) = 80, or a certified adversary forces ≥ 81?
2. `excess-vs-log-bound-alln` — is e(n) ≤ ⌈log₂(n+2)⌉ for all n?
3. `increment-log-upper-alln` — is S(n+1) − S(n) ≤ ⌈log₂(n+1)⌉ for all n?
4. `ff-optimal-window-23-30-alln` — any n ∈ [23,30] with S(n) < FJ(n)?
5. `post22-gap-growth-alln` — bounded excess through n ≥ 23, or a certified infinite ladder of excess growth?

**Honest limits:** no theorem or counterexample was established here; the claims are proposals only (the keeper labels them `ai_proposal_unverified`); I made no repo changes; my attack on FF-optimality found no refutation in certified data.

## Output 240 (msg_1fc1d70790010D44JU0dUrIWnJ)

Recovery audit complete.

**Effects that actually happened:**
- The only durable side effect from the prior turn is the untracked file `frontier-candidates.json` (5 fronts, valid JSON), verified present and unchanged.
- No commits were made (worktree still `## main...origin/main [behind 1]`, only the untracked file).
- No Antonina board posts, no ledger updates, no Lean/repo changes, and no running scratch processes were created.

**Unfinished work:** none. The curator deliverable is complete and validated. I will not repeat or duplicate any external action.
