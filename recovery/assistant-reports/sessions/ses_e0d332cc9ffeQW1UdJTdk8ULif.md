# antonina-ec2VWsjPt9eYzV053KcKzi-normal

Session: ses_e0d332cc9ffeQW1UdJTdk8ULif
Workspace: /home/lubko/soring-fronts/core-census-growth-exponent
Created: 1795074872261; updated: 1795075767568

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f2ccd75d001IHu25gQIWTPcLv)

I'll start by understanding the environment, the relevant documents, and the current state of the work.

## Output 21 (msg_1f2cce62e001yEUKwtfuOCboYG)

I'm on billy-dev. Let me look at the research board, operations, literature, and the newest committed research doc.

## Output 40 (msg_1f2ccf4d1001nXPMVKpg5DneND)

`docs/research-core-threshold.md` isn't on billy-dev's working tree. Let me locate it across branches and read board #301.

## Output 55 (msg_1f2cd0901001V8zEzVaRifSy3A)

The core-threshold doc is on `origin/main` (f89f6d0), head of my branch is 6a96398. Let me read it and check the board for any prior work on this exact front.

## Output 70 (msg_1f2cd2654001b4xwTX9mSi06ZB)

My local `origin/main` ref may be stale. Let me refresh and locate the core-threshold doc and its counts.

## Output 90 (msg_1f2cd513f001kDNEiIfQ0sPYGd)

The claim is about the growth of C(E), the number of cores with e≤E. Let me examine the census implementation and check the board for any prior post on this exact front before doing anything.

## Output 114 (msg_1f2cee1e0001Tsk1yux2f4pNcy)

No prior report on this exact growth front; only the core-threshold verification. Let me set up scratch analysis in `/tmp/opencode` and compute the actual distribution of cores by extension count.

## Output 150 (msg_1f2d1298d001KWTto4kj4c6bM8)

While that runs, let me check the literature on counting posets by number of linear extensions.

## Output 201 (msg_1f2d20195001P10CtpWHoIRpYZ)

Let me fetch the OEIS triangle of posets by exact linear-extension count (A263860) to ground the counting question in data.

## Output 230 (msg_1f2d3271f001yEoESCYm93Ef1m)

I have a candidate superpolynomial family. Let me verify it computationally before committing to it.

## Output 264 (msg_1f2d4fe6b001RjBhTkqM2icNA2)

The first family collapsed under isomorphism. Let me test a cleaner family: take any poset Q on k elements and adjoin one element incomparable with everything (so P = Q ⊔ single point). This is always a core with e(P) = (k+1)·e(Q).

## Output 282 (msg_1f2d5ebba001nPwiwmGXrp5Im3)

The clean family is verified: C((k+1)!) ≥ p(k) = A000112(k). Let me check the census job and confirm the numbers are consistent.

## Output 293 (msg_1f2d65646001N2KcnMI31wlcTO)

The theorem is established. Let me check the frontier ledger for this front's ID and the board-posting convention before reporting.

## Output 405 (msg_1f2d92451001oLL5kcsrA4r2h4)

The result is solid and the worktree is clean. Let me post the single board #301 deliverable.

## Output 432 (msg_1f2d9c6a40012l8MQJdloaGIH1)

## Finding

The polynomial-growth hypothesis for the core census is **false**: `C(E)` is superpolynomial. Posted as a single report to Antonina issue #301 (author `SoringP1 frontier: core-census-growth-exponent`). No repository, Lean, test, ledger or branch changes; worktree on `billy-dev` is clean at `6a96398`.

**Theorem [paper proof].** Let `E_k = (k+1)!` and `p(k)` = number of unlabeled posets on `k` elements (OEIS A000112). Then `C(E_k) ≥ p(k)` for every `k ≥ 1`.

- For any `k`-element poset `Q`, let `P_Q = Q ⊔ {z}` with `z` incomparable to all of `Q`. Every element is then non-universal (each `q ∈ Q` is incomparable with `z`), so `P_Q` is a core; and `e(P_Q) = (k+1)·e(Q) ≤ (k+1)·k! = E_k`. Disjoint union with a singleton reflects isomorphism, so the map `Q ↦ P_Q` is injective on isomorphism classes.
- Elementary count: `p(k) ≥ 2^{⌊k²/4⌋}/(a! b!)` with `a = ⌊k/2⌋, b = ⌈k/2⌉` (height-two posets, bipartite matrices modulo `S_a × S_b`).
- Hence `log₂ C(E_k) ≥ k²/4 − k·log₂ k − O(k)` while `log₂ E_k = (1+o(1)) k log₂ k`, so `C(E_k) > E_k^c` eventually for every fixed `c`. Quantitatively `C(E_k) ≥ E_k^{Ω(log E/log log E)}`.

A from-scratch check (my own transitive-closure enumeration, using the repo's canonizer only as a black box) confirmed for `k = 2..5`: exactly `2, 5, 16, 63` classes `Q`, each `P_Q` a core with `e(P_Q) = (k+1)e(Q)` and all pairwise nonisomorphic — giving `C(720) ≥ 63`.

## Failed falsification attempt

I first tried encoding exponentially many extras-posets at `e ≈ 2^k` via a chain `c₁ < … < c_k` with one extra `x_i` incomparable only with `c_i`. It collapses: transitivity forces `x_i < x_j` whenever `j ≥ i+2`, leaving only adjacent-pair freedom. At `k = 4`, all 16 candidate relations collapse to **2** isomorphism classes (verified). Disjoint union, not chain attachment, is what preserves the `2^{Ω(k²)}` distinct shapes.

## Honest limits

- The superpolynomial regime only overtakes a cubic fit around `k ≈ 80–110`, i.e. `E ≈ (111)!`; it does **not** contradict the near-cubic empirical slope at `E ≤ 88`, which is a small-`E` transient.
- The count is over **all** cores with `e ≤ E`. The witnesses are reachable from the antichain and information-tight, so a complete `e`-indexed threshold lookup cannot be polynomial-size. But this does **not** rule out a smaller table restricted to optimal-play states, and gives no complexity lower bound for computing `S(n)` itself (blocked anyway by the sparsity/tally barrier). The all-`r` Fibonacci inequality `e(P) ≥ F_{m(P)+2}` and Lemma A are untouched.
- No Lean or repository note was added: the argument is elementary and its crossover lies far beyond the committed census range, so under the publication gate it belongs on the board, not in the tree.

## Output 461 (msg_1f2da36d3001w1wl5N6u8K6Dvc)

Recovery inspection complete (no actions repeated):

- **Git / repo state:** `/home/lubko/soring-fronts/core-census-growth-exponent` on `billy-dev` at `6a96398` (`HEAD`), working tree clean (`git status --short --branch` empty). `origin/main` fetched to `f89f6d0` (read-only, to read `docs/research-core-threshold.md`); no merge, no commits, no pushes, no repo/Lean/test/workflow/ledger edits.
- **Board #301 (durable external effect):** `board_digest.py --contains "core-census-growth-exponent" --page 1` shows exactly **one** post authored `SoringP1 frontier: core-census-growth-exponent` (2026-11-19T08:08:21.542Z) plus the earlier Executive dispatch naming the front. No duplicate post exists; I did not repost.
- **Scratch artifacts:** `/tmp/opencode/census-growth/` contains the analysis scripts, `report.txt`, and `post_result.json` (the posted body/result). No active analysis process remains.
- **Unfinished work / uncertainty:** none identified. The front’s task (falsifiable all-`n` claim about growth of `C(E)`, serious falsification attempt, honest limits, single board report) was fully completed in the prior turn.

**Result already delivered:** `C(E)` (isomorphism classes of cores with `e ≤ E`) is superpolynomial — for `E_k=(k+1)!`, `C(E_k) ≥ p(k) = A000112(k)` via the injection `Q ↦ Q ⊔ {z}` (a core with `e=(k+1)e(Q) ≤ E_k`), hence `C(E_k) ≥ E_k^{Ω(log E / log log E)}` and `C(E_k) > E_k^c` eventually for every fixed `c`. This falsifies any fixed-polynomial bound (the `E ≤ 88` near-cubic trend is a small-`E` transient). Independent from-scratch check matched `p(2..5)=2,5,16,63`; a chain-attachment alternative collapsed (16→2 classes at `k=4`). Limits: census is over all cores (not optimal-play-only states), so it rules out polynomial-size complete `e`-indexed threshold lookup but gives no bound on computing `S(n)`; Fibonacci/Lemma A untouched. No further action taken.
