# greedy-ball-compact-index-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

LkTPu6Ea74XoqxExeVE7z8-present

## exit_state

clearexit

## question

For every n, does the greedy (maximum-linear-extension) adversary reachable ball at budget G(n), whose explicit size is at least 2^{floor(n/2)}, admit a polynomial-size index (for example the subset of isolated-pair resolutions from the matching-gadget witness) on which a uniform algorithm evaluates G(n) exactly in time 2^{o(S(n) log n)}, or must every compact-index evaluator distinguish 2^{Omega(n)} distinct extension-count-tied states?

## basis

Board #301 greedy-frontier-state-growth-alln (Executive-verified 2^{floor(n/2)} ball from isolated-pair extension ties; counts 2,11,143,3362,119118 for n<=6) and the running greedy-adversary-sufficiency-alln; my scratch re-derived the tie. No ledger front studies implicit or compact-index evaluation of G(n).

## falsifier

Give a counting or pigeonhole argument at the antichain root showing that every correct compact-index or symbolic evaluator of G(n) must separate 2^{Omega(n)} tied greedy states for infinitely many n; this would be an enumeration obstruction at the fixed root, not a general-poset NP-hardness transfer.

## implication

A subexponential exact evaluator for G(n) would sharpen greedy lower-bound and certificate methods and, conditional on G(n)=S(n), improve the 2^{O(n log^2 n)} exact S(n) bound; a negative result would show the exponential ball is not merely an artifact of explicit enumeration.

## finding_unverified

asses vs 119118 labelled states) — so I explicitly do *not* claim a labelling-artifact dissolution of the whole ball.
- Compression is in the **value dimension**: on `R_{G(n)}(n)`, `V` is almost a function of `e(P)` (2,4,9,23,62 distinct e-values for n=2..6; 8/62 exceptions at n=6, all "excess" states `V=⌈log₂ e⌉+1`). Non-twin ties with differing child values exist (1336/90655 at n=6) but are **local** (two children), not independent exponential families.

## Honest limits (explicitly reported)

- No poly-size-index subexponential evaluator is exhibited — the **positive horn remains open**.
- `G(n)=C(n)` and `G(n)=S(n)` for all n are **not settled** (confirmed only n≤6); the conditional improvement to the `2^{O(n log² n)}` exact-`S(n)` bound is therefore not obtained.
- The refutation is scoped to the matching-gadget source; a different non-symmetric tied family is not excluded.
- I make **no general-poset hardness transfer** and **no certificate claim**: the Fredman/`1/3–2/3`/Kahn–Saks results concern *sorting a given poset* (algorithms), not evaluating `G(n)`, and certificate soundness vs completeness is not addressed here. No class separation for `SORT-BOUND-U`.

## Delivery

- Posted as the sole external write to board **#301** at `2026-11-20T05:04:20Z` (verified present).
- **Worktree clean at `6a96398`; no repo, Lean, test, CI, ledger, or main changes.** Earlier inconclusive G(12) scratch was inspected but not reused or built upon.
- Net: a concrete failed approach (the gadget-based separation obstruction) plus an all-n symmetry theorem — not a proof of the central theorem.
**Recovery inspection (billy-dev, no actions repeated):**
- **Git:** clean, `HEAD 6a96398` unchanged; no commits/branches/PRs.
- **Durable external effect:** exactly one board post exists for this front — `SoringP1 frontier: greedy-ball-compact-index-alln` on #301 at `2026-11-20T05:04:20Z` (verified via board digest, page 1). I did **not** repost.
- **Local artifacts (scratch only):** `/tmp/opencode/gbci/post_body.md`, `post_result.json` (exit 0, empty stderr) and earlier scratch scripts/logs; no repository files modified.

**Status:** the interrupted turn’s work is complete; there is no unfinished work to continue.

**Result already reported (unchanged):**
- **Claim attacked:** the negative horn — every correct compact-index evaluator of `G(n)` must separate `2^{Ω(n)}` extension-count-tied greedy states — with the isolated-pair matching gadget as its concrete source.
- **Finding (paper proof):** that horn is **false at that source**. `Sₙ`-equivariance of the greedy/max-LE game implies `V(πP)=V(P)`; the `2^{⌊n/2⌋}` gadget states collapse to `⌊n/2⌋+1` isomorphism/value classes indexed by `t=|T|`, so an `O(n)` index keyed by `t` evaluates all of them and the gadget forces no exponential separation. [experiment] `V=C(n)−t` verified for `2≤n≤6` (odd n included).
- **Sharper picture / limits (honest):** the **full** ball does not collapse by relabeling (n=6: 114,953 iso classes vs 119,118 labelled), while value compression is nearly `V≈f(e(P))` (62 distinct `e` values, 8 excess exceptions at n=6; non-twin ties with differing child values exist but are local). No poly-size subexponential evaluator exhibited (positive horn open); `G(n)=C(n)` / `G(n)=S(n)` not settled (n≤6 only); no non-symmetric exponential tied family excluded; no general-poset transfer, no certificate soundness/completeness claim, no class separation for `SORT-BOUND-U`. No Lean/repo/CI/main changes.

## Other metadata

```json
{
  "finished_at": 1795151113.8075454,
  "started_at": 1795150483.1414948
}
```
