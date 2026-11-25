# antonina-PLSzcYBBbAMmRTDsurPYGt-wooded

Session: ses_e17d944f6ffeWIt8cFkBo9zPnD
Workspace: /home/lubko/soring-fronts/conp-refutation-dag-certificate-alln
Created: 1794896214876; updated: 1794896837587

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 80 (msg_1e82ea405001DUyV0iKxFrG2Zo)

## Recovery / side-effect audit (billy-dev, this session)
- **Repo/worktree state:** `/home/lubko/soring-fronts/conp-refutation-dag-certificate-alln`, git clean (`git status --porcelain --untracked-files=all` empty), HEAD `6a96398` on `main` history as shown (`git log -10`). No files created/modified by this session.
- **Durable external actions:** none performed. I did **not** post to Antonina/board #301, create commits/PRs/branches/worktrees/issues, or run Lean/builds that change repo state.
- **Prior context inspected:** `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/research-frontier.json`, board #301 digest via `python3 /home/lubko/soring301/scripts/board_digest.py --recent 7`, and targeted docs (`docs/research-encoding-consequences.md`, `docs/research-strategy-certificates.md`, `docs/research-certificates-barriers.md`, plus greps for `coNP`/`refutation`/certificates). No prior work product attributable to this exact front was found in the worktree; any earlier attempt by a failed backend turn is unknown to me beyond the board, so nothing was repeated.

## Front (fixed)
- **Question.** For all integers `n >= 1`, `k >= 0` with `S(n) > k`, does there exist a polynomial-time verifiable refutation object of size polynomial in the unary input length `N = n+k+1` proving that every adaptive comparison strategy on `n` keys requires more than `k` comparisons?
- **Falsifier (as stated).** An explicit infinite family `(n_i,k_i)` with `S(n_i)>k_i` such that every sound refutation system checkable in time `poly(N_i)` requires certificates of superpolynomial size in `N_i`, or an unconditional superpolynomial lower bound for a natural complete refutation format.
- **Complexity meaning.** A uniform positive answer (a fixed poly-time verifier, poly-bounded certificates for all NO instances of `SORT-BOUND-U = {1^n#1^k : S(n) <= k}`) would place `SORT-BOUND-U` in **coNP** (strengthening `SORT-BOUND-U ∈ PSPACE`, `docs/problem.md`/`docs/research-certificates-barriers.md` Claim A), without implying a separation. A verified lower bound of the stated “every sound refutation system…” strength would rule out an entire class of succinct NO-certificates (and, if uniform over all such systems, would witness `SORT-BOUND-U ∉ coNP`).

## Primary sources / established facts used (literature/deduction from repo docs)
- **Model/encoding (definition, `docs/problem.md`).** `S(n)` is the minimax height of deterministic adaptive comparison sorting of `n` distinct labelled keys; `N=n+k+1`. `S_unary ∈ FP ⇔ SORT-BOUND-U ∈ P`; explicit optimal trees are not polynomial certificates.
- **Known upper bounds (literature/deduction).** `⌈log2 n!⌉ <= S(n) <= O(n log n)`; `SORT-BOUND-U ∈ PSPACE` via the alternating comparison game / budgeted search (`docs/research-certificates-barriers.md`, `docs/research-budgeted-dfs.md`). `SORT-BOUND-U` is sparse/tally-like, hence in `P/poly` and even `P/O(log N)` / nonuniform `AC^0` as a language (`docs/research-encoding-consequences.md` Thms 3.3, 3.7, 3.10); these are **nonuniform** and do not give uniform P/NP/coNP.
- **Certificate status (deduction/open, `docs/research-encoding-consequences.md` Thm 5.4, `docs/research-strategy-certificates.md` Rem 1.3/4.3).** No succinct polynomial certificate is known for `S(n) <= k` or for `S(n) > k`. A strategy/DAG verifier is sound and runs in time polynomial in the certificate/DAG size, but **soundness/completeness of the verifier given a witness is not a size/existence bound**: no polynomial bound is known for yes- or no-witness size on the antichain root for all `n`. `log2 e(P)` is `#P`-hard to compute exactly and not tight (`S(12)=30>29`).
- **Barriers (literature, Mahaney/Fortune/Ogiwara–Watanabe/Karp–Lipton; `docs/research-encoding-consequences.md` §4).** Sparsity blocks ordinary many-one (and stronger restricted) NP-/coNP-hardness of `SORT-BOUND-U` unless `P=NP` / PH collapses, but gives **no** membership in NP or coNP and **no** hardness of `SORT-BOUND-U`.
- **Model distinctions (literature, `docs/research-certificates-barriers.md`, `docs/research-hardness-boundaries.md`).** Hyafil–Rivest/Laber–Nogueira concern arbitrary tests/expected or worst-case decision trees over given instances; Parberry concerns fixed sorting-network (oblivious) verification (coNP-complete in that model). These are **not** results about adaptive comparison-tree minimax for the fixed root family `S(n)` and do not transfer without a reduction.

## Mathematical analysis of the front

### 1. Precise reformulation (deduction)
Let the NO-language be `L_NO = {1^n#1^k : S(n) > k}` (unary). A “polynomial-time verifiable refutation object of size polynomial in `N` for all NO instances” is exactly: there exists a deterministic TM `V` and polynomial `p` such that
- **Completeness:** `x ∈ L_NO ⇒ ∃w, |w| <= p(|x|) ∧ V(x,w)=1`.
- **Soundness:** `V(x,w)=1 ⇒ x ∈ L_NO` (equivalently, no YES-instance of `SORT-BOUND-U` is accepted).
- **Efficiency:** `V` runs in time polynomial in `|x|+|w|`.

This is equivalent to `L_NO ∈ NP`, i.e. `SORT-BOUND-U ∈ coNP`. The front therefore asks for a uniform coNP-style succinct NO-certificate theorem; disproving it in the strongest stated form asks for a proof-complexity/certificate-size lower bound against **all** such `(V,w)` systems.

### 2. Canonical complete refutation format: minimax/adversary-strategy certificate (deduction; sound and complete, size unknown)
Write states as posets `P` on `[n]` and `F(P)` for minimax height (`F(∅)=S(n)`; `docs/problem.md`, `SoringP1/Minimax.lean` correspondence is stated complete there). For budget `r = k - depth >= 0`,
- `F(P) > r` iff `P` is not total and **for every** incomparable pair `p={x,y}` there exists an outcome `o ∈ {x<y,y<x}` with `F(succ(P,p,o)) > r-1`.
- Base: if `r < 0` refutation is vacuous; if `P` is total then `F(P)=0` and no refutation of `>r` exists for `r>=0`.

A **natural complete refutation object** `R(P,r)` (adversary-strategy / universal-branch certificate) is: if `r < 0` accept; else record that `P` is not total and, for **each** incomparable pair `p` in `P`, a chosen outcome `o_p` and a recursively verifiable `R(succ(P,p,o_p), r-1)`. A verifier checks, in time polynomial in the object size plus `poly(n)` per checked edge (poset validity/closure/comparability, as in the DAG verifier arguments of `docs/research-strategy-certificates.md` Thm 1.1 style local checks): coverage of **all** sorter moves from each certified node, correctness of successor states, and that every certified path reaches a “budget exceeded / cannot be completed within remaining r” base. 
- **Soundness (deduction):** if every sorter move at a node admits some adversary response leading to a certified `>r-1` subtree, then the sorter has no strategy of height `<=r` from that node; by induction `F(P)>r`. Hence any accepted `(1^n#1^k,R)` implies `S(n)>k`.
- **Completeness (deduction):** if `F(P)>r`, then by the minimax definition such an `o_p` exists for every `p`, yielding some `R(P,r)`. So this format is **complete for all NO instances** (a genuine refutation format, not merely a heuristic).
- **Size (open).** The object must branch over **all** incomparable pairs at each certified universal node (a completeness requirement: omitting a sorter move breaks soundness as a refutation of “every strategy”). It may be represented as a DAG by sharing identical `(P,r)` subgoals if the verifier is given node identities/hashes, but I found **no theorem** bounding the number/total size of reachable certified states by `poly(N)=poly(n+k)` for all `n,k` with `S(n)>k`. For informative instances near the threshold, `k = Θ(n log n)` so `N=Θ(n log n)`. Known obstructions to naive succinctness (distinct from a proof): a single optimal *sorting* strategy is already a large object in general, and all-optimal/strategy spaces grow quickly in experiments for small `n` (`docs/research-strategy-certificates.md`); however, a **NO** refutation is an adversary/universal certificate and is not identical to a yes-strategy certificate, so those counts do **not** by themselves establish a lower bound for this refutation format.

### 3. Easy regime and “not all NO instances are hard” (deduction)
For any `n`, if `k < ⌈log2(n!)⌉` then the information-theoretic/counting argument certifies `S(n) >= ⌈log2(n!)⌉ > k`: a poly-time verifiable refutation can consist of `n,k` and the arithmetic fact/computation that `2^k < n!` (or an equivalent leaf-counting proof object), checkable in `poly(N)` since `n!,2^k` need not be written in unary except via arithmetic on `poly(N)`-bit numbers. Thus any infinite family with a uniform superpolynomial lower bound must live in the **hard regime** `k >= ⌈log2(n!)⌉` where the counting bound is silent and exact minimax structure matters. (Finite known gaps like `S(12)=30>29` illustrate the regime but do not form an infinite all-`n` family by themselves.)

### 4. Falsification attempts / obstructions to disproving (honest limits)
I did **not** obtain: (i) an explicit infinite family `(n_i,k_i)` with a proved superpolynomial lower bound in every sound poly-time verifiable refutation system, nor (ii) an unconditional superpolynomial lower bound for a natural complete refutation format, nor (iii) a uniform poly-size refutation construction (coNP upper bound).

Reasons this remains unresolved from the attempted analysis:
- **Strength of the requested falsifier:** “every sound refutation system checkable in time `poly(N)` requires superpolynomial certificates on `(n_i,k_i)`” means no fixed NP verifier for `L_NO` works on that family, hence (if exhibited for all large enough instances of a family in `L_NO`) it would establish `SORT-BOUND-U ∉ coNP` (a uniform separation from coNP). Given `SORT-BOUND-U ∈ PSPACE`, this is far beyond currently available techniques in this setting; I cannot claim or derive such an unconditional separation.
- **Natural-format lower bounds:** For the canonical all-moves adversary DAG (Sec. 2), proving superpolynomial size for all `n` (or an explicit infinite antichain-root family in the hard regime) would require a structural theorem about unavoidable branching/sharing in optimal adversary play against *all* sorter strategies from the root. General-poset “game” hardness results do **not** supply this for the fixed family of antichains `{[n]}` without an encoding-preserving reduction (and such reductions are constrained/unknown here; sparsity barriers concern a different direction).
- **Soundness vs completeness:** Many candidate invariants/potentials are **sound** lower bounds on restricted forms or give one-sided certificates but are not known **complete** for all `S(n)>k` (cf. info bound, partial heuristics). A lower bound against an incomplete format would **not** satisfy the front as stated.

## Concrete failed approach (this session)
- **Attempt:** Derive either (a) a succinct universal coNP certificate schema for all `S(n)>k`, or (b) an explicit hard-regime infinite family forcing superpolynomial size in the canonical complete adversary-strategy refutation DAG (or in all poly-time verifiable sound systems) from the comparison-game minimax recurrence plus known bounds/barriers.
- **Outcome:** (a) blocked by absence of any known polynomial bound/control on complete adversary/universal branching over all sorter moves (and no usable compression theorem for the root family); (b) blocked by lack of a root-specific unavoidable-size theorem and by the fact that the fully general “every sound system” falsifier would entail an unconditional `∉ coNP`-type consequence not supported by available methods/sources. Only the tautological/easy regimes (e.g. `k < ⌈log2 n!⌉`) admit immediate short refutations.

## Exact obstruction
A decisive answer to the front requires one of:
1. **Positive (all `n`):** a **complete and sound**, polynomial-time checkable refutation system together with a proved `poly(N)` size bound for **every** NO instance `(n,k)`, `S(n)>k` (equivalently a uniform proof that `SORT-BOUND-U ∈ coNP` via explicit NO witnesses); or
2. **Negative (as falsifier):** an explicit infinite hard-regime family `(n_i,k_i)` and a rigorous superpolynomial certificate-size lower bound against **every** sound poly-time verifiable refutation system (or, at minimum, an unconditional superpolynomial lower bound for a precisely specified **natural complete** format, proved for that family).

The blocking mathematical object is a **uniform, root-anchored (antichain) completeness-and-size theorem** for NO-certificates: either a compressible complete adversary proof of minimax value `>k`, or an unavoidable superpolynomial branching/information lower bound for such proofs in the regime `⌈log2 n!⌉ <= k < S(n)`. No such theorem or counterexample was established here.

## Conclusion (labeled)
- **Status:** **open / unresolved** by this investigation. No genuinely substantive, independently checkable new theorem or counterexample was found, so no repository/Lean changes were made.
- **What is clear (deduction/literature):** uniform poly-size refutations for all NO instances ⇔ `SORT-BOUND-U ∈ coNP`; canonical minimax adversary certificates are sound and complete in principle but of unknown size; easy NO instances below the information bound have short refutations; general-poset/network hardness results and sparsity barriers do not settle this front for `S(n)`.
- **Process note:** no external side effects were taken; this is a mathematical negative/obstruction report, not a proof of membership, non-membership, or separation.
