# antonina-njd3VLlTsaBJkuarZyTaaC-dessaix

Session: ses_e41f6fd65ffeHxD0nJXNcHOKwW
Workspace: /home/lubko/soring-fronts/compact-delta-one-certificates
Created: 1794189624022; updated: 1794189646391

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 53 (msg_1be092275001XX9f4Srfh18Re7)

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
