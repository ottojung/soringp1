# Executive independent verification — two cleared SoringP1 fronts — 2026-11-20 ~06:0xZ

**Author:** Executive (fresh session, handover from `pMiFTvWNbvityuOwdsOr8Y-hardship`)
**Class:** independent verification / audit disposition — **not** a theorem claim,
**not** mission closure, **not** an Act 22 order, **not** a legislative act.
**Scope:** independently check the two freshly posted, now-clearexit SoringP1 front
results; record live Town/SoringP1 state; do not repeat completed work.

## Why these were verified

Since my predecessor's last pass (whose newest #301 write was the 05:47:48Z
commissioning-QA note), two newly commissioned fronts posted results and then
clearexit: `minimax-witness-family-size-alln` at `2026-11-20T05:56:36Z` and
`greedy-e-index-exception-density-alln` at `2026-11-20T05:59:03Z`. No prior
independent verification existed for either. The frontier status is
`fronts_claimed_or_ready_not_verified`, so the mandated action this pass is to
independently check claimed results, not to dispatch more fronts. The standing
Founder directive requires independent checking of claims before reliance.

## Claim 1 under review — `greedy-e-index-exception-density-alln`

THEOREM (as claimed): for all `n >= 9`, the greedy ball `B_{G(n)}(n)` contains
states with `e(P) = n!/prod_{p in S} p!` for every set `S` of distinct primes with
prime-sum `<= n`; these e-values are pairwise distinct, so the ball has at least
`2^{Omega(sqrt(n/log n))}` distinct linear-extension counts. Hence any evaluator
indexed by `e(P)` needs superpolynomially many entries for infinitely many `n`:
the TABULAR e-index form of the positive horn is FALSE.

### Independent checks performed (own scratch, not the reporter's scripts)

- **L2 exact e-value.** For the disjoint union of prime chains plus `r` free
  elements, `e = multinomial(n; p_1..p_k,r) * prod(1) * r! =
  n!/prod p!` (the `r!` of the antichain cancels the padding). Recomputed from
  the multinomial definition and compared to the closed form for every
  admissible prime subset at `n = 6,7,8,10,12,20,40`: all MATCH.
- **L3 injectivity (largest-prime valuation).** If `q = max(S union T)` and
  `q in S \ T`, then `v_q(prod_{p in S} p!) = 1` while `v_q(prod_{p in T} p!) = 0`,
  since only `q!` among factors `p! <= q!` contains the prime `q`. Exhaustive
  check of all admissible prime subsets at `n = 10,30,50,100`: 0 collisions in
  `prod p!`. The valuation argument is a correct all-n proof.
- **L1 reachability.** Build each chain as a STAR: comparing a center with a free
  element, the "new element above center" child has strictly more linear
  extensions, so the greedy adversary keeps it; then order the (twin) tops,
  which are e-ties, so either orientation is a greedy child. Total `<= 2n`
  comparisons and `2n <= ceil(log2 n!) <= G(n)` for `n >= 9`. Proof sound by
  inspection; the front's BFS confirmed all chain-union posets are in the ball
  for `n <= 6` and the front explicitly corrected its earlier non-transitively-
  closed BUG.
- **Counting.** Independent DP over prime subsets with sum `<= n` reproduced the
  front's numbers exactly: `11 (n=10), 89 (n=30), 4687 (n=100), 159061 (n=200),
  137973786 (n=500)`, with `log(count)/log(n)` growing `1.84, 2.26, 3.02, 3.78`
  at `n = 100,200,500,1000` — superpolynomial, consistent with
  `2^{Omega(sqrt(n/log n))}` from `q_i = O(i log i)`.

Scratch artifacts: `/tmp/opencode` inline Python (own sieve + DP; no reporter code).
SoringP1 main `/home/lubko/soring301` and this office worktree were not modified.

### Disposition — Claim 1

**Accepted** as a correct all-n barrier in the TABULAR e-index form, with the
front's own caveats preserved and concurred:

- kills the one-entry-per-e-key table; does **not** rule out a poly-size
  closed-form evaluator `V(e)` plus sparse exception list — the remaining
  decisive obstacle, which the front explicitly leaves open;
- mixed-e-value / exception density is measured only for `n <= 6`, not bounded
  all-n; `ceil(log2 e) <= V <= ceil(log2 e)+1` is experimental for `n <= 6`;
- no `G(n)=S(n)` claim, no `SORT-BOUND-U` class separation, no Lean artifact.

## Claim 2 under review — `minimax-witness-family-size-alln`

FRONT: is the witness number `tau(n) = min{|H| : h(H) = S(n)}` subexponential
or `2^{Omega(n log n)}`? The front reports neither horn proved, but three pieces
of defensible content plus an honest failed approach.

### Independent checks performed

- **Comb lower bound.** `h(H) <= |H|-1` for `|H| >= 2` (pick `pi != pi'` differing
  at some pair, compare it, recurse on the larger side): sound deduction, gives
  `tau(n) >= S(n)+1 = Omega(n log n)`. Tight for comb families (defect `Theta(n)`).
- **Hitting-set reformulation.** If `h(H)=S(n)` then `H` meets `D(T)` for every
  optimal tree `T`, giving the one-sided bound `tau(n) >=` min hitting-set size.
  The converse needs an extension lemma the front could NOT establish; it is
  correctly reported as one-sided, not an equality.
- **Reduction to defect bound.** `h(H) <= log2|H| + D(n)` gives
  `|H| >= 2^{S(n)-D(n)}`; so `D(n)=O(n)` would refute the positive horn. The
  whole question is reduced to a single well-defined falsifiable statement.
  Clean and correct.
- **Empirical** `tau(3)=5, tau(4)=12, tau(5)<=49` (ratios consistent with
  `n!/2^{Theta(n)}`). I did NOT re-run the expensive minimax search; these small-n
  values are accepted as reported, with that limitation stated.

### Disposition — Claim 2

**Accepted** as a reformulation + precise obstruction, not a solution. The failed
per-step balanced-split/potential approach (refuted by comb families) and the
missing extension lemma are honest and useful. `S(n)` / `SORT-BOUND-U` open.

## Overall disposition

Both claims are valid negative/reformulation progress, not theorem completion.
The decisive remaining obstacles are now sharply identified: (1) prove or refute
`D(n)=O(n)` (defect bound); (2) bound the exception density for the closed-form
`V(e)` route. Research frontier remains open; S(23) stays [75,76]. No dispatch
this pass: frontier status is `fronts_claimed_or_ready_not_verified` and both just-
finished fronts are the claimed results being checked; dispatching a near-duplicate
would violate the no-filler rule.

## Live state observed this pass (read-only)

- Antonina `agent list --running`: `unreadable=[]`; 4 running — this Executive,
  one integrator reviewer (`delivery/ikca-ballot-candidate-v4-20261120`), the
  institutional innovator (`c1a00009`), and at query time the now-clearexit
  `greedy-e-index-exception-density-alln` (finished `~06:00Z`).
- Both SoringP1 front agents (`minimax-witness-family-size-alln`,
  `greedy-e-index-exception-density-alln`) are `clearexit`; no SoringP1 front is
  currently running.
- `integrator.py office executive`: no pending items; all four prior executive
  deliveries landed on main (latest `exec-curator-commissioning-qa` as `48671fa`).
- `obligation-expiry.py report`: no live handoffs/mailbox/receipts (expired 3/104/12).
- Institutional cases: `executive_unhealthy:1795150900` open, signal clear 14/20
  observations (auto-closing) — no manual action.
- Founder directive authored exactly `Vitalik` at `2026-11-20T05:17:49Z`
  (knowledge-institutions expansion) was already Clerk-acknowledged (05:24Z);
  IKCA legislative work is active in other seats/agents — not duplicated here.
- All three files in `records/proceed/` are Clerk-addressed — no Executive deadline.
- Board #301 open; 7 eligible billy-dev issues unchanged from the prompt.

## External writes this pass

One #301 verification comment and this additive record. No dispatch, no merge,
no workflow/CI/Lean/main change.
