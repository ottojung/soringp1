# antonina-aHkhXvDRJbTgaYx1yh2le3-idle

Session: ses_e45e482d2ffeFiFd0AgWEDFogo
Workspace: /home/lubko/soring-fronts/ks-step-audit
Created: 1794123726194; updated: 1794124778821

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 483 (msg_1ba27060c00174SIpuhlFMX003)

# Audit: the Kravitz–Sah step in the #301 shallow-state argument

Report only. No tracked files changed, nothing committed or posted.

## 0. Bottom line

**Verdict: SOURCE-GAP** — not SOURCE-CONTRADICTS.

- The *existence* of a **width-2** poset \(M\) with \(e(M)=p\) and \(|M|=O(\log p\log\log p)\) is **SOURCE-SUPPORTS** (Kravitz–Sah), modulo a harmless printed off-by-one in Proposition 4.1.
- The *effective/randomized* use made in #301 — find such a \(d\) with good Euclidean quotient sum by sampling, construct the Stern–Brocot poset, verify its extension count — is **not** stated or proved in Kravitz–Sah. It is a plausible, likely fillable deduction, but as an audit of the source it remains a gap. The #301 post itself calls it “a paper deduction, currently unaudited.”
- The #301 post’s **intermediate arithmetic bound** \(\operatorname{cov}(Q)\lesssim 2|M|^2+n^2/2\) is **false as written**: the worst-case cover count is \(2.5|M|^2+1.5n^2+O(n+|M|)\). The final inequality \(\operatorname{cov}(Q)\le S(N)\) nevertheless holds for all \(n\ge2\) in the claimed constant range; the error does not overturn the conclusion.
- The shallow post’s explicit bound \(|M|\le C n\log n\log\log n\) is also wrong; the correct KS-derived bound is \(C n\log^2 n\). Using the larger correct bound still passes.

---

## 1. Exact primary sources

### 1.1 Kravitz–Sah is not the #P-completeness paper

The #P-completeness result is Brightwell–Winkler, not Kravitz–Sah.

- Graham Brightwell and Peter Winkler, **“Counting linear extensions,”** *Order* **8**(3) (1991), 225–242.  
  DOI: `10.1007/BF00383444`.
- Conference version: **“Counting linear extensions is #P-complete,”** *Proceedings of the 23rd Annual ACM Symposium on Theory of Computing (STOC ’91)*, 175–181.  
  DOI: `10.1145/103418.103441`.

The #301 post cites “Brightwell–Winkler, Order 8 (1991) 225–242” correctly; that is the journal version above.

### 1.2 The source actually used for the extension-number construction

- Noah Kravitz and Ashwin Sah, **“Linear Extension Numbers of \(n\)-Element Posets,”** *Order* **38**(1) (2021), 49–66.  
  DOI: `10.1007/s11083-020-09527-2`. Published online 11 May 2020; print April 2021.
- arXiv: `1906.06036v1` [math.CO], 14 June 2019, 17 pp.

**Access note.** I read the full arXiv v1 PDF. Crossref confirms the published title, authors, venue, volume and pages. The Springer full text is paywalled; the arXiv PDF itself numbers **Theorem 5.2** on p. 13 and **Proposition 4.1** on p. 9, matching the “Theorem 5.2” route named in #301. I did not inspect the published version’s full text, so any copy-editing difference between arXiv v1 and the journal version is not audited here.

The auxiliary Stern-array fact used in the paper is:

- D. H. Lehmer, “On Stern’s Diatomic Series,” *American Mathematical Monthly* **36**(2) (1929), 59–67.

---

## 2. What Kravitz–Sah actually proves

### 2.1 Existence and size

The relevant number-theoretic theorem is stated in the paper as Theorem 1.2 and restated/proved as Theorem 5.2. Exact statement from arXiv v1, p. 13:

> **Theorem 5.2.** There is an absolute constant \(c\) such that the following holds: for every \(n\ge 2\), there exists some \(1\le d\le n-1\) relatively prime to \(n\) such that
> \[
> s(n,d)\le c\frac{n}{\phi(n)}\log n\log\log n.
> \]

Here \(s(n,d)\) is the sum of the quotients in the Euclidean algorithm on \((n,d)\).

The Stern–Brocot/poset construction is Proposition 4.1, arXiv v1, p. 9:

> **Proposition 4.1.** Let \(d<n\) be relatively prime positive integers, and let \(\ell\) denote the sum of the quotients obtained when the Euclidean algorithm is run on the pair \((n,d)\). Then there is some \(P_b\) on at most \(\ell\) elements with exactly \(n\) linear extensions.

For \(n=p\) prime, \(p/\phi(p)=p/(p-1)\le 2\), so Theorem 5.2 gives
\[
s(p,d)\le 2c\log p\log\log p.
\]
Proposition 4.1 then gives a poset \(M=P_b\) with
\[
e(M)=p,\qquad |M|\le 2c\log p\log\log p
\]
(up to the off-by-one discussed in §2.5). This is exactly the prime case used in #301.

For general \(m\), the paper’s proof takes the ordinal/direct sum of the constructions for the prime factors and obtains
\[
|M|\le 2c\log m\log\log m,
\]
as stated in the proof of Theorem 1.1 on p. 9.

### 2.2 Width two

Width two is **not** an extra assumption in #301; it is explicitly guaranteed by the source.

From Section 3, arXiv v1, p. 4:

> “We now use the \((M,m)\)-direct sum to construct a large family of **width-2 posets** whose linear extension numbers we can control.”

From the Conclusion, arXiv v1, p. 16:

> “Recall that the posets used in the proof of Theorem 1.1 are all **width-2**.”

The family \(\{P_b\}\) is constructed recursively by adding a new minimal element to one of two chains, and the \((M,m)\)-direct sum preserves width two. The recurrence used to control the counts is Proposition 3.1, arXiv v1, p. 5:

> **Proposition 3.1.** Let \(b\) be a dyadic rational in the range \((0,1)\). If \(P_b\) first appears in the \(n\)-th stage, i.e., \(b=0.b_2b_3\cdots b_{n-1}1\), then
> \[
> \operatorname{le}(P_b)=\operatorname{le}(P_{b-2^{1-n}})+\operatorname{le}(P_{b+2^{1-n}}),
> \]
> where we convene to let \(\operatorname{le}(P_1)=0\).

Thus the #301 statement that “the width-two claim for \(M\) is taken at abstract level” is unnecessarily cautious: the source proves width two.

### 2.3 Density guarantee

Theorem 5.2 itself is an **existence** statement (a minimum over \(d\)). The proof contains a density statement that is stronger and is what #301 needs for sampling. The exact proof objects are:

\[
M_0=10C\frac{n}{\phi(n)}\log n,
\]
\[
D=\left\{d\in\{1,\dots,n-1\}:\gcd(n,d)=1\text{ and every quotient in }\mathbf q(n,d)\text{ is }\le M_0\right\}.
\]

The proof shows
\[
|D|\ge 0.9\,\phi(n)
\]
and
\[
\sum_{d\in D}s(n,d)\le Cn\log n\log\log n+O(n\log n\log\log\log n).
\]

Therefore the average of \(s(n,d)\) over \(D\) is at most
\[
\frac{C}{0.9}\frac{n}{\phi(n)}\log n\log\log n+O(\cdots).
\]
For prime \(p\), this is at most
\[
\frac{2C}{0.9}\log p\log\log p+O(\cdots).
\]

Applying Markov to the nonnegative random variable \(s(d)\) on \(D\): for any fixed \(t>1\), at least \((1-1/t)|D|\) elements of \(D\) satisfy
\[
s(p,d)\le t\cdot \frac{2C}{0.9}\log p\log\log p.
\]
With \(t=10\), at least
\[
0.9\cdot 0.9\,(p-1)=0.81(p-1)
\]
of all \(d\) satisfy \(s(p,d)\le \frac{20C}{0.9}\log p\log\log p\).

So the correct density statement is:

- \(D\) itself has density at least \(0.9\) among the \(\phi(p)=p-1\) admissible \(d\);
- the subset of \(D\) with \(s(p,d)=O(\log p\log\log p)\) has density at least \(0.9\) inside \(D\), hence at least \(0.81\) among all \(d\);
- more generally, for every fixed \(\varepsilon>0\), density at least \(0.9-\varepsilon\) among all \(d\), with the constant in \(O(\cdot)\) depending on \(\varepsilon\).

The literal statement “a \(0.9\)-density of draws has \(s(p,d)=O(\log p\log\log p)\)” is therefore slightly too strong at fixed constant, but the constant-fraction version needed for Las Vegas sampling is correct. Expected trials are \(O(1)\) (\( \le 1/0.81<1.24\) for \(t=10\)).

### 2.4 What the source does not prove

The source does **not** provide:

1. an explicit polynomial-time algorithm that, given prime \(p\), finds a good \(d\);
2. an explicit algorithm mapping \(d\) to the dyadic parameter \(b\) and constructing \(P_b\);
3. a complexity analysis of constructing \(P_b\) or of verifying \(e(P_b)=p\) by the recurrence;
4. an explicit numerical value of the absolute constant \(c\).

The ingredients are explicit enough that the effective version is a reasonable deduction: the continued fraction of \(p/d\) gives the Stern–Brocot path, the recursion builds \(P_b\) in \(O(\ell)\) steps, and the recurrence of Proposition 3.1 verifies the count in \(O(\ell)\) big-integer operations. Since \(\ell=O(\log p\log\log p)=O((\log p)^2)\), this is polynomial in the input length \(\log p\). But **none of this is stated or proved in Kravitz–Sah**. That is the precise source gap. It is a construction/effectivity gap, not a contradiction.

### 2.5 A printed off-by-one in Proposition 4.1

Proposition 4.1 as printed says “at most \(\ell\) elements.” The natural Stern–Brocot left-child construction appears to give \(\ell+1\), not \(\ell\).

Take \(n=6\), \(d=1\). The Euclidean quotient sum is \(\ell=6\). The fraction \(d/n=1/6\) sits at Stern–Brocot depth \(6\); its left child is \(1/7\), whose denominator-minus-numerator is \(6\). So the explicit construction gives a \(P_b\) of size \(7=\ell+1\) with \(e=6\). Direct computation of the \(P_b\) recurrence confirms that the first \(P_b\) with \(e=6\) has size \(7\), not \(6\).

For the asymptotic theorem this is harmless: replacing \(\ell\) by \(\ell+1\) changes \(2c\log p\log\log p\) by \(+1\), absorbed into the absolute constant. The #301 use \(|M|=O(\log p\log\log p)\) is therefore safe. But any exact audit should quote the safe form \(\le \ell+1\), and the published version’s full text was not inspected to see whether the journal version corrects this.

---

## 3. Arithmetic audit of the pumping inequality

### 3.1 Exact cover count

Let \(n=|P|\), let \(M\) be the Kravitz–Sah poset with \(e(M)=c\) prime, and put \(m=|M|\). Insert an \(L\)-chain between \(P\) and \(M\):
\[
Q=P\oplus C_L\oplus M.
\]
The exact cover count is the formula used in #301:
\[
\operatorname{cov}(Q)
=
\operatorname{cov}(P)+(L-1)+|\min(M)|+\operatorname{cov}(M)+|\max(P)|.
\tag{1}
\]
I verified (1) directly on all labelled posets with \(n,m\le3\) and \(1\le L\le4\), and simultaneously verified
\[
e(Q)=e(P)e(M)
\]
on the same family. Both checks pass.

### 3.2 The intermediate posted bound is too small

The #301 post fixes
\[
L=2m^2+n^2
\]
and then claims
\[
\operatorname{cov}(Q)\lesssim 2m^2+\frac{n^2}{2}.
\tag{2}
\]
Using the elementary bounds
\[
\operatorname{cov}(P)\le \frac{n(n-1)}2,\qquad
|\max(P)|\le n,\qquad
\operatorname{cov}(M)\le \frac{m(m-1)}2,\qquad
|\min(M)|\le m,
\]
equation (1) gives
\[
\operatorname{cov}(Q)
\le
\frac{n(n-1)}2+(2m^2+n^2-1)+m+\frac{m(m-1)}2+n,
\]
i.e.
\[
\boxed{
\operatorname{cov}(Q)
\le
\frac52 m^2+\frac32 n^2+\frac{n+m}{2}-1.
}
\tag{3}
\]
Thus the true worst-case coefficient is \(2.5\), not \(2\), and \(1.5\), not \(0.5\). The ratio
\[
\frac{\operatorname{cov}(Q)}{2m^2+n^2/2}
\]
is already \(1.7\) at \(n=2,m=2\), and tends to \(1.25\) as \(m/n\to\infty\). So (2) is false as an exact inequality. As an \(O(\cdot)\)-type statement it is true with the corrected constants (3); the “\(\sim\)” in the post masks a genuine \(25\%\) coefficient error.

### 3.3 The final inequality survives

We need
\[
\operatorname{cov}(Q)\le S(N),\qquad N=n+L+m.
\]
Use the conservative \(N_0=n+L=n+2m^2+n^2\le N\) (dropping the \(+m\), which only makes \(S\) smaller). For \(N_0\ge4\),
\[
\log_2(N_0!)\ge \frac{N_0}{2}\log_2\frac{N_0}{2}.
\]
Since
\[
\frac{N_0}{2}=m^2+\frac{n^2}{2}+\frac{n}{2}\ge m^2+\frac{n^2}{2},
\]
we get
\[
\log_2(N_0!)
\ge
\left(m^2+\frac{n^2}{2}\right)\log_2(m^2)
=
2m^2\log_2 m+n^2\log_2 m.
\tag{4}
\]
For \(m\ge3\), \(\log_2 m\ge\log_2 3>1.58\), so (4) gives
\[
\log_2(N_0!)
\ge
3.17\,m^2+1.58\,n^2,
\]
which dominates (3) for all \(n\ge2\) with room to spare. The only remaining case is \(m=2\), which in the range \(C\ge1\) occurs only at \(n=2,C=1\); there
\[
N_0=14,\quad \log_2(14!)\approx36.34,\quad \operatorname{cov}(Q)=17,
\]
so it also holds.

Thus, with the corrected constants, the pumping inequality is true for all \(n\ge2\), not merely for large \(n\).

### 3.4 Constants and numerical check

The correct KS-derived size bound is **not** \(C n\log n\log\log n\). In the reduction,
\[
\log c=O(\log K)=O(n\log n),
\]
so
\[
\log\log c=O(\log(n\log n))=O(\log n),
\]
and hence
\[
|M|\le 2c_{\mathrm{KS}}\log c\log\log c
=O(n\log^2 n).
\]
The shallow post’s “\(C n\log n\log\log n\)” is too optimistic by a factor \(\Theta(\log n/\log\log n)\). I used the larger, correct bound
\[
m=\left\lceil C n(\ln n)^2\right\rceil
\]
(with \(m\ge2\)) and also checked the smaller literal \(C n\ln n\ln\ln n\) bound. Both pass; the larger bound is the relevant one for a rigorous audit.

Numerical check over **all integers \(2\le n\le 200000\)**, using the exact worst-case formula (3) and the conservative \(N_0=n+L\):

| \(C\) | \(\max_n \operatorname{cov}(Q)/\log_2(N_0!)\) | attained at | minimum margin \(\log_2(N_0!)/\operatorname{cov}(Q)\) |
|---:|---:|---:|---:|
| \(1\) | \(0.467762\) | \(n=2\) | \(2.14\) |
| \(10\) | \(0.202107\) | \(n=2\) | \(4.95\) |
| \(100\) | \(0.098173\) | \(n=2\) | \(10.19\) |
| \(1000\) | \(0.064533\) | \(n=2\) | \(15.50\) |
| \(10^6\) | \(0.031802\) | \(n=2\) | \(31.44\) |

No failures in any case. Sample rows for \(C=1\):

| \(n\) | \(m\) | \(L\) | \(\operatorname{cov}(Q)\) | \(\log_2(N_0!)\) | ratio |
|---:|---:|---:|---:|---:|---:|
| \(2\) | \(2\) | \(12\) | \(17\) | \(36.34\) | \(0.46776\) |
| \(100\) | \(2121\) | \(9.007\times10^6\) | \(1.126\times10^7\) | \(1.951\times10^8\) | \(0.05773\) |
| \(1000\) | \(47718\) | \(4.555\times10^9\) | \(5.694\times10^9\) | \(1.396\times10^{11}\) | \(0.04080\) |
| \(200000\) | \(29797642\) | \(1.776\times10^{15}\) | \(2.220\times10^{15}\) | \(8.740\times10^{16}\) | \(0.02540\) |

The same check with the literal smaller bound \(|M|\le C n\ln n\ln\ln n\) also produced zero failures over the same range.

If one also wants the shallow post’s stronger requirement \(b+\operatorname{cov}(Q)\le S(N)\) with \(b=O(n\log n)\): with \(b=2n\log_2 n\) all tested cases pass; with \(b=10n\log_2 n\) only the tiny case \(n=2,C=1\) fails in the conservative estimate, which is a finite small-instance issue, not an asymptotic obstruction.

---

## 4. Verdict

**SOURCE-GAP.**

More precisely:

1. **SOURCE-SUPPORTS** the mathematical existence of a **width-2** poset \(M\) with
   \[
   e(M)=p,\qquad |M|=O(\log p\log\log p),
   \]
   for every prime \(p\) (with the safe printed bound \(\le\ell+1\), not \(\le\ell\)). Kravitz–Sah Theorem 5.2 + Proposition 4.1 + the width-2 family prove this. This part of #301 is correct.

2. **SOURCE-GAP** for the *effective/randomized* step. Kravitz–Sah prove existence, not an algorithm. The proof does yield a constant fraction of good \(d\) (density at least \(0.81\) among all \(d\) after Markov, or \(0.9-\varepsilon\) for any fixed \(\varepsilon\)), and the Stern–Brocot construction is explicit enough to implement, but the source does not state or analyze the construction/verification algorithm or give an explicit constant. The #301 post correctly labels this “a paper deduction, currently unaudited.” It is a fillable gap, not a contradiction.

3. **Post arithmetic, not source:** the intermediate bound
   \[
   \operatorname{cov}(Q)\lesssim 2|M|^2+\frac{n^2}{2}
   \]
   is **false as written**; the correct worst case is
   \[
   \operatorname{cov}(Q)\le \frac52|M|^2+\frac32 n^2+\frac{n+|M|}{2}-1.
   \]
   The final inequality \(\operatorname{cov}(Q)\le S(N)\) is nonetheless true for all \(n\ge2\) in the claimed constant range, and is provable for \(m\ge3\) by the elementary bound above, with the single \(m=2\) case checked directly. So the error is a coefficient slip, not a refutation of the pumping conclusion.

4. **Post size bound, not source:** \(|M|\le C n\log n\log\log n\) should be \(|M|\le C n\log^2 n\). The larger bound still passes the pumping check; the error is conservative.

5. **Source off-by-one:** Proposition 4.1 as printed in arXiv v1 says “at most \(\ell\) elements”; the explicit construction gives \(\ell+1\). This is asymptotically harmless and does not affect the \(O(\log p\log\log p)\) bound, but should be recorded in any exact audit.

**What is missing to close the gap:** an explicit polynomial-time (Las Vegas) procedure that, given prime \(p\), samples \(d\), constructs the Stern–Brocot poset \(P_b\), and verifies \(e(P_b)=p\) via Proposition 3.1, together with an explicit absolute constant/density bound. The source supplies the mathematical existence and width-two structure but not that effective packaging.

## Output 523 (msg_1ba28e30e001LxcKduMLf95hgs)

I’ll verify what actually happened before doing anything else: Git state, durable files, and the temp artifacts from the completed audit. I will not re-run the research, post, or commit anything.



## Output 598 (msg_1ba2b473e001fh0y1oJN4C2gu8)

## Recovery inspection

I checked the existing conversation, repository, board, and durable state before doing anything. No research was re-run and no external write action was taken in this turn.

### What actually happened

**Git / repository**
- Worktree: `/home/lubko/soring-fronts/ks-step-audit`
- `git status --short`: **empty** — no tracked or untracked changes in the repo.
- `HEAD`: `f89f6d034a5f4bf36eac5f3c420b1e9a9a1b39c2` (`Advance research note: FO(TC) strategy programs for exact optimal sorting`)
- Detached `HEAD`; `git reflog` shows only that commit.
- **No commits, merges, or pushes were made.**

**Board #301**
- Newest message on page 1 is `2026-11-08T07:34:30.158Z` (Viche Executive, `T(9)=143`).
- No message from this audit exists after 07:42Z, and the `Kravitz` search still returns only the pre-existing posts.
- **No board post was made and therefore no duplicate post needs retracting.**

**Durable task state**
- `/home/lubko/.local/state/soringp1/frontier-ledger.json` has **no `ks-step-audit` entry**. The six `Kravitz` mentions are prior front records about the Fibonacci-threshold work, not this audit.
- No durable record of this audit was written; the audit result exists only in the conversation.

**Local scratch side effects**
- These are local `/tmp/opencode` artifacts only:
  - `ks.pdf`, `ks_src.tar`, `kssrc/`
  - `board301.json`, `arxiv.xml`, `crossref.json`, `ks_meta.json`, `bw.json`
  - `pump_audit.py`, `pump_summary.py`, `cov_check.py`
- No purchases, posts, remote writes, or repository changes.
- The MIT DSpace download attempts were rate-limited HTML responses; they had no external effect.

### Unfinished work

**None.** The previous turn’s audit report was completed in full. Its conclusion still stands:

> **Verdict: SOURCE-GAP** — Kravitz–Sah supports the existence, width-2 structure, and \(O(\log p\log\log p)\) size of \(M\); it does not supply the effective/randomized construction and verification used in #301. The post’s intermediate bound \(\operatorname{cov}(Q)\lesssim 2|M|^2+n^2/2\) is arithmetically too small, but the final pumping inequality survives. The printed Proposition 4.1 has a harmless \(\ell\) vs. \(\ell+1\) off-by-one.

The only remaining external step is the collector’s independent verification and posting, which is intentionally outside this agent’s mandate.
