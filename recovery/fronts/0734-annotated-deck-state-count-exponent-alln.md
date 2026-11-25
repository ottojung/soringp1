# annotated-deck-state-count-exponent-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Zq3jaGw7rAcKjwPGzDEiIa-religion

## exit_state

clearexit

## question

Let Adec(n) be the number of distinct (e,F)-annotated one-step child decks Dstar(P) as P ranges over all poset states on n labelled elements, and let Adec^reach(n) be the same count restricted to states reachable in the budgeted minimax game at budget S(n). Is Adec^reach(n) = 2^{o(n log^2 n)} for all n, so that grouping states by Dstar could support a new exact evaluator, or does Adec(n) grow at least 2^{Omega(n log^2 n)} along an infinite family, matching or exceeding the exponent of the current best exact evaluation algorithm?

## basis

docs/problem.md records the 2^{O(n log^2 n)} evaluator and faster evaluation as the active frontier; docs/research-strategy-certificates.md counts unannotated and all-optimal DAG states; board #301 establishes Dstar as a finite, independently checked invariant at n<=7; no ledger front counts F-annotated decks.

## falsifier

Exhibit an infinite family of n for which the number of distinct annotated child decks among reachable n-element states is at least 2^{c n log^2 n} for a fixed c>0, or conversely construct a uniform grouping by Dstar that provably evaluates S(n) exactly in 2^{o(n log^2 n)} time.

## implication

A subexponent annotated-deck count would open a new exact-evaluation route by grouping minimax states on Dstar and would improve the time bound for unary SORT-BOUND-U, an explicitly listed achievable outcome; a superexponent count is a barrier showing annotated decks cannot compress the minimax DP. Neither horn by itself separates complexity classes or proves a new S(n) value.

## finding_unverified

he Viche Executive 20:45Z independent n<=7 verification and extends it by one size. It is **not** an all-`n` theorem; the board already records the all-`n` question as open and notes no mixed-F obstruction found. `[experiment]`

2. **Trivial upper bound (deduction).** Since `Dstar` is a function of the unlabelled poset, `Adec^reach_tight(n) <= Adec(n) <= A000112(n)`. Kleitman–Rothschild give `A000112(n)=2^{n^2/4 + 3n/2 + O(log n)}`. Therefore
   `Adec(n) <= 2^{O(n^2)}`.
   This upper bound is **above** the `2^{O(n log^2 n)}` threshold: it does **not** imply the subexponent horn, and it is consistent with either horn. `[deduction, literature: Kleitman–Rothschild asymptotic for posets]`

3. **No nontrivial all-n lower bound proved (obstruction).** Proving `Adec(n) >= 2^{c n log^2 n}` would require exhibiting, for infinitely many `n`, that many nonisomorphic posets have pairwise distinct `(e,F)`-annotated child decks. Distinct posets can share invariants (the board has many e/F-collision examples), so A000112 is not a lower bound. I did not find a constructive infinite family forcing distinct `Dstar` at the needed rate. Conversely, proving `Adec^reach(n)=2^{o(n log^2 n)}` would require a uniform deck-collision/compression argument; I did not find one. `[obstruction]`

4. **Small-n data is inconclusive for the exponent question.** The `n=6..8` ratios `log2(Adec)/(n log2^2 n) ~ 0.179` are stable but cover only three tiny sizes; this cannot distinguish `2^{Theta(n log^2 n)}`, `2^{Theta(n^2)}`, or intermediate growth. The relevant comparison is `2^{O(n log^2 n)}` current exact-evaluation time (problem.md) versus poset-space `2^{Theta(n^2)}`: the deck count sits between “same as all posets” and “small enough to explain the evaluator” and is unresolved here. `[experiment + deduction]`

## Why this does not settle the front

- **No all-n theorem either way.** Neither the `2^{o(n log^2 n)}` upper horn nor the `2^{Omega(n log^2 n)}` lower horn is proved.
- **No evaluator improvement.** Even a subexponent `Adec^reach` count would only “support/open a route” if one also has a way to enumerate/transition by deck classes efficiently and prove `Dstar`-completeness of F for the relevant states; I have not produced such an evaluator. The front already states this implication boundary.
- **No complexity-class separation.** As the front notes, neither horn by itself separates complexity classes or proves a new `S(n)` value.
- **Reachability notion caveat.** I used tight `delta+F==S(n)`. A looser budget-reachable definition could make `Adec^reach` larger; a stricter actual-play definition could make it smaller. The all-n exponent question should pin this down.
- **n=9 incomplete.** The n=9 unlabelled enumeration completed (183231 classes, matching A000112) but deck/F census was killed by SIGKILL; no n=9 Adec number is reported.

## Concrete next falsification target

A decisive next step would be either (a) a rigorous counting/lower-bound argument producing `2^{c n log^2 n}` distinct reachable `Dstar` values on an explicit family (even a general-poset family, clearly labelled as such, would be a barrier signal but would not directly settle the reachable-S(n) question), or (b) a provable compression of `Dstar` classes on the tight reachable set below `2^{o(n log^2 n)}` together with a sound transition argument. Small-n enumeration beyond n=8 should use a memory-efficient streaming/indexed representation rather than holding full per-state deck objects in maps.

## Other metadata

```json
{
  "finished_at": 1795469725.3637955,
  "started_at": 1795468014.9079802
}
```
