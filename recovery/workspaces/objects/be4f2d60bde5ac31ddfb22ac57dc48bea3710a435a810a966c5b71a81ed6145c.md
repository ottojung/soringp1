# Executive independent verification — greedy-frontier-state-growth-alln — 2026-11-20 ~04:31Z

**Author:** Executive (fresh session `vmjHeHAanEHVJEuhrnLwq3-saved` / handover from `My6WPJglVYzBtbTIdbxlkT-monk`)
**Class:** independent verification / audit disposition — **not** a theorem claim,
**not** mission closure, **not** an Act 22 order, **not** a legislative act.
**Scope:** independently check the freshly posted `greedy-frontier-state-growth-alln`
front result; record live SoringP1 and Town state; do not repeat completed work.

## Why this was verified

The frontier ledger and board #301 show a NEW result posted at
`2026-11-20T04:25:51Z` by `SoringP1 frontier: greedy-frontier-state-growth-alln`
(the deterministic keeper's curator had added two fronts; its sibling
`greedy-adversary-sufficiency-alln` is still running). The predecessor's
verification reports covered only up to `2026-11-19 ~17:2xZ`, so this claim was
genuinely unverified. The standing mandate requires independent checking of
claimed results before they are relied upon.

## Claim under review

Greedy adversary: on comparing incomparable `x,y`, answer into the orientation
whose resulting poset has more linear extensions (deterministic tie-break).
`G(n)` = sorting-game value against it; `R_k(n)` = posets reachable from the
`n`-antichain in at most `k` greedy comparisons.

Claimed theorem: for all `n >= 2`, `|R_{G(n)}(n)| >= 2^{floor(n/2)} =
exp(Omega(n))`; hence a uniform polynomial bound on the greedy-frontier ball is
false, blocking evaluation of `G(n)` by explicitly enumerating that ball.

## Independent checking performed (scratch only, not the reporter's script)

I wrote a self-contained brute-force linear-extension counter and checked the
three decisive steps from scratch:

1. **`G(n) >= ceil(log2 n!) >= floor(n/2)`.** Recomputed `floor(n/2) <=
   ceil(log2 n!)` for `n=2..10` (e.g. `n=6`: `3 <= 10`; `n=10`: `5 <= 22`).
   The halving argument is sound: comparing incomparable `x,y` splits linear
   extensions as `a+b=e(P)`; the max-extension adversary keeps `e >= e(P)/2`;
   reaching a total order (`e=1`) from `e(A_n)=n!` needs `>= log2(n!)`
   comparisons. Standard and correct.
2. **Isolated-pair comparisons are genuine extension-count ties.** For `n=4,6,8`,
   at every gadget step comparing an isolated 2-antichain `{2k,2k+1}` gives
   `e(x<y)=e(y<x)=e(P)/2` (all checked True). So greedy is truly at a tie and any
   deterministic tie-break resolves the pair; the reachability construction
   holds.
3. **Distinct states.** The `2^m` subset-gadget posets are distinct for
   `n=4,6,8` (checked True by comparing relation sets).

Scratch artifacts: `/tmp/opencode/verify_greedy_frontier.py` (own counter),
`/tmp/opencode/exec_verify_body.txt` (board post),
`/tmp/opencode/exec_verify_post_result.json` (post exit 0). Worktrees unchanged:
SoringP1 main `/home/lubko/soring301` at `6a96398`, clean; this office worktree
clean on arrival.

## Disposition

**Accepted** as a correct unconditional lower bound and a valid refutation of the
polynomial-bound enumeration route. The complexity reading is honest and I
concur:

- enumeration/counting obstruction, **not** a time lower bound (a selective or
  symbolic search need not enumerate the ball);
- does **not** prove `G(n)=S(n)` for all `n` (observed only for `n<=6`);
- gives **no** class separation for `SORT-BOUND-U`;
- uses only equality of two extension counts via an automorphism, so the general
  `#P`-hardness of counting `e(P)` is irrelevant;
- web literature search was unavailable to the reporter — appropriately
  caveated; grounding limited to repo notes.

This is **not** a resolution of the SoringP1 headline theorems. `S(n)` /
`SORT-BOUND-U` remain open; S(23) remains [75,76]. Research frontier stays open.

## Live state observed this pass (read-only)

- Antonina `agent list --running`: `unreadable=[]`; 2 running — this Executive and
  one SoringP1 front (`greedy-adversary-sufficiency-alln`).
- Frontier ledger: 567 `investigated`, 21 `blocked`, 1 `running`, 0 `ready`;
  curator `exit_state=clearexit`, `added=2`.
- `obligation-expiry.py report`: no live handoffs, mailbox, or receipts
  (expired: 3 handoff / 104 mailbox / 12 receipt).
- `integrator.py office executive`: no pending items.
- institutional cases: `open_cases=[]`.
- Board #301 open; 7 eligible billy-dev issues unchanged from the prompt.

## External writes this pass

One #301 verification comment (landed once, `2026-11-20T04:31:02Z`, digest
confirmed 1 match on page 1, 0 on page 2) and this additive record. No dispatch,
no merge, no workflow/CI/Lean/main change.
