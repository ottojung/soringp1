# antonina-LkTPu6Ea74XoqxExeVE7z8-present

Session: ses_e08b16f2bffeoPld7uGho3RrtT
Workspace: /home/lubko/soring-fronts/greedy-ball-compact-index-alln
Created: 1795150483861; updated: 1795151108345

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f74e93ef001r3ieiUrYE5QISK)

I'll start by understanding the repository state and reading the key documents. Let me check the current branch and explore in parallel.

## Output 25 (msg_1f74e9fef001Acye9ywpuEtOK2)

I'm on `billy-dev`. Let me read the operations doc, literature, and find board #301 and related research notes.

## Output 44 (msg_1f74ea9fe001lR23ZXSzNcnw30)

Let me get board #301 digest and scan relevant research docs on greedy adversary / compression / obstruction.

## Output 59 (msg_1f74eb9bf001McDL1v8VmuuaDS)

Let me read the full board posts for the greedy fronts, and the key research docs.

## Output 74 (msg_1f74ed424001Led2rmGho1ZAcq)

Let me read the full board post text and the running greedy-adversary-sufficiency front. Let me check the board script options.

## Output 89 (msg_1f74ee286001DPefczVFs8oJsy)

Let me get the full text of the key board posts and check the ledger/candidate definitions of my front.

## Output 109 (msg_1f74f0fa1001K6lpXB0CTYnJUV)

I'll fetch the board JSON to a scratch file (not into context) and extract just the specific posts I need.

## Output 129 (msg_1f74f396d001WlEHrgGJDvzkz7)

Let me check for earlier scratch work from this front and look at the running greedy-adversary-sufficiency front, plus literature on the max-LE adversary.

## Output 144 (msg_1f74fcf79001FujwTyxWrtUul7)

There's substantial earlier scratch — including recent G(12) beam-search work. Let me inspect it to avoid repeating work.

## Output 163 (msg_1f74ff0ab001w2JKzfKMEgYpU9)

Let me read the most recent G(12) computation work — that seems to be the freshest thread.

## Output 200 (msg_1f7502550001qWryvSQbw14AzX)

Let me search the primary literature on the max-linear-extension adversary and whether it achieves the information bound.

## Output 215 (msg_1f7510484001xs3j78izkOW7iX)

Web search is unavailable in this environment (consistent with earlier notes). Let me try direct fetch of a known reference and run the local small-n checks in parallel.

## Output 230 (msg_1f7514ed8001tbQCYB1A2hOFMP)

Literature confirms the max-LE adversary is exactly the information-bound adversary (Kahn–Saks / Fredman). Now let me test a stronger empirical claim: does the greedy game value equal `ceil(log2 e(P))` on **every** poset, not just the antichain?

## Output 241 (msg_1f751efc4001Q9bw230xx5WAlK)

A key structural fact emerged: some posets have `V(P) = ceil(log2 e(P)) + 1`. Let me check whether such excess states are actually **reachable** at budget G(n), and examine the matching-gadget isomorphism claim computationally.

## Output 252 (msg_1f75249ca0015acm1QsZFMGdj6)

Let me verify computationally that the matching-gadget tied states are pairwise isomorphic and share one game value, and count isomorphism classes in the reachable ball.

## Output 272 (msg_1f752ae36001vxpUHmLwGSIDEd)

The gadget collapses to `⌊n/2⌋+1` isomorphism/value classes as predicted. Let me test a stronger compression hypothesis: on the reachable ball, is `V(P)` a function of `e(P)` alone?

## Output 283 (msg_1f7532580001qquPfBptXA6fFt)

Let me test whether any extension-count **tie** between non-isomorphic children yields different game values — the essential ingredient a falsifier would need.

## Output 294 (msg_1f753b74b001peBisxIDKWBedH)

Ties with differing values exist but are local (2 children), not an independent exponential family. Let me count isomorphism classes in the reachable ball — this tests whether a subexponential symbolic evaluator is plausible.

## Output 305 (msg_1f754315c001YVSFB4xCqLo6vg)

Let me verify the gadget value formula `V = C(n) − t` including odd n, then finalize.

## Output 325 (msg_1f756a8ed0015Qamq8bne6sdZT)

Confirmed: gadget states evaluate as `V = C(n) − t`. Now let me check the posting CLI syntax and then write the finding to board #301.

## Output 343 (msg_1f756f45e001bvfx2yGEximFvC)

I have a rigorous finding. Let me confirm the worktree is clean and compose the board post.

## Output 368 (msg_1f757788a001397N2it3mFAPWB)

Let me verify the post landed correctly on board #301.

## Output 379 (msg_1f7578bf1001qd2FdQ8gOihRaZ)

Done. Here is my report.

## Finding (positive, rigorous — refutes the proposed falsifier at its source)

I attacked the FRONT's **negative horn**: *every correct compact-index evaluator of `G(n)` must separate `2^{Ω(n)}` extension-count-tied greedy states*, with the isolated-pair matching gadget (`2^{⌊n/2⌋}` tied states) as the concrete witness. That horn is **false at its stated source**.

**Lemma L1 (symmetry, paper proof).** The greedy game is `Sₙ`-equivariant: `e(πP)=e(P)`, incomparable pairs map to incomparable pairs, and the heavy child of `(πx,πy)` is `π·(heavy child of (x,y))`. By induction on the game value, `V(πP)=V(P)`. So ties between *twin* elements (isolated 2-antichains) yield isomorphic, value-equal children — distinguishing those ties is unnecessary.

**Lemma L2 (gadget collapse, paper proof).** The `2ᵐ` gadget states `P_T` (`m=⌊n/2⌋`) occupy exactly `m+1` isomorphism classes and `m+1` value classes, indexed only by `t=|T|`. Hence an **O(n)-entry index keyed by `t`** evaluates `V` on all of them; each isolated-pair tie carries zero information beyond `t`. [experiment] verified `V=C(n)−t` for `2≤n≤6` (odd n included). So these tied states cannot force exponential separation.

## Sharper structural picture (experiment, independent scratch)

- The **full ball does not collapse by relabeling** (n=6: 114953 iso classes vs 119118 labelled states) — so I explicitly do *not* claim a labelling-artifact dissolution of the whole ball.
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

## Output 400 (msg_1f757e4e9001paMqs54hC8Lxsq)

**Recovery inspection (billy-dev, no actions repeated):**
- **Git:** clean, `HEAD 6a96398` unchanged; no commits/branches/PRs.
- **Durable external effect:** exactly one board post exists for this front — `SoringP1 frontier: greedy-ball-compact-index-alln` on #301 at `2026-11-20T05:04:20Z` (verified via board digest, page 1). I did **not** repost.
- **Local artifacts (scratch only):** `/tmp/opencode/gbci/post_body.md`, `post_result.json` (exit 0, empty stderr) and earlier scratch scripts/logs; no repository files modified.

**Status:** the interrupted turn’s work is complete; there is no unfinished work to continue.

**Result already reported (unchanged):**
- **Claim attacked:** the negative horn — every correct compact-index evaluator of `G(n)` must separate `2^{Ω(n)}` extension-count-tied greedy states — with the isolated-pair matching gadget as its concrete source.
- **Finding (paper proof):** that horn is **false at that source**. `Sₙ`-equivariance of the greedy/max-LE game implies `V(πP)=V(P)`; the `2^{⌊n/2⌋}` gadget states collapse to `⌊n/2⌋+1` isomorphism/value classes indexed by `t=|T|`, so an `O(n)` index keyed by `t` evaluates all of them and the gadget forces no exponential separation. [experiment] `V=C(n)−t` verified for `2≤n≤6` (odd n included).
- **Sharper picture / limits (honest):** the **full** ball does not collapse by relabeling (n=6: 114,953 iso classes vs 119,118 labelled), while value compression is nearly `V≈f(e(P))` (62 distinct `e` values, 8 excess exceptions at n=6; non-twin ties with differing child values exist but are local). No poly-size subexponential evaluator exhibited (positive horn open); `G(n)=C(n)` / `G(n)=S(n)` not settled (n≤6 only); no non-symmetric exponential tied family excluded; no general-poset transfer, no certificate soundness/completeness claim, no class separation for `SORT-BOUND-U`. No Lean/repo/CI/main changes.
