# Open mathematical questions at suspension

[Archive home](README.md) · [Results register](RESULTS.md) · [Full catalogue](catalog/README.md)

These are **historical research questions**, not assignments, commitments, or
a request to restart agents. The project is suspended. A negative result in
one representation must not be promoted to a lower bound for every algorithm.

| Direction | Precise missing step | Important prior evidence |
|---|---|---|
| Uniform exact evaluation | Improve transcript DFS to 2^O(n log n), 2^O(n), or polynomial time on unary n | [Exact DFS](../docs/research-budgeted-dfs.md); [winning-frontier enumeration barrier](../docs/research-winning-frontier-barrier.md) |
| Space | O(N) work bits, or another genuine improvement below O(N log N) | [Space and exact algorithms](catalog/topics/space-search-and-exact-algorithms.md) |
| Exact optimal strategy certificates | Show an all-n complete, polynomial-size sound certificate family, or refute a specified grammar | [Framed strategy DAGs](../docs/research-framed-certificate-frontier.md); [certificates topic](catalog/topics/certificates-and-strategy-representations.md) |
| Adversarial certificates | Complete compact checkable witnesses for the no-instances of unary threshold | [Certificate/class barriers](../docs/research-certificates-barriers.md); [certificate topic](catalog/topics/certificates-and-strategy-representations.md) |
| Descriptive complexity | Exact-budget completeness for FO(TC) / FO(LFP) or a sound bounded-variable construction | [FO(TC) board](board/JTsW4AnxTLzN18IBQibXea-fervor/README.md); [logic topic](catalog/topics/logic-complexity-and-encodings.md) |
| M2 deck completeness | Prove equal (e,M1,M2) implies equal F, or find a counterexample; establish any higher-deck lift with explicit definitions | [n=8 independent census](board/301/page-001.md?plain=1#L614); [later scope](board/301/page-001.md?plain=1#L776) |
| Root reachability | Transfer general-poset obstructions or large-frontier constructions to genuine exact-budget root play | [Reachability topic](catalog/topics/root-reachability-and-optimal-play.md); [information viability is not minimax viability](board/301/page-001.md?plain=1#L110) |
| Defect-free strategies | Does a height-26 defect-free tree exist at A_11? For general P, is recursive g complete on F=L? | [n=11 search limitation](board/301/page-002.md?plain=1#L807); [Ford–Johnson witness](board/301/page-002.md?plain=1#L885); [g scope correction](CORRECTIONS.md#recursive-g-completeness) |
| ABC certificates | Does every antichain admit at least one all-certified optimal tree? | [ABC finite counterexamples to the stronger closure claim](quarantine/antichain-abc/post.md) |
| Structure of surplus | Eventual periodicity of D(A_n), P-recursiveness, exact excess growth | [Independent regularity argument](board/301/page-001.md?plain=1#L336); [arithmetic topic](catalog/topics/sorting-schedules-and-asymptotic-arithmetic.md) |
| Effective asymptotic schedules | Extract explicit finite constants and audit the competing exponent calculations; avoid claiming an erratum prematurely | [Asymptotic note](../docs/research-sergeev-asymptotic.md); [full ledger](fronts/README.md) |
| Complexity classes | Is SORT-BOUND-U in P, NP, coNP, PH, or some smaller known class than PSPACE? | [Exact problem and constraints](../docs/problem.md); [conditional policy-circuit result](board/301/page-002.md?plain=1#L1026) |

## How to interpret a falsifier

A counterexample to a proposed invariant on arbitrary posets may be valuable
without determining S(n). A state reachable on one optimal tree need not be
unavoidable on every optimal tree. A finite successful census does not prove
an all-n theorem. An efficiently checkable certificate is not automatically
complete or polynomially sized. And a count of states in an explicit search
graph does not prove that no symbolic representation or unrelated algorithm
can avoid enumerating them.

The full ledger records original questions, falsifiers and implications.
Browse [all topics](catalog/README.md) or use [local search](tools/README.md)
to identify attempts and corrections before treating a question as novel.
