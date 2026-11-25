# antonina-jMzo3NdG3DjWeSlRdwDDXd-analogies

Session: ses_e1700c007ffeUzSVSJeEr30JlL
Workspace: /home/lubko/soring301-exec-framed-dag-n15-20261117e
Created: 1794910404734; updated: 1794910678202

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 143 (msg_1e9030dfd001ocgGfwcZLtWn9m)

## Deliverables (saved)
- **Report:** `exec-report.md`
- **Verified artifact:** `artifacts/bubble_n15_budget105.json` (also `/tmp/opencode/soring301-n15-artifacts/bubble_n15.json`)

## (1) Problem / baseline `S(15)=42`
- Front: `framed-dag-witness-n15-exact` (falsifiable). Question: explicit, checkable permutation-framed strategy DAG certificate of exact height `S(15)=42` for `n=15`, and its concrete size/depth/profile vs polynomial envelopes.
- Format/checker: `scripts/check_framed_strategy.py` (topological DAG, root 0, `compare` + `lt/gt` edges with slot `perm`, `leaf`; propagated/intersected guaranteed strict orders; sound, polynomial in explicit graph size and `n`; polynomial-size completeness for optimal strategies unknown per `docs/research-framed-certificate-frontier.md`).
- Baseline/literature in repo: `S(15)=42` (`docs/research-certificates-barriers.md`, citing Jing et al.). Bounds recomputed: `ceil(log2(15!))=41`, Ford–Johnson `F_FJ(15)=∑_{j=1}^{15} ceil(log2(3j/4))=42` (equals `S(15)` for n=15, not in general), balanced merge-sort worst-case `M(15)=45`, bubble `105`.

## (2) Methods / tools / commands
- Inspected: `docs/research-framed-certificate-frontier.md`, `docs/research-strategy-certificates.md`, `docs/research-certificates-barriers.md`, `docs/research-state-compression.md`, `scripts/check_framed_strategy.py`, `scripts/strategy_dag_probe.py`, `scripts/generate_optimal_tree.py`, `scripts/evaluate.py`, `scripts/upper_witness.py`.
- Ran: `python3 scripts/check_framed_strategy.py --bubble 4|15`, bound computations (info/FJ/merge/bubble), generated+verified bubble cert via `triangular_bubble_certificate`/`check_certificate` and saved artifact. Attempted `python3 scripts/strategy_dag_probe.py --max-n 6` (timed out at 120s; not needed). No existing in-repo `*n15*` witness artifacts found.

## (3) Results — witness or obstruction (evidence)
- **Verified baseline witness (not exact-height):** `artifacts/bubble_n15_budget105.json` — triangular bubble framed certificate, checker result `ACCEPT: n=15, depth=105, nodes=106` (105 comparison nodes + 1 leaf, chain/path structure), budget 105, 19075 bytes.
- **Exact-height `S(15)=42` witness:** **not constructed** (no explicit checker-verified framed DAG at height 42 produced).
- **Precise obstruction/evidence:** (a) no framed DAG generator for exact/Ford–Johnson strategies in tooling (`check_framed_strategy.py` has only `--bubble`; `upper_witness.py` does not emit framed DAG JSON). (b) Explicit optimal/reduced comparison tree is infeasible at n=15 (`15! ≈ 1.31e12` leaves); single-policy hash-consed DAG equals tree in small-n evidence (`docs/research-strategy-certificates.md`, Thm 2.6/Cor 2.7). (c) Known polynomial framed constructions don’t certify 42 here: merge-sort framed construction is `O(n^2)` nodes but path length `O(n log n)`/45 for n=15; Ford–Johnson rank-envelope framed embedding is described as *plausible* for `F_FJ(n)` but requires audited complete recursive frame/join construction (`research-framed-certificate-frontier.md` §3/§5). Since `F_FJ(15)=42=S(15)`, a correct framed FJ certificate would be an exact witness, but this implementation/audit is missing. (d) Naive optimal/all-optimal DAG/quotient sizes grow rapidly in experiments (n≤6 data in docs), giving no compact explicit n=15 witness by enumeration.
- **Best certifiable budget found (explicit verified framed artifact):** 105 (106 nodes). **Best known algorithmic budget matching target:** 42 (Ford–Johnson), without an explicit checker-verified framed DAG artifact.

## (4) Verification
- `python3 scripts/check_framed_strategy.py --bubble 4` → `ACCEPT: n=4, depth=6, nodes=7`
- `python3 scripts/check_framed_strategy.py --bubble 15` → `ACCEPT: n=15, depth=105, nodes=106`
- Saved artifact programmatically verified: `check_certificate(...)` depth `105`, nodes `106`.
- Baselines recomputed: `ceil(log2(15!))=41`, `F_FJ(15)=42`, merge-sort worst-case `45`.

## (5) Next falsifiable step
1. Implement a framed-certificate JSON generator for standard Ford–Johnson (merge insertion) with explicit slot permutations and locally checkable rank-envelope joins per `docs/research-framed-certificate-frontier.md` §3 (pairing, winner recursion carrying losers, Jacobsthal order, `current[ell_j] < x_j < current[u_j+t]`, odd case), including join/cost/frame audit (§5 item 4).
2. **Falsifiable test:** `python3 scripts/check_framed_strategy.py <fj_n15.json>` with budget 42. **Pass:** `ACCEPT`, depth ≤42 (target 42) with recorded node/edge/depth/profile vs `O(n^2)` envelope. **Fail/refute:** `REJECT` or inability to realize sound joins within 42 exposes a concrete gap in the proposed framed embedding for n=15 (frames/boundaries/odd/recursion accounting). If blocked, produce an audited framed merge-sort certificate at budget 45 for n=15 as an intermediate verified polynomial-size profile point.
