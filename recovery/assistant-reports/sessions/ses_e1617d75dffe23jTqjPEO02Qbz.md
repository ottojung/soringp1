# antonina-rJbsLMp8EvvaAImtf6yzJC-acorn

Session: ses_e1617d75dffe23jTqjPEO02Qbz
Workspace: /home/lubko/soring301-exec-local-certificate-verifier-complexity-20261117
Created: 1794925668593; updated: 1794925799063

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 53 (msg_1e9e9f24c001Uo4o7vmbqbxf3n)

## Delivered
- Created `exec-report.md` (only repo change) with labeled evidence ([definition], [deduction], [paper construction/claim], [experiment/implementation], [open/literature context]) addressing permutation-framed DAG certificates of height `S(n)`.

## What the report covers
- **Definitions:** explicit permutation-framed comparison DAG grammar/semantics (queries, outcomes, slot permutations/frames, transitive closure, join-by-intersection, reachable total-order leaves, depth/budget), size parameters, and restricted forms (tree/in-degree, bounded width, local frame constraints), grounded in `docs/research-framed-certificate-frontier.md` and `scripts/check_framed_strategy.py`.
- **Soundness checking vs completeness/existence:** separated clearly—soundness is a property of a given explicit certificate; completeness/existence asks for poly-size certificates for all yes-instances at `S(n)` and remains open.
- **Verification complexity (soundness):** theorem-style argument that local checking is polynomial in explicit graph size and `n` (checker-level bound `O(|V|·n^3)` from closure/rename/intersection/leaf checks); acceptance implies a sound witness for `S(n) ≤ k`. Notes this is polynomial in certificate size, not by itself NP membership.
- **Restricted forms/obstructions:** 
  - **Tree / in-degree ≤1:** unavoidable `≥ 2·n!−1` node obstruction (exponential; joins required for succinctness).
  - **Local frame constraints:** poly-size all-`n` non-optimal witnesses exist (e.g. bubble compare-exchange, `Θ(n^2)`), but no known all-`n` optimal-height `S(n)` poly-size certificate under such/local constructions.
  - **Bounded in-degree ≥2 / bounded width (DAG sharing):** necessary to beat tree blowup, but no proved all-`n` poly-size optimal completeness and no proved universal super-polynomial obstruction established in consulted sources (open).
- **Implications for `SORT-BOUND-U` in NP/coNP:** poly-size all-`n` optimal framed certificates would imply `SORT-BOUND-U ∈ NP`; framed DAGs are upper-bound witnesses (coNP/lower-bound succinct certificates not established); explicit trees are exponential; no separation claims (consistent with `SORT-BOUND-U ∈ PSPACE`, sparsity/Mahaney constraints).
- **Falsifiable/open next checks:** optimal-height poly-size family or class-specific obstruction, audit of rank-envelope/FJ frame construction, and optimal-play state-count measurements.

## Sources used
`AGENTS.md`, `docs/problem.md`, `docs/research-plan.md`, `docs/research-framed-certificate-frontier.md`, `docs/research-certificates-barriers.md`, `scripts/check_framed_strategy.py`. No Lean/repo changes beyond `exec-report.md`, no PR.
