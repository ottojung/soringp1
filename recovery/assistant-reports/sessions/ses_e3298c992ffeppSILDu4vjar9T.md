# antonina-8lq6zFsW9w3QwxvqLXY8tZ-takes

Session: ses_e3298c992ffeppSILDu4vjar9T
Workspace: /home/lubko/soring-fronts/optimal-certificate-root-forcing-20261112
Created: 1794447455894; updated: 1794456586141

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 168 (msg_1cdf1dd7e001MYGhnwxrzsqP5Y)

**Recovery inspection (no external actions repeated)**
- Git: `HEAD` detached at `6a96398` (`git status --short --branch` clean). No repo/Lean changes, commits, or PRs found.
- Frontier/board: `~/.local/state/soringp1/frontier-ledger.json` has no `antichain-reachable-abc-tree-completeness` front; local `board_digest.py --recent 10` excerpts show no post by that id/title. I cannot definitively prove absence on Antonina #301 itself from this environment, so any prior external posting of this exact front remains **uncertain** (not duplicated here).
- Durable scratch: `~/soring-scratch/antichain-abc/` contains `post.md` plus substantial artifacts (`abc.cpp`, nauty/genposet inputs/outputs, `all7..all9`, `reach7..9`, `verify*`, `path*`), consistent with a prior interrupted run. No #301 post artifact/result file found there.

**Question (restated, precise)**
- Let `A_n` be the `n`-element antichain root, `F(P)=S(P)` exact minimax height, and let a node’s comparison be *Peczarski A/B/C-certified* in the local sense used by prior #301 work: for the compared pair with extension counts `(a,b)` and at most the allowed “slaves”, A = (≤1 slave ∧ `2a>=e(P)`), B = (`2a=e(P)`), or C = a triple with `e(P+xy+yz) <= max{e(P+yx),e(P+zy)} <= e(P)/2` on that node’s first comparison. Let `H(P)` be the minimum height of a correct tree all of whose nodes are certified (`H>=F`).
- **Reachability vs forcing:** “a certificate-starved optimal state is reachable from `A_n` at optimal depth” means some optimal comparison sequence reaches `P` with `F(P)` still achievable but `H(P)>F(P)` (no certified move that is also minimax-optimal/optimal-continuable in that local tree sense). “Every height-`S(n)` root strategy encounters a starved state” (adversarial forcing) would mean `G(A_n): (H(A_n)==F(A_n))` is false, i.e. no all-certified height-`S(n)` tree exists.

**Findings from inspected durable evidence (`~/soring-scratch/antichain-abc/post.md`, unverified by me in this session but internally supported by listed artifacts/scripts/independent replay claims; treat as *prior experiment/deduction report, not re-established here*)**

| n | unlabeled posets (reported) | posets with `H>F` | `F(A_n)=S(n)` | `H(A_n)` | optimal-move-reachable states | bad among them |
|---|---:|---:|---:|---:|---:|---:|
| 7 | 2045 | 1 | 13 | 13 | 802 | 0 |
| 8 | 16999 | 52 | 16 | 16 | 5102 | 18 |
| 9 | 183231 | 839 | 19 | 19 | 33054 | 153 |

- **Mere reachability (starved states on some optimal branch): YES at `n=8,9` (decisive, finite, in that report).** Example `Q8` reached from `A_8` by optimal comparisons `(0,1),(2,3),(4,5),(1,3),(2,6),(7,1)`: `up=(10,8,72,0,32,0,0,10)` with `F(Q8)=10`, `H(Q8)=11`, `G(Q8)=false` (certified optimal root moves of `Q8` led to children with no certified optimal continuation). Analogue `Q9: up=(10,8,8,0,32,0,128,0,10)` via `(0,1),(2,3),(4,5),(6,7),(1,3),(8,1)` with `F=13,H=14,G=false`.
- **Adversarial forcing / nonexistence of an all-certified optimal tree: NO for `n<=9` in that report.** `H(A_7)=13, H(A_8)=16, H(A_9)=19` equal `S(n)`, so height-`S(n)` trees exist whose every node is A/B/C-certified for `n<=9` tested, even though some optimal branches hit starved states at `8,9`. Thus reachability does **not** imply forcing.
- **Net dichotomy answer (current evidence):** not “every height-`S(n)` root strategy necessarily encounters…” (false as a necessary property of arbitrary optimal play at `n>=8`), and not refuted as “no all-certified optimal tree can exist” (an all-certified optimal tree exists at `n<=9`); the all-`n` **existential completeness** question `G(A_n)?` remains **open**.

**Finite `n=11` falsification certificate / all-`n` invariant — tractability**
- A concrete falsifier of “all-certified optimal trees exist at 11” would be an independently checkable proof/certificate that `H(A_11)>S(11)` (or `S(11)` known and every height-`S(11)` strategy forced into a starved state). A concrete falsifier of “starvation is forceable” at 11 would be an explicit all-certified height-`S(11)` tree (nodewise A/B/C-checkable, but exponentially large to exhibit/store).
- `S(11)=29` is literature-known, but exhaustive evaluation in the same style is **not tractable/useful to invest in here now**: the prior report already states `~10 h`-scale for `n=10` (~3.24M unlabeled posets) and ~63M for `n=11`; no compact forcing invariant or succinct all-certified witness is formulated. I found no rigorous all-`n` invariant deciding `G(A_n)` and no `n=11` certificate.

**Limits / blocker (narrow)**
- I did **not** independently rerun/verify the `n<=9` exhaustive computations in this session (only inspected `post.md` and artifact presence). The decisive all-`n` obstacle is: prove for all `n` either `H(A_n)=S(n)` (construct/argue an always-certified optimal branch choice exists, despite reachable starved optimal states) or that some `n` forces `H(A_n)>S(n)` — no bridge from the `n=8,9` reachability phenomenon to forcing is known. Any use must distinguish Peczarski’s GPC/certified-move facts at small states from *minimax-optimal* certified continuations (per prior notes). No complexity-class consequence for `SORT-BOUND-U` follows. No repository/board/Lean changes made.
