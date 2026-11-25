# antonina-MFpOF57F7bOlCOJxdt31D4-flash

Session: ses_e178f1a6cffePv8n8MoD7EFgVW
Workspace: /home/lubko/soring301-exec-framed-dag-n5-20261117d
Created: 1794901075435; updated: 1794901185698

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 100 (msg_1e8726df00015ShbXRhqNMRyz4)

Produced and saved a checked exact-height permutation-framed strategy DAG witness for `n=5` at budget `S(5)=7`, with measurements and report.

**Deliverables (worktree):**
- [`exec-report.md`](exec-report.md) — problem/baseline, methods/tools/commands, concrete results, verification, open questions/next falsifiable step.
- [`witness_n5_h7_framed.json`](witness_n5_h7_framed.json) — explicit framed strategy DAG certificate (`n=5`, `budget=7`, identity slot permutations).
- [`witness_n5_h7_framed_stats.json`](witness_n5_h7_framed_stats.json) — derived size/profile data.

**Verified result (soundness checker):**
- `python3 scripts/check_framed_strategy.py witness_n5_h7_framed.json` → `ACCEPT: n=5, depth=7, nodes=239`
- Control: `python3 scripts/check_framed_strategy.py --bubble 5` → `ACCEPT: n=5, depth=10, nodes=11`

**Concrete measurements (exact-height-7 witness):** 239 nodes total (119 compare, 120 leaves), 238 directed edges, max depth 7, depth histogram `{0:1,1:2,2:4,3:8,4:16,5:32,6:64,7:112}`, rooted tree (`edges = nodes-1`), all arc permutations identity. Construction: one optimal minimax policy over labelled successor-bitmask posets (logic consistent with `scripts/strategy_dag_probe.py`, which gives `S(5)=7`, `DAG(1)=239`, `quotient(1)=11`).

**Structural note:** This is an explicit checked optimal-policy tree in labelled slot space (no state merges in this policy), small at `n=5` but not evidence of an all-`n` polynomial-size exact-height framed certificate; polynomial framed envelopes exist at larger/non-optimal heights (e.g. bubble) per `docs/research-framed-certificate-frontier.md`. Details, comparisons, and the next falsifiable compression/join step are in `exec-report.md`.
