# antonina-5VaCMoRCg21JGtfPidft5w-dryly

Session: ses_e14f356efffeKqzfFEJR0pWxYD
Workspace: /home/lubko/soring301-exec-polytime-root-adversary-invariant-n12-20261117f
Created: 1794944837945; updated: 1794944972852

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 73 (msg_1eb0e81530018tN1JYrJ0PFJvM)

Created `exec-report.md` in the worktree (front: `polytime-root-adversary-invariant-n12`).

**Contents (per request):**
- **Candidates (all poly-time checkable on standard poset/transcript representation, no `#P` extension counting):**
  - **J1 (Dilworth width/antichain):** `J1(P,d):=[w(P) >= g(n,d)]` via chain-cover/matching; initializable (`w(A_n)=n`), maintainable in weak forms, but **fails to force/explain** the `n=12` deficit (`C(12)=29, S(12)=30`) or any super-information gap (deduction+literature; schematic small-`n` counterexample at `n=5`, `S(5)=C(5)`).
  - **J2 (incomparable-pair/degree summaries):** `m(P), c(P), d_{inc}` thresholds; initializable/maintainable as delay measures, but **not sound** for deficit forcing (coarse, does not determine extension structure; global strategic obstruction).
  - **J3 (chain-height/width summaries):** `(h(P), w(P))` predicates; poly-time/initializable, mixed maintenance, but **no implication** to n=12 deficit and insufficient as predictors given strategic/non-scalar gap.
  - **J4 (poly-time one-ply/transitive-closure balance proxy):** motivated by forbidden `L1/e(P)`; poly-time definable but **soundness unargued** and vulnerable to sorter balanced-proxy moves; no deficit proof.
- **Analysis:** formalized goal/representation, per-candidate poly-time checkability, initializability, adversary-reply maintenance attempts, and soundness toward n=12/infinite-family deficit.
- **Falsification attempts:** for each, concrete/schematic sorter counterstrategy or demonstration of non-initializability/non-poly-time/soundness failure relative to the front criterion (with emphasis on failure to force super-information deficit where required).
- **Evidence & claim types:** explicitly labeled **literature/definition/deduction/experiment (as reported in repo docs)/conjecture**; grounded in `docs/problem.md`, `docs/research-plan.md`, `docs/research-n12-nontightness.md`, `docs/research-one-ply-obstruction.md`, `docs/research-structural-lower-bounds.md`, `docs/literature.md`.
- **Cross-cutting barrier:** soundness–maintainability tension under the no-`#P`-counting constraint; global strategic nature of the n=12 obstruction.
- **Obstacles and next decisive question:** need a poly-time potential `Φ(P,d)` from chain-decomposition/comparability data with a checkable maintenance+certification argument on the n=12 frontier (or a proof no such `Φ` can succeed), stated as a falsifiable next step.
