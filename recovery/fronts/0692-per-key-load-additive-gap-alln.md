# per-key-load-additive-gap-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ozstbvhkvhsx7OoTGL91Vu-streaming

## exit_state

clearexit

## question

For every n let Lambda(n) be the least achievable worst-case per-key comparison load over all height-S(n) adaptive sorting trees on n labelled keys. Is the additive gap Lambda(n) - ceil(2*S(n)/n) bounded by an absolute constant for all n, given that the newest board #301 reports gaps 0,0,0,1,0,1,1 for n=2..8 and derives only the average-load counting lower bound?

## basis

docs/problem.md model and newest Antonina #301 per-key-load post (2026-11-22T07:42Z): Lambda(2..8)=1,2,3,4,4,5,5 against counting bound ceil(2*S(n)/n). Only the O(log n) asymptotic class was attacked there, not the additive integrality gap; gap values were checked against the board's reported table.

## falsifier

Exhibit an infinite family of n for which every height-S(n) tree forces some key into at least ceil(2*S(n)/n)+f(n) comparisons on a single path with f(n) unbounded, for instance via a per-key adversary/potential argument that beats the average-load counting bound; the reported small-n table alone does not settle the all-n claim.

## implication

If the gap is uniformly bounded, the trivial average-load counting bound becomes an essentially exact, checkable invariant for load-constrained optimal strategies and a branch-and-bound pruning rule when computing S(n); if it is unbounded, no counting-only potential certifies load-optimality, narrowing the route to a compact optimal-tree normal form.

## finding_unverified

,35,2)`, unique incomparable pair `(2,3)`, loads `(1,1)`.
- Losing: `succ=(18,0,59,51,2,18)`, unique incomparable pair `(0,5)`, loads `(0,2)` — the zero-load key cannot be compared.

So `(F, #linear extensions, load multiset)` does not decide load-feasibility: **no counting-only potential can certify load-optimality**, independent of whether the gap is bounded. Mixed-invariant groups proliferate: 35 at n=6, 258 at n=7. This sharpens the front's complexity implication into an unconditional no-go for that invariant family.

### 3. Concrete failed approach — greedy load balancing `[experiment]`

Greedy among optimal comparisons (pick one minimizing the two keys' current max load) **fails at n=8 with cap Λ(8)=5** under all six natural tie-breaks. Explicit stuck state reachable under greedy: `succ=(254,252,136,128,236,204,136,0)`, loads `(2,5,4,4,3,5,5,2)`, `F=1`, `e=2`, unique incomparable pair `(2,6)` with key 6 already at cap; verified `G=False`. Unrestricted greedy uses max load 6 > Λ(8)=5. A winning strategy must be **anticipatory** (reserve capacity on keys needed for forced late comparisons), so no one-step greedy/potential proof works.

### Non-transfer and soundness `[deduction + literature]`

Kahn–Saks balanced pairs (`O(log e(P))` for arbitrary posets) and Hyafil–Rivest/Cardinal et al. give neither exact `S(n)` nor per-key load control; hardness for general posets/tests does not transfer to the fixed antichain root. Even an all-n `O(log n)` load normal form would be a **sound** structural restriction, not a polynomial-size **complete** NP/coNP certificate (`SORT-BOUND-U` trees still have exponentially many nodes); NP membership and the sparsity/Mahaney barrier are unchanged.

### Honest limits

- Neither the bounded-gap claim nor the unbounded-gap falsifier was proved; I found no potential beating counting.
- The n≤8 gaps `0,0,0,1,0,1,1` cannot settle all n. The n=9 search computed `S(9)=19` and all 183231 unlabelled 9-posets but the load-game search was incomplete; I stopped it rather than leave a runaway process, so **Λ(9) is not a result**.
- The decisive obstacle is unchanged: an all-n anticipatory load-balancing lemma. No new `S(n)`/`SORT-BOUND-U` theorem.

Verification artifacts are in `/tmp/opencode/` (`load_solver.py` reproduces Λ(2..8) exactly; `potential_witness.py`, `extract_witness.py`, `load_greedy*.py`). Worktree clean at `6a96398` on `billy-dev`.
## Recovery check (no actions repeated)

Inspected git state, processes, and board #301. The previous turn’s effects already happened; I did **not** repost/commit/mutate anything.

- **Git**: `billy-dev` @ `6a96398`, working tree clean; no commits made by this front.
- **External post**: already present on Antonina #301 — `[2026-11-22T09:57:30.902Z] SoringP1 frontier: per-key-load-additive-gap-alln` (confirmed via board digest). Not duplicated.
- **Processes**: no `load_solver.py 9` running; I had stopped the incomplete n=9 run.
- **Artifacts**: scratch-only in `/tmp/opencode` (`load_solver.py`, `load_greedy*.py`, `potential_witness.py`, `extract_witness.py`, etc.).

**Completed finding (as reported):** additive-gap reframing does not bypass the anticipatory load-balancing obstacle; exact counting-invariant no-go (same `F,e,load` multiset, opposite `G` at n=6; 35/258 mixed groups at n=6/7); greedy load-balancing fails robustly at n=8, cap Λ(8)=5. Neither bounded-gap nor unbounded-gap horn proved; Λ(9) not computed. No new `S(n)`/`SORT-BOUND-U` theorem, no repo/Lean changes.

## Other metadata

```json
{
  "finished_at": 1795341497.0899827,
  "started_at": 1795340325.9593515
}
```
