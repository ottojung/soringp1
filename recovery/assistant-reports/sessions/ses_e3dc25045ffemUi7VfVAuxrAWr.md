# antonina-m0RXW3w3oCPNAlfgipzJkK-adoration

Session: ses_e3dc25045ffemUi7VfVAuxrAWr
Workspace: /home/lubko/soring-fronts/height-three-excess-root-equivalence
Created: 1794260185212; updated: 1794261597958

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 522 (msg_1c2518b5e001O6twrcrouFX2NE)

**Bottom line.** I attacked the front’s proposed separation via disjoint unions, and found a genuine error in that route. It does **not** produce a height-three family with excess growing faster than \(E(n)\). The corrected composition lemmas give a precise no-bootstrap obstruction: any counterexample must be a *prime* height-three poset, not an ordinal/disjoint composition. I proved no equivalence and no separation.

## The attempted falsifier

Let
\[
\delta(P)=F(P)-\lceil \log_2 e(P)\rceil .
\]
Using the board’s excess-3 witness \(K=A_{13}\oplus A_{14}\):
\[
|K|=27,\quad e(K)=13!\,14!,\quad \lceil\log_2 e(K)\rceil=69,\quad F(K)=S(13)+S(14)=72,
\]
so \(\delta(K)=3\). The hope was that \(F(A\sqcup B)\ge F(A)+F(B)\) would make \(t\) disjoint copies satisfy \(\delta\ge 3t\), giving linear excess while \(E(N)=o(N)\).

**This fails because extension counts do not multiply under disjoint union:**
\[
e(A\sqcup B)=\binom{a+b}{a}e(A)e(B).
\]
For \(t\) copies of \(K\),
\[
e_t=\frac{(27t)!}{\binom{27}{13}^t}.
\]
Numerically,
\[
\begin{array}{c|c|c|c}
t & tF(K) & \lceil\log_2 e_t\rceil & \text{useful excess}\\ \hline
1 & 72 & 69 & 3\\
2 & 144 & 189 & \text{none}\\
10 & 720 & 1555 & \text{none}
\end{array}
\]
The interleaving entropy \(\sim N\log t\) overwhelms the superadditivity gain.

## Corrected all-\(n\) composition lemmas

- **Series/ordinal sum:** \(F(A\oplus B)=F(A)+F(B)\) and \(e(A\oplus B)=e(A)e(B)\), hence
  \[
  \delta(A\oplus B)=\delta(A)+\delta(B)+\eta,\qquad \eta\in\{0,1\}.
  \]
  Series composition adds excess; it never amplifies it. Height \(\le3\) permits at most three such factors.

- **Parallel/disjoint union upper bound:**
  \[
  \delta(A\sqcup B)\le \delta(A)+\delta(B)+\max(|A|,|B|).
  \]
  Proof: sort \(A\), sort \(B\), merge two sorted orders, and use \(\binom{a+b}{a}\ge 2^{\min(a,b)}\).

- **Parallel lower bound:**
  \[
  \delta(A\sqcup B)\ge \delta(A)+\delta(B)-\log_2\binom{a+b}{a}-3.
  \]
  So positive amplification requires the component excesses to exceed the interleaving entropy, which is at least \(\min(|A|,|B|)\).

Consequently ordinal, disjoint, and blow-up compositions cannot turn the height-two excess \(E(n)\) into a larger independent height-three excess. A separation would have to come from a **prime** height-three poset.

## Finite exhaustive checks

- \(n=6\): all \(130{,}023\) labelled posets; among the \(4{,}117\) of height \(\le3\), max \(\delta=1\).
- \(n=7\): all \(6{,}129{,}859\) labelled posets via a full minimax DP; among height \(\le3\), max \(\delta=1\). Maximizer: successor mask \([30,0,0,0,0,0,0]\), \(e=1008\), \(F=11\), \(\lceil\log_2 e\rceil=10\).

Both maxima are attained at height two; no height-three surplus appeared. Since \(E(6)=E(7)=0\), these are consistent with the endpoint bound (RHS \(=1\)). These are finite checks, not an all-\(n\) proof.

## Honest status and limits

- \(H_3(n)\ge E(n)\) is immediate from the one-edge height-two family, so unbounded \(E\) forces unbounded height-three excess.
- The converse, or a constant-multiple equivalence, remains **open**. I did not prove either.
- Fredman’s \(\log_2 e(P)+O(n)\) bound only gives the trivial universal \(O(n)\) additive excess; the SUPI constant-factor results (Kahn–Kim, Cardinal et al.) do not bound additive excess.
- These are general-poset minimax facts, not certificate-completeness results and not root-reachable states. No consequence for `SORT-BOUND-U` or \(S(n)\) follows.
- The naive disjoint-union refutation of the board’s endpoint conjecture is also invalid for the same multinomial reason.

I posted this correction and obstruction to board #301 (2026-11-09 21:57Z). The repository worktree is clean at `6a96398`; no Lean or repository changes were made. Scratch reproduction is in `/tmp/opencode/h3excess/`.

## Output 592 (msg_1c2531e030016BfEdi8KLHN0M0)

State inspection completed; no duplicate external actions were taken.

## What actually happened

- **Board #301:** the intended update exists exactly once, at `2026-11-09T21:57:51.029Z`, authored `SoringP1 frontier: height-three-excess-root-equivalence`, containing the disjoint-union correction and no-separation result. I did **not** repost it.
- **Git:** worktree is clean at `6a96398`; no commits, branches, Lean files, or repository changes were made.
- **Host:** `billy-dev`.
- **Scratch artifacts:** present under `/tmp/opencode/h3excess/` (`verify_excess.py`, `exhaustive_n6.py`, `n7.go`, `board_post.txt`, etc.).
- **Durable ledger:** the front entry `height-three-excess-root-equivalence` still shows `status: running`, `finished_at: null`. That is the keeper’s record to finalize when this agent session exits; I did not edit it manually.

## Mathematical result already recorded

The attempted disjoint-union separation is false: for \(t\) copies of the excess-3 witness \(K=A_{13}\oplus A_{14}\),
\[
e(K^{\sqcup t})=\frac{(27t)!}{\binom{27}{13}^t},
\]
so the interleaving entropy is \(69,189,1555\) for \(t=1,2,10\), while \(tF(K)=72,144,720\). The superadditivity lower bound gives no positive excess for \(t\ge2\).

Corrected composition facts:
- series: \(\delta(A\oplus B)=\delta(A)+\delta(B)+\eta\), \(\eta\in\{0,1\}\);
- parallel upper: \(\delta(A\sqcup B)\le\delta(A)+\delta(B)+\max(|A|,|B|)\);
- parallel lower: \(\delta(A\sqcup B)\ge\delta(A)+\delta(B)-\log_2\binom{a+b}{a}-3\).

Hence only a **prime** height-three poset could separate height-three excess from \(E(n)\). No equivalence or separation was proved. Exhaustive checks through \(n=7\) found maximum excess \(1\), attained only at height two.

No unfinished research work remains from the interrupted turn.
