# antonina-il5V3bF9yyl9Y7gWdbkrxL-disposed

Session: ses_e16fcf9f0ffe8G50igRhUwDrFv
Workspace: /home/lubko/soring301-exec-framed-dag-n16-20261117f
Created: 1794910651984; updated: 1794911041757

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 164 (msg_1e908c1d2001mJkEltqE5HABs8)

## Outcome (framed-dag-witness-n16-exact, n=16)

- **Exact-height framed witness (budget 46): not achieved.** No explicit, checkable permutation-framed strategy DAG certificate of height `S(16)=46` for `n=16` was found in the repo or constructed/derived in this run. No height-46 artifact was produced/verified.
- **Best certifiable framed witness constructed & verified:** bubble compare-exchange certificate for `n=16`.
  - Artifact: `artifacts/bubble_n16_framed.json`
  - Verification: `python3 scripts/check_framed_strategy.py artifacts/bubble_n16_framed.json` → `ACCEPT: n=16, depth=120, nodes=121`
  - Exact counts/profile: `budget=120`, `depth=120`, `nodes=121` (120 comparison nodes + 1 leaf), `240` directed edges (2 outcomes/node), linear compare-exchange path (depth = nodes−1).
- **Baselines (evidence):** `S(16)=46` [literature: Stober & Weiß 2022], `⌈log2(16!)⌉=45`, Ford–Johnson `M(16)=∑⌈log2(3i/4)⌉=46` (equals optimum at 16), balanced merge-sort worst case `49` (`n log2 n - n + 1`). Docs note a plausible all-`n` polynomial framed certificate for standard Ford–Johnson (targeting `M(n)`) subject to audited recursive frame/join construction, but no explicit n=16 FJ/optimal framed generator or instance exists in-repo.
- **Obstruction (falsifiable/precise):** `S(16)=46` comes from large-scale search; an unshared optimal framed tree is infeasible (`2·16!-1` nodes, `16!` leaves). Poset-state DAG probe (`artifacts/strategy_dag_probe_max5.txt`, `scripts/strategy_dag_probe.py --max-n 5`, consistent with `docs/research-strategy-certificates.md`) shows single-policy DAG = tree and rapid all-optimal growth; no evidence/generator here for a polynomial-size explicit framed certificate at exact optimum for n=16. `--max-n 6` probe and `upper_witness.py --max-n 16` timed out (>120s) in this environment.
- **Next falsifiable step:** implement & audit an explicit Ford–Johnson framed-certificate generator for `n=16` and check with `scripts/check_framed_strategy.py` — `ACCEPT` at `depth==46` would yield the requested exact witness with concrete counts/profile; `REJECT` or `depth>46` would falsify that framing/implementation as an exact `S(16)` certificate.

**Durable deliverables saved:**
- `exec-report.md` — (1) problem/baseline, (2) methods/tools/commands, (3) results/witness or obstruction with evidence, (4) verification, (5) next falsifiable step.
- `artifacts/bubble_n16_framed.json` — verified framed certificate (n=16, depth 120).
- `artifacts/strategy_dag_probe_max5.txt` — strategy DAG scaling context (n≤5).
