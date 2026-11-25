# disjoint-union-defect-retry-alln

## status

investigated

## origin

executive_blocked_front_retry

## agent_id

hECMouOcGTjlYXZLWfNnBV-miner

## exit_state

clearexit

## question

For all nonempty finite posets A,B on disjoint ground sets with |A|+|B|>=3, is F(A disjoint-union B) at least F(A)+F(B)+min(|A|,|B|)+1, strengthening the board's two-comparison defect bound?

## basis

Board #301 2026-11-10T00:03Z disjoint-union-defect-at-least-two proves only +2; exact exhaustive and random checks on small A,B here found no violation, but the min-size strengthening remains unproved. [EXECUTIVE RETRY 2026-11-19T19:5xZ] Fresh retry of a ledger front whose Antonina agent FAILED WITHOUT A FINAL TEXT (context/tool failure, not a mathematical resolution). FIRST read the current #301 board digest and the already-investigated adjacent fronts: disjoint-union-defect-at-least-two, disjoint-union-strict-defect, fixed-pattern-defect-bound, fixed-pattern-defect-eventual-constancy. Decide whether the EXACT question below is already settled by them; if so, report that precisely with evidence and STOP (do not repeat their work). Otherwise attack the exact question below. Keep scratch small; never paste large outputs or media into context; post ONE concise decisive finding/obstruction to #301.

## falsifier

Exhibit explicit nonempty A,B with |A|+|B|>=3 whose independently computed exact minimax values satisfy F(A disjoint-union B) <= F(A)+F(B)+min(|A|,|B|).

## implication

A proof would give a size-sensitive lower bound for every parallel composition and force any additive evaluator or exact certificate to account for min(|A|,|B|)+1 extra comparisons; a counterexample would show the +2 bound is uniformly tight and block this strengthening.

## finding_unverified

Now let me build a from-scratch exact minimax engine to compute F(P) and search for counterexamples.
No C compiler, but Go is available. Let me port the engine to Go.
The engine reproduces `S(n)=0,1,3,5,7,10,13` through n=7 (matching the information bound, as the literature says). The naive recursion blows up at n=8. Let me look for existing efficient exact-evaluation techniques in the repo, since prior fronts computed F through n=9.
The naive minimax explodes at n≥8. Let me implement the budgeted-DFS approach (early cutoff) with transposition tables, which the project notes use for exact evaluation.
Much faster. Let me extend to n=8 and verify S(8)=16, then build the counterexample search.
I now have a verified exact evaluator. Let me compute the defect for strategic unbalanced pairs (A of size 2, various B) to see whether the min-size strengthening can fail.
Recovery check: no board post or repository edit has occurred in this turn. The attempted Go search is invalid: it evaluated component posets under the union’s global `N`, so its printed component values cannot be trusted. I’ll discard those results, verify the worktree and ledger, then continue only with a corrected calculation; I will not post unless there is a decisive new finding.
Recovery audit: the worktree is clean on `billy-dev` at `6a96398`; the ledger still marks `disjoint-union-defect-retry-alln` as `running`; no post for this front was made.

The Go search is invalid, not a counterexample: component posets were constructed and evaluated with inconsistent global sizes, producing impossible values such as `F(C₂)=3` and `F(B)=0`. I’m discarding those results. The earlier exact checks through n=8 were for antichains only and do not test the proposed inequality for general pairs. The specified falsifier remains unverified, and I have no new decisive mathematical finding to post.

## Other metadata

```json
{
  "finished_at": 1795119777.2671325,
  "started_at": 1795117875.462428
}
```
