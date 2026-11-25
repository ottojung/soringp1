# sergeev-band-widening-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

kGFmrCsLXSlhXZPLSRkPDL-femur

## exit_state

clearexit

## question

If the Ford-Johnson upper bound F(m)=log2(m!)+c*m+o(m) in the information-plus-upper-bound sufficient condition ceil(log2(n!)) >= U(a)+U(b)+a+1 is replaced by Sergeev's constructive sublinear-surplus bound U(m)=log2(m!)+O(m/(log m)^{1/5}), does the set of certified splits strictly widen from the linear threshold a>=0.017n to a sublinear threshold a>=omega(n/(log n)^{1/5}) for all sufficiently large n?

## basis

Board #301 certifiable-band scope (FJ surplus c=1/ln2-4/3 approx 0.10936, threshold t(n) approx 0.0174n, dyadic sawtooth) and Sergeev ECCC TR20-096 sublinear surplus; at constant fractions H(eps)>eps, so the widening is plausible and to be tested, not established here.

## falsifier

Prove the Sergeev-substituted condition still fails at some split a=omega(n/(log n)^{1/5}) for infinitely many n, or exhibit a Ford-Johnson-certifiable split that fails under U, refuting any widening.

## implication

Determines whether a known improvement in sorting upper bounds widens the information-theoretic certification route to the antichain defect inequality, bridging an upper-bound gain to a structural lower bound for S(n) without any class separation.

## finding_unverified

y no post exists under this exact tag once more, then make the single board post (the project's required reporting mechanism; no repo/Lean changes).
The comment command returned the updated issue object. Let me verify the post actually landed under the tag.
Post confirmed (one write, 19:24:17Z). Final state check.
## Result

Work done on `billy-dev` only. Recovery audit first: branch `billy-dev` clean at `6a96398`, stash empty, no worktrees, ledger front `sergeev-band-widening-alln` was `running` with no finding, and #301 had **zero** posts under this tag — so nothing from the interrupted turn was duplicated. I made exactly one external write: a result post to #301 (19:24:17Z). No Lean, repo, test, CI, or ledger changes.

### The all‑n claim is TRUE; both falsifier horns fail (paper proof)

With `U(m)=log₂(m!)+E(m)`, `E(m)≤K·m/(log m)^{1/5}` (Sergeev ECCC TR20‑096 Thm 3; constant ineffective), the substituted condition `P_U` is equivalent (up to O(1) ceiling slack) to

`log₂ C(n,a) > a + E(a) + E(b)`,  `b = n−a`.

- **Horn (b) fails:** for any `a = ω(n/(log n)^{1/5})`, `E(b)=O(n/(log n)^{1/5})=o(a)` and `E(a)=o(a)`, so the RHS is `(1+o(1))a`. The LHS is `≥ a·log₂(n/a)=ω(a)` when `a=o(n)`, and `≥ nH(a/n)−O(log n) ≥ (2−o(1))a` at constant fractions, using `H(ε)≥2ε` on `[0,½]`. **Hence every such split is certified for all large n.**
- **Horn (a) fails:** since `E(m)=o(m)` while the Ford–Johnson surplus `Δ(m)≥0.02724m`, we have `U≤F` for large m (patch small m). Taking `U'=min(F,U)` keeps a valid upper bound, so `P_F ⇒ P_U'` — **no FJ‑certifiable split is lost**.

The mechanism is exactly the one anticipated in the basis: FJ's linear surplus needs `H(ε)−ε > D≈0.1137` (ε≳0.01835), whereas Sergeev's sublinear surplus only needs `H(ε)−ε>0`, which holds for **every** ε∈(0,½).

### Sharper threshold

The true U‑threshold is `Θ(n / ((log n)^{1/5}·log log n))` — the front's "ω(n/(log n)^{1/5})" is true but off by one log‑log factor. Scratch checks: with a model constant K=0.1 the minimal certified fraction drops 0.0090→0.0075 (n=10⁴→10⁸), below FJ's 0.0174; K=1 is nonempty only past ~10⁷ and decays 0.292→0.062 (10⁷→10³⁰⁰), consistent with log‑log decay.

### Honest limits (explicitly separated in the post)

- **Soundness ≠ completeness:** `P_U` is sufficient only. Widening it widens this method's reach, not the set of splits where the defect inequality is actually true.
- **General‑poset results not used or transferred:** D, T1/T2, refinement counterexamples, framed‑DAG soundness are untouched; this is purely the antichain‑root sequence plus published upper bounds.
- **No improved numerical bound:** the recursive `L(n)` (reproduced `L(1000)=5443`) attains its max at a *constant* fraction `a/n≈0.48`, already inside the FJ band — so the extra sublinear splits add no maximizer and don't strengthen the lower bound on `S(n)`.
- **Ineffective constants:** "sufficiently large n" depends on Sergeev's hidden K (for K=1, the U fraction falls below FJ's only near 10¹⁷⁵). An effective all‑n version needs explicit constants from the group‑insertion proof.
- **No complexity consequence:** no faster evaluator, no class placement; `SORT‑BOUND‑U` stays in PSPACE, `S(n)` open beyond n=22. "P false" is not a counterexample to the defect inequality.

I tried to disprove the claim (both horns, plus an exhaustive check of the inequality `H(ε)>ε`, the ceiling slack, and small‑m patching) and found no obstruction; the finding is a method‑scope theorem, not a completion.

## Other metadata

```json
{
  "finished_at": 1795289090.5045304,
  "started_at": 1795288258.4650176
}
```
