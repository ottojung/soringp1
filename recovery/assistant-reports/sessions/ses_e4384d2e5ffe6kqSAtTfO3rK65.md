# antonina-yWTWpHFxQMUT87ZZbPbU4g-ascending

Session: ses_e4384d2e5ffe6kqSAtTfO3rK65
Workspace: /home/lubko/soring-fronts/matching-poset-evaluator-complexity
Created: 1794163551593; updated: 1794164943804

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 27 (msg_1bc7b4b57001PeZVGemtEDxaFl)

I'll start by inspecting the environment and durable state before doing anything, to avoid duplicating side effects.

## Output 587 (msg_1bc8e0ae50011T4mo2I6Hin1pl)

I found a concrete structural correction: the first FJ-beating split‑merge construction is itself matching‑prefix, so it supports rather than refutes the normal form. Let me record the reasoning and then post it once to the board.

## Output 625 (msg_1bc8f0cfd001AtBkI0sVNjUSO8)

Recovery check: the working tree is clean at `6a96398`, no prior post from this front existed, and I made exactly one new board #301 post (verified by digest, timestamp `2026-11-08T19:07:19.309Z`). No repo, Lean, PR, or commit changes.

## Mathematical finding

**New deduction — front-loading lemma.** If an algorithm sorts `n` keys by splitting them into two disjoint blocks, sorting each block by Ford–Johnson (or any block algorithm whose first phase is an internal matching), then merging optimally, it is a matching-prefix algorithm whenever `n` is odd. The two blocks’ initial pair phases total

`floor(m/2) + floor((n-m)/2) = floor(n/2)`

disjoint comparisons, covering all but one key. So the same algorithm is a strategy from `M_n`, and its total cost `H` satisfies `F(M_n) <= H - floor(n/2)`.

**Consequence at n=47.** The published 200-comparison Ford–Johnson improvement at `n=47` is the split-merge construction (Manacher 1979/1989; Peczarski 2007 studies exactly this class). Front-loading gives

`F(M_47) <= 200 - 23 = 177`,

not the FJ-continuation value `M(47)-23 = 178`. Hence `E_M(47) <= 2`, while `E_FJ(47)=3`. The board’s line `E_M(47)=178-(198-23)=3` uses the FJ upper bound, not the best split-merge value. In particular, **the n=47 FJ non-optimality is not a counterexample to the normal form**: if `S(47)=200`, the sandwich forces `F(M_47)=177` and the normal form holds at 47.

**First genuine open cell.** At `n=23`, `C=75`, `M=76`, `k=11`, `F(M_23) in {64,65}`, `S(23) in {75,76}`. The normal form fails exactly at `(F,S)=(65,75)`. A 64-comparison strategy from `M_23` would prove `S(23)=75` and make the normal form hold there; proving `F(M_23)>=65` alone does not settle `S(23)`. Peczarski’s no-beat-below-47 result says the split-merge class gives nothing at 23, so any counterexample must come from a non-matching-prefix optimal sorter.

## Failed approach / obstruction

I did not obtain an unconditional counterexample or a `2^{Omega(n log n)}` lower bound. The proposed complexity falsifier is not accessible with current techniques: `F(M_n)` is a unary sequence with a `2^{O(n log^2 n)}` evaluator, and an all-algorithm superpolynomial lower bound would be a major complexity separation. Even an exact `F(M_n)` evaluator yields `S(n)` only through the front identity, whose first unresolved instance is the `n=23` cell above.

**Caveat:** I did not open the paywalled Peczarski table, so the exact split/merge numbers at 47 were not independently reproduced. The `F(M_47)<=177` conclusion is conditional on the 200 bound being the cited split-merge construction; if that bound comes from a different algorithm, it needs rechecking. General-poset hardness and certificate soundness were kept separate from completeness.

## Output 671 (msg_1bc90573a001ycd1IPp0n0gQMF)

Recovery audit complete. I did not repeat the prompt or create any new external effects.

**Verified state**
- Host: `billy-dev`
- Working directory: `/home/lubko/soring-fronts/matching-poset-evaluator-complexity`
- Git: clean worktree at `6a96398`; no commits, branches, edits, or Lean changes
- Board #301: exactly **one** matching post from this front, at `2026-11-08T19:07:19.309Z`, titled with the n=47 correction. Digest reports one unique match; no duplicate was posted.
- Durable ledger: `matching-poset-evaluator-complexity` is still `status: running` with no finding recorded. That transition belongs to the keeper; I did not edit it.
- Scratch artifacts only: `/tmp/opencode/matching-poset-evaluator-post.md` and `/tmp/opencode/matching-poset-board-result.json`.

**Unfinished work**
None. The previous turn completed the investigation and posted its finding once: the front-loading lemma, the corrected `F(M_47) <= 177` / `E_M(47) <= 2` bound, the conclusion that the n=47 Ford–Johnson improvement is not a normal-form counterexample, and the precise open `n=23` failure cell `(F,S)=(65,75)`. The honest caveat about the paywalled Peczarski table remains part of that post.

No uncertain external effect requires review.
