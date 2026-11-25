# fixed-pattern-defect-bound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

OLcZt3cDTQMKD4QC043tqc-suite

## exit_state

clearexit

## question

For every fixed finite poset Q, is the defect D_Q(n)=S(n)-F(Q disjoint-union A_{n-|Q|}) bounded by a constant depending only on Q, rather than growing unboundedly with n?

## basis

The board #301 t=1 lemma gives D_{C_2}(n)=1 for all n; independent exact minimax for n<=7 gives D_{C_3} in {2,3}, D_{C_4} in {4,5}, and D_V,D_L in {1,2} for the three- and four-element seed posets.

## falsifier

Exhibit one fixed Q and an infinite sequence n_j for which D_Q(n_j) exceeds every constant; the computed chain values D_{C_3}(3..7)=3,3,2,2,3 show no plateau yet, so a growth proof or a longer computed plateau would discriminate.

## implication

Bounded defects would say fixed known comparability changes the exact bulk sorting number by only O(1), supporting pattern-decomposition and certificate arguments; unbounded defects would show local structure amplifies into the antichain root.

## finding_unverified

## Finding: the defect is bounded for every fixed pattern

Let `q=|Q|` and `P = Q ⊔ A_{n-q}`. The front's question has a clean affirmative answer:

\[
0 \;\le\; D_Q(n)=S(n)-F(Q\sqcup A_{n-q}) \;\le\; S(q)\;\le\;\binom q2 .
\]

### Proof

Since `P` has more known relations than `A_n`, `F(P) ≤ S(n)`, so `D_Q(n) ≥ 0`.

For the other side, fix any linear extension `C_q` of `Q`. Then `C_q ⊔ A_{n-q}` is a superposet of `P`, hence

\[
F(C_q\sqcup A_{n-q}) \le F(P).
\]

Now sort an arbitrary `n`-key antichain:

1. Sort any chosen `q` keys optimally, costing `S(q)`.
2. Label them in increasing order along `C_q`, and label the rest as the antichain block.
3. Run an optimal sorter for `C_q ⊔ A_{n-q}`.

The actual labelled order is a linear extension of `C_q ⊔ A_{n-q}`, so the second phase returns the true order. Therefore

\[
S(n) \le S(q)+F(C_q\sqcup A_{n-q}) \le S(q)+F(P),
\]

which gives the claimed bound.

Consequently no fixed `Q` admits an infinite sequence `n_j` with `D_Q(n_j)` exceeding every constant. The proposed falsifier is impossible.

### Sharpness and limits

- The bound is attained at `n=q` for `Q=C_q`, where `D=S(q)`. So the constant cannot be made independent of `q`.
- The theorem does **not** determine the exact defect. The bound `S(q)` may be loose for large `n`.
- It is a general-poset structural inequality, not a certificate-completeness result. It yields no new evaluator and no P/NP/PSPACE consequence, since `F(Q⊔A_{n-q})` still must be computed.
- The argument is elementary/folklore — essentially “sort the seed, then relabel along an extension” — not a substantive new theorem. I therefore made no repository or Lean changes.

### Falsification attempt

Exact minimax over all posets `Q` on `q≤4` elements for `n≤6` found no violation of `D_Q(n)≤S(q)`. The maximum was exactly `S(q)` at `n=q` for the chain and did not grow with `n`. This matches the board values for `C_2`, `C_3`, `C_4`, `V`, and `L`.

The honest next frontier is the exact asymptotics of `D_Q`, not whether it is bounded. I posted the finding to board #301; the worktree remains clean.

## Other metadata

```json
{
  "finished_at": 1794167494.0604856,
  "started_at": 1794166291.008116
}
```
