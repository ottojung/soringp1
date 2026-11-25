# antonina-HmbeIADfmNb6iu9yD3Ct98-stupidity

Session: ses_e4818365effena2qd6qUdmobML
Workspace: /home/lubko/soring-fronts/exec-fibonacci-threshold-proof-20261107
Created: 1794086783480; updated: 1794089521657

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 259 (msg_1b80081a9001iEFxrKFi23Z5dD)

## State check first

I inspected the session, worktree, and Git state:

- Working directory: `/home/lubko/soring-fronts/exec-fibonacci-threshold-proof-20261107`
- `git status --short`: clean
- `HEAD`: `c865b23` (“Correct reachability experiment module documentation”)
- No repo edits, commits, Lean changes, board posts, or other external actions were made in this turn.
- The earlier exploratory enumeration ran only from `/tmp/opencode` against scripts in a sibling worktree; it did not modify this repository. I have run no further enumeration after your stop instruction.

Below I treat the two proof obligations separately.

---

# (A) The core-completeness lemma

## The literal statement has one boundary exception at \(n=2\)

Use the standard definition:

> **Definition.** An element \(u\in P\) is *universal* if it is comparable with every other element of \(P\). A poset is a **core** if it has no universal element.

Then a singleton is universal vacuously, hence is not a core.

With that definition, the literal lemma is false at \(n=2\):

> \(P=\) the 2-element antichain is a core and is ordinal-indecomposable. Its maximal elements are the two points; deleting either leaves a singleton, and a singleton is universal, hence not a core.

So the smallest counterexample to the statement “for every ordinal-indecomposable core \(P\) with \(|P|\ge 2\)” is \(P=\mathbf 2\), not an \(n\ge 10\) example. If the intended convention is that singletons count as cores, or if the assertion is only for \(|P|\ge 3\), this exception disappears.

The positive result is the following.

## Theorem A

> Let \(P\) be a finite ordinal-indecomposable core with \(|P|\ge 3\). Then there is a maximal element \(x\in P\) such that \(P-x\) is a core.

### Proof

Assume for contradiction that for every maximal \(x\), the deletion \(P-x\) is not a core. Thus \(P-x\) contains a universal element; choose one and call it \(u(x)\).

**Step 1. \(u(x)\) is incomparable with exactly \(x\).**

Since \(u(x)\) is universal in \(P-x\), the only element of \(P\) with which it could fail to be comparable is \(x\). But \(P\) is a core, so \(u(x)\) is not universal in \(P\). Hence it is incomparable with \(x\), and

\[
\operatorname{Inc}(u(x))=\{x\},\qquad u(x)\parallel x.
\]

**Step 2. \(P\) has at least two maximal elements.**

Suppose \(P\) had a unique maximal element \(x\). In a finite poset, every element lies below some maximal element, so every \(y\ne x\) satisfies \(y<x\). Since \(|P|\ge 3\), the poset \(P-x\) is nonempty, so \(u(x)\) exists and \(u(x)\in P-x\). Hence \(u(x)\ne x\) and \(u(x)<x\), contradicting \(u(x)\parallel x\). Therefore \(P\) has at least two maximal elements.

**Step 3. Take two distinct maximal elements \(x,y\).**

For any maximal \(z\), and any other maximal \(w\ne z\), the element \(u(z)\) lies in \(P-z\), hence is comparable with \(w\). Since \(w\) is maximal, we cannot have \(w<u(z)\). Thus

\[
u(z)=w \quad\text{or}\quad u(z)<w.
\]

Apply this to \(x,y\):

\[
u(x)=y \ \text{ or }\ u(x)<y,
\qquad
u(y)=x \ \text{ or }\ u(y)<x.
\]

There are four cases.

**Case 1: \(u(x)\ne y\) and \(u(y)\ne x\).**

Then \(u(x)<y\) and \(u(y)<x\). Since \(u(x)\in P-y\), and \(u(y)\) is universal in \(P-y\), the elements \(u(x),u(y)\) are comparable.

- If \(u(x)\le u(y)\), then \(u(x)\le u(y)<x\), so \(u(x)<x\), contradicting \(u(x)\parallel x\).
- If \(u(y)<u(x)\), then \(u(y)<u(x)<y\), so \(u(y)<y\), contradicting \(u(y)\parallel y\).

So Case 1 is impossible.

**Case 2: \(u(x)\ne y\) and \(u(y)=x\).**

Then \(u(x)<y\). Also \(u(x)\in P-y\), and \(u(y)=x\) is universal in \(P-y\), so \(x\) is comparable with \(u(x)\), contradicting \(u(x)\parallel x\). Impossible.

**Case 3: \(u(x)=y\) and \(u(y)\ne x\).**

Symmetric to Case 2: \(u(y)<x\), and \(u(y)\in P-x\), while \(u(x)=y\) is universal in \(P-x\), so \(y\) is comparable with \(u(y)\), contradicting \(u(y)\parallel y\). Impossible.

**Case 4: \(u(x)=y\) and \(u(y)=x\).**

Then \(x\parallel y\). Let \(Q=P-\{x,y\}\). For any \(z\in Q\):

- \(y=u(x)\) is universal in \(P-x\), so \(y\) is comparable with \(z\). Since \(y\) is maximal, \(z<y\).
- \(x=u(y)\) is universal in \(P-y\), so \(x\) is comparable with \(z\). Since \(x\) is maximal, \(z<x\).

Thus every element of \(Q\) lies below both \(x\) and \(y\), while \(x\parallel y\). Therefore

\[
P=Q\oplus \{x,y\},
\]

where \(\{x,y\}\) is a 2-element antichain. Since \(|P|\ge 3\), we have \(Q\ne\varnothing\), so this is a nontrivial ordinal-sum decomposition, contradicting the ordinal-indecomposability of \(P\).

All cases are impossible. Hence some maximal \(x\) has \(P-x\) a core. \(\square\)

### Cases explicitly closed

The proof closes:

- unique maximal element: Step 2;
- several maximal elements: Step 3;
- \(u(x)\) maximal: this is exactly the subcase \(u(x)=y\) in Cases 3–4;
- \(u(x)\) non-maximal: subcase \(u(x)<y\) in Cases 1–2;
- the “both maximal deletions have universal elements” configuration: leads to \(P=Q\oplus\{x,y\}\), the ordinal-sum contradiction.

The only unresolved point is the \(n=2\) definitional boundary above.

---

# (B) The general Fibonacci induction

Let \(F_0=0,F_1=1,F_{k+2}=F_{k+1}+F_k\). The target is

\[
e(P)\ge F_{m(P)+2}
\qquad\text{for every finite poset }P,
\]

equivalently \(T(r)=F_{r+3}-1\).

## B1. Ordinal sums

**Lemma B1.** For nonempty posets \(A,B\),

\[
e(A\oplus B)=e(A)e(B),
\qquad
m(A\oplus B)=m(A)+m(B).
\]

*Justification.* Every linear extension of \(A\oplus B\) is a linear extension of \(A\) followed by one of \(B\), so extension counts multiply. For the depth, sorting \(A\oplus B\) requires sorting \(A\) and sorting \(B\); conversely, run optimal strategies for \(A\) and \(B\) independently, so the depths add. This is the ordinal-sum additivity already recorded in `docs/research-series-decomposition.md`.

**Lemma B2.** For all integers \(a,b\ge 0\),

\[
F_{a+2}F_{b+2}\ge F_{a+b+2}.
\]

*Proof.* Let

\[
G(a,b)=F_{a+2}F_{b+2}-F_{a+b+2}.
\]

Using the Fibonacci recurrence in the first index,

\[
G(a,b)=G(a-1,b)+G(a-2,b).
\]

The base cases are

\[
G(0,b)=F_2F_{b+2}-F_{b+2}=0,
\]

and

\[
G(1,b)=F_3F_{b+2}-F_{b+3}
=2F_{b+2}-(F_{b+2}+F_{b+1})
=F_{b+2}-F_{b+1}=F_b\ge 0.
\]

Hence \(G(a,b)\ge 0\) for all \(a,b\ge 0\). \(\square\)

Therefore, if the Fibonacci bound holds on \(A\) and \(B\), then it holds on \(A\oplus B\):

\[
e(A\oplus B)=e(A)e(B)
\ge F_{a+2}F_{b+2}
\ge F_{a+b+2}
=F_{m(A\oplus B)+2},
\]

where \(a=m(A)\), \(b=m(B)\).

## B2. Reduction to ordinal-indecomposable cores

Take a counterexample to the Fibonacci bound chosen with lexicographically minimal \((e(P),|P|)\).

- If \(z\) is universal in \(P\), then \(P=L\oplus\{z\}\oplus U\), and deleting \(z\) preserves both \(e\) and \(m\):

\[
e(P)=e(P-z),\qquad m(P)=m(P-z).
\]

So \(P-z\) is a smaller counterexample, contradiction. Hence \(P\) is a core.

- If \(P=A\oplus B\) with both summands non-total, then \(e(A),e(B)<e(P)\), so by minimality both satisfy the Fibonacci bound, and Lemma B2 gives it for \(P\), contradiction.

- If one summand is a total chain, then it has \(e=1\) and \(m=0\), so the other summand has the same \(e\) and the same \(m\), giving a counterexample with fewer elements, contradiction.

Thus a minimal counterexample may be assumed to be an **ordinal-indecomposable core** (of size at least \(2\)).

## B3. What the induction actually needs

Let \(P\) be an ordinal-indecomposable core with \(m(P)=m\ge 1\). Choose an optimal first comparison of an incomparable pair \(x,y\). Let

\[
P_1=P+\{x<y\},\qquad P_2=P+\{y<x\},
\]

with \(e_1=e(P_1)\), \(e_2=e(P_2)\), \(m_1=m(P_1)\), \(m_2=m(P_2)\). Then

\[
e(P)=e_1+e_2,\qquad
m(P)=1+\max(m_1,m_2)
\]

for the chosen optimal pair, and \(m_1,m_2\le m-1\), with \(\max(m_1,m_2)=m-1\).

If \(P\) is a minimal-\(e\) counterexample, then \(P_1,P_2\) have smaller \(e\), so by minimality they satisfy the Fibonacci bound:

\[
e_1\ge F_{m_1+2},\qquad e_2\ge F_{m_2+2}.
\]

WLOG \(m_1=m-1\). Then

\[
e(P)\ge F_{m+1}+F_{m_2+2}.
\]

To force \(e(P)\ge F_{m+2}=F_{m+1}+F_m\), we need

\[
m_2+2\ge m,
\qquad\text{i.e.}\qquad
m_2\ge m-2.
\]

Thus the induction closes precisely if the optimal split is **balanced to within one**:

\[
\tag{\(\star\)}
\text{some optimal first comparison has }
\min(m_1,m_2)\ge m-2.
\]

If instead every optimal split has \(m_2\le m-3\), the Fibonacci summation is too weak. For example, with \(m=7\):

\[
m_2=4:\quad F_8+F_6=21+8=29< F_9=34,
\]

and

\[
m_2=3:\quad F_8+F_5=21+5=26<34.
\]

So the first genuinely unproved step is the passage from the child bounds to the parent bound when the split is unbalanced. It is not an arithmetic slip: the implication

\[
e\ge F_{m+1}+F_{m_2+2},\quad m_2\le m-3
\;\Longrightarrow\;
e\ge F_{m+2}
\]

is simply false in general. A proof must use extra structural information, or a stronger induction invariant.

## B4. Equivalent threshold form of the missing lemma

The clean threshold form of the missing step is:

> **Fibonacci splitting lemma, \(\operatorname{FSL}(r)\).**  
> For every finite poset \(P\) with
> \[
> e(P)\le F_{r+3}-1,
> \]
> there exists an incomparable pair \(x,y\) such that both children satisfy
> \[
> e(P+\{x<y\})\le F_{r+2}-1,
> \qquad
> e(P+\{y<x\})\le F_{r+2}-1.
> \]

If \(\operatorname{FSL}(r)\) holds, then \(T(r)=F_{r+3}-1\) follows from \(T(r-1)=F_{r+2}-1\): both children are sortable in \(r-1\) comparisons, so \(P\) is sortable in \(r\). The matching upper bound is the staircase \(S_{r+2}\), which has \(e=F_{r+3}\) and \(m=r+1\).

The relevant range is only

\[
F_{r+2}\le e(P)\le F_{r+3}-1,
\]

because if \(e(P)\le F_{r+2}-1\), any comparison already has both children with fewer than \(F_{r+2}\) extensions.

In the top part of this window the required split is genuinely strong: at \(e\approx F_{r+3}\), one needs a child with at least

\[
e-(F_{r+2}-1)\approx F_{r+1}
\]

extensions, i.e. a minority fraction approaching

\[
\frac{F_{r+1}}{F_{r+3}}\longrightarrow \frac1{\varphi^2}\approx 0.382.
\]

Kahn–Saks guarantees only a comparison with both orientations between \(3/11\approx0.273\) and \(8/11\). Thus Kahn–Saks does not imply \(\operatorname{FSL}(r)\), and the gap is not a rounding issue.

## B5. Why the remaining gap is not merely technical

The best uniform exponential lower bound available from the project’s cited tools is the Kahn–Saks recurrence

\[
T(r)\ge \left\lfloor \frac{11}{8}T(r-1)\right\rfloor,
\]

which gives a lower bound of the form

\[
e(P)\ge c\left(\frac{11}{8}\right)^{m(P)}.
\]

The Fibonacci conjecture predicts the much stronger exponential base

\[
e(P)\ge c'\,\varphi^{m(P)},\qquad \varphi\approx1.618.
\]

So the missing lemma is equivalent to improving the uniform exponential base from \(11/8=1.375\) to \(\varphi\), an improvement of about \(17.6\%\). That is a substantive strengthening, not a finite case check.

The core-completeness lemma (A) is genuinely useful for a core-only enumeration, but it does not address this split-balance issue: it controls which maximal deletions remain cores, not how extension counts distribute across the two orientations of a comparison.

## B6. Precise statement of the remaining gap

The minimal-counterexample induction is rigorous up to the following statement:

> **Gap (balanced optimal split / Fibonacci split).**  
> Let \(P\) be an ordinal-indecomposable core and a minimal-\(e\) counterexample to
> \(e(P)\ge F_{m(P)+2}\), with \(m=m(P)\). Then some optimal first comparison
> of \(P\) has both children of depth at least \(m-2\); equivalently, it is not
> the case that every optimal comparison has child depths differing by at least
> \(2\).
>
> In threshold form: for every \(P\) with
> \[
> F_{m+1}\le e(P)\le F_{m+2}-1,
> \]
> there is a comparison whose two children have at most \(F_{m+1}-1\)
> extensions.

I cannot close this from the core lemma, ordinal-sum additivity, and Kahn–Saks. Neither can I produce a counterexample to it. The first open numerical case remains \(T(6)\); the given \(n\le18\) check rules out small counterexamples, but does not supply the missing all-\(n\) split argument.

---

## Bottom line

- **(A)** is proved for all \(|P|\ge3\) by the case analysis above. The literal statement fails at the single boundary case \(P=\mathbf 2\) under the standard “no universal element” definition; with singletons declared cores (or with the assertion restricted to \(|P|\ge3\)), there is no counterexample.
- **(B)** reduces rigorously to the Fibonacci splitting lemma / balanced optimal split condition. That lemma is the exact first unproved induction step; the naive Fibonacci summation is insufficient precisely when every optimal split has child-depth gap at least two. The gap is a genuine exponential-base strengthening from \(11/8\) to \(\varphi\), not a technical rounding gap.

## Output 271 (msg_1b8116e1b001f9lPH68hlWWr6z)

The prior turn’s inspections are complete: the worktree is clean at `c865b23`. No files, commits, or board posts were changed. I will not run enumerations.

I cannot prove or refute Lemma A from the arguments available. The earlier reduction to a balanced *optimal* split does not establish it: Lemma A permits a different, non-optimal pair, and the child depths for that pair need not obey the optimal-split recurrence in the way the earlier argument assumed.

The precise obstruction is this. Let \(m=m(P)\). For every incomparable pair, its children’s depths satisfy
\[
\max(m_1,m_2)\ge m-1,
\]
otherwise that comparison followed by the deeper child’s strategy would sort \(P\) in fewer than \(m\) comparisons. Lemma A additionally needs **some** pair with \(\min(m_1,m_2)\ge m-2\). The first fact alone does not imply the second. To prove A, one must show that if every pair has a child of depth at most \(m-3\), then some strategy sorts \(P\) in \(m-1\) comparisons—or otherwise construct a qualifying pair. I have no valid exchange or strategy argument closing that implication, and no verified counterexample.

The Executive’s induction is sound conditional on A: for its pair, the depth range is \(m-2\le m_i\le m-1\), both children are non-total, and induction gives
\[
e(P)\ge F_{m_1+2}+F_{m_2+2}\ge F_{m+1}+F_m=F_{m+2}.
\]
But this does not prove A. Consequently I cannot claim the all-\(r\) threshold theorem or \(T(6)=33\) from this work.
