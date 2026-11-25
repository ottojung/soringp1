# antonina-BWsV2XVdvmuCSsrbbzNPdB-religion

Session: ses_e3cda9652ffeJuu9e5NkFXcp3C
Workspace: /home/lubko/soring-fronts/prime-excess-unbounded
Created: 1794275371628; updated: 1794276086366

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 16 (msg_1c3257eed001pl9wygM812sTv2)

I'll start by inspecting the environment state and any durable records before doing any work.

## Output 307 (msg_1c330066a001YZIUcXEwp51Mgg)

## Recovery / side effects

- Host: `billy-dev`; worktree clean at `6a96398`; no commits, Lean, tests, or repository edits.
- I found the interrupted turn’s board post **already present**: `2026-11-10T01:56:17Z`, author `SoringP1 frontier: prime-excess-unboundedness`. It already proves the main unconditional unboundedness theorem by iterated self-gluing of the `n=27` base.
- I did **not** repeat that theorem. I posted exactly one follow-up at `2026-11-10T02:00:40Z` containing only new material: the strict `A_a(+)A_b` class theorem and a smaller `n=34` explicit excess-4 witness. Verified as one unique post.
- Ledger entry `prime-excess-unbounded` remains `running`; I left it untouched.

## Mathematical findings

### 1. The literal front class does not amplify beyond the global gap

For \(a,b\ge 2\), let

\[
P=(A_a\oplus A_b)\setminus\{(a_0,b_0)\}.
\]

Then, by a two-case extension count,

\[
e(P)=a!\,b!+(a-1)!\,(b-1)!.
\]

Moreover,

\[
F(P)\in\{S(a)+S(b),\;S(a)+S(b)+1\}.
\]

Lower bound: adding the deleted relation back gives the ordinal sum \(A_a\oplus A_b\), so \(F(P)\ge S(a)+S(b)\). Upper bound: sort both antichains separately, infer \(a_0<b_0\) by transitivity unless \(a_0\) is maximal in \(A\) and \(b_0\) is minimal in \(B\), and only in that case compare \(a_0,b_0\).

Writing \(C_m=\lceil\log_2 m!\rceil\), \(E(m)=S(m)-C_m\), one gets

\[
\boxed{\;E(a)+E(b)-1\;\le\;F(P)-\lceil\log_2 e(P)\rceil\;\le\;E(a)+E(b)+2\;}
\]

So the literal single-deletion-from-\(A_a\oplus A_b\) class is **unbounded iff \(E(n)\) is unbounded**. Deleting one cross relation cannot amplify local excess beyond an additive constant. The previous 01:56Z statement that “this family alone does not grow” is therefore only conditional: it follows from bounded \(E\), which is open.

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

## Output 319 (msg_1c33031c0001GeSMQtoL2U2VQt)

Verifying existing work before taking any further action.

## Output 337 (msg_1c3304a93001SxaPADxiTjRA65)

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
