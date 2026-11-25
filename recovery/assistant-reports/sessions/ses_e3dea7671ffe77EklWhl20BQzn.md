# antonina-VnzbFEgglvaBjpWItcUCtm-stature

Session: ses_e3dea7671ffe77EklWhl20BQzn
Workspace: /home/lubko/soring-fronts/two-wl-child-extension-count-soundness
Created: 1794257554162; updated: 1794258938172

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1c2158df1001jNGxtwuaMB07WG)

I'll start by studying the repository context and the current research board.

## Output 492 (msg_1c22819d5001vGBC39Rd3hHoCx)

## Result

The all-`n` claim is **false**. The stable full/paired 2-WL colour does **not** determine the unordered pair of exact child extension counts, even for height-two incidence posets.

Posted to board #301 at `2026-11-09T21:11:47Z`; worktree clean at `6a96398`; no repository or Lean changes.

## Explicit counterexample

Let `P` be the incidence poset of the `(16,6,2)` biplane `D_7` already used by the earlier n=32 child-isomorphism front:

- `G = Z₂ × Z₈`, `D = {(0,0),(0,1),(1,0),(1,2),(1,5),(1,6)}`, whose ordered differences cover every non-identity element exactly twice;
- points `0..15` minimal, blocks `16..31` maximal, `x < 16+idx(g)` iff `x = idx(g+d)` for some `d ∈ D`;
- height two, 32 elements, `N(0) = {0,7,8,10,11,14}`, so blocks `17,18` are incomparable with point `0`.

All **160** nonincident point–block pairs share one stable full/paired 2-WL colour: `(3,5)` in the board’s labelling, `(5,7)` under an independent rank-canonical implementation. In particular `{0,17}` and `{0,18}` have identical ordered colours.

| pair | `e(P+x<y)` | `e(P+y<x)` | unordered pair |
|---|---:|---:|---|
| `{0,17}` | 2,276,299,698,560,887,528,488,960,000 | 49,924,969,500,547,847,946,240,000 | `A` |
| `{0,18}` | 2,276,301,192,920,103,671,562,240,000 | 49,923,475,141,331,704,872,960,000 | `B` |

with

- `A = {49,924,969,500,547,847,946,240,000, 2,276,299,698,560,887,528,488,960,000}`
- `B = {49,923,475,141,331,704,872,960,000, 2,276,301,192,920,103,671,562,240,000}`

`A ≠ B`; each coordinate differs by `1,494,359,216,143,073,280,000`. Both child-count sums equal

`e(P) = 2,326,224,668,061,435,376,435,200,000`,

as they must because every linear extension satisfies exactly one of `x<B`, `B<x`.

## Verification

- Two independent linear-extension DPs agree exactly: removing maximal elements from ideals, and adding minimal elements.
- Both DPs were validated against brute-force enumeration on random height-two posets up to size 8.
- A random-relabelling check reproduces the counts.
- Two independent 2-WL implementations (first-occurrence and lexicographic-rank canonicalisation) give the same stable partition.
- A full scan of all 160 nonincident point–block pairs splits them into 64 pairs of type `A` and 96 of type `B`.

Reproduction script: `/tmp/opencode/wlcount/witness.py`; full scan data: `/tmp/opencode/wlcount/pb_both.json`.

## Why the earlier n=32 witness was not enough

For all **120 point–point pairs**, including the non-isomorphic-child pairs `{0,1}` and `{0,4}` from the previous front, exact counting gives

`e(P+x<y) = e(P+y<x) = e(P)/2 = 1,163,112,334,030,717,688,217,600,000`.

So the earlier child-isomorphism counterexample does **not** refute the weaker exact-count claim. The count failure appears for the point–block pair type.

## Structural reason

For a symmetric `2-(v,k,λ)` design, an elementary induction on the paired update shows that the 2-WL signature depends only on the incidence type: point–point, block–block, incident point–block, or nonincident point–block. The design parameters determine all the required `k`-pattern counts, so the colour collapses each type to one class and is strictly coarser than the automorphism orbits.

Here translations by `G` act regularly and preserve incidence, so extension counts are constant on each translation orbit. The 160 nonincident point–block pairs form 10 translation orbits; the computed values take one type on 4 orbits (64 pairs, including `t=(0,1)`) and the other on 6 (96 pairs, including `t=(0,2)`). The 2-WL colour sees the design parameters but not the orbit.

## Soundness vs. completeness

This is a **completeness failure of the colour for the exact child-extension-count statistic**. It strengthens the n=32 child-isomorphism obstruction: the numerical leaf-count invariant is also not a 2-WL invariant.

It is **not** a `T`/`F` collision, and it does not prove that every colour-based pruning scheme is unsound. A scheme using the actual child counts or additional structural information may still be sound. A colour-only scheme that assumes the exact child-count pair is determined by the colour is refuted.

Importantly, the weaker information-theoretic statistic is **not** separated by this witness: both unordered count pairs have `ceil(log₂)` pair `{86,91}`. Whether the colour determines the unordered pair of `ceil(log₂ e)` remains open. Thus a pruning certificate using only information-theoretic leaf counts is not ruled out here.

## Honest limits

- `n=32` is not claimed minimal; `n=12..31` is not settled, and the earlier n=12 scan was incomplete.
- No claim is made about `T`, `F`, or the minimax move quotient.
- No `S(n)` bound, NP certificate, or complexity-class separation follows.
- The counterexample is exact machine computation, not Lean-formalised.
- General-poset context only: 2-WL is incomplete in general (Cai–Fürer–Immerman), and exact `e(P)` is `#P`-complete in general (Brightwell–Winkler). The new point is that the obstruction is realised inside the root-relevant height-two incidence family, not merely for arbitrary posets.

## Output 594 (msg_1c22a8661001ZULvTQ1jKjdHLN)

Recovery inspection completed on `billy-dev`; no duplicate external actions taken.

**Effects that actually happened**

- **Board #301:** exactly one matching comment exists, by `SoringP1 frontier: two-wl-child-extension-count-soundness`, timestamp `2026-11-09T21:11:47.002Z`. I searched board pages 1–5; there is no duplicate post.
- **Git:** worktree clean at `6a96398`; no new commits, branches, or repository changes from this session.
- **Scratch artifacts:** `/tmp/opencode/wlcount/witness.py`, `/tmp/opencode/wlcount/pb_both.json`, and `/tmp/opencode/wlcount/board_post.md` are present.
- **No Lean changes**, no tests, no commits, no additional purchases or external actions.

**Unfinished / uncertain operational state**

The durable ledger entry for `two-wl-child-extension-count-soundness` still has `status: running` (agent id `VnzbFEgglvaBjpWItcUCtm-stature`). That is expected until the keeper observes the agent’s `clearexit` and transitions it to `investigated` or `blocked` (`scripts/research_frontier.py`, the `status='investigated' if s=='clearexit' else 'blocked'` branch). I did **not** edit the ledger manually, because guessing the transition would conflict with the keeper’s durable claim/exit protocol.

**Bottom line**

The mathematical work and its board report are already complete. The posted result stands: the all-`n` exact child-extension-count claim is false, with the explicit height-two `n=32` biplane counterexample and independently verified exact counts. The only outstanding item is the ledger’s keeper-owned status transition, which should be reviewed or left to the keeper rather than duplicated or guessed.
