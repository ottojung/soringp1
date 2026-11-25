# Oracle-aided pruning traces for `G(12,29)` / `G(12,30)` (falsifiable attempt)

**Task:** SoringP1 #301 (billy-dev), 2026-11-05.  
**Model:** adaptive pairwise comparison sorting of `n` distinct labelled keys; `S(n)` is the minimax comparison height (`docs/problem.md`, `SoringP1/Minimax.lean` context). `G(n,k)`: sorter picks an incomparable pair, adversary answers consistently, transitive closure applied; sorter wins iff a total order is reached within `k` comparisons, so `S(n) <= k` iff sorter wins `G(n,k)` `[definition, deduction]`. Unary target: `SORT-BOUND-U = {1^n#1^k : S(n)<=k}`.  
**Labels:** `[definition]`, `[literature]`, `[deduction]`, `[experiment]`, `[open]`. No separation/NP/PSPACE claim is made.

## 1. Question and required trace discipline

Falsifiable target: produce a small, independently replayable oracle-aided refutation trace for `G(12,29)` or height-30 yes trace for `G(12,30)` where
1. the trace format is explicit, and
2. every oracle claim is a stated checkable lemma/constraint (not raw search output treated as a certificate).

If full `n=12` is infeasible, report the maximal verified small-`n`/constrained fragment trace and the exact `n=12` blocking step with measured resource/size.

## 2. Inputs / related artifacts read

- `AGENTS.md`, `docs/problem.md`, `docs/research-n12-nontightness.md`,
  `docs/research-certificates-barriers.md`, `docs/research-framed-certificate-frontier.md`.
- `scripts/check_framed_strategy.py` (yes-side framed DAG checker), `scripts/budgeted_dfs.py`, `scripts/transcript_dfs.py`.
- Sibling artifacts: `/home/lubko/soring-fronts/g1229-c4-compression-test-20261105/docs/g1229-c4-compression-test.md`, `/home/lubko/soring-fronts/s12k30-refuter-dag-size-20261105/docs/s12k30-refuter-dag-size.md`, and their `scripts/strategy_dag_probe.py`.
- Additional context consulted: `s12k29-refuter-certificate` / audit notes in `/home/lubko/soring-fronts/*s12k29*refuter*`.

`[literature]` `S(12)=30 > 29 = ceil(log2 12!)` (Wells; Ford–Johnson upper bound; later exhaustive confirmations summarized in repo literature/non-tightness notes). The known proofs are strategic/exhaustive searches; raw search output is not a short certificate.

## 3. Explicit oracle-trace format and checker `[definition, experiment]`

Added:
- `scripts/check_oracle_trace.py` — explicit JSON trace checker.
- `scripts/make_oracle_trace_examples.py` — generates replayable examples.

**Trace object (JSON):**
```json
{
  "kind": "refuter" | "sorter",
  "n": <int>, "k": <int>, "root": "<id>",
  "nodes": {
    "<id>": {
      "state": [succ_bitmask_int,...],  // transitive-closure successor bitmasks
      "budget": <int>,
      "type": "internal" | "leaf" | "oracle",
      // refuter internal: "rule" maps "i,j" (all incomparable pairs) to
      // {"answer":"lt|gt","next":id}
      // sorter internal: "compare":[i,j], "lt":{"next":id}, "gt":{"next":id}
      // oracle: {"name":..., "params":{...}, "constraints":[...]}
    }
  }
}
```

**Checked constraints/lemmas (mechanical, no raw search output trusted):** `root_antichain`, `budget_eq`, `state_tc` (antisymmetry+transitivity), `non_total`/`total`, `budget_zero`, `tc_edge` (child is TC of state+answer, budget decrements), `covers_all_incomparable` (refuter total move coverage), `budget_decrements`, `exhaustive_can_sort`/`exhaustive_cannot_sort` with `node_cap` (recomputes the claim by running `budgeted_dfs.can_sort`; rejects on node-cap hit). The checker also validates explicit refuter/sorter internal edges and leaf semantics.

Replay commands (independently rerunnable from repo root):
```bash
python3 scripts/check_oracle_trace.py docs/oracle-traces/g4k4_refuter_oracle.json
python3 scripts/check_oracle_trace.py docs/oracle-traces/g4k5_sorter_oracle.json
python3 scripts/check_oracle_trace.py docs/oracle-traces/g4k4_refuter_fragment.json
python3 scripts/check_oracle_trace.py docs/oracle-traces/g12k29_blocked.json
```
Observed `[experiment]`:
```
ACCEPT: ACCEPT refuter n=4 k=4 nodes=1
ACCEPT: ACCEPT sorter n=4 k=5 nodes=1
ACCEPT: ACCEPT refuter n=4 k=4 nodes=2
ACCEPT: ACCEPT refuter n=12 k=29 nodes=1   (structural constraints only; see §5)
```

## 4. Maximal verified small-n / constrained fragment traces `[experiment]`

| artifact | claim form | nodes | what is checked | result |
|---|---|---:|---|---|
| `docs/oracle-traces/g4k4_refuter_oracle.json` | `G(4,4)` refuter win (`S(4)>4`) | 1 | root antichain, TC, non-total, budget 4, `exhaustive_cannot_sort(value=False,node_cap=10^7)` recomputed by `budgeted_dfs.can_sort` | ACCEPT |
| `docs/oracle-traces/g4k5_sorter_oracle.json` | `G(4,5)` sorter win (`S(4)<=5`) | 1 | root antichain, TC, budget 5, `exhaustive_can_sort(value=True,node_cap=10^7)` recomputed | ACCEPT |
| `docs/oracle-traces/g4k4_refuter_fragment.json` | constrained `G(4,4)` fragment | 2 | root oracle plus explicit `tc_edge` move `(0,1), lt -> c01`; child state/budget/non-total and `exhaustive_cannot_sort` recomputed | ACCEPT |
| `scripts/check_framed_strategy.py --bubble 4` (existing yes-side checker) | framed yes witness | 7 | existing permutation-framed DAG checker | `ACCEPT: n=4, depth=6, nodes=7` |

These are **small-n/constrained** replayable traces: oracle claims are explicit constraints and, where used, the exhaustive budgeted-DFS lemma is mechanically rechecked by the verifier (not a raw search dump accepted on faith). The root-only oracle traces are intentionally *not* presented as short refuter/sorter strategy objects with total move coverage; they are checkable lemma-carrying trace objects demonstrating the format.

## 5. `n=12` blocked: exact blocking step and measurements `[experiment, deduction]`

**Blocked targets (not produced):** a full independently replayable oracle-aided refutation trace for `G(12,29)` and a full height-30 yes trace for `G(12,30)`.

### 5.1 Exact blocking step

1. **Trace-format/semantics blocker (refuter).** A complete refuter trace for `G(12,29)` must give, at every reachable sorter state, an adversary answer for **every** incomparable pair (total move coverage, `∀` sorter / `∃` adversary). At the antichain root `|Inc(P_0)| = C(12,2)=66` `[experiment]`. The existing framed checker is yes-side only; no in-repo refuter framed checker exists `[deduction]` (cf. `s12k30-refuter-dag-size.md`).
2. **Exhaustive-oracle blocker.** Replacing subgames by an `exhaustive_cannot_sort` / `exhaustive_can_sort` oracle is only replayable here if the checker can recompute it. Pure budgeted DFS (`scripts/budgeted_dfs.py`, no memoization, transcript/backtracking-style recursion) is the available uniform checker; it becomes infeasible long before `n=12`.
3. **Explicit/DAG/C4 materialization blocker.** Prior bounded measurements show explicit total-coverage refuter/C4/DAG materialization explodes rapidly (`G(5,6)` ~1,146 nodes/3,995 rule entries uncompressed; `G(6,9)` C4 build aborted >30,003 nodes with 58,806 adversary-win memo states; yes-side unfolded trees have `2*n!-1` nodes — `958,003,199` for `n=12`). `n=12` labelled posets are `A001035(12)=414,864,951,055,853,499` in general `[literature/deduction from cited notes]`. Naive `S_n` canonicalization is `12!=479,001,600` per state `[deduction]`.

### 5.2 Measured resources (this worktree)

Commands/measurements (`python3`, budgeted DFS primitive, node-cap counted by recursive calls, RSS from `resource` maxrss KB on this Linux host):

| instance | oracle/check attempted | result | calls | wall sec | RSS KB |
|---|---|---|---:|---:|---:|
| `G(4,4)` | `can_sort(empty,4,4)` cannot-sort | False, exact under cap | 645 | 0.0020 | 12472 |
| `G(5,6)` | `can_sort(empty,5,6)` cannot-sort | False, exact under cap | 125,407 | 0.2674 | 12472 |
| `G(6,9)` | `can_sort(empty,6,9)` cannot-sort | **hit cap** | 10,000,001 | 33.64 | 12472 |
| `G(7,12)` | `can_sort(empty,7,12)` cannot-sort | **hit cap** | 2,000,001 | 7.04 | 12472 |
| `G(12,30)` | `can_sort(empty,12,30)` can-sort probe | **hit cap** | 100,001 | 0.63 | — |
| `G(12,30)` | `can_sort(empty,12,30)` can-sort probe | **hit cap** | 1,000,001 | 6.81 | — |
| `G(12,29)` | structural-only blocked trace | TC/root/budget/non-total constraints checked; no exhaustive claim | 1 node | n/a | 9 KB JSON |

The `G(12,29)`/`G(12,30)` exhaustive oracle lemmas therefore **cannot be discharged** by the replayable checker at the tested caps; emitting them as raw search success would violate the task constraint. `docs/oracle-traces/g12k29_blocked.json` records only structural constraints and explicit blocking parameters — it is **not** a proof/certificate that `S(12)>29`.

## 6. Conclusion

- **Achieved:** explicit oracle-trace format + independent checker (`scripts/check_oracle_trace.py`), checked small-n/constrained replayable traces (`G(4,4)` refuter oracle, `G(4,5)` sorter oracle, `G(4,4)` explicit tc-edge fragment), and a structural blocked `G(12,29)` trace object.
- **Not achieved:** a full `G(12,29)` refuter trace or full `G(12,30)` height-30 yes trace. Full `n=12` is infeasible with available exhaustive/explicit/compressed-checked methods.
- **Exact blocking step:** total-coverage adversary semantics at the 66-move root plus exponential/strategic search below it; exhaustive budgeted-DFS oracle recomputation hits a 10^7-call cap already at `G(6,9)` and cannot make progress on `G(12,30)` probes at 10^5–10^6 calls; explicit/C4/refuter DAGs and canonicalization have measured/derived blowup barriers from the cited sibling experiments.
- **No separation/NP claim.** This is an obstruction/feasibility report with replayable small traces and measured resource limits only.
