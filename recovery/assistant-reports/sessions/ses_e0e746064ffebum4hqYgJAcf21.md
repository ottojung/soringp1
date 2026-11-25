# antonina-yGAWVGXBzhHIhx0l2L4ey8-friendly

Session: ses_e0e746064ffebum4hqYgJAcf21
Workspace: /home/lubko/soring-fronts/curator
Created: 1795053821953; updated: 1795054128784

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 184 (msg_1f18fbbc3001OkHkf9v3nM0bAN)

## Studied (billy-dev context)
- Read: `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, `docs/research-winning-frontier-barrier.md`, `docs/research-framed-certificate-frontier.md`, plus recent `board_digest.py` outputs for Antonina issue #301 (page 1, recent/frontier-filtered excerpts). Board shows recent frontier reports including `loose-n-transition-depth-bound`, `compositional-antichain-strict-excess`, `lookahead-tightness-strategy-extraction`, `admissible-frontier-growth-alln` (report title variant in posts), `sublinear-window-lookahead-attainment`, `info-gap-*`, `abc-tree-completeness-*`, `t12-*`, etc., and Executive verification notes (2026-11-19). No repo/Lean/workflow changes made by me.

## Attacker attempt (precise all-n falsifiable claim about complexity of EXACT unary S(n)) — serious attempt, honest limits

I attacked two concrete, all-n falsifiable claims (stated carefully) and tried to disprove them using primary/literature + repo docs + board context. Labels below use: definition/literature/deduction/experiment/conjecture as appropriate.

### Claim 1 (complexity/class): “`SORT-BOUND-U ∈ NP` for all valid unary inputs” (i.e. some polynomial-time verifiable, polynomial-size certificate family exists for every yes-instance in unary encoding).
- **Evidence (literature/deduction):** `problem.md`/`AGENTS.md`: NP membership not established; an optimal sorting decision tree may be exponential in nodes so it is not a certificate by itself. `SORT-BOUND-U` is sparse (deduction from structure) so Mahaney implies many-one NP-hardness ⇒ P=NP (barrier), but this does **not** imply NP membership. `docs/research-framed-certificate-frontier.md` (paper-level constructions + implemented sound checker): sound permutation-framed DAG certificates are checkable in time polynomial in the explicit graph and n; polynomial-size sound DAGs exist for merge-sort style witnesses in form but merge architecture gives a known comparison surplus vs `S(n)` for all large powers of two (Sergeev asymptotics cited), and explicit Ford–Johnson framed constructions give polynomial DAGs for `F_FJ(n) != S(n)` in general; **optimal-height (height `S(n)`) completeness for all n is open**. Parberry-style generic-network verification hardness is noted as a different model barrier (not a direct proof about fixed-root framed completeness), reinforcing the need to separate soundness from completeness.
- **Attempt to disprove (serious):** tried to find any all-n argument that forbids polynomial-size framed (or any polynomial-checkable) certificates for all yes-instances. Found none: no infinite counterfamily, no proved representation lower bound for framed DAGs at height `S(n)`, and the winning-frontier barrier (`research-winning-frontier-barrier.md`) constrains naive enumeration of many winning states (|frontier| `2^((1/4-o(1))n(log n)^2)` in that construction family context) but explicitly states selective/symbolic methods are not excluded and does **not** imply certificate nonexistence/non-membership. 
- **Honest limits / consequence:** cannot disprove Claim 1. Importantly, a disproof in the strong sense “`SORT-BOUND-U ∉ NP`” would imply **`NP ≠ PSPACE`** (since `SORT-BOUND-U ∈ PSPACE`, deduction from `problem.md`/`AGENTS.md`) — that is an equivalent-to-known-open separation and out of scope to “achieve”; I produced no such proof and have no method. Thus the claim remains open; current evidence supports “no proof either way”, with soundness≠completeness as the central pitfall (framed grammar sound, all-n polynomial completeness unproved).

### Claim 2 (complexity/time): “`S_unary(1^n)` is computable in deterministic time `2^{O(n log n)}` for all `n>=1`” (uniform exact evaluation).
- **Evidence:** `problem.md`/`research-plan.md` list this as an open target; known upper bound from budgeted DFS is `2^{O(n log^2 n)}` time for the numeric function (with stated space), and unary threshold bounds given separately. `research-winning-frontier-barrier.md` (paper theorem + finite witnesses, audited in repo context): a large reachable winning frontier exists (`2^((1/4-o(1))n(log n)^2)` nonisomorphic winning states in the constructed family at relevant budgets, including in the exact-`S(n)` surplus regime by Sergeev asymptotics as stated there), so any method that must enumerate all such winning states is excluded from that class of approaches; it **does not** exclude selective minimax/search, symbolic compression, algebraic methods, etc., and gives no general time lower bound for arbitrary evaluators.
- **Attempt to disprove (serious):** sought an obstruction forcing `>=2^{ω(n log n)}` uniform time. No such unconditional/established obstruction found; barrier rules out one broad enumeration route but not the claim. No counterexample algorithm refutation possible from known finite data alone.
- **Honest limits:** cannot disprove Claim 2. A general proof of the `2^{O(n log n)}` upper bound is also open (and would avoid the winning-frontier enumeration trap). I did not confuse general-poset phenomena with antichain `S(n)` results beyond citing the docs’ warnings; all points above stay tied to the antichain/unary `SORT-BOUND-U`/`S_unary` setting as in `problem.md`.

### Distinctions applied (required)
- **General-poset vs antichain root:** cited barriers/constructions are discussed only in the sorting-number/antichain-root framework of this repo; I did not claim transfer from arbitrary partial-order optimization hardness without reduction (per `AGENTS.md`).
- **Certificate soundness vs completeness:** framed-DAG soundness/checkability is distinguished from all-n polynomial completeness at height `S(n)` (the open gap). I did not treat “some polynomial witnesses exist for weaker bounds/special schemes” as completeness for exact `S(n)`.

### What I did **not** do
- No Lean files created/modified; no repository code changes. No proof or verification claimed. No attempt to solve NP!=PSPACE/PSPACE separations.

## Curator output (written file)
Wrote **only** this JSON object to: `/home/lubko/soring-fronts/curator/frontier-candidates.json`

```json
{
  "fronts": [
    {
      "id": "framed-optimal-height-polysize-existence",
      "question": "For every integer n>=1, does some sound permutation-framed DAG of node count polynomial in n achieve longest path exactly S(n) for the n-key antichain, beyond known merge-sort and Ford-Johnson surpluses?",
      "falsifier": "Find an infinite family of n where every sound permutation-framed DAG with polynomially many nodes in n has longest path >= S(n)+1, proved by an invariant or explicit witness argument.",
      "implication": "A uniform affirmative would imply SORT-BOUND-U in NP via checkable framed certificates; a uniform negative would block framed-DAG completeness at exact height and refocus certificate work.",
      "basis": "research-framed-certificate-frontier.md reports sound polynomial merge/FJ constructions with known surpluses and states optimal-height completeness is open for all n."
    }
  ]
}
```

If you want, I can also propose a second front (e.g. a sharp, all-n question about whether any uniform symbolic/state-compression method can bypass the winning-frontier enumeration barrier in a provable model) — but I kept the list minimal and non-duplicative per instructions; current file contains the single front above.
