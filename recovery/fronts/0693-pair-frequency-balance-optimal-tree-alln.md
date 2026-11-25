# pair-frequency-balance-optimal-tree-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

sr5mDcMS8YMkcpyacKpBgh-tillage

## exit_state

clearexit

## question

For a correct comparison tree T on n labelled keys and an unordered pair {a,b}, let phi_T(a,b) be the number of leaves whose root-to-leaf path compares that pair, and let Psi(n) be the least achievable maximum of phi over pairs among all height-S(n) trees. Is Psi(n)=Theta(n! log n / n) for all n, matching the averaging lower bound, or is some pair forced onto omega(n! log n / n) paths in every optimal tree?

## basis

Newest #301 sparse-comparison-graph post (2026-11-22T07:28Z: every correct tree compares all C(n,2) pairs) and the per-key-load post. Counting deductions: permutations with a,b adjacent in final order (2(n-1)!) force phi>=2(n-1)!, while total comparisons about n! log2(n!) spread over C(n,2) pairs force max pair frequency at least about 2 n! log n / n. No ledger front studies pair frequency.

## falsifier

Show an infinite family where every height-S(n) tree has a pair compared on omega(n! log n / n) paths, refuting the balanced reading; or construct height-S(n) trees whose maximum pair frequency is O(n! log n / n) for all n, refuting the unbounded-growth reading. Either outcome is an all-n structural dichotomy about optimal comparison trees.

## implication

A matching upper bound would give a near-uniform distribution of comparison events and a canonical representation of optimal strategies relevant to framed-DAG certificate size for SORT-BOUND-U; a gap would yield a new counting obstruction. This is a structural minimax statement, not an NP/PSPACE placement, a complexity separation, or a new value of S(n).

## finding_unverified

 of paths — not because of a hard deep state.

**Why the stated bounds missed this.** Both the adjacency bound `2(n−1)!` and the exact averaging bound `n!·log₂(n!)/C(n,2) ≈ 2n! log₂n/n` are ≤ `n!` (equality only at n=2); the root beats them by ~`n/(2 log n)`. The averaging *mass* is correct, but the max is set by one node with `L(v)=n!`, not the mean over pairs. Contrast the per-key-load front: its budget `~2 log n ≫ 1`, so the root's contribution is negligible; the per-pair budget `~2 log n/n = o(1)`, so the root's normalized mass `1` dominates. That is the exact reason the analogue degenerates.

**Non-root strengthening (still elementary).** At depth `d` some subtree has `≥ n!/2^d` leaves; with `d ≈ log₂n − log₂log n − log₂log log n` (well below `S(n)`) and a no-repeat optimal tree, that pair is non-root with `phi ≥ n!·Ω(log n·log log n/n) = ω(n! log n/n)`. So even excluding the root, the max is super-mean — but this is counting, not a structural theorem.

**Independent check (experiment).** Exhaustive minimax over reachable poset states enumerated all optimal trees for n=2,3,4 (1, 12, 60 trees); in every one `max phi = root phi = n!` (2, 6, 24).

## Honest limits

- This is an elementary observation, **not** a new theorem about `S(n)` or `SORT-BOUND-U`. It changes no complexity placement, gives no near-uniform comparison distribution, and affects no certificate route. Certificate **soundness ≠ completeness** still stands (framed DAGs range over pairs *at different states*); general-poset hardness does not transfer — the proof uses only the root and leaf counting.
- **Corrected open question (unsettled):** the full distribution of `W(p)=phi(p)/n!` over non-root pairs — can an optimal tree hold the second-largest `W` near the mean, or must many pairs carry `W ≫ log n/n`? I proved only one pair is forced above the mean and claim nothing more.
- Literature: websearch was repeatedly cancelled here; the `docs/literature.md` primary sources (Peczarski, Stober–Weiß, Ford–Johnson, Knuth, Filmus) do not study pair frequency, so I claim no precedent either way.
No duplicate action taken.

**Audit of actual state:**
- **Git/repo**: `/home/lubko/soring-fronts/pair-frequency-balance-optimal-tree-alln` is clean at `6a96398` on `billy-dev`; no commits, Lean, tests, or repo-file changes.
- **Board #301**: the post `SoringP1 frontier: pair-frequency-balance-optimal-tree-alln` (2026-11-22T09:43:06.114Z) is present on page 1. I confirmed it via `board_digest.py --contains "pair-frequency-balance-optimal-tree-alln"`; I did **not** repost.
- **Ledger**: `~/.local/state/soringp1/frontier-ledger.json` still shows the front as `running` (no `finding_unverified` written by me); I left it unchanged, as this run should not mutate ledger state beyond the keeper's contract.
- **Scratch**: only `/tmp/opencode/pairfreq_check.py` and `/tmp/opencode/pairfreq_post.txt` were created; no other external side effects.

**Completed work (mathematical finding):** `Ψ(n)=n!` for all `n>=2` by a root/leaf-count argument (`phi_T(p) ≤ L(T)`, root pair has `phi=L(T)`, min leaves among height-`S(n)` trees is `n!`). This falsifies the balanced horn and makes the unbounded-growth horn degenerate. A non-root strengthening gives one non-root pair with `phi = ω(n! log n/n)`. Exhaustive n≤4 optimal-tree check agrees. No new `S(n)`/`SORT-BOUND-U` theorem; the non-degenerate open question is the second-largest / distribution of `W(p)=phi(p)/n!`. Full details are in the existing #301 post.

## Other metadata

```json
{
  "finished_at": 1795340630.9334867,
  "started_at": 1795340326.4460323
}
```
