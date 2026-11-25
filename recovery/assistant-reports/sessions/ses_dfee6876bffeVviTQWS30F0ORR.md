# antonina-1Om0VcKkbB77vLHB4U7V3F-chest

Session: ses_dfee6876bffeVviTQWS30F0ORR
Workspace: /home/lubko/soring-fronts/near-antichain-excess-gadget-size
Created: 1795314776331; updated: 1795321020993

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 565 (msg_20158c600001VCXx8pgPLT9Mm9)

Let me assess the current state. The `highm7.py` process appears to have been killed (infrastructure failure) and produced no output. Let me check git state, existing scripts, and confirmed values before continuing the unfinished computation.


## Output 594 (msg_20159da3c001QkGJcSDWTOlLZo)

Confirmed S(5)=7, S(6)=10. So for g(6): need a 7-element poset with e≤720 and m≥11; and m(P)≤S(|P|)≤10 for |P|≤6, so g(6)>6 automatically. Now I'll write an efficient exhaustive n=7 search: enumerate all posets (no expensive e-computation yet), compute m bottom-up, then check e only for posets with m≥11.


## Output 684 (msg_20161e605001fniNvaDVlIE4WE)

The `g6_search.py` process was killed by the infrastructure failure at 5M enumeration, and there's an unrelated parallel front process (`w7_phase1.py`, about winning-count peaks) which I must not interfere with. My computation left no side effects. Let me rewrite the search with checkpointing so it can survive another interruption, using a `succ_of` dict to speed the hot loop.

## Output 776 (msg_20170067e001ftE2Xrk7Eb7smo)

The search completed but returned `hard=0`, which is suspicious — the 7-element antichain should have m=S(7)=13≥11. Let me verify the minimax computation; there may be a bug in my bottom-up DP.

## Output 787 (msg_2017036180013qqILejmpV1dYj)

Found the bug: I computed `min over all children` instead of `min over pairs of max(two outcomes)`. S(7) came out as 6 instead of 13. Let me fix the minimax recurrence and rerun (enumeration checkpoint is saved, so I skip re-enumeration).

## Output 832 (msg_201758223001y5TnGJwqWf3Yxw)

Now the corrected result: S(7)=13 ✓, and the minimum e among 7-element posets with m≥11 is **840 > 720**. Let me independently cross-check this with a separate top-down minimax and brute-force e-count, and validate the framework on the known g(5)=6 witness.

## Output 843 (msg_20176b360001h0MX1iQQ1iz67X)

Cross-checks pass: independent brute-force e-count and independent top-down minimax both confirm min e=840 for m≥11 on 7 elements (e.g. relations 0<2,0<3,1<2,1<3 plus 3 free elements → e=840, m=11). Let me validate the same framework reproduces the known g(5)=6 result.

## Output 854 (msg_20177035f001v2N25V8Nh5Cxlk)

The framework is validated: it reproduces g(5)=6 (min e=120 among 6-element posets with m≥8). The n=6 result is solid. Before deciding on any external side effect (board post), let me check whether this front already has a posted result, to avoid duplication.

## Output 899 (msg_20177b776001FBIkVp042Sq0RT)

My front (`near-antichain-excess-gadget-size`, id 675) is status `running` with no posted finding, and board searches confirm no prior result post — so there's nothing to duplicate. Let me find the board posting mechanism (operations.md mandates reporting findings to #301).

## Output 951 (msg_2017899a6001fAMUSr3DOBfx5d)

Done. Here is my honest completion report.

## Side-effect audit (done first)
The two earlier interrupted runs (`highm7.py`, `g6_search.py`) were killed by the backend failure with **no output and no side effects**. Worktree is clean at `6a96398` on `billy-dev`; front 675 was `running` with no finding, and board searches for this front returned zero matches — so nothing was duplicated. My only external write is one verified #301 post.

## Mathematical finding — the all‑n claim is FALSIFIED at n=6

Claim attacked: `g(n)` = minimum elements of a poset `P` with `e(P) ≤ n!` and `m(P) > S(n)`; is `g(n)=n+1` for all `n≥5`? (Given: `g(5)=6`.)

- `S(6)=10`, so we need `e(P) ≤ 720` and `m(P) ≥ 11`.
- **`g(6) > 6` for free:** `m(P) ≤ S(|P|)` (sorting from scratch is always a valid strategy), so any poset on ≤6 elements has `m ≤ S(6)=10 < 11`.
- **Exhaustive n=7 search:** all 6,129,859 labelled 7‑element posets (matches OEIS A001035), with the correct recurrence `m(P)=1+min_pairs max(child₁,child₂)`, were checked. Sanity `m(antichain)=S(7)=13` ✓. Exactly 2213 posets have `m≥11`, and the **minimum `e` among them is 840 > 720**. Hence no 7‑element poset satisfies `e ≤ 720, m ≥ 11`.

**Therefore `g(6) ≥ 8 ≠ 7 = n+1` — the pattern fails at n=6.** (Exact `g(6)` not computed.)

## Independent cross-checks
- Brute permutation e‑count and a separate top‑down memoized minimax reproduce `e=840, m=11`; witness `succ=(12,12,0,0,0,0,0)` = relations `{0<2,0<3,1<2,1<3}` + 3 free elements.
- The same pipeline reproduces the known `g(5)=6` (min `e=120` among 6‑element posets with `m≥8`).
- **Failed approach caught:** my first bottom‑up DP used `min over all children` instead of `min over pairs of max(children)` and wrongly gave `S(7)=6`; the `S(7)=13` sanity check exposed it and it was fixed before any result was trusted.

## Complexity implication and honest limits
The stated implication ("must examine n+1‑element posets") does **not** hold at n=6 — the first `m>S(6)` poset with `e≤720` needs ≥8 elements. This is a **finite falsification of a structural regularity**, not a complexity‑class result or a new bound/algorithm for `S(n)`; no P/NP consequence follows. These are **general posets**, not states reachable from the antichain root, so this is a gadget‑size fact — certificate soundness (`e≤n!`, exact `m>S(n)`) is fine, but it yields no antichain‑root lower bound and no completeness claim. Exhaustion stops at 7 elements; 8‑element labelled posets (~4.3×10⁸) were out of scope, so only `g(6) ≥ 8` is established. No Lean/repository changes were made.
