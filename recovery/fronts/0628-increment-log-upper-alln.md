# increment-log-upper-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

pJXFTGmCVaFugQYaaEIDy9-pulses

## exit_state

clearexit

## question

Prove or refute: for every n >= 2, S(n+1) - S(n) <= ceil(log2(n+1)), so increments in the exact optimal count stay bounded by the information growth of one new key.

## basis

Certified increments through 22 all <= ceil(log2(n+1)); S(3) - S(2) = 2 = ceil(log2 3); S(22) = 71; tightening the bound by one is refuted by certified data at n = 2 (increment 2 > 1).

## falsifier

A certified n with S(n+1) - S(n) > ceil(log2(n+1)), via a certified depth of n+1 beyond S(n) + ceil(log2(n+1)).

## implication

A stable increment bound constrains DP recurrences and certificate arithmetic for the exact evaluation of S(n).

## finding_unverified

 (`2 > 1`) — as you noted, so the claim itself cannot be tightened; but it holds as stated.

## Certificate soundness vs completeness

A falsifier per the front would be "a certified `n` with `S(n+1) − S(n) > ⌈log2(n+1)⌉`, via a certified depth of `n+1` beyond `S(n) + ⌈log2(n+1)⌉`" — i.e. a tree of height `> S(n) + ⌈log2(n+1)⌉` sorting `n+1` keys. The proof above rules this out for all `n`, so no such certificate can exist: **completeness of the negation fails, and certificate soundness is moot** (the claim is true). General-poset bounds (e.g. `S(n) = m(A_n)`, `S_eq_adv_univ` per `docs/problem.md`/`docs/research-n12-nontightness.md`) are a different object — per the fidelity rules I did not transfer them to this claim; the proof above uses only `docs/problem.md` definitions.

## Honest limits

- Proof relies on standard adaptive-tree definitions; brute force verified the insertion bound to `n = 500`.
- Certified data extends through `n = 22` (`S(23)` is open, Stober–Weiss).
- No broader literature search completed (web tool unavailable here; repo `docs/literature.md`/OEIS don't state this theorem).
- No repo/Lean changes, per your constraint.

**Board #301:** finding posted at `2026-11-21T03:27:25Z` ("Front increment-log-upper-alln — result … PROVED true"); ledger status for front `increment-log-upper-alln` remains `running`.

**Bottom line:** I could not refute the claim — it is provably true via the optimal-tree-plus-binary-search insertion argument, and all certified increments through `n = 21` (and `S(22)=71`) are consistent with it.
Inspection complete. Here's the state I verified, and what I will / won't repeat.

## What actually happened (verified, not re-executed)

- **Board #301 comment** — confirmed landed: a single comment by `SoringP1 researcher: increment-log-upper-alln` at `2026-11-21T03:27:25.317Z` ("Front increment-log-upper-alln — result … PROVED true"). Digest shows exactly **one** match. I will **not** re-post.
- **Git state** — clean working tree, no staged or unstaged changes, no new commits. HEAD remains `6a96398` (unchanged from before the investigation). No repository files were modified or created.
- **Frontier ledger** — `increment-log-upper-alln` still shows `status: "running"` with the original agent id; I did not edit it. The board comment is the durable report of the result.
- **Scratch artifacts** — only `/tmp/opencode/board301-post.json` (the antonina output redirect required by ops doc), which is outside the repo and harmless.

## Unfinished work

None that I can safely act on. The investigation is complete and its result is recorded on the board. The one operational item I'm leaving untouched is the ledger status transition (`running` → `investigated`), which the keeper/agent-pool machinery owns — I won't edit it to avoid duplicating or racing the keeper's own state writes. If you want it advanced now, that's a review-level decision (the ledger lives at `~/.local/state/soringp1/frontier-ledger.json`).

## Outcome already reported (for the record)

The claim **S(n+1) − S(n) ≤ ⌈log2(n+1)⌉ for n ≥ 2 is PROVED TRUE** via optimal-tree-plus-binary-search insertion; no falsifier exists (the strengthened "−1" variant is refuted at n=2 by certified data); all certified increments through n=21 (S(22)=71) are consistent; limits: proof is elementary, data through n=22, no wider literature search possible in this environment. Full argument and limits are in the board #301 comment above — I'm not duplicating it here.

## Other metadata

```json
{
  "finished_at": 1795231730.3155065,
  "started_at": 1795231174.1805758
}
```
