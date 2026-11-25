# antonina-ZiessRiP5n3fqzMCHP0DUj-exercise

Session: ses_e44352856ffegrCFTE3fiOpLKt
Workspace: /home/lubko/soring-fronts/logarithmic-information-excess-alln
Created: 1794151995532; updated: 1794152884396

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1bbcadd4c001SlOGiCuAonDRtc)

I'll start by orienting myself in the repository, reading the governing documents and the current research board.

## Output 353 (msg_1bbd2ec39001EmTkX8F60Lz6w8)

I've established the literature picture. Now let me verify the key small-instance facts I'll rely on, with an independent computation.

## Output 481 (msg_1bbd66d64001I8zCIgzn6pY9Jf)

I have a clear picture now. Let me write up the finding, then post it to the research board.

## Output 510 (msg_1bbd6fb5e001cJTXMxipRLth21)

The post is live. One sentence in it needs tightening for accuracy — let me add a short correction rather than leave an overstated check.

## Output 530 (msg_1bbd74336001HW4iV4RMAKvwiE)

Work is done on `billy-dev` only. Worktree is clean; no Lean, scripts, docs, workflow or ledger changes. Findings are on board #301 (one post, plus one precision follow-up).

## What I studied
`AGENTS.md`, `docs/problem.md`, the #301 digest, the frontier ledger, and the primary literature — in particular I downloaded and read Sergeev, *On the asymptotic complexity of sorting*, ECCC TR20-096 (2020), plus Fredman 1976, Haeupler et al. 2024/26, van der Hoog–Rotenberg–Rutschmann 2024/26, OEIS A036604, and the Peczarski/Stober–Weiß exact-value line.

Let `C(n)=⌈log₂(n!)⌉`, `E(n)=S(n)−C(n) ≥ 0`.

## Mathematical findings

**1. The front is open, and its two "horns" are not complementary.**
Sergeev gives `E(n)=o(n)` (his paper is an upper-bound/algorithms paper; its only lower bound is the information bound). Exact data give `E=1` for `12–19`, `E(20)=E(21)=0`, `E(22)=1`, `E(28)≥1`. So `0≤E≤o(n)`, and both `E=O(log n)` and `E=ω(log n)` on a family are open. The literal second alternative ("`E≥c log n` infinitely often") is strictly weaker than the negation of the first ("`E=O(log n)`"); e.g. `E=Θ(log n)` satisfies both. The correct falsifier is `limsup E/log n = ∞`, which matches the FALSIFIER's `ω(log n)`.

**2. The stated complexity implication does not follow (model fidelity).**
The first horn would make the poly-time computable `round(log₂ n!)` an `O(log n)`-additive approximation, but gives no `S_unary ∈ FP` (the residual offset is unresolved). The second horn only says the *information bound* is not `O(log n)`-close; it does not rule out exact polynomial-time evaluation (error 0) nor any other logarithmic-additive approximation. Neither horn decides `S_unary ∈ FP` / `SORT-BOUND-U ∈ P`. This corrects a conflation of value asymptotics with computational complexity.

**3. Exact obstruction to the natural lower-bound routes.**
- **Root one-ply is neutral:** the first antichain comparison splits `n!` exactly in half, so `L1(antichain_n)=L0(antichain_n)=⌈log₂ n!⌉` for `n≥2`.
- **Rounding is harmless:** if `h(1)=0`, `h(e)=1+h(⌈e/2⌉)`, then `h(e)=⌈log₂ e⌉`. So if every split were integer-perfect the height would be exactly `⌈log₂ n!⌉`; **all** excess is structural, not 2-adic/parity rounding.
- **Sound local gaps do not transfer:** independent minimax recomputation gives `e(W)=8, F(W)=4` and `e(Merge(2,4))=15, F(Merge(2,4))=5` (local gap 1 each), yet `S(5)=7=C(5)` and `S(6)=10=C(6)` (memoized 4231 and 130023 posets), so `E(5)=E(6)=0`. Certificate soundness at a reachable poset is not completeness/transfer at the antichain.
- **The exact missing lemma:** if the larger-child adversary path reaches `P` with `F(P)≥log₂e(P)+g`, then `S(n)≥log₂n!+g`. No construction gives `g=Ω(log n)`; suffix-extension/ordinal-sum/merge witnesses fail because added relations only decrease `F`.

**4. Correction of a recurring ledger error.** Several fronts used "Fredman's `n−log₂n−O(1)` additive *lower* bound." Fredman's `log e(P)+O(n)` is an *upper* bound on comparisons; read as an all-n lower bound it contradicts Sergeev for all large `n`. (I tightened one accompanying `n=10` remark on the board to the unconditional asymptotic contradiction.)

## Honest limit
I did **not** prove either horn, nor find a counterexample family. The contribution is a precise no-transfer obstruction, two verified non-transfer counterexamples, a closed-off rounding route, and the model-fidelity correction that the front's complexity consequence is invalid. Proving the first horn needs an explicit `O(log n)`-surplus sorting construction (a major strengthening of Sergeev); proving the second needs a new lower-bound mechanism forcing `Ω(log n)` bias along every balanced path.

## Output 594 (msg_1bbd84f13001g7QcX17Uhnf4ar)

Inspected state after the backend failure. No re-posting, re-running, or repository edits were performed.

## Effects that actually happened
- **Board #301 — exactly two comments**, both from author `SoringP1 frontier: logarithmic-information-excess-alln`:
  - `2026-11-08T15:46:21Z` — main finding (front status, literature audit, non-complementarity of the two alternatives, complexity-implication correction, one-ply/rounding/non-transfer obstructions, honest limits).
  - `2026-11-08T15:46:41Z` — precision follow-up tightening the `n=10` sentence to the unconditional asymptotic contradiction with Sergeev.
  - Digest confirms **2 unique matches**, so there is no duplicate post.
- **No repository changes.** `git status` is clean at `6a96398` on branch `billy-dev`; no new commits, no Lean/script/doc/workflow edits.
- **Local scratch only:** `/tmp/opencode/lgx/{post.md,sergeev.pdf,sergeev.txt,verify.py}`.

## Durable task record
- `frontier-ledger.json`: `logarithmic-information-excess-alln` is still `status: running`, `agent_id: ZiessRiP5n3fqzMCHP0DUj-exercise`, `exit_state: None`, `finding_len: 0`.
- This is the expected keeper state for an active agent: `research_frontier.py::reconcile()` only writes `exit_state` / `finding_unverified` / `investigated` after the agent reaches `clearexit` (or another terminal state). I did **not** hand-edit the shared ledger, to avoid racing the keeper.

## Remaining work
None that is mathematically or operationally safe to continue. The research, the one board report, and the correction are complete and recorded exactly once. The only open item is the automatic ledger reconciliation on agent exit, which should be left to the keeper. No uncertain external effect needs review.
