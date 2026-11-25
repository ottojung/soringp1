# optimal-matching-prefix-normal-form

## status

investigated

## origin

ai_proposal_unverified

## agent_id

mKMS3QndNIaNPEN0JdV9KH-exciting

## exit_state

clearexit

## question

For every n, is there an optimal height-S(n) sorting tree whose first floor(n/2) comparisons are pairwise disjoint, so that S(n) = floor(n/2) + F(M_n), where M_n is the matching poset of floor(n/2) two-chains plus one singleton when n is odd?

## basis

Ford-Johnson pairing is optimal through n<=11, and a local exact-minimax check at n<=8 is consistent with the identity (evidence only, not a proof); docs/problem.md and docs/research-plan.md fix the model and values; board #301 split-merge and GPC threads; no ledger front tests a matching-prefix normal form, so a primary-literature check is part of the front.

## falsifier

An explicit n with S(n) < floor(n/2) + F(M_n), equivalently a proof that every optimal-height tree for that n uses a comparison sharing a key among its first floor(n/2) comparisons.

## implication

A positive answer gives an exact structural reduction of the minimax game to the single matching-poset family and a new normal form for exact evaluation; a counterexample shows that sharing comparisons in the opening phase is essential and blocks the pairing-reduction route to S(n).

## finding_unverified

he same poset up to relabelling, the two child values are equal, both are at most `S(n)-1`, and one is exactly `S(n)-1`. So equality holds at `t=1`, not only tautologically at `t=0`.

Consequently, the front is exactly

```
E_M(n) = E_S(n).
```

Both quantities lie in `[0, E_FJ(n)]`, where `E_FJ = M - C`. Ford–Johnson optimality implies the front because `E_M ≤ E_FJ`, but the converse is false. This is the exact reason the `n=47` Ford–Johnson non-optimality result does **not** refute the front: it gives only `E_S(47) ≤ E_FJ(47)-1`; `E_M(47)` may be lower or equal.

## Finite status and first possible falsifier

For every `n ≤ 22`, `S(n) = M(n)`, so the front holds throughout that range. The first possible failure is `n=23`. There:

```
C(23)=75, M(23)=76, k=11,
a_23 ∈ {64,65},  S(23) ∈ {75,76}.
```

The front holds for `(a_23,S(23)) = (64,75)` or `(65,76)`, and fails exactly for `(65,75)`. The pair `(64,76)` is impossible, since pairing plus a 64-comparison matching sorter would sort 23 keys in 75 comparisons. Thus a counterexample at `n=23` needs both:

1. a proof that `M_23` is not sortable in 64 comparisons, and
2. an explicit 75-comparison sorter for 23 keys.

Neither is known. At `n=47`, the analogous failure route requires `a_47 = 178`, i.e. `E_M(47)=E_FJ(47)=3`.

## Failed concrete route

The obvious way to get `a_23=64` is: sort the 11 winners optimally (`S(11)=26`), then insert the 11 losers plus straggler. For a fixed insertion order, with anchor index `i` and `t` prior insertions, the binary-search prefix has at most `i+t` slots (straggler: `12+t`), so the abstract cost is `ceil(log₂(i+t))` / `ceil(log₂(12+t))`. A subset DP over all `12!` orders gives minimum **39**, exactly the Ford–Johnson insertion cost:

```
11 + 26 + 39 = 76.
```

So no fixed-order binary-insertion schedule reaches 75. This does not rule out a different architecture, but it closes the obvious schedule-optimisation route.

## Honest limits

- No counterexample to the front was found.
- The front is **not** equivalent to Ford–Johnson optimality; the earlier board equivalence was already withdrawn, and the new `t=1` lemma shows even more strongly that “equality at some `t`” is automatic.
- No entropy, selection-rank, or general-poset lower bound distinguishes the matching value from `S(n)-k`.
- A genuine disproof must produce a matching-poset lower bound strictly above entropy, or equivalently show that every optimal sorter for some `n` must share comparisons in its first `floor(n/2)` steps.

The worktree is clean.
Recovery check complete. The previous turn’s external effect did happen, so I did not repeat it.

**Durable state verified**

- Board #301 contains exactly one post by agent `SoringP1 frontier: matching-prefix-normal-form`, timestamped `2026-11-08T17:27:09.762Z`.
- Post title/content matches the completed work: no counterexample to the matching-prefix normal form; corrected excess formulation; new `t=1` lemma; first possible case `n=23`; failed insertion-schedule route.
- Local artifacts exist under `/tmp/opencode/`:
  - `matching_prefix_post.md`
  - `board_post_result.json`
- Git worktree is clean. No commits, branches, repository files, or Lean files were created or changed.

**Conclusion**

All intended work from the interrupted turn is already complete. The only external side effect was the single board #301 comment, now independently confirmed present. I made no additional posts or changes and do not need to rerun the research or post again.

## Other metadata

```json
{
  "finished_at": 1794158954.1835666,
  "started_at": 1794157709.169076
}
```
