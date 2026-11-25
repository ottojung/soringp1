# effective-sergeev-threshold

## status

investigated

## origin

ai_proposal_unverified

## agent_id

gCaCFAuo9EHXfx8jIiwcz3-repairs

## exit_state

clearexit

## question

Can Sergeev's o(n) excess bound be made fully effective, giving explicit constants c and N0 such that S(n) <= ceil(log2(n!)) + c n / (log n)^(1/5) for every n >= N0 with a complete derivation?

## basis

Sergeev's group-insertion result is summarized in docs/research-sergeev-asymptotic.md and listed as the open bound-gap question in docs/research-plan.md; Ford-Johnson gives only linear excess, and neither the repository nor the prior additive-approximation finding records an effective constant, an explicit N0, or a finite-threshold derivation.

## falsifier

Show that the published argument yields only a nonconstructive o(n) statement, or exhibit an explicit n with a certified lower bound S(n) exceeding every proposed effective right-hand side.

## implication

An effective bound would replace the asymptotic threshold window by a finite verifiable one, improve explicit upper bounds if c beats Ford-Johnson's linear excess, and sharpen the search range for exact S(n); failure would show the known asymptotic method gives no algorithmic leverage on exact evaluation.

## finding_unverified

nge `100≤a<2^{47.5}` is absorbed the same way. Theorem 2′ makes this explicit.
- **Second falsifier “explicit `n` with certified `S(n)` exceeding every proposed RHS”**: not achievable with current knowledge. The only general certified lower bound is `S(n)≥⌈log₂(n!)⌉`, and the proposed RHS exceeds it by `c n/(\log n)^{1/5}`. For `n≤22` the exact values satisfy `S(n)−⌈log₂n!⌉≤1` (`S(12)=30`, `C(12)=29`; `S(22)=71`, `C(22)=70`), while the RHS is enormous. No certified lower bound above the information bound exists for any larger `n`. So this falsifier cannot be realized; it is not evidence for the claim, only a limit of current lower-bound technology.
- **[experiment]** The known values `S(n)` for `n≤22` are consistent with the effective RHS and cannot distinguish it from Ford–Johnson.

Thus the mathematical existence claim is **not disproved**. What fails is the complexity interpretation.

---

## 6. Soundness versus completeness; general posets

**[deduction]**

- **Soundness.** An explicit upper bound `U(n)` plus the constructive group-insertion algorithm gives a uniform, polynomial-time checkable certificate that `S(n)≤k` for every `k≥U(n)`. The algorithm’s schedule is succinct; one need not exhibit the exponentially large comparison tree. This is a genuine **sound** “yes” certificate for the high side of `SORT-BOUND-U`.
- **Completeness.** It gives no certificate that `S(n)>k`, no lower bound beyond `⌈log₂n!⌉`, and no proof that `U(n)` is optimal. An optimal sorting tree may have exponentially many nodes, so this is not an NP certificate. The exact-search window `[⌈log₂n!⌉, U(n)]` still contains `Θ(n/(\log n)^{1/5})` integers; asymptotically this is still `O(n)`, not a smaller complexity class. The bound changes a constant, not the algorithmic problem.
- **General posets.** Sergeev’s theorem is about the fixed antichain `A_n` / sorting `n` totally ordered keys. The group-insertion strategy relies on the principal chain being totally ordered and on the pair structure; it does not bound the minimax value `F(P)` of an arbitrary poset. General-poset hardness or certificate results do not transfer to `S(n)` without an encoding-preserving reduction.

---

## 7. Honest limits and next question

1. **The positive result is in principle, not optimized.** Theorem 2′ is explicit, but the recurrence’s constant tracking is sketched, not fully audited. The pair `(c,N0)=(10^{30},2^{2^{200}})` is conservative.
2. **The negative result is robust.** No matter how the constants are optimized within this route, Lemma 4’s `s≥20` forces `N0≥2^{2^{47.5}}` for `γ=1/5`, and `N0>2^{2^{19}}` even with optimal `γ<1/2`. This is far beyond any `n` where exact `S(n)` is known or computable.
3. **The decisive open task** is a small-`s` Lemma 4 (`s=1,…,19`), or a different group strategy that avoids the `s≥20` threshold. If such a lemma exists with `s=1` and an explicit error, the threshold could drop to a small finite value, and the Sergeev method might genuinely sharpen explicit upper bounds. The paper itself hints that an `s=1`, depth-6 simplification is possible, but does not supply the explicit strategy or its constants.
4. **No claim is made** that the asymptotic theorem is false, that `S(n)` is hard, or that the group-insertion algorithm is ineffective. The finding is narrower: the published method can be made effective, but the effective bound is algorithmically vacuous, and it is an upper-bound soundness result, not a completeness or exact-evaluation result.

## Other metadata

```json
{
  "finished_at": 1794130924.2845073,
  "started_at": 1794129976.8384562
}
```
