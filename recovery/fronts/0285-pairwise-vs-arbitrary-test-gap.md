# pairwise-vs-arbitrary-test-gap

## status

investigated

## origin

ai_proposal_unverified

## agent_id

lLM0j1WzJjEje5Wv4rN2Hy-manned

## exit_state

clearexit

## question

Does the restriction to pairwise comparisons (the sorting test class) create an all-n exponential gap between the height of an optimal adaptive tree for pairwise tests and the information-theoretic/abstract test lower bound in a sense that is not explained by the standard log2(n!) bound, or is the pairwise restriction exactly captured by the minimax game with no additional all-n complexity barrier beyond the known bounds?

## basis

Hyafil–Rivest/Laber–Nogueira concern arbitrary tests and construction/hardness of tree optimization, while S(n) is the height for the fixed pairwise test class; model separation must not be conflated with certificate soundness/completeness or with general partial-order hardness.

## falsifier

Construct for all sufficiently large n an infinite family of comparison problems (derivable from the antichain/S(n) game) where every adaptive strategy using only pairwise comparisons requires height >= c * S(n) * f(n) with f(n)->infty while there exists an abstract test family (or show a general lower bound technique) that would suggest smaller height, or alternatively prove equality up to lower-order terms for all n.

## implication

A genuine pairwise-vs-arbitrary gap would identify a model-specific barrier for S(n) distinct from general decision-tree NP-hardness; demonstrating no such gap (beyond log2(n!)) would clarify that the difficulty is the minimax/adversarial structure rather than test-class restriction alone.

## finding_unverified

ormation-theoretic lower bound is `⌈log_t M⌉`. With arbitrary yes/no tests (Hyafil–Rivest style, free subset tests) one can approach/achieve the information bound for sorting-like identification by querying arbitrary predicates; with only pairwise order queries the test family is restricted to `{(i<j)?}`.
- `S(n)` is the height for the restricted (pairwise) adaptive test class. The leaf-counting/information bound gives `S(n) >= ⎡log2(n!)⎤ =: C(n)`. Tight for `n≤11,20,21`; for others `S(n) > C(n)` (e.g. `n=12: 30>29`).

**Why no exponential gap:**
- The excess is sublinear relative to the main term: Sergeev (ECCC TR20-096, 2021) shows `S(n)=log2(n!)+O(n/(log n)^(1/5)) = Θ(n log n)`, so `(S(n)-C(n))/n → 0` and `S(n)/C(n) → 1` as `n→∞`. No exponential blowup for any infinite family derivable from the antichain/S(n) game; the ratio is asymptotically 1.
- The pairwise restriction is exactly captured by the minimax (poset) recurrence `F(P)=1 + min_{incomparable (i,j)} max(F(P+(i<j)), F(P+(j<i)))`, `F(antichain)=S(n)`. The gap beyond `log2(n!)` arises from combinatorial constraints of this game (e.g. unbalanced splits / local obstructions like the one-ply `L1>L0` on some posets), not from an uncaptured “extra” barrier.
- “Abstract test lower bound” here is best read as the information-theoretic bound achievable by more powerful tests; the pairwise class cannot reach it in general but approaches it asymptotically with only sublinear excess. One cannot construct an infinite family with `S_{pairwise}(n) >= c*S(n)*f(n)`, `f(n)→∞` while abstract tests do exponentially better — abstract tests are easier (logarithmic in possibilities), pairwise are Θ(n log n); the relevant ratio is bounded above in the limit and the obstruction is combinatorial/game-theoretic.

**Distinctions (as required):**
- **General-poset results vs antichain/S(n):** hardness/approximation for arbitrary posets or arbitrary tests (Hyafil–Rivest, Laber–Nogueira, Cardinal et al. constant-factor approximation to `log e(P)`) do not transfer to exact `S(n)` on the antichain without a reduction; the question concerns the test class on the sorting (antichain/minimax) game specifically.
- **Certificate soundness vs completeness:** framed certificates are sound and polynomially checkable, but no all-n polynomial-size completeness theorem is known for exact optimal height; Parberry’s coNP-completeness is for sorting-network *verification* (different object). This is orthogonal to the height-gap question above.

**Concrete failed approach / obstruction:** trying to get exponential gap fails because (1) information bound is shared form but restriction is captured by minimax (no model leakage), (2) asymptotics force ratio→1 (Sergeev), (3) known obstructions are local/combinatorial (one-ply) giving constant/additive gaps in that refinement, not exponential in n for the full game height. No counterexample family exists; the most plausible falsification is ruled out by asymptotics + exact model capture.

**Honest limits:** exact values remain open for large n; `S(n)` computation complexity is separate from tree height; we cannot rule out some exotic “abstract test lower bound technique” not obviously information-theoretic, but under standard combinatorial search theory (information theory + decision tree complexity with restricted tests) no exponential gap is supported. The frontier reduces to the minimax/adversarial structure of pairwise tests, not to a pairwise-vs-arbitrary test class barrier.

## Other metadata

```json
{
  "finished_at": 1793801317.1652746,
  "started_at": 1793799606.9900663
}
```
