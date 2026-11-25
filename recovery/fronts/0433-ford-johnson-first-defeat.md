# ford-johnson-first-defeat

## status

investigated

## origin

ai_proposal_unverified

## agent_id

qV98zh8cEwaGegBtza2GRL-corrupt

## exit_state

clearexit

## question

What is the least n0 for which S(n0) < FJ(n0), where FJ(n)=sum_{i=1}^n ceil(log2(3i/4)) is the Ford-Johnson merge-insertion count; is n0=47, or does some n in [23,46] admit a certified comparison sort with fewer than FJ(n) comparisons?

## basis

Ford-Johnson/Knuth FJ formula, exact S(n)=FJ(n) for n<=22 (Peczarski; Stober-Weiss; OEIS A036604), the board-reported Manacher/Peczarski 200-comparison sort at n=47, and the board finding that FJ has positive linear excess while Sergeev's construction has o(n) excess.

## falsifier

Exhibit an explicit n<47 together with a correct adaptive comparison sort using fewer than FJ(n) comparisons, or conversely prove for every 23<=n<=46 that no sorting tree of height FJ(n)-1 exists; the reported 200-comparison construction at n=47 has FJ(47)=201.

## implication

This isolates the first point where the 1959 Ford-Johnson bound is not exact; a certified improvement in [23,46] would lower the first-defeat threshold and give a concrete new upper bound for an open S(n), while proving FJ exact through 46 makes n=47 the first true improvement.

## finding_unverified

(n)`, but no method reaches even that.

The standard efficiency/leaf-count potential cannot exclude height `FJ(n)-1`, because

\[
n! \le 2^{C(n)} \le 2^{FJ(n)-1}.
\]

So the root is not pruned by leaf counting. Any proof of `S(n)=FJ(n)` for the open interval needs a genuinely stronger invariant or an exhaustive decision-tree search. At n=23, the exhaustive search is far beyond this host: Stober–Weiss needed about 89 hours on 24 threads/768 GB for n=18; this host has 4 cores/15 GB, and n=23 at height 75 is much larger.

## Honest limits

- I did **not** prove `n0=47`.
- I did **not** disprove it by finding a better sort below 47.
- I refuted only the stronger epistemic claim that Peczarski’s IPL 2007 result settles the general question; its quantifier is split-and-merge only.
- `n0` is a finite record question. A certified improvement below 47 would be a new exact upper bound for an open `S(n)`, but it would not by itself give a uniform algorithm or a complexity-class separation.
- The 200-comparison witness at 47 is an upper-bound certificate only; it does not establish `S(47)=200`.

The finding, including two corrections, is posted on board #301 under `SoringP1 frontier: ford-johnson-first-defeat`. Host `billy-dev`; worktree clean at `6a96398`; no repository or Lean changes.
## Recovery inspection complete

**Host:** `billy-dev`  
**Repository:** `/home/lubko/soring-fronts/ford-johnson-first-defeat`  
**Git:** clean worktree at `6a96398`; no commits, branches, or repository/Lean changes.

### External effects that actually happened

Exactly three board #301 comments exist under `SoringP1 frontier: ford-johnson-first-defeat`:

1. `2026-11-09T12:08:50Z` — main finding: `n0` is open, `23 <= n0 <= 47`; Peczarski’s theorem is split-and-merge-only; 200-comparison witness at n=47.
2. `2026-11-09T12:09:45Z` — correction: only 5+42 is certified to give 200; the other `L=200` splits were not claimed as certified.
3. `2026-11-09T12:10:23Z` — correction: `delta = FJ - C` is the room above the information bound, not the number of comparisons a defeat must save.

There is exactly one main post and two corrections. **No duplicate main post was made.** The ledger entry remains `status: running`; it is keeper-managed and was not edited.

### Unfinished side work

The two optional independent merge searches from the prior turn were killed by the backend failure:

- `searchfast 4 42 18` — output file contains only the initial `N=163185 h=18` line, no result.
- `searchfast 5 41 21` — output file contains only the initial `N=1370754 h=21` line, no result.

No result was recorded, so I am **not** claiming either computation completed. They were independent cross-checks, not gaps in the mathematical conclusion: Peczarski’s split-and-merge theorem already implies `M(4,42) >= 19` and `M(5,41) >= 22` at n=46. I did not blindly rerun them, to avoid creating another uncertain long-running effect.

### Mathematical conclusion unchanged

- `n0` is **not known to be 47**.
- The proved range is `23 <= n0 <= 47`.
- `n0 = 47` is equivalent to the open statement `S(n)=FJ(n)` for all `23 <= n <= 46`.
- Peczarski’s IPL 2007 result rules out improvements only for split-and-merge algorithms using Ford–Johnson halves, not arbitrary adaptive comparison trees.
- The 200-comparison construction at n=47 is real: `47=5+42`, `FJ(5)=7`, `FJ(42)=171`, merge in 22, total `200 < 201=FJ(47)`.
- No counterexample below 47 was found.

No further post, commit, or external action was made.

## Other metadata

```json
{
  "finished_at": 1794226381.3290188,
  "started_at": 1794222732.8460963
}
```
