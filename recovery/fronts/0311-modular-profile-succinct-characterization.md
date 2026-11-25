# modular-profile-succinct-characterization

## status

investigated

## origin

ai_proposal_unverified

## agent_id

0eU3lFmUD8Fgewq0jCBiAY-balls

## exit_state

clearexit

## question

For all n, does the exact minimax value S(n) admit a characterization by a polynomial-size system of modular/counting constraints on profile vectors of total extensions along every optimal comparison path, checkable without reconstructing the full comparison decision tree?

## basis

Antichain-split-coprime-obstruction studied root divisibility necessary conditions only; framed-certificate/state-compression docs focus on poset/DAG representations. No prior front targets an exact all-n modular profile characterization of S(n) itself.

## falsifier

Find n or an infinite family where any exact characterization of optimal root value requires constraints that distinguish superpolynomially many non-equivalent profile behaviors on root-optimal paths, or show a proposed modular system is unsound/incomplete against exact minimax.

## implication

A sound complete succinct modular/profile characterization could yield a new certificate form or evaluator for S(n); an all-n obstruction would limit counting-modular approaches that avoid explicit tree/DAG enumeration.

## finding_unverified

 `S(n)`. Even sound complete path constraints can still amount to an implicit encoding of a winning strategy unless a canonical polynomial quotient/normal form is proved.

### 3. Labeled positional profiles are highly discriminating but not proved sufficient; coarse counting is insufficient (experiment, small `n`, not a theorem)
Using the exact minimax model (`F(P)`, transitive closure over comparisons; `S(n)=F(A_n)`, checked to `S(4)=5`), enumerating all labeled strict partial orders (all reachable posets) gave:

| `n` | labeled posets `A001035(n)` | distinct labeled positional profiles `f_P(x,r)` | profile collisions with different `F` (labeled) |
|---|---:|---:|---:|
| 2 | 3 | 3 | 0 |
| 3 | 19 | 19 | 0 |
| 4 | 219 | 213 | 0 |
| 5 | 4231 | 4081 | 0 |

At `n=4,5`, all observed labeled-profile collisions were **isomorphic relabelings** (bucket size 2, `iso? True` in a sampled bucket), and no same-labeled-profile/different-`F` pair was found. This is **evidence, not proof**: it does not rule out nonisomorphic profile collisions or same-profile/different-`F` states at larger `n`, and it does not test pathwise modular constraint systems. It does confirm (consistently with `docs/research-state-compression.md`, reproduced: `P`/`Q` on 5 elements, `e=8`, different profiles and `F(P)=3,F(Q)=4`) that the coarse count `e(P)` alone is insufficient, while the full positional profile is much stronger.

### 4. Honest limit on the front as stated
I did **not** obtain a full all-`n` refutation of every possible modular/profile constraint system, because the front leaves “profile vector”, “modular/counting constraints”, and “checkable without reconstructing the full comparison decision tree” underspecified. I **did** obtain: (a) a rigorous incompleteness obstruction for the natural local modular/counting/divisibility subclass (extending exact-reset branch divisibility), and (b) a reduction of the fully general positive reading to an open succinct-certificate/NP-membership-style breakthrough subject to #P/checkability and completeness barriers. No independently checkable new theorem/counterexample beyond these deductions was established; I did not create Lean/repo artifacts.

## Failed / non-deciding attempts
- Searched repo/worktrees/board for prior “modular profile characterization”, “profile vector of total extensions”, and the named “antichain-split-coprime-obstruction” result; found only the front candidate and the related exact-reset branch-divisibility note.
- Exhaustive labeled-poset profile-vs-`F` scan for `n<=5`: no same-profile/different-`F` counterexample (useful negative evidence, not exhaustive over all profile notions/`n`).

## Concrete next falsification target
Fix a precise profile/constraint language, e.g. `\phi(P)= (e(P), (\Pr_P[x<y])_{x<y})` or the full rank matrix with polynomial witnesses, and test: (1) **incompleteness** — construct/infer two root-reachable states (or path prefixes) indistinguishable to that language but with different exact `F`; (2) **sound complete but tree-encoding** — show any complete `\Sigma_{n,k}` implicitly encodes a height-`k` strategy (a communication/strategy-certificate lower-bound argument); (3) **realizability** — extend the odd antichain-to-star branch-mass obstruction from a single reset to multi-step optimal antichain paths, proving a specific modular/counting family cannot certify root-optimal realizability. Any of (1)–(3) made all-`n` and rigorous would settle this front negatively in that class.

## Other metadata

```json
{
  "finished_at": 1793866821.6909814,
  "started_at": 1793866035.1936977
}
```
