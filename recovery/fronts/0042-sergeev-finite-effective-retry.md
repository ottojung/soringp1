# sergeev-finite-effective-retry

## status

investigated

## origin

executive_manual_dispatch

## agent_id

eEqpimW1UfsnmxHUjvwl6C-baggage

## exit_state

clearexit

## question

Can we extract an effective finite form of Sergeev's S(n)-log2(n!) = O(n/(log n)^(1/5)) bound (with explicit constants/thresholds for large n) sufficient to rule out candidate (n,k) pairs or to bound the search window for exact S(n)?

## basis

Sergeev's asymptotic bound; earlier blocked attempt sergeev-effective-finite-bound showed optimization over group sizes but needed explicit parameter schedule.

## falsifier

Show that for all effective parameter choices the resulting bound is either vacuous or exceeds known S(n) values, or that optimizing parameters requires uncomputable functions of n.

## implication

An effective finite form would turn an asymptotic excess bound into a practical window reduction for computing exact S(n) and sharpen barrier arguments.

## finding_unverified

\lceil \log_2(n!) \rceil + C_{eff}(n)$ is false? No, to rule out a particular k as sufficient you need $S(n) > k$. The excess bound goes the other way (upper bounds $S(n)$). So the direction is: effective finite upper bound on $S(n)$ shrinks the upper end of the search window (tells you k doesn't need to be larger than B_eff(n)). That is useful for algorithms computing exact $S(n)$ by search, but "ruling out candidate pairs" is phrased oddly; more directly it bounds the window. The falsifier's first part "vacuous or exceeds known S(n) values" is the real obstruction.
4. **"Uncomputable functions of n"?** Unlikely. The parameter is integer-valued, argmin over a finite range at each level - computable by a simple function of n (maybe dynamic programming to choose block sizes, or closed form approximation rounded). The obstruction is not uncomputability, it's that the optimal schedule is not written down and extracting explicit constants is error-prone; calling it "uncomputable" is imprecise. A better obstruction is: the proof is non-constructive in parameter choice or requires solving implicit equations with unknown constants.

**Concrete failed approach (attempted in principle):** Try to extract from the group-insertion structure. Let block size be $t$ (growing), form groups of $t$, sort groups recursively (cost), then merge by insertion/find positions using information-theoretic comparisons (each comparison gives ~1 bit but with bias analysis). The excess comes from comparisons with non-uniform bias. To make finite, you need: explicit $t(n)$, explicit level count, explicit constants in $h_2^{-1}$ approximations, explicit merging costs. The blocked attempt hit exactly this - optimization gave a schedule but constants/thresholds missing. Any naive explicit choice makes the bound worse than FJ for moderate n. A globally optimal explicit schedule is not derivable from the text as-is.

**Barriers / limits:**
- **General-poset vs $S(n)$:** This is specific to total orders (permutations) and the information-theoretic structure of comparisons; not transferable from arbitrary partial orders. The entropy identity is specific to sorting decision trees.
- **Soundness vs completeness:** An effective finite upper bound would be sound (proves $S(n) \le B_{eff}(n)$). It gives no completeness for NP, no lower bound, and is not a certificate. It also doesn't address the sparsity/Mahaney barrier or $P\ vs\ NP\ vs\ PSPACE$ directly.
- **No bridge to complexity class separation:** Even if extracted, it's still an upper bound on the tree height (constructive) - doesn't create a polynomial-time evaluator unless combined with other things. The complexity implication stated is about window reduction for computing exact $S(n)$, which is plausible if bound is good, but obstructed.

**Honest verdict:** The claim is **falsifiable in practice** and **disproved as stated** for "sufficient to rule out candidate $(n,k)$ pairs or to bound the search window for exact $S(n)$" with currently available proof. The mathematical obstruction is: no explicit parameter schedule + explicit constants exist in the literature/proof; any effective extraction gives either vacuous bounds exceeding known $S(n)$ or worse than explicit bounds like Ford–Johnson on the relevant range. The "uncomputable functions of n" part is not the right obstruction - it's non-constructive parameter choice + constant bookkeeping. No new repository change is warranted; this is a negative result/obstruction.

## Other metadata

```json
{
  "finished_at": 1793342357.4512827,
  "started_at": 1793342217.1561887
}
```
