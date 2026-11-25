# antonina-rGc3Acck78UzXUSegCASbZ-society

Session: ses_e473cf52fffedo07075mVTrKHp
Workspace: /home/lubko/soring-fronts/succinct-cert-complete-antichain
Created: 1794101152781; updated: 1794101167349

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 37 (msg_1b8c320a9001aVfNAiDpyxtaWm)

## Finding

**Question.** Does there exist a polynomial-length (in \(N=n+k+1\)) certificate for \(\text{SORT-BOUND-U}=\{1^n\#1^k : S(n)\le k\}\) that is sound and complete, verifiable in polynomial time, and not reliant on an exponentially large optimal sorting tree?

**Answer (paper-level).** This question is *exactly* the NP-membership gap for \(\text{SORT-BOUND-U}\), and it cannot be resolved unconditionally by any technique available to this project.

**Why no unconditional "no" is possible.** \(\text{SORT-BOUND-U}\in\text{PSPACE}\) is already proved here (budgeted transcript DFS, \(2^{O(N\log N)}\) time, \(O(N\log N)\) space). Hence \(\text{SORT-BOUND-U}\notin\text{NP}\) would imply \(\text{NP}\neq\text{PSPACE}\). No proof of that is in reach, and the contract forbids claiming otherwise.

**Why no unconditional "yes" is in hand.** A certificate would have to certify \(S(n)\le k\) without exhibiting an optimal decision tree (which may have \(2^{\Omega(n\log n)}\) nodes). General-poset certificates do not transfer: the Fibonacci-threshold predicate \(L_{\text{fib}}\) is PP-hard under Las Vegas reductions, and counting linear extensions of arbitrary posets is #P-hard, so no polynomial pruning rule survives for unrestricted posets. But \(S(n)\) is a fixed single-parameter family, not an arbitrary poset instance; the width-two threshold is easy (Peczarski's GPC). No reduction from a hard poset family to the specific sequence \(S(n)\) is known, and Mahaney sparsity rules out ordinary many-one NP-hardness anyway. So the general-poset barrier is a *barrier to a method*, not a barrier to NP membership of this tally language.

**Obstruction (the real one).** The only known complete witness for \(S(n)\le k\) is an optimal (or budgeted) decision tree of exponential size. Any succinct certificate would have to compress the minimax value \(S(n)\) into polynomial bits while remaining polynomially verifiable — i.e. it would put the *function* \(S_{\text{unary}}\) into a certificate-checkable class below PSPACE. That is precisely the open frontier "membership in NP via a succinct, checkable certificate"; no compression scheme (recurrence, structural invariant, or partial-order certificate) is currently known that is both sound and complete for all \(n\).

**Consequence.** Neither branch of the falsifier is attainable today: proving that every complete certificate needs \(2^{\Omega(n\log n)}\) nodes would settle \(\text{NP}\neq\text{PSPACE}\); exhibiting a poly-size verifier would put \(\text{SORT-BOUND-U}\in\text{NP}\). The decisive obstacle is not a missing small instance or a missing Lean lemma — it is the absence of any known succinct invariant of the minimax game \(S(n)\). The width-two Fibonacci threshold and the threshold-pruning node-count results are the nearest structural leads, but neither lifts to the full family.

**No repository changes made.** No new theorem, counterexample, or Lean statement is available to check; per the publication gate, this remains a documented open obstruction rather than an integrated result. Honest limit: the question as posed is coextensive with the \(\text{NP}\) vs \(\text{PSPACE}\) gap for this tally language, and no partial progress beyond the existing PSPACE upper bound and sparsity barrier is claimed.
