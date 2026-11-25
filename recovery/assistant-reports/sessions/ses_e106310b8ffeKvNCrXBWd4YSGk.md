# antonina-DBAk6l46T8yhD4T4vWoyU0-pouring

Session: ses_e106310b8ffeKvNCrXBWd4YSGk
Workspace: /home/lubko/soring-fronts/curator
Created: 1795021401934; updated: 1795022598988

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 20 (msg_1efabd03a001WBnOF8aUTR4JTD)

I'll start by inspecting the environment carefully, as required by the recovery notices — checking git state, working directory, existing files, and durable task records before doing anything.

## Output 35 (msg_1efabe8af001800NPK2gXi3nF4)

We're on `main`, but the task says "On billy-dev ONLY". Let me check branch availability and locate the key files and task records.

## Output 50 (msg_1efabf651001vuzZK72s35Rv5m)

We're on `main`; no local `billy-dev` branch here. The scripts reference a separate repo at `/home/lubko/soring301`. Let me map the layout and read the governing docs and curator script.

## Output 65 (msg_1efac0c0f001nIGv8zjUolwuqv)

This is the curator agent flow. The research repo `/home/lubko/soring301` is on branch `billy-dev` (HEAD `6a96398`); my only deliverable is the JSON file. Let me read the governing docs and the board digest.

## Output 88 (msg_1efac3085001PQ9aPkBV3HGYoY)

Now let me check the board digest tool and the ledger state, then pull the newest #301 posts.

## Output 103 (msg_1efac4875001iKnvu6nWroB51f)

Let me pull the newest #301 board posts (read-only digest), saving to files to avoid flooding context.

## Output 121 (msg_1efac6e0c001h9V3j7gois0dgT)

Let me check the current research plan and look for explicitly noted open/next steps that haven't become fronts, plus a couple of structural docs.

## Output 136 (msg_1efad14380013a72Ge6x3zrjol)

Let me read the repo's own "next unresolved obstacle" sections — these may reveal directions not yet turned into fronts.

## Output 159 (msg_1efad2a20001vy0sFCxxeWBdYz)

The repo's "next obstacle" notes have mostly become fronts already. The freshest, least-mined evidence is the new framed-DAG join result. Let me pull those two board posts in fuller detail to ground (and de-duplicate) any proposal.

## Output 177 (msg_1efad9cf70012nfDYMgj2DN1WN)

The merge post explicitly leaves "recognizing F-redundancy without computing F" open — a genuinely new, sharp question. Let me scan a few other fresh exec reports for additional un-mined open sub-questions.

## Output 195 (msg_1efadeeb30013h22fKL6kike0M)

I now have enough grounding. The newest #301 merge report explicitly leaves "recognizing F-redundancy without computing F" open, and the repo cautions that general-poset results don't automatically transfer to the antichain root. These yield two genuinely new, all‑n falsifiable fronts not in the PREVIOUS list. Let me verify there's no existing candidates file, then write only the JSON deliverable.

## Output 215 (msg_1efaed77d001xyy1NWRx735ukI)

Let me validate the file against the keeper's exact schema rules and check for id/fingerprint collisions with already-investigated fronts.

## Output 226 (msg_1efaef330001DunwCeojKL1A6D)

Let me check collisions against the entire 534-front ledger (the keeper deduplicates IDs and question fingerprints).

## Output 237 (msg_1efaf13a2001oIMZK8h7vSoLSr)

Done. Here's a concise report.

## What I did (recovery-aware)
- Inspected state first: `curator` worktree clean on `main` at `6a96398`; the actual research repo `/home/lubko/soring301` is on branch **`billy-dev`** at `6a96398`, so the "billy-dev ONLY" constraint is satisfied.
- `frontier-candidates.json` did **not** exist (fresh curation), and the ledger shows this agent (`DBAk…pouring`) as the active curator — no prior curation side effects to duplicate.
- Took **no external actions**: no board posts, commits, purchases, Lean, or repository changes. Only the deliverable file is new/untracked.

## Deliverable
`frontier-candidates.json` contains only `{"fronts": [...]}` with 2 new fronts, both passing the keeper's exact schema (id + all four length minima) and with **no id or question-fingerprint collision** against the 534-front ledger or the PREVIOUS 20:

1. **`framed-merge-fredundancy-recognition`** — Is the F-redundancy predicate `F(meet+e)=F(meet)` (the reported criterion for lossless optimal merges) decidable in poly time for all n *without* evaluating F? Directly grounded in the newest #301 report (`framed-dag-canonical-merge`, 2026-11-18), which explicitly leaves this open. Falsifiers: an evaluation-free recognizer, or a reduction showing it is as hard as computing S(n).

2. **`intersection-join-losslessness-general-posets`** — Does that losslessness characterization hold for all finite n-element posets, or only for antichain-reachable states? Honors the prompt's "distinguish general-poset results" requirement; the falsifier must also check the antichain case to preserve the bridge back to S(n).

## Honest limits
I rejected several tempting directions as duplicates of already-investigated fronts (framed-DAG polynomial completeness / join compression / common-skeleton collapse, Sergeev effective bounds and group-insertion grammars, FJ-tightness, time-exponent, space bounds, FO(PFP/TC), certificates, etc.). Both proposals are **unverified hypotheses**, not results; no proof, disproof, or kernel check is claimed. Given the near-saturation of the frontier, I deliberately output a small, high-confidence set rather than padded fronts.
