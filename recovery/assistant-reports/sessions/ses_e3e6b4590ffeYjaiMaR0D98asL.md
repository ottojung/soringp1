# antonina-9iV8kegSKg3qxfPDIZb7XW-pike

Session: ses_e3e6b4590ffeYjaiMaR0D98asL
Workspace: /home/lubko/soring-fronts/one-coordinate-kwl-move-quotient
Created: 1794249112416; updated: 1794255522936

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 652 (msg_1c1f64e950015QnCZKi7ypMAAJ)

**Front `one-coordinate-kwl-move-quotient` — report**

**Verdict:** the standard one-coordinate hierarchy is **definitively refuted at `k=2`** by an explicit same-poset witness, but for `k>=3` I found neither an all-`n` counterexample nor a finite-`k` definability proof. The first open case is `k=3`. I posted one concise update to board #301 at `2026-11-09T20:18:15Z`; the repository worktree remains clean at `6a96398`, with no Lean or repo changes. All scratch work is under `/tmp/opencode/kwl3`.

**1. Concrete `k=2` counterexample [experiment + paper-checkable certificate].**
For the standard separate-coordinate two-WL (initial colour = atomic `<,>,=,||` type; update by replacing one coordinate at a time), take

`P = (0,0,1,1,5,9,7,11)`

with row `i` the successor bitmask. Exact minimax gives `F(P)=9`. The four incomparable pairs

`(4,6), (4,7), (5,6), (5,7)`

all have the **same unordered stable 2-WL pair colour**, but their exact move values are

`T(4,6)=9, T(4,7)=8, T(5,6)=8, T(5,7)=9`.

So equal stable two-WL colour does not determine `T`. This is independent of the earlier `n=8` witness `(0,0,0,0,0,1,7,25)` and is a direct same-poset falsifier. The earlier folklore scan found no such collision through `n=7`, so `n=8` is the first possible size.

**2. `k=3` finite status [experiment, not theorem].**
- Exhaustive over all `16,999` unlabeled 8-element posets: I computed the standard one-coordinate stable 3-WL colour of every triple. For every same-colour class of incomparable pairs I compared the two oriented children by `(in,out)`-degree signature. **Zero** classes contained children with different signatures — no non-automorphic candidate even at that coarse level.
- On the first `3,000` of those posets I computed exact `T` for every nontrivial same-colour class: **zero** collisions. The full exact-`T` sweep of all `16,999` was not completed.
- Random general posets at `n=9,10,11,12` (several densities) and random height-two posets through `n=12` gave zero same-colour classes with non-isomorphic oriented children.
- A partial cross-poset check found no shared 3-WL pair term among the first `11,000` of the `16,999` `n=8` posets.

These are **soundness observations**, not completeness: they show no detected failure of “equal colour ⇒ equal `T`” on the tested range. They do not show the colour separates all distinct moves, and finite absence of a counterexample is not an all-`n` bound.

**3. Exact obstruction to the obvious all-`k` proof [literature + deduction].**
Cai–Fürer–Immerman (*Combinatorica* 12 (1992) 389–410) gives, for every fixed `k`, non-isomorphic `k`-WL-equivalent structures (incidence posets of CFI graphs). Hence the sufficient mechanism “same pair colour implies isomorphic children” fails for every fixed `k`, and cannot prove a uniform finite-`k` bound. It does **not** refute `T`-soundness: CFI controls isomorphism, while `T` is a numeric minimax value. To refute fixed `k` one needs two `k`-WL-equivalent *pointed* posets `(P,x,y)`, `(Q,x',y')` with different `max(F(P+x<y),F(P+y<x))`. No such pair is known for `k>=3`. Conversely, a positive fixed-`k` theorem must establish an arithmetic coincidence of child `F`-values across colour classes, not child isomorphism.

**4. General-poset hardness does not transfer [literature + deduction].**
Hyafil–Rivest (1976) is NP-completeness for arbitrary subset tests, not pairwise comparisons; Cardinal et al. give constant-factor approximation to `log e(P)`, not exact `F`; counting linear extensions is #P-hard, but `F` is not a function of `e(P)` (the repo’s `n=5`, `e=8`, `F=3` vs `4` pair). Exact `GEN-SORT` hardness remains open. None of these turns a fixed `k` into a contradiction.

**5. Certificate/complexity distinction.**
A fixed `k` plus an effective, uniformly defined polynomial-time map from colour (and `n`) to `T` would put `S_unary` in FP: build the antichain `A_n`, compute its single pair colour, return `T+1`. That would be a major open positive result. A colour label alone is not an algorithm, and a sound **move** quotient still needs a sound **state** quotient with an equivariant successor transition. So “fixed `k` gives a polynomial-time sound move quotient” is false as written unless the colour-to-value map and state transition are supplied.

**6. Honest limits.**
`k=2` is refuted; `k=3` is open. Our `n=9` exhaustive attempts were killed by memory/time, so the decisive next test remains an optimized exhaustive `n=9` (then `n=10`) standard 3-WL search over all unlabeled posets, comparing oriented-child isomorphism or exact `T` on every same-colour class. No claim is made that the required `k` is unbounded, and no new `S(n)` or `SORT-BOUND-U` consequence follows.
