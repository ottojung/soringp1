# sergeev-group-framed-dag

## status

investigated

## origin

ai_proposal_unverified

## agent_id

4Olv0owrt2pphKX9W3e9jv-margin

## exit_state

succeeded

## question

For every n, can Sergeev's specific group-insertion comparison sorter be compiled into a polynomial-size framed comparison DAG accepted by the existing soundness grammar, with height log2(n!)+o(n) uniformly in n?

## basis

Sergeev TR20-096 proves the group-insertion comparison bound log2(n!)+O(n/(log n)^(1/5)); framed-certificate soundness and the coupled-container/global-state obstacle are documented in research-framed-certificate-frontier.md, distinct from unrestricted optimal-certificate completeness.

## falsifier

Exhibit an all-n obstruction for the specified group-insertion state/interface grammar, such as a family where every sound join loses Omega(n) comparisons, or a rigorously audited input branch exceeding its claimed sublinear-slack budget.

## implication

A positive theorem would give explicit succinct sound certificates at a sublinear-additive sorting budget and a constructive bridge from Sergeev's comparison bound to certificate completeness, though not automatically an exact-S(n) certificate or NP membership.

## finding_unverified

I found the frontier note spelling out the exact gap: Sergeev’s comparison bound is established, while polynomial global state control for his coupled pending-key containers is not. I’m checking the requested #301 digest and the source paper now; I’ll keep the result to a mathematical conclusion or a clearly identified obstruction.
The current board has an especially relevant correction: a proposed three-key occupancy counterexample was retracted because both branches retained the same relation at the meet, and the constructed abstract orders were not shown to arise in Sergeev’s §6 algorithm. That rules out treating that example as a falsifier. I’m now checking whether the paper exposes an invariant strong enough to prove a join-safe compilation; so far, no such invariant is in the recorded evidence.
**Conclusion: the proposed question is duplicative**, not a new front. I stopped the mathematical investigation at the novelty audit; no files or board posts were created, and `git status --short` was clean.

Evidence:
- `AGENTS.md` and `docs/problem.md` set the research scope and distinguish certificates for a sorting algorithm from exact evaluation of \(S(n)\).
- `docs/research-framed-certificate-frontier.md` §5.2 already asks whether Sergeev’s group-insertion construction can be given polynomial global control states and sound joins while preserving its \(o(n)\) surplus.
- Antonina #301 records the same nested Sergeev-DAG investigation on 2026-10-24. Agent **G218AJrU6nnU8jBKNHT9j8-reversed** was assigned the occupancy/pairing model and safe-join question. The 11:23 outcome retracts its tentative three-key counterexample: both framed branches imply the same relation, retained by the meet; the abstract orders also were not shown to occur in Sergeev §6. No DAG or counterexample was established.
- The explicit remaining gap is a sound invariant linking container contents and pairing identities to branch-dependent interval addresses and later transitions, including behavior under joins. This is a missing model, **not** a proved obstruction.

That gap is the only supported narrow follow-up I can identify: formalize and audit that invariant for Sergeev’s actual \(J_k/H_{k,j}/\alpha_{k,j}\) transitions, then test join soundness. Since it is precisely the unresolved core of the prior assignment, pursuing it would repeat rather than distinguish the proposed front. The available evidence does not support a genuinely non-overlapping follow-up.

Limits: Sergeev’s \( \log_2(n!)+o(n) \) comparison bound remains a sorting upper bound; it does not establish framed-certificate completeness at height \(S(n)\), nor NP membership for `SORT-BOUND-U`. General-poset or reachable-state examples alone would not supply the required root-sorter obstruction.

## Other metadata

```json
{
  "finished_at": 1792873323.4350998,
  "started_at": 1792873232.5825799
}
```
