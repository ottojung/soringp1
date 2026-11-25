# bulk-insertion-information-defect

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Hp0b1YFe7t2jWaX8CgllDv-wicked

## exit_state

clearexit

## question

For a fixed alpha in (0,1), let P(n)=C_{floor(alpha n)} disjoint-union A_{n-floor(alpha n)} and D_alpha(n)=F(P(n))-ceil(log2(n! / floor(alpha n)!)). Is D_alpha(n) bounded by a constant depending only on alpha for all n, or unbounded along an infinite subsequence?

## basis

Board #301's matching-prefix and Ford-Johnson insertion reductions; literature on multiple insertion and sorted-list merging; a small exact minimax probe through n=8 gives defect 1 at (n,m)=(6,3),(6,4),(7,4),(8,4), while larger-n behavior is unchecked.

## falsifier

Exhibit a fixed alpha and an infinite sequence n_i with D_alpha(n_i) tending to infinity via certified lower bounds, or construct an all-n insertion strategy proving a uniform bound for some alpha.

## implication

A uniform bound for one alpha gives S(n)<=S(floor(alpha n))+F(P(n)) and hence a new route to S(n)<=ceil(log2 n!)+O(log n); unboundedness would rule out bulk insertion as a route to sublinear excess.

## finding_unverified

**Outcome: the front is not resolved; it is a genuine open dichotomy. No repository or Lean changes. One board post was made (after checking there was no prior post for this front).**

## Mathematical finding

Let `P(m,n)=C_m ⊔ A_{n-m}`, `F(m,n)` its exact minimax, `C_P=ceil(log2(n!/m!))`, and `D(m,n)=F(m,n)-C_P`.

**New all-`m` theorem (elementary, unconditional).** For every fixed free block size `r`,
```
D(m, m+r) <= E(r) + r,     E(t)=S(t)-ceil(log2 t!).
```
Proof: sort the `r` free keys optimally, then merge with the chain by the Hwang–Lin generalised binary merge, whose excess over the merge information bound is at most `r-1`, and `C_P >= C(r)+I-1`. This bounds `D` on fixed-`r` slices, but not in the front’s regime where `r=(1-alpha)n` grows. It also shows why the board’s `fixed-pattern-defect-bound` does not apply: that result bounds `S(n)-F(P)`, a different quantity.

**Exact new data.** `D=1` at `(n,m)=(6,3),(6,4),(7,4),(8,4),(9,6)`; `D=0` at `(5,3),(7,3),(7,5),(9,5)`; no `D=2` for `n<=9`. For `r=2`, `D∈{0,1}` for all tested `m<=40`. Computations were done with two independent exact minimax implementations.

**Decomposition identity.** With `delta(m,n)=F(m,n)-S(n)+S(m)>=0` and `C_P=C(n)-C(m)+eta`, `eta∈{0,1}`,
```
D(m,n) = E(n)-E(m) + delta(m,n) - eta,      hence D >= E(n)-E(m)-1.
```
A natural strengthening `delta<=1` is **false**: at `(n,m)=(21,19)`, the independent `r=2` exact DP gives `F=10`, and with `S(21)=66`, `S(19)=58`,
```
delta(21,19)=10-66+58=2.
```
That instance still has `D=1`.

## Concrete obstruction

- **Unbounded horn** requires either `E(n)-E(floor(alpha n))` unbounded (so `E` unbounded; no published result even gives `E(t)>=2` for one `t`) or the new decomposition gap `delta` unbounded. All available sound lower bounds — `C_P`, `S(r)<=F`, the merge number `K(m,r)<=F`, and `S(n)-S(m)<=F` — are `Theta(n)` below `C_P` at fixed `alpha`, or give at most `E`-difference `<=1` with current certificates. Sound count-lookahead potentials are also incomplete.
- **Bounded horn** is not a finite check: if `D_alpha(n)<=K` for one `alpha`, iteration gives `E(n)=O_alpha(log n)`, i.e.
```
S(n) <= ceil(log2 n!) + O_alpha(log n),
```
improving Sergeev’s `O(n/(log n)^(1/5))` excess to logarithmic. That is a major open upper-bound theorem.

General-poset results (fence defect `Omega(n)`, GPC’s multiplicative bound) do not transfer to `C_m ⊔ A_r`. Full note: `/home/lubko/.local/state/soringp1/bulk-insertion-information-defect-20261108.md`.

## Other metadata

```json
{
  "finished_at": 1794180276.1956878,
  "started_at": 1794172071.729141
}
```
