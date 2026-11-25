# divisible-split-obstruction-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

jZDy5LPX0jIWaQZfA0siVC-seventeen

## exit_state

clearexit

## question

For the n-element antichain, is there an infinite family of n where every comparison strategy that first achieves the information-theoretic split ratio consistent with some depth-S(n) path produces a subsequent state partition whose linear-extension counts are not all powers-of-two compatible, forcing total height > ceil(log2(n!)) for those n?

## basis

Exact-reset realizability showed odd-ratio/partition obstructions for specific boundary families; generalize to first-split/divisibility for the antichain root against all-n strategies.

## falsifier

Construct for all sufficiently large n a deterministic adaptive strategy achieving height ceil(log2(n!)) via a comparison tree whose every node's child branches have numbers of linear extensions whose binary/partition structure is exactly realizable by some comparison, or prove no such universal divisibility obstruction exists.

## implication

A general all-n divisibility obstruction would explain why S(n) > C(n) infinitely often and constrain the shape of optimal decision trees without relying on local poset hardness transfer from arbitrary partial orders.

## finding_unverified

 one-ply/information-budget sense — matching exact-reset’s “partition realizability/divisibility” language. The evidence points to branch/divisibility obstructions like the odd-n antichain→star reset (a *transition*-specific obstruction), to be generalized to the *full sorting tree of minimum height*.

### What the literature/repo shows
- **Tightness is irregular, not universal.** C(n)=⌈log₂(n!)⌉ is achieved at n≤11 and again at n=20,21 despite n! not a power of two; missed at 12,16,17,18,... (Stober–Weiss/Jing et al.). No known result forces gaps for all large n or for an infinite arithmetic family.
- **Balanced splits are natural but not the only option.** Root antichain forces 50-50; from there balanced comparisons (equal chains/merge-like) are info-theoretically best, but unbalanced splits remain possible in many cases unless budget forces otherwise (some n forbid unbalanced at first step yet are still tight/wide). The obstruction is not “balanced split exists” but whether *any* strategy achieves height C(n).
- **One-ply is necessary but weak.** L1> L0 gives a genuine obstruction at a node (some child exceeds 2^(r-1) for every comparison), but it’s sporadic (smallest witness n=5) and doesn’t obviously propagate to force > C(n) on an infinite family of antichains regardless of strategy choice. Higher-order/structural obstructions (n=12) are global and found by search, not a simple recursive divisibility forcing every balanced path to fail.
- **Comparison constraints vs general tests.** Hyafil–Rivest/Laber–Nogueira/Parberry don’t transfer to fixed pairwise basis for S(n) (certificates/soundness vs completeness distinguished). The winning frontier shows exponential state blowup but is an enumeration barrier, not a proof of class separation or that C(n) is unachievable.

### Attempt to disprove / honest limits
- **Counterexamples exist.** n=20,21 achieve C(n) with n! not power of two → no “n! not power of two => obstruction” all-n rule.
- **Transition-specificity.** Exact-reset’s odd-n obstruction is strong for that fixed target (V_n); the sorting tree wants to reach *any* total order within budget (much more flexible). Lifting that exact divisibility to “every strategy achieves height C(n)” is non-obvious and fails in known tight cases.
- **Asymptotics cut both ways.** Sergeev gives S(n)=log₂(n!)+o(n); C(n)-log₂(n!) < 1, so excess S(n)-C(n) is o(n) integer — compatible with 0 sometimes, 1 sometimes, or growing slowly, but no theorem forces it to be ≥1 on an infinite family for all balanced strategies.
- **No constructive obstruction found.** Tracing balanced merge-like paths hits budget constraints only in known non-tight n; I see no general modular/divisibility invariant forcing failure for all strategies on an infinite family.

**Conclusion:** I find no evidence supporting the claim as stated. The natural generalization of exact-reset (transition divisibility) does not lift cleanly to a universal all-n obstruction for achieving minimum height C(n) on the antichain; tight cases recur (20,21), obstructions appear sporadically (12,16,17,18), and the falsifier’s “construct for all sufficiently large n a strategy achieving height C(n)” is not obviously false. A rigorous proof of “infinitely many gaps forced by this obstruction” or a disproof “all sufficiently large n achieve C(n)” both appear beyond current known results — I report honest limits rather than a theorem. No repository changes or Lean additions are warranted by this analysis.

## Other metadata

```json
{
  "finished_at": 1793652789.4033055,
  "started_at": 1793647382.3288784
}
```
