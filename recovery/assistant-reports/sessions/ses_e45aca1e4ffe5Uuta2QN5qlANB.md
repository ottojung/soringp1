# antonina-vOgvOvT2G1AdUAKos7ua0v-manners

Session: ses_e45aca1e4ffe5Uuta2QN5qlANB
Workspace: /home/lubko/soring-fronts/height-two-minimax-exact-complexity
Created: 1794127388221; updated: 1794128611860

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 607 (msg_1ba654b230016kcT82hxZlsWxr)

## Recovery check (effects reconciled)

- On `billy-dev` only; worktree clean at `6a96398`, no commits, stashes, or Lean changes.
- The durable ledger contained the front `height-two-minimax-exact-complexity` as `running` under agent `vOgvOvT2G1AdUAKos7ua0v-manners`, with **no recorded finding**.
- Board #301 had **no** prior height-two post. I therefore completed the unfinished research/board step exactly once. The new comment is at `2026-11-08T09:02:31Z`, author `SoringP1 frontier: height-two-minimax-exact-complexity`.
- The ledger still shows the front `running`; I did not hand-edit durable operational state. If the named live agent posts separately, that is a possible race to review, not something I duplicated deliberately.

## Mathematical finding

**1. The “in particular” one-edge family is exactly `S(n)`, not a weaker intermediate.**

Let `P_n = ({0<1} ⊔ A_{n-2})`. Every first comparison from the antichain gives a state isomorphic to `P_n`, so

\[
S(n)=1+F(P_n)\qquad\text{for every }n.
\]

Thus a polynomial-time algorithm for height-two `F` on just this subfamily is equivalent to `SORT-BOUND-U ∈ P`; an unconditional negative result there would prove `P ≠ PSPACE`. The one-edge part therefore cannot be falsified by a #P-hardness construction without a major separation.

**2. A second exact height-two subfamily already contains `S`.**

For `K_{m,m}=A_m \oplus A_m`, all cross pairs are known, so the game splits into two independent antichain games:

\[
F(K_{m,m})=2S(m)
\]

for all `m` (checked exactly for `m=1..4`: `0,2,6,10`).

**3. Concrete obstruction: `F` is not determined by `(n,e(P))` on height two.**

On `n=6`, both height two:

- `P = {0<2, 0<3, 0<5, 1<2, 1<3, 1<4}`: `e(P)=60`, `F(P)=6`.
- `Q = {0<4, 0<5, 1<4, 1<5, 2<3}`: `e(Q)=60`, `F(Q)=7`.

`e` by exhaustive `6!` permutation count, `F` by exact minimax; two independent implementations agree (`/tmp/opencode/verify_pair.py`). No such collision exists for height-two posets on `n≤5`; at `n=6` the other class is `e=120` with `F∈{7,8}`.

Hence **no function of `n` and `e(P)` computes `F`**. No extension threshold `e(P)≤T(k)` can *characterize* `F≤k` on height two: at `k=6`, `T(6)≥60` makes `Q` unsound, while `T(6)<60` fails to certify `P`. A threshold may remain a sound sufficient condition; it cannot be complete. This is the soundness/completeness gap concretely.

**4. Literature and terminology correction.**

- `#H2LE` is `#P`-complete, even for incidence posets of graphs (Dittmer–Pak, arXiv:1802.06312v1, Theorems 1.1–1.2). But by (3), counting hardness does **not** transfer to `F` through `e`, since `e(P)=e(Q)` with `F(P)≠F(Q)`.
- The Fibonacci “staircase” `W_n` cited with the width-two threshold is **width two, not height two**: `i` above `j` iff `j≤i−2` is a disjoint union of the even/odd chains, with height `≈n/2`. The height-two staircase from `docs/research-time-exponent.md` has `e=1,5,57,1145` and `F=0,3,7,11` for `m=1..4`, not Fibonacci. Width-two GPC/threshold evidence is therefore not height-two evidence.

## Failed approaches and honest limits

- Attempted a `#H2LE → F` reduction via extension thresholds; blocked by the `n=6` collision.
- Attempted to extend the collision to an infinite family by disjoint union with chains; exact minimax at `n=8` exceeded the time budget, so no all-`n` claim.
- No polynomial algorithm for all height-two `F`, no proof that none exists, and no new claim about `S(n)` beyond the identities above.
- No Lean or repository changes; the worktree remains clean at `6a96398`.

**Next decisive target:** a height-two family whose exact `F` (or decision `F≤k`) encodes a #P-/PP-hard parameter *not* reducible to `e`, or a two-way reduction showing all-height-two `F` is equivalent to `S(n)`.

## Output 670 (msg_1ba65f2e4001Wc31dKKwQRdNOA)

## Recovery inspection result

I inspected the conversation, Git/worktree, board, and durable ledger before acting.

**Effects that actually happened (previous turn):**
- Exactly **one** board #301 comment was posted, at `2026-11-08T09:02:31Z`, author `SoringP1 frontier: height-two-minimax-exact-complexity`. I re-read it from the board and confirmed its stored body matches the prepared text (only a trailing newline was stripped).
- **No repository changes:** worktree clean at `6a96398`; no new commit, branch, stash, or Lean file.
- Verification artifacts remain outside the repo in `/tmp/opencode/` (`verify_pair.py`, `height-two-post.md`).

**Unfinished / uncertain items:**
- The durable ledger still records the front as `status: running` under agent `vOgvOvT2G1AdUAKos7ua0v-manners`, with no recorded finding or exit state. That is keeper/ledger reconciliation state, not a missing research result. I did not hand-edit operational state, to avoid a duplicate or conflicting record.
- No second height-two post exists, so I did **not** repost or repeat any external action.

**Research outcome already delivered:**
- `S(n) = 1 + F(P_n)` for the one-edge height-two family `P_n`, making that subfamily exactly equivalent to the `SORT-BOUND-U` target.
- `F(K_{m,m}) = 2S(m)`.
- Concrete height-two collision: at `n=6`, two posets both with `e=60` but `F=6` and `F=7`, blocking any extension-count threshold as an exact evaluator.
- Correction that the Fibonacci staircase `W_n` is width two, not height two.
- No poly-time algorithm, no #P-hardness proof, no complexity-class separation claimed.

No further side effects were performed. The only remaining action is operational recording of the completed front by the keeper; that record is currently still `running` and should be reconciled there rather than duplicated manually.
