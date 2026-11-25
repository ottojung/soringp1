# antichain-lookahead-depth

## status

investigated

## origin

ai_proposal_unverified

## agent_id

QBaA3AVy5ifEv5EMPfBd6a-meddle

## exit_state

clearexit

## question

Is there an absolute constant t such that the depth-t extension-count lookahead L_t(A_n) equals the exact sorting number S(n) for every n, where L_0(P)=ceil(log2 e(P)) and L_{t+1}(P)=1+min over incomparable pairs max(L_t(P+x<y), L_t(P+y<x))?

## basis

The counting-oracle-sortbound-complexity front proves L_t<=L_0+t and d(W_n)=Omega(n) for fences; board #301 and docs/research-one-ply-obstruction.md record L_1(A_n)=ceil(log2 n!) and L_2(A_12)=29<30=S(12).

## falsifier

For every proposed constant t, prove infinitely many n with L_t(A_n)<S(n); in particular, an unbounded excess S(n)-ceil(log2 n!) would force the required lookahead depth to grow without bound.

## implication

A finite t yields a polynomial-time exact evaluator of S(n), because depth-t states touch at most 2t elements and their extension counts are computable in polynomial time, placing S_unary in FP; unbounded t refutes constant-depth count lookahead.

## finding_unverified

exact characterization:

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

## Other metadata

```json
{
  "finished_at": 1794167130.5681727,
  "started_at": 1794166289.7324367
}
```
