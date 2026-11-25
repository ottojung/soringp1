# g-measure-lossless-defect-evaluator

## status

investigated

## origin

ai_proposal_unverified

## agent_id

0RwSsIN26eYxjhFcX0WEvq-kamenski

## exit_state

clearexit

## question

Can the signed ceiling-loss / G measure (the minimum number of forced non-clean steps over minimax-optimal play) be turned into a uniform exact evaluator for the defect D(n) = S(n) - ceil(log2 n!), i.e. is there an algorithm running in 2^{o(n log^2 n)} time that scores each state using only linear-extension counts of children rather than solving the full minimax F at arbitrary states?

## basis

Board #301 posts 16:15Z (ceiling-loss identity and Kraft-clean sufficient lemma), 16:51Z (G recurrence), 18:30Z/18:43Z (converse refuted). Scratch computation found G(A_n)=D(n)=0 for n<=11, G=eps on all 4231 posets at n=5 and at the n=6 witnesses, yet G=1>eps=0 at the board's n=8 witness; all finite and unverified, not a proof.

## falsifier

Show that any G/ceiling-loss recursion must first identify minimax-optimal pairs (hence compute F at each reachable state), or exhibit a state family where the signed loss ledger is strategy-dependent so that no local extension-count scoring determines D(n).

## implication

A positive answer would give the first sub-2^{n log^2 n} exact evaluator for S(n) and SORT-BOUND-U; a negative answer is a barrier ruling out the whole Kraft-clean / ceiling-loss family of faster-evaluation methods.

## finding_unverified

died
`AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, `docs/research-frontier.json`, and board #301's pivotal posts: **16:15Z** (ceiling-loss identity + Kraft-clean sufficient lemma), **16:51Z** (G recurrence, open converse `G(P) ≤ eps(P)`), **18:30Z/18:41Z** (n=8 refutation of that converse), **18:43Z** (Kraft-clean not a tightness-completeness certificate), and **11:39Z** (enumeration blocker for a faster exact evaluator).

### Mathematical finding — barrier for the G/ceiling-loss "extension-count-only scoring" family

**Falsifier prong confirmed:** any G/ceiling-loss recursion must compute full minimax `F` at reachable states to identify minimax-optimal pairs; child extension counts alone cannot do it.

**Reachable n=6 witness** [experiment, verified two ways]:
- State `S` = successor masks `(0,21,0,33,5,0)`, `e=26`, `b=5`, `F=5`, `eps=0`.
- Reached from `A₆` (`e=720, F=10`) via the adversary-only optimal path of comparisons `(0,3),(1,4),(0,4),(2,4),(3,5)` (child F's 9,8,7,6,5; both children tied at each step).
- At `S` two incomparable pairs have **identical child extension-count multisets `{10,16}`** but different optimal status:
  - `(0,5)`: children `(e,F)=(10,4),(16,5)` → `1+Fmax=6 ≠ F(S)` → **suboptimal**;
  - `(1,3)`: children `(e,F)=(16,4),(10,4)` → `1+Fmax=5 = F(S)` → **minimax-optimal**.
- Both pairs are *clean* (threshold `2⁴=16`), so even restricting to clean comparisons, extension counts can't pick the optimal one. Extension count `16` carries `F=5` in one split and `F=4` in the other — `F` is not a function of `e` even at child level. `e` counts cross-checked by subset-DP and brute force over all `6!=720` permutations.

**Deduction:** any scoring `σ` reading only child extension counts assigns the same value to both pairs, so it cannot determine `G`'s admissible pair set at `S`, hence cannot compute `G(S)`. Therefore `G(A_n)` cannot be evaluated by extension-count scoring without solving `F` at reachable states — no `2^{o(n log² n)}` speedup is available *within this family*. The board's W6 witness shows the same ambiguity (`{30,6}` multiset, Fmax 5 vs 6).

### Honest limits
- **Finite n=6 counterexample, not an all‑n theorem.** It refutes the *universal sufficiency* claim (extension counts determine optimal pairs / suffice to score `G`), already false at a reachable state. I do not claim it fails at every reachable state or all n.
- **No time lower bound** for `S(n)`, no class separation, no change to `SORT-BOUND-U` status — exactly the route-specific barrier the falsifier asked for, not a proof that no algorithm exists.
- **A second probe failed and is reported as such:** I looked for an optimal pair where the adversary's max-`F` child disagrees with the larger-`e` child (which would make the ledger term `π` extension-count-invisible). Over all 65,551 optimal-play-reachable n=6 states, **no strict inversion** exists (all inversions were `F`-ties). I do not claim that obstruction.
- The **signed ledger sum is invariant** (`=eps`); what is extension-count-invisible is the *move choice*, not the sum.
- The witness **is reachable from the antichain root**, so it bears on the `G`-recursion for `S(n)` — it is not a general-poset-only artifact (respecting the AGENTS.md transfer caveat).

I did not confuse a successful process with a proof: the deliverable is a concrete reachable counterexample plus a deduction giving a route-specific barrier, with the unproved general statements explicitly flagged.

## Other metadata

```json
{
  "finished_at": 1795202226.4545174,
  "started_at": 1795201708.90265
}
```
