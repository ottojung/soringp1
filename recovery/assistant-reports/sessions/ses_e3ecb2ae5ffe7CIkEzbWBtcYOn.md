# antonina-U583bQWoKVFm7yCwV27aDc-window

Session: ses_e3ecb2ae5ffe7CIkEzbWBtcYOn
Workspace: /home/lubko/soring-fronts/height-two-f-decision-np
Created: 1794242827594; updated: 1794244451853

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 627 (msg_1c14b250b0010yLhs73KJZ84ic)

## Result

**No proof of height-two NP membership, no NP-hardness proof, and no all-\(n\) super-polynomial certificate lower bound was obtained.** The front remains open. What I did establish is a precise obstruction to the front’s stated falsifier and a new exact finite collision that rules out the natural extension-count certificate at \(n=7,8\).

### 1. The stated falsifier is logically wrong

Let

\[
H=\{\langle P\rangle\#1^k:\; P\text{ height }2,\; F(P)\le k\},\qquad
S=\text{SORT-BOUND-U}.
\]

The reduction \(S\le_m^p H\) is the known one-edge map
\[
1^n\#1^k \longmapsto \langle Q_n\rangle\#1^{k-1},\qquad
Q_n=C_2\sqcup A_{n-2},
\]
with \(F(Q_n)=S(n)-1\) for all \(n\ge2\). Hence

\[
H\in\mathrm{NP}\;\Longrightarrow\;S\in\mathrm{NP}.
\]

But **NP-hardness of \(H\) does not refute \(H\in\mathrm{NP}\).** An NP-complete \(H\) would satisfy both NP-hardness and NP membership; and if \(H\) were NP-complete then \(H\in\mathrm{NP}\), so the reduction above would give \(S\in\mathrm{NP}\). Thus the front’s first falsifier branch (“establish NP-hardness”) is compatible with, indeed potentially proves, the positive answer. The genuine negative statement is \(H\notin\mathrm{NP}\).

The second branch (“every sound certificate has super-polynomial size”) is not well-posed until the certificate language and verifier are fixed. With an unrestricted verifier, “certificate” has no complexity meaning; with a polynomial-time verifier, a no-certificate lower bound is exactly a proof that \(H\notin\mathrm{NP}\).

This is the main mathematical finding about the front itself: **it confuses hardness with non-membership.**

### 2. Why the \(Q_n\) route cannot yield the negative answer cheaply

Any attempt to disprove \(H\in\mathrm{NP}\) by exhibiting a super-polynomial certificate lower bound on the subfamily \(Q_n\) would prove

\[
S\notin\mathrm{NP}.
\]

Since \(S\in\mathrm{PSPACE}\), that would prove \(\mathrm{NP}\ne\mathrm{PSPACE}\). So this natural negative route is at least as hard as a major unconditional separation. It is not a viable finite or structural counterexample.

### 3. New exact obstruction to extension-count certificates

I extended the board’s \(n=6\) collision to \(n=7,8\). Let

\[
P_6=(44,28,0,0,0,0),\qquad Q_6=(48,48,8,0,0,0)
\]

in successor-bitmask notation, i.e.
\[
P_6:\;0<2,0<3,0<5,1<2,1<3,1<4,
\]
\[
Q_6:\;0<4,0<5,1<4,1<5,2<3.
\]

Both are height \(2\), and \(e(P_6)=e(Q_6)=60\), while \(F(P_6)=6\), \(F(Q_6)=7\). Add \(m\) isolated keys:

\[
P_m=P_6\sqcup A_m,\qquad Q_m=Q_6\sqcup A_m.
\]

Then for every \(m\ge0\),

\[
e(P_m)=e(Q_m)=\frac{(6+m)!}{12},
\]

so the two families have **identical extension counts for every \(m\)**. Exact minimax gives:

\[
\begin{array}{c|ccc}
m & n & F(P_m) & F(Q_m)\\ \hline
0 & 6 & 6 & 7\\
1 & 7 & 9 & 10\\
2 & 8 & 12 & 13
\end{array}
\]

The \(m=1\) and \(m=2\) values are new relative to the board’s \(n=6\) statement; the board had reported that its \(n=8\) computation exceeded budget. I verified \(n=6,7\) with two independent minimax implementations, and \(n=8\) with the optimized independent solver. The extension counts were checked by an independent downset DP. Therefore:

**For \(n=7,8\), \(F(P)\) is not determined by \((n,e(P))\) on height-two posets.** Equivalently, no certificate of the form “\(e(P)\le T(k)\)” can be complete at those sizes. This is sound as a finite obstruction, not an all-\(n\) theorem.

At these sizes the defects are
\[
D_P(n)=S(n)-F(P_m)=4,\qquad D_Q(n)=S(n)-F(Q_m)=3
\]
for \(n=6,7,8\), consistent with the open eventual-constancy question for fixed patterns, but I did not prove constancy for all \(m\).

### 4. Literature position

- Yao, *On the Complexity of Partial Order Productions*, SIAM J. Comput. 18 (1989), proves \(C(P)=\Theta(\bar C(P))\) and an upper bound \(C(P)=O(\log(n!/\mu(P))+n)\). It treats the exact comparison number but does **not** settle decidability in NP.
- Cardinal–Fiorini–Joret–Jungers–Munro and later work give constant-factor approximations to \(\log e(P)\), not exact \(F(P)\).
- Dittmer–Pak, arXiv:1802.06312, prove that counting linear extensions of height-two posets is \(\#P\)-complete. This does **not** transfer to \(F\): the \(n=6,7,8\) collisions show \(F\) is not a function of \(e\).
- I found no primary source establishing NP membership or NP-hardness of the height-two exact decision problem. General-poset hardness results and arbitrary-test decision-tree hardness do not apply to the pairwise-comparison model.

### 5. Failed approaches and honest limits

- **\(\#H2LE\to F\) hardness:** blocked by the \(e\)-collision; equal extension counts give different \(F\).
- **Super-polynomial certificates on \(Q_n\):** would prove \(S\notin\mathrm{NP}\), hence \(\mathrm{NP}\ne\mathrm{PSPACE}\).
- **Infinite extension-count collision family:** the \(e\)-equality holds for all \(m\), but I could not prove the \(F\)-gap persists beyond \(m=2\). The finite data suggest it does; this is a conjecture, not a result.
- **NP-hardness reduction:** no reduction found. The height-two comparison game has short local moves but a global minimax condition; I did not construct a gadget encoding a known NP-hard problem.

**Bottom line:** the front’s negative falsifier is mis-specified, the natural negative route is blocked by the \(S\)-subfamily, and the only unconditional new content is the exact \(n=7,8\) extension-count collision. The actual question \(H\in\mathrm{NP}\) remains open and is at least as hard as the missing \(S\in\mathrm{NP}\) certificate problem.

No repository or Lean changes were made; the worktree is clean at `6a96398`.

## Output 721 (msg_1c14d79f9001KadPykJCJIkzsh)

## Recovery inspection complete

I did not repeat the research prompt, post to the board, commit, or edit the repository.

### Effects confirmed to have happened

- **Host:** `billy-dev`.
- **Repository:** `/home/lubko/soring-fronts/height-two-f-decision-np`
  - `git status` clean.
  - Still at `6a96398`.
  - No commits, stashes, Lean files, or tracked/untracked repository changes.
- **Board #301:** I searched pages 1–12 for the front ID, the \(n=7/8\) data, and the main formulas.
  - **No post exists** under `height-two-f-decision-np`.
  - No duplicate board action was made.
- **Scratch work:** only files under `/tmp/opencode`, outside the repository. The exact \(n=7,8\) collision computations and literature searches were scratch-only.

### Durable record status — uncertain, for review

The frontier ledger entry is still:

```json
{
  "id": "height-two-f-decision-np",
  "status": "running",
  "exit_state": null,
  "finished_at": null,
  "agent_id": "U583bQWoKVFm7yCwV27aDc-window"
}
```

So the previous turn’s mathematical finding is present in this conversation/agent log, but **not yet written into the durable ledger as an investigated finding**. I deliberately did **not** modify the ledger manually: the keeper’s recovery path normally reads the agent output log and updates the entry when the agent is no longer active, and a manual write could race with that mechanism.

**Review item:** confirm that the keeper records this front as `investigated` / `clearexit` from the agent log. If it does not, the ledger needs a manual bookkeeping update — not a re-run of the research.

No unfinished mathematical or external action remains beyond that durable-record check.
