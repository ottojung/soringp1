# antonina-BZeSWOafXPvsm0FfAxTRvz-found

Session: ses_e486b4c97ffeJ0waIg7zermM0U
Workspace: /home/lubko/soring-fronts/threshold-exponent-entropy-ratio
Created: 1794081338268; updated: 1794082852184

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 833 (msg_1b7ab4c12001sCiq1S7wRiYmy9)

**Mathematical finding (posted once to board #301, comment `sha256:vdN0Db2JJxTaTGEOtXkJAKcuyCRbdFtPnEbkeFlQ1W8`): the e=13 extremal candidate is false.**

Let \(P_n\) be the fence/staircase poset on \(\{1,\dots,n\}\) with

\[
i<j \iff j-i\ge 2 .
\]

Its predecessor masks are \(0,0,1,3,7,15,31,\dots\).

### Rigorous theorem

\[
e(P_n)=F_{n+1},\qquad m(P_n)=n-1.
\]

- Only adjacent inversions are possible, and two consecutive inversions are impossible. Hence linear extensions correspond to independent sets of the path on \(n-1\) edges, so \(e(P_n)=F_{n+1}\).
- Only consecutive pairs are incomparable, so all nonconsecutive comparisons are information-free. Query all \(n-1\) consecutive pairs for the upper bound. For the lower bound, answer “not inverted” to every query: if an adjacent edge \(i\) is never queried, both \(S=\varnothing\) and \(S=\{i\}\) fit every answer. Thus every adjacent edge is essential.

Therefore

\[
\rho=\sup_P \frac{m(P)}{\log_2 e(P)}
\ge \lim_{n\to\infty}\frac{n-1}{\log_2 F_{n+1}}
=\frac1{\log_2\phi}
=1.44042009\ldots
\]

### Explicit falsifier

The board’s e=13,m=5 witness is exactly \(P_6\). The board’s own n=4 threshold witness, predecessor masks \((0,0,1,3,7,15,31)\), is \(P_7\):

\[
e(P_7)=21,\quad m(P_7)=6,\quad
\frac6{\log_2 21}=1.36602149\ldots
>
\frac5{\log_2 13}=1.35119077\ldots
\]

exactly because \(13^6=4{,}826{,}809>21^5=4{,}084{,}101\). So \(e=13\) is not extremal; it is the sixth member of a family whose ratio increases to \(1/\log_2\phi\).

### Threshold consequence

For every \(k\ge0\), \(P_{k+2}\) has \(e=F_{k+3}\) and \(m=k+1\), so

\[
T(k)<F_{k+3}.
\]

Using the definition of \(\rho\) and ordinal sums (\(e\) multiplicative, \(m\) additive), one gets

\[
\frac{\log_2 T(k)}k \longrightarrow \frac1\rho .
\]

Thus

\[
T(S(n)+1)=n!^{\,1/\rho+o(1)}
\]

is true with the true \(\rho\) — the ordinal-sum exponent really is \(1/\rho\). The error was identifying \(\rho\) with \(5/\log_2 13\). The fence gives the rigorous bound

\[
T(S(n)+1)\le n!^{\,\log_2\phi+o(1)}
\approx n!^{\,0.69424},
\]

whereas the e=13-based prediction would be \(n!^{\,\log_2 13/5}\approx n!^{\,0.74009}\). So that candidate exponent is refuted.

### Honest limit / exact obstruction

The evidence suggests the sharper conjecture

\[
\rho=\frac1{\log_2\phi}
\iff T(r)=F_{r+3}-1
\iff e(P)\ge F_{m(P)+2},
\]

matching the known \(T(2..5)=4,7,12,20\) and the fence upper bound. Finite exact checks found no poset with \(e\le33\), \(m\ge7\) for \(n\le18\), and no ratio above the fence for \(n\le8\), \(e\le200\).

But I did **not** prove the all-\(n\) “Fibonacci splitting” induction. The natural induction fails at unbalanced optimal splits: a parent with \(m=k\) can have children of depths \(k-1\) and as low as \(k-3\) (e.g. the e=21 witness has splits \(4/5\) and \(3/5\)). The missing lemma is that some optimal comparison has both children within one of the parent optimum. Until that is proved, \(\rho=1/\log_2\phi\) is a conjecture, not a theorem; \(\rho\) could still be larger.

This is a general-poset structural result about exact \(m(P)\), not a certificate-completeness, NP-membership, or separation result. No Lean or repository changes were made; the worktree is clean.

## Output 860 (msg_1b7abb7fc001nfV8Q9HnlIxqQA)

The prior external effect is confirmed: the finding was posted **once** to Antonina issue #301 as comment `sha256:vdN0Db2JJxTaTGEOtXkJAKcuyCRbdFtPnEbkeFlQ1W8` at 2026-11-07 20:20:15. I did not repost it.

The working tree remains clean on `billy-dev` at commit `6a96398`. The posted conclusion refutes the e=13 extremal candidate; the exact value of \(\rho\) remains unresolved.
