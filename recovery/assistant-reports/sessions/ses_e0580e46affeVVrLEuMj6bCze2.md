# antonina-UMxWod95NraL64TSS0ZeCS-released

Session: ses_e0580e46affeVVrLEuMj6bCze2
Workspace: /home/lubko/soring-fronts/root-nonclean-count-excess-alln
Created: 1795203996589; updated: 1795205678096

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fa7f2043001OnSIhjxi8SRf0B)

I'll start by understanding the environment and the research contract, then locate the relevant documents and board #301.

## Output 25 (msg_1fa7f2a92001q01vVmJ7CUtx2y)

Let me confirm the host and read the board digest plus literature.

## Output 40 (msg_1fa7f3ad4001bS2Ile01MWjRuU)

I'm confirmed on billy-dev. Let me examine the specific front definition and the key board posts (16:51Z, 18:30Z) in detail.

## Output 81 (msg_1fa7f7122001717CXYOg92snhF)

I have a clear picture of the definitions and state. Let me check for any earlier scratch work and look at the key notes before designing my attack.

## Output 96 (msg_1fa8053a7001NbvUfozE9Nfoj2)

There's substantial prior scratch work. Let me inspect the most relevant files to avoid repeating work and to nail down exact definitions.

## Output 119 (msg_1fa807078001oIt2eJMfPzQGSd)

Let me look at the existing independent implementations to reuse correct machinery, then design my own attack.

## Output 155 (msg_1fa80c3bb00192iHRljRysTCDI)

Let me examine how the n=8 computation was done and check the reachable-state exploration scripts.

## Output 196 (msg_1fa81179e001kbH0yow63fXjKF)

I have a validated canonicalized solver. Let me compute G(A_n) at n=7,8 to validate timing and correctness, then push to n=9.

## Output 225 (msg_1fa87704a001c5jwvs3RMk4Bcg)

n=7,8 confirmed G(A_n)=0=D(n), with bad reachable states present but avoidable. Let me launch n=9 in the background while I develop the theory.

## Output 237 (msg_1fa87eb390016Iwh8EpzLgGEvS)

While n=9 computes, let me study the primary literature and prior notes for structural facts about optimal/tight sorting trees.

## Output 257 (msg_1fa882ad2001xwBcGKAsMEUgxU)

Let me check the n=9 computation progress once and convert the Peczarski PDF text for study.

## Output 272 (msg_1fa887dd7001HYYeqUid9q60h9)

I found a key simplification worth exploiting. Let me verify it rigorously and turn it into a cheap falsifier search.

For D(n)=0, a comparison is clean iff both children have b(child)=b−1, so **any all-clean tree from A_n automatically has depth exactly ceil(log₂ n!) and sorts** — hence G(A_n)=0 iff A_n admits an all-clean sorting tree. This needs only extension counts, not full minimax F. Let me implement this cheap test.

## Output 292 (msg_1fa88f784001K48rstlqwU56VK)

The cheap test is ~70× faster and agrees on n=6–8. Let me push it to n=9,10,11 (all D=0).

## Output 310 (msg_1fa907230001NxGp5qb5cucooH)

The interrupted computation confirmed n=9’s clean-tree existence but was killed before n=10/11. I’ll audit current state and side effects first, then continue only the unfinished mathematical work; I have not posted anything to the board.

## Output 329 (msg_1fa90937e001LgPENg2eibCAqf)

Audit: still on billy-dev, repository clean, no running computations, and no board post or other external write from this session. Scratch results are only under `/tmp/opencode`. I’ll resume with n=10 separately; the prior combined run likely exhausted resources after n=9.

## Output 347 (msg_1fa982a8b001awio65ddTbv30v)

The n=10 clean-tree search was killed by the OOM killer (state-space explosion), so I won't push further brute force. Let me check whether the earlier full F/G n=9 job survived, and do a final state audit before writing up my honest finding.

## Output 358 (msg_1fa986eb5001z4fyOdp0UdjvPa)

State audit complete: still on `billy-dev`, repository clean, no lingering processes, and — importantly — **no external write from this session**: I did not post to Antonina #301, make any repository/Lean/test/ledger change, or commit. The earlier board failure is unrelated to my work; the only scratch artifacts are under `/tmp/opencode/reachdisc/`. The interrupted n=10 run was OOM-killed, which is a local compute limit, not a side effect. Per the recovery directive and because Antonina is still recovering, I am deliberately not posting to the board and am reporting here instead.

## Mathematical finding (FRONT: is $G(A_n)=D(n)$ for every $n$?)

**No root mismatch was found.** The equality survives to $n=9$; the all‑$n$ question remains open. What I did establish is a clean reduction of the root question and a precise statement of the obstruction. Labels: definition / deduction / experiment.

Setup: $e(P)$=linear extensions, $b=\lceil\log_2 e\rceil$, $F$=exact minimax, $\varepsilon=F-b$, clean = both children $e\le 2^{b-1}$, and
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
