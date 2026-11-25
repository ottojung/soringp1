# antonina-7BmRzGoEDRVeQDjwfPzEMa-rival

Session: ses_e30a1d72affeoFqtT03rdIGdV0
Workspace: /home/lubko/soring-fronts/sparse-manyone-pspace-completeness-barrier
Created: 1794480417032; updated: 1794489651765

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 148 (msg_1cfea2519001BBPamIS9xcPhfq)

# Frontier: SORT-BOUND-U many-one PSPACE-completeness (sparsity/isomorphism barrier)

**Labels:** [definition] [literature] [deduction] [open]. **Outcome:** no new theorem, no counterexample/reduction, no Lean/repository change.

## 0. Recovery / state inspection (no duplicated side effects)
- Host/workdir: `billy-dev`, `/home/lubko/soring-fronts/sparse-manyone-pspace-completeness-barrier` (git repo).
- `git status --porcelain -uall`: clean. HEAD `6a96398` inspected; no prior in-repo artifact for this specific front found. Board #301 recent digest inspected via `/home/lubko/soring301/scripts/board_digest.py --recent 7` (recent items are unrelated n=8/n=12 fronts). No external side effects (no board post/commit/PR/purchase) performed.

## 1. Precise all-`n` falsifiable question
Let `SORT-BOUND-U = { 1^n # 1^k : S(n) ≤ k }`, total input length `N = n+k+1` (docs/problem.md, AGENTS.md; active unary scope).

**Question:** Is `SORT-BOUND-U` unconditionally *not* many-one PSPACE-complete under polynomial-time reductions `≤_m^p` (by sparsity/isomorphism generalizations of Berman–Hartmanis/Mahaney)?

- **Barrier resolution:** prove for all PSPACE-complete `L`, `L \not≤_m^p SORT-BOUND-U` (unconditionally), or derive an unconditional contradiction from such a reduction in this model.
- **Falsifier (disproof of “not complete”):** exhibit a fixed PSPACE-complete language `L` (e.g. `TQBF`) and polynomial-time computable `f` with `x∈L ⇔ f(x)∈SORT-BOUND-U` for all `x`, with complete correctness and encoding analysis (`f(x)` always well-formed `1^{n}#1^{k}`, `|f(x)|=poly(|x|)`).

**Complexity implication:** would fix the exact relation of the sparse unary threshold to PSPACE without relying only on `P/poly` circuit barriers. `SORT-BOUND-U ∈ PSPACE` is established, so completeness would make it a canonical PSPACE-complete representative; unconditional non-completeness would separate it (under many-one) from PSPACE-complete problems.

## 2. Established basis (model-faithful)
- [deduction, repo] `SORT-BOUND-U ∈ PSPACE` (value in `FPSPACE`) via the comparison-game/alternating-TM formulation, `APTIME=PSPACE` (Chandra–Kozen–Stockmeyer 1981); `docs/research-certificates-barriers.md` Claim A.
- [deduction] `SORT-BOUND-U` is sparse/tally-threshold: `O(N^2)` strings of length ≤`N`; accepted `n` at fixed total length form an initial interval by monotonicity of `f(n)=n+S(n)`. Hence `SORT-BOUND-U ∈ P/log ⊂ P/poly` and in nonuniform `AC^0` (nonuniform upper bounds only, not uniform membership); `docs/research-hardness-boundaries.md` Lemma 4.1/Thm 4.3, `docs/research-encoding-consequences.md`.
- [literature, as cited in repo] Mahaney 1982: sparse NP-hard under `≤_m^p ⇒ P=NP`. Fortune 1979 / Ogiwara–Watanabe 1991 / Karp–Lipton 1980 give the corresponding coNP/btt/Turing barriers. For `SORT-BOUND-U` these bar NP/coNP-hardness (conditionally), not PSPACE-hardness.
- [literature, as cited in repo] Berman–Hartmanis 1977: no polynomially sparse language is EXPTIME-complete under `≤_m^p` (unconditional). Therefore `SORT-BOUND-U` is **unconditionally not many-one EXPTIME-hard/complete** (`docs/research-hardness-boundaries.md` Thm 4.2a/Cor 4.2b). This is the settled sparse/isomorphism-style case in-repo.
- [deduction, non-transfer] `GEN-SORT` (arbitrary poset, matrix encoding) differs: `SORT-BOUND-U ≤_m^p GEN-SORT` (unary antichain embedding), so upper bounds transfer down and hardness up in that direction only; binary antichain embedding is not polynomial. Hardness/approximation results for general posets or arbitrary tests (Hyafil–Rivest, arbitrary subset tests ≠ pairwise comparisons; Cardinal et al., constant-factor approximation, not exact `S(P)`/completeness) do **not** transfer to antichain `S(n)` without an explicit reduction. Certificate **soundness** (valid witness ⇒ `S(n)≤k`) is distinct from **completeness** (witness exists for every yes-instance) and from many-one hardness/completeness of the language.

## 3. Serious falsification attempts

### 3.1 Falsifier attempt: construct `L ≤_m^p SORT-BOUND-U` (`L=TQBF`, PSPACE-complete)
A reduction must map `φ` (|φ|=`m`) in poly(`m`) time to `1^{n(φ)}#1^{k(φ)}` with `φ∈TQBF ⇔ S(n(φ))≤k(φ)`.
- **Size/encoding:** requires `n(φ)+k(φ)+1 ≤ poly(m)`; informative band is `S(n)=Θ(n log n)` but `k` is arbitrary.
- **Structure:** for each output length there are only polynomially many well-formed (and threshold-consistent yes) instances (sparse/tally-threshold structure). A reduction may vary output length, so a contradiction is not immediate from cardinality alone; NP-style pruning arguments (Mahaney) crucially exploit SAT disjunctive self-reducibility. `TQBF` has quantifier/PSPACE self-reduction structure, but I did **not** obtain a complete Mahaney/Ogihara–Watanabe-style argument yielding either `P=PSPACE` or an unconditional impossibility from `TQBF ≤_m^p SORT-BOUND-U`, nor a correct direct encoding of quantified alternation into the single antichain threshold `S(n)`.
- **Result:** [open] no reduction found; falsifier not constructed. Absence of construction is not a proof.

### 3.2 Barrier attempt: unconditional non-completeness by sparsity/isomorphism generalization
- **Berman–Hartmanis (EXPTIME):** gives an unconditional sparse-completeness exclusion for EXPTIME — exactly the template sought — but this does not transfer automatically to PSPACE (different padding/closure/census regime); I cannot certify a PSPACE instance of that theorem from the primary sources available here.
- **Mahaney/NP machinery:** for NP the standard consequence is conditional (`… unless P=NP`), not an unconditional non-hardness theorem; generalizing the proof method to PSPACE-complete sets would require a careful PSPACE-specific self-reducibility/census argument and primary-source verification.
- **Isomorphism conjecture framing:** not a proof of non-completeness for this specific sparse set without an established theorem instance.
- **Result:** [open] unconditional non-completeness not proved here.

**Concrete failed approach:** treating the unconditional EXPTIME sparse-completeness exclusion (Berman–Hartmanis 1977) as a black-box consequence of sparsity that applies equally to PSPACE is not justified by the cited facts available in-repo; PSPACE-specific padding/self-reducibility or census consequences must be established with verified primary sources.

## 4. Mathematical finding / honest limit
1. **[deduction] Settled vs open:** `SORT-BOUND-U` is sparse, in PSPACE, and unconditionally not many-one EXPTIME-complete (Berman–Hartmanis, as recorded). The analogous many-one **PSPACE-completeness** question is **not settled by the sparsity results currently established in-repo** (Mahaney/Fortune/Ogiwara–Watanabe/Karp–Lipton address NP/coNP/PH collapses; the EXPTIME argument is class-specific).
2. **[open] No falsifier:** no polynomial-time many-one reduction from a known PSPACE-complete language to `SORT-BOUND-U` was found/proved.
3. **[open] No unconditional barrier proof:** no complete, independently checkable proof was obtained that sparsity (or `SORT-BOUND-U`’s stronger `P/log`/`AC^0`/tally-threshold structure) unconditionally rules out many-one PSPACE-completeness.

This is an **exact obstruction**, not a proof and not a completeness claim.

## 5. Decisive next step (primary-source audit)
A resolution requires one of:
- a verified **primary-source theorem** showing (unconditionally, or under a hypothesis known false) that no sparse/tally language is `≤_m^p`-complete for PSPACE, with assumptions matching `SORT-BOUND-U`; or
- a complete **PSPACE-specialized census/self-reducibility argument** (e.g. from `TQBF ≤_m^p SORT-BOUND-U`) yielding `P=PSPACE` or an unconditional contradiction; or
- an explicit, fully proved **reduction** `TQBF → SORT-BOUND-U` (major, model-sensitive result).

Primary sources to verify (not fetched here; web search was unavailable/cancelled in this environment): Berman–Hartmanis 1977 (full scope beyond EXPTIME), Hartmanis 1978, Berman 1978, and census/collapse results for sparse hard sets of PSPACE under many-one reductions. Until audited, the front remains **open** (EXPTIME ruled out; PSPACE unresolved).

## Output 188 (msg_1cfeb04540018qxndu6nCUGEUs)

Recovery check complete. The prior turn produced a scratch report at `/tmp/opencode/pspace_completeness_report.md`; it made no repository changes or commits. Git remains clean at `6a96398`, and the #301 page-1 search found no matching post. No external side effect needs repeating.

The research remains unfinished mathematically: the report found neither a PSPACE-hardness reduction nor a verified unconditional sparse-PSPACE barrier. It records the EXPTIME exclusion and leaves PSPACE many-one completeness unresolved.
