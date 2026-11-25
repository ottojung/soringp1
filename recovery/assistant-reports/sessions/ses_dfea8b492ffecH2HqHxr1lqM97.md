# antonina-uqpbLxMlP3iV1GHQ35btdv-fighting

Session: ses_dfea8b492ffecH2HqHxr1lqM97
Workspace: /home/lubko/soring-fronts/non-tight-infinitely-often-alln
Created: 1795318828025; updated: 1795319351572

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 57 (msg_20158e4db001926S89ICOa8fre)

Let me inspect the relevant docs on tightness and the information bound, and check git state.


## Output 85 (msg_20159165f001JVFD9jnbBhjsQs)

Let me look at the specific fronts related to tightness/density-zero on board #301.


## Output 126 (msg_20159591e001yDz50FZNkzVlkk)

Now let me look at the available scripts and the key docs on structural lower bounds and the plan.


## Output 154 (msg_20159e16b001z8nMqHK2thM0h8)

Let me check the evaluation scripts and verify known values, then examine key structural docs.


## Output 210 (msg_2015cba34001X9a0UrfANsUAXw)

Let me check a few more relevant docs and the board digest for the specific front.


## Output 292 (msg_2015dd350001Mzru2LNAHYc0vL)

Now I have a thorough understanding. Let me verify the n=28 non-tight claim precisely and do a final computational check.


## Output 312 (msg_2015e2d4a001hBDujYwRs4zfhN)

Let me try to assess the computational feasibility of extending known values.


## Output 323 (msg_2015ee5ad001mnm0b8vk0z8hz4)

Now I have a comprehensive understanding of the problem. Let me compile my findings.

---

## Research Report: Information-Tightness of S(n) — Infinitely Often?

### 1. What I studied

- **AGENTS.md** — research contract: unary encoding, `SORT-BOUND-U`, no unconditional super-polynomial lower bounds; realistic frontier is upper bounds, barriers, structural theorems.
- **docs/problem.md** — model: deterministic adaptive comparison decision trees; `S(n)` = min worst-case height; `SORT-BOUND-U = {1^n # 1^k : S(n) ≤ k}`; information bound `ceil(log2 n!) ≤ S(n)`; exact `S(n)` known for n ≤ 6 (kernel-checked), n ≤ 22 (literature).
- **docs/literature.md** — primary sources: Wells (S(12)=30), Stober–Weiß ALENEX 2023 (S(16)=46, S(17)=50, S(18)=54, S(28)≥99), Peczarski, Knuth TAOCP.
- **docs/research-n12-nontightness.md** — audit of why S(12)>29; falsification of 5 scalar invariants (slack ratio, monotone-in-e, local tightness, forced prefix, symmetry).
- **docs/research-certificates-barriers.md** — `SORT-BOUND-U ∈ PSPACE`, sparse, no NP-hardness unless P=NP; explicit tree witness has `2·n!−1` nodes (not poly-size).
- **docs/research-sergeev-asymptotic.md** — Sergeev TR20-096: `S(n) − log2(n!) = O(n/(log n)^(1/5)) = o(n)`.
- **docs/research-structural-lower-bounds.md** — ordinal-sum/merge-factor compositional bound; smallest strict witness `Merge(2,4)` at n=6.
- **docs/research-one-ply-obstruction.md** — one-ply bound `L1` with `L0 ≤ L1 ≤ F`; strict witness at n=5 (`e=8, m=4`); ordinal-sum suffix gives strict witnesses at every n ≥ 5 (poset-level, not antichain).
- **Board #301 digest** — `tightness-density-zero-alln` front (limsup density of tight n = 0; both horns unattained); `S(23)` open; exact values end at n=22 (OEIS A036604, independently verified by Viche Executive).

---

### 2. The precise claim

**FRONT:** Are there infinitely many integers `n` such that `S(n) > ceil(log2 n!)`?

**Negation (eventual tightness):** `S(n) = ceil(log2 n!)` for all sufficiently large `n`.

**FALSIFIER horns:** (a) prove eventual tightness, or (b) construct/verify the first non-tight case beyond n=22 **plus** an infinite family with excess ≥ 1.

---

### 3. Known data (verified)

| n | S(n) | C(n)=ceil(log2 n!) | tight? | excess | source |
|---|------|---------------------|--------|--------|--------|
| 1–11 | = C(n) | various | yes | 0 | literature |
| 12–19 | C(n)+1 | various | no | +1 | Wells, Peczarski, Stober–Weiß |
| 20 | 62 | 62 | yes | 0 | Stober–Weiß |
| 21 | 66 | 66 | yes | 0 | Stober–Weiß |
| 22 | 71 | 70 | no | +1 | Stober–Weiß |
| 23–27 | open | 75–94 | unknown | — | open |
| 28 | ≥ 99 | 98 | **no** | ≥ +1 | Stober–Weiß |

**New confirmation beyond n=22:** `S(28) ≥ 99` (Stober–Weiß, exhaustive bidirectional search, ~89 hrs on 48-thread/768GB machine) and `C(28) = 98`, so `S(28) > C(28)`. This is a non-tight case beyond n=22. `S(23)` through `S(27)` remain open; no exact `S(n)` is known for any `n` in `23..27` (confirmed via OEIS A036604, which ends at a(22)=71).

Ford–Johnson upper bound `FJ(n) = Σ ceil(log2(3k/4))`:
- `FJ(20)=62=C(20)`, `FJ(21)=66=C(21)` (tight, achieved)
- `FJ(22)=71 > C(22)=70`, `FJ(23)=76 > C(23)=75`, `FJ(24)=81 > C(24)=80`, `FJ(28)=101 > C(28)=98`
- FJ does **not** achieve the information bound at any `n ≥ 12` except the isolated tight cases n=20,21 (where FJ happens to equal C).

---

### 4. Approaches attempted and why they fail

**Horn (a): Prove eventual tightness `S(n)=C(n)` for all large n.**

This would require a general sorting algorithm achieving `ceil(log2 n!)` comparisons for all sufficiently large `n`.
- Ford–Johnson (merge-insertion) achieves `FJ(n) = n log2 n − 1.329n + O(log n)`, while `C(n) = n log2 n − 1.443n + O(log n)`. The gap is `~0.114n` — linear, not zero. FJ does **not** achieve `C(n)` at any `n ≥ 12` except n=20,21 (coincidence, verified by exhaustive search).
- Sergeev's bound is `C(n) + o(n)` — sublinear excess, but not zero excess.
- No construction is known that achieves `C(n)` for any infinite family of `n`. The only tight cases ≥ 12 are n=20,21, established by exhaustive search, not by a general method.
- **Result: Horn (a) cannot be established with current techniques.**

**Horn (b): First non-tight beyond n=22 + infinite family with excess ≥ 1.**

- First non-tight beyond n=22: `n=28` is confirmed (`S(28) ≥ 99 > 98 = C(28)`). But we do **not** know whether n=23, 24, 25, 26, or 27 is non-tight — those values are open.
- Infinite family: to verify any member beyond n=28 requires computing `S(n)` exactly, which is infeasible (naive minimax times out at n=7; published computations for n≤22 took days on large machines; n=28 took 89 hours). No structural lower-bound technique can show `S(n) > C(n)` without computing `S(n)`.
- **Result: Horn (b) cannot be established — no infinite family is verifiable.**

**Other falsification attempts (all blocked):**

1. **Slack-ratio threshold** (H1 from n12-nontightness): falsified — `n=5` tight with ratio 1.067, `n=12` non-tight with 1.121, `n=20` tight with 1.896, `n=22` non-tight with 1.050. Slack does not predict tightness.
2. **Monotonicity propagation**: tightness is **not monotone** — `S(20)=C(20)`, `S(21)=C(21)`, but `S(22)>C(22)`; `S(28)>C(28)` but we don't know about 23–27. No propagation argument works.
3. **Power-of-two families**: `2^k` tight for k≤3 (2,4,8), non-tight at 16; `2^k+1` tight at 3,5,9, non-tight at 17; `2^k−1` tight at 3,7, non-tight at 15. No consistent family.
4. **Ordinal-sum / direct-sum lifting** (research-structural-lower-bounds, research-one-ply-obstruction): poset-level strict witnesses (`Merge(2,4)`, one-ply `W`) exist, but they bound `F(P)` for specific posets `P`, not `S(n)` for the antichain. `F(P) > ceil(log2 e(P))` does **not** imply `S(n) > C(n)` because `e(P) ≤ n!` and `C(n)` grows much faster than `ceil(log2 e(P))` as we add elements.
5. **Structural lower bound (Theorem B)**: gives `F(P) ≥ Σ ceil(log2 e(P_i)) + Σ delta_i`, but for the antichain there's one block (not a Merge), so `delta=0` and the bound reduces to `ceil(log2 n!) = C(n)`. No improvement.
6. **One-ply bound `L1`**: at the antichain root, every comparison splits `n!` evenly (`n!/2` each), so `L1(A_n) = C(n)`. The obstruction must occur deeper, which is exactly the exhaustive-search problem.

---

### 5. Exact obstructions

**Obstruction 1 — Computational barrier.** `S(n)` is exactly known only for `n ≤ 22` (plus `S(28) ≥ 99`). `S(23)`–`S(27)` are open. The backward/forward poset search for n=23 hits a wall at level 3 (~21M states, level 4 projected at ~3×10⁹). No feasible computation can verify any specific `n` in `23..27` or beyond 28. **Consequence:** we cannot verify the first non-tight case beyond n=22 (it could be 23, 24, 25, 26, 27, or 28), and we cannot verify any member of a candidate infinite family.

**Obstruction 2 — No general tightness construction.** No sorting algorithm achieves `ceil(log2 n!)` for any `n ≥ 12` except the isolated tight cases n=20,21 (established by exhaustive search). Ford–Johnson has linear excess; Sergeev has sublinear but nonzero excess. **Consequence:** eventual tightness cannot be proved by exhibiting a construction.

**Obstruction 3 — No general non-tightness lower bound.** Every known non-tight case (12–19, 22, 28) required individual exhaustive computation of `S(n)`. There is no technique to show `S(n) > C(n)` for any infinite family without computing each `S(n)`. **Consequence:** infinite non-tightness cannot be proved.

**Obstruction 4 — Non-monotonicity.** Tightness is not monotone in `n` (tight at 20,21; non-tight at 22, 28). No propagation from one `n` to another is possible.

**Obstruction 5 — Certificate soundness vs completeness.** A sound certificate for `S(n) ≤ k` (exhibit a sorting tree) has `2·n!−1` nodes — exponential in the unary input length, so it is not a polynomial-size certificate. No complete (succinct) certificate for `S(n) > k` is known. The information bound `log2 e(P)` is sound but incomplete (poset-level counterexamples at n=5,6). **Consequence:** we cannot even succinctly certify either direction for large `n`.

---

### 6. Honest conclusion

**The question is open.** Neither horn of the falsifier is established:

- **Eventual tightness** (`S(n) = ceil(log2 n!)` for all sufficiently large `n`): cannot be proved — no construction achieves the information bound for any infinite family, and the best known upper bounds (Ford–Johnson, Sergeev) have nonzero excess.
- **Infinite non-tightness**: cannot be proved — `S(n)` is only known exactly for `n ≤ 22` (plus `S(28) ≥ 99`), and no structural lower-bound technique can show `S(n) > C(n)` without computing `S(n)`.

**Concrete finding:** `n=28` is confirmed non-tight (`S(28) ≥ 99 > 98 = C(28)`), extending known non-tight cases beyond n=22. But `S(23)`–`S(27)` are unknown, so we cannot identify the *first* non-tight case beyond n=22, and no infinite family with excess ≥ 1 is verifiable.

**Next decisive obstacle:** either (i) compute `S(23)` (or show `S(23) > 75` or `S(23) = 75`), or (ii) develop a structural lower-bound technique that proves `S(n) > C(n)` for some `n` without exhaustive computation, or (iii) develop a sorting algorithm achieving `C(n)` for an infinite family. All three are beyond current reach — this is a genuine open problem in comparison-sorting complexity.

No repository changes, Lean formalizations, or commits are warranted: there is no genuinely substantive, independently checkable new theorem or counterexample to integrate. All work was read-only analysis on billy-dev; working tree remains clean at `6a96398` (branch `billy-dev`).
