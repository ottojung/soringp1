# antonina-EhRH9IOEgM39JTUBajuMai-pack

Session: ses_e4515de33ffe81apoMz2em7Ldg
Workspace: /home/lubko/soring-fronts/optimal-tree-depth-spread
Created: 1794137268817; updated: 1794141089215

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 437 (msg_1bb240af60013oLTmgGah27IuZ)

**Bottom line:** I found an exact structural counterexample at `n=7` and an exact barrier to the proposed counting falsifier. I did **not** prove whether `s(n)` is bounded or unbounded for all `n`. No Lean or repository changes were made; the worktree is clean.

I inspected the interrupted state first: no earlier board post or commit existed, so I posted the result once to Antonina #301 (2026-11-08 12:30, author `SoringP1 frontier: optimal-tree-depth-spread`).

### 1. Exact small values: `s(7)=2`

For a poset `P`, let `m(P,r)` be the maximum possible minimum relative leaf depth among correct height-`≤r` trees for `P`:

- `m(P,0)=0` for total `P`;
- otherwise  
  `m(P,r)=1+max_{x||y} min(m(P+x<y,r-1), m(P+y<x,r-1))`,

discarding choices whose child cannot be sorted in `r-1`. Only incomparable pairs are compared, so the trees are irredundant. Then `s(n)=S(n)-m(A_n,S(n))`.

Exact exhaustive DP gives:

| `n` | `S(n)` | max min depth | `s(n)` |
|---|---:|---:|---:|
| 1,2 | 0,1 | 0,1 | 0 |
| 3,4,5,6 | 3,5,7,10 | 2,4,6,9 | 1 |
| **7** | **13** | **11** | **2** |

For `n=7`, the leaf-count bound allows minimum depth `floor(log2 7!)=12`, but the DP proves depth `12` is impossible (`need=12` infeasible, 89,589 states, 448 s) while depth `11` is achievable (`need=11` feasible, 20,914 states, 416 s).

**Consequences.** This disproves:

- the strong bounded-spread guess `s(n)≤1`;
- the leaf-count-tight formula `s(n)=S(n)-floor(log2 n!)`, which predicts `1` at `n=7`.

So even when the information bound is tight (`S(7)=C(7)=13`), the combinatorially available near-perfect tree shape cannot be realized by a correct comparison tree. This is a genuine sorting-tree obstruction, not a Kraft/leaf-count effect.

### 2. The stated counting falsifier is blocked by the information gap

Every correct tree has exactly `n!` leaves. If every leaf has depth at least `d`, the tree is perfect to depth `d`, so `n!≥2^d`. Hence

`d ≤ floor(log2 n!) = C(n)-1` for non-power `n!`,

and therefore universally

`\boxed{s(n) ≥ S(n)-floor(log2 n!) = S(n)-C(n)+1}`.

Thus any shallow-leaf counting/entropy argument proving `s(n)≥cn` infinitely often must first prove

`S(n)-C(n) ≥ cn-O(1)` infinitely often.

That is exactly the longstanding information-tightness gap. The general adaptive model has only the information lower bound `S(n)≥C(n)`, while Ford–Johnson gives `S(n)≤C(n)+0.1138n+O(log n)` (Ford–Johnson 1959; Knuth, TAOCP Vol. 3, §5.3.1). No linear lower bound on `S(n)-C(n)` is known. The `n=7` result shows the inequality is strict already in the tight case, so even resolving the information gap would not automatically settle spread.

### 3. Honest limits

- The `n=7` result is an exact finite exhaustive computation, not a paper proof of an all-`n` statement.
- It does **not** decide whether `s(n)` is bounded by an absolute constant. It only rules out `K=1` and shows the next structural obstruction.
- An `n=8` attempt (`need=15`) was killed by memory before completion.
- Certificate soundness here means the necessary condition `e(P)≥2^need`; completeness for `n=7` comes from the exhaustive poset recurrence, not from the leaf bound.
- No claim is made about general partial orders beyond the antichain root, and no Lean verification was attempted.
