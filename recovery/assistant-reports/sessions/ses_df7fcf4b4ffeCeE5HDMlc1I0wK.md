# antonina-QE0ErFs2NndXJwzKmEAQuj-rickety

Session: ses_df7fcf4b4ffeCeE5HDMlc1I0wK
Workspace: /home/lubko/soring-fronts/sortboundu-eso-certificate-20261123
Created: 1795430746996; updated: 1795431043009

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 159 (msg_20806da48001UjGYlJ7UL1W94I)

## Posting status

I prepared the report at `/tmp/sortboundu-eso-report.md` but **could not post it to SoringP1 #301**: no GitHub credentials were available in this environment (`gh` CLI unauthenticated, no `GH_TOKEN`/`GITHUB_TOKEN`, no git credential helper, SSH-only remote). I made no other external writes and made no repo/Lean/test/CI/ledger/main/PR/commit changes.

## Report (ready for issue comment)

## ESO / NP-certificate probe for `SORT-BOUND-U` (fresh session, billy-dev)

**Question.** Does `SORT-BOUND-U = {1^n # 1^k : S(n)<=k}` admit an explicit existential second-order (ESO, i.e. NP-style on ordered strings) certificate/verifier polynomial in the unary input length `N=n+k+1`, beyond the exponential-size explicit sorting-tree witness?

**Model precision (definition).** `S(n)` is the minimum worst-case height of a deterministic adaptive comparison decision tree sorting every permutation of `n` distinct labelled keys (`docs/problem.md`). `SORT-BOUND-U` is a decision language; NP membership means: there exist polynomial `p` and polytime verifier `V` with `x ∈ SORT-BOUND-U ⇔ ∃w, |w| ≤ p(|x|), V(x,w)=1`. By Fagin's theorem, NP = ESO on finite structures, and on ordered strings ESO captures NP [Fagin 1974]; so an explicit poly-size ESO witness for an ordered unary-string encoding is equivalent to an NP certificate. This is a statement about the *decision language*, not an NP class of numeric functions. I make no theorem-completion claim.

### (A) Explicit certificate/verifier candidates

**A1. Explicit sorting tree (baseline, NOT polynomial).** Witness: a full binary comparison decision tree of height `<=k`. Verifier: check root/labels, check every internal node compares an incomparable pair under path poset, check both outcomes present, check transitive-closure feasibility, check every leaf determines a unique total order, check height `<=k`. This is polytime in the tree size. But any correct reduced tree has exactly `n!` leaves and `2n!-1` nodes [deduction, `docs/research-certificates-barriers.md` Claim C]; for informative unary inputs `k <= n ceil(log2(n+1))`, `N=Θ(n log n)` so `n!=2^{Θ(N)}` — exponential, not NP.

**A2. Strategy DAG / hash-consed branching program (candidate, size open).** Witness: a DAG `D=(V,E)` whose nodes are transitive-closure poset states on `[n]` (or canonical isomorphism representatives), root = antichain, each nonterminal has one comparison and two outcome edges, terminals are total orders, longest root-terminal path `<=k`. For a quotient form, each edge carries an explicit relabelling permutation `σ` mapping the successor poset to the stored canonical child (`docs/research-strategy-certificates.md` Remark 3.3/Thm 3.4).

*Verifier (poly in |D|,n,log k; deduction):* (1) root empty antichain; (2) every node is a valid transitive antisymmetric poset matrix `O(n^3)`; (3) every nonterminal edge compares an incomparable pair; (4) compute outcome transitive closure, apply supplied `σ`, check equality to target node `O(n^3)` per edge; (5) both outcomes present; (6) terminals total; (7) DAG acyclic; (8) DP height `height(leaf)=0`, `height(P)=1+max(height(P1),P0)` gives `height(root)<=k`. Total `O((|V|+|E|)n^3 + |E|log k)`. This is an NP-style verifier *given a poly-size DAG*; it does not prove such a DAG exists.

**A3. Framed permutation-certificate grammar (candidate, completeness open).** `docs/research-framed-certificate-frontier.md` gives a sound, locally checkable acyclic-graph grammar: arcs carry comparison outcome + explicit slot permutation; node annotation is guaranteed strict order `R`; joins intersect incoming guaranteed relations; terminals have total `R`; path length `<=k`. Soundness checker exists in `scripts/check_framed_strategy.py`. Paper constructions give all-`n` poly-size framed DAGs for adaptive merge sort (`O(n^2)` comparison nodes, `O(n log n)` path length) and a plausible rank-envelope/Jacobsthal Ford–Johnson upper-bound construction (`O(n^2)` query nodes) — but both certify upper bounds `F(n)` that can exceed `S(n)` (merge sort is worse by `(log2(e)-1)n+O(log n)` on powers of two; `F_FJ(n)!=S(n)` in general). They are NP witnesses for those upper bounds, not for exact `S(n)<=k`.

### (B) Concrete obstructions / falsifiers

**B1. Size blowup / no completeness theorem.** A single optimal policy is a reduced tree with `2n!-1` nodes and no hash-consing sharing (Thm 2.6/Cor 2.7, `research-strategy-certificates.md`, experiment `n<=6`). The all-optimal DAG is smaller after sharing but grows rapidly (`DAG(all)=65551` at `n=6`, `log2(DAG(all))/n` increasing on `n<=6`; evidence inconclusive, not an asymptotic proof). The symmetry quotient shrinks it (`q(all)=134` at `n=6`) but has no proved poly bound. The winning-frontier barrier [`research-winning-frontier-barrier.md`] gives `2^{(1/4-o(1))n log^2 n}` nonisomorphic winning states at one depth, including at budget `S(n)` via Sergeev `S(n)-C(n)=o(n)`: this rules out full winning-frontier enumeration, but **does not** rule out a single succinct optimal strategy certificate — a different object.

**B2. Join soundness / nonlocal verification.** In the framed grammar, intersection at joins may discard disjunctive correlations needed later; an optimal 4-element 5-comparison network gives a counterexample when joined immediately (`research-framed-certificate-frontier.md`). Therefore "any correct strategy compresses" is false for this naive join rule. A sound grammar must carry enough local invariant to justify every join; finding an invariant complete for exact optimal root strategies is open.

**B3. Optimality gap / equivalence to frontier enumeration pressure.** Known poly-size framed constructions certify non-optimal upper bounds. Making them exact at `S(n)` requires either proving the constructed bound equals `S(n)` (false in general) or constructing a different poly-size optimal strategy. Sergeev gives `S(n) <= log2(n!) + O(n/(log n)^{1/5})` [Sergeev 2020, ECCC TR20-096] but the construction stores pending keys in coupled interval containers; a poly-state sound rank-envelope/nested-subroutine grammar with `o(n)` surplus is open (`research-framed-certificate-frontier.md` §5). The `n=12` gap (`C(12)=29`, `S(12)=30`, Wells 1965) shows information-theoretic certificates are insufficient.

**B4. Counting/greedy route barrier (route-specific, not hardness).** Choosing comparisons by minimizing `max(e(P+x<y),e(P+y<x))` uses linear-extension counting `e(P)`, which is #P-complete [Brightwell–Winkler 1991]. This blocks a specific greedy-optimal certificate route, not NP membership and not a hardness theorem for `S(n)`.

**B5. Sparsity/Mahaney is a hardness barrier, not a membership barrier.** `SORT-BOUND-U` is sparse; many-one NP-hardness would imply `P=NP` [Mahaney 1982], and under polytime Turing reductions PH collapses to `Δ2^P` [Ogiwara–Watanabe 1991]. This does **not** obstruct NP membership; it obstructs the easiest hardness proofs.

**B6. Lower-bound certificates are the coNP direction.** A witness for `S(n)>k` (no height-`k` strategy exists) would be a coNP-style certificate. No succinct lower-bound certificate is known for the hard regime `k >= ceil(log2(n!))`; published proofs are exhaustive searches [Wells 1965; Peczarski 2004/2012; Stober–Weiß 2023, arXiv:2206.05597].

### (C) Honest assessment

**Inconclusive (open).** There is an explicit NP-style verifier for any *explicitly given* poly-size strategy DAG/framed certificate (A2/A3), and poly-size framed certificates exist for some non-optimal upper bounds. But no explicit poly-size existential certificate/verifier is known for the exact language `SORT-BOUND-U` at all `n,k`, because completeness at optimal height `S(n)` is unproved and the natural compressions face size/join/optimality obstructions (B1-B3). This is consistent with `SORT-BOUND-U ∈ NP` being open; it is not evidence against NP membership, and no separation claim is made. The strongest defensible current statement remains: `SORT-BOUND-U ∈ PSPACE` [game/alternating TM, APTIME=PSPACE, Chandra–Kozen–Stockmeyer 1981; `research-certificates-barriers.md` Claim A], NP/coNP membership open.

**Primary sources:** Fagin, *Generalized first-order spectra and polynomial-time recognizable sets*, 1974; Chandra–Kozen–Stockmeyer, *Alternation*, JACM 28(1) 1981; Mahaney, *Sparse complete sets for NP*, JCSS 25(2) 1982; Ogiwara–Watanabe, SICOMP 20(3) 1991; Brightwell–Winkler, *Counting linear extensions is #P-complete*, STOC 1991; Parberry, *On the computational complexity of optimal sorting network verification*, PARLE 1991; Peczarski, Algorithmica 40 (2004), Acta Univ. Sapientiae Inform. 4(2) (2012); Stober–Weiß, arXiv:2206.05597 / ALENEX 2023; Sergeev, *On the asymptotic complexity of sorting*, ECCC TR20-096, 2020. Repo docs: `docs/problem.md`, `docs/research-certificates-barriers.md`, `docs/research-framed-certificate-frontier.md`, `docs/research-strategy-certificates.md`, `docs/research-winning-frontier-barrier.md`.
