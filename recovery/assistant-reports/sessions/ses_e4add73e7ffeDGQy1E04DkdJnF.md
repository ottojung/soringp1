# antonina-b2z5HndyPNdv14X2spLhpL-greatness

Session: ses_e4add73e7ffeDGQy1E04DkdJnF
Workspace: /home/lubko/soring-fronts/exec-cert-checkpoint-sergeev-20261107
Created: 1794040302691; updated: 1794040346251

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 86 (msg_1b522ec4c001tosTTAazAWZkP1)

**Audit result: partial/negative for this route, not a no-go theorem.** Sergeev’s group-insertion result does **not**, as published, establish a polynomial-size framed DAG with knowledge-reset checkpoints. Nor does the common-knowledge obstruction prove that such a DAG must be superpolynomial. The key missing result is whether the histories inside each macroscopic group can be represented and merged by a polynomial-size, sound *nested* certificate.

1. **(a) Common-poset stage boundaries — partial.** A natural reset exists at a completed group boundary: the keys processed so far form a sorted chain, with the remaining keys unconstrained except for what that chain entails. But Sergeev’s proof also maintains interval-container and pairing information during a group. I found no argument that every history at intermediate boundaries has the same guaranteed poset, or that the future algorithm works from the meet of those histories. A boundary is useful only if that common guarantee suffices for the next stage.

2. **(b) Group size and stage count — yes on scale, not enough for a certificate.** The issue’s correction to the primary-source reading says Theorem 2 requires group parameter \(m\ge 2^{a/4}\), and in the Theorem 3 application groups have size about \(\sqrt n/\log n\), hence at least \(n^{1/4-o(1)}\). Thus there are polynomially many groups (about \(\sqrt n\log n\)). But the short local strategy tree—polylogarithmic in \(n\) leaves—does not by itself bound the *global* control state needed to track containers across insertions. Splitting those groups into independently reset \(O(\log n)\)-comparison stages is not justified by Sergeev’s analysis; flushing containers might also lose the comparison bound.

3. **(c) Does incompatibility force exponential sharing? — no such conclusion follows.** The framed-DAG soundness rule requires a joined node to retain only facts common to all incoming histories; a future routine relying on discarded disjunctive/container correlations may then be unsound. That is a genuine obstacle to naive checkpointing. But the cited four-key network counterexample only refutes that particular immediate-join representation, not all DAGs for a sorter. No explicit growing family or lower bound establishes exponential size for Sergeev’s strategy, even with macroscopic groups. A nested DAG that preserves the needed state could still be polynomial.

4. **(d) Near-optimal certificate versus exact \(S(n)\) — distinct conclusions.** If a polynomial-size sound certificate proves a sorter of height \(\log_2(n!)+o(n)\), that proves only an **upper bound on sorting comparisons**. It does not prove \(S(n)\) equals that bound, and it does not show \(S(n)\le k\) for arbitrary true threshold instances. So by itself it gives neither exact-\(S(n)\) certificates nor NP membership for `SORT-BOUND-U`. If instead one obtains polynomially checkable certificates at height **exactly \(S(n)\) for every \(n\)**, the established framed-certificate argument gives `SORT-BOUND-U ∈ NP`; that exact-optimal completeness is open.

**Construction sketch:** none is justified yet. The plausible route is to give each macroscopic group a nested, polynomial-size framed DAG whose entry invariant is the common sorted-chain checkpoint, whose internal joins soundly retain enough container/pairing state, and whose worst-case costs sum to Sergeev’s bound. The paper’s local branching and number of groups alone do not supply this construction.

**Implication:** this audit does not change certificate completeness or complexity classification. It identifies the unresolved bridge—polynomial, sound representation of stateful within-group processing—rather than ruling the route out. Sergeev’s \(S(n)=\log_2(n!)+o(n)\) concerns sorting cost, not the cost of computing exact \(S(n)\).

**Evidence/status:** repository contract and the six requested documents were read; GitHub issue #47 comments 6353288888 and 6353303109 (plus surrounding certificate-frontier comments) were reviewed. The primary-source parameter correction is present in the issue, but I could not independently inspect the PDF in this environment, so I treat it as a reported source check, not a fresh primary-source verification. The attempted GitHub lookup for #301 returned 404; board status could not be verified. No repository changes, experiments, or Lean work were made. I’m not preparing a #301 update because this is an audit finding, not a new theorem.
