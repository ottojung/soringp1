# antonina-JR7nynmJIlsGtiiDHwzZ11-twitched

Session: ses_e3f40830affeO8G69aj9WYEq8J
Workspace: /home/lubko/soring-fronts/local-excess-root-transfer
Created: 1794235137375; updated: 1794235930232

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 269 (msg_1c0cb1c59001PmfypsScpxlCjq)

## Finding: no transfer for the proposed ordinal-sum block family

Board #301 post: `2026-11-09T14:51:24Z`, author `SoringP1 frontier: local-excess-root-transfer`. Worktree remains clean at `6a96398`; no Lean or repository changes.

### 1. Ordinal-sum scaling theorem `[paper proof]`

For a fixed finite poset \(B\) with \(m=|B|\ge 2\), maximal-element count \(M(B)\), and minimal-element count \(\mu(B)\), let \(P_k=B^{\oplus k}\) be the ordinal sum of \(k\) copies. Then

\[
e(P_k)=e(B)^k,\qquad F(P_k)=kF(B),
\]
\[
\operatorname{cov}(P_k)=k\,\operatorname{cov}(B)+(k-1)M(B)\mu(B).
\]

The first two identities are the standard ordinal-sum product/additivity facts (deterministic direct-sum theorem; Jain–Klauck–Sántha 2010, specialized in `docs/research-series-decomposition.md`). The cover identity follows because internal covers survive, non-consecutive cross relations have an intermediate block, and a cross relation is a cover exactly when its lower endpoint is maximal and its upper endpoint is minimal.

Consequently \(F(P_k)=O(k)\) and \(\operatorname{cov}(P_k)=O(k)\). But with \(n=km\),

\[
C(n)=\lceil \log_2 n!\rceil\ge n\log_2 n-n/\ln 2,
\]

while \(C_{P_k}=\lceil k\log_2 e(B)\rceil\le km\log_2 m+1\) because \(e(B)\le m!\). Hence

\[
C(n)-C_{P_k}\ge n\log_2 k-O(n)\to\infty.
\]

The local excess \(F(P_k)-C_{P_k}\le F(P_k)=O(k)\) is therefore swallowed by a superlinear information gap. Even the whole path cost \(\operatorname{cov}(P_k)+F(P_k)=O(k)\) is far below \(C(n)\) for large \(k\). This rules out every fixed-block ordinal-sum amplification, independently of the exact cover count.

### 2. Exact \(W\) arithmetic, and a correction

The documented one-ply witness is \(W=(26,0,10,0,8)\), with

\[
e(W)=8,\quad C_W=3,\quad F(W)=4,\quad \operatorname{cov}(W)=5,\quad M(W)=\mu(W)=2.
\]

Thus \(W^{\oplus k}\) has \(n=5k\), \(e=8^k\), \(C_{W^{\oplus k}}=3k\), \(F=4k\), and

\[
\operatorname{cov}(W^{\oplus k})=5k+4(k-1)=9k-4,
\]

**not** \(11k-6\). The value \(11k-6\) would require \(M(W)\mu(W)=6\); an exhaustive check of all labelled 5-element posets shows every one with \(e=8,F=4\) has exactly 5 covers and \(M=\mu=2\) (120 labelled posets). The conclusions below survive unchanged even if \(11k-6\) is used.

| \(k\) | \(n=5k\) | \(C(n)\) | cov | \(C_P\) | \(F\) | cov+\(F\) | \(C(n)-(\text{cov}+F)\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5 | 7 | 5 | 3 | 4 | 9 | \(-2\) |
| 2 | 10 | 22 | 14 | 6 | 8 | 22 | 0 |
| 3 | 15 | 41 | 23 | 9 | 12 | 35 | 6 |
| 4 | 20 | 62 | 32 | 12 | 16 | 48 | 14 |
| 5 | 25 | 84 | 41 | 15 | 20 | 61 | 23 |

\(F(W^{\oplus k})=4k\) was checked exactly for \(k=1,2,3,4\) and follows for all \(k\) by additivity.

### 3. Two distinct obstructions

- **Cover/root cost at \(k=1\).** \(W\) is reachable from \(A_5\) in 5 comparisons, but \(\operatorname{cov}(W)+F(W)=9>C(5)=7=S(5)\). So \(W\) cannot occur at depth 5 of any optimal height-7 tree: its subtree would need 4 more comparisons, producing a path of length 9. This is the smallest explicit counterexample to “a reachable hard block gives a root lower bound.”
- **Information scaling for \(k\ge3\).** \(\operatorname{cov}(W^{\oplus k})+F(W^{\oplus k})=13k-4<C(5k)=\Omega(k\log k)\). At \(k=2\) the path exactly equals \(C(10)=22\), so it can at best tie. Thus no \(k\) yields a path above \(C(5k)\).

### 4. General root barrier `[deduction]`

For every poset \(P\) on \(n\) keys, \(A_n\subseteq P\), so extension monotonicity gives

\[
F(P)\le F(A_n)=S(n).
\]

A local excess \(E(P)=F(P)-C_P\) can imply \(S(n)\ge C(n)+1\) only if

\[
C_P+E(P)=F(P)\ge C(n)+1.
\]

Relative excess alone has no force. The only sound transfer is extension monotonicity, and it requires the block itself to be an antichain-strength witness. This is the precise separation between local general-poset gaps and antichain-root hardness: the antichain maximises \(F\) over all \(n\)-key posets, so a proper poset cannot exceed the root. Reachability is not the missing ingredient; reaching the global information level is.

The height-two \(A_{12}(+)A_{12}\) example shows the same: \(n=24\), \(C_P=58\), \(F=60\), but \(C(24)=80\); its excess 2 is offset by a 20-bit gap, and ordinal-summing \(k\) copies gives \(F=60k\) against \(C(24k)=\omega(k)\).

### 5. Soundness versus completeness

Ordinal-sum additivity, the cover formula, and extension monotonicity are sound. What fails is the completeness/quantitative step: a local certificate for \(F(P)\) is neither a proof that every near-optimal sorter passes through \(P\), nor a proof that \(F(P)\) reaches the global information bound. The \(W\) family exhibits both failures explicitly.

### Honest limits

I did **not** prove that no transfer of any non-ordinal form exists, and I did **not** prove \(S(n)\ge C(n)+1\) for infinitely many \(n\). The all-\(k\) no-go covers fixed-block ordinal-sum amplification; the general root barrier says any successful transfer must already supply a proper poset with \(F(P)\ge C(n)+1\), which is not a weaker local statement. No Lean or repository changes were warranted.
