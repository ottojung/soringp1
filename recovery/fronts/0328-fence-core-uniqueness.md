# fence-core-uniqueness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

i8pfGFOTTFiA6T1nJrkDo4-fingering

## exit_state

clearexit

## question

For every r >= 1, is the fence poset P_{r+1} the unique core poset (no element comparable to all others) with exact minimax depth m(P)=r and exactly F_{r+2} linear extensions, up to isomorphism?

## basis

Newest board #301 extension-threshold conjecture T(r)=F_{r+3}-1 with fence e=F_{n+1}, m=n-1; docs/research-budget-pruning.md and docs/research-obstruction-next.md; independent connected-core census check that all 21 e=21, m=6 representations are fence-isomorphic, plus the finite T(4)=12 and T(5)=20 data.

## falsifier

Exhibit a core poset P with m(P)=r and e(P)=F_{r+2} that is not isomorphic to the fence P_{r+1} for some r, starting with r=6.

## implication

Uniqueness would make the fence the canonical extremal family for the extension threshold T(r)=F_{r+3}-1, transferring fence-specific certificate and evaluator lower bounds to every threshold extremal; it would be a structural theorem, not a P/PSPACE separation.

## finding_unverified

## Finding

The all-`r` fence-core uniqueness claim is **false**, and it already fails at **`r = 3`**, not at `r = 6`.

**Counterexample (`paper proof`).** Let  
`P = C₄ ⊔ K₁`, a 4-chain `0<1<2<3` together with an isolated element `x`.

- `e(P) = 5 = F₅ = F_{3+2}`: `x` can be inserted into any of the 5 chain positions.
- `m(P) = 3`: the information bound gives `m ≥ ⌈log₂ 5⌉ = 3`, and binary insertion of `x` into the sorted 4-chain uses 3 comparisons.
- `P` is a core: `x` is incomparable with every chain element; each chain element is incomparable with `x`; hence no element is comparable with all others.
- `P` is not isomorphic to the fence `P_{r+1} = P₄`, since `P` has 5 elements and `P₄` has 4.

So the claimed uniqueness is false for `r = 3`. This is exactly the already-known sharp core witness `C_{n-1} ⊔ {isolated}` with `e = n`, now colliding at `n = 5` with the fence’s `(m,e) = (3,5)`.

## The requested `r = 6` range

No `r = 6` falsifier exists in the full core census. An independent all-poset enumeration by maximal insertion with extension cap `e ≤ 21` and `n ≤ 21` found exactly 21 representations of `(e,m) = (21,6)`, all on 7 elements. Canonicalisation gives exactly **one** isomorphism class, the fence `P₇` (`pred = [0,0,1,3,7,15,31]`). Thus the failure starts at `r = 3`, not at `r = 6`.

Finite wider check: the core-only generator through `e ≤ 89` found no further non-fence `(m,e) = (r,F_{r+2})` for `r = 4..9`. That is finite evidence only, since the generator’s completeness lemma is a separate structural lemma.

## Honest limits

- This is a **general-poset structural non-uniqueness** result, not a complexity-class separation.
- It does **not** refute the threshold conjecture `T(r) = F_{r+3}-1`: the counterexample still has `m = r` and `e = F_{r+2}`, so it is a second equality witness, not a threshold violation.
- It does invalidate the proposed transfer of fence-specific structural lower bounds to *every* threshold-extremal poset via uniqueness. It says nothing against certificate **soundness**; it refutes a completeness/uniqueness bridge.
- If the front is silently restricted to **connected** cores, the disconnected witness `C₄ ⊔ K₁` is excluded. Connected uniqueness for all `r` remains open; the finite connected/core censuses through `r = 6` agree with the fence.

I posted this finding to board #301 as `SoringP1 frontier: fence-core-uniqueness`. No repository or Lean changes were made; the worktree is clean at `6a96398`.

## Other metadata

```json
{
  "finished_at": 1794095835.0001905,
  "started_at": 1794093578.4218998
}
```
