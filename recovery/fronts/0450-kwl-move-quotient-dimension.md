# kwl-move-quotient-dimension

## status

investigated

## origin

ai_proposal_unverified

## agent_id

zks3tQMeMpQzgF5Mx4wuyU-dream

## exit_state

clearexit

## question

Is there a fixed k such that stable full/paired k-WL colour on ordered pairs determines the exact minimax move value T({x,y}) for every finite poset and every incomparable pair, or does the required k grow without bound?

## basis

Board #301 newest posts: folklore 2-WL fails at n=8, full/paired 2-WL survives all posets through n=9 and height-two posets through n=10; no k>=3 hierarchy test or all-n completeness statement appears in the ledger.

## falsifier

For each proposed fixed k, exhibit a finite poset with two incomparable pairs of identical stable full/paired k-WL colour but different exact T, or give a uniform finite-k definability argument.

## implication

A bounded WL dimension would yield a polynomial-time computable sound move quotient for exact minimax search; an unbounded hierarchy would rule out colour refinement as a complete state-compression mechanism for exact S(n).

## finding_unverified

 `k`” has no canonical meaning for `k≥3` without specifying the extension. Joint-coordinate and one-coordinate extensions are different invariants, and no known monotonicity connects them at the move level.

### 3. Soundness versus completeness

The `n=10` result is **soundness** for the joint 2-WL move quotient: equal colour does not yield unequal `T`. It is not **completeness**, and the stronger “same colour ⇒ child posets isomorphic” mechanism cannot hold for all `n` for any fixed `k`: by Cai–Fürer–Immerman, incidence posets of CFI graphs give non-isomorphic same-`k`-WL posets for every fixed `k`. That refutes the natural proof route, but **not** `T`-soundness itself.

### 4. The stated complexity implication is false as written

A sound **move** quotient does not give a polynomial-time exact evaluator. One still needs:

1. a polynomial-time map from colour and `n` to the numerical `T`, and
2. a sound **state** quotient with a well-defined successor transition.

A colour is a label, not an algorithm. Conversely, a fixed `k` plus a polynomial-time colour-to-`T` map would compute `S(n)` in polynomial time: build `A_n`, colour it, look up its pair colour, return `T+1`. That would put `S_unary` in FP, a major open problem. So the front’s implication requires an extra effectiveness/nonuniform-lookup hypothesis.

### 5. Exact obstruction and honest limits

No all-`n` lower or upper bound on the required WL dimension follows. CFI gives unbounded WL dimension only for **isomorphism**, not for the numeric minimax value `T`; #P-hardness of counting linear extensions does not transfer to `F` or `T` (`S(P)` is not a function of `e(P)`). A proof of bounded `k` would have to establish an arithmetic coincidence of child `F`-values across colour classes, not child isomorphism. I did not find such a proof or an all-`n` counterexample, and I make no claim that the required `k` is unbounded.
**Recovery audit — no side effects repeated.**

- **Host:** `billy-dev`.
- **Working directory:** `/home/lubko/soring-fronts/kwl-move-quotient-dimension`.
- **Git state:** clean at `6a96398`; no commits, branches, stashes, or Lean changes created.
- **Board #301:** exactly **one** comment by `SoringP1 frontier: kwl-move-quotient-dimension`, timestamped `2026-11-09T17:12:53.294Z`. Digest search for `2,567,284` and for the front ID both return one unique match. No duplicate post was made.
- **Background processes:** none still running (`scanpos32`, `genposetg`, and board-post processes are all gone).
- **Scratch:** all work remains under `/tmp/opencode/kwl`; no repository files were modified.
- **Durable ledger:** the front still shows keeper-managed `status: running`, `exit_state: null`, `finding_unverified: null`. I did **not** hand-edit it; that reconciliation is the keeper’s responsibility.

The previously completed mathematical result stands: exhaustive check of all `2,567,284` unlabeled 10-element posets found **0** same-colour classes of incomparable pairs with differing oriented-child isomorphism type for the board’s full/paired 2-WL, so `T` is constant on those classes at `n=10`. The report also records the `k≥3` variant ambiguity, the soundness/completeness distinction, and the fact that the stated polynomial-time complexity implication does not follow without an effective colour-to-`T` map and a sound state transition.

**Unfinished work:** none from this front beyond ordinary keeper reconciliation of the ledger entry. No further external action was taken.

## Other metadata

```json
{
  "finished_at": 1794244452.4608,
  "started_at": 1794242825.5907912
}
```
