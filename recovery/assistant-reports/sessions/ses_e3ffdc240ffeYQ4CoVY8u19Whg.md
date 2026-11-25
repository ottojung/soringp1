# antonina-CfWf5KLvtIzIIaBTIbE9oV-gleam

Session: ses_e3ffdc240ffeYQ4CoVY8u19Whg
Workspace: /home/lubko/soring-fronts/fixed-k-extension-core-dichotomy
Created: 1794222734808; updated: 1794224076108

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 470 (msg_1c01457e8001jG4pSfOb4CvNha)

**Finding: the fixed-\(k\) core-dichotomy claim is TRUE — the proposed falsifiers cannot exist. But the key lemma is not new; it is already in the primary literature.**

## The missing lemma

Kravitz–Sah, *Linear extension numbers of \(n\)-element posets*, Order **38** (2021), 49–66, arXiv:1906.06036, Section 6, Lemma 6.1:

> If \(Q\) is an \(n\)-element poset that is not a disjoint sum of nonempty posets (equivalently, its Hasse/comparability graph is connected), then
> \[
> e(Q)\le (n-1)!.
> \]

Their proof is the spanning-tree induction the front anticipated: take a spanning tree of the Hasse diagram, delete the other covers, choose a leaf \(x\), and insert \(x\) into extensions of \(Q-x\). At most \(n-1\) insertion positions are available, giving \(e(Q)\le(n-1)e(Q-x)\le(n-1)!\). Equality holds exactly for the two star posets \(C_1\oplus A_{n-1}\) and \(A_{n-1}\oplus C_1\).

## Derivation of the front

Let \(P\) be \(n\)-element with \(e(P)\ge n!/k\). Decompose \(P\) into connected components. Let \(Q_1,\dots,Q_r\) be the nontrivial components, of sizes \(s_i\ge2\), let \(Q=\bigsqcup_i Q_i\) and \(s=\sum_i s_i\). Then
\[
P\cong A_{n-s}\sqcup Q.
\]
Put \(c_i=s_i!/e(Q_i)\). Lemma 6.1 gives \(e(Q_i)\le(s_i-1)!\), hence \(c_i\ge s_i\). The disjoint-union identity is
\[
e(P)=\frac{n!}{\prod_i c_i}.
\]
Therefore
\[
\prod_i c_i=\frac{n!}{e(P)}\le k,
\]
and
\[
s=\sum_i s_i\le \prod_i s_i\le \prod_i c_i\le k.
\]
So \(P\) has exactly the required form, the product condition holds, and \(s\le k\). Since there are only finitely many posets on at most \(k\) elements, only finitely many cores \(Q\) occur as \(n\) grows. Conversely, any such \(A_{n-s}\sqcup Q\) has \(e(P)=n!/\prod_i c_i\ge n!/k\), so the characterization is exact.

In particular:
- \(k=2\) gives exactly \(A_n\) and \(A_{n-2}\sqcup C_2\), recovering the board’s dichotomy.
- \(k=3\) gives \(A_n\), \(A_{n-2}\sqcup C_2\), \(A_{n-3}\sqcup V_3\), and \(A_{n-3}\sqcup V_3^{\mathrm{op}}\).

## Falsifier status

- There is no connected \(s\)-element \(Q\) with \(e(Q)>(s-1)!\); Lemma 6.1 rules it out.
- There is no fixed-\(k\) infinite family with \(e(P_n)\ge n!/k\) and unbounded nontrivial core, because \(s\le k\).

## Finite checks

As a sanity check, not as proof, I exhaustively enumerated all \(130{,}023\) labelled posets on \(6\) elements (and all smaller orders): every one satisfies
\[
s\cdot e(P)\le n!,
\]
where \(s\) is the total size of the nontrivial components. The maximum \(e\) among connected posets was \((n-1)!=120\). All tree posets through \(n=8\) also satisfy \(e\le(n-1)!\).

## Honest limits

- The core bound is **literature**, not a new theorem. Kravitz–Sah had already been cited on #301 for other results; the relevant missing piece was Section 6, Lemma 6.1, and its use for this fixed-\(k\) classification.
- This is a general-poset **extension-count** classification. It does not compute \(S(n)\), improve any upper or lower bound for \(S\), or establish P/NP/PSPACE membership.
- It is **not** a certificate soundness or completeness theorem. It says nothing about whether a height-\(k\) sorting tree exists. Knowing \(P=A_{n-s}\sqcup Q\) does not by itself determine the minimax value \(F(P)\); fixed-\(k\) relative-efficiency and insertion still need separate minimax work.
- It says nothing about the low-extension region \(e(P)<n!/k\).

I posted one concise update to board #301 (timestamp `2026-11-09T11:30:53Z`, author `SoringP1 frontier: fixed-k-extension-core-dichotomy`). No repository or Lean changes were made; the worktree remains clean at `6a96398`.

## Output 545 (msg_1c0167350001uCtnhluffBhWmE)

Recovery audit complete. I did **not** repeat the research prompt or create any new external effects.

**Effects that actually happened**
- **Board #301:** exactly one post from this front exists:
  - timestamp `2026-11-09T11:30:53.853Z`
  - author `SoringP1 frontier: fixed-k-extension-core-dichotomy`
  - content: the fixed-\(k\) core-dichotomy claim is TRUE, via Kravitz–Sah Lemma 6.1 and the component-count deduction.
- Searches for `fixed-k-extension-core-dichotomy` find **1 unique match** on the newest board page; no duplicate post was made.
- **Repository:** worktree clean on `billy-dev` at `6a96398`; no commits, stashes, or file changes.
- No Lean changes, no PRs, no other external actions.

**Durable record**
- The keeper ledger still marks `fixed-k-extension-core-dichotomy` as `status: running` with no `finding_unverified`. That is the normal pre-exit state; the keeper records the finding when the session terminates. I did not hand-edit the ledger.

**Mathematical status**
The earlier finding stands: the front is resolved affirmatively by Kravitz–Sah, *Linear extension numbers of \(n\)-element posets*, Order 38 (2021), Lemma 6.1. No counterexample exists. This is a literature-based structural classification, not a new \(S(n)\) bound and not a certificate completeness theorem.

No unfinished work remains.
