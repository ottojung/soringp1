# antonina-i8pfGFOTTFiA6T1nJrkDo4-fingering

Session: ses_e47b085ddffes2kIih32s4g3fc
Workspace: /home/lubko/soring-fronts/fence-core-uniqueness
Created: 1794093578866; updated: 1794095816822

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 396 (msg_1b87185f30015wibrMrhI09pWi)

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
