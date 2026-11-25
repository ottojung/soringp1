# defect-a1-universal-floor-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

teX4Q2YEwzQTZ9ghQuOkwQ-psoas

## exit_state

clearexit

## question

For every integer b >= 1 and every poset B on b elements, is the one-key disjoint-union defect delta(A_1,B) = F(B union A_1) - F(B) always at least ceil(log2(b+1)) - 1, or can an information-excess host B create a shortfall of two or more comparisons below the chain defect?

## basis

Board #301 2026-11-21: T1/T2 prove delta(A_1,B)<=c=ceil(log2(b+1)) for all B and the P2 bracket gives delta in {c-1,c} for information-tight B, while excess hosts only give delta>=gap-r(B) which can be below c-1; exhaustive b<=5 search found no c-2 case (min delta=c-1).

## falsifier

Exhibit explicit b >= 1 and a b-element poset B with delta(A_1,B) <= ceil(log2(b+1)) - 2, witnessed by an exact minimax value or a certified upper strategy for F(B union A_1) together with a certified lower bound for F(B).

## implication

A proof would extend the proved tight-host {c-1,c} dichotomy to all hosts, strengthening the a=1 defect envelope used in disjoint-union superadditivity bounds; a counterexample would isolate an excess-amplified insertion shortcut and refine the structural invariant governing when B union A_1 loses more than one comparison of the chain maximum.

## finding_unverified

 `e(B⊔A_1)=(b+1)e(B)`,
`delta = gapinfo + r(B⊔A_1) - r(B)`.
Thus a `c-2` shortfall is equivalent to a **large excess drop**:
- `gapinfo==c-1` (the dangerous case): `delta <= c-2  <=>  r(B⊔A_1) <= r(B)-1`.
- `gapinfo==c`: `delta <= c-2  <=>  r(B⊔A_1) <= r(B)-2`.

With `r(B⊔A_1)>=0`, any counterexample requires `r(B)>=1` (or `>=2` in the second case). This recovers the known P2 fact [literature/board, Viche 11:19Z disposition]: information-tight hosts (`r=0`) give `delta∈{c-1,c}`. The open content is exactly whether adding one isolated key can collapse host excess by >=1 (or >=2) unit.

### 2) The naive disjoint-channel lower bound fails [deduction, failed approach]
A tempting argument is: B-comparisons and x-comparisons are disjoint channels, adversary forces `F(B)` B-comparisons and `c` x-comparisons, so `F(U)>=F(B)+c`, `delta>=c`. **This is false.** Counterexample: N-poset gives `delta=2 < c=3`. The flaw: a comparison `(bi,bj)` can become forced by transitivity through `x` (`bi<x` and `x<bj` imply `bi<bj`), so x-comparisons can resolve B-incomparabilities. The two comparison sets are disjoint as edges but not informationally independent; the adversary cannot fix a B-strategy independently of x-placement. This is the same mechanism behind the verified tight-host `c-1` cases.

### 3) Exhaustive small-n evidence [experiment]
Exhaustive over all forward-labeled closures (every isomorphism type represented by some topological labeling; deduped by closure) found **no** `delta <= c-2`:
- `n=4`: 40 distinct posets, max `r-rU = 0`, time 0.05s.
- `n=5`: 357 distinct posets, max `r-rU = 1` (witness `n=5,e=8,F=4,r=1; eU=48,FU=6,rU=0,c=3,gapinfo=3,delta=2`), no violation, 3.0s.
- `n=6`: 4824 distinct posets, max `r-rU = 1` (witness `n=6,e=240,F=9,r=1; eU=1680,FU=11,rU=0,c=3,gapinfo=3,delta=2`), no violation, 371s.

A partial random search (`n=5..8`, incomplete; killed) observed `n=5 mindelta=2 maxdrop=0 maxr=0`; `n=6 mindelta=2 maxdrop=1 maxr=1` before kill; `n>=7` not completed. These are finite experiments, not an all-n argument.

## Obstruction / what would decide it
- **Falsifier (still open):** an explicit excess host B with certified `F(B)>=ceil(log2 e(B))+r`, `r>=1`, and a certified upper strategy for `B⊔A_1` making `r(B⊔A_1)<=r-1` (in the `gapinfo=c-1` case) or `<=r-2`. The b=5 excess host `(e=8,F=4,r=1,gapinfo=3)` gives `delta=2=c-1` (drop 1, not enough) — it saturates the drop but has `gapinfo=c`.
- **Proof route obstruction:** one needs a general inequality `F(B⊔A_1) >= F(B)+ceil(log2(b+1))-1` even for excess B, i.e. “transitivity through one isolated key can save at most one comparison beyond the chain defect”. The disjoint-channel proof fails because of transitivity shortcuts; a valid proof must control how many B-forcing comparisons can be made redundant by x-placement. I did not find such an all-n argument.
- **Complexity significance [deduction]:** this is a structural minimax invariant. A proof would strengthen the a=1 defect envelope in disjoint-union superadditivity; a counterexample would refine it. Neither gives a new bound on `S(n)` or any complexity-class separation for `SORT-BOUND-U` (which is in PSPACE; tally/P/poly barrier applies).

## Honest limits
No all-n proof, no counterexample. n<=6 exhaustive and partial random n<=8 give no `c-2` case; max observed excess drop is 1. I did not construct a certified c-2 witness and did not prove the c-1 floor. S(n) and SORT-BOUND-U remain open. No repo/Lean/board/ledger changes made.

## Other metadata

```json
{
  "finished_at": 1795266936.9052746,
  "started_at": 1795264147.05243
}
```
