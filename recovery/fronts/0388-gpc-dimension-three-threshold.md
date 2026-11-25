# gpc-dimension-three-threshold

## status

investigated

## origin

ai_proposal_unverified

## agent_id

sbJGHi4QcPZxJsW4KogLce-propose

## exit_state

clearexit

## question

Does every finite poset of order dimension at most three satisfy the Fibonacci extension inequality e(P) >= F_{m(P)+2}, extending the dimension-two threshold to a class whose height-at-least-three slice is not covered by the interval-order, height-two, or width-three fronts?

## basis

Peczarski, The Gold Partition Conjecture, Order 23 (2006); Gupta arXiv:2607.23926v2 reports an exhaustive GPC check through 14 elements; board #301 dimension-two and interval-order GPC posts; the standard example S_3 has dimension three.

## falsifier

Exhibit a 3-dimensional poset on at least 15 elements with e(P) < F_{m(P)+2}, or prove that every 3-dimensional counterexample must have an explicit minimum size and give one.

## implication

A positive answer extends the universal extension threshold T(r) to dimension three and lets the budgeted exact search prune 3-dimensional reachable states; a counterexample would refute the Peczarski consequence of the Gold Partition Conjecture beyond dimension two.

## finding_unverified

posets** (intersections of three linear orders), `1 <= e <= 1000`, exact threshold test: **no failure**.
- **2000 random `S_3`-plus-chain realizer shuffles**: **no failure**.
- **Every single-relation refinement of the staircases `W_n`, `n <= 13`**: **no failure**. The tight refinements are again staircases (`e = F_n`, `m = n-2`).
- **Every maximal insertion above an ideal of `W_n`, `n <= 10`**: **no failure**.

These are negative evidence, not an all-n proof.

### 4. Concrete failed proof route

`[deduction + experiment]` The naive one-element maximal-insertion induction does **not** work using only the Fibonacci hypothesis.

I found an explicit dimension-3 pair:

- `Q`: `e=88`, `m=7`;
- `P = Q` plus one maximal element above an ideal: `e=220`, `m=9`;
- both are dimension 3 (no two-order realizer);
- `e(P)/e(Q) = 2.5`, but `F_{11}/F_9 = 89/34 ≈ 2.6176`.

Both `Q` and `P` satisfy `e >= F_{m+2}`, so this is not a counterexample. It shows that a proof cannot proceed by bare insertion induction; it needs a stronger slack invariant.

The explicit upper-set masks are:

```text
Q = (644, 668, 512, 516, 640, 671, 1727, 512, 1727, 0, 671, 2047)
P = (4740, 4764, 512, 4612, 4736, 4767, 5823, 4608, 5823, 0, 4767, 6143, 0)
I = 3579
```

### 5. Certificate soundness versus completeness

Gupta’s GPC certificates (low-slave pair, half-balanced pair, balanced triple) are **sound sufficient conditions**. The exhaustive `open=0` result through 14 gives computational completeness only there; it is not a general completeness theorem.

A dimension-three Fibonacci theorem would be a **sound pruning rule** for reachable states with small extension count. It would not provide an optimality certificate, would not establish `SORT-BOUND-U ∈ NP`, and would not by itself improve the uniform complexity bound for `S(n)`: the root antichain is dimension 2, and reachable states need not remain dimension 3. A counterexample would refute the Peczarski consequence of GPC for dimension 3, but not the converse.

## Honest limits

- No all-n theorem and no counterexample.
- The dimension-two base is misidentified in the front’s evidence; the published result is width-two.
- The computational searches are finite and non-exhaustive beyond the stated ranges.
- One board post was made; no other external action, commit, PR, or Lean file was created.
Recovery inspection complete; no duplicate action was taken.

- **Working directory / Git:** `/home/lubko/soring-fronts/gpc-dimension-three-threshold` is on `billy-dev` at `6a96398`, with a clean worktree. No commits, PRs, Lean files, or repository edits were made.
- **Board effect:** exactly one comment exists for this front, at `2026-11-08T19:57:05Z`, author `SoringP1 frontier: gpc-dimension-three-threshold`. It appears once on page 1 and nowhere on pages 2–3. I did not repost it.
- **Durable ledger:** the `gpc-dimension-three-threshold` entry is still `running` with no `exit_state`/`finished_at`; this is keeper-managed and should be reconciled by the pool keeper when the agent exits. I did not edit the ledger manually.
- **Unfinished work:** none from the mathematical side. The investigation was completed and reported: no counterexample, no all-n proof, source correction (published width-two, not dimension-two, GPC), an exact first-counterexample window (`|P| ≥ 15`, `e ≥ 144`), finite falsification experiments, and a concrete dimension-3 obstruction to naive maximal-insertion induction.

No further external side effects are needed.

## Other metadata

```json
{
  "finished_at": 1794167984.205719,
  "started_at": 1794163550.2159
}
```
