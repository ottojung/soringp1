# defect-coordinatewise-monotonicity-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

xanJnNCcumhBPhsNVhvmP5-fathers

## exit_state

clearexit

## question

For all a,b >= 1 with a+b >= 3, let Z_b be the staircase poset (i<j iff j>=i+2) and A_a the a-antichain, and let delta(a,b) = F(Z_b disjoint-union A_a) - F(Z_b) - S(a). Is delta coordinatewise nondecreasing, i.e. delta(a,b+1) >= delta(a,b) and delta(a+1,b) >= delta(a,b) for every a,b, or is there an all-n family with a downward step in either coordinate?

## basis

Board #301 2026-11-21 09:01Z and 09:13Z posts and the freshly dispatched defect-a12 follow-up concern eventual values, not monotonicity. An independent from-scratch transitive-closure minimax with subset-DP extension counts reproduced delta(1,b)=2,2,2,2,2,3,3 for b=2..8 and delta(2,b)=3,3,4,4,5 for b=2..6 and found no dip in either coordinate through a<=3,b<=8 and a<=5,b<=2; this is finite evidence only, with no all-n conclusion.

## falsifier

Exhibit by independent exact minimax a pair (a,b) with delta(a,b+1) < delta(a,b) or delta(a+1,b) < delta(a,b), computing A_a, Z_b and their union from scratch rather than reusing board tables.

## implication

Together with the merge-insertion bound delta(a,b) <= sum_{i=1..a} ceil(log2(b+i)), coordinatewise monotonicity would turn the finite board delta tables into a disciplined nondecreasing growth law that rules out oscillatory closed forms for the superadditivity recursion S(a+b) >= S(a)+S(b)+min(a,b)+1; it is structural and does not by itself separate P, NP or PSPACE for SORT-BOUND-U.

## finding_unverified

ng.)

### Honest limits
Monotonicity for all `n` remains **open in both coordinates** — empirically supported, not proved. It is a structural growth law bearing on `S(a+b) ≥ S(a)+S(b)+min(a,b)+1`; it would not separate P/NP/PSPACE for `SORT-BOUND-U` (a tally, PSPACE language). I did not confuse the defect‑inequality/merge‑insertion certificates (soundness bounds) with an evaluation algorithm or completeness.

Reported as a single #301 comment (10:11Z); worktree clean on `billy-dev`, no repository, Lean, test, CI, or ledger changes.
Understood. I will not repeat any writes. Let me do a purely read‑only inspection of what actually happened — Git state, the board record, and the scratch artifacts.
Read‑only checks show the previous turn completed cleanly: working tree clean on `billy-dev` at the original clone HEAD (no commits), exactly one board post by my author tag at `10:11:20Z`, and all scratch artifacts intact. A Viche referee post at `10:15Z` already dispositioned that result. Let me read that referee post in full (read‑only) to confirm it raises nothing requiring a correction from me.
## Inspection complete — all prior effects confirmed, no unfinished work

I performed only read‑only checks. Here is what actually happened:

| Effect | Status | Evidence |
|---|---|---|
| Board #301 comment | **Happened exactly once** | `SoringP1 researcher: defect-coordinatewise-monotonicity-alln` post at `2026-11-21T10:11:20Z`; no duplicate by that author. A Viche Executive post at `10:15Z` is a *referee disposition* of it, not another post of mine. |
| Git / repository changes | **None** | Working tree clean; branch `billy-dev`; HEAD still the original clone `6a96398…`; reflog shows only `clone: from /home/lubko/soring301` — no commits. |
| Scratch artifacts | **Intact** | All files in `/tmp/opencode/mono_front/` (evaluator, cross‑check, reports, `post_result.json`). Nothing was written into the repository. |

The research task itself was delivered in full last turn and then independently refereed by Viche at `10:15Z`, who reproduced all five cross‑method anchors (`F(U_{2,4})=8`, `F(U_{3,3})=9`, `F(U_{3,4})=11`, `F(U_{1,6})=8`, `F(U_{4,2})=10`), confirmed the failed general‑poset lemma and the a‑coordinate obstruction algebra, and judged the result an honest negative/structural finding. So there is **no unfinished work to continue**.

### One caveat for review (I concur with the referee; no action taken)
Viche flagged a *non‑load‑bearing* flaw in one line of my board post: I wrote `2^{S(n+1)} ≥ (n+1)! > 2·2^{S(n)}` as a proof that `S` is strictly increasing. The first inequality is fine (leaf count), but the second implicitly assumes `S(n) < log₂(n!) + 1`, which is false in general — `S(n) ≥ ceil(log₂ n!)` can be strictly larger (e.g. `S(12)=30 > 29`), so the gap is not bounded by 1. **The conclusion is unaffected**: `S` strictly increasing follows instead from the simple adversary argument Viche supplied (sorting `n+1` keys needs ≥ `S(n)` uninformative comparisons among the first `n` plus ≥ 1 comparison to place the extra key). My finite tables and the main finding do not depend on that inequality.

I did **not** post any correction or duplicate any write: Viche already recorded the correction publicly, the conclusion stands, and an extra comment would be redundant external action. If you specifically want a one‑line acknowledgment appended to #301, say so and I will make exactly one such post — otherwise I am treating the prior turn as complete.

## Other metadata

```json
{
  "finished_at": 1795256462.7784948,
  "started_at": 1795254080.7555032
}
```
