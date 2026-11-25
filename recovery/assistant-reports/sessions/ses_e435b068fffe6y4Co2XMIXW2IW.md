# antonina-QBaA3AVy5ifEv5EMPfBd6a-meddle

Session: ses_e435b068fffe6y4Co2XMIXW2IW
Workspace: /home/lubko/soring-fronts/antichain-lookahead-depth
Created: 1794166290892; updated: 1794167111436

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 429 (msg_1bcb0b7b8001GEjJCOTmzCxuPD)

Posted one finding to Antonina #301 as `SoringP1 frontier: antichain-lookahead-depth`; repository remains clean at `6a96398`, with no Lean or repo changes.

## Mathematical finding

Let `C(n)=ceil(log2 n!)` and `E(n)=S(n)-C(n)`. The front has an exact characterization:

**Flatness theorem.** If a poset `P` has at least `2t` isolated elements, then `L_t(P)=L_0(P)`. In particular,

```
L_t(A_n) = C(n)    for every 0 <= t <= floor(n/2).
```

Proof: compare two isolated keys, use that the two children are isomorphic with exactly half the extensions, and induct. This independently re-derives the earlier “linear-depth barrier” theorem and explains `L_2(A_12)=29`: it is the information bound, not an improvement on it.

**Exact equivalence.**

```
There exists an absolute t with L_t(A_n)=S(n) for all n
   <=>  S(n)=C(n) for all sufficiently large n.
```

Hence the true falsifier is:

```
E(n)>0 for infinitely many n.
```

Unbounded excess is sufficient but unnecessary; even `E(n)=1` infinitely often would refute every fixed `t`. The front’s “unbounded excess” parenthetical is stronger than required.

## Consequence

The finite-`t` claim is not an independent finite combinatorial question: it is exactly the open statement that the information lower bound is eventually tight for the sorting number. No unconditional disproof is available from current literature. Finite exact data only refutes small `t`: `S(12)>C(12)` handles `t<=6`; `S(28)>=99>C(28)=98` handles `t<=14`.

The complexity implication is valid but not a new route: eventual tightness itself already gives a polynomial-time evaluator of `S(n)` (output `C(n)` eventually, brute-force the finite initial segment).

## Failed disproof attempt

I tried to prove the incremental bound

```
S(n) >= S(n-1) + floor(log2 n).
```

Combined with the infinitely many “carry” years where `{log2 n!}` wraps, this would prove `E(n)>0` infinitely often and refute the front. I could not prove the inequality, and it is not in the primary sources read. It would already force `S(23)>=76`, while the published envelope still leaves `S(23)=75` possible. So this route is not usable without a genuinely new theorem.

**Honest limit:** no counterexample was found. General-poset fence results (`d(W_n)=Omega(n)`) do not transfer to the antichain; soundness of extension-count pruning does not give completeness at `A_n`. The next decisive target is an infinite-family lower bound `S(n)>C(n)`.

## Output 485 (msg_1bcb16976001TJ3DTVw3R8nHU6)

Recovery inspection complete. No duplicate external action taken.

## Effects that actually happened

- **Host:** `billy-dev`.
- **Board #301:** exactly **one** post from this front:
  - author `SoringP1 frontier: antichain-lookahead-depth`
  - timestamp `2026-11-08T19:44:07.794Z`
  - digest match count: **1**
- **Git:** clean worktree at `6a96398`; no commits, stashes, branches, edits, Lean files, or tests created.
- **Local scratch only:** `/tmp/opencode/antichain-lookahead-post.md` and `/tmp/opencode/antichain-lookahead-result.json`, outside the repository.

## Durable task record

The ledger entry `antichain-lookahead-depth` is still:

- `status: running`
- `exit_state: null`
- `finding_unverified: null`

That is keeper/ledger reconciliation state, not missing research. I did **not** edit it manually or repost the finding.

## Mathematical status

The previous turn completed the intended work: the finite-`t` claim was shown to be exactly equivalent to eventual information tightness `S(n)=C(n)` for all sufficiently large `n`; the correct falsifier is `S(n)>C(n)` infinitely often, not unbounded excess. No unconditional counterexample was found, and the failed incremental-bound route was recorded honestly.

No unfinished mathematical work or uncertain external effect remains.
