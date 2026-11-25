# constant-round-am-sortbound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

gnEHOwyyDXDdZwRhMcdPYI-struggles

## exit_state

clearexit

## question

Does SORT-BOUND-U admit a public-coin interactive proof with O(1) rounds and a polynomial-time verifier (membership in AM), or does every constant-round protocol fail on infinitely many unary inputs because the minimax game's alternation cannot be compressed?

## basis

docs/problem.md PSPACE membership; docs/research-certificates-barriers.md soundness-versus-completeness gap; the ledger has alternation-block fronts but no interactive-proof or AM front.

## falsifier

An explicit O(1)-round Arthur-Merlin protocol with perfect completeness and soundness error at most 1/3 for all n,k, or a proof that every constant-round protocol errs on an infinite unary family.

## implication

AM membership would place the unary threshold in the polynomial hierarchy (AM is contained in Pi_2^P), a new upper bound below the known PSPACE bound; a lower bound would separate this minimax language from arbitrary PSPACE games.

## finding_unverified

` The existing DAG/frontier/potential results are **soundness** results: they check a proposed lower bound, prune safely, or count reachable winning states. They do **not** supply a **complete** succinct certificate for all \(n\). The winning-frontier theorem rules out methods that must enumerate all winning states at a common depth; an AM message could in principle be selective and need not enumerate that frontier, so the frontier barrier is not an AM lower bound.

## 5. Honest limits

- No explicit AM protocol was found, even for the hard window between the information bound \(C(n)=\lceil\log_2 n!\rceil\) and a known constructive upper bound such as Ford–Johnson or merge sort.
- No proof was found that every constant-round protocol fails. Such a proof would be a non-relativizing separation of `SORT-BOUND-U` from AM and would imply \(\mathrm{PSPACE}\ne\mathrm{AM}\).
- General-poset hardness and finite computation through \(n=22\) do not decide the question.
- The most defensible new statement is the boundary-advice/self-reduction obstruction above: AM membership gives nonuniform boundary advice and a circular boundary protocol; the missing ingredient is a sound, uniform way to verify the no-side of the cutoff.
## Recovery audit

I inspected the conversation history, working tree, Git state, board digest, and the durable frontier ledger before doing anything.

**Effects actually present:**

- Git: clean worktree at `6a96398` on `billy-dev`; no commits, branches, stashes, or file changes from this front.
- Repository: no Lean, docs, scripts, tests, or note files were created or modified.
- Board #301: the recent digest contains no AM/interactive-proof post from this front. No duplicate post was made.
- Durable ledger: the front `constant-round-am-sortbound` exists with agent `gnEHOwyyDXDdZwRhMcdPYI-struggles`, status `running`, and an **empty** `finding_unverified`. That is the only unfinished bookkeeping item. I did not edit the ledger manually, because it is keeper-owned and a concurrent write could corrupt or duplicate state.

No external action was repeated. I did not re-run the research prompt or post to the board.

## Mathematical status (carry-forward)

- No \(O(1)\)-round AM protocol was found for `SORT-BOUND-U`.
- No proof was found that every constant-round protocol fails.
- The useful exact obstruction is the **boundary-advice/self-reduction** result: AM membership gives, for each \(n\), a nonuniform polynomial-size advice string \(r_n\) that determines the entire cutoff \(S(n)\). The missing step to NP is finding/verifying that advice uniformly — not compressing the minimax game’s alternations.
- The natural boundary protocol is circular: verifying \(s=S(n)\) requires checking that \(s-1\notin L\), a universal no-witness/coAM-like condition. Flipping the AM protocol does not certify the complement.
- A lower bound \( \text{SORT-BOUND-U}\notin\mathrm{AM}\) would imply \(\mathrm{PSPACE}\ne\mathrm{AM}\), and it cannot be proved by relativizing methods (the oracle \(O=L\) makes \(L\in\mathrm P^O\subseteq\mathrm{AM}^O\)).
- General-poset hardness and the existing winning-frontier/DAG results do not transfer to the fixed antichain AM question; the frontier barrier concerns enumeration and does not establish AM non-membership.

**Recommended next action:** let the keeper record this run’s finding from the agent output, or flag the ledger entry for review. No further mathematical work or repository action is warranted from this turn.

## Other metadata

```json
{
  "finished_at": 1794133933.8644798,
  "started_at": 1794132517.8539636
}
```
