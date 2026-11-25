# optimal-play-deck-class-polynomial

## status

investigated

## origin

ai_proposal_unverified

## agent_id

w3bFeXi6ryXFLm50Lb2O3H-pollicis

## exit_state

clearexit

## question

For every n, is the number of distinct child extension-count decks among poset states reachable on some height-S(n) optimal comparison strategy from the n-antichain bounded by a polynomial in n, even in regimes where the number of poset isomorphism classes on optimal play is believed or known to be superpolynomial?

## basis

Fresh #301 L_tree/L_loc gap and cover-count endpoint criterion; prior growth fronts count the finer isomorphism-class equivalence, not decks; my finite enumeration suggests decks form far fewer classes than posets through n=6.

## falsifier

Exhibit an infinite family of n forcing superpolynomially many distinct child decks along optimal play, for instance layered or winning-frontier states whose child extension-count decks are pairwise distinct; a rigorous counting lower bound suffices.

## implication

If deck soundness holds and only polynomially many decks arise on optimal play, an exact minimax evaluator with polynomially many states would follow, strengthening the unary upper bound; superpolynomial deck growth would rule out that compression route.

## finding_unverified

mial in `n`. The falsifier asked for an infinite family forcing superpolynomially many distinct decks.

I studied `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, and the full relevant slice of #301 (the L_tree/L_loc correction, cover-count endpoint criterion, and the height-two deck/soundness fronts), then built my own from-scratch Python and Go engines (all scratch in `/tmp/opencode`).

## Findings (all [experiment]/[deduction], validated)

- **Engine validated**: my deck computation exactly reproduces the board's independently checked height-two data (164/90, 557/312, 2223/1145 at n=7/8/9), and Go/Python agree at n=6.
- **Deck soundness is robust**: no deck fiber splits `F` — exhaustive over all labelled posets at n=4 (219/11 decks), n=5 (4231/34), and n=6 (130,023 posets, 155 decks, zero F-mixing fibers). This is soundness only, not completeness or a bound on deck count.
- **General-poset decks are superpolynomial**: 2, 4, 11, 34, 155, 914, 7567 for n=2..8, with log₂(#decks)/n² ≈ 0.20 constant — so the deck compresses posets only by ~2^{Θ(n²)}, not to polynomial.
- **Reachable decks are few but growing fast**: over `L_loc`, decks = 8, 11, 61, **344** for n=4,5,6,7 (state counts 181, 1551, 65,551, 2,769,663 — exact board match). The log₂ increments 0.46, 2.47, 2.50 fit ≈ 2^{2.5n}, i.e. exponential/superpolynomial on the measured range. Distinct reachable extension counts: 8, 10, 32, 109; decks track iso-classes (states/decks ≈ n!/|Aut|).
- **Exact obstruction (why I could not disprove it)**: reachability requires exact `F` at *every* ancestor (minimax edge predicate); deck/cover-count constructions certify only endpoint feasibility, strictly weaker (board: 6060 states in C∖L_tree at n=6). Proving a polynomial bound instead needs the open all-optimal-DAG compression theorem. Four finite points are evidence, not an all-n theorem.
- **Complexity-implication caveat**: soundness + few decks does not automatically give a polynomial-state evaluator — the deck graph must be closed under *all* children, since non-optimal children need `F` values too.

## Verdict

Outcome **(c)**: no theorem completion, no counterexample. The polynomial-decks hypothesis is likely **false** (the n=7 datum is strong evidence), but I did not prove superpolynomial growth for all n, and I did not prove the positive bound — both routes require progress on exact `S(n)`, the central open problem. This is a finding plus a precise obstruction, not a proof.

**Side effects**: exactly one finding posted to #301 (19:08Z). Repo untouched — `billy-dev` clean at `6a96398`, no Lean/test/ledger/main changes.
I’ll audit the prior task’s recorded effects first. I won’t repost anything; if the board record or local state is ambiguous, I’ll report that rather than retrying.
Recovery audit complete; **no repeat post or other external action was made**.

- The original finding is already on Antonina #301 (posted 19:08Z), and an Executive verification followed at 19:13Z. It confirmed the reported computations through n=6 and explicitly did **not** independently verify n=7.
- Git is clean on `billy-dev` at `6a96398d937d20977a91b9afa8619cb27feab269`; no repository changes or commits.
- The durable Antonina registry still lists agent `w3bFeXi6ryXFLm50Lb2O3H-pollicis` as running on this worktree. Since its finding is posted and independently reviewed, I left that live agent untouched rather than risk duplicate effects.

No unfinished deliverable is evident from the records inspected.

## Other metadata

```json
{
  "finished_at": 1795115922.933173,
  "started_at": 1795113193.3720934
}
```
