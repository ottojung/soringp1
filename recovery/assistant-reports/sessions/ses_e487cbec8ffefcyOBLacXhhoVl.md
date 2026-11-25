# antonina-yh9I8mV2tlpMFtpXPVbzdm-soup

Session: ses_e487cbec8ffefcyOBLacXhhoVl
Workspace: /home/lubko/soring-fronts/exec-linear-extension-core-literature-20261107
Created: 1794080194941; updated: 1794080728753

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 31 (msg_1b78382fb001az2icczknNoXJe)

I could not verify a primary source for the proposed theorem, so I can’t present it as an established literature result. The attempted search did not locate one, and I don’t have a proof from a cited standard result to substitute. The exact missing item is a primary citation or proof of:

> For every finite poset \(P\) on \(n\) elements with no element comparable to every other element, \(e(P)\ge n\).

The chain-plus-isolated example does **not** refute the claim: for a chain of \(n-1\) elements plus one isolated element, the isolated element can occupy any of \(n\) positions, so \(e(P)=n\). It has no universal element; the chain elements are not comparable to the isolated element.

**Conditional corollary, assuming the theorem.** Let \(P\) be a minimal counterexample to \(T(4)\ge12\), so \(e(P)<12\). A universal element is comparable to every other element and is therefore forced to a fixed end of every linear extension (a universal minimum or maximum); deleting it preserves the number of extensions. Repeating deletion yields a core \(Q\) with no universal element and \(e(Q)=e(P)<12\). If the proposed theorem holds, then \(|Q|\le e(Q)<12\), hence \(|Q|\le11\). Thus a **complete** enumeration of cores through size 11 would suffice to rule out such a counterexample. Enumeration through size 6 does not suffice. This reduction also requires that the deletion process preserves the relevant counterexample condition and that the enumeration covers every core up to size 11.

I therefore cannot conclude that this theorem holds, nor claim that the requested finite reduction is currently justified.

## Output 147 (msg_1b78ae752001hS0lLWXnhB5mbF)

## Effect reconciliation first

I inspected before doing new work:

- **Working tree / Git:** clean detached `HEAD` at `c865b23` (`Correct reachability experiment module documentation`). No new commits, branches, stashes, or modified files were created by this route.
- **Board:** no post from this literature route. The only matching board text is the earlier Viche Recovery Steward reconciliation, which is a different turn.
- **Previous turn’s only external action:** one read-only arXiv search `GET`; no durable state.
- **Conclusion:** nothing was posted, committed, or edited that could be duplicated. I did not repeat the interrupted prompt; I completed the mathematical part below. All scratch work is in `/tmp/opencode/litcheck/`.

## Verdict: the statement is **true**

> If a finite poset \(P\) has \(n\) elements and no universal element, then \(e(P)\ge n\).

I did **not** verify a primary literature citation for it. The exact missing citation would be a paper stating this lemma (it is plausibly folklore/known, but I will not attribute it without a source). What follows is a complete elementary proof, so the result does not depend on the missing citation.

Two small but important corrections to the previous attempt:

1. A universal element need **not** be a unique maximum or minimum, nor be forced to an end of every extension. Example: two incomparable elements \(a,b\) below \(z\) and two incomparable elements \(c,d\) above \(z\); then \(z\) is universal but neither extremum.
2. Nevertheless, deleting a universal element **does** preserve \(e(P)\). If \(z\) is universal, write
   \[
   L=\{w:w<z\},\qquad U=\{w:w>z\}.
   \]
   Since \(z\) is comparable to everything, every element lies in \(L\cup U\), all of \(L\) is below \(z\), all of \(U\) above \(z\), and hence every \(l\in L\) is below every \(u\in U\). Thus
   \[
   P \;\cong\; L\oplus \{z\}\oplus U,
   \qquad
   e(P)=e(L)\,e(U)=e(P-z).
   \]
   The same argument gives \(m(P)=m(L)+m(U)=m(P-z)\): comparisons involving \(z\) carry no information because its final rank is fixed at \(|L|+1\), and all relations between \(L\) and \(U\) are already determined.

## Proof of the theorem

Let \(P\) be a minimal counterexample by \(|P|=n\), so \(P\) has no universal element and \(e(P)<n\). The cases \(n=1,2\) are immediate: \(n=1\) has a universal element vacuously; for \(n=2\) the only poset without a universal element is the antichain, with \(e=2\).

For \(n\ge3\), \(P\) has at least two maximal elements. Indeed, if \(m\) were the unique maximal element, every element would lie below \(m\), so \(m\) would be universal.

For a maximal element \(x\), let \(A_x\) be the linear extensions of \(P\) ending in \(x\). Because \(x\) is maximal, appending \(x\) to any linear extension of \(P-x\) gives a bijection
\[
A_x \longleftrightarrow \operatorname{Ext}(P-x),
\qquad |A_x|=e(P-x).
\]

**Claim.** For every maximal \(x\), \(P-x\) has a universal element.

Suppose not. Choose a maximal \(y\ne x\). The sets \(A_x,A_y\) are disjoint, so
\[
e(P)\ge e(P-x)+e(P-y).
\]
By minimality of \(P\), since \(P-x\) has no universal element and \(|P-x|=n-1\),
\[
e(P-x)\ge n-1.
\]
Also \(e(P-y)\ge1\). Hence \(e(P)\ge n\), contradiction. This proves the claim.

Let \(u_x\) be a universal element of \(P-x\). Then \(u_x\) is incomparable to \(x\); otherwise \(u_x\) would be comparable to all of \(P-x\) and to \(x\), hence universal in \(P\).

Now fix two distinct maximal elements \(x,y\). Put
\[
u=u_x\in P-x,\qquad v=u_y\in P-y.
\]
Because \(y\) is maximal, either \(u=y\) or \(u<y\). Because \(x\) is maximal, either \(v=x\) or \(v<x\). There are four cases.

1. **\(u\ne y\) and \(v\ne x\).** Then \(u,v\in P-x\). Since \(u\) is universal in \(P-x\), \(u\) and \(v\) are comparable. If \(u<v\), then \(v<x\) gives \(u<x\), contradicting that \(u\) is incomparable to \(x\). If \(v<u\), then \(u<y\) gives \(v<y\), contradicting that \(v\) is incomparable to \(y\).

2. **\(u\ne y\) and \(v=x\).** Then \(u\in P-y\), and \(v=x\) is universal in \(P-y\), so \(x\) is comparable to \(u\), contradicting that \(u\) is incomparable to \(x\).

3. **\(u=y\) and \(v\ne x\).** Then \(u=y\) is universal in \(P-x\), so \(y\) is comparable to \(v\); since \(y\) is maximal and \(v\ne y\), we get \(v<y\). Also \(x\) is universal in \(P-y\) and \(x\) is maximal, so \(v<x\). For every \(z\in P-\{x,y\}\), \(v\) is comparable to \(z\) because \(v\) is universal in \(P-y\). Hence \(v\) is comparable to all of \(P\), so \(v\) is universal in \(P\), contradiction.

4. **\(u=y\) and \(v=x\).** Then \(y\) is universal in \(P-x\) and \(x\) is universal in \(P-y\). Since \(x,y\) are maximal, every \(z\in Q:=P-\{x,y\}\) satisfies
   \[
   z<y,\qquad z<x.
   \]
   Also \(x\) and \(y\) are incomparable. Therefore every linear extension of \(P\) is obtained by taking a linear extension of \(Q\) and appending \(x,y\) in either order:
   \[
   e(P)=2\,e(Q).
   \]
   Moreover \(Q\) has no universal element: if \(z\in Q\) were universal in \(Q\), then \(z\) would be comparable to all of \(Q\), and since \(z<x\) and \(z<y\), it would be universal in \(P\). If \(Q\ne\varnothing\), minimality gives \(e(Q)\ge |Q|=n-2\), so
   \[
   e(P)=2e(Q)\ge 2(n-2)\ge n \quad (n\ge4),
   \]
   a contradiction. If \(Q=\varnothing\), then \(n=2\), already excluded. For \(n=3\), \(|Q|=1\), but a one-element poset has a universal element, so this case cannot occur.

All cases contradict \(e(P)<n\). Hence no counterexample exists. \(\square\)

The bound is attained by the **chain plus isolated point**: for \(P=C_{n-1}\sqcup\{\ast\}\), the isolated point may occupy any of the \(n\) positions, so \(e(P)=n\), and no element is universal: the isolated point is incomparable to every chain element, and every chain element is incomparable to the isolated point. This confirms the \(e=n\) example you asked about.

An exhaustive independent check for \(n\le6\) (all \(1,3,19,219,4231,130023\) labelled posets) found no poset without a universal element with \(e<n\); the finite data is consistent with the theorem but, as you said, is not evidence for all \(n\). The proof above is the all-\(n\) argument.

## Exact corollary for \(T(4)\ge12\)

Take the statement in the form used by the project:

> \(T(4)\ge12\): every finite poset \(P\) with \(e(P)\le12\) satisfies \(m(P)\le4\).

where \(e(P)\) is the number of linear extensions and \(m(P)\) is the minimax adaptive comparison depth.

Let \(P\) be a counterexample, so \(e(P)\le12\) and \(m(P)>4\).

1. **Delete universal elements.** While the current poset has a universal element \(z\), replace it by the induced subposet on the remaining elements. By the computation above,
   \[
   e(P-z)=e(P),\qquad m(P-z)=m(P).
   \]
   So after each deletion the extension count and minimax depth are unchanged. The process terminates at an induced subposet \(Q\subseteq P\) with no universal element, and
   \[
   e(Q)=e(P)\le12,\qquad m(Q)=m(P)>4.
   \]
   (If \(Q\) were empty, then \(e(Q)=1\) and \(m(Q)=0\), contradicting \(m(Q)>4\); so \(Q\ne\varnothing\). A nonempty terminal \(Q\) has at least two elements, since a singleton is vacuously universal.)

2. **Apply the theorem.** Since \(Q\) has no universal element,
   \[
   |Q|\le e(Q)\le12.
   \]

3. **Converse.** Conversely, any poset \(Q\) with \(|Q|\le12\), \(e(Q)\le12\), no universal element, and \(m(Q)>4\) is itself a counterexample to \(T(4)\ge12\).

Therefore \(T(4)\ge12\) is **equivalent** to the assertion that a finite set of posets is absent: all posets \(Q\) of size \(n\le12\) with \(e(Q)\le12\), no universal element, must have \(m(Q)\le4\). This is the promised finite reduction. Note the sharp form: if the counterexample has \(e(P)\le11\), then \(|Q|\le11\); the bound \(n\le12\) is needed exactly because \(e(P)=12\) is allowed, and equality is consistent with the chain-plus-isolated poset of size \(12\), which has \(e=12\) and \(m=\lceil\log_2 12\rceil=4\) and is therefore not itself a counterexample.

All premises used:

- \(e(P)\) is the number of linear extensions, and \(m(P)\) is minimax comparison depth.
- A universal element is one comparable to every other element; it may be neither minimum nor maximum.
- Universal deletion preserves both \(e\) and \(m\), via \(P\cong L\oplus\{z\}\oplus U\).
- The theorem applies to the terminal core because it has no universal element.
- Minimality of the original counterexample is not needed for the reduction; any counterexample yields a core of size at most \(12\). If “minimal” means minimal \(n\) or minimal \(e\), the same conclusion holds.

No repository edits, board posts, or commits were made.
