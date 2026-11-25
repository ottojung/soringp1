# antonina-x88egNle57nH24ErICREse-kaysarov

Session: ses_e414d0bccffeO1Yhy9dJ77P3a2
Workspace: /home/lubko/soring-fronts/certificate-completeness-polysize-framed
Created: 1794200761459; updated: 1794200776592

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 50 (msg_1beb306e30011NFF5izTXuIgmk)

I've studied the contract, problem statement, framed-certificate frontier note, and recent #301 board activity (including the Farkas support barrier and its verification). Here is an honest mathematical report rather than process success.

## Finding: framed certificate at exact budget S(n) is still open; no theorem or counterexample established here

**Claim under attack (falsifiable all-n):** There exists a uniform polynomial-size framed (ordered-partition) certificate that is both sound and complete for `SORT-BOUND-U` at the exact budget `k = S(n)` for all `n`, without computing `S(n)`.

**What is actually proved (literature/paper, independently verified):**
- Soundness of the framed grammar is polynomial-time checkable in graph size and `n` (local feasibility + depth in DAG order). So a polynomial framed certificate would put `SORT-BOUND-U ∈ NP`.
- The recent near-optimal Farkas support barrier (board #301 `near-optimal-farkas-succinctness`, verified by Viche) rules out polynomial *support* of Farkas certificates for the faithful state-expanded LP at budget `k = S(n)−1`. This is a decisive no-go for the **LP-dual/Farkas** route, not for the framed grammar.
- Sergeev's construction gives `S(n) ≤ log₂(n!) + o(n)`, but stores coupled interval containers; no polynomial-state rank-envelope grammar with sound joins and `o(n)` total surplus is known.

**Attempted disproof routes and where they stall:**
1. *Entropy/forgetting identity (§4 of the framed note):* On the auxiliary resampling walk, near-information-bound certificates require `o(n)` total imbalance + forgetting. This is a necessary condition, not a disproof; counting `e(P)` is #P-hard, so it cannot be turned into a polynomial-time verifier or a super-polynomial lower bound for the framed grammar.
2. *Farkas support → framed lower bound:* Does not transfer. The framed grammar's joins are intersection of guaranteed relations; a framed certificate need not be a Farkas certificate of the state-expanded LP. No reduction from Farkas support to framed DAG size is known.
3. *Merge-sort DAG (O(n²) nodes):* Sound and polynomial, but path length `O(n log n) > S(n)` for large `n` (Sergeev). It is a certificate for an upper bound, not for exact `S(n)`. Not a counterexample to the claim, and not a proof of completeness at `S(n)`.
4. *Ford–Johnson lifted frames:* Plausible polynomial construction for the standard FJ upper bound `F_FJ(n)`, but `F_FJ(n) ≠ S(n)` for some `n` (e.g. `n=12` gap). Completeness at exact `S(n)` unchecked; the odd-case and recursive frame audit is outstanding.

**Obstruction / exact limit:** The gap between soundness (known, checkable) and completeness at the exact budget `S(n)` is the open question. No infinite family of `n` is known where every sound-and-complete framed certificate has super-polynomial size, and no uniform polynomial construction verified on all `n` up to a bound exists. The Farkas barrier kills one certificate family (LP duals) but leaves the framed grammar untouched; conversely, the FJ construction is only for a non-exact upper bound.

**Conclusion:** No substantive new theorem or counterexample is established. The claim remains open with a precise boundary: polynomial framed certificate ⇔ `SORT-BOUND-U ∈ NP` via this grammar; neither direction is settled. I am making no repository, Lean, or board changes, since nothing here meets the publication gate. Next decisive step is the outstanding audit of the Ford–Johnson lifted frames (odd case + recursive frame permutations) to either obtain a verified polynomial construction for exact `S(n)` or expose a concrete failure.
