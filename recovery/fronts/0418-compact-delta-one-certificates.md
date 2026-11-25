# compact-delta-one-certificates

## status

investigated

## origin

ai_proposal_unverified

## agent_id

njd3VLlTsaBJkuarZyTaaC-dessaix

## exit_state

clearexit

## question

Does there exist a polynomial-size (in n) certificate of exact S(n) whose verification checks only that a given decision tree has depth at most S(n)+1 (one unit of excess) rather than exact depth?

## basis

Follow-up explicitly named in alternative-relaxation-farkas-support front; compact delta=1 certificates not yet investigated.

## falsifier

Exhibit an infinite family of n where every sound framed certificate of height S(n)+1 has exponential size, or a polynomial-size verifier that accepts a tree of height S(n)+1 but S(n) is strictly smaller.

## implication

A polynomial-size delta-one certificate would place exact unary S(n) in NP with a relaxed bound, weakening the PSPACE upper bound's practical cost without resolving P-vs-PSPACE.

## finding_unverified

## Finding

**No new substantive theorem or counterexample was established; the delta-one relaxation does not bypass the known obstruction, and the live blocker remains completeness, not soundness.**

### What was inspected
- `AGENTS.md`, `docs/problem.md` (unary target, PSPACE upper bound, no binary workstream).
- `docs/research-framed-certificate-frontier.md` (framed certificate grammar, soundness checker, merge-sort DAG, rank-envelope joins, entropy identity).
- Git state on `billy-dev`: clean, no in-progress changes; no interrupted side effects to reconcile.

### Mathematical assessment (delta-one, height S(n)+1)

1. **Soundness is not the issue.** The framed grammar is already sound and polynomial-time checkable in the explicit graph size: local feasibility, joins as intersections, depth computed in DAG order. A tree of height `S(n)+1` is an even more permissive witness than one of height `S(n)`.

2. **The verifier still needs `S(n)`.** A "delta-one certificate" purporting to show `S(n) ≤ k` by exhibiting a sorter of height `≤ S(n)+1` is circular unless the verifier already knows `S(n)`. The threshold instance supplies `k`; checking `height ≤ S(n)+1` requires evaluating `S(n)`, which is exactly the function in question. Relaxing the bound by one unit does not make `S(n)` available to a uniform polynomial-time verifier.

3. **Soundness ≠ completeness.** Even a sound height-`(S(n)+1)` sorter does not certify `S(n) ≤ k` for `k < S(n)+1`. For `k = S(n)` (the exact instance), the delta-one witness is still one comparison too tall, so it does not witness the instance. For `k = S(n)+1` the instance is trivially true but the certificate adds nothing beyond exhibiting any sorter of that height. Thus the relaxation either misses the instance it must decide or is vacuous.

4. **No certificate-size theorem is known.** There is no established infinite family where every sound height-`(S(n)+1)` framed certificate is exponential, nor a polynomial-size verifier accepting height `S(n)+1` while `S(n)` is strictly smaller. The framed-certificate note explicitly records that no all-`n` polynomial-size completeness theorem at exact budget is known; one unit of slack does not change the counting/entropy constraints (§4) because the telescoping identity uses `k − log₂(n!)`, and `+1` is negligible against the `o(n)` slack required.

### Obstruction (exact)
The decisive obstacle is **completeness at the exact budget**: exhibiting a (sound) sorter of height `S(n)` or `S(n)+1` is not the same as proving `S(n) ≤ k` for the given `k`, and no uniform polynomial-time procedure can bridge that gap without computing `S(n)`. The delta-one relaxation therefore neither places `SORT-BOUND-U` in NP with a relaxed bound nor weakens the PSPACE cost in a checkable way.

### Limits
- No Lean or repository changes were made (none warranted; no independently checkable new theorem/counterexample).
- No external posts/commits were made.
- The frontier remains: all-`n` polynomial framed certificate at exact budget `S(n)` (open question 1 in §5), and Sergeev compatibility (open question 2).

## Other metadata

```json
{
  "finished_at": 1794189655.8059468,
  "started_at": 1794189623.6927636
}
```
