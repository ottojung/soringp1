# antonina-VCljR8KrFckNklBmwn4QGs-neglect

Session: ses_dfe6b5493ffeBnkQTSqC62m3Ai
Workspace: /home/lubko/soring-fronts/curator
Created: 1795322850164; updated: 1795323576799

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_2019c1a19001WshHrug4j6ldCS)

I'll start by auditing the recovery state before doing anything else: hostname, git state, existing task records, and the key documents.

## Output 24 (msg_2019c2da1001aSq4OkM0i8auMk)

Confirmed on host `billy-dev`; working tree is clean, currently on branch `main` at `f89f6d0`. Let me inspect the existing task record and documents.

## Output 48 (msg_2019c4a15001oLiMKwZNEvxfzM)

Now the board digest, the full frontier ledger, and literature to ground novelty and avoid duplicates.

## Output 76 (msg_2019c78f3001CimxdhlBhgpjkZ)

Let me check the ledger for the previously-"running" front and dump the full front list for duplicate checking, plus read the newest research notes.

## Output 87 (msg_2019c917c001AFMB3RXAYt67O1)

The previous turn's front (`entropy-monotone-optimal-move-alln`) is already marked `investigated` with a finding recorded, and its board post (04:48Z) is live — so nothing to duplicate there. Let me read the newest research notes to ground genuinely novel fronts.

## Output 140 (msg_2019d24a9001BH9j4QzHd6D1uW)

Let me scan the 681 existing front questions for the specific concepts I'm considering, to avoid duplicates.

## Output 227 (msg_2019e8d46001KniwwbYI684JD2)

A genuinely novel angle surfaced: the newest board post (04:48Z, Finding 2) reports **sibling extension inversions** on optimal comparisons for general posets at n=6,7, but the ledger has zero fronts on the *reachable-optimal* version. Let me independently check this before proposing it.

## Output 238 (msg_2019ec294001IhsuzA2vfkPCu3)

Let me independently verify the inversion phenomenon and test the new "extension-monotone optimal move" claim exhaustively for n≤6 using a scratch script.

## Output 256 (msg_2019f2540001smVen2cY5C66kF)

My independent experiment confirms the newest board finding (sibling inversions first appear at n=6, 1440 labelled posets) and shows the *existence* form of the new claim survives exhaustively through n=6 (zero falsifiers) — an honest, non-refuted result. This angle has zero coverage in the 681-front ledger. Let me write the single defensible novel front.

## Output 276 (msg_2019f9d69001VYWzqxF0ke8XBV)

## Recovery audit
- Confirmed host `billy-dev`; working tree clean at `f89f6d0` on `main` before my work.
- **No `frontier-candidates.json` existed** — no prior write to duplicate.
- The previous `"running"` front (`entropy-monotone-optimal-move-alln`) is already `investigated` with its finding recorded in the ledger, and its board post (04:48Z) is live — nothing to repeat.
- I made **no board posts, commits, Lean, or repository changes**; the only file change is the required deliverable.

## What I studied
AGENTS.md, `docs/problem.md`, `docs/operations.md`, the #301 digest, `docs/literature.md`, the newest notes (FO(TC) strategy programs, core/Fibonacci threshold, width-two threshold, realizability window), and all **681** ledger fronts to enforce non-duplication.

## Claim attacked and honest limits
I attacked the all-n claim that every poset with `m(P)≥2` has at least one **extension-monotone** optimal comparison (harder minimax child never has strictly fewer linear extensions than its sibling). This is the corrected, reachable-relevant form of the gloss the newest board post showed false for general posets. I tried hard to falsify it with an independent exhaustive experiment over all 130,023 labelled n=6 posets:

- Sibling inversions **do** appear at n=6 (1,440 states), matching the board — but all off-budget.
- **Zero** falsifiers of the existence form through n≤6; it survives.

This is an *experiment*, not a proof; it covers n≤6 only (n=7 is ≈6.1M classes), yields no complexity-class result, and general-poset inversions have no established bridge to the antichain root without a reachability argument.

## Deliverable
Wrote one genuinely novel, schema-valid front to `/home/lubko/soring-fronts/curator/frontier-candidates.json`:
- `optimal-move-extension-monotonicity-alln` — grounded in the 04:48Z board finding and my independent check; it has zero coverage in the 681-front ledger. I did not claim proof or verification, and I did not inflate the list with near-duplicates of the saturated frontier.
