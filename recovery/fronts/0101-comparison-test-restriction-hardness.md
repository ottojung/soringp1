# comparison-test-restriction-hardness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

UKTU5OrxMrxmwIGxjtUJCs-luxury

## exit_state

clearexit

## question

For the minimum-height comparison decision tree (only pairwise comparisons, adversarial outcomes forming a total order), is the exact construction NP-hard for the antichain root S(n), or does the pairwise-test restriction strictly separate it from the arbitrary-test case where Hyafil–Rivest shows NP-completeness?

## basis

Hyafil–Rivest arbitrary tests vs pairwise comparisons audited in docs/research-hardness-boundaries.md; transfer blocked by model restriction and no known reduction for S(n).

## falsifier

Produce a polynomial-time reduction from some NP-complete problem to constructing a height-S(n) comparison tree for some family, or prove the comparison-restricted problem is in P by a uniform all-n construction with a checkable correctness argument.

## implication

A proof of NP-hardness for the restricted comparison model would change the complexity picture beyond arbitrary tests; a P-membership proof would rule out that route for NP membership of SORT-BOUND-U.

## finding_unverified

struction on completion.

## Relevant Files
- `/home/lubko/soring-fronts/comparison-test-restriction-hardness/AGENTS.md` — project contract (billy-dev only, unary target)
- `/home/lubko/soring-fronts/comparison-test-restriction-hardness/docs/problem.md` — definitions of `S(n)`, `SORT-BOUND-U/B`, models
- `/home/lubko/soring-fronts/comparison-test-restriction-hardness/docs/operations.md` — host, Antonina issue `#301`, board digest usage
- `/home/lubko/soring-fronts/comparison-test-restriction-hardness/docs/research-hardness-boundaries.md` — Hyafil–Rivest/Laber–Nogueira/Parberry audit, sparsity/non-sparsity, PSPACE notes
- `/home/lubko/soring-fronts/comparison-test-restriction-hardness/docs/research-certificates-barriers.md` — game `G(n,k)`, Claim A (PSPACE), certificate barriers
- `/home/lubko/soring-fronts/comparison-test-restriction-hardness/docs/research-strategy-certificates.md` — strategy DAG, verifier, Mahaney/sparsity, growth experiments
- `/home/lubko/soring-fronts/comparison-test-restriction-hardness/docs/research-framed-certificate-frontier.md` — framed certificates, soundness vs completeness
- `/home/lubko/soring-fronts/comparison-test-restriction-hardness/scripts/research_frontier.py` — frontier prompt/ledger integration (references issue `#301`)
- `/home/lubko/soring301/scripts/board_digest.py` — read Antonina issue `#301` without dumping full board
Continue if you have next steps, or stop and ask for clarification if you are unsure how to proceed.
Looking at the git history and docs in this repo, here's what we know:

## Context
This is the `comparison-test-restriction-hardness` worktree on billy-dev investigating whether constructing a minimum-height comparison decision tree for the antichain root S(n) is NP-hard (or separated from Hyafil–Rivest).

## Work done so far (git history)
Recent commits show:
- `0ca6bb1` - Prove odd antichain-star resets unrealizable
- `1f27d8e`, `e3aa9a3` - Extended two-phase exact sorting witness work
- `ab0d809` - Independent checker for two-phase witnesses
- `39e27a3` - Two-phase exactness fully characterized; n<=22 hit/miss table; tau(n)=Omega(n) drift
- `7b89ef5` - Independent Sergeev ceiling referee audit
- Merged to branch `research/exact-reset-tree-realizability-20261027`

The docs describe:
- **Model audit** (docs/research-hardness-boundaries.md): Hyafil–Rivest is about arbitrary subset tests (EC3 gadget needs 3-element subset tests), not pairwise comparisons. Transfer blocked. Laber–Nogueira also arbitrary tests. Parberry different model.
- **Sparsity barrier**: SORT-BOUND-U is sparse → many-one NP-hard would imply P=NP (Mahaney). SORT-BOUND-U ∈ PSPACE via alternating game G(n,k).
- **Certificates**: Strategy DAG verifier is sound/polytime in DAG size, but no known all-n polynomial-size certificate for exact S(n).
- **Known values**: S(n) known up to ~n<=22; strategy DAGs grow quickly.

## Current state
From Viche Executive updates on issue #301: this front (`comparison-test-restriction-hardness`) has been running alongside others (circuit-adversary-alternation, information-theoretic-transcript-barrier, reduction-to-graph-properties, etc.). The curator exhausted with 0 new fronts. Research continues until final theorems for S(n)/SORT-BOUND-U are proved and independently checked.

The active question is the NP-hardness/separation question described in AGENTS.md - whether constructing a minimum-height pairwise comparison tree for the antichain is NP-hard vs separated from Hyafil–Rivest.


## Other metadata

```json
{
  "finished_at": 1793453660.1614513,
  "started_at": 1793430403.0977015
}
```
