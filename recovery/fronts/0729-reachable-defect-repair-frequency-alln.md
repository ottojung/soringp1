# reachable-defect-repair-frequency-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

mDETFI9fgdJpgUWbvrSxxn-memorable

## exit_state

clearexit

## question

For local information excess delta(P)=F(P)-ceil(log2 e(P)) on states reachable along height-S(n) optimal play from the n-antichain, can delta drop from positive to zero in a single optimal comparison? From-scratch computations record zero such repairs over 1551 reachable states at n=5 but 7200 over 65551 states at n=6 (example: depth-5 state K=(30,16,8,0,0,18), delta=1, optimal move (0,5) gives child with delta=0). Is the set of n admitting a reachable defect repair cofinite, or are there infinitely many n whose optimal-play family is repair-free?

## basis

From-scratch subset-DP and world-set minimax computations at n<=6 (two distinct designs) record 0 reachable repairs at n=5 and 7200 at n=6; board #301 defect, k-safe and one-ply-flatness dispositions; AGENTS.md soundness-versus-completeness distinction.

## falsifier

Establish an infinite family of n for which every defective reachable optimal-play state has no delta-dropping optimal child, or conversely exhibit for all sufficiently large n a reachable optimal comparison whose outcome child has strictly smaller delta, with e and F recomputed from first principles.

## implication

If repairs are eventually impossible, positive defect becomes a monotone locally checkable invariant propagating toward the root and supporting a sound one-step defect certificate for S(n)<=k; if repairs persist, any defect-based certificate must track global remaining depth, blocking local-invariant routes toward NP membership of the unary threshold.

## finding_unverified

al worst-case edges [deduction + experiment]

The bound is tight in form: a drop of exactly 1 occurs iff `L(C)=L(P)` (the comparison does not cross a power-of-two information boundary) while `F` drops by 1. The n=6/n=7 witnesses are explicit instances. So “repairs persist / are possible” is true in the weak sense at finite n; the front's data already showed this.

### 3. The front’s complexity implication needs care [deduction, barrier]

The front suggested: “if repairs are eventually impossible, positive defect becomes a monotone locally checkable invariant propagating toward the root ... supporting a sound one-step defect certificate”. Proposition 1 already gives a stronger local fact: **on optimal worst-case edges `delta` is nonincreasing and can fall by at most 1**. But this is far from a useful sound NP-style certificate for `SORT-BOUND-U`:
- `delta(P)>0` is sound for `F(P)>L(P)`, but **not** for `S(n)>k` unless you also certify the edge is on an optimal-height play reaching a defect that forces the root. Soundness vs completeness (AGENTS.md) is the key obstruction.
- Certifying `delta`/`F` locally needs `e(P)`/`F(P)`, which are #P-hard / minimax-hard in general posets; `L1`-style one-ply tests are sound but incomplete (see `docs/research-one-ply-obstruction.md`).
- The antichain root has `delta(A_n)=D(n)=S(n)-ceil(log2 n!)`, which is 0 at the known tight n and 1 at the known non-tight n; a monotone-local defect invariant cannot by itself turn that into an NP witness without a global optimal-play certificate. An optimal tree is exponentially large (problem.md §61).
- Thus neither horn gives a complexity-class separation. At best it is a structural barrier/certificate-shape fact.

## Failed/blocked approaches

- **n=8 exhaustive enumeration**: killed by SIGKILL after the F memo filled; needs a memory-aware/out-of-core or stronger pruning design. I did not rerun it after the kill to avoid repeating an expensive effect.
- **Proving “no repair for all large n”**: refuted as a universal statement by n=6,7 and by the easy existence of local L-preserving F-drops; the live question becomes quantitative/frequency, which I did not settle for all n.
- **Turning monotonicity into SORT-BOUND-U certificate**: blocked by global optimal-play certification and #P/minimax cost of local predicates.

## Falsification attempt

I tried to falsify the unit-drop bound by searching for any `delta` drop >=2 in all reachable optimal worst-case edges through n=7 (2,769,663 reachable states at n=7). None found. I then looked for a paper counterexample shape; the partition inequality `e' < e => L' <= L` is unconditional, so no finite poset counterexample exists. The attempted falsification fails.

## Exact obstruction / honest limit

The mathematically strong content here is the **elementary one-ply unit-drop inequality** (Proposition 1), which settles the “drop by >=2?” subquestion negatively for all n. The remaining open content is the front’s asymptotic frequency question: is the set of `n` admitting *any* reachable optimal-play repair cofinite/infinite? My small-n data is `no,no,yes,yes` for n=4..7; n>=8 is uncomputed here. Settling “infinitely many n” would require an all-n construction of a reachable defective state on a height-`S(n)` play with an L-preserving optimal child — hard because optimal plays/`S(n)` are not explicitly characterized beyond small n. I make **no** theorem completion claim for S(n) or SORT-BOUND-U, no repo/Lean/test/CI/board change.

## Other metadata

```json
{
  "finished_at": 1795465008.0685534,
  "started_at": 1795463489.9926622
}
```
