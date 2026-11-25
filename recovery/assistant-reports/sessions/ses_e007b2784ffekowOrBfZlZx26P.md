# antonina-kGFmrCsLXSlhXZPLSRkPDL-femur

Session: ses_e007b2784ffekowOrBfZlZx26P
Workspace: /home/lubko/soring-fronts/sergeev-band-widening-alln
Created: 1795288258700; updated: 1795289086698

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_1ff8c48c2001mKGHPVXp4nS1LP)

I'll start by inspecting the environment carefully, since the recovery note warns not to repeat side effects. Let me gather state in parallel.

## Output 28 (msg_1ff8c5ae2001jG0pmi8NuLvspA)

Host is `billy-dev`, branch `billy-dev`, clean tree. Let me inspect durable records and prior-work traces before doing anything.

## Output 51 (msg_1ff8c6f3b001ZdelC9PXGShw8D)

Let me check the durable frontier ledger and the board digest to see whether a prior turn already claimed this front or posted anything.

## Output 66 (msg_1ff8c8e6e0016WMAMPUu3mSzhT)

This front is clearly live on #301. Before any action, I must check whether a prior turn already posted a result for this exact front. Let me search the ledger and board.

## Output 81 (msg_1ff8cbbdf001U1zFCZ3Aq87fp4)

No board post exists yet under this front's tag. Let me read this front's ledger entry and the related dispatch/foundational posts in full.

## Output 101 (msg_1ff8cdc300015cnOmnnTDv3yon)

Front is claimed (`running`, no finding yet) — I'll continue it, not re-claim or re-post. Now let me study the core documents in depth.

## Output 124 (msg_1ff8cf000001xJ8bfUYJuKsEze)

Let me read the full text of the key board posts — the dispatch, the certifiable-band result, and the referee disposition — using the board script's options.

## Output 162 (msg_1ff8d52580014XxzOnlwfjN432)

Now I understand the framework. Let me locate the exact derivation of the sufficient condition P and the defect inequality it certifies, to make sure the substitution is legitimate.

## Output 200 (msg_1ff8e4137001HkIL5Ww47w6Gwl)

I now have the full framework. Let me verify the primary source (Sergeev ECCC TR20-096) and run discriminating scratch computations in parallel.

## Output 215 (msg_1ff8f3fed001ffu9VOlFgjZB5c)

The primary source confirms `log₂(n!) + o(n)` with an ineffective constant. My first numeric probe was confounded by non-monotonicity near n/2; let me redo with careful scans and also examine the recursive bound L's argmax (the key caveat).

## Output 244 (msg_1ff8fb299001J7QwGnx17LHXEq)

Let me finalize the computations with the corrected L base case and check how to post to the board.

## Output 255 (msg_1ff90235a001DYqbSxuT62qm5O)

All checks line up (L(1000)=5443 matches the board; argmax ≈ 0.48n inside the FJ band). Let me find the exact board-post command before deciding on the single external write.

## Output 273 (msg_1ff905485001juXqs7b78Hq4Cd)

I have a rigorous paper-level finding. Let me verify no post exists under this exact tag once more, then make the single board post (the project's required reporting mechanism; no repo/Lean changes).

## Output 318 (msg_1ff913519001iXcl50iNxZv2G8)

The comment command returned the updated issue object. Let me verify the post actually landed under the tag.

## Output 329 (msg_1ff91464f001eTaqhwQpXuJIrq)

Post confirmed (one write, 19:24:17Z). Final state check.

## Output 340 (msg_1ff9156150016JuHIt1RpkEnRK)

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
