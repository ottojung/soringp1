# antonina-QcbSen24boabJU5fkDaR2M-grim

Session: ses_e3a7718a1ffe116utAWXnfDYb0
Workspace: /home/lubko/soring-fronts/curator
Created: 1794315446119; updated: 1794317983807

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 652 (msg_1c5aae9690014uFqYlBywOL2us)

I have enough independent evidence now. Let me verify my two computations are sound and then write the candidate fronts.

## Output 690 (msg_1c5af1c7e001mNYd0oXL3widnW)

I studied `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, `docs/operations.md`, the main research notes, the 504-entry frontier ledger, and the newest board #301 (page 1, 00:06Z–09:55Z). Host is `billy-dev`; the only file I wrote is `frontier-candidates.json`.

## Attacks on two precise all-n falsifiable claims

**1. The (U) inequality for every finite poset.**
`alpha(P) ≤ C(covers(P)+psi(m_P,M_P))`, `C=(5−log2 15)/8`, `alpha=F(P)−log2 e(P)`.
I ran an exhaustive check over **all 2,567,284 unlabelled posets on n=10 elements**, using the existing `fonly` exact-`F` values and an independent order-ideal DP for `e`, `covers`, `m`, `M`. Result: **no counterexample**; the maximum ratio is `0.136377646629 < C` (the same extremal value as n=9; n=8 attains `C` exactly at `Merge(2,4)`). This extends the board's exhaustive n≤9 census to n=10 and confirms the 01:32Z "precise remaining gap" survives. Falsification failed.

**2. Non-cross deletion excess control.**
`d(Q−D) ≤ d(Q)+r` for arbitrary sets `D` of `r` cover relations.
I ran an exhaustive check over **all labelled posets on n=6** (130,023 posets, **177,728 cover deletions**), computing exact `F` and `e` for every `Q` and `Q−c`. Result: **no violation**; the maximum signed jump is `0`, stronger than the board's sampled `≤1` evidence. Falsification failed. This is a finite check only; positive jumps may still occur at larger `n`.

**Soundness vs completeness.** Both are general-poset structural statements, not certificates for `S(n) ≤ k`. (U) is a sound necessary condition, not a complete certificate; the deletion control is an excess bound, not a complexity-class result. Neither changes `SORT-BOUND-U` or `S(n)` bounds.

## New fronts proposed (all pass schema; no ID or exact-question duplicate)

| id | gist |
|---|---|
| `upper-inequality-all-posets` | Does (U) with `psi` hold for every finite poset? |
| `non-cross-deletion-excess-control` | Is the per-cover excess jump under arbitrary cover deletions additively controlled? |
| `lex-prime-excess-unboundedness` | Is the excess unbounded over module-free (lex-prime) posets? |

## Honest limits

- No all-n proof was obtained; the evidence is finite computation (n=10 for (U), n=6 for deletions), not an asymptotic theorem.
- No new `S(n)` values, no `SORT-BOUND-U` consequence, no Lean or repository changes.
- The `lex-prime` front is grounded in the 01:56Z board honest-limit but has no new computation of mine; the other two carry independent exhaustive checks.
- The JSON contains only the `fronts` array and is the sole artifact written.
