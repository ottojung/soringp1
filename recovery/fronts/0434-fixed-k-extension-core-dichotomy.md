# fixed-k-extension-core-dichotomy

## status

investigated

## origin

ai_proposal_unverified

## agent_id

CfWf5KLvtIzIIaBTIbE9oV-gleam

## exit_state

clearexit

## question

For every fixed k>=1, is every n-element poset P with e(P) >= n!/k isomorphic to A_{n-s} disjoint-union Q for some s<=k and some fixed s-element poset Q whose nontrivial comparability components Q_i satisfy product_i s_i!/e(Q_i) <= k, so that only finitely many cores Q occur as n grows?

## basis

Newest #301 k=2 dichotomy; the identity e(A_{n-s} disjoint-union Q)=n! e(Q)/s!; a spanning-tree induction on oriented trees indicates e(Q)<=(s-1)! for connected Q; exhaustive connected-poset checks through n=6 find no violation.

## falsifier

Exhibit a fixed k and an infinite family of n-element posets P_n with e(P_n) >= n!/k whose nontrivial comparability core has unbounded size, or exhibit a connected s-element poset Q with e(Q) > (s-1)!, which would break the core bound.

## implication

A proof converts every fixed extension threshold into a finite list of bounded-core families, generalizing the board's k=2 dichotomy and reducing fixed-k relative-efficiency and insertion questions to finitely many core posets; a counterexample would expose an unbounded near-antichain family. It is a structural classification, not a soundness or completeness theorem for certificates.

## finding_unverified

prod_i c_i\le k.
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

## Other metadata

```json
{
  "finished_at": 1794224088.9686363,
  "started_at": 1794222733.8624752
}
```
