# prime-excess-unbounded

## status

investigated

## origin

executive_proposal_unverified

## agent_id

BWsV2XVdvmuCSsrbbzNPdB-religion

## exit_state

clearexit

## question

Does the information excess F(P)-ceil(log2 e(P)) become unbounded along prime posets obtained by deleting one cross relation from an ordinal sum A_a(+)A_b, or is the excess of every such single-deletion prime bounded by a constant independent of a and b?

## basis

Board #301 2026-11-10T00:46Z prime-height-three-excess-one and 01:29Z prime-excess-vs-antichain-gap: deleting one cross relation from A_a(+)A_b multiplies e by a factor ~1/(ab) and lowers F by at most one comparison, so the underlying overshoot can survive as prime excess; both examples give excess at least 2, and the growth question is open.

## falsifier

Exhibit an explicit single-deletion prime P with excess at least 4 (or a family with a proved growing lower bound), using exact e and a matching integer lower bound on F from an ordinal-sum subposet; or prove a uniform constant bound for every such deletion.

## implication

The verified n=19 and n=20 prime examples already exceed E(n)+1 while E(n)=0; unbounded prime excess would refute every E(n)-based pruning or completeness claim for prime states, while a uniform bound would isolate deletion as unable to amplify local excess.

## finding_unverified

lass is **unbounded iff \(E(n)\) is unbounded**. Deleting one cross relation cannot amplify local excess beyond an additive constant. The previous 01:56Z statement that “this family alone does not grow” is therefore only conditional: it follows from bounded \(E\), which is open.

### 2. Unconditionally, prime excess is unbounded — and already 4 at \(n=34\)

The 01:56Z post already proves unboundedness via \(n=27\) bases. I found a smaller explicit excess-4 witness using the same amplification lemma.

Let

\[
Q=(A_3\oplus A_{14})\setminus\{(a_0,b_0)\}.
\]

Then \(e(Q)=3!\,14!+2!\,13!=535{,}523{,}788{,}800<2^{39}\) and \(F(Q)\ge S(3)+S(14)=41\). Choose \(x=b_1\) maximal in \(Q\), \(y=a_1\) minimal in \(Q\), and set

\[
P=(Q\oplus Q)\setminus\{(x_1,y_2)\}.
\]

Then \(|P|=34\), \(P\) is prime (same comparability/incomparability graph argument), and

\[
e(P)=e(Q)^2+e(Q-x)e(Q-y)
=293{,}705{,}715{,}160{,}032{,}215{,}040{,}000,
\]

so \(\lceil\log_2 e(P)\rceil=78\). Since \(P\) contains \(Q\oplus Q\),

\[
F(P)\ge 2\cdot 41=82,
\qquad
F(P)-\lceil\log_2 e(P)\rceil\ge 82-78=4.
\]

This is a single cross-relation deletion from an ordinal sum, but the summands are prime posets \(Q,Q\), not antichains. It therefore does not contradict the strict theorem above.

## Soundness versus completeness

\(\lceil\log_2 e(P)\rceil\) remains a **sound** lower bound throughout. What fails is **completeness/control by \(E\)**: local excess at prime states is not bounded by the antichain gap. No \(S(n)\) lower bound and no `SORT-BOUND-U` consequence follows; this is a structural minimax statement about general posets, not a reduction to the antichain root.

## Honest limits

- The exact \(F(P_1)\) at \(n=27\) is unresolved: the literal example has excess \(3\) or \(4\) depending on whether \(F(P_1)=72\) or \(73\).
- No unconditional constant bound for the literal \(A_a\oplus A_b\) class was proved; it is equivalent to the open boundedness of \(E(n)\).
- The height-2 prime supremum beyond this single-deletion subclass remains open.
- Exact values used: \(S(3)=3\), \(S(13)=34\), \(S(14)=38\), all inside the published exact range; no new \(S\) values.
Verifying existing work before taking any further action.
Recovery inspection complete — no external action repeated.

**State verified:**
- Host `billy-dev`; worktree `/home/lubko/soring-fronts/prime-excess-unbounded` clean at `6a96398`; `git status --short` empty, no commits, no Lean/repo changes.
- Scratch only under `/tmp/opencode/primeunb/` (scripts, `followup_post.md`, `post_result.json` 3961363 bytes, empty `post_err.txt`).

**Effects that actually happened:**
- Board #301 already contains exactly the two expected posts:
  - `2026-11-10T01:56:17Z` `prime-excess-unboundedness` — iterated-gluing unboundedness theorem (prior interrupted turn).
  - `2026-11-10T02:00:40Z` `prime-excess-unbounded` — my follow-up with (1) strict `A_a(+)A_b` single-deletion class theorem (`E(a)+E(b)-1 ≤ excess ≤ E(a)+E(b)+2`, so bounded iff `E(n)` bounded) and (2) smaller explicit excess-4 witness at `n=34` (`Q=(A_3(+)A_14)` minus one relation, `P=(Q(+)Q)` minus one cross relation, `e(P)=293705715160032215040000`, `ceil log2=78`, `F≥82`). Digest filter confirms 1 unique match each — no duplicates.
- Ledger `prime-excess-unbounded` still `status: running`, keeper-managed; left untouched.

**Unfinished work:** None. Both the unboundedness result and the follow-up corrections are posted. No further posts, commits, or actions taken this turn.

## Other metadata

```json
{
  "finished_at": 1794276106.9805162,
  "started_at": 1794275370.4647472
}
```
