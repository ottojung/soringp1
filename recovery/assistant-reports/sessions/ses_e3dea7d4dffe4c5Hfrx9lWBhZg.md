# antonina-N7YUdbEHrvpGx0ktKlhnX4-eyelid

Session: ses_e3dea7d4dffe4c5Hfrx9lWBhZg
Workspace: /home/lubko/soring-fronts/disjoint-union-minimax-superadditivity
Created: 1794257552365; updated: 1794259756331

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1c2158a57001SOkJs3jWOH7CZ7)

I'll start by studying the repository state and the referenced materials.

## Output 747 (msg_1c235f131001K9dNyOs5jand6Y)

## Result

The front is **true for all finite posets**: the proposed falsifier cannot exist. I posted the finding to Antonina #301 on `billy-dev`. Worktree remains clean; no Lean or repository changes were made.

### Theorem (paper proof)

For all finite posets \(A,B\) on disjoint ground sets,

\[
F(A\sqcup B)\ \ge\ F(A)+F(B).
\]

Proof. Let \(A\oplus B\) be the ordinal sum (all of \(A\) below all of \(B\)). Then \(A\sqcup B\) is a subposet of \(A\oplus B\), so

\[
L(A\oplus B)\subseteq L(A\sqcup B).
\]

A comparison tree that identifies every linear extension of \(A\sqcup B\) also identifies every member of the subset \(L(A\oplus B)\). Hence \(F(A\oplus B)\le F(A\sqcup B)\). Ordinal-sum additivity gives \(F(A\oplus B)=F(A)+F(B)\) (repo proof in `docs/research-series-decomposition.md` §2; direct-sum theorem of Jain–Klauck–Sántha, IPL 2010). Chaining proves the claim. ∎

This uses only monotonicity of \(F\) under adding comparabilities and the standard ordinal-sum identity. It does **not** claim additivity for disjoint union: \(F(A_2\sqcup A_2)=5>2=F(A_2)+F(A_2)\). The 20:42Z correction is about a false insertion/equality formula involving \(I(|K|,s)\neq F(A_s)\), not about this inequality.

### Falsification attempt (exact minimax, not information bounds)

Using the repository's exact iso-quotient minimax recurrence:

- all poset pairs of total size \(n\le 8\): **0 violations**. Pair counts: \(5,14,46,178,851,5138,40246\).
- at \(n=8\), every nondegenerate pair has slack at least \(3\) (slack \(0\) occurs only with an empty component).
- for \(n=9\), a sound information prune over all \(23{,}687\) split pairs found **0 candidates** satisfying \(\lceil\log_2 e(A\sqcup B)\rceil\le F(A)+F(B)-1\); hence superadditivity at \(n=9\) also follows from \(F\ge\log_2 e\).

These finite checks corroborate the proof but are not the proof.

### Exact obstruction to the natural induction

The tempting component potential
\[
\Phi(P)=F(P|_A)+F(P|_B)-c(P)
\]
(where \(c(P)\) is the number of edge-containing components of the cross-comparability graph) survives exhaustive checks \(n\le8\), but it is **not** an adversary potential. Explicit \(n=6\) witness:

\[
P=(0,1,1,3,5,21),\quad A=\{2,3\},\quad B=\{0,1,4,5\},
\]
with exact values \(F(P)=4\), \(F(P|_A)=1\), \(F(P|_B)=2\), \(c(P)=1\), so \(\Phi(P)=2\). The single comparison \(1<4\) inside \(B\) has children with exact \(F=2\) and \(F=3\), and both children have \(\Phi=0\). One query drops \(\Phi\) by \(2\): it mediates \(3<2\) through \(3<1<4<2\), doing double duty across the two induced blocks. The maximum-matching correction fails similarly (drop \(3\)). This explains why a component-count/matching induction is the wrong route, even though the theorem is true.

### Honest limits

- This is a structural theorem about the minimax game, not a complexity-class result and not an improvement of the established \(SORT-BOUND-U\) bounds.
- It does not give a faster exact evaluator or an NP certificate.
- The finite scans are complete only for the tested sizes; they are not a substitute for the proof.
- Novelty is low/folklore-adjacent. The value is closing the front, ruling out the falsifier, and recording the precise failure of the obvious cross-component induction.

An Executive 21:17Z note also stated the conclusion; the monotonicity + ordinal-sum proof above is the argument I checked and stand behind.

## Output 807 (msg_1c2370c90001qjc4ihOJWGciFt)

Recovery inspection complete.

## Effects that actually happened

- **Board post: confirmed, exactly once.** Antonina #301 contains my post at `2026-11-09T21:27:41.054Z` under `SoringP1 frontier: disjoint-union-minimax-superadditivity`. It was followed by an independent Viche Executive verification at `21:28:06Z`. I did **not** repost or comment again.
- **Git: no changes.** Worktree is clean on `billy-dev` at `6a96398`; no commits, branches, or repository files were created or modified.
- **Lean: untouched.**
- **Scratch: only `/tmp/opencode/du_superadd/`**, containing the scan scripts, logs, and the board-post draft. No repository side effects.
- **Background job:** the `n9stats.py` process was deliberately killed; it was scratch-only and produced no external effect.

## Remaining work

None. The research question was resolved in the prior turn with a paper proof and finite exact-minimax checks, and the finding was posted. Repeating the prompt would risk duplicating the #301 post, so I stopped after verification.

## Result recorded

The front is **true**: for all finite posets \(A,B\) on disjoint ground sets,

\[
F(A\sqcup B)\ge F(A)+F(B),
\]

because \(A\sqcup B\) is a subposet of the ordinal sum \(A\oplus B\), hence \(L(A\oplus B)\subseteq L(A\sqcup B)\), so \(F(A\oplus B)\le F(A\sqcup B)\), and \(F(A\oplus B)=F(A)+F(B)\).

The falsifier cannot exist. The exact component-potential obstruction and the finite scans (\(n\le8\) exhaustive; \(n=9\) information-pruned) are in the existing #301 post.
