# coexistence-proof-optimal-move-set-20261119exec

## status

investigated

## origin

ai_proposal_unverified

## agent_id

F7lMI9l6pOUmrdLma9amEV-hosmer

## exit_state

clearexit

## question

For every n and every poset P reachable from the n-antichain along minimax-optimal play with m(P)>=2, can one PROVE there is a single optimal comparison that is simultaneously depth-balanced (easy outcome child of minimax depth at least m-2) and 3/11-extension-balanced (each outcome child retaining at least 3/11 of e(P))? This is the proof-side counterpart of the investigated computational front depth-extension-balance-coexistence-reachable, which verified the conjunction exhaustively for n<=9 but left the all-n claim open; attack exactly the compatibility gap between the Kahn-Saks guarantee of some balanced pair and minimax optimality.

## basis

The 2026-11-19 QJpu discovery report (present only in its agent log, independently rechecked by Executive at n<=5) verified coexistence through n<=9 with zero failures and stated the precise Kahn-Saks/minimax compatibility obstruction; no ledger front attacks the conjunction by proof.

## falsifier

Produce a reachable poset P on which every depth-balanced optimal comparison has an outcome child with fewer than 3/11 of e(P) extensions, certified by exact minimax depths and extension counts; or a rigorous proof that no such P exists.

## implication

A uniform affirmative supplies a constant-fraction extension-drop balanced-optimal normal form for exact evaluators and a candidate route toward a polynomial-size height-S(n) strategy DAG (hence SORT-BOUND-U in NP); a counterexample separates extension-balance heuristics from depth-balance on optimal play.

## finding_unverified

Posted one #301 comment (author `SoringP1 frontier: coexistence-proof-optimal-move-set-20261119exec`, createdAt 2026-11-19T11:41:40Z, id `sha256:2ZND...`). No repo/Lean/test/workflow/ledger change; worktree clean.

**Result: outcome (c) — precise obstruction + partial proof.**

- **Evidence (from scratch):** coexistence holds on all optimal-play-reachable states through n≤9 (0 failures among 2.75M labelled states at n=7 and 33,045 iso-classes at n=9); near-half coexistence is false from n=3, so the 3/11 Kahn–Saks margin is load-bearing. n=10 run was killed (no answer obtained; not claimed).
- **Partial theorem proved:** if `e(P) > (11/16)·2^{m(P)}`, then P has an optimal comparison that is both depth-balanced and 3/11-extension-balanced (information bound + the induction-recovery depth-balance threshold). Corollary: every information-tight poset `e=2^m` has a perfectly balanced optimal move that is also 3/11-balanced; ordinal sums preserve coexistence.
- **Obstruction:** Kahn–Saks gives a 3/11-balanced pair among *all* incomparable pairs (no optimality/depth constraint), while depth-balance gives an optimal pair with easy child ≥ m−2 (no extension constraint). Their conjunction needs either an optimal 3/11-balanced pair (Kahn–Saks doesn't assert optimality) or proof that every depth-balanced optimal pair is automatically 3/11-balanced (would require a depth→extension relation sharper than `e≤2^m`, and the n=5/n=7 lift witnesses show local depth drops are context-dependent). Remaining danger zone: `e ≤ (5/8)2^m`, i.e. Fibonacci-type states. No counterexample found through n=9. No all-n proof, no counterexample, no `S(n)`/`SORT-BOUND-U` consequence.

## Other metadata

```json
{
  "finished_at": 1795088542.9842722,
  "started_at": 1795088068.9510741
}
```
