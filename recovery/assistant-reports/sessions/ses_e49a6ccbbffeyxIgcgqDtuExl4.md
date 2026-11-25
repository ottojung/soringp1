# antonina-1sJ7HnKaNQ7GBlcryodBfN-emboli

Session: ses_e49a6ccbbffeyxIgcgqDtuExl4
Workspace: /home/lubko/soring-fronts/exec-winning-frontier-logdegree-20261107
Created: 1794060661636; updated: 1794063493136

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 139 (msg_1b67878e7001RHe3cHMP5fVDmB)

## Verdict first

The question splits cleanly:

1. **A fixed Δ-regular/expander-like pattern repeated across interfaces does not preserve the barrier — for any Δ.** Its entropy is at most \(2^{O(n\log s)}=2^{O(n\log n)}\), independent of Δ, which is far below \(2^{(1/4-o(1))n(\log_2 n)^2}\).
2. **An independent Δ-regular ensemble does preserve it.** For \(\Delta=c\log_2 s\) one gets \(2^{(c/4-o(1))n(\log_2 n)^2}\); with the maximal budget-allowed \(\Delta=\log_2 s-O(1)\) one recovers the stated \(1/4\) coefficient.

So the barrier is an **entropy-per-interface** statement, not a degree statement. The fixed-pattern version is false; the ensemble version is essentially the original construction with a degree constraint.

I did not modify, commit, or post anything.

---

## 0. Accounting and the true degree ceiling

Let \(s=L=2^r\), \(n=s^2\), \(r=\log_2 s\), so \(\log_2 n=2r\). Put
\[
t_0=s(L-1)=n-s,\qquad 
B=(s-1)+(n-1)r,
\]
\[
M=(L-1)(s^2-s).
\]
For \(k=C(n)+d(n)=\lceil\log_2 n!\rceil+d(n)\), \(d=o(n)\),
\[
m_t=k-t_0-B
= nr-(1+\log_2 e)n+O(r)+d(n)
= nr-2.4427\,n+O(r)+o(n).
\]
Hence the maximal degree that still leaves the \(B\)-strategy inside budget is
\[
\Delta_{\max}
=\left\lfloor\frac{m_t}{s(L-1)}\right\rfloor
=r-2.4427+o(1).
\]
At \(k=S(n)\), Sergeev gives \(S(n)-C(n)=O(n/(\log n)^{1/5})=o(n)\), so the same formula holds. **Thus \(\Delta=\log_2 s\) exactly overshoots the budget by about \(2.4427\,n\) edges; one must use \(\Delta=\log_2 s-O(1)\), still \(\Theta(\log s)\).**

This is already a correction to the premise: the loose bound \(2^{O(\Delta n\log s)}\) suggests \(\Delta=\Theta(\log s)\) is marginal, but the actual entropy is governed by \(2^{\Theta(\Delta n\log(s/\Delta))}\). Since \(\log(s/\Delta)=r-\log r-O(1)\) when \(\Delta=\Theta(r)\), the \(-\log r\) term produces the stated \(o(1)\) and the constant is what matters.

---

## 1. Existence and explicit construction

**[definition/deduction]** For each interface \(i=0,\dots,L-2\), choose a bipartite graph
\[
G_i\subseteq [s]\times[s]\setminus\{(x,x):x\in[s]\},
\]
and add edges
\[
(i,x)\longrightarrow(i+1,y)\qquad ((x,y)\in G_i).
\]
All extra edges go forward one level. The vertical chains
\[
(0,x)<(1,x)<\cdots<(L-1,x)
\]
are always present and contribute \(t_0\) edges.

A single explicit Δ-regular graph is trivial: take cyclic shifts
\[
G_i=\{(x,x+a\bmod s):x\in[s],\ a=1,\dots,\Delta\}.
\]
This is Δ-regular, diagonal-free, and all edges are forward.

But a **single** graph repeated gives only one state. For the family with entropy, use the following explicit construction:

**[construction]** At each interface choose an ordered \(\Delta\)-tuple of derangements
\[
(\sigma_{i,1},\dots,\sigma_{i,\Delta}),\qquad \sigma_{i,j}\in S_s,\ \sigma_{i,j}(x)\ne x,
\]
and let
\[
G_i=\bigcup_{j=1}^{\Delta}\operatorname{graph}(\sigma_{i,j}).
\]
Each \(G_i\) has max degree at most \(\Delta\) on both sides and no diagonal. This is an explicitly parameterized family; no random oracle is needed. It is “structured” but not a fixed pattern.

Expansion is irrelevant to the counting. A fixed expander is the worst case for entropy; an ensemble of random Δ-regular graphs is expander-like with high probability and has the same entropy order.

---

## 2. Counting: the encoding lemma and the entropy

**[deduction — encoding lemma]** A labelled poset \(P(G_0,\dots,G_{L-2})\) determines each \(G_i\) uniquely. Indeed, the only paths from level \(i\) to level \(i+1\) have length one, because every edge raises the level. Hence the comparabilities between consecutive levels are exactly the vertical edges plus \(G_i\). Therefore distinct tuples give distinct labelled posets.

**[deduction — reachability]** All edges are forward, so adding them in any order never creates an implied adjacent-level relation. Thus each tuple is reachable by exactly
\[
t=t_0+\sum_{i=0}^{L-2}|G_i|
\]
legal comparison outcomes.

**[deduction — winning]** The \(s\) vertical chains survive in every \(P\). The balanced winner tournament merges their heads in at most
\[
B=(s-1)+(n-1)\lceil\log_2 s\rceil
\]
further comparisons. Extra relations only help, so \(F(P)\le B\).

### Ensemble count

Let \(D_s=s!\sum_{j=0}^s(-1)^j/j!\) be the number of derangements. For one interface, the number of distinct \(G_i\) obtainable from ordered Δ-tuples is at least
\[
N_i\ \ge\ \frac{D_s^{\Delta}}{\Delta^{s\Delta}}.
\]
Reason: there are \(D_s^\Delta\) tuples. A fixed simple graph of max degree at most Δ has at most \(\Delta^s\) perfect matchings (choose an image for each left vertex among its \(\le\Delta\) neighbours), hence at most \((\Delta^s)^\Delta=\Delta^{s\Delta}\) ordered Δ-tuples of perfect matchings mapping to it.

Using \(D_s\ge s!/e\),
\[
\log_2 N_i
\ge \Delta\log_2(s!)-O(\Delta s)-s\Delta\log_2\Delta
= \Delta s\log_2\frac{s}{\Delta}-O(\Delta s).
\]
For all \(L-1\) interfaces, the number of labelled posets is at least
\[
\prod_i N_i\ \ge\ 2^{(L-1)\Delta s\log_2(s/\Delta)-O(nr)}.
\]
Each isomorphism class contains at most \(n!\) labelled posets, so the number of nonisomorphic states is at least
\[
2^{(L-1)\Delta s\log_2(s/\Delta)-O(nr)-\log_2 n!}.
\]
Since \(\log_2 n!=2nr+O(\log n)\),

\[
\boxed{\ \log_2\#\text{classes}
\ \ge\ \Delta n\log_2\frac{s}{\Delta}-O(nr\log r)\ }.
\]

Now set \(\Delta=c r\):
\[
\Delta n\log_2\frac{s}{\Delta}
=c r\,n\,(r-\log_2(cr))
=c n r^2-O(nr\log r).
\]
Since \(n r^2=\frac14 n(\log_2 n)^2\),
\[
\boxed{\log_2\#\text{classes}\ \ge\ \left(\frac c4-o(1)\right)n(\log_2 n)^2.}
\]

Consequences:

- \(\Delta=c\log_2 s\) for any fixed \(c>0\) gives a barrier with coefficient \(c/4\).
- \(\Delta=(1-o(1))\log_2 s\) gives the stated \((1/4-o(1))\) coefficient.
- \(\Delta=\omega(1)\) but \(o(\log s)\) gives \(2^{\Delta n r-O(nr)}\), which beats \(2^{O(n\log n)}\) whenever \(\Delta\to\infty\).
- \(\Delta=O(1)\) gives only \(2^{O(nr)}=2^{O(n\log n)}\), so constant degree fails.

**Correction to the premise:** “\(\Delta=\Omega(\log n)\)” is sufficient for the literal \((1/4)\) exponent only with constant \(1\); qualitatively, any unbounded \(\Delta\) already beats the \(2^{O(n\log n)}\) enumeration class. The sharp statement is: constant Δ fails, \(\Delta\to\infty\) beats \(2^{O(n\log n)}\), and \(\Delta=(1-o(1))\log_2 s\) recovers the full \(1/4\) coefficient.

### Fixed-pattern collapse

Now suppose each interface is restricted to a fixed base graph up to relabelling:
\[
G_i\in\{\pi H\sigma:\pi,\sigma\in S_s\}
\]
for a fixed \(H\), or more generally a catalogue \(\mathcal K\) with \(|\mathcal K|=K_0\). Then per interface there are at most \(K_0(s!)^2\) possibilities, so the total number of labelled posets is at most
\[
\bigl(K_0(s!)^2\bigr)^{L-1}.
\]
Hence
\[
\log_2\#\text{classes}
\le (L-1)\bigl(\log_2 K_0+2\log_2(s!)\bigr)
=O(n\log s+L\log K_0).
\]
If \(\log_2 K_0=O(s\log s)\) — which includes a fixed pattern, a polynomial catalogue, or a catalogue of size \(2^{O(s\log s)}\) — this is
\[
O(n\log s)=O(nr)=O(n\log n),
\]
which is \(o(nr^2)\). Therefore the fixed-pattern family **cannot** supply \(2^{(1/4-o(1))n(\log_2 n)^2}\) states for large \(r\).

This is the collapse. It does not rely on large automorphism groups; even if every member has trivial automorphism group, the labelled count is already too small. Explicitly:

- **Same \(H\) at every interface:** exactly one labelled poset, hence one isomorphism class. Its automorphism group contains the diagonal action of the translations of \(H\) if \(H\) is cyclic; for \(H\) a cyclic-shift graph, \(|\operatorname{Aut}(P)|\ge s\).
- **Per-interface translations of a fixed \(H\):** at most \(s^{L-1}\) labelled posets, and since the diagonal translation group of order \(s\) acts on every member, at most \(s^{L-2}\) isomorphism classes.
- **Per-interface arbitrary left/right permutations:** at most \((s!)^{2(L-1)}\) labelled posets, hence at most that many classes.

The exact threshold for a “structured” family to survive is: the per-interface description must carry
\[
\Omega(s r^2)
\]
bits, or more generally \(\varepsilon s r^2\) bits for a positive coefficient. A fixed pattern plus \(O(s\log s)\) bits of relabelling/seed information is short by a factor \(r\).

---

## 3. Winning and the exact budget

At depth
\[
t=t_0+m,\qquad m=\sum_i|G_i|,
\]
the remaining budget is \(k-t\). If \(m\le m_t\), then
\[
t\le k-B,\qquad k-t\ge B,
\]
so every state is winning.

For the Δ-regular family, \(m=\Delta s(L-1)=\Delta\,n(1+o(1))\). Choosing \(\Delta=\Delta_{\max}\) leaves slack
\[
m_t-m< s(L-1)=O(n).
\]
Thus at depth \(t=k-B\) one has exactly \(B\) comparisons left; with the regular family one has \(B+O(n)\) left.

For \(k=C(n)\): \(m_t=C(n)-t_0-B\).
For \(k=S(n)=C(n)+d(n)\): \(m_t=S(n)-t_0-B\), with \(d(n)=o(n)\) by Sergeev. The construction is asymptotic and gives no effective finite threshold at \(k=S(n)\), exactly as in the original theorem.

---

## 4. Obstruction: what the collapse excludes

**[paper proof — dichotomy]**

- If the family is a **fixed skeleton up to per-interface relabelling**, the frontier has at most \(2^{O(n\log s)}\) states. This excludes:
  - “enumerate all relabellings of one expander pattern”;
  - “enumerate a small catalogue of motifs with independent column permutations”;
  - “fixed local rule / short PRNG seed per interface” with seed length \(o(s\log s)\).

  It does **not** exclude a method that is correct only on a fixed skeleton; it only says counting cannot produce a barrier there.

- If the family is an **independent Δ-regular ensemble** with \(\Delta=c\log_2 s\), the frontier is \(2^{(c/4-o(1))n(\log_2 n)^2}\). This rules out any method that must enumerate all reachable winning states when the interface family has that much entropy. With \(\Delta=\log_2 s-O(1)\), it recovers the original \(1/4\) exponent.

The positive ensemble is a **subset** of the original arbitrary-edge family. Therefore it gives no lower bound stronger than the original theorem; it only adds the degree restriction. It does not touch selective minimax search, proof-number search, state compression, parametric certificates, or any method that does not list the frontier.

**For #47/#48 and exact evaluation: no change.** This remains static graph-enumeration arithmetic, not a time or space lower bound for computing \(S(n)\).

---

## 5. Exact finite witnesses

All values below are exact integer computations; they are finite evidence, not the asymptotic proof.

### 5.1 Budget table

| \(s=L\) | \(n\) | \(r\) | \(k=C(n)\) | \(t_0\) | \(B\) | \(M\) | \(m_t\) | \(\Delta_{\max}\) | \(m=\Delta_{\max}s(s-1)\) | \(t=t_0+m\) | \(k-t\) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 64 | 3 | 296 | 56 | 196 | 392 | 44 | 0 | 0 | 56 | 240 |
| 16 | 256 | 4 | 1684 | 240 | 1035 | 3600 | 409 | 1 | 240 | 480 | 1204 |
| 32 | 1024 | 5 | 8770 | 992 | 5146 | 30752 | 2632 | 2 | 1984 | 2976 | 5794 |
| 64 | 4096 | 6 | 43251 | 4032 | 24633 | 254016 | 14586 | 3 | 12096 | 16128 | 27123 |
| 128 | 16384 | 7 | 205748 | 16256 | 114808 | 2064512 | 74684 | 4 | 65024 | 81280 | 124468 |
| 256 | 65536 | 8 | 954037 | 65280 | 524535 | 16646400 | 364222 | 5 | 326400 | 391680 | 562357 |

For \(s=8\), the regular degree ceiling is \(0\), but a **Δ=1 partial-matching** family can realize exactly \(m=44\) edges: then \(t=100\) and \(k-t=196=B\). So Δ-bounded (not regular) is the right notion at small \(s\).

The key finite falsification: at \(s=L=16\), \(\Delta_{\max}=1\), not \(\log_2 s=4\). The exact budget forbids Δ=4: \(4\cdot16\cdot15=960>409\). So the suggested \(s=16\) instance **cannot probe the \(\Delta=\Theta(\log s)\) regime at all**. The first square instance with \(\Delta_{\max}=2\) is \(s=32\); with \(\Delta=3\) is \(s=64\); with \(\Delta=4\) is \(s=128\).

### 5.2 Fixed-pattern versus original counts (bits)

“Fixed-pattern upper” is \((s!)^{2(L-1)}\), a generous upper bound on the labelled states from a fixed base plus arbitrary per-interface left/right permutations. “Original lower” is \(\binom{M}{m_t}/n!\).

| \(s\) | fixed-pattern \(\log_2\) upper | original classes \(\log_2\) lower | asymptotic target \(n r^2\) |
|---:|---:|---:|---:|
| 8 | 214.19 | \(-101.36\) | 576 |
| 16 | 1327.50 | 148.99 | 4096 |
| 32 | 7295.12 | 4188.14 | 25600 |
| 64 | 37295.39 | 37296.16 | 147456 |
| 128 | 181905.08 | 257667.89 | 802816 |
| 256 | 858838.11 | 1574033.50 | 4194304 |

Exact integer inequalities verified:

\[
\binom{392}{44}<64!
\]
so \(s=L=8\) produces no nonisomorphic states even before any degree restriction.

\[
(16!)^{30}<\binom{3600}{409},
\qquad
\binom{3600}{409}>2^{148}\,256!.
\]
The second is the doc’s finite witness; the first shows the fixed-pattern bound is \(2^{505}\) below the original labelled count at \(s=16\). But at \(s=16\), the fixed-pattern bound \(2^{1327.5}\) is still **larger** than the original finite class count \(2^{149}\), so \(s=16\) does **not** refute the fixed-pattern barrier. The doc’s \(n=224\) witness is even less decisive here: \((16!)^{26}=2^{1150.5}\) versus original classes \(2^{39.6}\).

The collapse appears later:

\[
(64!)^{126}\,4096!<\binom{254016}{14586},
\]
\[
(128!)^{254}\,16384!<\binom{2064512}{74684}.
\]
The second is decisive: the fixed-pattern family has at most \(2^{181905}\) labelled states, while the original family has at least \(2^{257667}\) nonisomorphic states. At \(s=256\): fixed upper \(2^{858838}\) versus original lower \(2^{1574033}\).

### 5.3 Positive ensemble: finite numerical trend

For the explicit derangement family with \(\Delta=\Delta_{\max}\), numerical evaluation of the lower-bound formula gives:

| \(r\) | \(s\) | \(\Delta_{\max}\) | lower \(\log_2\) classes | \(n r\) | beats \(2^{O(n\log n)}\)? |
|---:|---:|---:|---:|---:|---|
| 7 | 128 | 4 | \(2.73\times10^4\) | \(1.15\times10^5\) | no |
| 8 | 256 | 5 | \(4.33\times10^5\) | \(5.24\times10^5\) | no |
| 9 | 512 | 6 | \(3.48\times10^6\) | \(2.36\times10^6\) | yes |
| 12 | 4096 | 9 | \(7.37\times10^8\) | \(4.83\times10^7\) | yes |
| 20 | \(2^{20}\) | 17 | \(2.28\times10^{14}\) | \(2.10\times10^7\) | yes |
| 30 | \(2^{30}\) | 27 | \(6.73\times10^{20}\) | \(1.04\times10^{21}\) | yes |

The ratio to \(n r^2\) rises from \(0.03\) at \(r=7\) to \(0.16\) at \(r=9\), \(0.31\) at \(r=12\), \(0.52\) at \(r=20\), \(0.65\) at \(r=30\), and tends to \(1\). This is finite numerical evidence for the asymptotic statement, not an exact finite certificate.

---

## 6. Honest outcome

- **Fixed repeated pattern:** a genuine no-go. The barrier does not survive; the family has only \(2^{O(n\log s)}\) labelled states regardless of Δ. This excludes “fixed expander skeleton + relabelling” and short-seed structured enumerations as a route to the barrier.
- **Independent Δ-regular ensemble:** the barrier survives, with the corrected threshold: constant Δ fails; any unbounded Δ beats \(2^{O(n\log n)}\); \(\Delta=(1-o(1))\log_2 s\) recovers the stated \(1/4\) coefficient. This is a useful quantitative refinement, but it is not a new barrier: the ensemble is a subset of the original arbitrary-edge family.
- **For #47/#48 or exact \(S(n)\) evaluation:** no methodological change. This is graph-enumeration arithmetic.

So the honest conclusion is: **the fixed-pattern version is false, the ensemble version is true but essentially the original construction, and nothing new is excluded beyond the fixed-skeleton class. Stop here.**
