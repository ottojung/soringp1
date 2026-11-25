# antonina-DT9a8bPKe8GhY9MPElEz70-throats

Session: ses_e11777cd8fferGSzsODXXC2Exi
Workspace: /home/lubko/soring-fronts/universal-information-gap-at-most-one
Created: 1795003286350; updated: 1795003722366

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 136 (msg_1ee8a67fd001P6E7awMDLL0fTN)

## Claim attacked (all $n\ge 1$, falsifiable)

**Front (literature/evidence as stated):** For every integer $n\ge 1$,
$$
S(n) \le \lceil \log_2(n!) \rceil + 1,\qquad C(n):=\lceil \log_2(n!) \rceil .
$$
Equivalently $S(n)-C(n)\in\{0,1\}$, since the decision-tree/leaf-count lower bound gives $S(n)\ge C(n)$ for the fixed model in `docs/problem.md` (adaptive worst-case pairwise comparisons on $n$ distinct labelled keys; $S(n)$ the minimax comparison height from the $n$-antichain).

**Falsifier sought:** any explicit $n\ge 1$ with a rigorous, independently checkable proof that $S(n)\ge C(n)+2$.

**Complexity relevance (model fidelity):** an affirmative all-$n$ theorem would pin the value/certificate target for `SORT-BOUND-U = {1^n#1^k : S(n)\le k}` to one threshold above the information bound (a strong structural fact about exact evaluation), but by itself it would not place `SORT-BOUND-U` in P/NP nor separate complexity classes; conversely a uniform super-polynomial separation for this tally/sparse unary language would run into the open-separation/circuit barriers noted in `docs/problem.md`/`AGENTS.md`.

## Primary-literature baseline (literature; independently citable)

- **Information bound / model:** $S(n)\ge \lceil \log_2(n!)\rceil$ is the standard leaf-counting bound for comparison decision trees (Knuth TAOCP Vol. 3, §5.3.1; Ford–Johnson 1959 give upper-bound constructions in the same comparison model). `docs/literature.md`, `docs/problem.md`.
- **$n=12$ non-tightness:** $C(12)=29$ but $S(12)=30$ (gap $1$), originally by exhaustive search of M. Wells (1966/1971), credited and discussed in Peczarski, *Towards optimal sorting of 16 elements*, Acta Univ. Sapientiae Informatica 4(2), 2012 (PDF https://real-j.mtak.hu/23036/2/Acta%20Info%202012_4_2.pdf). 
- **$n=16,17,18$ and $n=28$:** F. Stober and A. Weiß, *Lower Bounds for Sorting 16, 17, and 18 Elements*, ALENEX 2023 (SIAM), pp. 201–213, DOI 10.1137/1.9781611977561.ch17; preprint arXiv:2206.05597. They prove $S(16)=46$, $S(17)=50$, $S(18)=54$ and $S(28)\ge 99$ by exhaustive/pruned bidirectional search (computer proof). `docs/literature.md` records exact values known for all $n\le 22$, $n=23$ open.
- **Asymptotic upper bound:** I. Sergeev, *On the asymptotic complexity of sorting*, ECCC TR20-096 (2020), Thm. 3, gives $S(n)=\log_2(n!)+O(n/(\log n)^{1/5})=\log_2(n!)+o(n)$ (as cited/used in `docs/research-winning-frontier-barrier.md` §3.1). This is an **upper** bound and permits additive $o(n)$ overhead in principle; it does not imply $S(n)\le C(n)+1$ and does not yield any $S(n)\ge C(n)+2$ lower bound.
- **OEIS indexes (not primary proofs):** A036604 (sorting numbers), A003070 (information bound).

## Exact evidence checked (deduction/experiment, arithmetic)

Using $C(n)=\lceil \lgamma(n+1)/\ln 2\rceil$ and the literature exact values for $n\le 22$ (`docs/literature.md`: Peczarski 2012, Stober–Weiß 2023), I computed:

| $n$ | $C(n)$ | $S(n)$ | gap |
|---:|---:|---:|---:|
| 1–11 | 0,1,3,5,7,10,13,16,19,22,26 | 0,1,3,5,7,10,13,16,19,22,26 | 0 |
| 12 | 29 | 30 | 1 |
| 13 | 33 | 34 | 1 |
| 14 | 37 | 38 | 1 |
| 15 | 41 | 42 | 1 |
| 16 | 45 | 46 | 1 |
| 17 | 49 | 50 | 1 |
| 18 | 53 | 54 | 1 |
| 19 | 57 | 58 | 1 |
| 20 | 62 | 62 | 0 |
| 21 | 66 | 66 | 0 |
| 22 | 70 | 71 | 1 |

Further: $C(23)=75$, $C(24)=80$, $C(25)=84$, $C(26)=89$, $C(27)=94$, $C(28)=98$ (e.g. $\log_2(28!)\approx 97.944$). Stober–Weiß prove $S(28)\ge 99$ [literature], hence the **proved** gap at $n=28$ is $\ge 1$ ($99\ge C(28)+1$), not $\ge 2$. No exact $S(n)$ is known here for $n\ge 23$ beyond such lower bounds.

**Consequence:** for all $n$ where a rigorous value/lower-bound proof is currently established in this baseline, $S(n)\le C(n)+1$ is consistent and no $S(n)\ge C(n)+2$ witness is known.

## Serious disproof attempts (and why no falsifier was obtained)

### 1. Leaf-counting/information argument cannot force $+2$ (deduction)
A decision tree of height $h=C(n)+1$ can distinguish $2^{C(n)+1}\ge 2n!$ outcomes in principle. Therefore any proof of $S(n)\ge C(n)+2$ must be **strategic/structural** (adversarial imbalance along all root strategies), not a global counting argument. This is the same qualitative reason $S(12)>29$ required Wells’/later exhaustive poset search rather than a leaf bound (Peczarski 2012; Stober–Weiß 2023; analysis in `docs/research-n12-nontightness.md`).

### 2. Known non-tight instances give only $+1$ (literature)
The explicit computer-checked/proved non-tightness results in the cited literature ($n=12$ and the Stober–Weiß lower bounds/values including $n=16,17,18,28$) establish gaps of exactly/at least $1$ above $C(n)$, never $\ge 2$. Attempted “promote $+1$ to $+2$” by inspection of published outcomes fails because no such outcome is claimed.

### 3. Local poset/merge obstructions do not transfer to a global antichain $+2$ (deduction; general-poset ≠ root)
`docs/research-n12-nontightness.md` and `docs/research-obstruction-next.md` document: (i) the poset-level information bound $m(P)\ge \lceil\log_2 e(P)\rceil$ can fail locally (e.g. $e(P)=8, m(P)=4$) while the global $S(5)=C(5)$ remains tight; (ii) sortability is not monotone in $e(P)$ and no scalar invariant of $e(P)$ explains the global gap; (iii) the local gap $m(P)-\lceil\log_2 e(P)\rceil$ is unbounded over arbitrary posets (e.g. merge/two-chain families give $M(m,m)-\lceil\log_2 \binom{2m}{m}\rceil \to \infty$, using the equal-size merge value $M(m,m)=2m-1$ [literature/deduction as cited there]). 

However, $S(n)$ is the **antichain-root** minimax value. Hardness/obstruction for arbitrary reachable or arbitrary partial orders does not by itself force $S(n)\ge C(n)+2$: the sorter controls comparisons and may avoid realizing a locally bad poset within a $C(n)+1$ budget (and local +1 failures do not imply a global +1). I found no reduction or invariant turning any known unbounded local/merge obstruction into a rigorous all-root lower bound of $+2$ for any explicit $n$.

### 4. One-ply/adversarial information strengthening (deduction, repo result) is insufficient
`docs/research-one-ply-obstruction.md` proves a sound strengthening $L_0(P)\le L_1(P)\le F(P)$ with $L_1(P)=1+\min_{i,j}\max(L_0(P+i{<}j),L_0(P+j{<}i))$, and exhibits strict local witnesses (smallest at $n=5$, $e=8, L_0=3, L_1=F=4$). This shows the information bound can be strictly improved **locally by one ply** in some states, but (a) it is a local/state bound, (b) it yields $+1$-type strengthening at a node, and (c) without a global root argument it does not produce any explicit $n$ with $F(\text{antichain}_n)\ge C(n)+2$. I could not chain it into a global $+2$ certificate.

### 5. Winning-frontier/enumeration barriers are not lower bounds (literature/deduction, repo result)
`docs/research-winning-frontier-barrier.md` shows a large family of **winning** states can survive exact information/optimal-budget pruning (an enumeration barrier), but explicitly does not give a time/space/comparison lower bound for computing $S(n)$ or for $S(n)$ itself. It cannot serve as evidence for $S(n)\ge C(n)+2$.

### 6. Small-$n$/bounded search for a counterexample (negative, limited)
All exactly determined $n\le 22$ have gap $\le 1$ (above), so no counterexample exists there. I did not (and, given the combinatorial explosion, could not credibly) reproduce or extend a Wells/Stober–Weiß-scale exhaustive proof to show $S(n)>C(n)+1$ for any open $n$ (e.g. $n=23$ would require excluding all height-$76$ strategies in that model, far beyond lightweight checking here). No explicit falsifying $n$ was found.

## Certificate soundness vs completeness (distinction)

Not directly the object of this numerical-gap front, but relevant to adjacent `SORT-BOUND-U` interpretations: a locally **sound** pruning/certificate condition (e.g. $L_0,L_1$ lower bounds; a valid NO/witness rule on a state) may reject/certify some cases without being **complete** for the global predicate $S(n)\le k$ or for all $n$. Conversely, execution on a path or a root-tight/all-tight instance in a restricted sense does not by itself constitute a complete, polynomially checkable all-$n$ proof system. No completeness claim is made here.

## Finding (honest)

- **Disproof status:** **No falsifier found.** I did not identify any explicit $n\ge 1$ together with a rigorous, independently checkable proof that $S(n)\ge \lceil\log_2(n!)\rceil + 2$.
- **Support status:** the claim $S(n)\le C(n)+1$ is **consistent with all cited primary exact/lower-bound results** known here ($n\le 22$ gaps in $\{0,1\}$; $S(28)\ge C(28)+1$ only), but **remains unproved as an all-$n$ theorem**. Sergeev’s $\log_2(n!)+o(n)$ upper bound is far weaker than $+1$.
- **Exact obstruction:** a counterexample would require a non-counting, global minimax adversary argument showing the $n$-antichain is unsortable in $C(n)+1$ comparisons. Current public/primary evidence provides only exhaustive-search $+1$ separations at isolated $n$ and local (even unbounded) poset gaps that do not transfer to the antichain root; extending these to a certified $+2$ at any specific open $n$ appears to require either a new structural invariant or a computation/proof of Stober–Weiß/Wells scale beyond what was feasible to establish here. No repository/Lean change is warranted (no new independently checkable theorem or counterexample). 

**Labels used:** literature (Wells/Peczarski/Stober–Weiß/Sergeev/Knuth/Ford–Johnson as cited above), deduction (arithmetic, transfer/no-go reasoning), experiment (recomputed $C(n)$ and gap table for $n\le 22,23$–$28$); no kernel-checked claim.

## Output 309 (msg_1ee8f1731001oAF9Bgwy9Gbq72)

The recovery inspection confirms:

- **Git state:** clean worktree at `6a96398`, no uncommitted changes or new files.
- **Board #301:** the previous turn did **not** post its finding (no matching message existed). That was the unfinished work.
- **Completed now:** posted the mathematical finding as a single new comment (timestamp 2026-11-18T12:08:29.919Z, author "SoringP1 research agent (billy-dev)") — no duplicate, since none existed before.

**Summary of the finding (already in the board post and prior chat):**

- **Claim attacked:** $S(n)\le \lceil\log_2(n!)\rceil+1$ for all $n\ge1$.
- **Disproof status:** No falsifier found. All exactly known $n\le22$ have gap $\in\{0,1\}$; Stober–Weiß proves only $S(28)\ge C(28)+1$; Sergeev's bound is an upper bound $\log_2(n!)+o(n)$, far weaker than $+1$.
- **Obstruction:** A $+2$ counterexample needs a global (antichain-root) minimax adversary argument, not leaf counting; known local/merge obstructions do not transfer to the root (local gap can be unbounded while $S(5)=C(5)$ stays tight). No new repo/Lean/PR changes were warranted.

No further unfinished work remains.
