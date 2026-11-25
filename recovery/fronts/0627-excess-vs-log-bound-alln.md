# excess-vs-log-bound-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

EEmgDfEUIQklDBZkfhIEHv-confirm

## exit_state

clearexit

## question

Prove or refute: for every n >= 2, the certified excess e(n) = S(n) - C(n) satisfies e(n) <= ceil(log2(n+2)), so the gap grows at most one bit per level.

## basis

Certified data through 22: e(n) <= 1 on {12..19, 22}, e = 0 on {2..11, 20, 21}; FJ-C = 3 at n = 28 (A001768 a(28)=101 vs A003070 a(28)=98); board #301: 'FJ-C = 3 at 28, first 2 at 25'.

## falsifier

A certified n with e(n) > ceil(log2(n+2)), i.e., a sorting tree or adversary bound with S(n) >= C(n) + ceil(log2(n+2)) + 1.

## implication

A logarithmic excess bound would give cheap certificate-arithmetic bounds for bounded-excess constructions in SORT-BOUND-U.

## finding_unverified

 `e ≤ 1` there; the bound is `≥ 2` for `n ≥ 2`, so the claim holds trivially. No violation possible.
2. **Extend beyond 22:** computing optimal `S(n)` via the poset-minimax DP (A001035 state space: 3, 19, 219, 4231, 130023, 6.1M for `n = 2..7`) is infeasible in this environment beyond `n ≈ 6`. No new certified values obtained.
3. **Literature beyond 22:** the board reports `FJ-C = 3` at `n = 28` (Ford–Johnson, not optimal `S`); `S(28) ≥ 99` gives `e(28) ≥ 1 ≤ bound 5`. No counterexample known; the board front `excess-at-most-one-alln` claims no certified `S(n) ≥ C(n)+2` anywhere.

## 6. Proof attempt (concrete failed approach)

**Route:** induction on `n` via the minimax recurrence `S(n) = F(A_n) = 1 + F(A_n + ij)`, where `A_n + ij` is the antichain plus one relation `i < j`, which is the disjoint union `A_{n−2} ⊔ C_2`.

- **Base cases** `n = 2, 3, 4`: verified (`S(2)=1, S(3)=3, S(4)=5`).
- **Arithmetic:** `C(n) − C(n−2) ≥ 3` for `n ≥ 3` (verified numerically through `n = 30`), so the induction would close *if* `F(A_m ⊔ C_2) ≤ F(A_m) + δ(m)` with `δ(m) ≤ D(m) = C(m+2) − C(m) + (⌈log₂(m+4)⌉ − ⌈log₂(m+2)⌉) − 1`.
- **Obstruction (the missing lemma):** the key step is `F(A_m ⊔ C_2) ≤ F(A_m) + 2`. **This lemma is false:**
  - `m = 2`: `F(A_2 ⊔ C_2) = 4` (computed), `F(A_2) = S(2) = 1` → `4 ≰ 3`.
  - `m = 3`: `F(A_3 ⊔ C_2) = 6`, `F(A_3) = 3` → `6 ≰ 5`.
  - `m = 4`: `F(A_4 ⊔ C_2) = 9`, `F(A_4) = 5` → `9 ≰ 7`.
  
  The actual excess `δ(m) = F(A_m ⊔ C_2) − S(m)` is `3, 3, 4, …` (computed through `m = 4`), while the induction's tolerance is `D(m) = 4, 3, 4, …`. So the induction is **tight** at `m = 3, 4` (`δ = D`) and would require `δ(m) ≤ D(m)` for all `m`. I could not prove this, and computing `δ(5)` (7-element poset DP, 6.1M state space) was infeasible in pure Python within the available time.

- **Classical insertion bound:** `S(n) ≤ log₂(n!) + n` (binary insertion) gives `e(n) ≤ n + O(1)`, which does **not** prove `≤ ⌈log₂(n+2)⌉`.

## 7. Honest limits

- I did **not** prove or refute the all-`n` claim. The claim is consistent with all certified data I can access (through 22, plus `S(28) ≥ 99` and `S(47) ∈ {198,199,200}`).
- The claim is a **strict weakening** of the board front `excess-at-most-one-alln` (`e(n) ≤ 1`), since `⌈log₂(n+2)⌉ ≥ 2` for `n ≥ 2`: if the stronger front is ever proved, the user's claim follows trivially. Conversely, a counterexample to the user's claim would require `e(n) ≥ ⌈log₂(n+2)⌉ + 1`, i.e. excess at least `~log n`, which is far beyond the certified `e ≤ 1` and the board's `FJ-C = 3 at 28` (Ford–Johnson, not optimal `S`).
- The exact obstruction for a direct proof: the lemma `δ(m) ≤ D(m)` (equivalently `F(A_m ⊔ C_2) ≤ F(A_m) + (C(m+2)−C(m)) + (⌈log₂(m+4)⌉ − ⌈log₂(m+2)⌉) − 1`) is unproven; my induction is tight at `m = 3, 4`.
- No Lean or repository changes were made.

## 8. Conclusion

**Mathematical finding:** The claim `e(n) ≤ ⌈log₂(n+2)⌉` for all `n ≥ 2` is **not refuted** by any certified data through 22 (and consistent with the 28 and 47 data). It is **implied by** the stronger open board front `excess-at-most-one-alln`. I could not prove it directly: the natural induction is blocked by the unproven lemma `δ(m) ≤ D(m)`, with `δ(2)=3, δ(3)=3, δ(4)=4` and `D(2)=4, D(3)=3, D(4)=4` (tight at 3, 4). The classical insertion bound only gives `e(n) ≤ n + O(1)`, not `≤ ⌈log₂(n+2)⌉`. **I did not prove or refute the all-`n` claim; the exact obstruction is the missing lemma plus the absence of certified data beyond 22.**

## Other metadata

```json
{
  "finished_at": 1795233883.8072312,
  "started_at": 1795231173.651623
}
```
