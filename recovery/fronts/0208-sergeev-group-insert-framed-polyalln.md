# sergeev-group-insert-framed-polyalln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

vAi2qu4BViPylQhtH86iWE-restive

## exit_state

clearexit

## question

Can Sergeev's group-insertion construction for S(n) <= log2(n!) + o(n) be compiled into a polynomial-size sound framed certificate (permutation DAG with meet/intersection joins) that attains height exactly S(n) for all large n, or is there an all-n obstruction from coupled interval containers and join constraints?

## basis

Sergeev ECCC 2020 group insertion gives o(n) surplus; framed-certificate frontier notes coupled containers resist global join control states; multiple prior fronts investigated fragments without resolving all-n completeness.

## falsifier

Exhibit either (a) a polynomial all-n framed compilation with verified height bound and independent checker acceptance for tested n, or (b) an explicit infinite family and a proof that any sound permutation-frame compilation of group insertion forces exponential join size or height > S(n).

## implication

A successful all-n polynomial compilation would yield a uniform NP upper-bound pathway for SORT-BOUND-U; a general obstruction would rule out this major route to polynomial certificates.

## finding_unverified

me/lubko/soring-fronts/sergeev-group-insert-framed-polyalln/docs/research-framed-certificate-frontier.md` – framed grammar, “Sergeev compatibility”, coupled interval containers, join/entropy discussion
- `/home/lubko/soring-fronts/sergeev-group-insert-framed-polyalln/docs/research-sergeev-asymptotic.md` – Sergeev bound and structural entropy identity
- `/home/lubko/soring-fronts/sergeev-group-insert-framed-polyalln/scripts/check_framed_strategy.py` – intersection-join semantics
- `/home/lubko/soring-fronts/sergeev-group-insert-framed-polyalln/docs/problem.md`, `/home/lubko/soring-fronts/sergeev-group-insert-framed-polyalln/AGENTS.md`
- `/home/lubko/soring-fronts/framed-certificate-polynomial-completeness-barrier/docs/research-framed-certificate-completeness-obstruction.md` – sibling/forgetful-join obstruction
- `/home/lubko/soring-fronts/forgetful-join-exponential-classes/docs/research-framed-certificate-frontier.md` – forgetting loss identity
- `/tmp/tr20-096.pdf` – Sergeev ECCC TR20-096 source
Continue if you have next steps, or stop and ask for clarification if you are unsure how to proceed.
## What we did so far (in this front)

### Setup & orientation
- Read `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, `docs/operations.md` for constraints (unary `SORT-BOUND-U`, framed certificate model, complexity implications).
- Checked board #301 (front dispatched as falsifiable all-n compilation/obstruction target for Sergeev group-insertion → polynomial framed certificate).
- Searched across soring-fronts for `coupled interval containers`, `group insertion`, `framed compilation`, `join constraint`, `exponential join size`.
- Retrieved Sergeev ECCC TR20-096 (`/tmp/tr20-096.pdf`) and inspected key parts (interval containers / group-insertion structure).

### Docs & model verification
- Reviewed `docs/research-framed-certificate-frontier.md` (certificate grammar with intersection joins, soundness vs completeness, merge sort O(n²) DAG vs optimality, rank-envelope/Ford–Johnson, entropy/forgetting identity).
- Reviewed `docs/research-sergeev-asymptotic.md` (Theorem 3: `S(n)=log₂(n!)+O(n/(log n)^(1/5))`, entropy identity for excess).
- Reviewed `scripts/check_framed_strategy.py` and ran tests: `python3 -m unittest tests.test_framed_strategy` → OK (6 tests).
- Looked at sibling fronts: `framed-certificate-polynomial-completeness-barrier` (root-prefix sibling/forgetful-join obstruction ideas), `forgetful-join-exponential-classes` (forgetting loss identity).

### Current state
- **Goal**: Try to compile Sergeev’s group-insertion (uses coupled interval containers) into a polynomial-size sound framed certificate achieving height `S(n)` for all large `n`, or find an all-n obstruction.
- **Open**: No concrete polynomial all-n compilation or explicit infinite-family obstruction found yet. Exact mechanism of “coupled interval containers” + intersection joins is not fully pinned down; unclear if recoverable or forces exponential join size / height > S(n).

### Next steps (proposed)
1. Extract precise state of group-insertion (interval/container partitions + cross-container coupling) and see what the guaranteed relation `R` can represent / loses at joins.
2. Model forgetting loss `λ_b` under intersection joins for that class; test if maintaining height near `log₂(n!)` forces ≥ Ω(n) loss contradicting `o(n)` necessary condition.
3. Try to isolate a scalable gadget (inspired by sibling-prefix/root constraints) giving a falsifier or concrete obstruction.


## Other metadata

```json
{
  "finished_at": 1793666081.8482053,
  "retry_after": 0,
  "started_at": 1793657378.5795732
}
```
