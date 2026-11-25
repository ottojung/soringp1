# antonina-3qMbQ6mEBJoT1B4Reb1slr-proceed

Session: ses_e530d15f3ffec03NDiaCG5ktMo
Workspace: /home/lubko/soring301
Created: 1793902963218; updated: 1793903047443

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1acf2ea2800102feoLp4R6M7Fn)

I’ll inspect the current research framing and its cited sources, then isolate one route and audit whether its state can actually be composed with a polynomial-size certificate. I’ll keep this read-only and report any obstruction with a concrete lemma-level argument.

## Output 91 (msg_1acf38aa40017FqAnObY2QTGNl)

## Result: rank-envelope composition does not certify optimality

**Route audited:** compose Sergeev-style group insertion from independent rank envelopes for each pending key, using the existing permutation-framed DAG grammar.

**Conclusion:** I found a specific obstruction to the *naive independent-envelope composition*, not a counterexample to the existence of some polynomial certificate for optimal sorting. The envelope invariant is sound as a relaxation, but does not retain the joint order information needed to justify Sergeev’s coupled-container insertion costs. Thus it cannot, as stated, establish a polynomial-size certificate at height \(S(n)\).

### Definitions and the missing state

A framed node represents a set of possible input orders by a guaranteed partial order on the current slots. At a join, the guaranteed relation is the intersection of the incoming guarantees (after the supplied slot permutations). This is sound, but can discard correlations between incomparable elements.

An **independent rank-envelope state** records, for each pending key \(x_j\), a lower and upper rank bound in a known sorted chain. It does not record joint constraints such as “exactly one of \(x,y\) lies in this interval” or “\(x<y\).”

The frontier note’s envelope rule is sound: after \(t\) insertions, an endpoint can shift by at most \(t\), so widening a key’s window this way preserves every compatible order. Soundness alone does not preserve the sharper search widths required for a comparison budget.

### Concrete obstruction: forgotten coupling can enlarge a later search

Take a sorted chain \(c_1<c_2<c_3<c_4\), and two pending keys \(x,y\) with the coupled constraint

\[
c_1 < x < c_4,\qquad c_1 < y < c_4,\qquad x<y.
\]

This state allows six placements of the ordered pair among the four chain gaps. If a join forgets \(x<y\), the independent envelopes still allow \(x,y\) to occupy any of the three interior gaps independently: nine placements, including impossible joint histories. In particular, the join now admits orders with \(y<x\).

That is not an unsoundness of the certificate: the relaxed guarantee remains true for the union of histories. It is a loss of control information. A subsequent insertion routine that relies on \(x<y\), or on coupled interval occupancy, can no longer use that fact to exclude a search branch. It must either:

1. retain the coupling in its node state, or
2. use a search strategy correct for the larger relaxed set, potentially spending more comparisons.

This is a concrete failure of the proposed *independent-envelope state as a compositional summary*. It is not a lower bound on all possible framed DAGs: a richer grammar could carry the coupling explicitly.

### Lemma chain and what it establishes

1. **Envelope soundness.** The widened per-key intervals contain every order obtained after the intervening insertions. This is the shift argument in the frontier note, §3.
2. **Join soundness.** Replacing the incoming guarantees by their intersection cannot assert a relation absent from some feasible incoming history (§1).
3. **Correlation loss.** The example above shows the intersection can retain each individual interval while dropping a joint relation; the resulting abstract state admits orders no incoming history admitted.
4. **Cost implication.** A later comparison bound proved using the dropped relation is not justified from the joined annotation. The verifier sees only the weaker relation and must validate both the genuine and newly admitted orders.
5. **No polynomial-completeness consequence.** The construction gives no bound on how often correlations must be retained, nor proves that retaining them requires superpolynomial size. It rules out only the inference “local rank envelopes compose, therefore Sergeev’s optimal-cost algorithm has a polynomial framed certificate.”

The decisive global information is therefore not merely the current rank interval of each pending key; it includes the **joint feasible placement pattern** of pending keys in the chain (and, in a recursive group-insertion construction, how that pattern is transported when the group’s elements are permuted or inserted). The published asymptotic comparison bound does not itself supply a polynomial-size representation of this evolving control state.

### Sources and model

- **Sergeev, “On the asymptotic complexity of sorting,” ECCC TR20-096 (2020), abstract and group-insertion result.** The stated theorem is an adaptive pairwise-comparison upper bound \(S(n)\le \log_2(n!)+o(n)\); it does not state a framed-DAG certificate theorem or a polynomial bound on globally composable control states. [ECCC report](https://eccc.weizmann.ac.il/report/2020/096/).
- **Stober–Weiß, “On the Average Case of MergeInsertion,” Theory of Computing Systems 64 (2020), 1197–1224.** Relevant to the Ford–Johnson/Jacobsthal schedule; it does not resolve Sergeev’s coupled-state representation.
- **Framed certificate frontier, §§1, 3, 5.** Establishes soundness of the verifier grammar and presents rank envelopes as a plausible construction, explicitly leaving the global recursive frame/boundary audit open.
- **Cremer, “Selecting the 7th Smallest of 16 Elements Takes Exactly 28 Comparisons” (2026), §3.** Shows that a finite selection certificate can use a compact function/DAG grammar with checked preconditions and joins. This is a finite selection witness, not an all-\(n\) sorting construction.
- **Parberry (1991).** Concerns verification of arbitrary sorting networks; it does not obstruct certificates for one optimal adaptive sorter at each \(n\).

### Complexity accounting

If an all-\(n\) certificate had size polynomial in \(n\), the given checker’s runtime would be polynomial in \(n\) and the certificate length. On unary threshold input length \(N=n+k+1\), an exact-budget certificate with \(k=S(n)=O(n\log n)\) would therefore be polynomial in \(N\), yielding \(\texttt{SORT-BOUND-U}\in\mathrm{NP}\). The obstruction above yields no such certificate bound and implies no complexity-class result.

### Next decisive test

For Sergeev’s actual group-insertion recurrence, formalize one full group-insertion stage’s **joint feasible placement state** and its transition under every insertion/permutation. Then test whether that state has a polynomial-bit, verifier-checkable summary whose join preserves the recurrence’s claimed search widths. If not, quantify the width increase caused by forgetting the coupling across stages. A small instance is useful only if it distinguishes the actual Sergeev transition from the independent-envelope relaxation; the illustrative two-key example identifies the information loss but does not do that full audit.

## Output 100 (msg_1acf4049c001i1SxyKdJzTaVMS)

The prior task requested read-only research only, so I won’t repeat the literature sweep or initiate any external action. I’ll check the current filesystem and Git state for unexpected changes, then report what appears completed and any uncertainty.

## Output 121 (msg_1acf422d2001lor6qbCjhYK3DK)

The interrupted task appears complete, with no external side effects to continue or repeat.

- **Research:** The prior response audited the independent rank-envelope route, gave a two-pending-key example of lost coupling, and identified a next decisive test.
- **Git/worktree:** Clean; no modified or untracked files. `HEAD` is `6a96398` on `billy-dev`.
- **Durable records:** No separate task-record files were found.

The earlier work was read-only, as requested. No post, commit, or other external action is indicated.
