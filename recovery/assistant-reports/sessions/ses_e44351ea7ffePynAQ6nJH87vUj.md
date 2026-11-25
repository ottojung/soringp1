# antonina-NI8DLbijuuvXZn3LGEWrBo-exceed

Session: ses_e44351ea7ffePynAQ6nJH87vUj
Workspace: /home/lubko/soring-fronts/split-merge-fj-coefficient-limit
Created: 1794151997979; updated: 1794153218147

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 613 (msg_1bbd98945001KK4cKJzfgSpRH1)

## Report: split-merge / Ford–Johnson coefficient front

**Result in one sentence.** I did not disprove  
\[\liminf_{k\to\infty}\frac{m(n_k)}{n_k}\ge c_0,\qquad c_0=\log_2 3-3+\frac1{\ln 2}=0.0276575416\ldots ,\]  
and the exact data now point to the stronger statement that the limit exists and equals \(c_0\) from above. This is still an experimentally supported conjecture, not an all-\(k\) theorem.

No repository, Lean, workflow, or board changes. Worktree remains clean on `billy-dev`.

### 1. Precise claim attacked

With
\[
L(n)=\min_{a+b=n}\bigl[L(a)+L(b)+\lceil\log_2\binom na\rceil\bigr],\qquad
m(n)=L(n)-\log_2(n!),
\]
the front asks whether
\[
\liminf_k m(n_k)/n_k\ge c_0
\tag{C}
\]
or whether \(m(n_k)/n_k<c_0\) for all large \(k\). I tried to refute (C).

### 2. New structural finding: the \(n_k\) question reduces to powers of two

The sequence satisfies the exact identity
\[
n_k=\left\lfloor\frac{4\cdot2^k}{3}\right\rfloor
=\sum_{j\equiv k\pmod2,\;0\le j\le k}2^j
=2^k+n_{k-2}.
\]
Verified exactly for \(k=8,\dots,19\).

Define the excess over the Ford–Johnson line
\[
e(n)=m(n)-c_0 n.
\]
Since \(m(n)=m(a)+m(b)+r(n,a)\) with
\(r(n,a)=\lceil\log_2\binom na\rceil-\log_2\binom na\in[0,1]\),
the same recurrence holds for \(e\). The explicit split \(n_k=2^k+n_{k-2}\) gives the rigorous all-\(k\) inequality
\[
e(n_k)\le e(2^k)+e(n_{k-2})+1.
\]
Iterating along the parity chain,
\[
e(n_k)\le \sum_{j\equiv k\ (2)} e(2^j)+O(k).
\tag{1}
\]
Consequently, if \(e(2^k)=o(2^k)\), then \(e(n_k)=o(n_k)\) and
\[
m(n_k)/n_k\longrightarrow c_0.
\]
More generally, any bound \(e(2^k)\le C(2^k)^\alpha\) with \(\alpha<1\) suffices. This is a genuine reduction: the \(n_k\) front is controlled by the power-of-two subsequence.

Numerically (1) is almost an equality. From the certified k=19 checkpoint:

| \(k\) | \(e(n_k)\) | \(\sum_{j\equiv k}e(2^j)\) | difference |
|---:|---:|---:|---:|
| 14 | 1086.9476 | 1086.7312 | +0.216 |
| 15 | 2079.9285 | 2080.3027 | −0.374 |
| 16 | 3978.9476 | 3979.3030 | −0.355 |
| 17 | 7613.9285 | 7614.2720 | −0.344 |
| 18 | 14567.9476 | 14569.5675 | −1.620 |
| 19 | 27881.9285 | 27883.6267 | −1.698 |

So the additive error is tiny, while the excess itself is \(\sim 10^4\).

### 3. Quantitative obstruction to the strict-drop falsifier

The power-of-two excess is extremely well fitted by a pure power law over ten doublings:
\[
e(2^k)\approx 0.089449\,(2^k)^{0.936325}.
\]
Local exponents for \(e(n_k)\) at \(k=15,\dots,19\) are
\(0.93625,0.93584,0.93625,0.93608,0.93653\), essentially identical to the power-of-two exponent.

Thus
\[
e(2^k)/2^k\asymp (2^k)^{-0.0637}\to0,
\qquad
m(2^k)/2^k=c_0+e(2^k)/2^k\to c_0.
\]
The same holds along \(n_k\):
\[
m(n_k)/n_k-c_0=e(n_k)/n_k
\]
is positive and decreasing by about \(0.9565\) per doubling, exactly as \(n^{-0.0637}\). This is not a sequence heading for a finite crossing of \(c_0\); it is a sequence converging to \(c_0\) from above. A strict drop below \(c_0\) would require \(e(n_k)<0\) eventually, i.e. \(m(n_k)<c_0n_k\), whereas the computed \(e(n_k)\) is positive and increasing like \(n^{0.936}\).

Exact values at powers of two:

| \(k\) | \(m(2^k)/2^k\) | \(e(2^k)\) |
|---:|---:|---:|
| 14 | 0.075914904 | 790.6486 |
| 15 | 0.073803874 | 1512.1230 |
| 16 | 0.071794685 | 2892.5718 |
| 17 | 0.069878377 | 5533.9694 |
| 18 | 0.068056194 | 10590.2645 |
| 19 | 0.066318268 | 20269.3547 |

The minimum of \(m(n)/n\) over all \(3\le n\le 699050\) is \(0.066318268\) at \(n=2^{19}\), still \(2.4\) times \(c_0\). No computed \(n\) has \(m(n)/n<c_0\).

### 4. Failed approaches / exact obstructions

- **Product-of-odd-parts / AM–GM lower bound.** For a node, \(r=\lceil\log_2 C\rceil-\log_2C\) depends only on the odd part \(o\) of \(C\), and \(r\ge 1/(2o\ln2)\) for \(o\ge3\). Since \(\prod_v o_v=\operatorname{odd}(n!)\), AM–GM gives only a bound of the form \(N/(2\ln2\,P^{1/N})\). Zero-cost nodes exist: \(r=0\) exactly when \(\binom{s}{a}\) is a power of two, which by Sylvester–Schur happens only for \(a=1\) or \(b=1\) with \(s\) a power of two. A perfect matching of cherry nodes already has \(n/2\) zero-cost nodes. Then the relaxation gives \(O(1/n)\), not a linear bound. This route cannot prove \(m(n)\ge c_0n\).
- **Direct comparison with Ford–Johnson is not monotone.** \(L(n)<\mathrm{FJ}(n)\) already at \(n=56\) (\(L(56)=254\), \(\mathrm{FJ}(56)=255\)); the minimum of \((L-\mathrm{FJ})/n\) in the computed range is about \(-0.0455\) at \(n=486575\). The \(n_k\) are special precisely because there \(\mathrm{FJ}\) is at its asymptotic best (the \(x\to1\) endpoint, where its excess coefficient is \(c_0\)). A proof must use that special sequence, not a global \(L\ge \mathrm{FJ}\) claim.
- **Finite DP cannot decide the falsifier.** The observed decay factor \(0.9565\) per doubling means the excess \(e/n\) has roughly halved only after 20 doublings. A crossing, if it happened, would be far beyond any \(O(N^2)\) DP. Extrapolation of the observed power law predicts no crossing, but extrapolation is not proof.

### 5. Honest limits

- The k=20 run was started but stopped at \(n=740000\) because the host was heavily loaded; the k≤19 checkpoint values remain the certified data. No new k=20 value is claimed.
- The reduction (1) is rigorous. The statements \(e(2^k)\sim A(2^k)^p\) with \(p\approx0.9363\), and hence \(\lim m(n_k)/n_k=c_0\), are **experiment/conjecture**, not paper proof.
- I did not prove \(m(n)\ge c_0n\) for all \(n\), nor \(e(2^k)=o(2^k)\). That is the remaining decisive obstacle.
- Soundness/completeness: the DP is a sound exact evaluation of the split-merge lower-bound recurrence, not a certificate about the true sorting number \(S(n)\). The split-merge architecture is not complete for comparison sorting (e.g. \(R(12)=32>S(12)=30\) in the exact-merge variant), so the front’s complexity implication concerns an explicit architecture, not a proof about \(S(n)\).

### 6. Reproducibility

The independent check script is
`/tmp/opencode/splitmerge/front_coefficient.py`;
it parses the certified `k18/ckpt_k19.bin` checkpoint and prints all tables above. The script and checkpoint are outside the repository; no tracked files were modified.

## Output 732 (msg_1bbdd676a001YoObjtQDdXGDhO)

## Recovery audit

**State inspected:** conversation, worktree, processes, checkpoints, and recent board digest.

### Effects that actually happened
- No repository change: `git status --porcelain` is empty on `billy-dev`; no commits, no Lean changes.
- No board post: the recent #301 digest shows only other fronts. I did not post this front's report, so there is nothing to duplicate.
- Scratch artifacts only, all outside the repo:
  - `/tmp/opencode/splitmerge/front_coefficient.py` — independent check script.
  - `/tmp/opencode/splitmerge/k20/ckpt_k20.bin` — partial k=20 checkpoint, valid only through `n=750000`.
  - `/tmp/opencode/splitmerge/k18/lf.bin` extended; original saved as `lf_699050.bin.bak`.

### Unfinished work
The only unfinished item was the optional k=20 DP extension. I resumed it from the existing `n=740000` checkpoint, it advanced to `n=750000`, then I stopped it: host load average was ~10 on 4 cores and the remaining run was hours, not minutes. **No k=20 value is claimed or certified.** The k≤19 checkpoint remains the certified data.

### Status of the mathematical report
The prior finding stands unchanged:

- Did **not** disprove \(\liminf_k m(n_k)/n_k\ge c_0\).
- Proved the structural reduction \(e(n_k)\le \sum_{j\equiv k(2)}e(2^j)+O(k)\), so the front is controlled by powers of two.
- Exact k≤19 data fit \(e(2^k)\approx0.089449(2^k)^{0.936325}\), implying empirically \(m(n_k)/n_k\to c_0\) from above, not a strict drop below.
- No all-\(k\) proof; the remaining obstacle is proving \(e(2^k)=o(2^k)\).
- No external side effects were repeated or duplicated.
