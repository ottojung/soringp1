# antonina-MQcqBDywyIF7vkTVwsvArc-villain

Session: ses_e168b37ddffepvNo8n83n5X30M
Workspace: /home/lubko/soring301-exec-autquotient-optplay-20261117
Created: 1794918107194; updated: 1794918354420

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 66 (msg_1e978594b001DD8d74fKLBzfgw)

Delivered `exec-report.md` (and reproducible local script `scripts/autquotient_smalln_report.py`) for the automorphism-quotient optimal-play compression front.

**Conclusion (all `n`, barrier):** No — quotienting reachable/optimal-play states by poset automorphisms or stronger canonical/isomorphism symmetry, even combined with optimal-play ancestor constraints, does **not** yield a provably polynomial or `sub-2^{O(n log n)}` number of distinct states/certificate nodes for height-`S(n)` strategies in general.

**Core argument (cites/adapts `docs/research-winning-frontier-barrier.md`):**
- **Definitions:** states as transitive-closure posets `P`, reachability, minimax value `F(P)` (`S(n)=F(A_n)`), winning/optimal-play states `F(P) <= S(n)-t`, internal `Aut(P)`, and global isomorphism/canonical quotient (nonisomorphic states remain distinct under any relabelling-invariant canonicalization).
- **Barrier family:** for infinitely many `n`, there is a common depth with `>= 2^{(1/4-o(1)) n (log2 n)^2}` pairwise **nonisomorphic**, reachable, winning states. Pairwise nonisomorphism means canonical/automorphism quotient cannot merge them; `F(P) <= k-t` means optimal-play/value (ancestor) constraints retain them. §3.1 + Sergeev’s `S(n)=log2(n!)+o(n)` extends this from the information budget to the exact optimum `k=S(n)`. Since `n log^2 n = ω(n log n)`, growth is superpolynomial and `2^{ω(n log n)}` (hence not `sub-2^{O(n log n)}`).
- **Scope:** this is an enumeration/frontier-size obstruction (rules out methods that must list canonical winning frontiers), **not** a general time/space lower bound for arbitrary solvers and not excluding selective, symbolic, or parametric/DAG approaches.

**Small-`n` experiment (`[experiment]`, `n<=5`):** exhaustive transcript DFS with isomorphism canonicalization shows canonical quotient and optimal-play pruning reduce states substantially at small sizes but leave multiple winning isomorphism classes at intermediate depths (e.g. `n=5`, depth 4: 1390 winning labelled → 17 winning isom classes).

**Implications:** constrains state-enumeration/canonical-frontier routes for exact evaluation and state-distinct certificate schemes, but gives no complexity separation or class-membership claim for `SORT-BOUND-U` (consistent with `PSPACE`/tally barriers in `docs/problem.md`).

Reproduce small-`n` table: `python3 scripts/autquotient_smalln_report.py` (no other repo changes).
