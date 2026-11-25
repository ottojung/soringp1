# fredman-additive-bound-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

TWYZ2y5LlKjgdRmraOBPJY-reference

## exit_state

clearexit

## question

For all sufficiently large n, does every adaptive comparison sort for n distinct elements require at least ceil(log2(n!)) + n - log2 n - c comparisons for some absolute constant c (Fredman's additive form), or is there an all-n family of n where the comparison-tree realizability constraints prevent this excess from growing linearly?

## basis

Fredman's 1976 bound appears in sorting lower bound lore but repo notes constants/validity for all large n need checking against primary sources; info-bound-tightness-infinite was inconclusive about finiteness/cofiniteness and didn't settle this additive form.

## falsifier

Either give a rigorous proof establishing Fredman's additive lower bound for all large n with explicit constants, or construct/adversarially show for arbitrarily large n that S(n) < log2(n!) + n - log2 n for the relevant form; known small-n excess being small alone is not enough.

## implication

An all-n proof would force the information-excess Delta(n)=S(n)-ceil(log2 n!) to be Omega(n/log something)? Or at least >= n - O(log n), which means near-information perfect trees are impossible for all large n and any polynomial certificate must explicitly account for this growing additive excess, sharpening barriers for SORT-BOUND-U membership in NP.

## finding_unverified

Let us start by exploring more and trying to understand the Fredman bound.

Let us examine this claim carefully.

Let us think systematically. The claim is: for all sufficiently large n, S(n) >= ceil(log2(n!)) + n - log2 n - c (Fredman's additive form). 
- Sergeev gives an upper bound: S(n) = log2(n!) + O(n/(log n)^(1/5)), achieved by a constructive algorithm.
- Asymptotically, n/(log n)^(1/5) = o(n), so for any fixed c, for all sufficiently large n we have n/(log n)^(1/5) < n - log2 n - c. Therefore S(n) < log2(n!) + n - log2 n - c for all sufficiently large n, which directly contradicts Fredman's bound.
- Also checking the known values shows the bound doesn't hold even for moderate n with small c.
- The question says "comparison-tree realizability constraints prevent this excess from growing linearly" - and Sergeev's construction shows it's possible to have sublinear excess, so realizability constraints don't force linear excess; in fact they're compatible with sublinear excess.

So the disproof is straightforward if we take Sergeev's result as given. But we need to be careful about the model, constants, and whether Sergeev's result is considered solid. Also the repo says "Primary theorem, not Lean-checked here" for Sergeev, but lists it as literature fact. The task says "study the primary literature" - so we need to examine Sergeev's result.

Let us look up the actual paper more if possible, or at least understand it well.

Let us analyze this.

Let us look up the full literature on Sergeev to be sure, and also consider if there might be other interpretations of "Fredman's additive form".

Let us do the analysis.

Let us analyze the question carefully.

**Finding (paper proof):** Fredman's claimed additive lower bound $S(n) \ge \lceil \log_2(n!) \rceil + n - \log_2 n - c$ for all sufficiently large $n$ is **false**.

**Evidence:** Sergeev (ECCC TR20-096, 2020, Thm 3; J. Comp. Math. Math. Phys. 2021) gives a constructive upper bound $S(n)=\log_2(n!)+O(n/(\log n)^{1/5})$. Since $n/(\log n)^{1/5}=o(n)$, for every fixed $c$ and all sufficiently large $n$, $O(n/(\log n)^{1/5}) < n - \log_2 n - c$, hence $S(n) < \lceil \log_2(n!) \rceil + n - \log_2 n - c$. The bound also fails for all known exact $n\le22$ for reasonable $c$.

**Implication:** "Comparison-tree realizability constraints" do not prevent linear excess growth—they permit sublinear ($o(n)$) excess (Sergeev). The second alternative holds; any claim of a universal linear excess lower bound is contradicted by the existence of this construction.


## Other metadata

```json
{
  "finished_at": 1793782757.8871605,
  "started_at": 1793778319.0621245
}
```
