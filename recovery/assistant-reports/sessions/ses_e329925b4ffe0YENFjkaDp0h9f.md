# antonina-XxSNxZYA5QJ4JOdIsOfSuD-expense

Session: ses_e329925b4ffe0YENFjkaDp0h9f
Workspace: /home/lubko/soring-fronts/sergeev-effective-window-20261111
Created: 1794447432269; updated: 1794456629781

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 223 (msg_1cdf2037700167llSlfv7vZn7y)

## Recovery / prior-state inspection (no duplicated side effects)

- **Git/worktree state (current checkout):** `/home/lubko/soring-fronts/sergeev-effective-window-20261111` is a git worktree (`.git` -> `/home/lubko/soring301/.git/worktrees/sergeev-effective-window-20261111`), `git status --short` clean, HEAD `6a96398` (Merge commit `6859bc2` into `research/exact-reset-tree-realizability-20261027`), recent log shows `cc50630`/`6859bc2` "Recognize Antonina clearexit for research-frontier completion" etc. No local uncommitted changes found here.
- **Board #301 check (before any posting):** `board_digest.py --contains "Sergeev"` -> no matches; `--contains "effective"` -> no matches; `--contains "surplus"` -> only an unrelated 2026-10-24 `conp-adversary-memory` mention (budget surplus `d=k-C(n)`, not Sergeev comparison surplus). Recent pages show no posted Sergeev effective finite-window result. **I did not post to #301.**
- **Prior/related local artifacts inspected (read-only, in other worktrees):**
  - `docs/research-sergeev-asymptotic.md` (this repo and other front worktrees): records Sergeev TR20-096 Thm 3 as **primary theorem, not Lean-checked** `S(n)=log₂(n!)+O(n/(log n)^(1/5))`, explicitly notes "asymptotic big-O alone does not supply explicit constants or a finite computable upper-bound function for every input" and that extraction is a separate task.
  - `/home/lubko/soring-fronts/audit-sergeev-lemma2-finite-20261105/docs/sergeev-lemma2-finite-losses-audit.md` (uncommitted `??` in that separate worktree; not modified): independent paper-audit of an artifact targeting B6 recurrence closure / B3 Lemma 2 finite losses. It concludes the artifact identifies the right missing finite data but treats key TR20-096 internals as `[uncertain extraction]`/not primary-verified and notes gaps preventing a discharged effective bound. Consistent with "no extracted effective finite bound".
  - Frontier ledger `~/.local/state/soringp1/frontier-ledger.json` contains Sergeev-related investigated fronts (`sergeev-group-framed-dag`, `sergeev-canonical-ceiling-audit`, `referee-sergeev-ceiling-accounting-20261027`) focused on certificate/ceiling/framed-DAG questions, not on extracting an explicit finite constant/range for `S(n)-⌈log₂(n!)⌉`.
- **No repo/Lean changes, no commits, no PRs, no posts made.**

## Primary source inspected

- **I. S. Sergeev, _On the asymptotic complexity of sorting_, ECCC TR20-096 (2020), https://eccc.weizmann.ac.il/report/2020/096/** (downloaded PDF to `/tmp/opencode/sergeev_tr20_096.pdf`, 31 pages; text extracted via `pypdf`). Journal version noted by repo: DOI 10.1134/S0965542521020111.
- **Theorem 3 (p. 29):** `S(n) = log(n!) + O(n log^{-1/5} n)`.
- **Model/scope:** comparison-sorting algorithm (group insertion), number of pairwise comparisons while sorting `n` elements. This is an **upper bound on the sorting function/algorithm cost** in comparisons, **not** an algorithm or time bound for evaluating exact `S(n)`, and **not** a complexity-class separation/membership claim for `SORT-BOUND-U` (cf. `docs/problem.md`, `AGENTS.md`).

## Falsifiable result

**Claim (extraction/obstruction, paper-level):** *Sergeev TR20-096 proves the asymptotic comparison upper bound but, as stated, does not yield a rigorously quantified explicit finite bound of the form*
\[
S(n)-\lceil\log_2(n!)\rceil \le C\,\frac{n}{(\log_2 n)^{1/5}} \qquad \text{for all } n\ge n_0
\]
*(or any other fully explicit finite function/range for the comparison surplus over all sufficiently large or all finite `n`) with all constants and the valid range justified from the paper alone.* Equivalently, obtaining such a bound from this proof is a **separate effectivization/extraction task**: one must supply explicit finite values/bounds for every hidden constant, parameter choice, range condition, and finite prefix/base in the chain of lemmas and the final recurrence.

**Why this follows from the paper (exact non-effective loci):**

1. **Theorem 2 / Corollary 2 are asymptotic, not fully explicit.** Thm 2 (p. 28–29): for `a ≥ 2` and `2^{a/4} ≤ m ≤ 2^{a/2}`, `P_m(a) ≥ 2^{a+1/2} - O(a^{-γ}·2^a)` with `γ` "small enough, say, γ = 1/5". Proof: "For `a < 100`, the inequality (44) holds with sufficiently large values of the constant hidden behind the symbol `O`. Thus, we may assume `a ≥ 100`." Then sets `ϕ = log(mε/(4a^2))`, `s = ⌈2γ log a⌉`, and derives the final big-O chain (p. 29) with terms `O(2^{-s/2})`, `O(2^{-s})`, `O(2^a/a^2)`, `O(2^a·e^{-Θ(a·s^{-2}·2^{-2s})})` collapsed to `O(a^{-γ})`. Corollary 2 states `Q_{2m}(a) ≥ 2^a - O(a^{-1/5}·2^a)`. No explicit multiplicative constant or a uniform finite `a_0` covering all `a` is written out.
2. **Lemma 4 (strategy/system existence) has explicit parameter conditions but a nontrivial constructive proof with many estimated inequalities.** Lemma 4 (p. 26–27): for `s ≥ 20`, `d=2^s`, `µ=30·2^{-s}`, `λ=20·2^{-s/2}+64·2^{-s}`, `ε=1/(25·2^s)`, `y_i=i/d`, `v_i=(1-λ)·2^{y_i+1/2}`, it asserts `v∈T(σ[s])`, `u=v/2∈T^ε(σ[s])`. The proof (pp. 24–28, §6.5) establishes feasibility by a sequence of geometric length/partition bounds (e.g. (30),(32)-(39),(41)-(43) and reduced forms) with statements like "it is easy to verify", choices satisfying (38), and derived gaps `> ε` (e.g. `> 1/(24·2^s) > ε`, `> 1/(6·2^{s/2}) > ε`, `> 1/(25·2^s)`). Turning these into a single explicit, uniform finite inequality requires checking every intermediate numeric bound and normalization for the stated parameter regime; the paper does not package them as an explicit constant-carrying finite lemma statement.
3. **Lemma 2 is explicit in form but depends on the above and introduces further parameters/ranges.** Lemma 2 (p. 10, (17)-(18)) gives
   `P_m(r + y_i + (r+2)ϕ·2^ϕ/m) ≥ v_i·2^r - (R/ε)m·2^{ϕ+2} - R·2^r·exp(-ε/(2R)(ϕ/(w(d+1)(h+1)) - 2))` under conditions `m ≤ min{u_min, ε/2}·2^{r-ϕ-1}`, `u_i < v_i`, `u_i ≤ π(y_i)`, `R=||v-u||`, strategy depth `h`, width `w`. Its effective use in Thm 2 requires the concrete `v,u,ε,R,h,w,d,y_i` and valid `(r,m,ϕ)` ranges from Lemma 4; the exponential/rounding side conditions are then absorbed into big-O terms in Thm 2 rather than carried as an explicit finite inequality for all admissible `a`.
4. **Theorem 3 proof introduces further non-explicit choices and approximations.** Thm 3 (pp. 29–30): divides into pairs, sorts larger elements (`n/2 + S(n/2)`), inserts first `n_0 = n/log n` elements `α_i` by Ford–Johnson "by `n + O(n_0)` comparisons", splits remainder into groups of size `m ≈ √n/log n`, inserts groups via Corollary 2, "last group may contain less than m elements, so we use trivial binary method to insert them". For group `t`, `L_t = 2(n_0 + tm) - m` and `ρ_t = log L_t + O(log^{-1/5} n)` (Cor. 2), so insertion cost `≤ ρ_t·m`. Excess over the ideal (45) is estimated as `O(n_0 + m) + O((n/2 - n_0) log^{-1/5} n)` using `log(2k+m)=log(2k-1)+O(log^{-1/5} n)` for `n_0 < k < n/2-m` and `log(2k-1)+O(1)` at ends. This yields recurrence `s(n)=S(n)-log(n!) ≤ s(n/2) + O(n log^{-1/5} n)` and concludes "`s(n)=O(n log^{-1/5} n)`" trivially. **Not explicit:** the meanings/ranges of `≈` for `m`, the exact handling/count of all edge cases (small `n`, last/partial group, regime where `m`/`n_0` are valid relative to Cor. 2's `2^{a/4} ≤ m ≤ 2^{a/2}` and `a` large enough), the constant in `n+O(n_0)` Ford–Johnson prefix, the constant in `ρ_t`, the log-base conventions in comparisons-to-bits steps, and the finite basis/cutoff `n_1` needed to close the recurrence to `s(n) ≤ C n/(\log n)^{1/5}` for all `n≥n_1`.
5. **Logarithm base / surplus form is a minor but necessary explicitness point.** Theorem 3 is written `log(n!)` (natural/base unspecified in that line); standard comparison-count/information form is `log₂(n!)` and the target surplus is usually `S(n)-⌈log₂(n!)⌉`. Any effective finite bound must fix the base and relate `log` vs `log₂` and `⌈·⌉` explicitly (a constant-factor/`O(n)`-scale detail that is easy but must be stated).

**Falsification condition (what would refute this "no effective bound yielded" claim):** exhibit a concrete derivation from TR20-096's stated definitions/lemmas/theorems (possibly with routine, fully justified finite arithmetic/unfolding of its own estimates, but without new algorithmic ideas beyond the paper) producing explicit `C, n_0` (and base) such that `S(n) ≤ log₂(n!) + C n/(log₂ n)^{1/5}` for all `n ≥ n_0`, with every inequality step and range/base-case accounted for. Conversely, a small-`n` numerical check cannot falsify the asymptotic theorem and is irrelevant here except as sanity context (known exact `S(n)` up to small `n` are far below any coarse asymptotic envelope).

## Distinction of claim types

- **Theorem (literature, primary):** Sergeev TR20-096 Thm 3 proves `S(n)=log₂(n!)+O(n/(log n)^(1/5))` for the comparison complexity of sorting. Cor. 2/Thm 2/Lemmas 2,4 provide the group-insertion machinery supporting it.
- **Extraction (not established by the paper as written):** an explicit finite `(C,n_0)` or computable finite bound for `S(n)-⌈log₂(n!)⌉` over a stated range. **Absent.**
- **Experiment:** none performed/needed; the obstruction is the lack of explicit constants/ranges in the proof chain, not an empirical discrepancy.
- **Deduction (this report):** the listed loci (1)-(5) show the proof contains multiple unquantified big-O/`≈`/"sufficiently large"/"trivially follows"/edge-case steps, so it does not by itself constitute a rigorous finite quantified bound. This is consistent with prior local audit notes (`audit-sergeev-lemma2-finite-20261105`).

## Bottom line

- **Effective finite bound with all constants and range justified:** **not provided by Sergeev TR20-096** as stated.
- **Reason (precise):** the asymptotic result is proved, but constants/ranges are hidden across Cor. 2/Thm 2/Lemma 4/Lemma 2 and the Thm 3 recurrence/prefix/grouping approximations (pp. 10, 24–30), so finite quantification requires a nontrivial, separate explicit extraction/closure not carried out in the paper (and no such verified extraction was found in inspected repo artifacts/#301).
- This does **not** show impossibility of effectivization; it only establishes that the primary paper does not currently yield the requested explicit finite bound. No claim about `P/NP/PSPACE`, `SORT-BOUND-U` membership/separation, or exact `S(n)` evaluation is made.
