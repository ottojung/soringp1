# antonina-F7NjS41YxBABJ82we78q0T-horner

Session: ses_e464e7cebffea9anO5iQEPsc4C
Workspace: /home/lubko/soring-fronts/t9-universal-threshold-lower
Created: 1794116780823; updated: 1794122854295

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b9b18336001lMJD0XLNn44YFB)

I'll start by reading the key documents and scripts to understand the machinery.



## Output 45 (msg_1b9b1db5f0017GyKuPQftFlbv1)

Let me validate the machinery independently on small `n` before running the large census.



## Output 155 (msg_1b9b9b74f001w4bQnHmdL9ZEcM)

The full `E=88` census alone takes ~7.5 min, so `E=143` needs care. Let me build a progress-instrumented enumerator with an exact early-abort optimization, and first confirm it reproduces the `E=88` class set.



## Output 220 (msg_1b9bcec31001NkcQ5aqOLttodR)

While the census runs, I'll prepare the analysis and a supplementary independent check.



## Output 319 (msg_1b9c09411001X5XBZLcoI89xgv)

Validation is complete (machinery checked against brute force for all posets on `n<=4`, plus 120 random cores at `n<=6`), and the `E=143` census is running with an exact early-abort variant that reproduces the known `E=12`, `E=20`, and `E=88` totals. I'll continue when it finishes.



## Output 330 (msg_1b9c0bc5e001JYaJdI795bEgHy)

Status: census at level `n=12`, 52,757 core classes so far, ~3.5 min elapsed, memory ~0.4 GB. Waiting for completion.

## Output 377 (msg_1b9c12661001uCX72CwF8Ekf4W)

The background run was SIGKILLed after level 12. I'll make the census checkpointed per level so it can resume, and run it in chunks in the foreground.



## Output 422 (msg_1b9d15d43001XFpVUYGoyr1JAo)

Checkpointing works. The slow part is the ordinal-sum double loop; grouping factors by extension count will cut it drastically since `e_left*e_right <= 143`.



## Output 467 (msg_1b9d82a77001HzmITIUTEWgjRf)

Census complete: **101,826 core classes** with `e <= 143` (all levels 2..143 checkpointed). Now the sortability analysis, checkpointed per level.



## Output 487 (msg_1b9ece219001deO16qiGjsgIdR)

No core with `e <= 143` needs 10 comparisons. Let me extract exact counts, thresholds, and witnesses.



## Output 541 (msg_1b9f568fb001Mo06xNtt8EIpBb)

Let me independently re-verify the hardest `m=9` cases (including `e=143`) with the separate minimax implementation from the validation step.



## Output 568 (msg_1b9fa3b100010TXNv4wDqpEKkr)

The meaningful statement (`e<=143 => m<=9`) holds through the whole core census. The literal "8 comparisons" reading fails at `W_10`; let me extract an explicit 9-comparison strategy for it as a certificate.





## Output 649 (msg_1ba0dd21e001EwmUNSbPZNWqfX)

# Report: `t9-universal-threshold-lower`

## Verdict

**HOLDS-TO-E143-CORES** — for the intended Fibonacci statement  
`T(9) = 143`, i.e. **every poset with `e(P) <= 143` is sortable in at most 9 comparisons**.

There is an off-by-one in the prompt. Taken **literally** as “at most 8 comparisons”, the statement is **false**, so that reading is `T9-REFUTED`. The minimal counterexample is the staircase `W_10` with `e = 89 <= 143` and `m = 9`. In fact **2,303** core classes with `e <= 143` have `m = 9`; none has `m >= 10`.

---

## 1. Census and validation

Reused `scripts/core_threshold_census.py` (exact structural core generation and exact minimax on extension sets), with an exact extension-count early abort and per-level checkpointing.

**Independent validation**

| check | result |
|---|---|
| all unlabeled posets on `n <= 4` by brute force | 16 classes; generator reproduces exactly the 11 core classes |
| independent minimax vs `sortable` on those 11 cores | exact match on every `(e, m)` |
| 120 random cores from the `E=54` census, `n <= 6` | exact `e` and `m` match |
| 42 hardest `m=9` cases (`n >= 20` plus largest `e`) re-run with a separate minimax | all confirm `m = 9` |
| census reproduces known totals | `E=12` per-level exact; `E=20: 250`; `E=33: 1053`; `E=54: 4829`; `E=88: 22120` |
| structural sanity | all 101,826 classes are cores; `e >= n`; closed under order-duality; relabelling-invariance sampled |

---

## 2. Coverage

**101,826 core isomorphism classes** with `e <= 143`, at levels `n = 2..143`.

| cutoff | cores |
|---|---|
| `e <= 20` | 250 |
| `e <= 33` | 1,053 |
| `e <= 54` | 4,829 |
| `e <= 88` | 22,120 |
| `e <= 143` | **101,826** |

The first four rows are exactly the independently corroborated totals from the repo note. The new part is **79,706** classes with `89 <= e <= 143`.

Per-level counts for the mass of the census:

```
n= 2..23: 1, 2, 8, 35, 193, 1060, 3872, 8657, 12711, 14027,
          12191, 9244, 6629, 4778, 3784, 3236, 2329, 2150,
          1595, 1443, 1246, 1273
n=24..36: 859, 871, 722, 614, 617, 578, 603, 631, 658, 682, 715, 753, 232
n=37..71: 238, 106, 101, 90, 92, 94, 96, 98, 100, 102, 104, 61, 62, 59,
          54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74
n=72,73: 5, 5
n=74..143: exactly 1 class at each n
```

---

## 3. Exact sortability result

For every one of the 101,826 cores:

- `sortable(exts, 8)` tested; every failure then tested at `sortable(exts, 9)`.
- Results:
  - `m <= 8`: **99,523**
  - `m = 9`: **2,303**
  - `m >= 10`: **0**

So **no core with `e <= 143` needs 10 comparisons**, and the `E<=88` subcensus has zero failures at 8, reproducing `T(8) = 88`.

`m = 9` distribution by `n`:

```
{9:16, 10:301, 11:623, 12:625, 13:348, 14:140,
 15:130, 16:80, 17:24, 20:2, 21:6, 22:8}
```

`m = 9` distribution by `e`:

```
{89:1, 97:4, 98:1, 99:2, 102:6, 103:2, 104:2, 105:5,
 106:4, 107:8, 108:2, 109:6, 110:8, 111:20, 112:10,
 113:5, 114:12, 115:24, 116:10, 117:36, 118:3, 119:10,
 120:66, 121:16, 122:21, 123:46, 124:16, 125:50, 126:121,
 127:26, 128:33, 129:62, 130:98, 131:39, 132:67, 133:35,
 134:53, 135:300, 136:92, 137:56, 138:254, 139:51,
 140:248, 141:174, 142:115, 143:83}
```

- Minimum `e` with `m = 9`: **89**, attained by a **unique** core class: `W_10`.
- Maximum `e` with `m = 9`: **143** (83 classes).
- Maximum `n` with `m = 9`: **22**.
- `e=89` total: 206 core classes; exactly 1 has `m=9`.

---

## 4. Certificates

### `W_10`: refutes the literal 8-comparison claim

Elements `0..9`, with `i > j` iff `j <= i - 2`; equivalently cover pairs `(upper, lower)`:

```
(2,0), (3,0), (3,1), (4,1), (4,2), (5,2), (5,3),
(6,3), (6,4), (7,4), (7,5), (8,5), (8,6), (9,6), (9,7)
```

- `e(W_10) = 89 = F_11`.
- Exact minimax: **no depth-8 strategy**; a depth-9 strategy exists (89 leaves, first comparison `(0,1)`).
- Hence `m(W_10) = 9`, and since `89 <= 143`, the statement “every `e <= 143` sorts in 8” is false.
- It is the **unique** `e=89, m=9` core, hence the canonical minimal counterexample.

### `W_11`: upper bound `T(9) <= 143`

Elements `0..10`, same rule:

- `e(W_11) = 144 = F_12`.
- Exact minimax, independently confirmed: `m(W_11) = 10`.
- Therefore `e <= 144` does **not** guarantee 9 comparisons, so `T(9) <= 143`.

Combined with the census (`e <= 143` guarantees 9):

\[
T(9) = 143
\]

conditional on the census being faithful.

### Why cores suffice

Lemma 1 of `docs/research-core-threshold.md` is a paper proof: deleting an element comparable with all others preserves both `e` and `m`. Every poset therefore reduces to a core with the same `(e, m)`, or to the empty poset (`e=1, m=0`). Hence the all-poset statement follows from the complete core census.

---

## 5. Remaining gap

There is **no structural coverage gap**: the reduction to cores is proved, and the census enumerates all core isomorphism classes with `e <= 143` via the paper-proof generation lemmas.

The residual gap is **implementation faithfulness at `E=143`**:

- The `E <= 88` part is anchored by the repo’s prior independent dual-generator and all-poset checks.
- The new `79,706` classes with `89 <= e <= 143` rest on one complete implementation. A second full generator at `E=143` (the note’s dual generator currently reaches only `E=54`) would close this.
- The minimax was independently validated on `n <= 4`, sampled at `n <= 6`, and on all 42 hardest `m=9` cases.

The all-`r` statement `e(P) >= F_{m(P)+2}` remains open; this work settles only `r=9`.

---

## 6. Bottom line for the collector

- **If scored on the literal “8 comparisons” wording:** `T9-REFUTED`, with 2,303 core-class counterexamples; minimal is `W_10` (`e=89`, `m=9`).
- **If scored on the Fibonacci `T(9)=143` statement (9 comparisons):** `HOLDS-TO-E143-CORES`; all 101,826 cores with `e<=143` have `m<=9`, and `W_11` (`e=144`, `m=10`) makes 143 tight.

I recommend recording the second verdict, since the repo defines `T(6)=33, T(7)=54, T(8)=88` using 6, 7, and 8 comparisons respectively.

No tracked files were modified; `git status` is clean. Scratch data and scripts are under `/tmp` (`/tmp/e143_levels`, `/tmp/e143_analysis`, `/tmp/enum_ckpt.py`, `/tmp/analyze_ckpt.py`, `/tmp/summary143.py`, `/tmp/cert_w10.py`, `/tmp/verify_hard.py`).
