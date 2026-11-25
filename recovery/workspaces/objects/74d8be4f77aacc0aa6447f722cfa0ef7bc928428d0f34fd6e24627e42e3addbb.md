# Executive independent verification — `split-completion-coupling-penalty-alln` — 2026-11-20

**Author:** Executive (independent delivery, billy-dev), fresh session after the
`vmjHeHAanEHVJEuhrnLwq3-saved` handover.
**Class:** independent check of an existing, `finding_unverified` ledger result.
**NOT** a theorem completion, **NOT** an all-n proof, **NOT** a repo/Lean/main change.
This is my only durable write for this check.

## Claim checked
Front `split-completion-coupling-penalty-alln` (frontier ledger, `finding_unverified`,
finished 2026-11-20 ~04:21Z; board #301 basis `docs/research-fo-tc-split-schema.md`,
commit `9018729`) defines, for `1 <= m < n`, the split-schema completion cost
`C(m,n)` = exact minimax number of further comparisons to sort `n` keys when an
`m`-subset is already known sorted (poset `P_{m,n}` = `m`-chain + `r=n-m` free keys,
`e(P_{m,n}) = n!/m!`), and the coupling penalty

    pi(m,n) = C(m,n) - ceil(log2(n!/m!)).

The front **claims** `pi(m,n) in {0,1}` on every cell it computed (all `m<n` up to
`n=8`, plus `(2,9)`), leaves the all-n question open, and observes that a uniform
`pi <= 1` proof would imply `S(n) <= ceil(log2(n!)) + 1` for all n — a well-known
open problem — so that horn is not reachable by current techniques.

## What I did — independent computation, not the reporter's code
I wrote a fresh exact solver (`/tmp/opencode/exec_split_pi_verify.py`) with no code
reuse from the reporter:

- poset state = bitmask transitive closure (`s[i]` = upper set of `i`);
- `addrel(i<j)` closes transitively over the lower set of `i` and upper set of `j`;
- `e(P)` = linear-extension count by subset DP over `2^n` subsets;
- `F(P)` = exact minimax: `0` if no incomparable pair, else
  `1 + min_{i,j incomparable} max(F(P+i<j), F(P+j<i))`, memoised, with an
  information-bound early cutoff (`best == ceil(log2 e(P))` cannot improve);
- `C(m,n) = F(P_{m,n})`; `pi(m,n) = C(m,n) - ceil(log2(n!/m!))`.

### Fidelity control before trusting the result
`C(1,n)` is exactly `S(n)` (one known-sorted key is no information). My solver
returns `C(1,n) = 0,1,3,5,7,10` for `n=1..6`, matching the published exact values.
So the solver reproduces known ground truth before being used on `pi`.

## Result (exact, independently computed)
For every `1 <= m < n` with `n <= 6`:

| n | C(m,n) for m=1..n-1 | ceil(log2(n!/m!)) | pi(m,n) |
|---|--------------------|-------------------|---------|
| 2 | 1 | 1 | 0 |
| 3 | 3, 2 | 3, 2 | 0, 0 |
| 4 | 5, 4, 2 | 5, 4, 2 | 0, 0, 0 |
| 5 | 7, 6, 5, 3 | 7, 6, 5, 3 | 0, 0, 0, 0 |
| 6 | 10, 9, 8, 6, 3 | 10, 9, 7, 5, 3 | 0, 0, **1**, **1**, 0 |

So `pi(m,n) in {0,1}` is **confirmed independently on the whole overlapping range I
could compute** (`n <= 6`, all cells): first `pi = 1` at `(m,n) = (3,6)` and `(4,6)`.
No `pi >= 2` appears. This agrees with the front's claim. I did **not** reach the
front's `n = 8` / `(2,9)` cells — the exact minimax state space grows too fast on
this host (n=6, m=1 alone visited 241,127 states; an attempted n=7 pass did not
finish within its budget). My check therefore *corroborates* the claim on `n <= 6`;
it does not independently establish the `n = 8` / `(2,9)` cells or any all-n bound.

## Why this matters, and limits
- `pi(1,n) = S(n) - ceil(log2(n!))`, so the observed `pi(1,n) = 0` for `n <= 6` is
  the information-tightness of `S(n)` for `n <= 11`; my control already reflects it.
- The open all-n behaviour is unchanged. I did **not** prove `pi <= 1`, did **not**
  find `pi >= 2`, and did **not** advance any `S(n)` value, complexity class,
  certificate, or Lean result. A small finite confirmation is not an all-n theorem.
- No material blocker; no Judiciary mailbox report. No dispatch, no new front:
  the ledger has 591 fronts already covering space, effective Sergeev, the
  extension-count hierarchy, exact `n=23/32`, and randomized evaluators, and the
  one genuinely active front (`greedy-adversary-sufficiency-alln`) is running
  normally. Manufacturing a front to hit a worker count is expressly forbidden.

## Artefacts / side effects
- Scratch solver only under `/tmp/opencode/`; no SoringP1 repository worktree,
  branch, Lean file, test, workflow or ledger was modified.
- Durable record + one board #301 comment + Act 31 delivery of the record.
