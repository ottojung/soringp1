# antonina-PW9lYoOKJKBHY6ionE8lov-davout

Session: ses_e166d4e25ffdUfVYNkhGDitLHb
Workspace: /home/lubko/soring301-exec-polynomial-merge-certificate-20261117
Created: 1794920067574; updated: 1794920167160

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 57 (msg_1e994091a001P5bBn8xM4jipJo)

Wrote `exec-report.md` with a labeled-evidence analysis of the “polynomial merge-decomposition certificate” front.

**Covered in the report**
- **Question/scope:** all-`n`, falsifiable status of exact height-`S(n)` certificates via merge/series-parallel or bounded-width comparison-DAG/state-graph decomposition, and implications for `SORT-BOUND-U ∈ NP`.
- **Evidence reviewed:** `AGENTS.md`/`problem.md` constraints, `research-framed-certificate-frontier.md` (sound framed-DAG grammar, merge-sort `O(n^2)` construction, FJ rank-envelope construction, optimal-completeness open), `research-series-decomposition.md` (exact ordinal-sum identity, no state-count gain/root indecomposable), winning-frontier barrier (`2^{(1/4-o(1))n log^2 n}` nonisomorphic winning states), and literature baselines.
- **Construction/family & small-n checks (labeled `[computation]`):** compared `C(n)=ceil(log2 n!)`, known `S(n)` (`n<=22`), `F_FJ(n)`, and balanced merge sort. Found `F_FJ(n)==S(n)` for `n=1..21` but `F_FJ(22)=71 > S(22)=70`; merge sort exceeds `C(n)` for powers of two from `n=8` onward (`1,4,11,25` surplus at `8,16,32,64`), consistent with architectural non-optimality.
- **Obstruction/conclusion:** concrete obstructions for fixed merge architectures (asymptotic/exact deficits) and explicit optimal-state/frontier enumeration (superpolynomial winning frontier), plus no all-`n` exact optimal merge/series-parallel/bounded-width certificate currently constructed; winning-frontier/state-enumeration routes are blocked while a fully general succinct decomposed certificate remains open.
- **NP implication:** polynomial-size exact-height checkable certificates would imply `SORT-BOUND-U ∈ NP`; known decomposed constructions certify only upper bounds, and current obstructions narrow viable designs but do not prove `SORT-BOUND-U ∉ NP` (which would imply `NP != PSPACE`).

**Artifacts:** `exec-report.md` only (no other repo/Lean/PR changes, no saved scripts).
