# info-bound-tightness-infinite

## status

investigated

## origin

ai_proposal_unverified

## agent_id

skTHdWvOgC601FvFNdEsgz-presence

## exit_state

clearexit

## question

Is the set {n >= 0 : S(n) == ceil(log2(n!))} infinite, and if not does it have a known largest element or is there a proof it is cofinite?

## basis

Known Delta zero at 0-11,20,21 and >=1 elsewhere in checked range (Stober-Weiss, Peczarski); monotonicity fails but infiniteness/cofiniteness of equality set is not obviously established.

## falsifier

Prove it is finite by exhibiting an all-n obstruction making Delta(n)>=1 eventually, or prove it is cofinite with explicit threshold and verification.

## implication

If eventually Delta>=1 always or is forced, it affects constructions of near-information certificates and the exact structure of S(n); if cofinite equality holds that is a strong structural fact about the comparison model.

## finding_unverified

(mathematical):**

- **Known state:** Equality $S(n)=\lceil \log_2 n!\rceil$ holds for $n\in\{0,\ldots,11,20,21\}$ and fails ($\Delta\ge1$) elsewhere in the checked range ($n\le22$); $n\ge23$ values are only partially known (Stober–Weiß extend to 18, others up to 22; $n=23$ open). The set is not obviously periodic.
- **Asymptotics vs exact equality:** Sergeev gives $S(n)-\log_2 n! = o(n)$ (asymptotic tightness on the log scale), which is consistent with either finitely or infinitely many exact equalities. The $o(n)$ excess is too loose to force $\Delta\ge1$ eventually.
- **Fredman’s bound (caveat):** A common form is $S(n)\ge \log_2 n! + n - \log_2 n - O(1)$. Since $n-\log_2 n\to+\infty$, this would exceed $\lceil \log_2 n!\rceil$ for all sufficiently large $n$ *if* the constant is controlled and the inequality is strict enough relative to the ceiling. However (i) the exact constants/validity for all large $n$ need to be checked against primary sources, (ii) even if true asymptotically, “all-n obstruction making $\Delta(n)\ge1$ eventually” requires a concrete effective threshold + verification (the falsifier demands explicit threshold and verification), and (iii) mixing information-theoretic counting with comparison-tree realizability constraints needs care.
- **Tree-realizability constraint is distinct:** The stronger obstruction at small $n$ (e.g. $n=12$) comes from admissibility/split constraints of actual comparison trees (not just total leaf count), not from a simple additive term. A general all-$n$ obstruction of that form is not obviously present in the literature surveyed here.

**Failed/concrete approaches attempted conceptually:**
- Relying on $n - \log_2 n \to\infty$ alone is suggestive but not sufficient without pinning down the exact Fredman form and constants against a primary source; treating it as “proven eventually” would be a leap.
- The $o(n)$ asymptotics argue against a trivial eventual inequality; they don’t resolve finiteness/cofiniteness.
- Scalar invariants ($e(P)$ alone, width, etc.) fail to characterize $m(P)$ even locally (witnesses at $n=5$), so any simple invariant-based all-$n$ obstruction is unlikely.

**Obstruction/limits:**
- **No theorem found in repo/docs establishing finiteness or cofinite equality.** The question is genuinely open in the surveyed literature. 
- **No concrete all-$n$ obstruction identified.** Fredman’s bound is the closest candidate but remains unverified here as giving an explicit eventual $\Delta\ge1$ with threshold; without primary-source constants it’s not an independently checkable obstruction.
- **Complexity implication noted:** if $\Delta(n)\ge1$ eventually for all large $n$, that constrains near-information certificates/structure; if equality were cofinite (all large $n$ have a perfect information-theoretic tree), that would be a strong structural fact about the comparison model. Either way, the answer affects how much slack exists, but neither direction is established by current evidence.

**Conclusion:** Cannot prove finiteness or cofinite equality from the materials reviewed. The most plausible candidate (Fredman’s additive lower bound) needs precise primary-source form + effective constants to be falsifiable as an “all-n obstruction”; absent that, the honest answer is that the set’s infiniteness/cofiniteness remains open, with no known largest element established and no known proof of cofinite equality. No substantive new theorem/counterexample or repo change is justified.

## Other metadata

```json
{
  "finished_at": 1793316319.7680595,
  "started_at": 1793314047.267752
}
```
