# antonina-xKvC2sPn65uCQWiGxklucY-poisoning

Session: ses_e45479fe9ffeCWt4I1c4b4co0K
Workspace: /home/lubko/soring-fronts/split-merge-rounding-slack-alln
Created: 1794134007927; updated: 1794140378595

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1bab862160011V9yTV172DjMC1)

I'll start by reading the required documents and the current #301 discussion.

## Output 821 (msg_1bb187a4d001eSX7KneS7F7uM3)

I posted exactly one finding to Antonina #301 as `SoringP1 frontier: split-merge-rounding-slack-alln` (2026-11-08T12:18:12Z). The worktree is clean; no repo commits, Lean changes, or workflow edits.

## What was achieved

**Deliverable (3), plus an exact certification that resolves the prior uncertainty.**

I did **not** prove the linear-slack lemma (1), and I did **not** falsify it (2). The exact computation **agrees** with the prior disputed value, so it is a positive reproduction rather than a counterexample.

### 1. Exact certification [exact computation]
Reimplemented `L(n)=min_{a+b=n}[L(a)+L(b)+ceil(log2 C(n,a))]` with Kahan log2 factorials and an exact integer repair pass: every `log2 C(n,a)` within `1e-7` of an integer was recomputed via `math.comb`/`bit_length`. Up to `n=175000`: 2921 flagged pairs, **0 ceiling changes**. Exact tree costs (sum of exact bit lengths along the DP-optimal tree) match the DP value at every target.

| k | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
|---|---|---|---|---|---|---|---|---|---|---|
| `n_k` | 341 | 682 | 1365 | 2730 | 5461 | 10922 | 21845 | 43690 | 87381 | 174762 |
| `L` | 2414 | 5504 | 12372 | 27462 | 60375 | **131640** | 285080 | 613748 | 1314703 | 2803815 |
| `FJ` | 2392 | 5461 | 12291 | 27306 | 60078 | 131071 | 283993 | 611668 | 1310724 | 2796201 |
| `L-FJ` | 22 | 43 | 81 | 156 | 297 | **569** | 1087 | 2080 | 3979 | 7614 |

So `L(10922)=131640` and `R(10922)-S(10922)>=569` stand independently. `k=14..17` are new.

### 2. Structural obstruction [deduction]
For any full binary tree with `n` unit leaves, the binomials multiply exactly to `n!`. With `o_v` the odd part,
`m(n)=Σ_v [ceil(log2 o_v)-log2 o_v]`, `Π_v o_v = oddpart(n!)`.
Zero cost occurs exactly when `C(s_v,a_v)` is a power of 2; by Sylvester–Schur this happens only for a power-of-2 cherry (`a_v=1` or `b_v=1`, `s_v` a power of 2). In the optimal tree at `n=87381`, **36.8%** of nodes are such zero-cost cherries. Any linear lower bound must come entirely from the nonzero nodes.

### 3. Weakest missing inequality [deduction]
Since `FJ-I ~ 0.02766 n_k`, unboundedness reduces to
`(W) limsup_k m(n_k)/n_k > 0.02766`,
strictly weaker than `m(n_k)>=c n_k`. Equivalently, one needs a lower bound on the total nonzero rounding. No known theorem gives this: the only general bound is `r_v >= 1/(2 C_v ln2)`, exponentially small, and near-powers (`C=2^t-1`) make individual terms as small as `2^{-t}`.

### 4. Why natural proofs fail [deduction]
- `n log2 n - Cn + O(log n)` fails at the `a=1` split, forcing `C>=1/ln2=1.442695`, above FJ’s coefficient range.
- `αn-βn^p` works only for `p<1`; `p=1` is killed by `m(1)=0`.
- A periodic correction is killed at the zero-cost split `2^k -> 1+(2^k-1)`.
- A power-law ansatz `m~C n^p`, `p<1`, is not self-consistent because `(a/n)^p+(b/n)^p>1` for every split.

### 5. Numerical warning [experiment]
`m(n)/n` at `n=2^k`, `k=10..17`: `0.08496, 0.08292, 0.08031, 0.07809, 0.07592, 0.07380, 0.07180, 0.06988`. A naive fit is `m~n^0.959`, but by §4 that fit must break. Any uniform linear bound valid at `n=131072` has `c<=0.069878`, so the admissible window is `[0.02766, 0.06988]`. The finite spike is real, but unboundedness is not established.

**Bottom line:** the prior finite certificate is now independently certified and extended; the load-bearing all-n lemma is reduced to the precise inequality `(W)` and blocked by the simultaneous near-power problem for binomial coefficients.

## Output 895 (msg_1bb19786f001JKUkqU5Oe2EWFp)

Inspection complete. No duplicate action was taken.

## Verified state

- **Antonina #301:** exactly **one** message exists by `SoringP1 frontier: split-merge-rounding-slack-alln`, timestamp `2026-11-08T12:18:12.530Z`, body length 4721. No duplicate of the finding was posted.
- **Git:** worktree clean (`git status --porcelain` empty), HEAD `f89f6d0`. No commits, Lean changes, or workflow edits were made.
- **Durable ledger:** `~/.local/state/soringp1/frontier-ledger.json` exists but has **no entry under the exact ID** `split-merge-rounding-slack-alln`. The board message is the authoritative completed side effect; the ledger absence is an operational bookkeeping gap, not an action I should silently repair given the original “no workflow edits” constraint. Flagging it for review rather than editing it.
- **Local artifacts:** experiment scripts/outputs remain only under `/tmp/opencode/splitmerge`; nothing was added to the repo.

## Unfinished work

None. The requested single finding (exact certification of `L(10922)=131640`, extension to `k=17`, odd-part/zero-cost obstruction, reduction to `limsup m(n_k)/n_k > 0.02766`) was already posted once. I have not reposted it or repeated the interrupted computation.
