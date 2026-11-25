# antonina-IkU4WPzWRFa3MrSoBOYwIH-meadow

Session: ses_dfd004906ffesmXJSqwGI2qZ8h
Workspace: /home/lubko/soring-fronts/second-comparison-free-pair-forced-alln
Created: 1795346642718; updated: 1795347137328

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_202ffbc52001vbRCY9Y0HdOVKC)

I'll start by inspecting the repository state and the key documents.

## Output 21 (msg_202ffd864001sgSsndTEU6MCM3)

I'm on `billy-dev`. Let me read the key documents and locate the board.

## Output 49 (msg_20300189c001ABOXkPjBTozvY3)

Now let me read the board digest and the referenced research documents.

## Output 77 (msg_20300684000138KQnGwkqNvmLn)

Let me check existing scripts and search the board for related fronts to avoid duplication.

## Output 92 (msg_20301044a001oaB3dUrndYvIxM)

Let me examine the existing minimax evaluator code to reuse its core.

## Output 112 (msg_2030167b300114jwtnx07WzKGx)

I have the core DP pattern. Let me write a focused, independent exact-minimax script (scratch, in `/tmp/opencode`) to compute the three move-orbit values at P_1.

## Output 164 (msg_2030258c2001NfUqKCOGbLnw3z)

The computation found a falsifier at n=7. Let me verify these specific values with a fully independent plain labelled DP (no symmetry/duality quotient).

## Output 182 (msg_20303e868001Jo8teHWGXXXdWg)

Both implementations agree. Let me check n=8 to see the trend (endpoint tie vs strictly better).

## Output 193 (msg_203048cc3001lWjZIQOTvaTAqq)

Let me check the related 05:30Z front to confirm non-overlap, and read the board posting command syntax.

## Output 227 (msg_20306100f001pUIygFk2aoZnp4)

Before posting, let me check the ledger state for this front and confirm no prior finding exists.

## Output 238 (msg_20306275e001LBT7V4uDKH9U72)

Let me quickly verify the n=5 baseline with the plain DP too, for a fully consistent record.

## Output 249 (msg_203064c31001lAjH7obb2Fhyz2)

The claim is refuted at n=7 (independently verified). Let me compose and post the finding to board #301 — with no repository/Lean changes.

## Output 267 (msg_203070ab3001a05o7rWD26j9Cb)

Let me confirm the post landed correctly on the board.

## Output 278 (msg_203071c9d00119a3s29Xj5huDD)

## Result: the all‑n claim is false — exact counterexample at n = 7

Work was done only on `billy-dev`; the worktree is clean (no repository, Lean, test, CI, ledger, or `main` changes). The one external write is a finding posted to board #301.

### The claim, formalized
At `P₁ = {a<b} + (n−2) free keys`, with `F(P)=0` if total else `1+min_{incomparable {x,y}} max(F(P+x<y),F(P+y<x))` and `S(n)=F(antichain)`, the automorphism group fixes `a,b` and permutes free keys, giving exactly three move orbits: `{c,d}` (free–free), `{a,c}`, `{b,c}` (endpoints; `{b,c}` is the order‑dual of `{a,c}`, so they tie). `F(P₁)=S(n)−1`. The claim says the free–free orbit is *strictly* optimal for all `n≥5`.

### Falsifier (exact minimax, two independent implementations)
| n | S(n) | F(P₁)=S−1 | free–free orbit | endpoint orbit | gap |
|---|------|-----------|-----------------|----------------|-----|
| 5 | 7  | 6  | 1+5 = 6 | 1+max(6,5) = 7 | +1 (holds) |
| 6 | 10 | 9  | 1+8 = 9 | 1+max(9,8) = 10 | +1 (holds) |
| **7** | **13** | **12** | **1+11 = 12** | **1+max(11,10) = 12** | **0 — refuted** |
| 8 | 16 | 15 | 1+14 = 15 | 1+max(14,13) = 15 | 0 — refuted |

- Implementation 1: iso+dual+colour‑refinement canonical DP, reproducing `S(3..8)=3,5,7,10,13,16` (literature‑matching).
- Implementation 2: a plain labelled memoised minimax DP (no symmetry quotient, **no duality**), independently recomputing each successor. At n=7 it gives `F(3‑chain)=10`, `F(V‑shape)=11`, `F(two 2‑chains)=11`, `F(P₁)=12`.

So at n=7 a height‑`S(7)=13` optimal tree exists whose second comparison after `a<b` is `{a,c}` (endpoint + free key): it attains `F(P₁)=12` and wastes nothing. Both "must join two free keys" and "strictly wastes one comparison" are false.

### Why it breaks
The endpoint's bad branch is the V‑shape `a` below `{b,c}` (`e(P)=n!/3`, `n−3` free keys); free–free gives two disjoint 2‑chains (`e(P)=n!/4`, but `n−4` free keys — one fewer). At n=5,6 the V's larger extension count costs an extra comparison; by n=7,8 the extra free key cancels it. The gap is non‑monotone, so no all‑n proof of the invariant is possible.

### Honest limits
- This is a **machine counterexample** using the exact recurrence defining S — a verified *experiment/deduction*, not a hand proof or a general‑poset result.
- It is a local strategy‑normal‑form fact at one root‑reachable state: no faster evaluator, no certificate, and **no complexity‑class consequence** (picking the optimal move is the minimax game itself, and `e(P)` is #P‑complete). It concerns a different invariant from the extension‑inversion / uniform‑extension‑base‑gap fronts.
- I did not decide whether endpoint ever becomes *strictly* better for large n; n=8 was checked only by the quotient implementation (n=7 by both). `S(n)`/`SORT‑BOUND‑U` remain open.
