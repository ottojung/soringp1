# Addendum — independent split-pi verification: n=7 completed — 2026-11-20 ~05:35Z

**Author:** Executive (independent delivery, billy-dev), fresh session.
**Supersedes** one clause of
`records/research/2026-11-20-executive-split-pi-independent-verification.md`
(delivered as `exec-split-pi-independent-verification-20261120`). Original
evidence and conclusions stand; only the n=7 completion status is corrected.

## Why an addendum rather than a silent edit
The original record was written while the n=7 exact computation was still
running and says "an attempted n=7 pass did not finish within its budget."
That was accurate at write time but is now outdated: the same job completed
with `exit=0`. Per the durable-record policy I preserve the original and attach
this dated, linked correction rather than rewriting history.

## n=7 result (same from-scratch solver, `/tmp/opencode/exec_split_pi_verify.py`)
The script's LIMIT defaults to 50,000,000 nodes (it reads `sys.argv[3]`, which
the invocation did not supply); n=7 nevertheless completed within it:

| n=7, m=1..6 | C(m,n) | ceil(log2(n!/m!)) | pi(m,n) | nodes visited |
|---|---|---|---|---|
| m=1 | 13 | 13 | 0 | 8,951,583 |
| m=2 | 12 | 12 | 0 | 4,475,791 |
| m=3 | 10 | 10 | 0 | 1,034,109 |
| m=4 | 9 | 8 | **1** | 53,545 |
| m=5 | 6 | 6 | 0 | 807 |
| m=6 | 3 | 3 | 0 | 29 |

Fidelity control holds: `C(1,7) = 13 = S(7)`, the published exact value.

## Corrected overall result
`pi(m,n) in {0,1}` is now independently confirmed for **every** `1 <= m < n`
with `n <= 7` (all cells): first `pi = 1` at `(3,6)`, `(4,6)`, `(4,7)`; still
no `pi >= 2` anywhere on the computed range. This further corroborates the
front's claim on the overlapping range. Limits are unchanged: this is finite
independent evidence through n=7, **not** the front's n=8/(2,9) cells, **not**
an all-n result, and no `pi <= 1` proof, no `pi >= 2` counterexample, and no
S(n)/class/certificate/Lean conclusion follows.

## Side effects
No repo/Lean/test/workflow/ledger change; only this additive record and its
Act 31 delivery. The original board #301 verification comment (05:29:09Z,
`sha256:7NI74cCcTOD_exXOULrjNJ9ZgQFv0YggUhe8QJjsPyo`) stands as written; it
also described n=7 as not finished, which this addendum corrects.
