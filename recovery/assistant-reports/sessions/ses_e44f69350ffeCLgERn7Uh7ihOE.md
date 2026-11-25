# antonina-O6JJe0Tn4Tsgvg1aVUkF3f-bloodshed

Session: ses_e44f69350ffeCLgERn7Uh7ihOE
Workspace: /home/lubko/soring-fronts/determinant-representation-sortnumber
Created: 1794139319540; updated: 1794140669223

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 27 (msg_1bb0992ec001ZSKDm1r8tLaoLj)

I'll start by inspecting the environment and durable records to see what already happened before doing anything external.

## Output 96 (msg_1bb09e7ea001lgha2MzOlieZ3H)

The front is `determinant-representation-sortnumber` (status `running`), and the worktree is clean with no local edits. No board post for it appears in the recent digest. I'll check earlier algebraic-front work before deriving anything new.

## Output 213 (msg_1bb0e5199001yRqeW21MmiTsuY)

A crucial lead: Shah (2022) proves binary matrices realize every integral value up to Ω(2^n/n). Since S(n) = O(n log n), this may cap determinant rank at O(n). I'll verify the exact statement.

## Output 279 (msg_1bb0f65b2001aZ6KGw274yJYFE)

The Shah construction is explicit in the matrix rows; I'll implement it to check the determinant-rank cap concretely, including all known exact S(n) values.

## Output 317 (msg_1bb11b711001sml4hMo9Hu6t0P)

I have a decisive result: Shah's published theorem plus the elementary bound S(n) ≤ n(n−1)/2 caps the 0/1 determinant order at O(n), so the proposed superpolynomial determinant-rank lower bound cannot exist. I'll verify the posting interface and avoid duplicating any prior side effect.

## Output 385 (msg_1bb1565e5001lQjOmq52P2qvj0)

Shah's bound is exponential in the matrix order, so the rank cap is much stronger than linear: for target S(n)=O(n log n) it should be O(log n). Let me verify explicit constants.

## Output 414 (msg_1bb1744ca001HirVCVcOcD7JDA)

The result is solid: determinant rank collapses to O(log n) for 0/1 entries via Shah's theorem, while the unrestricted per-n model is exactly FP. I'll post one board update (no repo/Lean changes), then verify it appeared.

## Output 463 (msg_1bb19d3d5001xN4l6jZivS3EvR)

One correction strengthens the result: Shah's construction is explicit and polynomial-time given the target, so the 0/1 model is also *equivalent* to FP, not merely a sufficient route. I'll append a short correction.

## Output 530 (msg_1bb1ccf32001COrGh8IXz3nPQX)

**State check.** I found the worktree clean on `billy-dev`, no prior `determinant-representation-sortnumber` comment on #301, and the front still marked `running`. I posted one result and one short correction to #301. No repository or Lean changes were made.

## Mathematical finding

The determinant front is **not an independent algebraic route**. In every natural reading it collapses to the central `S_unary ∈ FP` question.

### 1. Universal determinant representation theorem

For any integer sequence \(f\) with polynomially many bits per value, the following are equivalent:

1. \(f \in \mathrm{FP}\) on unary inputs;
2. there is a polynomial-time family of integer matrices \(A_n\) with \(\det A_n=f(n)\);
3. there is a polynomial-time family of **0/1** matrices of order
   \[
   O(\log |f(n)|+\log\log |f(n)|)
   \]
   with determinant \(f(n)\).

Proof: (1)⇒(2) is the \(1\times1\) matrix \([f(n)]\); (2)⇒(1) because integer determinant is in FP (indeed uniform NC²); (1)⇒(3) is Shah's explicit binary-matrix construction applied to the target \(a=f(n)\); (3)⇒(1) again by computing the determinant.

For \(S(n)\), since \(S(n)\le n(n-1)/2<n^2\), this gives a **0/1 matrix of order \(O(\log n)\)** with determinant \(S(n)\), computable in polynomial time from \(1^n\) **iff** \(S\in\mathrm{FP}\).

### 2. The determinant-rank falsifier is impossible

Rikhav Shah, *Determinants of binary matrices achieve every integral value up to \(\Omega(2^n/n)\)*, Linear Algebra Appl. 645 (2022) 229–236 (arXiv:2006.04701), proves
\[
d_m>\frac{1}{201}\frac{2^m}{m},
\]
where \(d_m\) is the least positive integer not the determinant of an \(m\times m\) 0/1 matrix. Taking
\[
m=\lceil\log_2 S(n)\rceil+\lceil\log_2\log_2 S(n)\rceil+12
\]
makes \(\frac1{201}2^m/m>S(n)\), so an \(m\times m\) 0/1 matrix with determinant \(S(n)\) exists. Hence the 0/1 determinant order is at most
\[
\log_2 S(n)+\log_2\log_2 S(n)+O(1)
=\log_2 n+\log_2\log_2 n+O(1)=O(\log n).
\]
Hadamard's bound gives the complementary lower bound: for a \(k\times k\) 0/1 matrix,
\[
|\det|\le k^{k/2},
\]
so \(k\log_2 k\ge 2\log_2 S(n)\), i.e. \(k=\Omega(\log n/\log\log n)\).

Therefore **no superlogarithmic, and in particular no superpolynomial, determinant-rank lower bound can exist**. The proposed falsifier is not merely hard; it is false as a mathematical possibility.

### 3. Fixed algebraic templates are impossible

If \(A(x)\) is a fixed-size matrix with rational-function entries and \(\det A(n)=S(n)\) for all large \(n\), then \(S\) is a rational function. But
\[
S(n)/n\to\infty,\qquad S(n)/n^2\to0,
\]
while a rational function has growth \(\Theta(n^d)\) for an integer \(d\) or tends to zero. Contradiction. More strongly, if the entries are \(P\)-recursive, then so is the determinant, while the board's `exact-sortnumber-nonholonomy` result says \(S\) is not \(P\)-recursive. The same applies to a fixed straight-line arithmetic circuit in the single variable \(n\).

## The exact obstruction

The obstruction is **uniform target selection**, not determinant size. Shah's construction is a universal encoder: for every small integer \(a\) it produces a logarithmic-order 0/1 matrix with determinant \(a\). It is *sound* for each advised value, but to get \(S(n)\) one must choose \(a=S(n)\), which is exactly the FP question. Removing that \(O(\log n)\)-bit advice is precisely the central problem.

This also explains why the proposed barrier does not work: a determinant identity is a **global evaluator**, not a locally checkable threshold certificate. Verifying \(\det A_n=S(n)\) presupposes the sorting lower bound. It gives neither an NP certificate for `SORT-BOUND-U` nor a separation from P. General-poset and permanent determinantal-complexity results concern polynomial families, not the integer sequence \(S(n)\), and do not transfer to the antichain root.

## Computational check

I implemented Shah's explicit construction (k-step Fibonacci vector, the mod-\(k\) upper-triangular matrix \(T\), and the greedy subset-sum top row) and verified \(\det=S(n)\) exactly for all known \(n=1,\dots,22\). For example, for \(n=10\), \(S(10)=22\), the 10×10 0/1 matrix with rows
`1100110000 / 1011011100 / 1101101010 / 1110110001 / 0111011100 /`
`0011101010 / 0001110001 / 0000111100 / 0000011010 / 0000001001`
has determinant 22. These checks are evidence, not the all-\(n\) proof; the all-\(n\) rank bound is Shah plus \(S(n)\le n(n-1)/2\).

## Honest limits

- No unconditional lower bound on the uniform FP question is proved; none is possible here without a major separation.
- The 0/1 rank bracket \([\Omega(\log n/\log\log n),\,O(\log n)]\) is not tight.
- The only surviving non-vacuous reading is a binary-input arithmetic-circuit/determinant family of size \(\mathrm{poly}(\log n)\) with \(n\)-dependent wiring. Standard VP/VNP lower bounds do not apply to an integer sequence, and a positive answer there would still only give \(S\in\mathrm{FP}\); it is a restricted sufficient route, not an independent lower-bound frontier.
- The front as a distinct algebraic program is dissolved, not resolved in favor of a new hypothesis.

## Output 558 (msg_1bb1db0fa001XTWfkpjfPrCwne)

**Inspection complete — no duplicate actions taken.**

What actually happened:

- **Git:** worktree clean on `billy-dev`, HEAD `6a96398`, no commits, no untracked repo files. No repository or Lean changes exist.
- **Board #301:** exactly two comments from this front:
  - `2026-11-08T12:19:18Z` — main determinant-front result;
  - `2026-11-08T12:20:29Z` — short correction strengthening the 0/1 model to “exactly FP.”
- **No other external effects** were found. The `/tmp` scripts used for the Shah-construction checks are outside the repository.
- **Ledger:** `determinant-representation-sortnumber` still shows `status: running`, even though the mathematical work and board posts are complete. I did **not** edit the ledger; that completion record is the keeper’s operational responsibility. This is the only uncertain item and is reported for review rather than guessed at.

**Unfinished mathematical work: none.** The result stands:

1. The literal determinant front is exactly `S_unary ∈ FP`: a poly-time matrix family gives an FP algorithm via the determinant, and conversely FP gives the \(1\times1\) matrix \([S(n)]\).
2. The 0/1 model is also exactly FP. Shah’s theorem (LAA 645, 2022) plus \(S(n)\le n(n-1)/2\) gives a 0/1 matrix of order \(O(\log n)\) with determinant \(S(n)\), constructible in polynomial time once the target \(S(n)\) is known. Thus no superpolynomial determinant-rank lower bound can exist; the proposed falsifier is impossible, not merely hard.
3. Fixed algebraic templates are impossible: a fixed-size rational-function or \(P\)-recursive determinant would make \(S\) rational/\(P\)-recursive, contradicting \(S(n)=\Theta(n\log n)\) and the board’s non-holonomy result.

**Exact obstruction:** determinant size is not the barrier. Shah’s construction is a universal small-integer encoder; the only missing ingredient is the uniform choice of the target \(a=S(n)\). Removing that advice is precisely the FP question. A determinant identity is a global evaluator, not a locally checkable threshold certificate, so it does not resolve certificate soundness-versus-completeness for `SORT-BOUND-U`.

**Honest limits:** no unconditional separation is proved; the 0/1 rank bracket \([\Omega(\log n/\log\log n),O(\log n)]\) is not tight; and the binary-input arithmetic-circuit reading remains open but is only a restricted sufficient route to FP, not an independent lower-bound frontier.
