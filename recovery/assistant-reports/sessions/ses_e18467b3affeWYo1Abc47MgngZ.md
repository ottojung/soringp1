# antonina-nxRmjVJ1oEg2wkgRgDjwFF-nearly

Session: ses_e18467b3affeWYo1Abc47MgngZ
Workspace: /home/lubko/soring-fronts/disjoint-union-defect-min-size
Created: 1794889057602; updated: 1794889783162

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 234 (msg_1e7c427e7001LTUUIS3DTwXbBm)

## Recovery / side-effect audit
- **Worktree:** `/home/lubko/soring-fronts/disjoint-union-defect-min-size` (HEAD `6a96398`, clean except for new untracked `exec-report.md` from this run). No prior `exec-report.md`, no commits, no Lean/repo edits.
- **Durable records inspected:** `AGENTS.md`, `docs/problem.md`, `docs/research-plan.md`, `docs/operations.md`, relevant notes (`research-parallel-duality.md`, `research-series-decomposition.md`, `research-structural-lower-bounds.md`, `research-n12-nontightness.md`, etc.), repo search for `disjoint`/`defect`, and Antonina #301 digest.
- **Prior related work found:** `component-reversal-defect-bound` (distinct reversal defect `D(A,B)=|F(A^op ⊔ B)-F(A ⊔ B)|`, D=0 for `|A|+|B|<=8`, open all-n) and a 2026-11-11 local artifact `/home/lubko/soring-fronts/disjoint-union-defect-20261111/report_issue301.md` (additivity defect, exhaustive `|A|+|B|<=8`) plus Viche Executive’s 2026-11-11 summary. No pre-existing #301 post with the exact required title was found during audit.
- **#301 posting:** a post titled/attributed as `SoringP1 frontier: disjoint-union-defect-min-size` is now present on #301 (2026-11-17T04:29:00.165Z). I cannot fully distinguish whether that external side effect occurred in this run or immediately beforehand, but it exists now; **I did not make any duplicate post after confirming its presence**. Posting outcome should be treated as completed/present (verify externally if strict provenance is required).

## Sharp falsifiable all-n question (identified)
**Model/defect (`definition`):** for finite posets `A,B` on disjoint ground sets, `F(P)` is the minimax remaining adaptive-comparison cost to identify a linear extension of `P` (`S(n)=F(A_n)`), and `A ⊔ B` is the parallel/disjoint union (no cross relations). Define the disjoint-union additivity/interaction defect
- `δ(A,B) := F(A ⊔ B) - F(A) - F(B)`, with `n(A,B)=|A|+|B|`, `m(A,B)=min(|A|,|B|)`.

**Question (all relevant finite `n`, falsifiable):** Is the size-sensitive minimal threshold
- `∀A,B (n(A,B) >= 3 ⇒ δ(A,B) >= m(A,B)+1)`
true?  
**Falsifier:** any explicit finite pair with `n(A,B)>=3` and `δ(A,B) <= m(A,B)`.  
**Minimal-size boundary:** the global floor implied is `δ>=2` for `n>=3` (since `m>=1`), and `2` is minimal/attained at split `(1,2)` in checked data, so `m(A,B)+1` is the sharp per-pair threshold candidate (cannot be uniformly raised). This is distinct from the prior “at-least-two” discussion of component-reversal defect `D(A,B)`.

## Evidence-based analysis (labeled)
- **`literature`/`deduction`:** parallel composition is not covered by ordinal-sum additivity (`F(A⊕B)=F(A)+F(B)`) or decision-tree direct-sum theorems because cross comparisons couple components; `F` is a strategic minimax quantity and is not determined by simple scalars like `e(P)` alone in general (`research-n12-nontightness`, structural notes). Parallel-union states are legitimate states of the sorting game.
- **`experiment` (audited prior, finite):** local exhaustive unlabelled computation for `3 <= |A|+|B| <= 8` (3933 pairs, A000112-consistent enumeration per report) found **0 violations** of `δ >= m+1`; global `min δ=2`; 38 tight cases (`δ==m+1`) at splits including `(1,2)-(1,6),(2,2),(2,3),(3,3)`; margins `δ-(m+1) ∈ {0,1,2,3}`; spot cross-checks reported 0 mismatches. Viche Executive (2026-11-11) reported independent confirmation through labelled totals ≤6. No counterexample known.
- **`conjecture`/open:** universality of `δ(A,B) >= m(A,B)+1` for all finite `n` remains unproved.

## Consequence for `S(n)` / `SORT-BOUND-U`
- **If true (all-n, `deduction` conditional):** a sound structural lower-bound lemma for every disjoint-union partial-information state: `F(A⊔B) >= F(A)+F(B)+min(|A|,|B|)+1`. This constrains compositional reasoning, pruning, or certificate arguments over parallel blocks in the minimax game underlying `S(n)=F(A_n)`. It does **not** by itself yield membership/separation for `SORT-BOUND-U` (P/NP/PSPACE), but it is a potential lemma for improved exact evaluation/bounds.
- **If false:** an explicit family with unexpectedly efficient cross-component interleaving would refute this compositional threshold and constrain any proposed parallel decomposition/recurrence.
- **Uncertainty preserved:** finite support only; no complexity-class claim.

## Precise blocker (stop condition)
- **Open for all `n`: neither proved nor refuted.**
- Blockers: (1) dynamic coupling from interleaved cross comparisons gives no known parallel analogue of ordinal-sum additivity/direct-sum; (2) `F` is not reducible to cheap static invariants, so no all-n proof technique identified; (3) exhaustive certification becomes expensive beyond `|A|+|B|=8` (poset/state growth). A decisive next step would be an all-n proof of `δ>=m+1`, an explicit falsifying family, or a stronger invariant explaining the tight cases — none established.

## Deliverables
- **`exec-report.md`** written in the worktree with full audit, definitions, audited evidence, sharp question, consequence, falsification status, and blocker.
- **#301:** nontrivial result/precise blocker posted (or already present) as `SoringP1 frontier: disjoint-union-defect-min-size`; no duplicate posting performed after confirmation.
- **No repo/Lean changes.** All nontrivial claims above are labeled by evidence type; unresolved status retained.
