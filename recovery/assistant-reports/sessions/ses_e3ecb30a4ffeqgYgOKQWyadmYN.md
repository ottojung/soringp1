# antonina-zks3tQMeMpQzgF5Mx4wuyU-dream

Session: ses_e3ecb30a4ffeqgYgOKQWyadmYN
Workspace: /home/lubko/soring-fronts/kwl-move-quotient-dimension
Created: 1794242826079; updated: 1794244437537

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 1051 (msg_1c14c89860011cRz1D1t0gVRjm)

**Host/state:** billy-dev; worktree clean at `6a96398`; no repository or Lean changes. Scratch is confined to `/tmp/opencode/kwl`. The result was posted once to board #301 at `2026-11-09T17:12:53Z` under `SoringP1 frontier: kwl-move-quotient-dimension`.

## Mathematical finding

I could not prove or disprove the all-`n` bounded-`k` claim. What I did establish is a new exhaustive finite soundness theorem plus a precise obstruction to the question as posed.

### 1. New exhaustive `n=10` result

For the board’s actual full/paired 2-WL update

\[
c_{t+1}(i,j)=\bigl(c_t(i,j),\{\!\!\{(c_t(i,k),c_t(k,j)):k\}\!\!\}\bigr)
\]

with initial colours `(=,<,>,incomparable)`, I enumerated **all `2,567,284` unlabeled 10-element posets** (`genposetg`, matching `A000112(10)`). For every same-colour class of incomparable pairs I compared the unordered pair of oriented-child isomorphism types `(P+x<y, P+y<x)`:

- `6,035,925` same-colour classes of size ≥ 2,
- `13,143,035` incomparable pairs in those classes,
- **0** classes with more than one unordered child-isomorphism type.

Hence exact `T` is constant on every such class at `n=10`. This extends the ledger’s `n≤9` general result and height-two `n=10` result to **all** general 10-element posets. An independent Python/networkx sample of 300 posets reproduced 4,190 class comparisons with 0 failures. This is computation, not an all-`n` proof; the first possible general counterexample is now `n≥11`.

### 2. The `k≥3` question is not one well-defined hierarchy

The board’s full/paired 2-WL is the **joint** update. The standard oblivious `k`-WL tuple hierarchy updates one coordinate at a time; at `k=2` that gives the separate-multiset (“folklore”) colour, which is already false at `n=8`. Thus “the required fixed `k`” has no canonical meaning for `k≥3` without specifying the extension. Joint-coordinate and one-coordinate extensions are different invariants, and no known monotonicity connects them at the move level.

### 3. Soundness versus completeness

The `n=10` result is **soundness** for the joint 2-WL move quotient: equal colour does not yield unequal `T`. It is not **completeness**, and the stronger “same colour ⇒ child posets isomorphic” mechanism cannot hold for all `n` for any fixed `k`: by Cai–Fürer–Immerman, incidence posets of CFI graphs give non-isomorphic same-`k`-WL posets for every fixed `k`. That refutes the natural proof route, but **not** `T`-soundness itself.

### 4. The stated complexity implication is false as written

A sound **move** quotient does not give a polynomial-time exact evaluator. One still needs:

1. a polynomial-time map from colour and `n` to the numerical `T`, and
2. a sound **state** quotient with a well-defined successor transition.

A colour is a label, not an algorithm. Conversely, a fixed `k` plus a polynomial-time colour-to-`T` map would compute `S(n)` in polynomial time: build `A_n`, colour it, look up its pair colour, return `T+1`. That would put `S_unary` in FP, a major open problem. So the front’s implication requires an extra effectiveness/nonuniform-lookup hypothesis.

### 5. Exact obstruction and honest limits

No all-`n` lower or upper bound on the required WL dimension follows. CFI gives unbounded WL dimension only for **isomorphism**, not for the numeric minimax value `T`; #P-hardness of counting linear extensions does not transfer to `F` or `T` (`S(P)` is not a function of `e(P)`). A proof of bounded `k` would have to establish an arithmetic coincidence of child `F`-values across colour classes, not child isomorphism. I did not find such a proof or an all-`n` counterexample, and I make no claim that the required `k` is unbounded.

## Output 1130 (msg_1c14d5213001blPi9o1WZDdS10)

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
