# greedy-e-index-exception-density-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

g4yI4FMn1gRuJ6JqlNp7wP-dresses

## exit_state

clearexit

## question

For every n, does there exist a poly(n)-size index (for example a table keyed by the linear-extension count e(P) together with a poly-size exception list) that returns the exact greedy max-linear-extension adversarial-tie game value V(P) for every poset state P reachable from the n-antichain within G(n) comparisons, or must every correct such index have superpolynomial size for infinitely many n?

## basis

2026-11-20 #301 post greedy-ball-compact-index-alln reported V(P) determined by e(P) on the greedy ball except at 8 of 62 e-values at n=6 and explicitly left its positive horn open; matching-gadget extension ties collapse to m+1 isomorphism classes; non-twin extension ties with differing V exist (1336/90655 transitions at n=6). This front attacks the open positive horn, not the refuted negative horn, and is distinct from general-poset e-invariant results.

## falsifier

Exhibit an infinite family of n for which the set of reachable greedy states whose value is not determined by e(P) within any poly-size exception budget has size omega(poly(n)), forcing any correct e-indexed evaluator to have superpolynomially many entries; or produce an all-n poly-size correct e-index.

## implication

A correct poly-size e-index would yield a subexponential-time evaluator for the greedy value G(n), recursing only on exceptional states, and if G(n)=S(n) then a genuinely improved uniform bound for exact S(n), the active shrink-the-exponent frontier for SORT-BOUND-U; a superpolynomial lower bound would close the compact-index route as a barrier.

## finding_unverified

 for n = 6,7,8,10,12.
3. **Injectivity.** For q = max(S∪T), the q-adic valuation of ∏_{p∈S}p! is 1 iff q ∈ S. So distinct prime sets give distinct e-values (0 collisions in 4096 subsets).

Counting: the t smallest primes sum to ≤ t²(log t + log log t), so t = Θ(√(n/log n)) and all 2^t subsets qualify. Measured prime-subset counts: 4687 (n=100), 159061 (n=200), 1.38·10⁸ (n=500) — superpolynomial.

Verified computationally: all chain-union posets are in the all-ties ball for n ≤ 6; ball e-values equal all-poset e-values (1,2,4,9,23,62 for n = 1..6; 226 and 955 at n = 7,8 over isomorphism classes).

## Falsification attempts I actually ran
- An apparent counterexample to reachability was a **bug** (non-transitively-closed targets); with transitive closure all chain-union states are reachable.
- Searched for colliding prime products (none found); tried to make the growth merely polynomial (log(count)/log(n) increases: 1.84 → 2.26 → 3.02).
- Confirmed the prior matching-gadget route is unusable and not needed here.

## Honest limits
- This kills the **tabular e-index** (one entry per e-key) — the example form in the front. It does **not** rule out a closed-form evaluator plus a sparse exception list; that needs an exception-density theorem, which is the remaining decisive obstacle. Mixed e-values are only measured (0,0,0,1,8 for n = 2..6); the n=7 exception computation did not finish.
- V ∈ {⌈log₂ e⌉, ⌈log₂ e⌉+1} is verified only for n ≤ 6; no all-n claim. No G(n)=S(n) claim, no SORT-BOUND-U separation, no general-poset hardness, no Lean changes.

## Delivery
Posted to Antonina issue #301 at 05:59:03Z. Worktree on `billy-dev` is clean — no repository, Lean, or ledger changes.
**Recovery check (no repeated side effects):**
- **Conversation / prior work:** I completed the `greedy-e-index-exception-density-alln` investigation in the previous turn (scratch computations under `/tmp/opencode`, including background runs now stopped) and reported results.
- **Git state:** `/home/lubko/soring-fronts/greedy-e-index-exception-density-alln` is clean on `billy-dev...origin/billy-dev`, HEAD `6a96398` (no new commits, no staged/unstaged changes).
- **Durable external record:** Antonina board #301 already contains the post by `SoringP1 frontier: greedy-e-index-exception-density-alln` at **2026-11-20T05:59:03.442Z** (verified via `board_digest.py --contains "greedy-e-index-exception-density-alln"` on page 1). No duplicate post was made.
- **Other external actions:** none performed (no pushes/PRs, no Lean/repo changes, no purchases, no ledger/main edits).

**Conclusion:** All intended effects already happened; there is no unfinished external work to continue. I did not and will not re-post, commit, or repeat any external action.

**Result already delivered (summary):** Disproved the **tabular e-index** positive horn (all-n). For n ≥ 8, disjoint unions of chains of prime lengths plus an antichain pad are greedy-ball reachable within G(n) with `e(P_S)=n!/∏_{p∈S} p!`, pairwise distinct by a largest-prime valuation argument, yielding `≥ 2^{Ω(√(n/log n))}` distinct e-values — superpolynomial, so a table keyed by e(P) cannot be poly-size. This does **not** rule out a closed-form evaluator with a sparse exception list (decisive remaining obstacle); mixed/exception counts only measured for small n, no `G(n)=S(n)`/class-separation/Lean claim. Uncertainty: the interrupted n=7 exception-count run produced no durable mixed-count data, but it had no external side effects.

## Other metadata

```json
{
  "finished_at": 1795154432.6076999,
  "started_at": 1795153048.106751
}
```
