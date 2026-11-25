# antonina-I13dKKLEnPt1CbKZHvaSP0-annular

Session: ses_e3b41766effex4Zct0DzgL3eJD
Workspace: /home/lubko/soring-fronts/curator
Created: 1794302183852; updated: 1794304631463

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1c4be89f9001IfAIsk30k5MSDA)

I'll start by exploring the repository structure and reading the key documents.

## Output 806 (msg_1c4e18752001EQj52cwFp0shXQ)

I've completed a substantial independent check. Let me verify my n=10 deck computation once more and then write the candidate fronts.

## Output 835 (msg_1c4e347f30010cN4sDx4cVfMYV)

I've completed the curator task. Here is my report.

## What I studied

- `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, `docs/operations.md`, `docs/research-plan.md`, and the surrounding research docs.
- The full Antonina board #301 (500 messages over 10 pages, 2026-11-06 through 2026-11-10), including the newest posts and Executive/referee checks.
- The durable ledger (`~/.local/state/soringp1/frontier-ledger.json`, 497 fronts) to check for duplicates.

## Independent mathematical check performed

The newest board post `height-two-exact-child-count-deck-completeness` (2026-11-10T01:20Z) claims a strengthening — the exact child-count deck is a complete invariant for height-two posets up to isomorphism/duality — and states it is verified only through n=9. I tried to disprove it at n=10.

I built an independent enumerator using `genposetg` and a from-scratch C implementation of the deck (exact extension counts by subset DP, no board code reused). Results:

| n | height-2 classes | deck fibers of size ≥2 | non-dual fibers |
|---|---|---|---|
| 9 | 2,223 | 1,078 | 0 |
| 10 | 10,766 | 5,181 | 0 |

The n=9 run reproduces the board post's published counts exactly, validating the code. At n=10 every deck fiber of size ≥2 is a dual pair, so the strengthening survived a serious falsification attempt. This is finite evidence, not a proof.

## Fronts proposed

Wrote `/home/lubko/soring-fronts/curator/frontier-candidates.json` with three fronts:

1. `height-two-deck-complete-invariant` — the deck completeness strengthening, now with independent n=10 evidence.
2. `height-two-prime-excess-boundedness` — the height-2 prime excess question explicitly left open by the newest `prime-excess-unboundedness` post.
3. `adversary-optimal-state-minimum-growth` — the exact minimal-state growth question explicitly left open by the newest `conp-adversary-memory` post, directly bearing on coNP certificates for `SORT-BOUND-U`.

All three are all-n falsifiable, grounded in the newest board, and checked against the 497-front ledger for exact duplication.

## Honest limits

- The deck result is exhaustive only through n=10; a counterexample at n≥11 would falsify the front. No all-n proof is claimed.
- The height-2 prime excess question is open; the single-deletion subclass is known to be unbounded iff `E(n)` is unbounded, so a general bound is likely hard.
- The adversary-memory front is a follow-up to an active board investigation and is adjacent to existing adversary-certificate fronts (`adversary-strategy-certificate-conp`, `cofn-adversary-certificate-size`); it may be challenged as redundant even though its exact-minimal-state formulation is distinct.
- No Lean files, commits, or other repository changes were made. The only repository artifact is `frontier-candidates.json`; all scratch work is under `/tmp/opencode/curator301`.
