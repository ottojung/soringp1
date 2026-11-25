# Known gaps S(n)-C(n) for n<=22 and a uniform/local adversary candidate

**Status:** concise research note (local-source audit + computation + deduction). No Lean, no commits/PRs. Every claim is labeled **[literature]**, **[computation]**, **[deduction]**, or **[conjecture/open]**.

**Question.** From primary literature available in this workspace, what are the exact values of `S(n)` and `C(n)=ceil(log2 n!)` for all `n<=22`, and is every known positive gap `S(n)-C(n)>=1` explained by a uniform, locally-computable adversary/potential argument (a function `I(P)` or response strategy depending only on the current poset/state or a stated local class) that also correctly predicts tight cases?

## 1. Definitions and model [literature/definition]

- `S(n)` is the minimum worst-case number of adaptive pairwise comparisons needed to sort `n` distinct labeled keys (height of an optimal comparison decision tree). Model as in `curator/docs/problem.md`.
- `C(n) := ceil(log2(n!))` is the information-theoretic (leaf-counting) lower bound, so `S(n) >= C(n)` for all `n` [literature: standard decision-tree bound].
- Gap: `g(n) := S(n)-C(n)` when `S(n)` is known.

## 2. Table for n=1..22 [computation + literature]

`C(n)` values below are direct computations from `C(n)=ceil(log2(n!))` [computation]. `S(n)` values and source attributions are taken from local curated literature notes; where a full primary citation is not recorded locally, this is stated explicitly.

| n | C(n)=ceil(log2 n!) | S(n) | gap S(n)-C(n) | Status / primary-source basis (local) |
|---:|---:|---:|---:|---|
| 1 | 0 | 0 | 0 | [literature] exact small values; kernel-checked through n<=6 in repo context (`curator/docs/problem.md`, `research-plan.md`). |
| 2 | 1 | 1 | 0 | [literature] exact small values / kernel-checked context. |
| 3 | 3 | 3 | 0 | [literature] exact small values / kernel-checked context. |
| 4 | 5 | 5 | 0 | [literature] exact small values / kernel-checked context. |
| 5 | 7 | 7 | 0 | [literature] exact small values / kernel-checked context. |
| 6 | 10 | 10 | 0 | [literature] exact small values / kernel-checked context. |
| 7 | 13 | 13 | 0 | [literature] exact; information bound tight (`research-plan.md`, `literature.md` baseline). |
| 8 | 16 | 16 | 0 | [literature] exact; tight (`research-plan.md`). |
| 9 | 19 | 19 | 0 | [literature] exact; tight (`research-plan.md`). |
| 10 | 22 | 22 | 0 | [literature] exact; tight (`research-plan.md`). |
| 11 | 26 | 26 | 0 | [literature] exact; tight (`research-plan.md`, `literature.md`: equality with info bound through n=11 reported via Peczarski intro/Wells context). |
| 12 | 29 | 30 | 1 | [literature] Wells 1965/1971: `S(12)=30 > C(12)=29`; credited/discussed in Peczarski 2012 and Stober–Weiß 2023 (`literature.md`, `research-n12-nontightness.md`). |
| 13 | 33 | 34 | 1 | [literature] Kasai et al. 1994: `S(13)=34` (`research-certificates-barriers.md`); gap `>0` discussed by Peczarski 2012 §4 (as summarized locally). |
| 14 | 37 | unknown (locally) | unknown (>=1 claimed) | [literature, incomplete locally] exact value known for `n<=22` per local summaries (`research-plan.md`, `research-hardness-boundaries.md`), and info bound missed for n=14 discussed by Peczarski 2012 §4 (as summarized in `research-n12-nontightness.md`), but the exact value of `S(14)` and a primary citation giving it are not explicitly recorded in available local sources. |
| 15 | 41 | 42 (reported) | 1 (reported) | [literature, citation detail incomplete locally] `S(15)=42` reported by Jing et al. in `research-certificates-barriers.md`; Peczarski 2012 §4 discusses non-tightness for n=15 (summary). Full Jing et al. bibliographic details not present locally. |
| 16 | 45 | 46 | 1 | [literature] Stober & Weiß, ALENEX 2023 / arXiv:2206.05597: `S(16)=46` (`literature.md`, `research-plan.md`). |
| 17 | 49 | 50 | 1 | [literature] Stober & Weiß 2023: `S(17)=50`. |
| 18 | 53 | 54 | 1 | [literature] Stober & Weiß 2023: `S(18)=54`. |
| 19 | 57 | 58 (reported) | 1 (reported) | [literature, citation detail incomplete locally] `S(19)=58` reported by Jing et al. in `research-certificates-barriers.md`; full bibliographic details not present locally. |
| 20 | 62 | 62 | 0 | [literature] stated tight: `S(n)=C(n)` for `n<=11` and `n=20,21` in `research-hardness-boundaries.md`; consistent with `S(20)=62` used in `research-n12-nontightness.md` H1. Primary source not named in those local summaries (values treated as known in literature). |
| 21 | 66 | 66 | 0 | [literature] stated tight for `n=20,21` in `research-hardness-boundaries.md`; implies `S(21)=C(21)=66`. Primary source not named locally. |
| 22 | 70 | 71 | 1 | [literature/index-level locally] used as `S(22)=71 > C(22)=70` in `research-n12-nontightness.md` H1 and audit notes; exact values known for `n<=22` per local summaries. A specific primary proof citation for `S(22)` is not explicitly recorded in available local sources (OEIS A036604/A003070 are indices, not primary proofs, per `literature.md`). |

**Caveat [literature]:** Local sources state exact `S(n)` is known for all `n<=22` (`research-plan.md`, `research-hardness-boundaries.md`), but for `n=14,15,19,20,21,22` the available local files do not all provide complete primary bibliographic details/values in one place; the table above reflects what is explicitly supported or explicitly reported locally and marks uncertainties.

## 3. Positive gaps S(n)>C(n), n<=22 [deduction from table]

From values explicitly supported/reported above [literature] and computed `C(n)` [computation]:

- **Known positive-gap cases (gap 1):** `n = 12, 13, 15, 16, 17, 18, 19, 22`.
- **Tight cases:** `n = 1..11, 20, 21` have `S(n)=C(n)`.
- **Uncertain from local primary detail but indicated non-tight:** `n = 14` (`C(14)=37`, non-tightness discussed for 13–15 by Peczarski 2012 §4 as summarized locally; exact `S(14)` not recorded locally).

No gap larger than 1 appears among the cases with explicit `S(n)` values in local sources above [deduction].

## 4. Candidate uniform/local adversary potential: one-ply information bound L1 [deduction]

### Definition
Let `P` be the current poset state, `e(P)` its number of linear extensions, and `F(P)` the minimax remaining comparisons. Define the information bound
- `L0(P) := ceil(log2 e(P))`.

Define the **one-ply adversary** bound (a uniform response/score depending only on the current state `P` and one-step comparison outcomes):
- if `P` is total, `L1(P):=0`;
- otherwise `L1(P) := 1 + min_{(i,j) incomparable} max(L0(P + i<j), L0(P + j<i))`.

Interpretation [deduction]: the algorithm chooses a comparison `(i,j)` (local move in state `P`), the adversary answers to force the child with larger `L0` (local/state-based reply), and the cost is estimated by one lookahead plus the leaf-count bound. This is the same candidate family recorded/analyzed in `curator/docs/research-one-ply-obstruction.md`.

### General properties (as reasoned/recorded locally) [deduction]
- `L0(P) <= L1(P) <= F(P)` for all `P`: adversary can always keep a child with `e >= ceil(e(P)/2)` so `max(L0(children)) >= ceil(log2 ceil(e(P)/2)) >= L0(P)-1`; and replacing `F` by `L0` on children weakens the minimax recurrence (`research-one-ply-obstruction.md`, Theorems 1–2 logic).
- `L1` can be strictly stronger than `L0` on some posets (e.g. the `n=5`, `e=8`, `F=4` witness in `research-one-ply-obstruction.md`: `L1=4>L0=3`) [literature from local note].

### Test on antichain roots / S(n)-C(n) gaps (n=1..22) [deduction]
For the initial antichain `A_n`, `e(A_n)=n!` and every incomparable pair splits extensions evenly: `e(A_n + i<j)=e(A_n + j<i)=n!/2`. Hence
- `L1(A_n)=1 + ceil(log2(n!/2)) = ceil(log2(n!)) = C(n) = L0(A_n)` for all `n>=2` (and `0` for `n<=1`).

**Test outcome:**
- `L1(A_n)` predicts `g(n)=0` for every `n` (it certifies only the information lower bound at the root).
- Therefore it **fails to predict/explain every known positive gap case** in the table: `n=12,13,15,16,17,18,19,22` all have `S(n)-C(n)=1` but `L1(A_n)-C(n)=0`. It also cannot distinguish the indicated gap case `n=14` from tight cases.
- For tight cases (`n=1..11,20,21`) its root prediction `S(n)>=C(n)` is consistent but non-explanatory (same as leaf counting).

**Falsifier/strength assessment [deduction]:** at the antichain root (the state relevant to `S(n)`), `L1` is **equivalent to** `ceil(log2 e(P))=C(n)` as a lower bound and thus cannot account for any `S(n)>C(n)` gap. It is a sound, sometimes locally stronger refinement of leaf counting on intermediate posets, but it is **not** a uniform invariant explaining the known global gaps.

## 5. Relation to other local candidates (context) [literature/deduction]

Local note `research-n12-nontightness.md` audits several uniform/scalar candidates: global slack ratio `2^{C(n)}/n!` (H1) misclassifies tight vs gap cases (e.g. `n=5,20` tight vs `n=12,22` gaps), monotonicity in `e(P)` fails (H2), local `L0` tightness fails without implying global gaps (H3), forced balanced-prefix signatures occur at tight values too (H4), and no invariant depending only on `e(P)` can determine sortability because `F(P)` is not a function of `e(P)` [literature/experiment as recorded there]. Peczarski 2012 §4 (as summarized) gives a structural non-monotonicity example at `n=13`. These support that the known `+1` gaps are certified in the literature by exhaustive search/global strategic arguments rather than a known scalar state function [literature].

## 6. Obstacles and implications for all-n complexity of S(n)/SORT-BOUND-U

- **Obstacle [literature/open]:** No short, reusable uniform/local invariant stronger than leaf counting is known locally to explain the `n=12` gap or the pattern of gaps through `n<=22`; known proofs/certifications of specific gaps (notably Wells/Peczarski/Stober–Weiß for 12,16–18, and searches summarized for others) are exhaustive/strategic (`literature.md`, `research-n12-nontightness.md`).
- **Implication (positive, limited) [deduction]:** The tested one-ply local adversary is sound (`<=F`) and easy to state uniformly, but root-level equivalence to `C(n)` shows why one-step/state-scalar information arguments do not by themselves yield `S(n)>C(n)`; explaining known gaps requires multi-step/global tree/poset-structure constraints.
- **Non-implications [deduction]:** This audit does **not** determine `S(14)` from local primary sources, does **not** give a new lower-bound technique, and implies **no** complexity-class separation or membership claim for computing `S(n)` or for `SORT-BOUND-U` beyond what is already established (e.g. known upper bounds/barriers discussed in `problem.md`, `research-plan.md`). A gap `S(n)>C(n)` is a combinatorial fact about comparison trees, not by itself a complexity lower bound for the decision/evaluation problem.
- **Conjecture/open [conjecture]:** A uniform explanation, if it exists, likely must be strategic/non-scalar in the current poset dynamics (tracking reachability/frontiers over many steps), not a function of `e(P)` alone; identifying such an invariant remains open.

## 7. Sources consulted (local workspace)

- `curator/docs/problem.md` — model/definitions, established bounds.
- `curator/docs/literature.md` — Wells 1965/1971 (via Peczarski), Peczarski 2012, Stober–Weiß 2023 (ALENEX/arXiv:2206.05597), Ford–Johnson 1959, Knuth TAOCP §5.3.1, OEIS A036604/A003070 (indices).
- `curator/docs/research-plan.md` — baseline values/gaps summary, known n<=22 status.
- `curator/docs/research-n12-nontightness.md` — gap/non-tightness analysis, H1 table values (incl. n=20,22), scalar-invariant falsifications, Peczarski §4 discussion.
- `curator/docs/research-one-ply-obstruction.md` — L1 definition/properties and local witness.
- `curator/docs/research-hardness-boundaries.md` — states tightness for n<=11 and n=20,21, exact-known range n<=22, and cites Kasai et al. 1994, Peczarski 2004/2012, Stober–Weiß 2022/2023, Jing et al. (as reported).
- `curator/docs/research-certificates-barriers.md` — same exact-value/citation snippet including Jing et al. report for S(15), S(19).
