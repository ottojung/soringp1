# info-tightness-set-complexity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

SPlcZ0YRiZ3kGcveGcAksb-sends

## exit_state

clearexit

## question

Is the information-tightness set T = {1^n : S(n) = ceil(log2 n!)} decidable by a uniform polynomial-time algorithm, or is T as hard as exact S(n), so that even the zero-excess indicator encodes the full evaluation difficulty?

## basis

Exact values give E(n) in {0,1} for n<=22, with E=0 at n<=11,20,21; Sergeev gives E(n)=o(n); board #301 supplies the excess and tightness threads; a ledger scan found no front on the complexity of the tightness set itself, only on its infinitude or density.

## falsifier

A uniform polynomial-time decider for T on all n, or a polynomial-time Turing reduction from S_unary to T; either settles the stated dichotomy.

## implication

Membership of T in P would be a new uniform upper bound and the first efficiently decidable piece of the excess; equivalence to S would rule out 'decide zero excess, then refine' algorithms and show that the sign of E(n) already carries the exact-evaluation difficulty.

## finding_unverified

on.** `T ≤_T^p S_unary` always: compute `S(n)` and compare with `C(n)`. Thus `T` is never harder than exact `S`; the open direction is `S_unary ≤_T^p T`.

2. **`E(n)∈{0,1}` implies the hardness horn.** If `E(n)` is always `0` or `1`, then
   `S(n)=C(n)+1_{n∉T}`.
   One query to `T` computes `S(n)`, so `T ≡_T^p S`, and `T∈P` iff `S_unary∈FP`. Under this regime a polynomial-time decider for `T` would not be a weaker upper bound—it would compute `S` exactly. All exact values `n≤22` satisfy `E∈{0,1}`, and the Stober–Weiß range table through `n=47` has no certified lower bound `C+2` (the largest certified gap is `S(28)≥99=C(28)+1`). So `E≤1` is consistent with every published value/range.

3. **The sign pattern alone does not determine `E`.** There are two profiles matching the actual values on `n≤22`, satisfying the information bound, monotonicity, the insertion bound `S(n+1)≤S(n)+ceil(log₂(n+1))`, Sergeev’s `S(n)=log₂(n!)+o(n)`, and the published ranges through 47, with the *same* `T={1,…,11,20,21}`:
   - `S₁=C+1`, which is in `FP`;
   - `S₂=C+E₂`, where `E₂=1` on `23≤n≤47` and then increases only at “cheap” steps `d_n=floor(log₂(n+1))`, with `E₂=o(n)` and a sparse increment set encoding a unary PSPACE set. Conditional on `P≠PSPACE`, `S₂∈FPSPACE\FP`, while `T` is finite and in `P`.
   
   Thus a trivial `T` does not force `S` to be easy, and no argument using only the established constraints can prove `T≡S`. The missing ingredient is `S`-specific, most naturally `E≤1`.

4. **Obstruction to “decide zero excess, then refine.”** `T` gives one bit per `n`. Even if `T∈P` has bounded gaps `B`, the increment rule `E(n+1)-E(n)≤1` only yields `E(n)≤n-t(n)`, where `t(n)` is the last tight index. That gives an additive `B` approximation, not exact excess for `B≥2`. Two `E`-profiles with the same zero set and `E≤2` but different values at a nonzero position show the zeros alone do not refine the excess.

**Honest limits.** This does not prove `T∈P`, `T∉P`, or `S_unary≤_T^p T` for the actual `S`. It shows the front’s hardness alternative is not a consequence of current data and, in the `E≤1` regime, is just exact evaluation. General-poset hardness and certificate **soundness** were kept separate from **completeness**; neither transfers to the antichain. No Lean or repository changes were made; the worktree is clean. I posted one concise obstacle note to board #301, verified through the digest.
Recovery audit complete.

**Effects that actually happened (verified)**
- **Board #301:** exactly one comment was posted, at `2026-11-08T17:17:25.944Z`, author `SoringP1 frontier: info-tightness-set-complexity`. The digest shows one unique match; no duplicate was made.
- **Repository:** worktree is clean at commit `6a96398`; no modified/untracked files, no diff, no new commit.
- **Local scratch:** only `/tmp/opencode/board_post.txt` and `/tmp/opencode/board_post_result.json` were created outside the repository.
- **Ledger:** the `info-tightness-set-complexity` front still shows `status: running`, `exit_state: null`, `finding_unverified: null`. I did not modify it; that record is left for the keeper/review process.

**Not repeated**
- I did not re-run the research, re-post to #301, create a commit, or edit the repository or ledger.

**Uncertain effects**
- None identified. The only external mathematical communication is the single verified board comment.

The mathematical work from the previous turn was completed and reported; no further side effects are required.

## Other metadata

```json
{
  "finished_at": 1794158331.0910072,
  "started_at": 1794157709.9073265
}
```
