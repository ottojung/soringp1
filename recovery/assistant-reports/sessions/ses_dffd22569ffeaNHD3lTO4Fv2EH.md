# antonina-vgMPA21ZjfLhkwQjcNdcAf-reopening

Session: ses_dffd22569ffeaNHD3lTO4Fv2EH
Workspace: /home/lubko/soring-fronts/r-valued-relaxation-ladder-exact-evaluator-alln
Created: 1795299334855; updated: 1795300885690

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_20035490f001KM0y5TPUBM2dLO)

I'll start by inspecting the current state carefully, since this is a resume after a backend failure. I need to determine what already happened before doing anything.

## Output 28 (msg_200355671001yfeQKfCc96JD5k)

This is a shared workspace with extensive prior agent activity. I'm already on `billy-dev` and the tree is clean. I need to determine what happened in the interrupted turn related to *this specific* front (the r-valued ladder B_r(n)). Let me search the durable records.

## Output 87 (msg_20035e88b001NZ1FiOmoD03qsu)

I've confirmed: no prior board post or commit for this specific front exists; the tree is clean on `billy-dev`. The interrupted turn left no side effects I need to undo. Now I'll study the mathematical background.

## Output 102 (msg_200367fe7001AN9CPx2b1QWRWM)

I now have the model. Let me verify no repository/board side effects happened, then build a from-scratch evaluator. First, a quick literature check in parallel with reading the known-exponent derivation.

## Output 121 (msg_200377f0f001A1EPtRrv5z54Zg)

Web search is unavailable in this environment (cancelled); I'll rely on the repo's curated literature and be explicit about that limit. Now let me build a from-scratch evaluator in scratch space (no repo changes).

## Output 182 (msg_200383d200010c53LSD1xjfEcw)

Interesting — but the poset-keyed memo inflates state counts. Let me cross-validate with an independent subset-based minimax (memoized on the consistent set itself), which is unambiguous, and extend to n=7.

## Output 200 (msg_200388e6b001kDzVGEHq9O0T1A)

Two independent implementations agree on all values. A striking data point: B_3(6)=10=S(6) although its information bound is only 9. Let me push to n=7 for small r and check the local literature notes.

## Output 233 (msg_2003958ec001GPjSPBgRSDARR7)

Let me verify the n=7 run status and locate the board-posting mechanism (read-only inspection, no posting yet).

## Output 302 (msg_2003a105a001bAgKmP4WZV6YXV)

Let me check the n=7 computation result now.

## Output 313 (msg_2003a86d9001um44YUnqhdCgE4)

The n=7 job is still running (output buffered). I have enough for the core finding. Let me write the scratch finding note (no repo changes), then finalize once n=7 returns.

## Output 324 (msg_2003af258001pA5p7zxRlTe1Vx)

I found a sharpening of the main theorem and an error in my draft's entropy claim. Let me re-derive carefully and correct the note.

For general r = n^β, taking s = n^{1-β}, L = n^β in the frontier construction gives m = Θ(β n log n), M = Θ(n^{2-β}), and a frontier exponent β(1-β)·n log²n — so the barrier holds for *every* polynomially-large rung, not just r > n/2. Only subpolynomial rungs are cheap.

## Output 362 (msg_2003bd79d001B2ulhJqNefsnHv)

Let me validate the model itself (achievable outputs = permutations with ≤ r runs) by brute force over value assignments.

## Output 382 (msg_2003c189a001ZOxAI11UAKjKjG)

Model validated by brute force. Now let me draft the board report and verify the board state immediately before posting (single, careful external write).

## Output 427 (msg_2003ca6b3001m0wV4Irpdvqz4f)

The fresh board read confirms this front was just commissioned (22:26Z) and has no result post yet. My binary values match Viche's independent verification. Posting my result now — the single external write.

## Output 447 (msg_2003ce9a0001Alb7unLcfaNxwk)

Post succeeded. Let me verify it landed exactly once and check on the n=7 computation.

## Output 478 (msg_2003d3b2d001x5sBFVqp1Dh86f)

The n=7 run finished: B_2(7)=9, matching Viche's independent computation. (The r=3,4 n=7 runs hit the timeout.) Let me record this in scratch only — no duplicate board post.

## Output 505 (msg_2003d98c90010nnSRMrt9YOQGj)

## Recovery audit

On `billy-dev`, clean at `6a96398`; reflog shows no commit this session. Board #301 had **no prior post or ledger entry** for this front (the 22:26Z dispatch had just commissioned it), so the interrupted turn left no side effect to repeat. I made exactly **one** external write: a result comment on #301 (verified present once). No repository, Lean, test, CI, or ledger changes — all code is scratch under `/tmp/opencode`.

## Mathematical finding

**Model [definition].** With values in `[r]` and `(value,index)` tie-breaking, the achievable sorted outputs are exactly the permutations with ≤ r−1 descents (verified by brute force over all rⁿ assignments for n≤6). `X_r` is a strictly increasing family, `B_r(n)=F(X_r)`, and `B_n(n)=S(n)`. Crucially `X_r` is **not** `S_n`-invariant, so the sound full-relabelling quotient that compresses the `S(n)` DP does not apply to any proper rung.

**Small-n check [experiment].** Two independent from-scratch evaluators (poset+closure; subset-of-`X` minimax) agree, and `r=n` reproduces `S(2..6)=1,3,5,7,10`:

- `B_2(2..7) = 1,3,4,6,7,9` — matching Viche's independent 22:26Z values; far below `S`.
- `B_3(4,5,6) = 5,7,10`, `B_4(5,6)=7,10`.
- Sharpest datum: **`B_3(6)=10=S(6)` while its information bound is only 9** (`|X_3|=360`). A rung can be exactly as hard as full sorting from a root-level minimax/realisability gap, not a leaf-count artifact (same mechanism as `S(12)=30>29`). But this is finite-n: for fixed r, `|X_r|~rⁿ`, so these rungs are eventually `o(S(n))`.

**Falsifier horn A — barrier on every polynomially large rung [deduction].** Fix β∈(0,1], `r=n^β`; take `L=n^β/2`, `s=n/L`, apply the repo's winning-frontier construction at budget `k=B_r(n)`. New step: each constructed poset (s chains of length L plus forward extra edges) has a level-by-level linear extension with ≤ L ≤ r runs, so it is **reachable in the r-valued game**, and the merge strategy makes it **winning** in `k−t` comparisons. With `m=k−t₀−Bmerge=(β+o(1))n log n`, dividing `binom(M,m)` by `n!` labellings yields

`≥ 2^{(β(1−β)−o(1))·n log₂²n}` nonisomorphic reachable winning states at budget `B_r(n)`

(β=1/2 recovers the repo's 1/4 constant; `k` is pinned by `ceil(log₂|X_r|) ≤ B_r(n) ≤ S(n)=log₂(n!)+o(n)`, Sergeev TR20-096 Thm 3). Hence any evaluator of such a rung that enumerates its winning state space needs `2^{Ω(n log₂²n)}` time — the known exponent. Only subpolynomial rungs are cheap, and there `B_r(n)=O(n log r)=o(S(n))` with an Ω(n log n) value gap, so no cheap correction formula recovers `S(n)`'s leading term.

**Horn B [deduction].** `B_r(n)≤S(n)` is sound but complete only at r=n; a winning frontier state is a sound certificate `B_r(n)≤k`, not a complete evaluator. General-poset excess `F(P)−⌈log₂e(P)⌉` is unbounded on arbitrary posets but does not transfer to the fixed outcome family `X_r`.

## Honest limits

- This is an **enumeration barrier**, not a general time lower bound. The strict claim "whole ladder in `2^{o(n log²n)}`" is **not** refuted for selective/compact/symbolic methods; selective minimax is exactly what the source barrier doc leaves open.
- No membership or separation for `SORT-BOUND-U` in P/NP/PSPACE follows; tally/sparse constraints still apply. Sergeev is used only as an asymptotic, non-effective `o(n)` surplus (no finite threshold).
- Web search was cancelled in this environment; literature relies on the repo's curated baseline and the local Sergeev text, noted as such in the post.
- n=7 completed only for r=2 (r=3,4 hit the time cap); no all-`n` formula for `B_r(n)` is claimed from finite data.

Scratch record: `/tmp/opencode/rval_ladder_finding.md`, `rval_eval.py`, `rval_subset.py`.

## Output 524 (msg_2004540980017G7DQJdpz27dRO)

I'll do a read-only audit to confirm what already happened. I will not post, commit, or otherwise write anything.

## Output 539 (msg_20045633c001w9NJ2W3Cvr4ZE6)

## Read-only recovery audit — result: work already complete, nothing to redo

**Git state.** Branch `billy-dev`, clean working tree, HEAD `6a96398`. Reflog contains only the original clone — **no commits, branches, or repo/Lean/test/CI/ledger changes** were made by this front.

**Board #301.** Exactly **one** post by this front: 2026-11-21T22:32:16.290Z, author `SoringP1 researcher: r-valued-relaxation-ladder-exact-evaluator-alln`, body length 3858 — the RESULT comment containing the finding. (The newest board message, 22:35:43Z, belongs to a *different* front, `binary-test-universe-height-gap-alln`; I did not touch it.) Count of my posts = **1**, so no duplicate post occurred and none is needed.

**Durable scratch records** all intact under `/tmp/opencode`: `rval_ladder_finding.md`, `rval_eval.py`, `rval_subset.py`, `rval_post_body.md`, `rval_post_result.json`.

**Effects that actually happened in the prior turn:** scratch computation + one board comment. **Effects that did not:** any repository mutation, any second post, any commit/purchase/other external action.

**Unfinished work:** none. The research task's deliverable (a mathematical finding with honest limits) was produced and reported in that single post: the model validation, the exact `B_r(n)` table, the frontier-enumeration barrier on every polynomially large rung `r=n^β`, the subpolynomial-rung exactness loss, and the explicit scope caveats (enumeration barrier only; no complexity-class claim). The `n=7, r=3,4` computations that timed out were explicitly recorded as an honest limit, not an outstanding obligation.

No further external action taken this turn — I only read Git state and the board.
