# antonina-NBFYvvyrdbPgIEmFo3UV2k-prize

Session: ses_e11777b27ffeIfmOLwmlPoloZQ
Workspace: /home/lubko/soring-fronts/constant-truthtable-queries-for-unary-s-value
Created: 1795003286766; updated: 1795003948125

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 128 (msg_1ee8bec12001E2tU02lE8KfOgJ)

# Finding (all-`n`, mathematical): constant-query nonadaptive access is equivalent to constant-size poly-time candidate lists

## Scope / sources checked
- Studied `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, `docs/research-encoding-consequences.md` (§4 bounded-truth-table barriers), `docs/research-budgeted-dfs.md` (§5.3, §6), `docs/research-sergeev-asymptotic.md`, and `docs/research-frontier.json`.
- Checked board #301 via `scripts/board_digest.py` (`--recent 7` and searches for `truth-table`/`nonadaptive`/`constant-query`/`tt`/`parallel`/`binary search`/`Sergeev`): no prior post found attacking this exact front; related context includes adaptive-vs-nonadaptive/FO(TC) worst-case checking, certificate/succinctness barriers, and Sergeev-entropy discussion.
- Primary facts used [literature/definition]: `SORT-BOUND-U = {1^n # 1^k : S(n) <= k}`; `L(n)=⌈log₂ n!⌉ ≤ S(n) ≤ U(n)=O(n log n)`; `S(n)<=S(n+1)`; `S_unary ≡_T^p SORT-BOUND-U` via `O(log n)` adaptive threshold queries (`docs/problem.md`, `docs/research-budgeted-dfs.md` §6); Sergeev 2020: `S(n)=log₂(n!)+O(n/(log n)^(1/5)) = ⌈log₂ n!⌉ + o(n)` asymptotically, with no explicit finite constants/effective width extracted in-repo (`docs/research-sergeev-asymptotic.md`, ECCC TR20-096 Thm. 3 / journal DOI 10.1134/S0965542521020111). Ogiwara–Watanabe 1991 bounded-tt barrier in the repo concerns many-one/btt hardness *of sparse sets* (opposite reduction direction) and does not apply to this front.

## Model (made precise)
Let `A = SORT-BOUND-U`. A uniform polynomial-time nonadaptive (truth-table) reduction with `c` queries from `S_unary` to `A` is a pair of poly-time algorithms `(Q,E)` with
- `Q(1^n) = (q_{n,1}, ..., q_{n,c})`,
- `b_{n,i} = χ_A(q_{n,i}) ∈ {0,1}`,
- `E(1^n, b_{n,1}, ..., b_{n,c}) = S(n)` for all `n >= 1`.

`Q` may choose any well-formed instances in `A`’s domain (same or different `m,k`) as a function of `n` only (nonadaptive). This is the standard `FP^{||A}_tt[c]` notion.

## Theorem 1 [deduction]: characterization by constant-size poly-time candidate lists
For fixed `c >= 0`, the following are equivalent:
1. `S_unary ∈ FP^{||SORT-BOUND-U}_tt[c]`.
2. There is a poly-time computable function `L` with `|L(1^n)| <= 2^c` and `S(n) ∈ L(1^n)` for all `n >= 1` (`S_unary` is `2^c`-list-computable in uniform polynomial time on unary input).

Moreover, `(2)` implies `(1)` already with `2^c-1` same-input threshold queries of the form `(1^n # 1^k)`. Hence, for computing `S_unary`, constant nonadaptive query access to the full language `SORT-BOUND-U` has no more power than constant nonadaptive same-input threshold access (up to the list/query constant factor), and in particular cross-input queries `m != n` cannot circumvent the constant-list barrier.

**Proof.**
- `(1) ⇒ (2)`: Define `L(1^n) = { E(1^n, β) : β ∈ {0,1}^c }`. Since `c` is constant, `|L(1^n)| <= 2^c` and `L(1^n)` is computable in `2^c * poly(n)=poly(n)` time. For the true answer vector `b(n)`, correctness gives `S(n)=E(1^n,b(n)) ∈ L(1^n)`.
- `(2) ⇒ (1)`: Let `L(1^n)={v_1 < ... < v_m}` with `m <= 2^c` and `S(n)=v_j`. Ask queries `q_i=(1^n # 1^{v_i})`, `i=1..m-1`, all computable in poly-time from `1^n` and issued nonadaptively. Answers are `b_i=[S(n) <= v_i]`, so `b_i=0` iff `v_i < S(n)` and `b_i=1` iff `v_i >= S(n)`. Therefore `j = 1 + |{i : b_i=0}|` and output `v_j = S(n)`. This is a uniform poly-time tt-reduction with `m-1` same-input threshold queries. ∎

**Refinement (same-input threshold shape) [deduction].** If every query has the form `q_i=(1^n # 1^{k_i(n)})`, sort thresholds `k_{p1}<...<k_{pr}` (`r<=c`); then `b(n)` is one of the `r+1 <= c+1` monotone patterns consistent with `v <= k_{p1}`, `k_{pi} < v <= k_{p,i+1}`, or `v > k_{pr}`. Thus such a reduction yields a stronger ` (c+1)`-list `L'(1^n)=\{E(1^n,\beta): \beta \text{ monotone}\}`. Conversely a `(c+1)`-list is selectable by `c` same-input threshold queries as above. So same-input threshold tt-reductions are exactly `(c+1)`-list computations.

## Consequences for the front

- **Equivalent restatement.** The front
  > “Is there a fixed constant `c` such that for all `n >= 1`, `S(n)` is computable from `1^n` by a uniform poly-time `c`-query nonadaptive reduction to `SORT-BOUND-U`?”
  
  is equivalent to: *is there a fixed constant `k` and poly-time `L` with `S(n) ∈ L(1^n)` and `|L(1^n)| <= k` for all `n`?* I.e. constant parallel threshold-oracle access is exactly the power to resolve constant ambiguity, not to determine `Θ(log n)` bits of value over an unbounded candidate set except by precomputing a constant-size candidate family.

- **Contrast with known adaptive access [deduction/literature].** Since `L(n),U(n)` are poly-time computable and `U(n)-L(n)=O(n log n)` (or `o(n)` above `L(n)` asymptotically by Sergeev, but at least a known poly(n) window), `O(log n)` *adaptive* queries to `SORT-BOUND-U` determine `S(n)` by binary/linear-threshold search (`docs/problem.md`, `docs/research-budgeted-dfs.md` §6). Theorem 1 isolates nonadaptivity/constant-query as a genuine restriction: collapsing adaptive `O(log n)` to nonadaptive `O(1)` would require constant-size poly-time listability of `S_unary`.

- **`c=0` sanity check.** `c=0` iff `|L(1^n)|<=1` iff `S_unary ∈ FP`.

## Falsifier status (attempted) — no unconditional resolution

**Falsifier target:** for every constant `c` there exists `n` with no `c`-query uniform poly-time nonadaptive reduction determining `S(n)`.

By Theorem 1 this is equivalent to: for every constant `k`, no poly-time `k`-list contains `S(n)` for all `n`.

**Not proved / not disproved (honest limit).**
- I did **not** obtain an unconditional proof of this falsifier, and I did **not** construct a constant-query reduction/candidate list.
- An unconditional falsifier would imply in particular `S_unary ∉ FP` (take `k=1`), and more generally rule out constant-ambiguity poly-time computation of `S(n)`. Proving a uniform superpolynomial lower bound for a natural problem in `PSPACE`/`P/poly` is beyond currently known techniques (`docs/problem.md` “Realistic outcomes”: `SORT-BOUND-U` is in `PSPACE` and, as a tally language, in `P/poly`; uniform super-polynomial separation would need methods not known for any natural PSPACE problem). So an information-theoretic/structural all-`c` falsification in the strong unconditional sense appears out of reach here.
- Conversely, a positive answer is not supported: `S_unary ∈ FP` is open; Sergeev 2020 gives `S(n)=⌈log₂ n!⌉ + o(n)` [literature] but only asymptotically, with no effective constant bound, so it does **not** yield `|L(1^n)|=O(1)` and does **not** rule it out (an `o(n)` width may still be `ω(1)`).

## Concrete failed / insufficient approaches (and why)

1. **Naive counting on the fixed function [failed as stated].** One cannot argue “`c` bits < `log |window|` so impossible” directly for the actual `S`, because `b(n)` is a deterministic function of the fixed `S` and `Q(n)`; correctness requires only `E(1^n,b(n))=S(n)` on the true `b(n)`, not separation of hypothetical `S`-values. The correct invariant is Theorem 1: regardless of correlation, the reduction induces the poly-time list `E(1^n,·)`, so the unavoidable necessity is *constant listability*, not raw bit-counting against the true singleton.
2. **Same-input “threshold interval must be singleton” as an absolute impossibility [insufficient].** For queries `(1^n # 1^{k_i})`, `b(n)` identifies which of `c+1` threshold intervals contains `S(n)`. This does force `S(n)` into a `c+1`-list (Theorem 1 refinement), but it does **not** by itself force `S_unary ∈ FP` or force incorrectness: a fixed `E` could in principle satisfy `E(1^n,b(n))=S(n)` without naming the interval boundary as a query. It becomes a hardness only insofar as constant listability is hard/open.
3. **Cross-input monotonicity propagation as extra power [does not beat characterization].** A query `(1^m # 1^k)` yields a numeric consequence on `S(n)` only in cases `m>=n, b=1 => S(n)<=k` or `m<=n, b=0 => S(n)>=k+1` [deduction from `S` monotone]; these can tighten a computable interval but still feed only `c` answer bits total. Theorem 1 shows they cannot produce more than a `2^c`-list, and any `2^c`-list is already selectable via same-input queries — so cross-input queries give no asymptotic advantage for this front.
4. **Sergeev/window argument [inconclusive].** Known/claimed uncertainty is `⌈log₂ n!⌉ + o(n)` [literature, asymptotic, non-effective in-repo]: too wide to certify a constant list, not provably `ω(1)` in an effective form that would exclude one. I found no finite effective narrowing to `O(1)` and no proof of unbounded effective width.

## Exact obstruction
The front reduces cleanly to a sharp open condition but is not closed by available methods:
- **Solved here:** structural equivalence `FP^{||SORT-BOUND-U}_tt[O(1)] ⇔ O(1)`-listable in poly-time; same-input thresholds suffice; cross-input queries add no list power. (Independently checkable by the short proof above.)
- **Open:** decide that listability condition for the specific function `S`. A proof of the falsifier needs (at least) a theorem that `S(n)` cannot lie in any fixed-size poly-time enumerable set for infinitely/all sufficiently large `n`; a proof of the positive answer needs an explicit constant-size poly-time candidate generator. Neither follows from current repo results, Sergeev’s asymptotic bound, or standard sparse-set btt theorems, and an unconditional negative would subsume a separation far beyond the known `PSPACE ∩ P/poly` landscape for this tally language.

**Bottom line:** I did not disprove or prove the existence claim; I proved the precise all-`n` characterization that any constant-`c` nonadaptive truth-table reduction to `SORT-BOUND-U` exists iff `S(n)` is uniformly `2^c`-list-computable in polynomial time (a barrier/normal form), and identified the unconditional falsifier as open for the same reason strong uniform lower bounds for `S_unary` are open. No Lean/repository changes were warranted (no independently checkable new theorem/counterexample beyond this reported deduction, and no closure of the front).
