# antonina-EEmgDfEUIQklDBZkfhIEHv-confirm

Session: ses_e03e23207ffeFKKrfQdHK7rwxy
Workspace: /home/lubko/soring-fronts/excess-vs-log-bound-alln
Created: 1795231174164; updated: 1795233850925

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 48 (msg_1fc20f530001YuilI10B2W2Yub)

I'm on billy-dev, good. Let me study the model, the certified data, and the board context.

## Output 71 (msg_1fc255d49001QXyy0sl7bjRAJI)

I'm on billy-dev. I've now read the model (`SoringP1/Model.lean`: leaves return the sorted *sequence of input positions*, so the tree must have ≥ n! leaves and `S(n) ≥ ceil(log2 n!)`), the board digest (front `excess-at-most-one-alln`, open), and the literature. Next: the full board, the frontier ledger status, certified values through 22, and the Stober–Weiss primary source.

## Output 244 (msg_1fc466a080012C8KWYn3YoJ1C6)

# Report: attack on the claim `e(n) = S(n) − C(n) ≤ ⌈log₂(n+2)⌉` for all `n ≥ 2`

**Environment:** billy-dev (verified via `hostname`), repo at `6a96398`, worktree clean. No Lean/repository changes made (no substantive theorem or counterexample found). No board posts or commits performed.

## 1. Claim tested

**Front (user):** For every `n ≥ 2`, the certified excess `e(n) = S(n) − C(n)` satisfies `e(n) ≤ ⌈log₂(n+2)⌉`, i.e. the gap grows at most one bit per level.

Where `C(n) = ⌈log₂ n!⌉` (the information-theoretic lower bound; `SoringP1/LowerBound.lean` certifies `S n ≥ log₂(n!)`).

**Falsifier:** a certified `n` with `e(n) > ⌈log₂(n+2)⌉`.

## 2. Distinguishing general-poset results from the `S(n)` family

- The claim is specifically about the **antichain family** `A_n` (`S(n) = m(A_n)`), not about arbitrary posets.
- General-poset results that do **not** settle this claim: the disjoint-union defect `F(A⊔B) ≥ F(A)+F(B)+min(|A|,|B|)+1` (board `exec-du-asymmetric-structured-search-20261121`); the merge-family `M(a,b)` excess over the tape bound (`research-n12-nontightness.md` §7, H7); Hanamura–Iwata's `e=7` local tightness (single-instance poset sorting). These are about the game `m(P)` on general posets, not about the fixed family `S(n)`.
- **Certificate soundness vs. completeness:** the board front `increment-log-upper-alln` (`S(n+1)−S(n) ≤ ⌈log₂(n+1)⌉`) is a *sound* paper proof (binary insertion + the insertion game bound `⌈log₂(n+1)⌉`) and is **not** a completeness route to the user's claim: telescoping gives `S(n) ≤ 1 + Σ_{k=3}^n ⌈log₂ k⌉`, i.e. `e(n) ≤ n + O(1)` — much weaker than `⌈log₂(n+2)⌉`. The user's claim needs the *optimal* tree to stay near the information bound, which is a global statement.

## 3. Data verification

Computed `C(n) = ⌈log₂ n!⌉` for `n = 2..22` and compared with the board #301 certified data (user's evidence: `e(n) = 0` on `{2..11, 20, 21}`, `e(n) ≤ 1` on `{12..19, 22}`):

| n | C(n) | bound `⌈log₂(n+2)⌉` | e(n) (board) | claim holds? |
|---|---|---|---|---|
| 2–11 | … | 2–4 | 0 | ✓ |
| 12–19 | … | 4–5 | 1 | ✓ |
| 20 | 62 | 5 | 0 | ✓ |
| 21 | 66 | 5 | 0 | ✓ |
| 22 | 70 | 5 | 1 | ✓ |

Every certified `n ≤ 22` satisfies the claim with room (bound ≥ 2 > e ≤ 1). The claim is also consistent with:
- Stober–Weiss ALENEX 2023: `S(16)=46` (C(16)=45, e=1), `S(17)=50` (C(17)=49, e=1), `S(18)=54` (C(18)=53, e=1); `S(28) ≥ 99` (C(28)=98, e≥1 ≤ bound 5).
- Wells 1966/1971: `S(12)=30` (C(12)=29, e=1, bound 4).
- Manacher 1979 (board digest): `S(47) ∈ {198,199,200}`; `C(47)=198` → `e(47) ∈ {0,1,2} ≤ bound 6.

**No counterexample in any certified data I can reach.**

## 4. Literature consulted

- Stober–Weiß, *Lower Bounds for Sorting 16, 17, and 18 Elements*, ALENEX 2023 (arXiv:2206.05597) — primary source for `S(16)=46, S(17)=50, S(18)=54` and `S(28) ≥ 99`.
- Wells 1966/1971 — `S(12)=30 > C(12)=29`.
- Peczarski 2012 — `S(7)=13, S(8)=16, S(12)=30`; structural non-tightness discussion.
- Knuth, TAOCP Vol. 3 §5.3.1.
- Ford–Johnson 1959 (merge-insertion).
- `docs/literature.md` (project baseline).

## 5. Disproof attempts (concrete)

1. **Certified data through 22:** `e ≤ 1` there; the bound is `≥ 2` for `n ≥ 2`, so the claim holds trivially. No violation possible.
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
