# antonina-JN5JcRTk1wAoyoHCohhgsc-journal

Session: ses_e4b3f3b69ffeaiHZ6GAykNBo12
Workspace: /home/lubko/soring-fronts/exec-rutschmann-exactness-audit-20261107
Created: 1794033894623; updated: 1794033957188

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 104 (msg_1b4c154ba001TgnqQNJ4eLmXvF)

## Audit result

**Conclusion:** The 2026 preprint gives a uniform, input-sensitive sorting algorithm for a known partial order, with a comparison bound of \(O(\log e(P))\). It does **not** establish that the resulting strategy is exact-optimal for that state, nor that its decomposition or reuse yields a polynomial-size framed DAG for exact-optimal strategies. This is not a new positive certificate result for issue #47; transferring the algorithm to that frontier would require a stronger theorem than the paper proves.

### Model and semantics

Rutschmann, *Sorting under Partial Information with Optimal Preprocessing Time via Unified Bound Heaps*, arXiv:2604.12653v2, defines \(G\) as a DAG on items \(X\); \(e(G)\) is the number of linear orders compatible with \(G\). In the two-phase model, preprocessing sees \(G\) but makes no comparisons; the sorting phase compares items and must output them in sorted order. The algorithm’s comparisons reveal the input’s actual linear order \(L\), which extends \(G\). (Preprint, §1, “Sorting under Partial Information”; Theorem 5.)

Theorem 5 states \(O(m)\) preprocessing and \(O(\log e(G))\) sorting time and comparisons. Its sorting phase is a single deterministic algorithm operating on the preprocessed structure and actual comparison outcomes. Thus, for each fixed \(G\), it induces a comparison decision tree valid across all feasible transcripts. This is an ordinary uniform correctness guarantee, not a claim that the induced tree is minimax-optimal.

The paper’s cost statements must be kept separate:

- **Preprocessing:** \(O(m)\), measured on the supplied DAG representation.
- **Sorting phase:** \(O(\log e(G))\) time and comparisons, per Theorem 5.
- **Exact minimax value:** \(F(G)\), the minimum worst-case comparison count for \(L(G)\).

The theorem gives an asymptotic upper bound on the third quantity, not equality with it. In particular, it does not show \(F(G)=\lceil\log_2 e(G)\rceil\). The \(O(\log e(G))\) bound is not itself an exact-cost bound with a specified constant.

The abstract/introductory comparison to a “decision tree of height \(O(\log e(G))\)” is consistent with the induced tree, but does not provide a compact certificate in the framed-DAG grammar of `research-framed-certificate-frontier.md`. A sorting algorithm’s implementation data structure and transitions are not automatically a locally checkable permutation-framed DAG.

### Transfer lemma—and why it does not transfer exactness

A valid conditional statement is:

> **Transfer lemma (conditional).** If, for every reachable state \(P\), an algorithm’s sorting phase can be compiled into a sound permutation-framed DAG of size polynomial in \(n\), with height at most \(F(P)\), then that DAG is an exact-optimal framed certificate for \(F(P)\). For antichain roots, an all-\(n\) polynomial-size compilation at height \(S(n)\) would give the exact-optimal certificates sought in issue #47.

The preprint supplies neither hypothesis needed to apply this lemma: it does not bound its induced tree’s compiled framed-DAG size, and its \(O(\log e(P))\) guarantee does not imply height \(F(P)\). Since \(F(P)\ge \log_2 e(P)\), the information bound only gives a lower bound; a constant-factor upper bound is not an exact-optimality result.

The familiar \(e=60\) checks illustrate the gap without relying on them as a disproof of a broad asymptotic theorem: \(\lceil\log_2 60\rceil=6\), while the known states A/B have \(F=6/7\). A guarantee stated as \(O(\log e)\) does not identify which state receives which exact cost, and cannot establish height \(F\). At antichain roots, the algorithm’s guarantee is \(O(\log(n!))\); it does not compute or certify the exact \(S(n)\).

This is compatible with the existing certificate frontier: polynomial framed certificates are known for some non-optimal sorting constructions, while exact-optimal completeness remains open. The preprint’s use of a data structure and repeated operations does not close that gap.

### Novelty and consequences

The distinction between exact \(F(P)\), an \(O(\log e(P))\) sorting algorithm, and polynomial-size framed certificates is already the core issue in the certificate-frontier note. The current audit finds no additional transfer theorem or counterexample to report: the proposed implication fails at the level of what Theorem 5 asserts, rather than through a new separating instance.

For unary `SORT-BOUND-U`, **no complexity consequence follows** from this preprint alone. It gives neither a polynomial-size exact-optimal certificate (which would imply unary NP membership) nor a faster uniform evaluator for \(S(n)\). Its input-sensitive sorting cost on a known poset is not the runtime for evaluating the minimax value over all comparison states. The antichain root is not simplified into an exact \(S(n)\) computation by the \(O(\log e)\) bound.

**Candidate assessment:** unsuitable as a new SoringP1 result unless a separate paper argument establishes a compact framed-DAG compilation or exact-optimality preservation. No source changes, commit, post, or Lean work was made.

## Output 123 (msg_1b4c1b594001d9yX0XoemKONkq)

Worktree is clean and no source changes, commits, posts, or other external actions occurred. The audit result stands as delivered. No further work is needed.
