# recursive-abc-exact-height-completeness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

QGBIMrmkHJTIQu97zChC9U-clonic

## exit_state

clearexit

## question

For every finite poset P, does there exist a comparison tree of height exactly F(P) in which every internal node is labelled by a Peczarski A/B/C witness (low-slave, half-balanced, or balanced-triple) for its chosen comparison?

## basis

Board #301 2026-11-10T00:24Z abc-certificate-checking-complexity and 2026-11-09T22:37Z certificate-disjoint-union-closure treat A/B/C as sound GPC witnesses; the running recursive union front does not test general exact-height A/B/C completeness.

## falsifier

Exhibit a finite poset P for which exact minimax shows every height-F(P) comparison tree has at least one node whose chosen incomparable pair satisfies none of the three A/B/C conditions.

## implication

A proof would upgrade A/B/C from sound GPC witnesses to a complete exact-minimax strategy grammar; a counterexample would establish a concrete soundness-versus-completeness separation for recursive A/B/C certificates and block their use as exact S(n) certificates.

## finding_unverified

## Finding

The front's universal claim is **false** under its node-local reading. I found a 6-element counterexample and reported it once to board #301 at `2026-11-10T01:03:19Z`.

**Poset P.** Elements `{a,b,c,d,e,f}` with cover relations

```
f < c < b < a,     d < b,     f < e
```

Equivalently, the witness string `6:000000010003000300000017`. Root counts: `e(P)=14`, so `F(P) ≥ ⌈log₂14⌉ = 4`.

**Key fact.** Every height-4 tree must open with `b` versus `e`:

| pair | branch counts `(e(P+xy), e(P+yx))` |
|---|---|
| `(a,e)` | `(3,11)` |
| `(b,e)` | `(6,8)` |
| `(c,d)` | `(5,9)` |
| `(c,e)` | `(10,4)` |
| `(d,e)` | `(11,3)` |
| `(d,f)` | `(4,10)` |

Every pair other than `{b,e}` has a child with at least 9 extensions, hence that child needs at least 4 further comparisons. For `{b,e}`, both children are sortable in 3 comparisons, so `F(P)=4`.

**The unique optimal pair `{b,e}` is not A/B/C-certified.**

- A: `(b,e)` has `2·6 < 14`; `(e,b)` has two slaves (`c,d`).
- B: `6,8 ≠ 7`.
- C: all eight ordered triples fail. For `(b,e,z)`, the middle bound is `8,10,11,14 > 7`; for `(e,b,z)`, `z=c,d,f` give 14, and `z=a` gives bound 6 but `e(P+e<b+b<a)=8>6`.

Thus every height-`F(P)` tree has an uncertified root — stronger than merely containing one uncertified node.

## Verification

- Independent permutation-based checker: transitive closure by Floyd–Warshall, extension counts over all `6!` orders, A/B/C written directly from Peczarski's definitions. Reproduces `e=14`, all branch counts, and all failures.
- Exhaustive scan of all 318 unlabeled order-6 posets: this and one other counterexample; none at order ≤5.
- The official Gupta classifier reports `bilateral` for `P` (witness pair `{c,d}`), confirming the root is GPC-certifiable while the only optimal move is not.
- Scratch artifact: `/tmp/opencode/abcx/counterexample.py`.

## Honest limits

- This is a general-poset result. It does **not** change `S_unary` or `SORT-BOUND-U`. The order-6 antichain still has an all-certified height-10 optimal tree (`H=F=10` in the exhaustive scan), so no antichain/S(n) counterexample is established.
- It blocks A/B/C as a complete node-local exact-minimax grammar and any exact evaluator that prunes to certificate-positive moves at every state.
- Under a weaker reading where a balanced-triple witness certifies **both** of its comparisons, this example is covered by triples `(c,e,b)` and `(d,e,b)`, and an exhaustive order-7 search found no counterexample. I do not adopt that reading: the triple's counts are computed at the parent state and do not license the child's comparison. This is the precise interpretation boundary.

No Lean or repository changes were made; worktree clean at `6a96398`.

## Other metadata

```json
{
  "finished_at": 1794272659.8060744,
  "started_at": 1794271330.2621942
}
```
