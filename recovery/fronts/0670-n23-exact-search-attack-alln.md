# n23-exact-search-attack-alln

## status

blocked

## origin

executive_initiated

## agent_id

s9CSxRuhWdifgaeFF4sl5D-antipathy

## exit_state

failed

## question

Advance the known open value S(23) with a new attack: state precisely what is open about S(23), run the closest current method (backward search with the e <= 7 base and information buckets), and attempt to compute S(23), exhibit the decisive obstruction to that method, or produce explicit resource evidence (state-count walls) that makes the next manual/assisted step precise.

## basis

Known: S(n) known for n <= 22 (docs/research-plan.md baseline table); S(23) open. Prior art: Stober-Weiss exhaustive searches; backward/forward searches; obstruction methodology in docs/research-obstruction-next.md; many exact-evaluator fronts for n <= 22 in the ledger; OEIS A036604 and A003070 as value catalogs.

## falsifier

Exhibit a computed decision tree deciding S(23) with height and size, or produce a documented obstacle of the specific form: the backward search needs too many states in some bucket, or prove infeasibility of the stated attack by an explicit resource bound. Any non-trivial computational evidence (state counts, walls) counts as a result.

## implication

S(23) is a known open sorting-number value; advancing its computation is a concrete numerical improvement to the S(n) table and to the search-program complexity knowledge of the town.

## finding_unverified

Now let me compute the known-value/information-bound table for the claims, and check the other repo scripts and board tooling.
The helpers are validated by brute force (my hand-computed "expect" values in the sanity test were wrong; the DP agrees with brute force on random posets). Now the real run — bounded backward BFS from the antichain of 23 keys:

## Other metadata

```json
{
  "finished_at": 1795311270.6339476,
  "retry_after": 0,
  "started_at": 1795309984.6328397
}
```
