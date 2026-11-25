# non-tight-infinitely-often-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

uqpbLxMlP3iV1GHQ35btdv-fighting

## exit_state

clearexit

## question

Are there infinitely many integers n such that S(n) is strictly greater than ceil(log2 n!), i.e. the information bound is not tight for infinitely many n?

## basis

Known values S(12..19,22) exceed ceil(log2 n!) while S(20),S(21) are tight; board #301 tightness-density-zero front; Sergeev surplus o(n).

## falsifier

Prove that S(n)=ceil(log2 n!) for all sufficiently large n, or construct and verify the first non-tight case beyond n=22 plus an infinite family with excess at least one.

## implication

Infinitely many non-tight cases would make a persistent asymptotic penalty in the budget window; eventual tightness would let exact evaluators clamp the search budget to the information bound for large n.

## finding_unverified

chain root, every comparison splits `n!` evenly (`n!/2` each), so `L1(A_n) = C(n)`. The obstruction must occur deeper, which is exactly the exhaustive-search problem.

---

### 5. Exact obstructions

**Obstruction 1 — Computational barrier.** `S(n)` is exactly known only for `n ≤ 22` (plus `S(28) ≥ 99`). `S(23)`–`S(27)` are open. The backward/forward poset search for n=23 hits a wall at level 3 (~21M states, level 4 projected at ~3×10⁹). No feasible computation can verify any specific `n` in `23..27` or beyond 28. **Consequence:** we cannot verify the first non-tight case beyond n=22 (it could be 23, 24, 25, 26, 27, or 28), and we cannot verify any member of a candidate infinite family.

**Obstruction 2 — No general tightness construction.** No sorting algorithm achieves `ceil(log2 n!)` for any `n ≥ 12` except the isolated tight cases n=20,21 (established by exhaustive search). Ford–Johnson has linear excess; Sergeev has sublinear but nonzero excess. **Consequence:** eventual tightness cannot be proved by exhibiting a construction.

**Obstruction 3 — No general non-tightness lower bound.** Every known non-tight case (12–19, 22, 28) required individual exhaustive computation of `S(n)`. There is no technique to show `S(n) > C(n)` for any infinite family without computing each `S(n)`. **Consequence:** infinite non-tightness cannot be proved.

**Obstruction 4 — Non-monotonicity.** Tightness is not monotone in `n` (tight at 20,21; non-tight at 22, 28). No propagation from one `n` to another is possible.

**Obstruction 5 — Certificate soundness vs completeness.** A sound certificate for `S(n) ≤ k` (exhibit a sorting tree) has `2·n!−1` nodes — exponential in the unary input length, so it is not a polynomial-size certificate. No complete (succinct) certificate for `S(n) > k` is known. The information bound `log2 e(P)` is sound but incomplete (poset-level counterexamples at n=5,6). **Consequence:** we cannot even succinctly certify either direction for large `n`.

---

### 6. Honest conclusion

**The question is open.** Neither horn of the falsifier is established:

- **Eventual tightness** (`S(n) = ceil(log2 n!)` for all sufficiently large `n`): cannot be proved — no construction achieves the information bound for any infinite family, and the best known upper bounds (Ford–Johnson, Sergeev) have nonzero excess.
- **Infinite non-tightness**: cannot be proved — `S(n)` is only known exactly for `n ≤ 22` (plus `S(28) ≥ 99`), and no structural lower-bound technique can show `S(n) > C(n)` without computing `S(n)`.

**Concrete finding:** `n=28` is confirmed non-tight (`S(28) ≥ 99 > 98 = C(28)`), extending known non-tight cases beyond n=22. But `S(23)`–`S(27)` are unknown, so we cannot identify the *first* non-tight case beyond n=22, and no infinite family with excess ≥ 1 is verifiable.

**Next decisive obstacle:** either (i) compute `S(23)` (or show `S(23) > 75` or `S(23) = 75`), or (ii) develop a structural lower-bound technique that proves `S(n) > C(n)` for some `n` without exhaustive computation, or (iii) develop a sorting algorithm achieving `C(n)` for an infinite family. All three are beyond current reach — this is a genuine open problem in comparison-sorting complexity.

No repository changes, Lean formalizations, or commits are warranted: there is no genuinely substantive, independently checkable new theorem or counterexample to integrate. All work was read-only analysis on billy-dev; working tree remains clean at `6a96398` (branch `billy-dev`).

## Other metadata

```json
{
  "finished_at": 1795319382.2044492,
  "started_at": 1795318827.201301
}
```
