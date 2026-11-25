# antonina-mPBe8eFJsiMnRkAo0Rsyp5-lannes

Session: ses_e08d0fecbffeNEIJTMiPNHpJ5i
Workspace: /home/lubko/soring-fronts/greedy-adversary-sufficiency-alln
Created: 1795148415320; updated: 1795152349739

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f72f06f4001CCeJ1yzMfTvmIJ)

I'll start by understanding the environment: which branch I'm on, the repository state, and the key documents.

## Output 21 (msg_1f72f10fb001pnaa0hicqY7hpa)

I'm on `billy-dev` with a clean worktree. Let me study the key documents.

## Output 40 (msg_1f72f1b790016KNfRq0CT5gVoy)

Now let me check the board digest, the one-ply obstruction doc, and look for prior work specific to this front.

## Output 55 (msg_1f72f2acc001QtgIdYJuhPiOqb)

Let me find the board #301 post about the L_k hierarchy and check for prior work on this exact front.

## Output 96 (msg_1f72f6a9f001mTthwFShAsNZ6j)

Let me look at existing scripts and prior work relevant to the greedy adversary / extension-count game.

## Output 163 (msg_1f7322046001eLZjD2rkzzYYuq)

Let me read the most relevant prior board posts in full: the GREEDY-HEAVY-PATH lemma, the slack-parameter adversary, and the r3-greedy-adversary result.

## Output 174 (msg_1f73234210015qv2roihrt5J3e)

This is very relevant. A prior board post (2026-10-21) already studied exactly the greedy/heavy-child adversary value `g` and claimed `g(A_12)=30=S(12)`. Let me verify independently. First, let me examine the existing reference code and check the primary literature.

## Output 185 (msg_1f732af1a001JXanGMPzWN3CvR)

Let me check the primary literature on Wells' method for the S(12)=30 lower bound, in parallel with setting up my own computation.

## Output 227 (msg_1f7335850001xKhE0CcNHTCkgB)

Web search is unavailable, so I'll rely on the repository's primary-source notes plus independent computation. Let me write a scratch solver for the greedy-adversary game value `G` and validate it on small n.

## Output 245 (msg_1f733b886001Oeqyiz2I0SkNje)

Small-n values confirm `G(n)=S(n)` for n≤6 and the sandwich `C≤G≤F`. Now the decisive case: n=12. Let me build a budgeted search for a 29-comparison sorter strategy against the greedy adversary (if one exists, `G(12)=29<S(12)=30`).

## Output 320 (msg_1f73bb5c40012E8Lxv3VbRFMuU)

The Python search is too slow because each node recomputes extension counts for many children. Let me measure the heavy-child-reachable state space and then implement a fast C search.

## Output 338 (msg_1f740b623001dvMPWY0OuAFonJ)

A key tension: the FRONT cites a 2026-11-17 board result `L_k(A_n)=ceil(log2 n!)` for the whole greedy leaf-count hierarchy, while a 2026-10-21 post claims `g(A_12)=30`. Let me find the exact 2026-11-17 post.

## Output 349 (msg_1f741038f001C3Hba5wm1sIJud)

I found the tension. Let me examine the exact L_k hierarchy claim and look at the Stober–Weiß paper for Wells' actual method.

## Output 369 (msg_1f7417a52001vnDnT1RzwNuLCP)

The primary literature is decisive on n=12: Stober–Weiß (§1, §3) states Wells' 1965 algorithm checks **only the larger-extension child** and this suffices to prove S(12)>29. So G(12)=S(12)=30. But the FRONT asks all n — let me get exact S and C values to find where greedy may be weaker.

## Output 389 (msg_1f741f3d2001aMrAL3cKrprqyP)

Critical distinction found in the primary source: Wells' check-only-one-child is a **search optimization for S**, not an adversary model — it does not directly give `G(12)=30`. So `G(12)` is genuinely unresolved. Let me build a fast C search for a 29-comparison strategy against the greedy adversary.

## Output 503 (msg_1f74518110012192G2cgxR3znh)

The search needs symmetry reduction. Let me fix the canonicalization in the C program with a correct permutation generator.

## Output 569 (msg_1f74e9702001u1erjrRMcIiM54)

Let me try a direct greedy-heavy-path walk: at each state pick the most balanced comparison, follow the heavy child, and see if e reaches 1 within 29 steps. This can produce an explicit certificate.

## Output 587 (msg_1f74f6c71001jyZ3rVqLzAR7TC)

The most-balanced policy needs 30 steps, but capacity allows 29. Let me run a beam search over heavy-child paths to find a 29-step route — that would be an explicit certificate `G(12)=29`.

## Output 628 (msg_1f75411e0001641Uh2yOVnwKub)

I found a buffer-swap bug in the beam search. Let me fix the buffer sizes.

## Output 646 (msg_1f7589ab6001V7cqJDNnim0WCK)

The beam search is now correct but slow. Let me run it longer in the background while I continue analysis.

## Output 686 (msg_1f7594120001sEH5gn3O9diRZK)

Let me rewrite the beam search with robust caches (no infinite loops on saturation) and a smaller beam.

## Output 704 (msg_1f75b353b001Ix3mkDYGG7ZqtT)

The beam (width 1500) died at depth 19 — all surviving states lacked a near-balanced split. Let me try a wider beam in the background; meanwhile I'll verify the theoretical distinctions.

## Output 733 (msg_1f75be5b0001YZkYheZjc2Sxfy)

Let me check whether the repository documents the L_k hierarchy result and its proof, while the wide beam runs.

## Output 762 (msg_1f75c4620001G5Fmy275iSJdky)

A key theoretical point emerged: iterating the leaf-count hierarchy must converge to the true minimax F, so `L_k(A_12)=29 for all k` cannot hold since S(12)=30. Let me verify `L_k → F` computationally on a known gap instance.

## Output 780 (msg_1f75ca270001a2UJoeIkuGkCt4)

`L_k → F` confirmed, so the board's "L_k(A_n)=C(n) for all k" is false at n=12. Now let me compute the analogous heavy-child iteration `h_k → G`, which may converge fast enough to decide G(12).

## Output 816 (msg_1f7691c6a001GJ0gmbLPpixh0a)

# Front: greedy-adversary sufficiency for exact $S(n)$ (`G(n)=S(n)` for all $n$?)

**Host/workspace:** `billy-dev`, `/home/lubko/soring-fronts/greedy-adversary-sufficiency-alln`, branch `billy-dev`, clean worktree at `6a96398` (no repo/Lean/test/workflow/ledger/main changes). Recovery audit: inspected prior conversation state, git state, and board; all computation below was scratch-only under `/tmp/opencode/` (`greedy_game.py`, `heavy_states.py`, `g12.c`, `heavy_walk.py`, `beam12b.c`, `lk_converge.py`, `hk.py`, logs). No external side effects (no board post, no commit). I did **not** duplicate any external action.

**Sources studied:** `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, `docs/research-one-ply-obstruction.md`; board #301 (full local scan, 3045 messages / 2608 unique), especially `n12-obstruction-invariant` (2026-11-17), `exact-reset-branch-mass-profile` (2026-11-17), `entropy-balance-conditional-necessity` (2026-11-17), `ROOT-ANTICHAIN CAPACITY / ONE-SIDED ADVERSARY` (2026-10-21), `GREEDY-HEAVY-PATH`/`SLACK-PARAMETER` (2026-10-20), `r3-greedy-adversary-splitter-bounds` exec verification (2026-11-11); primary literature context via `docs/literature.md` and Stober–Weiß, arXiv:2206.05597v2 (Wells’ 1965 forward-search pruning and the $S(12)=30>C(12)=29$ / $S(16,17,18)$ results). Web search/fetch of some primary PDFs was unavailable in-session; claims below distinguish literature from my deductions/experiments.

## Definitions [definition]

Fix $n$ distinct labelled keys. A state is a transitively closed strict partial order $P$; $e(P)=|\mathrm{Ext}(P)|$, $C(P)=\lceil \log_2 e(P)\rceil$.
- Unrestricted minimax (sorting number on a state): $F(P)=0$ if $P$ total, else $F(P)=1+\min_{q=(i,j)} \max(F(P+i{<}j),F(P+j{<}i))$, and $S(n)=F(A_n)$.
- **Greedy-adversary value** $G(P)$: adversary must answer into the child with more linear extensions; ties adversarial.
  $G(P)=0$ if total, else $G(P)=1+\min_{q}\, v_G(P,q)$ with
  $v_G(P,q)=G(P+i{<}j)$ if $e(P+i{<}j)>e(P+j{<}i)$, $G(P+j{<}i)$ if larger the other way, else $\max(G(P+i{<}j),G(P+j{<}i))$.
- Heavy lookahead hierarchy (analogous to $L_k$ but scoring by the forced heavy child, ties adversarial): $h_0(P)=C(P)$, $h_{k+1}(P)=0$ if total else $1+\min_q h_k(\text{heavy/tie-worst child of }q)$.

## Findings

### 1. Basic sandwich and small-$n$ consistency [deduction + experiment]
For all finite posets $P$, **$C(P)\le G(P)\le F(P)$**.
- *Proof sketch (deduction):* $G\le F$ by induction: $F$ lets the adversary choose the child maximizing $F$, which is at least the heavy/tie-adversarial choice in $G$-value, and $F\ge G$ pointwise gives $1+\min_q \max(F(c_1),F(c_2)) \ge 1+\min_q v_G(q)=G(P)$. $C\le G$: every comparison’s heavy (or either, on tie) child has $e_h \ge \lceil e(P)/2\rceil$, so $G(P)\ge 1+C(\text{heavy}) \ge 1+\lceil\log_2 \lceil e/2\rceil\rceil \ge C(P)$ (same inequality as Thm. 2 in `docs/research-one-ply-obstruction.md`).

*Experiment (independent, exhaustive over all labelled transitively closed posets, exact $e$ by downset DP, exact $F,G$ by memoized minimax, `/tmp/opencode/greedy_game.py`):* for $n\le 6$ (1,3,19,219,4231,130023 posets) there are **0** violations of $G<C$ and **0** of $G>F$, and
$G(A_n)=F(A_n)=S(n)=0,1,3,5,7,10$ for $n=1..6$. Consistent with the prompt’s “small independent $n\le 9$ experiments… consistent with $G(n)=S(n)$” (I reproduced only through $n=6$).

### 2. $n=12$ remains unresolved by this investigation; candidate falsifier not found, equality not proved [experiment, inconclusive]
- *Literature:* $S(12)=30$, $C(12)=29$ (Wells; see `docs/literature.md` / Peczarski 2012 intro / OEIS A036604). So $G(12)\in\{29,30\}$ by (1).
- *Fixed-policy stress test (experiment):* from $A_{12}$, always taking a comparison minimizing the heavy-child extension count (most balanced first, lex tie-break) and following the heavy child yields $e$-sequence
  `[239500800, 119750400, 59875200, 29937600, 14968800, 7484400, 3742200, 1871100, 935550, 467775, 249480, 124740, 62370, 31185, 16335, 8295, 4395, 2211, 1119, 609, 315, 164, 86, 46, 23, 12, 6, 3, 2, 1]`
  (30 steps to $e=1$). This shows this *particular* sorter policy needs 30 against the greedy adversary, but **does not** prove $G(12)\ge 30$ because the sorter may choose different comparisons.
- *Budget-feasible heavy path / strategy search (experiment, heuristic/incomplete):* beam search over states reachable by some capacity-feasible heavy choice ($\lceil\log_2 e_{heavy}\rceil \le$ remaining budget), keeping lowest-$e$ states (hash-dedup per layer, cached $e$-counts): width 1 fails at depth 16; width 1500 reaches depth 18 ($\min e=1953$, remaining 11) but **exhausts at depth 19** (no continuation found within beam). A wider run (width 8000) was started but progressed very slowly and was terminated during recovery (no result). **Inconclusive:** beam pruning is not sound as a proof of impossibility, and non-exhaustion would not by itself be a full strategy certificate without path reconstruction/verification.
- *Heavy lookahead $h_k(A_{12})$ (experiment):* $h_0=h_1=h_2=29$ (memo states 1, 133, 7393 respectively). $h_3$ was not completed in a naive memoized implementation (state/cost growth; run killed). No separation from 29 found at depth $\le 2$; not evidence for $G(12)=29$.

**Status:** I did **not** exhibit an $n$ with $G(n)<S(n)$, and I did **not** prove $G(n)=S(n)$ for $n=12$ or for all $n$. The falsifier direction remains open.

### 3. Correction/clarification relevant to the stated evidence: $L_k$ does not stay at $C$ for all $k$; $h_k$ convergence is the right analogue [deduction + experiment]
The FRONT states: “Board #301 (2026-11-17) proves $L_k(A_n)=\lceil\log_2 n!\rceil$ for the entire greedy leaf-count hierarchy…” (cf. `n12-obstruction-invariant`, which argues $L_k(A_n)=C(n)$ for all $k,n$ via an inductive balanced-split path). This cannot hold as stated for all $k$: by definition $L_k$ scores leaves of a $k$-ply minimax by $L_0=C$ and converges to the unrestricted minimax $F$ as $k$ grows to game height ($L_k \to F$ pointwise, since at sufficient depth the recurrence becomes $F$). But $F(A_{12})=S(12)=30$ [literature], so for large enough $k$, $L_k(A_{12})=30>29$.
- *Experiment (poset with known gap, $n=6$, `/tmp/opencode/lk_converge.py`):* $P=(0,0,0,1,3,27)$ has $e(P)=30, C(P)=5, F(P)=6$ and $L_0=5, L_1=5, L_2=6, L_3=6,\ldots$ (converged to $F$). This independently confirms $L_k \uparrow F$ and shows a fixed-depth plateau can break.
- Consequence for the FRONT: the *leaf-count* hierarchy $L_k$ (unrestricted adversary choice, $C$-scored leaves) is a sound lower-bound family $C\le L_k\le F$ that must eventually certify $S(12)=30$, though possibly only at large $k$ (no efficient-$k$ certification claimed/known). The greedy-adversary question is different: it concerns $G$/$h_k$ where the adversary is restricted to the heavy child. $C \le h_k \le G \le S$ (by the same induction, restricting adversary to heavy), and $h_k\to G$; but $h_k(A_{12})\le G(A_{12})$ can remain 29 even if $L_k(A_{12})$ becomes 30. Thus the $L_k(A_n)=C(n)$ claim, if read as blocking all finite-ply lift, is misleading for $L_k$ vs $F$, while the genuine open point is whether the **heavy-child** restriction $G$ already captures $S$.

I also note a model distinction from Stober–Weiß/Wells [literature]: “check only the larger-extension child” is used as a *forward-search pruning/lower-bound* device for proving $S(n)>C$ in explored cases; it is sound as a refutation search heuristic in that context but, as a general poset claim, the heavy branch is not always the $F$-hardest branch (board `ROOT-ANTICHAIN CAPACITY`: $g(P)<F(P)$ for 1620/130023 labelled $n=6$ posets, min witness $e=30,g=5,F=6$). $G\le F$ holds by definition, but $G=S$ at the antichain root for all $n$ is exactly the unresolved question.

## Concrete failed/inconclusive approaches and exact obstruction

- **Exact/DFS decision of $G(A_{12})\le 29$:** naive memoized search (Python, then C without symmetry reduction) too slow (~$2.4\times 10^4$ nodes/45s C, enormous branching/state count) to reach a conclusion.
- **Heuristic 29-step heavy-child path (beam):** widths 1 and 1500 failed to maintain a feasible frontier to depth 29 (1500 died at depth 19); wider search not completed. Not a refutation of $G(12)=29$.
- **Iterative heavy lookahead $h_k$:** computed $k\le 2$ only ($=29$); $k=3$ infeasible here.

**Exact obstruction:** A resolution needs either (i) an explicit, independently checkable height-29 strategy whose every heavy/tie-consistent play solves $A_{12}$ (a *completeness* certificate for $G(12)=29<S(12)$ — and note: verifying such a strategy against the restricted adversary is easier than unrestricted, but producing it requires search/argument I did not complete), or (ii) a proof that every sorter strategy has some heavy/tie-consistent answer path of length $\ge 30$ (showing $G(12)=30=S(12)$ at this $n$). The antichain-root state space and comparison branching make exhaustive certification nontrivial; no known compact invariant was obtained.

## Complexity implication (careful, as requested)

- A verified $G(n)<S(n)$ (e.g. at $n=12$) would rule out **soundness-as-completeness** for any exact lower-bound/certificate method whose adversarial justification inspects only the larger-extension (entropy/heavy) child — including one-ply/heavy-leaf-lookahead families in the greedy-adversary sense and entropy-balance arguments that take the heavier side — for certifying $S(n)>C(n)$ at that $n$. It would be a barrier to that *method family*, not a separation of P/NP/PSPACE and not a complexity lower bound for computing $S(n)$.
- A proof of $G(n)=S(n)$ for all $n$ would show greedy-adversary analysis is sufficient (complete) for exact $S(n)$, reducing the exact game to that restricted adversary model; computational tractability would remain a separate issue.

## Honest limits

No new theorem or counterexample was established. $G(12)$ and the all-$n$ question remain open from this pass. Small-$n$ evidence ($\le 6$ here) supports but cannot prove equality; beam/ply experiments were negative-or-inconclusive only. Primary-source details of Wells’ original $n=12$ argument were not fully re-derived from the PDF here (fetch unavailable), so I rely on the standard literature attribution recorded in-repo for $S(12)=30$ and on the structural distinction above rather than claiming a reproduced $g(A_{12})$ certificate. No Lean/repository/board changes were made.
