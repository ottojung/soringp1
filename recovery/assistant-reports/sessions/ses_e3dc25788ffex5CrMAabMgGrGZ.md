# antonina-VN2VOe2CmMmM0YZIBZ8i4m-oxford

Session: ses_e3dc25788ffex5CrMAabMgGrGZ
Workspace: /home/lubko/soring-fronts/disjoint-union-strict-defect
Created: 1794260183231; updated: 1794261961373

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 310 (msg_1c257b7a2001XS7ityK0Gecs3s)

Stopped the search as instructed. No further enumeration, no Lean or repository changes. Work was scratch-only under `/tmp/opencode/du_strict`.

## Finding

The strict-defect claim is **true**:

> For every pair of nonempty finite posets \(A,B\) on disjoint ground sets,
> \[
> F(A\sqcup B)\ \ge\ F(A)+F(B)+1,
> \]
> hence \(\delta(A,B)=F(A\sqcup B)-F(A)-F(B)\ge 1\).

So no equality family exists, and no exact additive formula
\(F(A\sqcup B)=F(A)+F(B)\) can hold.

## Proof

I use the already-established non-strict superadditivity
\[
F(A\sqcup B)\ge F(A)+F(B),
\]
which follows from \(L(A\oplus B)\subseteq L(A\sqcup B)\) and ordinal-sum additivity
\(F(A\oplus B)=F(A)+F(B)\).

Proceed by induction on the number \(m\) of incomparable pairs of \(A\sqcup B\).

**Base \(m=0\).** Then \(A\) and \(B\) are chains, so \(F(A)=F(B)=0\). Since both are nonempty, \(A\sqcup B\) is not total, so \(F(A\sqcup B)\ge 1\). Hence the claim holds.

**Inductive step.** Take a correct decision tree \(T\) for \(A\sqcup B\), with no redundant comparisons, and look at its first comparison.

1. **Cross comparison \(a\in A\), \(b\in B\).**  
   In the branch \(a<b\), the subtree must still identify every extension of \(A\sqcup B\) satisfying \(a<b\), in particular every extension of the ordinal sum \(A\oplus B\). Therefore that subtree has height at least \(F(A\oplus B)=F(A)+F(B)\). Including the first comparison,
   \[
   \operatorname{height}(T)\ge 1+F(A)+F(B).
   \]

2. **Internal comparison \(x,y\in A\).**  
   Let \(A_< = A+x<y\) and \(A_> = A+y<x\). The branch \(x<y\) must solve \(A_<\sqcup B\), and the branch \(y<x\) must solve \(A_>\sqcup B\). Both child posets have fewer incomparable pairs, so induction applies:
   \[
   \operatorname{height}(T)
   \ge 1+F(A_<\sqcup B)
   \ge 1+F(A_<)+F(B)+1.
   \]
   The same holds for \(A_>\). Therefore
   \[
   \operatorname{height}(T)
   \ge F(B)+2+\max\{F(A_<),F(A_>)\}.
   \]
   But comparing \(x,y\) first in \(A\) gives
   \[
   F(A)\le 1+\max\{F(A_<),F(A_>)\},
   \]
   so
   \[
   \max\{F(A_<),F(A_>)\}\ge F(A)-1.
   \]
   Hence
   \[
   \operatorname{height}(T)\ge F(A)+F(B)+1.
   \]

3. **Internal comparison in \(B\).** Symmetric.

Thus every correct tree has height at least \(F(A)+F(B)+1\). \(\square\)

## Important correction to the 21:37Z proof

The Executive conclusion is correct, but step (1) of that proof as written is not literally rigorous: restricting a strategy to \(A\)-\(A\) comparisons does **not** immediately yield a tree sorting \(A\), because cross comparisons can transmit information about \(A\) through transitivity with \(B\)’s relations. The induction proof above avoids that gap. It uses the ordinal-sum lower bound only in the cross-comparison case and induction on internal-comparison branches.

## Finite corroboration

I completed an exhaustive unlabeled-poset pair check for all partitions with total size \(\le 8\), using directed canonical forms (`pynauty`), stronger than the earlier total-size-\(\le 6\) labelled check. There were **zero equalities**. Minimum observed defect by total size:

- total 2: 1
- total 3–7: 2
- total 8: 3

The n=9 run was started before the STOP instruction and then killed; it produced no mathematical result and is not evidence. I did not rely on it.

## Honest limits

- What is proved is **positivity** of the defect, not its size or growth. The induction gives only \(+1\); the observed defect is already larger at small sizes, but no all-\(n\) growth theorem follows.
- This is a general-poset structural theorem about the minimax game. It does **not** by itself give a new uniform complexity bound for exact unary \(S(n)\), nor a certificate-completeness result.
- It does rule out additive parallel decomposition
  \(F(A\sqcup B)=F(A)+F(B)\): any evaluator using disjoint-union additivity must account for at least one additional comparison. The genuinely open refinement remains the size/asymptotics of the strict defect.
