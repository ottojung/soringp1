# antonina-rCQMA8p3EAVhFcr0UG4xqm-breakfast

Session: ses_e464e7ad4ffeoxjieIkqNM7oc1
Workspace: /home/lubko/soring-fronts/dimension-two-fibonacci-threshold
Created: 1794116781357; updated: 1794118634157

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 446 (msg_1b9cd18de001Yw24rYVEz3qbxK)

## Report: dimension-two Fibonacci threshold

**Verdict: HOLDS-TO-8** (exhaustive over all isomorphism classes of posets of order dimension ≤ 2 on at most 8 elements). No counterexample found. The all-`n` statement is **not settled**; the width-two proof does not extend verbatim.

No tracked files were edited, no commit/push/merge was made, and nothing was posted to the board. The worktree is clean at `f89f6d0`.

---

### 1. Enumeration method

Every poset of dimension ≤ 2 is, by definition, an intersection of two linear orders:
`P = L1 ∩ L2`. Relabelling by `L1` puts it in the form

    P ≅ (identity order) ∩ σ,   σ ∈ S_n.

Conversely every such intersection has dimension ≤ 2. I therefore enumerated all `σ ∈ S_n`, formed the corresponding poset, and deduplicated by an isomorphism-canonical form. This is complete for dimension ≤ 2 up to isomorphism.

Counts obtained:

| n | dim ≤ 2 classes | all unlabeled posets |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 5 | 5 |
| 4 | 16 | 16 |
| 5 | 63 | 63 |
| 6 | 315 | 318 |
| 7 | 1956 | 2045 |
| 8 | 14794 | 16999 |

For `n ≤ 5` every poset has dimension ≤ 2. At `n = 6` there are 3 classes outside the class; at `n = 7`, 89; at `n = 8`, 2205.

---

### 2. Exact `e` and `m` for `n ≤ 6`

`e` was counted by direct linear-extension enumeration. `m` was computed by exact minimax on extension states, and independently cross-checked against the relation-state minimax routine; all 402 values agreed.

#### Minimum `e` for each exact `m`

Entries are indexed by `m = 0,1,2,...`.

| n | min `e` by `m` |
|---:|---|
| 1 | 1 |
| 2 | 1, 2 |
| 3 | 1, 2, 3, 6 |
| 4 | 1, 2, 3, 5, 12, 24 |
| 5 | 1, 2, 3, 5, 8, 18, 40, 120 |
| 6 | 1, 2, 3, 5, 8, 13, 30, 57, 120, 240, 720 |

Compare with

    F_{m+2} = 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

Every entry is at least `F_{m+2}`. For example, at `n = 6` the potentially dangerous values are `m = 6,7,8,9,10`, where the minimum `e` is `30,57,120,240,720`, all above `21,34,55,89,144`.

#### Exact `m` histograms

| n | classes | max `e` | `m` histogram |
|---:|---:|---:|---|
| 1 | 1 | 1 | `{0:1}` |
| 2 | 2 | 2 | `{0:1, 1:1}` |
| 3 | 5 | 6 | `{0:1, 1:2, 2:1, 3:1}` |
| 4 | 16 | 24 | `{0:1, 1:3, 2:4, 3:6, 4:1, 5:1}` |
| 5 | 63 | 120 | `{0:1, 1:4, 2:8, 3:16, 4:18, 5:12, 6:3, 7:1}` |
| 6 | 315 | 720 | `{0:1, 1:5, 2:13, 3:32, 4:63, 5:81, 6:68, 7:38, 8:10, 9:3, 10:1}` |

**Violations for `n ≤ 6`: 0 out of 402 classes.**

---

### 3. Checks at `n = 7` and `n = 8`

For larger `n` I did not need full exact `m` everywhere. For each class I computed the largest `r` with `F_{r+2} ≤ e`; then:

- if the state is sortable within `r` comparisons, then `m ≤ r`, hence `e ≥ F_{r+2} ≥ F_{m+2}`;
- if it is not sortable within `r`, then `m > r`; since `e < F_{r+3}`, this is an immediate violation.

Thus the bounded minimax decision is exact for the threshold test. Large-`e` classes were discharged by elementary merge-sort upper bounds: `m ≤ 14` for `n=7`, `m ≤ 17` for `n=8`.

| n | dim ≤ 2 classes | exact `m` | threshold decision | safe by upper bound | violations |
|---:|---:|---:|---:|---:|---:|
| 7 | 1956 | 1929 classes, `e < 610` | 17 classes, `610 ≤ e < 987`, checked at `r=13` | 10 classes, `e ≥ 987`, using `m ≤ 14` | 0 |
| 8 | 14794 | — | 14675 classes, `e < 2584`; 81 classes, `2584 ≤ e < 4181`, checked at `r=16` | 38 classes, `e ≥ 4181`, using `m ≤ 17` | 0 |

So:

- **`n = 7`: 0 violations among all 1956 dimension-2 classes.**
- **`n = 8`: 0 violations among all 14794 dimension-2 classes.**

The `n=8` computation covers every dimension-2 class: `14675 + 81 + 38 = 14794`.

---

### 4. GPC two-comparison inequality on the tested class

I checked the derived form used in the width-two note: there is a first comparison splitting a state into sizes `a ≥ b`, and a second comparison inside the `a`-child whose two grandchildren both have size at most `b`.

| n | classes | trivial (`e ≤ 2`, at most one comparison needed) | nontrivial with GPC witness |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 |
| 2 | 2 | 2 | 0 |
| 3 | 5 | 3 | 2 |
| 4 | 16 | 4 | 12 |
| 5 | 63 | 5 | 58 |
| 6 | 315 | 6 | 309 |
| **total** | **402** | **21** | **381** |

**No GPC failure in the dimension-2 class for `n ≤ 6`.** Since Peczarski's 2006 paper also proves GPC for posets with at most 11 elements, GPC itself is not the obstruction in this finite range. The obstruction is the closure failure described below.

---

### 5. Staircase family `W_n`

Define `W_n` on `0,...,n-1` by `i > j` iff `j ≤ i-2`. It has width 2, hence dimension ≤ 2. Verified.

| n | `e(W_n)` | `m(W_n)` | `F_{m+2}` |
|---:|---:|---:|---:|
| 2 | 2 | 1 | 2 |
| 3 | 3 | 2 | 3 |
| 4 | 5 | 3 | 5 |
| 5 | 8 | 4 | 8 |
| 6 | 13 | 5 | 13 |
| 7 | 21 | 6 | 21 |
| 8 | 34 | 7 | 34 |
| 9 | 55 | 8 | 55 |
| 10 | 89 | 9 | 89 |

Thus `e(W_n) = F_{n+1} = F_{m+2}` for the checked range: the Fibonacci bound is **tight**, not violated, inside the dimension-2 class.

---

### 6. Why the width-two proof does not extend

The width-two induction uses two facts:

1. GPC for width two;
2. width two is closed under adding comparisons.

Dimension 2 satisfies neither closure property. Explicit obstruction:

Let `P` be the dimension-2 poset with upward masks

    up(P) = (8, 60, 8, 0, 32, 0),

meaning `up[i]` has bit `j` set iff `i < j`. A two-realizer is

    L1 = 0 1 2 3 4 5
    L2 = 1 4 5 2 0 3

and indeed `P = L1 ∩ L2`. For `P`, `e(P) = 26` and `m(P) = 5`, so the bound holds.

Now add the single comparison `0 < 5`. The child is

    up(Q) = (40, 60, 8, 0, 32, 0),

with `e(Q) = 22`, `m(Q) = 5`. This child is **not** of dimension ≤ 2: no `σ ∈ S_6` gives `Q = identity ∩ σ` (all 720 checked). It does have dimension exactly 3, with three-realizer

    0 1 2 3 4 5
    0 1 4 5 2 3
    1 2 4 0 3 5

So a dimension-2 poset can acquire a dimension-3 child after one comparison. The width-two induction cannot simply be transplanted to dimension 2; a genuinely new argument would be needed.

---

### 7. Bottom line

- **`n ≤ 6`:** exact `e,m` for all 402 dimension-2 classes; **0 violations**.
- **`n = 7`:** all 1956 dimension-2 classes; **0 violations**.
- **`n = 8`:** all 14794 dimension-2 classes; **0 violations**.
- **GPC two-comparison form:** holds on all tested dimension-2 classes for `n ≤ 6`.
- **Staircase `W_n`:** gives equality `e = F_{m+2}` for `n = 2..10`.
- **No counterexample found.**
- **The all-`n` dimension-2 statement remains open.** The width-two proof does not extend, because dimension 2 is not closed under adding comparisons; the explicit `P → Q` example above demonstrates the failure of the induction step.
