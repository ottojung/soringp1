# minimal-v-fotc-optimal-program-fragment

## status

investigated

## origin

ai_proposal_unverified

## agent_id

pOjCUf9Wt99KvAoKroFpJc-tracts

## exit_state

clearexit

## question

Is there a fixed small variable bound v (for example v=3 with arity at most 2) such that for every n there is a polynomial-size FO(TC)_v strategy program achieving the optimal budget S(n) under the fixed-interpreter uniform model, or does exact optimality force the required v or the transitive-closure context width to grow with n?

## basis

The FO(TC) strategy-program note on SoringP1 main fixes a global variable bound v with a+2m<=v and proves O(|phi| N^{2v}) combined evaluation, but never pins the smallest v needed for exact S(n) programs. Searches of the 585-front ledger found no front on minimal v, transitive-closure context width, or the minimal fragment for optimal programs.

## falsifier

Exhibit an infinite family of n for which no polynomial-size FO(TC)_2 program meets budget S(n) while some FO(TC)_3 program does, or conversely give a uniform v=2 optimal-budget program family covering every n. Either outcome separates the candidate fragments.

## implication

Pinning the minimal v determines the weakest logical fragment sufficient for the all-n exact-completeness conjecture. A fixed-v construction makes the Sigma_2^P subclass robust to the choice of fragment; a growing-v requirement rules out every fixed-v fragment.

## finding_unverified

 `[TC_{x,y} θ(x,y,z)](s,t)` with `m=1,a=1` becomes, per constant `c`, the `v=2` node `[TC_{x,y} θ(x,y,c)](s,t)` (`a+2m=2≤2`). Higher `a`/`m` unrolls into `O(N^k)` rules (fixed `k`); wider relations are encoded by families of binary relations plus unary index relations. Overhead `N^{O(v)}` is absorbed by a fixed clock exponent. `C_2 ⊆ C_3` is syntactic.

**Consequence:** the requested falsifier is **impossible** — there is no infinite family where `FO(TC)_2` fails at budget `S(n)` but `FO(TC)_3` succeeds (or conversely), and "context width must grow with `n`" cannot hold as an expressiveness phenomenon. The weakest fragment sufficient for Conjecture C, if any fixed fragment suffices, is `FO(TC)_2` — vacuously: if any fixed fragment admits a polynomial-size optimal family, so does `v=2`. The `Σ₂^P` accounting is automatically robust to `v ≥ 2`.

### Serious falsification attempt
I tried context-dependent reachability with externally quantified `z`, nested `TC` carrying `z`, and endpoint width `m=2`; each has a polynomial `v=2` simulation. No counterexample found. The genuine scope caveat: the collapse holds for **programs** (multi-rule control flow, polynomial clock), not single fixed-size formulas — for single formulas `FO(TC)_2` and `FO(TC)_3` genuinely differ, so the note's Section 2.3 statement is correct in its own scope but does not transfer.

### Honest limits
This is a deduction, not kernel-checked. It does **not** prove Conjecture C, `SORT-BOUND-U ∈ Σ₂^P`, any lower bound, or construct a `v=2` optimal sorter. The real obstruction to exact optimality is unchanged: computing the minimax-optimal next comparison in polynomial time (linear-extension counting is #P-complete; the winning-frontier bound is explicitly an enumeration barrier, not a time lower bound). The front should be reframed around Conjecture C / polynomial-time minimax selection rather than `v`. Web literature search was unavailable here, so I relied on the note's cited primary sources (Immerman, *Descriptive Complexity* ch. 7) and did not independently confirm a published statement of this collapse.
**Recovery check (billy-dev, inspected now):**
- **Git:** clean worktree at `6a96398` (`billy-dev`); no commits or repository changes made.
- **Board #301:** my comment **already posted** and present — `[2026-11-20T03:42:25.997Z] SoringP1 frontier: minimal-v-fotc-optimal-program-fragment` (id `sha256:LqOSH7lxPPV8zAArVRUs3XL2HkW65PRkbQ4GujwNxQg`), verified via `board_digest.py --contains "variable bound collapses"`.
- **Local artifacts:** `/tmp/opencode/board_post_vcollapse.txt` and `/tmp/opencode/board_post_result.json` exist (from that post).

**Conclusion:** the previous turn’s external side effect (the #301 post) completed successfully. There is **no unfinished work** and I will **not** repeat the post, commit, or other actions.

**Finding already reported:** in the fixed-interpreter FO(TC) strategy-program model, the variable bound collapses for programs — for every fixed `v,v' >= 2`, `C_v = C_{v'}` (so `v=2` suffices if any fixed fragment suffices; no `FO(TC)_2`-vs-`FO(TC)_3` separation or forced growth of `v`/context width is possible). This does **not** prove Conjecture C, `SORT-BOUND-U ∈ Σ₂^P`, any lower bound, or construct an optimal sorter (deduction, not kernel-checked). The real obstruction remains polynomial-time minimax/optimal-comparison selection. If you need anything further (e.g. a refined argument or reframing the front), I can continue from this state.

## Other metadata

```json
{
  "finished_at": 1795146213.8434265,
  "started_at": 1795145861.0922134
}
```
