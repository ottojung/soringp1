# antichain-superadditivity-minplusone-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

jRZ2Or27XrdCLX2UXmUJTc-glaring

## exit_state

clearexit

## question

For every a,b >= 1 with a+b >= 3, must the exact sorting number satisfy S(a+b) >= S(a)+S(b)+min(a,b)+1, the antichain-only case of the disjoint-union defect inequality, which is the sole case needed for superadditivity lower bounds on S(n)?

## basis

Newest #301 (16:07Z) closed all scalar-potential proofs of general D; theorem [T] covers only inside-component optimal roots, while A_a u A_b has exclusively cross roots; published exact values through n=22 satisfy the bound.

## falsifier

Exhibit a certified pair (a,b) with S(a+b) < S(a)+S(b)+min(a,b)+1 (a finite counterexample refutes the all-n claim), or establish an unconditional all-n proof that no such pair exists.

## implication

A proof supplies a uniform polynomial-time superadditivity lower bound on S(n) and settles the S(n)-relevant core of the board's open defect inequality; a counterexample refutes the general defect inequality as well.

## finding_unverified

hin a factor of ~100. Script: `/tmp/opencode/antichain_defect_check.py`.

### Exact obstruction to the all‑\(n\) claim

- The sufficient condition provably **fails first at \((a,b)=(1,50)\)**: \(C(51)=220 < U(1)+U(50)+2=221\). Then it fails at every \((1,b)\), \(b\ge50\), and first at \((2,104),(3,196),(4,211),(5,250),(6,398)\). So the residual open region is *extremely unbalanced* splits; any proof there needs a lower bound on \(S(a+b)\) strictly stronger than leaf counting — the information bound plus the best general upper bound known (Ford–Johnson) cannot reach it.
- Necessary-but-insufficient fact re-derived: fixing internal orders, only cross comparisons distinguish the \(\binom{a+b}{a}\) interleavings, forcing \(\ge\lceil\log_2\binom{a+b}{a}\rceil\ge\min+1\) cross comparisons on some path. This cannot be added to \(S(a)+S(b)\): a cross comparison plus an existing relation creates new within-group relations by transitivity (blue \(x<\) red \(y<\) blue \(z\Rightarrow x<z\)), so cross comparisons sort inside groups "for free." This is the same transitivity coupling that closed the general-\(D\) potential routes.

### Honest limits

The all‑\(n\) claim is **neither proved nor refuted**. The \(n\le50\) result is finite-range and uses no new algorithm; it yields **no new uniform complexity result** for evaluating \(S(n)\) and no class membership for `SORT-BOUND-U`. No general-poset hardness or certificate soundness was conflated with completeness. No Lean/repository/CI/main/ledger changes were made; worktree remains clean.

A concise finding was posted to board **#301** at 16:42:03Z (verified), with `--json` redirected to a file as required. `S(n)`, `SORT-BOUND-U` and general \(D\) remain open.
**Recovery inspection (no repeated side effects).**

- **Git/worktree:** `/home/lubko/soring-fronts/antichain-superadditivity-minplusone-alln` is clean on `billy-dev` at `6a96398`. No commits, PRs, Lean/repo changes, or ledger/main changes.
- **External side effect already performed:** board #301 comment exists and was verified: `[2026-11-21T16:42:03.436Z] SoringP1 researcher: exec-antichain-defect-infofj-20261121`. I did **not** repost it. Post stderr was empty; JSON output was redirected to `/tmp/opencode/antichain_defect_post.json`.
- **Durable/scratch artifacts present:** `/tmp/opencode/antichain_defect_finding.txt`, `/tmp/opencode/antichain_defect_check.py`, `/tmp/opencode/antichain_defect_post.{json,err}`. The check script runs and reproduces the finite-range result and first failure.

**Already-completed work (not repeated):** attacked the antichain-only defect front \(S(a+b)\ge S(a)+S(b)+\min(a,b)+1\), \(a+b\ge3\). No counterexample found in certified ranges. Proved the claim for all splits with \(3\le a+b\le 50\) by exact-integer check using published bounds \(C(n)=\lceil\log_2 n!\rceil\le S(n)\le U(n)\) (exact \(S\) for \(n\le22\), Ford–Johnson \(F\) otherwise). Identified the precise obstruction: the cheap info+FJ sufficient condition fails first at \((1,50)\) (\(C(51)=220 < 221\)) and on extremely unbalanced splits; a cross-comparison count \(\ge\lceil\log_2\binom{a+b}{a}\rceil\ge\min+1\) is necessary but cannot be added to \(S(a)+S(b)\) because cross comparisons create within-group relations by transitivity.

**Unfinished/open:** the all-\(n\) antichain defect inequality remains **unproved and unrefuted**. No new uniform complexity result for \(S(n)\)/`SORT-BOUND-U` was obtained; no further external action is pending from this turn.

## Other metadata

```json
{
  "finished_at": 1795279394.6455622,
  "started_at": 1795278209.7962112
}
```
