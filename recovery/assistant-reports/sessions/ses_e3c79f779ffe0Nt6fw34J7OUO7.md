# antonina-5DcbL6YJBe6EH0JQCsqsm5-humane

Session: ses_e3c79f779ffe0Nt6fw34J7OUO7
Workspace: /home/lubko/soring-fronts/cover-destruction-induction-barrier
Created: 1794281703752; updated: 1794285788114

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1c3860c07001deUASR29kp5nvx)

I'll start by studying the repository context: AGENTS.md, problem.md, operations.md, and the current board #301.

## Output 25 (msg_1c38621bc001TbGSq7geho2scd)

Now let me look at the board #301, the literature, and any existing work on the cover-destruction front.

## Output 44 (msg_1c3863e150010LRdKgpRsZOjy5)

Let me read the full 02:20Z post and the repo docs, and understand the front's definitions.

## Output 154 (msg_1c387d920001at5oW6vVVCbpha)

Let me search the board and the ledger/curator for the exact evidence claim and definitions.

## Output 212 (msg_1c38ce9ce001Qls4yoqM7P9jVL)

The post's GC verification code isn't saved. Let me independently check the key condition with my own implementation.

## Output 232 (msg_1c38d8aa1001fbmdG5u3Ko7QEA)

My first checker used too strong a condition. Let me correct it to the exact induction condition and the post's literal GC, and check nauty availability for larger n.

## Output 282 (msg_1c390a06a001B2X2V24cIfBrqb)

`genposetg` works. Let me write a parser and an independent exhaustive checker for the exact induction condition.

## Output 347 (msg_1c3944a10001zeZS7Z0zvWIdoV)

The exact induction condition fails much earlier than n=6,7. Let me pin down what "exact D-balanced condition" the front means and find the curator's computation.

## Output 362 (msg_1c3970fa2001BmLsMDACkp8uxv)

The key question is whether a larger constant C′ with the same potential D can close the induction universally. Let me compute the valid C′ intervals per poset.

## Output 409 (msg_1c3998a62001r3KADeVEDAH545)

A concrete n=5 poset has no valid C′ at all with potential D. Let me examine it and the exact condition variants.

## Output 420 (msg_1c399f3a3001D5IgTReiZd2lVD)

I found a corrected potential that restores the induction. Let me verify it and check the literature/docs for prior art.

## Output 448 (msg_1c39d1a2f001wFzgOgDNlhNNIs)

Let me extract the height-two exact-condition failures and verify the corrected potential theorem computationally.

## Output 468 (msg_1c39e0627001KKg4MwtHGaeYI6)

I found a much simpler corrected potential: the number of incomparable pairs. Let me verify the theorem and search for prior art.

## Output 553 (msg_1c3a3134e0013Scsj9KLAFLyQf)

Let me compute the post's literal GC condition (D_i ≤ D or p_i < threshold) and find its first failures.

## Output 890 (msg_1c3b991fe001VIdrUuzdW2J1Pn)

I need to stop the unproductive search loop and consolidate. Let me verify the key computational claims once more and then write the report.

## Output 919 (msg_1c3bc8e27001xtSMCApy8KTHWe)

I'm going to stop the search loop and consolidate. Let me do one final check on the literature in the repo and then write the report.

## Output 952 (msg_1c3be5d27001NetuQrzZzG5EnB)

I need to break out of this loop. Let me write the report based on the verified mathematics.

## Output 963 (msg_1c3bf6016001dQAl5CvgTScFo2)

I have the verified mathematics. Let me post a concise, honest update to board #301.

## Output 1032 (msg_1c3c1e9280010VOVGijsHNoFYN)

I've completed the investigation and posted the finding to board #301. Here is the summary.

## Mathematical finding

**The exact D-balanced condition fails from n=3, not n=6,7.** For the potential `D = covers + psi` and `C = (5 − log₂15)/8`, the induction step for `(U)` needs, for the chosen incomparable pair and both orientations,

`1 + log₂ pᵢ + C(Dᵢ − D) ≤ 0`, where `pᵢ = eᵢ/e`.

Exhaustive computation over all non-total unlabeled posets (nauty `genposetg`, independent parser) gives failures at n=3: **1**, n=4: **2**, n=5: **10**, n=6: **56**, n=7: **324**, n=8: **2236**. The first failure is the 2-chain plus isolate `(0,0,1)`. The curator's "n=6,7" premise is imprecise.

**Concrete obstruction at n=5.** The poset `P = (16,16,17,23,0)` has `e=3`, `covers=5`, `m=M=1`, `psi=0`, `D=5`, `ip=2`, `F=2`. Its two incomparable pairs split extensions `(1,2)`, so `p=(1/3,2/3)`. The majority branch creates one cover, destroys none, and preserves `m=M=1`, so `Dᵢ = D`. The condition becomes `1 + log₂(2/3) = 0.4150 > 0` for **every** `C′ ≥ 0`. No constant rescues the cover-destruction induction with potential `D` at this poset.

**Corrected potential.** `D′(P) = ip(P)` (number of incomparable pairs) with `C′ = 1` restores the induction for all finite posets:

`F(P) ≤ log₂ e(P) + ip(P)`.

Adding a relation makes its pair comparable and creates no new incomparable pair, so `ipᵢ ≤ ip − 1` (verified for all 250,665 pairs up to n=8). Then `F ≤ 1 + max(log₂ eᵢ + ipᵢ) ≤ 1 + log₂ M + (ip−1) = log₂ e + log₂ p + ip ≤ log₂ e + ip`, since `p = M/e ≤ 1`. This satisfies the falsifier's first disjunct.

## Why this does not revive (U)

`(U)` is `alpha ≤ C(covers+psi)`. At the antichain, `covers+psi = 2n` but `ip = C(n,2)`, so the corrected potential gives `alpha ≤ n(n−1)/2`, vastly weaker than `(U)`'s `0.273n`. Against Fredman's known `F ≤ log₂ e + 2n` (recorded in `docs/research-hardness-boundaries.md`), the corrected bound is stronger only when `ip < 2n`. So the route to `(U)` is **not** restored; only a weak general excess inequality is obtained.

## Honest limits

- The corrected-potential theorem is a short elementary induction and the inequality is weak; it may be folklore and does not imply `(U)`.
- The exact-condition failures are exact computations up to n=8, not an all-n proof.
- The n=5 obstruction kills the specific potential `D = covers+psi`, not every potential.
- This is a structural minimax statement about general finite posets. It does not change `S(n)` or `SORT-BOUND-U` bounds, and it is not a certificate soundness/completeness result.

**External effects:** one board comment posted to #301 at `2026-11-10T04:39:58Z` under `SoringP1 frontier: cover-destruction-induction-barrier` (verified unique). Worktree clean at `6a96398`; no repo, Lean, or ledger changes.

## Output 1106 (msg_1c3c429320018q6hIeBwfqKaV6)

**Recovery inspection (no actions taken, no side effects repeated)**

- **Repo state:** `/home/lubko/soring-fronts/cover-destruction-induction-barrier` on `billy-dev`, clean working tree at `6a96398` (`billy-dev...origin/billy-dev`), no local diff and no untracked files.
- **Durable scratch/artifacts present:** `/tmp/opencode/cdcheck/` contains `post.md`, `report.md`, `post_result.json`, and analysis scripts (`exact.py`, `gc.py`, `cinterval2.py`, `h2fails.py`, `posets.py`, etc.). `post.md` matches the completed `cover-destruction-induction-barrier` finding (exact D-balanced condition fails from n=3; `D=covers+psi` blocked at n=5 for all `C'` by `P=(16,16,17,23,0)`; corrected potential `D'=ip, C'=1` gives `F(P) <= log2 e(P)+ip(P)` but does not revive `(U)`).
- **External side effects (based on durable records):** The board post to #301 for `cover-destruction-induction-barrier` appears to have already been recorded (summary/checkpoint states `2026-11-10T04:39:58Z`, verified unique; `post.md`/`post_result.json` exist locally). I did **not** re-post or verify against the live board API from this environment, so if absolute certainty is required that should be confirmed on Antonina/board side—but I am not duplicating the post.
- **Commits/PRs/purchases/Lean/repo changes:** none detected; nothing to commit or publish.

**Status:** front appears complete and reported; **no unfinished work identified** in this checkout from available records. Per the checkpoint, the only natural continuation would be a new investigation (e.g. whether any stronger corrected potential can recover `(U)`), but that would be a separate front/question, not continuation of an interrupted side effect. I have not started any new work.
