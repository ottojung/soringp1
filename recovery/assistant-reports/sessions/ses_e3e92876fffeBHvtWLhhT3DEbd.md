# antonina-iLJSgGkqHjF6nbk79DK0qf-officers

Session: ses_e3e92876fffeBHvtWLhhT3DEbd
Workspace: /home/lubko/soring-fronts/height-two-f-s-turing-equivalence
Created: 1794246539621; updated: 1794249618890

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_1c16d859f001GGV496hwjRp4te)

I'll start by inspecting the current state: repository, git status, docs, and board #301.

## Output 577 (msg_1c19aa1b40011CI3q26bg4p1u2)

Recovery inspection done; no prior side effect was repeated.

## External effects

- **Board #301:** exactly one new comment, at `2026-11-09T18:33:41.823Z`, author `SoringP1 frontier: height-two-f-s-turing-equivalence`. No prior post for this front existed, so nothing was duplicated.
- **Repository:** worktree still clean at `6a96398`; no commit, branch, file, or Lean change.
- **Scratch:** only `/tmp/opencode/h2turing/` and earlier `/tmp/opencode` artifacts.
- The durable ledger still lists the front as `running`; that is keeper-managed operational state, so I did not hand-edit it.

## Mathematical finding

Write \(P_{k,m}=kC_2\sqcup A_m\), i.e. \(k\) disjoint known relations plus \(m\) isolated elements, with \(n=2k+m\). The new rigorous result is the **all-\(n\) sandwich**

\[
S(n)-k \;\le\; F(P_{k,n-2k}) \;\le\; F_{\mathrm{FJ}}(n)-k,
\]

where \(F_{\mathrm{FJ}}(n)=\sum_{j=1}^{n}\lceil\log_2(3j/4)\rceil\) is the Ford–Johnson comparison count.

- **Lower bound:** from a \(P_k\)-strategy of height \(h\), sort the antichain by first comparing the \(k\) pairs, then using the strategy transported across the orientation pattern. Hence \(S(n)\le h+k\).
- **Upper bound:** choose the Ford–Johnson initial pairing to contain the \(k\) prescribed pairs, then omit those \(k\) comparisons. Their outcomes are fixed, and the remaining algorithm is still a correct sorter. Hence \(F(P_k)\le F_{\mathrm{FJ}}(n)-k\).

Since \(F_{\mathrm{FJ}}(n)=S(n)\) for every \(n\le 22\) (Ford–Johnson upper bound against OEIS A036604), this gives the **exact identity**

\[
F(P_{k,n-2k})=S(n)-k \qquad (n\le 22,\ 0\le k\le \lfloor n/2\rfloor).
\]

This extends the board’s one-edge identity \(F(P_{1,n-2})=S(n)-1\) to the whole matching slice in that range.

## Front status and exact obstruction

For all \(n\), the identity would follow from the existence of an optimal sorting tree whose first stage compares a prescribed matching — a “matching-spine” optimal tree. Ford–Johnson supplies such a tree with \(F_{\mathrm{FJ}}(n)\) comparisons, but whether \(F_{\mathrm{FJ}}(n)=S(n)\) beyond \(n=22\) is the standard open comparison-sorting frontier. Thus even this restricted height-two slice’s exact all-\(n\) value is a **matching-restricted sorting number**, not visibly an \(S\)-oracle computation.

I did **not** find:

- a polynomial-time Turing reduction from all-height-two \(F\) to \(S\);
- a height-two family whose \(F\) is not determined by polynomially many \(S\)-oracle answers;
- a \(\#P\)-hard height-two family;
- any separation or unconditional non-reduction.

A failure of the matching identity at some \(n,k\) would only show that the matching slice is not exactly \(S\); it would not refute all-height-two \(F\le_T S\).

## Other relevant distinctions

- **General posets do not transfer:** \(\#H2LE\) is \(\#P\)-complete (Dittmer–Pak), but \(F\) is not a function of \(e\) (the \(n=6\) collision: \(e=60\), \(F=6\) vs \(7\)).
- **Output-size barrier:** \(F(P)\le S(n)=O(n\log n)\), so one \(F(P)\) value has only \(O(\log n)\) bits. It cannot encode \(e(P)\) or a \(\#P\) count of super-logarithmic length; any \(\#P\)-hardness of \(F\) would have to be a Turing reduction over many derived instances.
- **Conditional complexity barrier:** if height-two \(F\) were \(\#P\)-hard, then \(F\le_T S\) would put \(\#P\subseteq FP/poly\), hence \(PH=\Sigma_2P\) by Toda plus Karp–Lipton. This is a hypothetical barrier, not a proved hardness.
- **Soundness vs completeness:** leaf counting and Ford–Johnson are sound upper/lower certificates, but not complete; \(e\)-thresholds are incomplete because of the collision, and the \(n\le22\) matching theorem is completeness only on that slice.
- The one-comparison slice is not the only \(S\)-hard height-two family: \(F(K_{m,m})=2S(m)\) gives another unconditional one, and the matching slice is exactly \(S\)-equivalent through \(n=22\).

**Honest bottom line:** the all-height-two equivalence remains open. The new content is the sandwich, the finite exact matching identity, and the precise reduction of the remaining matching-slice obstacle to matching-spine/Ford–Johnson optimality.

## Output 646 (msg_1c19c5801001jyPzWEzlYmYp7Q)

Recovery inspection complete; nothing was repeated.

## Effects confirmed

- **Host:** `billy-dev`.
- **Repository:** `/home/lubko/soring-fronts/height-two-f-s-turing-equivalence`; worktree clean at `6a96398`; no commits, branches, files, or Lean changes.
- **Board #301:** exactly **one** post for this front, at `2026-11-09T18:33:41.823Z`, author `SoringP1 frontier: height-two-f-s-turing-equivalence`. No duplicate was made.
- **Scratch:** only `/tmp/opencode/h2turing/`, outside the repository.

## Unfinished / uncertain items

- The durable ledger still records `height-two-f-s-turing-equivalence` as `status: running` with no finding recorded, under agent `iLJSgGkqHjF6nbk79DK0qf-officers`.
- This is keeper/Executive bookkeeping, not a missing research result. I did **not** hand-edit the ledger, since doing so could race with the keeper’s reconciliation.

## Mathematical result already delivered

The board post contains the complete result; I did not re-run or repost it:

- All-\(n\) sandwich  
  \[
  S(n)-k\le F(kC_2\sqcup A_{n-2k})\le F_{\mathrm{FJ}}(n)-k.
  \]
- Exact identity \(F(kC_2\sqcup A_{n-2k})=S(n)-k\) for every \(n\le22\).
- All-\(n\) equality reduces to the open matching-spine/Ford–Johnson pairing question.
- No all-height-two reduction to \(S\), no separating family, no \(\#P\)-hardness result, and no repository change.

No further external action is warranted; the only pending item is keeper reconciliation of the ledger record.
