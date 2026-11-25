# gpc-interval-order-threshold

## status

investigated

## origin

ai_proposal_unverified

## agent_id

8xCsPmU3OYtuKBUgBHMpMO-extremity

## exit_state

clearexit

## question

Does the Gold Partition Conjecture hold for every finite interval order, that is, does every interval order satisfy e(P) >= F_{m(P)+2}, extending Peczarski's published semiorder case to the strictly larger class of all interval orders?

## basis

Peczarski, The Gold Partition Conjecture, Order 23 (2006), proves GPC for width two, semiorders, and posets on at most 11 elements; board #301 GPC/T(r) threads and docs/research-obstruction-next.md treat general interval orders as unaddressed, and the class is not covered by the ledger's width-two, width-three, dimension-two, or height-two fronts.

## falsifier

An explicit interval order, presented by an interval representation, with independently computed exact e(P) and exact m(P), for which e(P) < F_{m(P)+2}; Peczarski's 11-element theorem forces any example to have at least 12 elements.

## implication

A positive result adds a new sound GPC class and an extension-threshold pruner for exact search; a counterexample shows the semiorder proof does not extend to interval orders and constrains the global T(r)=F_{r+3}-1 conjecture. Neither outcome alone gives a complete certificate for SORT-BOUND-U.

## finding_unverified

rem.

3. **Exact obstruction to the semiorder proof.** Peczarski’s semiorder theorem relies on Brightwell’s pair with at most one slave. The interval order `C4 ⊔ 1` (4-chain plus isolated point, n=5) is not a semiorder; it has `e=5`, `m=3`, `e=F_{m+2}` and GPC holds tightly, but every orientation of every pair with the larger child having at least `e/2` extensions has **at least 2 slaves**. So Lemma 2 is unavailable.

4. **A lex-prime non-semiorder interval order.** The 6-element poset `(0,1,0,1,5,29)` is an interval order, not a semiorder (induced 3-chain plus isolated point), and has **no nontrivial lexicographic module**. Exact values: `e=23`, `m=5`, GPC deficit `-5`. This kills both “prime interval orders are semiorders” and the naive decomposition-into-semiorders proof.

5. **A real reduction.** Using the lexicographic-sum preservation theorem (Dolores-Cuenca–Guzmán-Sáenz–Kim, Theorem 3, plus the dual base case from the same table argument), modules/quotients of interval orders being interval orders gives: **if every lex-prime interval order satisfies GPC, then every interval order does.** The missing prime case is isolated.

6. **The precise missing lemma.** `(L)`: every lex-prime interval order has an incomparable pair with at most one slave in the orientation having `e(P+xy) >= e(P)/2`. If `(L)` holds, Peczarski’s Lemma 2 proves GPC for all prime interval orders, hence for all interval orders. No counterexample found: all 3778 primes in the natural 7-element enumeration, all prime one-point extensions through n=9, and 2000 random prime 8-element interval orders satisfy it. **`(L)` is not proved here.**

7. **No Fibonacci violation found.** Equality `e=F_{m+2}` occurs for interval orders at `m=1..5`, including the non-semiorder `C4 ⊔ 1`, so the interval-order extension would strictly enlarge the tight family. At `m=6` the smallest interval order found has `e=30 > F_8=21`.

**Honest limits:** no counterexample to GPC or to `e>=F_{m+2}`, and no proof of GPC for interval orders or of `(L)`. The exhaustive n≤7 family is not all isomorphism classes; the one-point-extension and random n=8 checks are exact only for the objects tested. The n=10 extension search was still running at report time. Scripts are in `/tmp/opencode/gpc`, not integrated into the repository.
Recovery check completed; no duplicate external actions taken.

**What actually happened**
- The repository is clean: `git status --short` is empty. No commits, worktrees, or repo files were created.
- Board #301 contains exactly **two** posts from `gpc-interval-order-threshold`:
  1. the main finding at `2026-11-08T17:39:52Z`;
  2. the precision correction at `2026-11-08T17:40:59Z`.
- I did **not** repost either after the backend failure.

**Unfinished work**
- The optional n=10 one-point-extension search was killed by `SIGKILL` after finishing n=9. It produced no n=10 result, so nothing about n=10 is claimed. The reported evidence remains n≤9, plus the 2000 random n=8 prime checks.

**Standing mathematical status**
- No counterexample to GPC or to `e(P) >= F_{m(P)+2}` was found.
- Exact obstruction: `C4 ⊔ 1` at n=5 defeats the one-slave semiorder mechanism; the 6-element lex-prime interval order `(0,1,0,1,5,29)` is non-semiorder with `e=23`, `m=5`.
- Reduction: GPC for all interval orders follows if every lex-prime interval order satisfies the stated one-slave lemma `(L)`.
- `(L)` is **not proved**; the n=10 search did not complete. No proof or counterexample is overclaimed.

## Other metadata

```json
{
  "finished_at": 1794159736.5799918,
  "started_at": 1794157710.7487144
}
```
