# antonina-gx5BTBqXqVzbTuT3IfYyHN-macerated

Session: ses_e3b9d4f30ffewRLDaRUHf61oEQ
Workspace: /home/lubko/soring-fronts/adversary-strategy-certificate-conp
Created: 1794296164993; updated: 1794296293741

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 94 (msg_1c463a710001UYATMSDPScG2Wb)

## Scope and sources (studied)
- `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/research-certificates-barriers.md`, `docs/research-winning-frontier-barrier.md`, `docs/literature.md`, `docs/research-sergeev-asymptotic.md`, `docs/research-frontier.json`.
- Board #301 sampled via `scripts/board_digest.py` (`--recent 7`, and filters `coNP`/`adversary`/`G(n,k)`, page 1): no prior post found on this exact coNP/adversary-certificate front on page 1 (so no duplicated claim detected from available digest).
- Model/encoding fixed per `docs/problem.md`: `S(n)` is the exact minimax height of an adaptive comparison decision tree on `n` distinct labelled keys; `SORT-BOUND-U = {1^n#1^k : S(n) <= k}` has input length `N=n+k+1`; informative `k` lie in an `O(n)` window. `S(n)>k` iff the adversary wins `G(n,k)` [definition/deduction, `problem.md`/`research-certificates-barriers.md`].

## Front attacked
**Question.** For all integers `n,k` with `S(n)>k`, is there a polynomial-in-`(n+k+1)`-size, polynomial-time-checkable adversary winning-strategy certificate for `G(n,k)`?  
**Falsifier sought.** An infinite family `(n_i,k_i)` with `S(n_i)>k_i` such that every correct adversary strategy witness for `G(n_i,k_i)` requires superpolynomial size in `n_i+k_i`.  
**Complexity implication.** A uniform YES answer with a poly-time verifier would place the complement of `SORT-BOUND-U` in NP, hence `SORT-BOUND-U ∈ coNP` [deduction, standard], strengthening its known position below PSPACE for the unary threshold language (`SORT-BOUND-U ∈ PSPACE`, Claim A in `research-certificates-barriers.md`).

## Mathematical finding (status: **open; no theorem/counterexample proved**)

1. **No succinct adversary certificate is known; the front remains open.** [`deduction` from `docs/research-certificates-barriers.md` §6–§8, `docs/problem.md`] I found no polynomial-size, polynomial-time-checkable witness system for all `S(n)>k` instances and no proof that `SORT-BOUND-U ∈ coNP`. This is consistent with the documented central obstruction: absence of a succinct certificate in either direction and absence of a compact canonical object for optimal comparison play.

2. **Soundness vs completeness must be separated for every candidate witness.** [`deduction`]
   - **Information/extension-count witness (sound when checkable, incomplete).** A transcript reaching poset `P` in `d` comparisons with `F(P)>k-d` certifies `S(n)>k`. A sufficient local condition is `e(P) > 2^(k-d)` since always `F(P) >= ceil(log2 e(P))`. However:
     - *Verification obstacle:* counting/deciding `e(P)` is #P-complete for general posets (Brightwell–Winkler, cited in `research-certificates-barriers.md`/`literature.md`), so “`e(P)` is large” is not by itself a known poly-time-checkable predicate.
     - *Completeness obstacle (hard regime):* for `k >= ceil(log2 n!)`, `n!/2^k <= 1`; the entropy-only invariant `e(P_t) >= n!/2^t` (maintainable by halving, a standard adversary heuristic) cannot certify survival to step `k`. Exact lower bounds beyond the information bound (literature: e.g. `S(12)=30 > 29 = ceil(log2 12!)`) are precisely instances where no pure entropy certificate is complete. Thus extension-count certificates are, at best, sound incomplete witnesses, not a uniform coNP proof system.
   - **Exhaustive-search transcripts (complete in effect, not succinct).** Published exact lower bounds above the information bound are obtained by exhaustive/pruned searches over posets/strategies (Wells, Peczarski, Stober–Weiß; see `literature.md`, `research-certificates-barriers.md` §8.2). These are computational evidence/procedures, not polynomial-size, polynomial-time-checkable certificates in `N=n+k+1`.

3. **General-poset results do not transfer to a certificate for `S(n)>k`.** [`deduction`, per AGENTS/model fidelity] Hardness/complexity of optimizing or certifying over arbitrary partial orders, arbitrary-test decision trees, or fixed sorting networks is not a statement about the fixed antichain-root family `S(n)` or about `G(n,k)` without an encoding-preserving reduction. In particular, Parberry-style coNP-completeness concerns fixed-network verification (a different model), and Hyafil–Rivest/Laber–Nogueira concern arbitrary tests; neither yields an adversary-certificate lower bound for `SORT-BOUND-U` (`research-certificates-barriers.md` Claim D).

4. **Explicit strategy objects are not known to be succinct, but this is not a falsification of all witnesses.** [`deduction`]
   - An explicit adversary response policy over all sorter choices/histories (tree/DAG/branching program of states) is checkable in time polynomial in its size if it carries enough local information, but its size is the obstruction: worst-case reachable/state counts are `2^{Theta(n^2)}` (A001035-scale), and large winning frontiers exist at fixed depths (`research-winning-frontier-barrier.md`: `2^{Omega(n (log n)^2)}` nonisomorphic winning states for constructed families). Crucially, those enumeration barriers exclude methods that must list the whole frontier, **not** every possible selective/symbolic adversary certificate.
   - Therefore the explicit-strategy route fails as a *known* succinct certificate, but does not establish the requested falsifier (“every correct adversary strategy witness requires superpolynomial size”).

## Concrete failed approach (attempted refutation direction)
- **Attempt:** derive the falsifier by forcing any correct adversary witness to encode/visit a superpolynomial winning frontier (or all optimal adversary responses), using the `2^{Omega(n (log n)^2)}` winning-frontier phenomenon and the optimal-play/DAG state explosion. 
- **Why it failed / did not close:** (i) a certificate need not enumerate states; it may compress play by an invariant, proof, or symbolic object; (ii) the frontier theorems are existence/counting statements about states, not lower bounds on the description complexity of *some* valid certificate for the corresponding `(n,k)`; (iii) I found no argument that every poly-time-checkable proof of “adversary wins” must implicitly separate or list superpolynomially many cases. Hence no infinite superpolynomial witness-size family was exhibited. [`deduction`]

## Exact obstruction
To answer the front affirmatively one needs a **sound, complete, polynomial-size, polynomial-time-checkable** object certifying `F(antichain_n) > k` for the relevant unary instances (or, equivalently for the decision gap, for all true `S(n)>k` instances); to answer it negatively (the stated falsifier) one needs an unconditional/absolute lower bound against **all** correct certificate formats for an infinite family. The obstruction is:
- known potentials/certificates split into *sound-but-uncheckable* (general `e(P)`), *sound-but-incomplete* (information/entropy in the non-tight regime), or *complete-but-nonsuccinct* (explicit strategies/exhaustive search); and
- no compact canonical invariant stronger than `log2 e(P)` is known for the exact minimax adversary at the antichain root (`research-certificates-barriers.md` §8.2), while proving impossibility of every succinct witness would be a major proof-complexity/coNP-barrier result not available here and not implied by current enumeration/frontier theorems.

## Honest limits
- **Not proved:** `SORT-BOUND-U ∈ coNP`, `SORT-BOUND-U ∉ coNP`, existence of any uniform succinct adversary certificate, or existence of the requested infinite superpolynomial witness-size family. No new theorem or counterexample is claimed.
- **No experiment discriminated** a hypothesis here beyond what the cited documents/literature already establish (the critical gap is logical/certificate-theoretic, not a small-`n` enumeration gap I could close).
- **Process note:** this is a mathematical/status report only; no Lean or repository source changes were made (no substantive independently checkable new theorem/counterexample to integrate). Any board posting of this assessment should follow `docs/operations.md` and only if it adds a non-duplicative, precise obstacle record.
