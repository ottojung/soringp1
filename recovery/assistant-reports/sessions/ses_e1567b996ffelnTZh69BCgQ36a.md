# antonina-gaM1uX8QhzVX2cK6xgcRaJ-features

Session: ses_e1567b996ffelnTZh69BCgQ36a
Workspace: /home/lubko/soring301-exec-root-composition-exact-recurrence-20261117e
Created: 1794937210537; updated: 1794937330787

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 116 (msg_1ea99e4d1001u00kELKCI1ddmQ)

Wrote `exec-report.md` in the worktree.

**Question addressed:** `root-composition-exact-recurrence` — sought a compositional exact recurrence for optimal sorting from chain/ordinal-product interfaces preserving the adversarial root and both sibling branches (not just post-transcript `F(P)`), with falsifier/implication framed per `docs/problem.md` and the frontier basis.

**Candidates examined (with claim types):**
- **C1 Ordinal-sum/series interface** (`F(A⊕B)=F(A)+F(B)`): exact for post-state `F(P)` (literature/deduction) but does not compose the antichain root (series-prime) and fails under parallel/interleaved composition; naive direct-sum/root transfer rejected.
- **C2 Local `F(P)` / sound symmetry-quotient summaries:** preserve `F`/class transitions but omit prefix depth and sibling obligations (deduction) — insufficient for root viability.
- **C3 Depth+remainder `(d,F(P))`:** falsified as root-sufficient by the stated sibling obstruction (packet/ledger basis): `n=5` `C2 ordinal A3` has `d+F=S(5)` yet `min_h R_h=8>S(5)=7`, showing sibling incompatibility.
- **C4 History-sensitive reachability `R(P)=min_h R_h(P)`:** root-correct by definition but not a demonstrated polynomial-state chain/ordinal-product compositional recurrence.
- **C5 Parallel/comparability/module-style factorization:** in-repo results (`docs/research-compression-next.md`, `docs/research-orientation-modules.md`) show stronger structural collapses are not sound/exact for `F` in general; no root+sibling-preserving antichain decomposition.

**Evidence/falsification attempts:** deduction from consulted docs (series decomposition, symmetry/module notes, `R_h` functional in `docs/research-packets.json`); no new experiments run and no claims depend on new computation. Extensibility of the sibling pattern stated only as a conjectural argument sketch, not a theorem.

**Findings:** negative/falsifying for C1–C3 as root-preserving compositional interfaces given the sibling-branch obstruction; positive clarity that any exact root recurrence must be history/sibling-aware (capture `max(d+F(P), max_i i+F(Q_i^{sibling}))`), but C4 is not realized succinctly; overall inconclusive on existence of a uniform polynomial-state exact root recurrence.

**Obstacles:** adversarial-root vs local-minimax gap, antichain non-decomposability/interleaving, risk of reverting to transcript/state enumeration under known barriers, and reliance on the in-repo recorded `n=5` witness without an independently constructed parameterized infinite family here.

**Next decisive question:** define an explicit, checkable sibling-closed interface/congruence `I(h,P)` implying `R_h(P)=R_{h'}(P')` and either prove polynomially many classes for all `n` or exhibit a concrete infinite root-relevant family forcing superpolynomial classes for every sound candidate (upgrading the witness to a barrier).

**Claim-type summary:** definition/literature, deduction, packet/ledger-cited witness, conjecture sketch; no new theorem/bound/NP-or-P claim/Lean result/experiment.
