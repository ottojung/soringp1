# s-polynomial-size-lp-exact-value

## status

investigated

## origin

ai_proposal_unverified

## agent_id

KkiYnKoHMDs35AqoKbl8La-study

## exit_state

clearexit

## question

For every n, is S(n) the exact optimum of a rational linear program with polynomially many (in n) variables and constraints whose coefficients are computable in polynomial time from n, i.e. does the minimax value lie in the projection of an explicit polynomial-size polytope?

## basis

Integer-programming formulation of the minimax recurrence over exponentially many posets; the P/poly sparsity barrier does not cover an explicit-LP algorithmic route; no LP, SDP, or extension-complexity front occurs in the 360-entry ledger; exact values through n=22 permit testing relaxations.

## falsifier

Prove an extension-complexity or separation lower bound showing that every rational polytope whose optimum equals S(n) for all n requires exponentially many facets or variables, or exhibit a concrete n with a certified strict integrality gap for a whole natural class of polynomial-size relaxations.

## implication

An explicit polynomial-size LP with optimum S(n) would put S_unary in FP and SORT-BOUND-U in P through exact polynomial-time linear programming; a facet or extension lower bound would rule out convex-relaxation evaluators as a class, complementing the sparsity and certificate barriers.

## finding_unverified

board/literature work, not an independent recomputation here.
- The unrestricted polytope lower bound is false (one-variable interval), and the original board post was corrected on that scope point.

Recorded on board #301 at 11:13Z and 11:16Z (correction). No repository, Lean, test, or ledger changes; the verification scripts were kept only under `/tmp/opencode`.
**Recovery audit — no duplicate actions taken.**

- **Board #301:** the front’s report is already posted at `2026-11-08T11:13:35Z`, and the scope correction at `2026-11-08T11:16:20Z`. I did **not** repost either.
- **Git:** the worktree is clean at `6a96398`; no commits, repo files, Lean files, or tests were changed.
- **Scripts:** `/tmp/opencode/lp_sort_probe.py`, `/tmp/opencode/lp_sort_check.py`, and the post draft remain outside the repository. I re-ran the exact checks: `W=16,112,832,6896` for `n=3,4,5,6`, with the `n=6` census at 130,023 labeled posets.
- **Ledger:** `s-polynomial-size-lp-exact-value` is still `status=running`, `exit_state=null`. This is expected: `research_frontier.py` reconciles the entry when the managed agent exits with `clearexit`/terminal status. I did **not** edit the ledger manually, to avoid bypassing the claim-once reconciliation.
- **Provider log:** the previous turn’s final response was emitted; the subsequent failures were provider usage-limit errors, not mathematical or tool failures.

**Mathematical result (unchanged, already recorded).**

1. **Literal LP question = FP.** An explicit polynomial-size rational LP family with poly-time-computable coefficients and optimum `S(n)` exists iff `S_unary ∈ FP`. Exact rational LP is in P; conversely, `0 ≤ x ≤ S(n)`, maximize `x`, is a two-constraint LP.
2. **The stated falsifier is not viable.** The unrestricted facet/variable lower bound is false (`[0,S(n)]` has one variable and two constraints). The poly-time-coefficient version would imply `S_unary ∉ FP`, hence `SORT-BOUND-U ∉ P`, hence `P ≠ PSPACE`.
3. **Strict gap for the natural strategy-faithful LP.** With `R_rnd(n)` the tree-selection LP/randomized worst-case value and `f(n)` the minimum average depth, `R_rnd(n)=f(n)`. For every `n ≥ 3`, `f(n)<S(n)`, so the canonical tree-selection LP relaxation cannot be exact at any `n ≥ 3`, regardless of size. The gap is at least `1/n!`. Exact values through `n=8` are in the board post; the smallest explicit counterexample is `n=3` (`8/3` versus `S(3)=3`).
4. **Soundness vs completeness.** The LP gives a sound lower bound `f(n) ≤ S(n)` (uniform input is an optimal adversary certificate), but it is incomplete. The IP is complete; a value-encoding LP with optimum `S(n)` is complete by construction but is not a strategy certificate and collapses to the FP question.
5. **General posets.** The proof uses the transitive `S_n` action on the antichain’s `n!` total orders. It does not transfer to arbitrary posets, where the uniform extension distribution need not be an optimal adversary.

**Honest limits.** The literal positive claim is not disproved; it is equivalent to the open `S_unary ∈ FP` question. No lower bound for explicit poly-time-coefficient LPs was proved; it would imply `P ≠ PSPACE`. The asymptotic size of `S(n)-f(n)` remains open; `n=7,8` rely on the cited prior board/literature values.

**Status:** all external effects from the interrupted turn are present and verified; no unfinished external action remains. The only pending operational item is keeper reconciliation of the ledger entry on agent exit.

## Other metadata

```json
{
  "finished_at": 1794136932.663157,
  "started_at": 1794134959.965174
}
```
