# antonina-jeEythCwoCGToerrrvrOMS-segments

Session: ses_e0644422effe6YalCTg8PpPf1U
Workspace: /home/lubko/soring-fronts/winning-family-obdd-order-alln
Created: 1795191193111; updated: 1795192103645

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 92 (msg_1f9c3ad80001pkjBGxGutVDr1l)

## State / recovery check (no duplicate external effects)
- Working tree: clean (`git status --porcelain -uall` empty), HEAD `6a96398` on `main` history state present locally; no local commits, no repo files added/modified, no Lean changes.
- Board #301 inspected via `/home/lubko/soring301/scripts/board_digest.py` (recent, and filtered for `fixed-order poset BDD`, `symbolic-poset-dd-obstacle`): recent posts on 2026-11-20 include `fixed-order poset BDD` (15:05:48Z, result reported as “C: precise obstruction; no width theorem proved”) and `symbolic-poset-dd-obstacle-20261120`. I found no prior post/result by this session and performed **no** board posts, commits, purchases, or other external actions here.
- Read: `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/research-plan.md`, `docs/literature.md`, `docs/upper-bound.md`, `docs/research-state-compression.md`, `docs/research-frontier.json`, and board excerpts above.

## Front attacked (exact, all-`n` falsifiable)
Let `m = C(n,2)`. Fix the pair-lex ternary encoding by variables `V_n = {x_{ij}, y_{ij} : 1 ≤ i < j ≤ n}` with `(x_{ij},y_{ij}) = 10 ↦ i<j`, `01 ↦ j<i`, `00 ↦ incomparable`, `11 ↦ illegal`. Let `W_{n,d} : {0,1}^{V_n} → {0,1}` be 1 iff the assignment encodes a valid strict partial order `P` on `[n]` and `P` is sortable within `d` adaptive comparisons, i.e. `F(P) ≤ d` for the minimax value
`F(P)=0` if `P` total, else `F(P)=1+min_{(u,v)∈Inc(P)} max(F(P+u<v), F(P+v<u))` (definition; model fixed in `docs/problem.md`, recurrence in `docs/upper-bound.md`, `F(∅)=S(n)`).

**Question.** Is there any fixed variable order (a total order on `V_n`, possibly depending on `n`) under which every `W_{n,d}` has OBDD width polynomial in `n,d` uniformly? Or is the minimum width over all variable orders superpolynomial for an infinite family `(n,d)`?

**Falsifier routes.** (1) exhibit one fixed order with `width(W_{n,d}) ≤ poly(n,d)` for all `n,d`; or (2) prove a superpolynomial all-order lower bound for some infinite family.

**Complexity implication (standard, conditional on the route).** A uniformly polynomial-width and polynomial-time constructible OBDD for `W_{n,k}` evaluated at the antichain encoding would decide `SORT-BOUND-U = {1^n#1^k : S(n) ≤ k}` in polynomial time. An all-order superpolynomial width lower bound would rule out this fixed-order (O)BDD representation/evaluation route only; it would not by itself rule out other DD models or other algorithms, and (given `SORT-BOUND-U ∈ PSPACE`, `docs/problem.md`) an unconditional superpolynomial separation from P is not a realistic target here.

## Prior-work / board position (as checked)
- Board `fixed-order poset BDD` (15:05Z) reports a precise obstruction, no width theorem, for this fixed encoding/question; `symbolic-poset-dd-obstacle-20261120` treats encoding/order as unspecified. I do not claim novelty over that obstruction; the result below sharpens it by a checkable lower bound against the canonical pair-lex variable order for a specific family member.
- General-poset/state-compression results do **not** settle this: the minimax state set is exactly labelled posets / quotients (`docs/research-state-compression.md`) but OBDD width here is about a *fixed-order read-once* representation of the characteristic functions `W_{n,d}` over pair bits, not about DP memoization classes. Certificate **soundness** of a proposed compact strategy/diagram is distinct from **completeness** (exactly `W_{n,d}` for all valid `P` and the claimed `n,d`).

## Mathematical findings

### 1. [deduction] Exponential OBDD width for `W_{n,0}=TOT_n` under the pair-lex variable order
`W_{n,0}(P)=1` iff `P` is a total linear order (a non-total poset needs ≥1 comparison). Let `π_lex` be the variable order reading pairs in lex order `(1,2),(1,3),…, (1,n),(2,3),…, (n-1,n)` with bits `(x_{ij},y_{ij})` consecutively. Let `S={2,…,n}` and let `ρ_A` be the prefix assignment after the first `n-1` pairs, for `A ⊆ S`, defined by
`ρ_A(x_{1j},y_{1j}) = 10` if `j∈A`, else `01` (`j∈S\A`, i.e. `j<1`).

**Claim.** For `n ≥ 2` and distinct `A,B ⊆ S`, the subfunctions `W_{n,0}|_{ρ_A}` and `W_{n,0}|_{ρ_B}` differ. Hence `width_{π_lex}(W_{n,0}) ≥ 2^{n-1}`.

**Proof.** Assume `A ≠ B`. Note the semantic constraint of a prefix: `ρ_A` means `1<j` for `j∈A` and `k<1` for `k∈S\A`, so by transitivity any total order extending `ρ_A` must satisfy `k<j` for all `k∈S\A, j∈A` (and is a total order on `S`).

- *Case I: there exist `j∈A\B` and `k∈B\A`.* Then `ρ_A` forces `k<j` (`k∈S\A, j∈A`) while `ρ_B` forces `j<k` (`j∈S\B, k∈B`). Let `τ` be any assignment to remaining pairs encoding a total order on `S` with all `S\A` before all `A` (e.g. concatenate an arbitrary total order of `S\A` with one of `A`); this is consistent with `ρ_A`, so `W_{n,0}(ρ_A τ)=1` and `τ` contains `k<j`, contradicting `j<k`, hence `W_{n,0}(ρ_B τ)=0`.
- *Case II: `B ⊊ A`* (the only remaining case up to symmetry, since if neither difference is empty Case I applies). Pick `j∈A\B` and set `D = A∩B = B`, `E = S\A`, so `S` is partitioned into `E, D, {j}` with `E=S\A ⊆ S\B = E∪{j}` and `D=A\B`? more directly: `S\A = E`, `A = D∪{j}` (disjoint), `B=D`. `ρ_B` requires all `D < all (E∪{j})`; `ρ_A` requires all `E < all (D∪{j})`. Choose `τ` as the total order `E < {j} < D` on `S` (arbitrary within `E,D`). Then `E < D∪{j}` holds and `j<D` is allowed, so `ρ_A τ` is a total order and `W_{n,0}(ρ_A τ)=1`. But `ρ_B` requires every element of `D` to be `< j` (`D ⊆ B`, `j ∈ S\B`), while `τ` has `j < D`; since `D=B ≠ ∅` in this proper-subset case, `W_{n,0}(ρ_B τ)=0`.
- *Case III: `A ⊊ B`.* Symmetric to Case II, swapping `A,B`.

Thus all `2^{n-1}` prefixes yield distinct subfunctions. ∎

**Consequence.** The canonical pair-lex variable order is **not** a uniform polynomial-width order for the family `{W_{n,d}}_{n,d}` (it fails already at `d=0`, exponentially in `n`, hence superpolynomial in `|V_n|=Θ(n^2)`). This is a concrete falsification of route (1) restricted to that order, not of route (1) in general.

### 2. [deduction / obstruction] Why this does not settle “any fixed variable order” and why route (2) is nontrivial
- To obtain an all-order lower bound for some family `(n,d(n))` one needs, for **every** variable order `π` on `V_n`, some cut/prefix with superpolynomially many subfunctions of `W_{n,d}` (a fooling-set/rank/1-way-communication obstruction uniform over all `π`). 
- For `TOT_n=W_{n,0}`, the opposite-constraint argument above shows many vertex-split prefixes force distinctions, but a variable order may interleave bits/pairs across vertices; a full all-order theorem would have to account for arbitrary interleaving while transitivity couples non-adjacent pairs globally. I did not obtain (and do not claim) such a theorem.
- For `d ≥ 1`, `W_{n,d}(P) ≡ [∃(u,v)∈Inc(P): W_{n,d-1}(P+u<v) ∧ W_{n,d-1}(P+v<u)]` is an alternating/game value over the same relation bits: the relevant “information” a prefix must retain is not a local visible-pair count but the exact minimax winnability consistent with all completions, against an adaptive adversary/chooser (soundness/completeness of any summary is the issue). Known failures of scalar/leaf-count invariants to determine `F(P)` (e.g. `e(P)` insufficient; `S(12)>⌈log₂ 12!⌉`, per `docs/literature.md`/notes) indicate the value is strictly stronger than information-theoretic counting, but this is an **obstruction to naive summaries**, not an all-order OBDD width lower bound.
- Conversely, route (1) would require a fixed scan order and a polynomial-state invariant computable read-once from pair bits that is complete for `F(P) ≤ d` for all `P,n,d`; no such invariant/order is exhibited, and `F(P)` is not determined by coarse invariants (above).

## Concrete failed approach (this pass)
- **Attempted:** promote the pair-lex `2^{n-1}` subfunction argument (Case I/II/III, proved above for the `n-1` vertex-1 pairs prefix) to an all-order superpolynomial lower bound for `TOT_n` or some `W_{n,d}`, e.g. by finding, in every order, a vertex/star cut or a balanced partition with a large fooling set despite arbitrary interleaving and transitivity. 
- **Outcome:** failed to produce a complete all-order argument. The obstruction is precise: arbitrary `π` can distribute/incur pair bits so that the “vertex-split” opposite constraints are not presented as a single pure prefix of the same simple form, and I lack a reduction showing every induced cut still carries superpolynomial residual dependence for this transitive/game-defined family. Therefore this remains a **precise obstruction**, not a theorem.

## Honest limits / status
- **Not proved:** existence of any fixed polynomial-width (uniform in `n,d`) variable order for all `W_{n,d}`. **Not proved:** a superpolynomial OBDD width lower bound holding simultaneously for every variable order for any infinite family `(n,d)` (the asked all-order falsifier). The front remains **open**.
- **Established here:** a rigorous, independently checkable all-`n` lower bound `width_{π_lex}(W_{n,0}) ≥ 2^{n-1}` (pair-lex order), falsifying that specific natural order; and a clarified separation between (i) this fixed-order obstruction, (ii) the unproved all-order DD question, and (iii) general-poset / certificate-soundness observations (which do not imply completeness or an OBDD width theorem).
- No repository/Lean changes were made (nothing here meets the publication gate as a new theorem/counterexample resolving the front or a necessary model fix). Any further claim would require either an explicit poly-width order+proof (route 1) or a verified all-order fooling-set/rank lower bound for a concrete `(n,d)` family (route 2).
