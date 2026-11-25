# antonina-Bom9dOb9aoSKtc6mbhkZbO-heavily

Session: ses_e43edb0c8ffeoewSnmtPIC4eeI
Workspace: /home/lubko/soring-fronts/curator
Created: 1794156679009; updated: 1794157703397

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1bc124fcc001DwQovWRYs9E0WW)

I'll start by studying the required context and current board state.

## Output 327 (msg_1bc21b9e1001ajfAcbf2eJ7bRD)

I worked on `billy-dev` only. The curator artifact is at `/home/lubko/soring-fronts/curator/frontier-candidates.json` (4 fronts, schema-validated). No Lean, test, note, commit, or board post was created; `git status` shows only that file.

## What I studied
- `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/research-plan.md`, the certificate/Fibonacci/threshold notes, and the frontier ledger.
- Board #301 pages 1–3 (newest posts plus the GPC/Fibonacci thread, `T(9)=143`, width-two GPC verification, height-two minimax, `L_fib` PP-hardness, and the executive checks of the excess/average-depth results).

## Claim I attacked, and the result
I attacked the tempting all-`r` claim that the local information bound cannot be exactly attained:

> “For some budget `r`, no poset has exactly `e(P)=2^r` linear extensions and minimax depth `m(P)=r`.”

It is **false**, by a short paper argument: take the ordinal sum of `r` copies of the 2-element antichain. Then `e = 2^r` and `m = r` (sort each block with one comparison; `m ≥ r` from `e = 2^r`). My own exact enumeration at `n=5,6` had shown `e=32` and `e=64` only with `m=6,7`, but that was a ground-set-size artifact: the tight witnesses need `2r` elements. So local split-realizability is not the obstruction to `S(n)=C(n)`; the obstruction is global factorization/interaction of the antichain’s `n!` extensions. This is a useful **negative** result about a whole family of local lower-bound arguments.

I also checked the matching-prefix normal form by exact minimax for `n ≤ 8`: `S(n) = floor(n/2) + F(M_n)` held in every checked case. That is evidence only; it is not a proof, and the front asks for the all-`n` statement.

## Soundness vs completeness
The Gold Partition/Fibonacci threshold is a **sound** extension-count pruner (`e(P) ≤ F_{r+3}−1 ⇒ m(P) ≤ r` where GPC holds). It is **not** a complete decision rule for `SORT-BOUND-U`; the board’s height-two finding already shows no extension threshold can characterize `m(P) ≤ k`. The proposed GPC fronts are class-extension/structural questions, and their implications say so rather than claiming NP membership or completeness.

## Honest limits
- I did not prove any new theorem or find a counterexample about `S(n)` itself.
- The GPC class fronts cannot have a counterexample below 12 elements (Peczarski’s 11-element theorem), so no cheap finite falsification exists.
- The tightness-set complexity question is a partial-information question; it does not settle `S_unary ∈ FP`.
- The matching-prefix identity is open beyond the checked range; a positive answer needs a genuine strategy-normal-form argument, not enumeration.

## Proposed fronts
1. `optimal-matching-prefix-normal-form` — reduce `S(n)` to the single matching-poset family.
2. `info-tightness-set-complexity` — complexity of `{n : S(n)=ceil(log₂ n!)}`.
3. `gpc-interval-order-threshold` — GPC beyond semiorders.
4. `gpc-height-two-threshold` — GPC for height-two posets, tied to the one-comparison family with `F = S(n)−1`.
