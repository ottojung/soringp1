# antonina-1PKBOuQSpNue6NVm8qtRRd-wretched

Session: ses_e489414cfffetFJsPH7o0AWH3K
Workspace: /home/lubko/soring-fronts/exec-sergeev-constant-reconstruction-20261107
Created: 1794078665612; updated: 1794078708946

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b76bed3d0017zAoqqAnG660jG)

I’ll trace the cited proof and its dependencies in the supplied PDF, then separate estimates with explicit constants from any step whose proof leaves a constant or finite range unspecified. I’ll keep this to a self-contained audit—no repository edits or board post.

## Output 22 (msg_1b76c07ef001ncZoqzW31lUs86)

## Result

The proof gives a route to an explicit asymptotic bound for sufficiently large \(a\), but not the requested all-\(a\) result. The first finite-range obstruction is explicit in the text: after proving Lemma 4 only for \(s\ge20\), Theorem 2 selects \(s=\lceil(2/5)\log_2 a\rceil\) for \(a\ge100\). At \(a=100\), this is \(s=3\), not \(s\ge20\). Thus the invocation of Lemma 4 is unsupported throughout the stated \(100\le a<2^{47.5}\) range. Separately, the assertion for \(a<100\) relies on “sufficiently large” unspecified \(O\)-constant and supplies no finite verification.

I did not find a justified way to turn the proof into concrete \(C,a_0\) and a finite bound for smaller \(a\). The central calculation (44) does support an explicit *conditional* asymptotic estimate if Lemma 4 is available at the chosen \(s\); the paper’s stated range does not establish that condition.

## Quantitative trace

Page references below are PDF page numbers; equation numbers are those printed in the paper.

Theorem 2 (p. 28) sets
\[
\gamma=\tfrac15,\qquad
s=\lceil 2\gamma\log_2 a\rceil=\lceil\tfrac25\log_2a\rceil,\qquad
d=2^s,\quad
\epsilon=\frac1{25\cdot2^s},
\]
and uses Lemma 4, which requires \(s\ge20\) (p. 27). Since \(2^s\ge a^{2/5}\), this parameter requirement holds only when
\[
a^{2/5}\ge2^{20},\quad\text{i.e.}\quad a\ge2^{50}.
\]
The paper instead assumes \(a\ge100\). At \(a=100\), \(s=3\); indeed the gap persists through \(a<2^{47.5}\), where \(s<20\).

For \(a\ge2^{50}\), follow the displayed substitutions on pp. 28–29. Put
\[
\phi=\log_2\!\left(\frac{m\epsilon}{4a^2}\right)
=\log_2m-s-\log_2a-\log_2 100.
\]
Then the requirement \(\phi>0\) follows from \(m\ge2^{a/4}\), \(s\le(2/5)\log_2a+1\), and hence
\[
\phi\ge a/4-\tfrac75\log_2a-\log_2 200>0.
\]
Also \(m\le2^{a/2}\) and \(s\ge(2/5)\log_2a\) give
\[
m\epsilon \le \frac{2^{a/2}}{25a^{2/5}},
\]
so the paper’s stated \(m\epsilon\ge2^{a/4}/(50a^{2/5})\) is not a consequence of the allowed \(m\)-range; it is a lower bound, not an upper bound. This matters because the proof’s displayed control of the \(m\)-dependent error terms is not justified uniformly just by that inequality.

Lemma 2 (pp. 9–13), with depth \(h=2s+3\), width \(w\le s+4\), and \(d=2^s\), yields (18):
\[
P_m(r+y_i+\tfrac{(r+2)\phi2^\phi}{m})\ge
v_i2^r-\frac{R}{\epsilon}m2^{\phi+2}
-R2^r e^{-\frac{\epsilon}{2R}
(\phi/[w(d+1)(h+1)]-2)}.
\]
The theorem maps this to \(P_m(a)\) by choosing \(r+y_i\le a-\frac{(r+2)\phi2^\phi}{m}\le r+y_i+1/d\). The printed derivation then asserts the error terms are \(O(2^a/a^2)\) and \(2^{a-O(a s^{-2}2^{-2s})}\), and concludes the relative loss is \(O(a^{-1/5})\). Those are asymptotic estimates, not numerical bounds: constants are not evaluated, and the assertion that the condition (17) is “automatically satisfied” is not accompanied by its numerical verification. More importantly, none repairs the \(s\ge20\) gap.

The parameter mismatch is consequential: at the cutoff \(a=2^{50}\), \(s=20\), while \(2^s\) is already very large. The proof could plausibly be made quantitative for \(a\ge2^{50}\), but that does not establish Theorem 2 as stated for \(a\ge100\), nor does it by itself give a finite bound for \(a<2^{50}\).

## Eq. (44), Theorem 2, and Corollary 2

On p. 27, Lemma 4’s vector is
\[
v_i=(1-\lambda)2^{y_i+1/2},\qquad u=v/2,
\]
with \(\lambda=20\cdot2^{-s/2}+64\cdot2^{-s}\) and \(\epsilon=1/(25\cdot2^s)\). The paper states the resulting simplex inclusions only for \(s\ge20\).

Equation (44) (p. 28) is
\[
P_m(a)\ge 2^{a+1/2}-O(a^{-1/5}2^a).
\]
Its derivation proves this asymptotically from Lemma 2 and Lemma 4, then handles \(a<100\) by asserting the same inequality with a sufficiently large hidden constant. No value of that constant, individual \(P_m(a)\) values, or finite enumeration method/bound is supplied. Thus the small range cannot be certified from the paper alone.

Corollary 2 (p. 29) follows from the identity \(Q_{2m}(a)\ge P_m(a-\tfrac12)\), equation (6), by substituting \(a-\tfrac12\) into (44). Its stated lower bound is therefore dependent on the same unquantified and finite-range gaps. Theorem 3 then invokes Corollary 2 to insert groups, so its proof inherits those gaps if interpreted as a fully explicit finite-parameter proof.

## First non-quantifiable step and what would fix it

The first exact finite-range failure is the use of Lemma 4 outside its hypothesis \(s\ge20\). Before that, the construction on pp. 24–27 supplies parameter inequalities, but Lemma 4’s simplex verification is expressly restricted to \(s\ge20\). The later small-\(a\) step is independently non-quantifiable: “sufficiently large values” of the \(O\)-constant on p. 28 provides no numerical constant.

To make the requested result effective, one would need:

1. A corrected, numerically checked version of the Lemma 2 substitution for all \(a\) above a valid cutoff (at least \(2^{50}\) if using the stated Lemma 4 hypothesis), including explicit bounds for \(\phi\), condition (17), \(R\), and both error terms.
2. A finite certificate for every remaining parameter range: either Lemma 4 verified for smaller \(s\), or explicit lower bounds for the relevant \(P_m(a)\) (and the corresponding shifted values needed by Corollary 2), with a rigorous finite method and a stated bound on its coverage.
3. A corrected treatment of the \(m\epsilon\) estimates: the printed lower bound does not establish the uniform upper control needed for the displayed error estimate over \(2^{a/4}\le m\le2^{a/2}\).

**Conclusion:** This audit neither refutes the asymptotic theorem nor supplies concrete \(C,a_0\). It identifies the exact unsupported parameter range and the missing finite data/lemmas needed to quantify it.
