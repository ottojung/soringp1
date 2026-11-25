# antonina-xAZJSxeeOupKI9fDxYWslq-cropped

Session: ses_e3f407d61ffeplIIWqIWdExNF4
Workspace: /home/lubko/soring-fronts/reachable-excess-per-cover-ratio
Created: 1794235138811; updated: 1794237855162

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 415 (msg_1c0e70004001uJYP73p4CeDj0J)

## Finding: the depth-one ratio is exactly the global excess

I proved an all-\(n\) identity that exposes the proposed ratio as the central sorting-number excess in disguise.

Let \(Q_n=C_2\sqcup A_{n-2}\) be the state after one comparison: one known relation plus \(n-2\) isolated keys. For every \(n\ge 2\),

\[
F(Q_n)=S(n)-1.
\]

**Proof.** Both children of the root comparison of any sorting tree on \(A_n\) are one-relation posets, hence both are isomorphic to \(Q_n\). Therefore an optimal height-\(S(n)\) tree gives \(F(Q_n)\le S(n)-1\). Conversely, any height-\(F(Q_n)\) tree for \(Q_n\) also sorts the opposite (isomorphic) outcome, so prefixing the one comparison gives a sorting tree of height \(1+F(Q_n)\); hence \(S(n)\le 1+F(Q_n)\). Equality follows.

Now \(e(Q_n)=n!/2\), \(C(Q_n)=\lceil\log_2(n!/2)\rceil=C(n)-1\), and \(\operatorname{covers}(Q_n)=1\). Thus

\[
\frac{F(Q_n)-C(Q_n)}{\operatorname{covers}(Q_n)}
= (S(n)-1)-(C(n)-1)
= S(n)-C(n)
=: E(n).
\]

So the shallowest reachable state already attains ratio \(E(n)\), with denominator one.

### Consequences

- Any proposed universal bound \(c<1\) is **false**: at \(n=12\), \(E(12)=30-29=1\), so \(Q_{12}\) has ratio \(1\). This lies on an optimal-play path as well as being reachable in one comparison.
- A finite universal constant would force boundedness of \(E(n)=S(n)-\lceil\log_2 n!\rceil\), which is open. Sergeev only supplies \(E(n)=O(n/(\log n)^{1/5})\). If \(E(n)\) is unbounded, the supremum in the front is infinite.
- Known exact values through \(n=22\) have \(E(n)\in\{0,1\}\); \(S(28)\ge 99\) versus \(C(28)=98\) gives \(E(28)\ge1\). No \(E(n)\ge2\) is currently known, so I could not refute \(c=1\).

## Explicit lower-bound families

The documented one-ply witness \(W=(26,0,10,0,8)\) has \(e=8\), \(F=4\), \(5\) covers, and \(2\) minima and \(2\) maxima. Hence

\[
W^{(+)k}:\quad e=8^k,\quad C=3k,\quad F=4k,\quad X=k,
\]
\[
\operatorname{covers}=5k+4(k-1)=9k-4,
\qquad
\frac{X}{\operatorname{covers}}=\frac{k}{9k-4}\to\frac19.
\]

The premise's \(11k-6\) is not the cover count of this documented \(W\).

A better block is \(B=\operatorname{Merge}(2,4)\): \(e=15\), \(F=5\), \(4\) covers, \(2\) minima/maxima. Then

\[
B^{(+)k}:\quad e=15^k,\quad F=5k,\quad \operatorname{covers}=8k-4,
\]
\[
\frac{X}{\operatorname{covers}}
=
\frac{5k-\lceil k\log_2 15\rceil}{8k-4}
\to
\frac{5-\log_2 15}{8}
\approx 0.136638 > \frac19.
\]

Exhaustive \(n\le6\) confirms this is the best block ratio of the form
\(\alpha/(\operatorname{covers}+\#\min\cdot\#\max)\); the best single small ratio is \(1/2\) at \(n=6\) (e.g. \(V_3\sqcup A_3\), \(X=1\), covers \(2\)). I did not exhaust \(n=7\), so these are lower bounds, not the supremum.

## Optimal-play versus literal reachability

Under the literal reading “reachable in at most \(S(n)\) comparisons,” the ordinal-sum families above are valid. Under the stronger reading “on an optimal height-\(S(n)\) tree,” the recent board root-gap result excludes them—but \(Q_n\) remains reachable and still gives ratio \(E(n)\). So either reading leads back to the same open excess question.

## Soundness versus completeness

\(C(P)=\lceil\log_2 e(P)\rceil\) is a sound lower bound at every reachable state. The ratio measures its worst-case incompleteness, not a new certificate. The theorem shows the one-cover incompleteness is exactly \(E(n)\); no completeness theorem, polynomial certificate, or complexity-class consequence follows. General-poset hardness results are not used.

## Failed approach and honest limits

I tried to build a family exceeding every proposed constant. That succeeds for every \(c<1\) via \(Q_{12}\), but reaching \(c>1\) would require a known \(E(n)>1\), which is unavailable. The all-\(n\) identity is a paper proof; the block computations and \(n\le6\) exhaustive checks are exact experiments. No Lean or repository change was made; the result was posted to board #301.

## Output 495 (msg_1c0e8c64e001Yv6t0zOt6RNU5T)

Inspected state before doing anything:

- **Host:** `billy-dev`.
- **Git:** clean at `6a96398`; no commits, file changes, or Lean changes were made.
- **Board #301:** exactly **one** matching post for this front, timestamped `2026-11-09T15:21:59.641Z`. It contains the depth-one identity and the lower-bound families. No duplicate post was created.
- **Scratch:** only `/tmp/opencode/coverratio/` (scripts, `board_post.md`, post result). No repository artifacts.
- **Ledger:** `/home/lubko/.local/state/soringp1/frontier-ledger.json` still records `reachable-excess-per-cover-ratio` as `"status": "running"`.

No unfinished mathematical work remains from the previous turn, and I did not repeat the board post.

The only uncertain durable-record item is the ledger status still being `running`; I did not modify it manually to avoid guessing at the keeper’s lifecycle semantics. That should be reconciled by the frontier keeper or an operator as `investigated`, not by another duplicate post.
