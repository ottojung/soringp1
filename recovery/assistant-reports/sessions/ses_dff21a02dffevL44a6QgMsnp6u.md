# antonina-qfKTh4Jrm6ftE3CZUEDUjl-juice

Session: ses_dff21a02dffevL44a6QgMsnp6u
Workspace: /home/lubko/soring-fronts/winning-frontier-peak-at-exact-budget-alln
Created: 1795310903365; updated: 1795311927068

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_200de680a0015YuJ0VRwLmzp8u)

I'll start by checking the environment (hostname for billy-dev) and reading the key docs.

## Output 25 (msg_200df83d4001t6Piwr4CeHjLFm)

On billy-dev confirmed. Now let me look at the docs directory, find the board and the winning-frontier barrier notes.

## Output 40 (msg_200df939e001wVtqKgEsZ9a9E4)

Now reading the operations doc (board #301), the winning-frontier barrier doc, literature, and the frontier state.

## Output 71 (msg_200e42d5d0012PA2iJbA7H0aCP)

Continuing after the restart — I have the definitions now. Let me check the barrier's certified integers, the board tooling, and the board digest, then write a brute-force W_t(n) checker.

## Output 90 (msg_200e63346001dYtlANLPP4ewFc)

Board digest is readable. Now I'll write the independent brute-force checker for W_t(n) per the user's definition, and check how board posts are done.

## Output 114 (msg_200e75e98001OSc9BqE0ZPFar7)

Bug in my script: I wrote `n*(n-1)` for the total-order check; a total order on n elements has `n*(n-1)//2` pairs. Fixing.

## Output 143 (msg_200e7b5a1001v4ngu2rECowkis)

The F-DP itself looks right (S(3)=3). The IndexError is in the reachable-depth BFS — let me debug it interactively.

## Output 154 (msg_200e8461b001m6z1R1R4NqGubN)

Found it: `R = [frozenset()]` makes `R[0]` the empty antichain itself; iterating it yields nothing. It must be `R = [{frozenset()}]` (a set containing the antichain).

## Output 172 (msg_200e8a211001FWdMcZh0I9lXaZ)

The brute force ran, but W_1=6 for n=3 is suspicious — all six one-edge posets should be isomorphic under my definition of isomorphism (relabeled posets). Let me debug `canon`.

## Output 183 (msg_200e8f409001DRwg95zBpwxNvE)

`canon` uses `<` on frozensets, which is subset comparison, not a lexicographic minimum — so isomorphic posets weren't identified. Fixing it to take the minimum by `sorted` key.

## Output 201 (msg_200e9acbe0017jcq91WzedYPw1)

The brute force now gives clean results. Before reporting, let me check the Antonina CLI for how to post a board update (per the repo contract findings go to board #301), and confirm no repo changes were made.

## Output 216 (msg_200ea334b001g4t6Y9aiQLBY5j)

Repo is clean (no changes). Now let me check how to post a board comment and search issue #301 for prior posts on this question before posting the finding.

## Output 231 (msg_200eaddd7001xKyB7Pp4NtpnTe)

The board show needs `--page`. Let me retry the search with pagination.

## Output 242 (msg_200eb0b85001xWaVVMolXIRCfz)

No prior post on this exact question visible so far. Let me list the recent message titles to double-check, then post the finding.

## Output 253 (msg_200eb3e83001gGjcpO7DPa0p7t)

Board posted findings go to #301 via `antonina board comment`. Posting the finding now (author matches the digest's convention for researcher findings).

## Output 273 (msg_200ec2fca001pvDRTZDaVhZ0mk)

The comment may not have landed (still 50 messages, newest from 11-21). Let me check exit status and search the board for the posted title.

## Output 293 (msg_200ecd596001IMKp7w8G1I78ZO)

The finding is posted to board #301 (two identical copies; the digest dedups). Here is the report.

## Finding: the claim is REFUTED — the winning frontier does not always peak at the exact budget

**Claim attacked (restated):** for every n, `max_t W_t(n)` is attained at `t = S(n)`, where
`W_t(n)` = number of pairwise nonisomorphic posets P that are *reachable by exactly t legal comparison outcomes* from the n-antichain and satisfy `F(P) ≤ S(n) − t` ("winning at remaining budget"). Interpretation per `docs/research-winning-frontier-barrier.md` ("reachable from the n-antichain by exactly t legal comparison outcomes"); `F` is the minimax remaining comparison count, model as in `docs/problem.md`.

**Structural fact (deduction):** `W_{S(n)}(n) = 1` for every n — the only reachable depth-`S(n)` posets with `F ≤ 0` are total orders, and all total orders on n labelled elements are isomorphic. So the claim ⇔ "no depth has ≥ 2 winning reachable posets".

**Independent brute force** (`/tmp/opencode/w_t_check.py`, DP over all labelled posets; scratch only, repo untouched):

| n | S(n) | W_t (t=0..) | peak |
|---|------|-------------|------|
| 3 | 3 | [1, 1, 3, 1] | 3 at t=2 ≠ 3 |
| 4 | 5 | [1, 1, 4, 6, 4, 1, 0] | 6 at t=3 ≠ 5 |
| 5 | 7 | [1, 1, 2, 6, 17, 11, 5, 1, 0, 0, 0] | 17 at t=4 ≠ 7 |

In every case `W_{S(n)} = 1` and the peak is strictly below — the claim already fails at n=3.

**Infinite family (from the repo's barrier, exact integer checks recomputed in the script):** `docs/research-winning-frontier-barrier.md` gives the rectangular-chain construction for `n = s·L` with `s = L = 2^r` (family `n = 4^r`): at depth `t = k − B` it puts ≥ 2 nonisomorphic winning reachable posets with `F(P) ≤ B`, and `t ≤ k − 1 < k ≤ S(n)` by the information bound `S(n) ≥ ceil(log2(n!)) = k`. Verified exactly:
- n=224 (witness): `binom(3120,316) > 2^39 · 224!` → `W_524(224) ≥ 2^39`
- n=256: `binom(3600,409) > 2^148 · 256!` → `W_649(256) ≥ 2^148`
- family: n=1024 (r=5, depth 3624) and n=4096 (r=6, depth 18618): ≥ 2 classes at depth `k−B`, both < k ≤ S(n).

So `max_t W_t(n) ≥ 2 > 1 = W_{S(n)}` for infinitely many n — the frontier peaks at depth `k−B`, far below the exact budget.

**Soundness vs completeness:** the barrier is a *soundness* result — its constructed states are genuinely winning (`F(P_A) ≤ B` by construction; integer certs hold; per the doc, "genuinely *winning*, not merely allowed"). The refuted claim is the *completeness-type* statement about where the frontier peaks — false. Per `AGENTS.md`, hardness results about arbitrary partial orders do not transfer to the fixed family `S(n)`; this is about the location of winning states, not hardness.

**Complexity implication (per your framing):** since the frontier does not peak at the exact budget, exact-budget state counts are **not** load-bearing for this barrier; there is an earlier-peak family where the winning set is huge at depth `k−B` with remaining budget `B` — consistent with lower-depth-first search strategies.

**Honest limits:**
- Brute force covers only n ≤ 5 (state spaces explode; n=5 has 3010 reachable posets at depth 10).
- The family's integer certificates are recomputed, but the barrier theorem is not re-derived here; the doc calls it paper-level. r=3 (n=64) yields < 2 classes in the finite check, so the infinite family starts at r ≥ 4.
- Your margin variant (`W_{S(n_i)−1}/W_{t_i} < 1/2` for arbitrarily large n) was not computed; the essential falsifier (peak strictly below `S(n)`, `W_{S(n)}=1`) holds.

**Process:** no Lean/repo changes (`git status` clean). Board finding posted to #301 (`SoringP1 researcher: frontier-peak-at-exact-budget-refuted`).
