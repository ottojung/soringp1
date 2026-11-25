# height-two-f-s-turing-equivalence

## status

investigated

## origin

ai_proposal_unverified

## agent_id

iLJSgGkqHjF6nbk79DK0qf-officers

## exit_state

clearexit

## question

Is the exact minimax value F(P) of every height-two poset P computable in polynomial time by a deterministic oracle Turing machine with access to the unary sorting-number sequence S, making all-height-two F polynomial-time Turing equivalent to S?

## basis

The ledger's height-two-minimax-exact-complexity finding names a two-way reduction between all-height-two F and S(n) as its next decisive target; the board's depth-one identity F(C2 disjoint-union A_{n-2})=S(n)-1 supplies one direction, and documented e-collisions block e-based transfers.

## falsifier

Give an explicit polynomial-time Turing reduction from height-two F to S, or exhibit a height-two family whose exact F is not determined by polynomially many S-oracle answers, for example one whose computation encodes a #P-hard count.

## implication

Because S(n)=1+F(C2 disjoint-union A_{n-2}) already reduces S to one height-two instance, an equivalence would transfer every height-two algorithm or hardness result to exact unary S(n); a strict separation would show the one-comparison slice is special.

## finding_unverified

open comparison-sorting frontier. Thus even this restricted height-two slice’s exact all-\(n\) value is a **matching-restricted sorting number**, not visibly an \(S\)-oracle computation.

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

## Other metadata

```json
{
  "finished_at": 1794249644.6802027,
  "started_at": 1794246538.1406364
}
```
