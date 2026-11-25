# antonina-bLxrT9SXgA6yUWDIgv95FM-tavern

Session: ses_e0866ce9bffeoPWnxq7cmoYO7M
Workspace: /home/lubko/soring-fronts/greedy-tiebreak-value-invariance-alln
Created: 1795155374539; updated: 1795156219009

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f79933c30010OOGWOjdPe4V3e)

I'll start by understanding the environment and studying the required documents in parallel.

## Output 29 (msg_1f79954c20012kgN6OtWzWNY4z)

Let me check the research board #301 and inspect this worktree for prior work (the task mentions possible infrastructure failure resumption).

## Output 44 (msg_1f7997254001eYWjpVaNo9hzLH)

Let me search the board for the specific front context (greedy-adversary-sufficiency, tie-breaking, G(12)) and check for any prior scratch work from this front.

## Output 63 (msg_1f7998942001G7TvkKo2qWQGAr)

There's substantial prior scratch work from this front. Let me inspect it carefully to avoid repeating side effects, and check whether this front has already posted to the board.

## Output 78 (msg_1f7999ec1001TqZFb6XhN47iyv)

Let me run the existing probes and inspect the remaining prior scratch to understand what's already established.

## Output 97 (msg_1f79bded7001bXHRbukLQQ0w7V)

The brute-force probes are too slow. Let me check the remaining prior analysis outputs and then write an efficient from-scratch solver.

## Output 112 (msg_1f79c8055001SWn2yQJAo6Xz7U)

Let me extract the full text of the key board posts about the greedy adversary from the archived board.

## Output 141 (msg_1f79cd08a001OzV6jZP740go6u)

I now have enough context. Let me write an efficient, independent solver and compute the greedy values Vmax/Vmin (the extremes over tie-breaking rules) for n up to as large as feasible, plus analyze the n=6 sibling tie.

## Output 166 (msg_1f79d87a6001IR53w0JVBy8yfn)

n≤6 confirmed. Let me launch n=7 in the background and analyze the decisive structural question: whether tied max-e siblings can have unequal greedy values (the mechanism a falsifier needs).

## Output 191 (msg_1f79edec70019539mGjrXVHvRM)

The local mechanism exists at n=6 (1440 poisoned ties) yet the root stays invariant. Let me check whether any reachable state itself has Vmax ≠ Vmin — that would be a stronger local counterexample.

## Output 209 (msg_1f79fb1dc001rrAekT3eVpXiea)

No reachable state has Vmax≠Vmin at n=6, despite 1440 poisoned sibling ties — so the sorter always avoids them. Let me dissect one concrete parent to find the avoidance mechanism.

## Output 227 (msg_1f7a080f8001odC8ZzN3GqHxGx)

Let me check the literature on whether the maximum-linear-extension adversary is known to be sufficient, and check the n=7 computation progress.

## Output 278 (msg_1f7a19410001peFlkW5NFrw8dv)

Let me verify the known S(n) values from a primary index (OEIS A036604) to anchor the n≤11 deduction.

## Output 314 (msg_1f7a23982001EomwufT4yVUltR)

While n=7 runs, let me test whether tie-break invariance is a general-poset phenomenon or a small-n accident by searching random posets on 7–9 elements for Vmax ≠ Vmin.

## Output 348 (msg_1f7a303ba001dsDG3djjM3UT2x)

Found a general-poset counterexample at n=7 (Vmax=7, Vmin=6). Let me verify it independently with a different representation and pinpoint the tie where the values diverge.

## Output 366 (msg_1f7a37282001Mq3dCnq6xsU7xJ)

Independently confirmed. Let me check the n=7 antichain job and whether the counterexample poset is greedy-reachable from A₇.

## Output 386 (msg_1f7a3e239001iT7K9d2aLty51n)

Let me check how board posts are made (prior agents' posting mechanism) before writing up the finding.

## Output 427 (msg_1f7a44b58001sqlka7lsCXertu)

I have solid findings. Let me compose and post the result to Antonina board #301.

## Output 463 (msg_1f7a4ec96001Q7KJmyBz6pMYh5)

## Report — front `greedy-tiebreak-value-invariance-alln` (billy-dev, worktree clean at `6a96398`, no repo/Lean changes)

Posted one result to board #301. Scratch only in `/tmp/opencode/tieinv`.

### What was established

**Model.** For a poset `P`, `Vmax(P)` / `Vmin(P)` are the greedy max-linear-extension game values with ties broken adversarially / cooperatively — the extrema over all deterministic tie-break rules. Invariance on `A_n` ⟺ `Vmax(A_n) = Vmin(A_n)`.

**1. Theorem (deduction, all n): `ceil(log2 n!) ≤ Vmin(A_n) ≤ Vmax(A_n) ≤ S(n)`.** Every greedy-legal answer keeps `e ≥ e(P)/2`, so any tie rule needs ≥ `ceil(log2 n!)` comparisons; the greedy adversary is a restriction of the unrestricted one, so `Vmax ≤ S(n)`. Hence invariance is **forced with no computation** whenever `S(n) = ceil(log2 n!)`. With primary values (OEIS A036604) this covers **n ≤ 11 and n = 20, 21**; within known range n ≤ 22 a counterexample can only lie in **{12,…,19,22}**. This strictly extends the earlier n ≤ 6 evidence and localizes the falsifier without search.

**2. Finite confirmation (from-scratch solver).** `Vmax=Vmin=S(n)=ceil(log2 n!)` for n ≤ 6; at n=6 the greedy ball exhausts all 130023 labelled posets and *every* one is invariant. Poisoned ties exist (1440 e-ties with unequal child values, e.g. children with e=14 and values 4 vs 5), but the sorter always has a non-poisoned optimal move — dissected an explicit e=28 parent showing pairs scoring 6 (poisoned) versus 5 (safe, equal to root value).

**3. New counterexample (general posets, n=7).** The poset with successor masks `[2,0,75,67,64,66,0]` has `e=56`; at the root, comparing elements 3 and 4 is an e-tie (both children e=28) with greedy values **5 vs 6**, so **`Vmax=7 ≠ 6=Vmin`**. Independently verified with a second representation (edge sets + permutation-counted extensions). n=7 is minimal (no smaller poset is non-invariant). This falsifies the *general-poset* invariance claim — but by item 1 the n=7 **antichain** is still invariant, so general-poset non-invariance does not transfer to `A_n`.

**4. Exact obstruction.** An antichain falsifier needs `S(n) > ceil(log2 n!)` (first at n=12) and a reachable optimal state where *every* optimal greedy move is an unavoidable poisoned tie. At n=12 this means `Vmin=29 < 30=Vmax` — requiring greedy sufficiency **and** cooperative-tie info-tightness simultaneously; `G(12)` is open (Wells/Peczarski/Stober–Weiss exhaustive-search barrier). Not settled.

### Honest limits / failed approaches
- No all-n proof and **no antichain counterexample**; the all-n question stays open, first candidate n=12.
- Full exact computation at n=7 was attempted but abandoned (state explosion) — the sandwich theorem makes it unnecessary.
- General-poset non-invariance does **not** yield a reduction to `A_n`; there is no valid transfer.
- A positive answer would only make the greedy value *well defined* — not a polynomial evaluator (still full minimax). A greedy transcript is a **sound** upper-bound certificate for `S(n) ≤ k`, but **completeness** (no succinct proof that no better tree exists; optimal trees have ≥ n! leaves) is not implied.
- No class separation, no new `S(n)` value, no Lean or repository change.

## Output 484 (msg_1f7a53c62001St58C754bF5yG2)

**Recovery check (no actions repeated):**
- **Working tree / git:** clean, HEAD still `6a96398` on `billy-dev`; no commits, PRs, or repository file changes made by this session.
- **Board #301 external side effect:** already completed. `antonina board comment --id 301 --author "SoringP1 frontier: greedy-tiebreak-value-invariance-alln"` is present (2026-11-20T06:28:45.661Z; payload/result recorded at `/tmp/opencode/tieinv/post_result.json`, exit 0). No duplicate post made.
- **Scratch:** independent computations under `/tmp/opencode/tieinv/` only (no durable/external effect beyond /tmp).
- **No unfinished external work** identified; no uncertain external effects.

**Finding already reported (front `greedy-tiebreak-value-invariance-alln`, from-scratch):**
- **All-n theorem (deduction):** `ceil(log2 n!) ≤ Vmin(A_n) ≤ Vmax(A_n) ≤ S(n)` (Vmin/Vmax = greedy max-LE value extrema over tie-break rules), so invariance on the antichain is *forced* whenever `S(n)=ceil(log2 n!)` — i.e. for known `n ≤ 11` and `n = 20,21` (OEIS A036604). Within known `n ≤ 22`, any counterexample can only lie in `{12,…,19,22}`.
- **Finite confirmation (experiment):** `Vmax=Vmin=S(n)` for `n ≤ 6`; at `n=6` all 130023 greedy-reachable states invariant. 1440 poisoned e-ties exist (equal-e siblings with unequal greedy values, e.g. value 4 vs 5) but the sorter always has a non-poisoned optimal move.
- **General-poset counterexample (experiment, independently re-verified):** n=7 poset with successor masks `[2,0,75,67,64,66,0]`, `e=56`: root pair (3,4) is an e-tie with children `e=28` and values `5 vs 6`, hence `Vmax=7 ≠ 6=Vmin`. Minimal (none for ≤6). Falsifies *general-poset* invariance but does **not** transfer to `A_n` (n=7 antichain remains forced-invariant).
- **Exact obstruction:** an `A_n` falsifier requires `S(n)>ceil(log2 n!)` and a reachable optimal state where every optimal greedy move is an unavoidable poisoned tie (at n=12 equivalent to `Vmin=29 < 30=Vmax` alongside `G(12)=30`); `G(12)` open (exhaustive-search barrier).
- **Honest limits:** no all-n proof, no antichain counterexample, no n=12 resolution, no general-poset→antichain transfer, no class separation / new `S(n)` / polynomial evaluator; positive answer would only make greedy value well defined (sound upper-bound transcript, not a completeness certificate). No Lean/repo changes.
