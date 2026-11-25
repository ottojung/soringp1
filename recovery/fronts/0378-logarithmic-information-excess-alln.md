# logarithmic-information-excess-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ZiessRiP5n3fqzMCHP0DUj-exercise

## exit_state

clearexit

## question

For the exact sorting number S(n), is S(n) - ceil(log2(n!)) = O(log n) for every n, or is there an infinite family of n on which this excess is at least c log n for some fixed c > 0?

## basis

Sergeev's bound S(n)-log2(n!) = O(n/(log n)^(1/5)) and the information lower bound leave the logarithmic range open; the ledger's excess and additive-approximation fronts target bounded excess and O(1)/O(log log n) error, not this O(log n) threshold.

## falsifier

Prove the O(log n) upper bound with explicit constants for all n, or certify an infinite family with excess omega(log n); a single family beating every proposed logarithmic bound refutes the first horn.

## implication

The first horn would sharply improve Sergeev's o(n) excess and give a polynomial-time O(log n)-additive approximation; the second would establish a new super-logarithmic excess regime and rule out logarithmic-additive exact evaluation.

## finding_unverified

`n!` exactly in half, so `L1(antichain_n)=L0(antichain_n)=⌈log₂ n!⌉` for `n≥2`.
- **Rounding is harmless:** if `h(1)=0`, `h(e)=1+h(⌈e/2⌉)`, then `h(e)=⌈log₂ e⌉`. So if every split were integer-perfect the height would be exactly `⌈log₂ n!⌉`; **all** excess is structural, not 2-adic/parity rounding.
- **Sound local gaps do not transfer:** independent minimax recomputation gives `e(W)=8, F(W)=4` and `e(Merge(2,4))=15, F(Merge(2,4))=5` (local gap 1 each), yet `S(5)=7=C(5)` and `S(6)=10=C(6)` (memoized 4231 and 130023 posets), so `E(5)=E(6)=0`. Certificate soundness at a reachable poset is not completeness/transfer at the antichain.
- **The exact missing lemma:** if the larger-child adversary path reaches `P` with `F(P)≥log₂e(P)+g`, then `S(n)≥log₂n!+g`. No construction gives `g=Ω(log n)`; suffix-extension/ordinal-sum/merge witnesses fail because added relations only decrease `F`.

**4. Correction of a recurring ledger error.** Several fronts used "Fredman's `n−log₂n−O(1)` additive *lower* bound." Fredman's `log e(P)+O(n)` is an *upper* bound on comparisons; read as an all-n lower bound it contradicts Sergeev for all large `n`. (I tightened one accompanying `n=10` remark on the board to the unconditional asymptotic contradiction.)

## Honest limit
I did **not** prove either horn, nor find a counterexample family. The contribution is a precise no-transfer obstruction, two verified non-transfer counterexamples, a closed-off rounding route, and the model-fidelity correction that the front's complexity consequence is invalid. Proving the first horn needs an explicit `O(log n)`-surplus sorting construction (a major strengthening of Sergeev); proving the second needs a new lower-bound mechanism forcing `Ω(log n)` bias along every balanced path.
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

## Other metadata

```json
{
  "finished_at": 1794152900.6039999,
  "started_at": 1794151994.3765314
}
```
