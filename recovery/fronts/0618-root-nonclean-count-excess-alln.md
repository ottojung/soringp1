# root-nonclean-count-excess-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

UMxWod95NraL64TSS0ZeCS-released

## exit_state

clearexit

## question

Let G(A_n) be the minimum, over all height-S(n) optimal sorting strategies from the n-antichain, of the worst-case number of non-Kraft-clean comparisons, where a comparison is clean iff both outcome children have at most 2^(b-1) linear extensions; is G(A_n) equal to the sorting excess D(n)=S(n)-ceil(log_2(n!)) for every n, or do the two differ at some antichain root?

## basis

Board #301 16:51Z records G(A_n)=D(n) for n<=6 and leaves the all-n root converse open; 18:30Z refutes only the reachable-state version. Ledger running front covers the reachable supremum of G-eps, not this root-specific equality.

## falsifier

Determine an n with G(A_n) != D(n): board #301 reports equality only through n=6 and the n=8 counterexample concerns reachable intermediate states, not the root; a single root-level mismatch refutes equality, an all-n equality proof refutes the inequality alternative.

## implication

Equality would be a new structural characterization of the sorting-number excess at the exact state that determines S(n), sharpening loss-based evaluators; inequality would push the signed-ceiling-loss obstruction to the root itself rather than only reachable intermediate states.

## finding_unverified

xact minimax, $\varepsilon=F-b$, clean = both children $e\le 2^{b-1}$, and
$G(P)=\min_{\text{minimax-optimal pairs}}\big[\mathbf 1_{\text{nonclean}}+\max(G(c_1),G(c_2))\big]$.

**1. Soundness, self-contained proof (deduction).** $G(P)\ge\varepsilon(P)$ for every $P$, hence $G(A_n)\ge D(n)$. Induction on $e$: let $a$ be the max-$F$ child of the $G$-minimizing pair, so $F(P)=1+F(a)$ and $b(a)\le b(P)$. Then $G(P)\ge \mathbf1_{\text{nonclean}}+G(a)\ge \mathbf1_{\text{nonclean}}+F(a)-b(a)$, and one checks $\mathbf1_{\text{nonclean}}\ge 1-(b(P)-b(a))$ in both cases $b(a)=b(P)$ (child $a$ nonclean, LHS=1) and $b(a)\le b(P)-1$ (RHS $\le0$). So the front is exactly the **completeness** direction $G\le D$; the 16:15Z criterion proves only soundness.

**2. Tight-state clean-comparison lemma (deduction).** If $F(P)=b(P)=t$ and a comparison at $P$ is clean, then $1+\max(F(c_1),F(c_2))=t$, so it is minimax-optimal. Consequently, for $D(n)=0$: an all-clean tree from $A_n$ must have every $b$-drop exactly 1 and depth exactly $\lceil\log_2 n!\rceil$, and conversely any such tree is optimal. Therefore
$$D(n)=0:\quad G(A_n)=0 \iff A_n \text{ admits an all-clean sorting tree},$$
i.e. a height-$S(n)$ tree where every comparison splits $e$ into two children with $b(\text{child})=b(\text{parent})-1$. This removes minimax $F$ entirely from the test — only extension counts are needed (a structural reduction; $e$ is still $\#P$-hard, so not an algorithmic speedup).

**3. Forced-obstruction lemma (deduction).** Let $\mathrm{Bad}=\{P:G(P)>\varepsilon(P)\}$ (nonempty: the n=6/n=8 reachable witnesses). Using $\varepsilon(A_n)=\varepsilon(P)+\sum_{\text{path to }P}(1-\text{drop})$, if **every** height-$S(n)$ strategy from $A_n$ has an adversary path entering $\mathrm{Bad}$, then $G(A_n)>D(n)$. So a root mismatch must come from a *forced* bad state; the n=8 bad states are reachable but avoidable, which is why $G(A_8)=D(8)=0$. General-poset families with $G>\varepsilon$ (ordinal sums) do **not** transfer to the antichain root without this forcedness argument — this is the soundness/completeness and general-poset/root distinction the task asked for.

**4. Computation (experiment, my own implementation).** The all-clean test (canonical posets, subset-DP extension counts) returns **True for n = 6, 7, 8, 9** (n=9: 9,875 states, 155 s), so $G(A_n)=D(n)=0$ for $n\le 9$ (n≤6 known on the board; n=7,8,9 new). Independent full minimax $G$ recomputation gave $G(A_7)=0$, $G(A_8)=0$ with 13 bad reachable states at n=8 — confirming bad states exist but are avoidable at the root. This extends the board's "equality only through n=6."

## Honest limits
- No root-level mismatch was found; the inequality alternative is not refuted either. The all-$n$ equality is **not proved**.
- n=10, 11 clean-tree searches were OOM-killed (state-space explosion); this method cannot reach them, so the first $D>0$ case (n=12, $D=1$) is out of reach here.
- The decisive remaining obstacle is whether a bad state becomes **unavoidable** from some antichain root. Deciding that is essentially the open problem of compact certificates for optimal sorting trees (Wells/Peczarski/Stober–Weiß obstructions are certified only by exhaustive search), so this front is not separable from that difficulty by the present techniques.

No deliverable was created because none of this is a genuinely new theorem/counterexample settling the front; it is a reduction, two structural lemmas, and a finite extension of the evidence.

## Other metadata

```json
{
  "finished_at": 1795205682.0713656,
  "started_at": 1795203996.252155
}
```
