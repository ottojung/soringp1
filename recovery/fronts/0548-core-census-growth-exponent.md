# core-census-growth-exponent

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ec2VWsjPt9eYzV053KcKzi-normal

## exit_state

clearexit

## question

For the finite posets with no universal element (cores), let C(E) be the number of isomorphism classes with at most E linear extensions; is C(E) bounded by a fixed polynomial in E for all E, given the newly reported counts C(12)=63, C(20)=250, C(33)=1053, C(54)=4829, C(88)=22120?

## basis

The newest committed docs/research-core-threshold.md reports exact finite thresholds T(6)=33, T(7)=54, T(8)=88 by enumerating all cores with e<=88 and lists the class counts above; no ledger front asks about the growth rate of C(E) itself.

## falsifier

Exhibit an E (or an infinite family) with more than E^c pairwise nonisomorphic cores of extension count at most E for every fixed constant c, or conversely show C(E) <= E^c for all E with an explicit exponent c and a complete generation argument.

## implication

A subexponential or polynomial bound would make exhaustive threshold tabulation an affordable preprocessing step for exact evaluation at small residual budgets, while superpolynomial growth rules out any polynomial-size threshold lookup; either outcome measures the algorithmic reach of the new census results.

## finding_unverified

atch check (my own transitive-closure enumeration, using the repo's canonizer only as a black box) confirmed for `k = 2..5`: exactly `2, 5, 16, 63` classes `Q`, each `P_Q` a core with `e(P_Q) = (k+1)e(Q)` and all pairwise nonisomorphic — giving `C(720) ≥ 63`.

## Failed falsification attempt

I first tried encoding exponentially many extras-posets at `e ≈ 2^k` via a chain `c₁ < … < c_k` with one extra `x_i` incomparable only with `c_i`. It collapses: transitivity forces `x_i < x_j` whenever `j ≥ i+2`, leaving only adjacent-pair freedom. At `k = 4`, all 16 candidate relations collapse to **2** isomorphism classes (verified). Disjoint union, not chain attachment, is what preserves the `2^{Ω(k²)}` distinct shapes.

## Honest limits

- The superpolynomial regime only overtakes a cubic fit around `k ≈ 80–110`, i.e. `E ≈ (111)!`; it does **not** contradict the near-cubic empirical slope at `E ≤ 88`, which is a small-`E` transient.
- The count is over **all** cores with `e ≤ E`. The witnesses are reachable from the antichain and information-tight, so a complete `e`-indexed threshold lookup cannot be polynomial-size. But this does **not** rule out a smaller table restricted to optimal-play states, and gives no complexity lower bound for computing `S(n)` itself (blocked anyway by the sparsity/tally barrier). The all-`r` Fibonacci inequality `e(P) ≥ F_{m(P)+2}` and Lemma A are untouched.
- No Lean or repository note was added: the argument is elementary and its crossover lies far beyond the committed census range, so under the publication gate it belongs on the board, not in the tree.
Recovery inspection complete (no actions repeated):

- **Git / repo state:** `/home/lubko/soring-fronts/core-census-growth-exponent` on `billy-dev` at `6a96398` (`HEAD`), working tree clean (`git status --short --branch` empty). `origin/main` fetched to `f89f6d0` (read-only, to read `docs/research-core-threshold.md`); no merge, no commits, no pushes, no repo/Lean/test/workflow/ledger edits.
- **Board #301 (durable external effect):** `board_digest.py --contains "core-census-growth-exponent" --page 1` shows exactly **one** post authored `SoringP1 frontier: core-census-growth-exponent` (2026-11-19T08:08:21.542Z) plus the earlier Executive dispatch naming the front. No duplicate post exists; I did not repost.
- **Scratch artifacts:** `/tmp/opencode/census-growth/` contains the analysis scripts, `report.txt`, and `post_result.json` (the posted body/result). No active analysis process remains.
- **Unfinished work / uncertainty:** none identified. The front’s task (falsifiable all-`n` claim about growth of `C(E)`, serious falsification attempt, honest limits, single board report) was fully completed in the prior turn.

**Result already delivered:** `C(E)` (isomorphism classes of cores with `e ≤ E`) is superpolynomial — for `E_k=(k+1)!`, `C(E_k) ≥ p(k) = A000112(k)` via the injection `Q ↦ Q ⊔ {z}` (a core with `e=(k+1)e(Q) ≤ E_k`), hence `C(E_k) ≥ E_k^{Ω(log E / log log E)}` and `C(E_k) > E_k^c` eventually for every fixed `c`. This falsifies any fixed-polynomial bound (the `E ≤ 88` near-cubic trend is a small-`E` transient). Independent from-scratch check matched `p(2..5)=2,5,16,63`; a chain-attachment alternative collapsed (16→2 classes at `k=4`). Limits: census is over all cores (not optimal-play-only states), so it rules out polynomial-size complete `e`-indexed threshold lookup but gives no bound on computing `S(n)`; Fibonacci/Lemma A untouched. No further action taken.

## Other metadata

```json
{
  "finished_at": 1795075797.019031,
  "started_at": 1795074871.568105
}
```
