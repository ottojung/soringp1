# class-stable-optimal-strategy-chain-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

pJiCpHbL5LGEDPjabSjqKP-reply

## exit_state

clearexit

## question

Does there exist any n >= 3 admitting a height-S(n) optimal comparison strategy from the n-element antichain in which every comparison yields two unlabeled-isomorphic outcome posets?

## basis

Independent exhaustive search on billy-dev (n<=6): roots have symmetric optimal pairs but no full height-S(n) unlabeled-child-isomorphic chain exists for n=3..6; motivated by #301 m(8)=22 class-collapsing next step.

## falsifier

Exhibit some n >= 3 with an explicit verified height-S(n) strategy where every internal comparison has isomorphic unlabeled children, or prove no such strategy exists for all n >= 3.

## implication

A yes instance collapses an optimal play to a chain of S(n)+1 isomorphism classes, giving a maximally succinct strategy normal form; an all-n no is a barrier to sibling-outcome class compression.

## finding_unverified

ts on resume).
No prior post by my author string. Let me post the single report to board #301.
Let me verify the comment actually posted (the JSON returned the issue object).
The report is posted (single comment). Final side-effect audit:
Done. Here is my completion report.

## Mathematical finding (paper proof, all n)

**The FRONT question has answer NO for every n ≥ 3:** there is no height‑`S(n)` optimal comparison strategy from the `n`‑antichain in which every internal comparison yields two unlabeled‑isomorphic outcome posets.

The decisive obstruction is a counting identity, not an exhaustive search:

> **Lemma.** If a poset `Q` admits a correct sorting tree of height exactly `F(Q)` in which every internal node's two outcomes are unlabeled‑isomorphic, then `L(Q) = 2^{F(Q)}` (`L` = number of linear extensions).

*Why:* for such a tree, inputs reaching a node `v` are exactly `Ext(P_v)`, so its subtree has `L(P_v)` leaves. Because `F` is a minimum height and `S(n)=F(antichain)`, a top‑down induction shows at every internal node `h_T(v)=F(P_v)` and the two (isomorphic) children have equal subtree height `F(child)`. Hence every subtree is a perfect binary tree of height `F(P_v)` with `2^{F(P_v)}` leaves, forcing `L(Q)=2^{F(Q)}`.

Applying it to the antichain: `n! = 2^{S(n)}`. But `3 | n!` for `n ≥ 3`, so `n!` is never a power of two — contradiction. The boundary `n ≥ 3` is *exactly* where `n!` stops being a power of two (`n=0,1,2` trivially work). This also explains why the earlier `n≤6` exhaustive search found symmetric root pairs but no full chain: the obstruction sits strictly below the root.

## Serious falsification attempt (failed, as expected)

I tried to construct a yes‑instance by taking a diagonal optimal split at each depth, exploiting the fully symmetric root. It dies at depth 1 for every `n≥3`: at `P={i<j, k isolated}` all optimal incomparable pairs have non‑isomorphic children (e.g. `n=3`: `V`‑poset vs chain, chain vs `Λ`‑poset). Adaptivity and relabelling cannot bypass an information‑theoretic leaf count.

## Independent verification (scratch only)

A from‑scratch Go verifier (`/tmp/opencode/classstable/verify.go`) reproduced class counts A000112(2..6)=2,5,16,63,318 and `S(2..6)=1,3,5,7,10`. The all‑diagonal strategy predicate is true only for `n=2`, false for `n=3..6`. Scanning **all** classes up to `n=6`: 0 violations of the lemma, and the converse already fails at `n=4` (3 classes with `L=2^F` but no diagonal strategy) — confirming the condition is necessary, not sufficient.

## Honest limits

- This is a **structural barrier for the fixed antichain family and `S(n)`**, not a general‑poset (GEN‑SORT) hardness result and not a complexity‑class statement — no P/NP/PSPACE membership or separation follows.
- It is distinct from certificate **soundness**: soundness verifies an upper bound; this result neither provides nor refutes completeness of any certificate system.
- It does **not** rule out other succinct normal forms — the board's `m(8)=22` shows substantial class compression survives; only the extreme one‑class‑per‑depth collapse is impossible.
- It is an elementary counting obstruction, **not** a faster evaluator or improved bound for `S(n)`; no known value or complexity bound changes.

No repository, Lean, test, workflow, ledger, or `main` changes. Worktree clean at `6a96398` on `billy-dev`; scratch confined to `/tmp/opencode/classstable`. One board comment posted to #301 (verified: exactly one post by this author).

## Other metadata

```json
{
  "finished_at": 1795102860.1402142,
  "started_at": 1795102350.1126657
}
```
