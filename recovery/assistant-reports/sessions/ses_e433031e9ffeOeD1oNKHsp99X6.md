# antonina-U6gCceX2KdvTOeVuRJIMlu-inclined

Session: ses_e433031e9ffeOeD1oNKHsp99X6
Workspace: /home/lubko/soring-fronts/gpc-antichain-upper-bound-barrier
Created: 1794169097840; updated: 1794169860835

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 402 (msg_1bcd9c1a7001SnngoMgjs0t3ni)

Recovery inspection: on `billy-dev`, worktree clean at `6a96398`; no prior board post existed for `gpc-antichain-upper-bound-barrier`; the ledger entry was still `running`. I did not repeat any external action. I posted the finding once to issue #301 at `2026-11-08T20:28:37Z` and made no repository or Lean changes.

## Mathematical finding

Define

\[
G(n)=\lfloor \log_\varphi(n!)\rfloor,\qquad 
\operatorname{FJ}(n)=\sum_{k=1}^n\left\lceil \log_2(3k/4)\right\rceil .
\]

**Theorem.** \(G(n)>\operatorname{FJ}(n)\) for every \(n\ge 4\), with equality only at \(n=1,2,3\).

Proof by increments: with \(\alpha=1/\log_2\varphi>1.44\) and \(c=1+\log_2(3/4)<0.585\),

\[
G(n)-G(n-1)\ge \alpha\log_2 n-1,
\]
\[
\operatorname{FJ}(n)-\operatorname{FJ}(n-1)\le \log_2 n+c.
\]

For \(n\ge13\), \(\log_2 n>3.7\), so the difference of increments is \(>0.44\cdot3.7-1.585>0\). The finite base \(4\le n\le12\) is

| n | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(G(n)\) | 6 | 9 | 13 | 17 | 22 | 26 | 31 | 36 | 41 |
| \(\operatorname{FJ}(n)\) | 5 | 7 | 10 | 13 | 16 | 19 | 22 | 26 | 30 |

So the GPC-implied root bound is strictly weaker than Ford–Johnson. The gap is not constant: asymptotically it is \(\sim(\alpha-1)n\log_2 n\approx0.44\,n\log_2 n\).

Even the Peczarski Fibonacci form \(e(P)\ge F_{m(P)+2}\), applied at \(A_n\), gives only the integer bound \(H(n)=\max\{m:F_{m+2}\le n!\}\), which is \(G(n)\) or \(G(n)-1\), hence still strictly above \(\operatorname{FJ}(n)\) for all \(n\ge4\).

## What is and is not excluded

The theorem excludes **direct substitution of the GPC inequality at the antichain root**, and any argument using only the scalar bound \(G(n)\). It does **not** exclude every conceivable use of the full universally quantified GPC conclusion.

The concrete obstruction: for a prefix of depth \(d\) with leaf posets \(P_i\), GPC gives

\[
S(n)\le d+\max_i\lfloor\log_\varphi e(P_i)\rfloor,
\]

and the counting constraint only implies this is at least \(G(n)-(\log_\varphi2-1)d\), which decreases with \(d\). Thus a hybrid prefix-plus-GPC argument is not ruled out by the numeric dominance; it would need an all-\(n\) prefix construction not supplied by GPC. For \(n\le22\), any bound below \(\operatorname{FJ}\) is outright impossible because \(\operatorname{FJ}(n)=S(n)\) on the known exact range; the first possible use is \(n\ge23\) and would be a genuinely new algorithm, not a corollary.

Honest limits: the dominance theorem is elementary and probably folklore, not a new GPC theorem or algorithm. The broad claim that *every* GPC-derived argument is excluded is not proved; only the direct root use is. No counterexample to GPC was found.

## Output 459 (msg_1bcdb4920001WleVArZcnwOi85)

Recovery inspection complete; no external action was repeated.

- **Host:** `billy-dev`
- **Working directory:** `/home/lubko/soring-fronts/gpc-antichain-upper-bound-barrier`
- **Git:** clean worktree at `6a96398`; no commits, branches, Lean files, or repository edits were made.
- **Board #301:** exactly **one** post exists for this front, at `2026-11-08T20:28:37Z`, author `SoringP1 frontier: gpc-antichain-upper-bound-barrier`. I did not repost it.
- **Ledger:** the `gpc-antichain-upper-bound-barrier` entry is still `running`; this is keeper-managed and was not edited manually.

The mathematical investigation is finished. The posted finding is the all-`n` dominance theorem

\[
\lfloor\log_\varphi(n!)\rfloor > \operatorname{FJ}(n)\qquad(n\ge4),
\]

with the Peczarski Fibonacci form also strictly dominated. The honest limit remains: this excludes the direct GPC substitution at the antichain root, but not every possible auxiliary-poset or hybrid use of the full GPC conclusion. No further side effects or research work are required.
