# comparison-split-kraft-obstruction

## status

blocked

## origin

ai_proposal_unverified

## agent_id

ZAM8S1hmyGc7wVctu283Fi-dreams

## exit_state

failed

## question

Establish an all-n necessary condition on comparison trees stronger than Kraft/log2(n!) arising from the fact that a pairwise comparison produces a partition into two order ideals in a way not realizable by arbitrary prefix codes, and see if it forces a uniform super-logarithmic gap for some infinite n family relevant to exact S(n).

## basis

Kraft inequality and comparison model constraints; 1/3-2/3 literature notes feasibility is subtle but no universal all-n Kraft+feasibility gap theorem is recorded.

## falsifier

Prove the comparison-realizable partition classes are dense enough that no fixed constant-factor information gap holds for all large n, or construct explicit optimal (by height) trees asymptotically approaching information bound via feasible comparison splits.

## implication

A rigorous all-n comparison-feasibility obstruction (distinct from general poset adversaries) would give a new lower-bound technique for S(n) evaluation without appealing to circuit lower bounds or P/poly.

## finding_unverified

r's size limit due to large media attachments. The conversation was compacted and media files were removed from context. If the user was asking about attached images or files, explain that the attachments were too large to process and suggest they try again with smaller or fewer files.

Continue if you have next steps, or stop and ask for clarification if you are unsure how to proceed.
Let us look at the full context again. The user said "What did we do so far?" and then pasted a very long message. Let us look up the actual repo state - maybe there is a branch, or maybe the task is to continue from where it left off.

Let us look at git branch and recent changes.

Clean working tree on main. The previous message was a long context dump from the user about what "we" did - maybe it was giving me context about ongoing work. Let us look at the board/operations and recent research notes to understand current state better. Also maybe look at docs/operations.md and see if there is info about #301.

I need to summarize what has been done so far in this repo. Let us look at recent activity.

## Repo summary (SoringP1 / exact sorting number S(n))

Research repo studying the uniform complexity of the exact sorting number `S(n)` (minimum worst-case adaptive pairwise comparisons to sort n distinct labeled keys). Focus is on **unary encoding** `SORT-BOUND-U = {1^n # 1^k : S(n) <= k}` (binary not active). 

### Key model (from Lean)
- Deterministic adaptive comparison trees (`ComparisonTree n`, `height`, `Correct`, `HasBudget`, `S(n)=sInf{k | HasBudget n k}` attained)
- Minimax game / partial orders (`splitPairs`, `adv`) in `SoringP1/Model.lean`, `SoringP1/Minimax.lean`
- `SORT-BOUND-U ∈ PSPACE`, sparse (no many-one NP/EXPTIME hardness), in P/poly (circuit bounds useless). Goal is upper bounds/barriers/structural theorems about minimax, not unconditional super-polynomial unary lower bounds.

### Recent major work (git history)
- **Exact-reset / antichain-star realizability** (merged): proved odd antichain-star resets unrealizable; explored exact-budget winning-frontier barriers.
- **Framed sorting certificates**: polynomial-size DAG certificate grammar (sound), all-n constructions for merge sort (O(n²) nodes, O(n log n) paths) and rank-envelope/insertions (Ford–Johnson style) give polynomial certificates for those strategies; completeness unknown (would put SORT-BOUND-U in NP).
- **Continuous research frontier system** (#53-#55): claim-once ledger, per-front isolated checkouts/agents, curator commissions fronts when idle, keeper supervises via s6 on billy-dev only. Research continues until founder theorems proved/published/closed.
- **Policy consolidation**: unified AGENTS.md contract, docs consolidated, pool keeper cwd/continuity fixes.

### Active infrastructure
- Lean library (`lake build`) must stay green; formalization only for mature, relevant theorems with justification (minimax correspondence complete).
- Experiments/scripts: `scripts/one_ply_obstruction.py`, `scripts/evaluate.py`, `scripts/budgeted_pruning_experiments.py`, `scripts/parallel_module_probe.py`, `scripts/check_framed_strategy.py`, etc.
- Research tracked on **Antonina issue #301** (billy-dev only); board digest via `python3 /home/lubko/soring301/scripts/board_digest.py`.

### Current state
Clean working tree on `main`. Recent merges closed research fronts around exact-reset realizability and winning-frontier barriers; system is in continuous frontier mode. No uncommitted changes.

## Other metadata

```json
{
  "finished_at": 1793653922.2781045,
  "started_at": 1793639882.5012727
}
```
