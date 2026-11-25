# antonina-mKMS3QndNIaNPEN0JdV9KH-exciting

Session: ses_e43ddf66bffeo6Ikotht3AHLsv
Workspace: /home/lubko/soring-fronts/optimal-matching-prefix-normal-form
Created: 1794157709856; updated: 1794158951728

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 475 (msg_1bc334c04001WKbEq9UfRdov7N)

No counterexample found. I did not disprove the matching-prefix front, and I made no repository or Lean changes. The mathematical output is a corrected reduction of the front and a precise obstruction; it is posted to board #301.

## What is actually true

Let

- `P_{n,t} = tC₂ ⊔ A_{n-2t}` — the state after `t` disjoint pair comparisons,
- `M(n) = Σ_{j≤n} ceil(log₂(3j/4))` — the Ford–Johnson count,
- `F` — exact remaining minimax comparisons,
- `k = floor(n/2)`, `a_n = F(M_n)`,
- `C(n) = ceil(log₂ n!)`, and define the two information excesses
  - `E_S(n) = S(n) - C(n)`,
  - `E_M(n) = a_n - (C(n) - k)`.

The standard sandwich is valid:

```
S(n) - t  ≤  F(P_{n,t})  ≤  M(n) - t.
```

A new small all-`n` lemma: for every `n ≥ 2`,

```
F(C₂ ⊔ A_{n-2}) = S(n) - 1.
```

Proof: take an optimal height-`S(n)` tree. Its root compares some pair; both outcomes give the same poset up to relabelling, the two child values are equal, both are at most `S(n)-1`, and one is exactly `S(n)-1`. So equality holds at `t=1`, not only tautologically at `t=0`.

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

## Output 539 (msg_1bc34e7c8001Lsyq1NQmv2MAAq)

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
