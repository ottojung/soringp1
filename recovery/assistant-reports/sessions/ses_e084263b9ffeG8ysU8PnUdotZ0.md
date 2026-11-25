# antonina-z76w4zy9cg0nXue4EOIT99-wart

Session: ses_e084263b9ffeG8ysU8PnUdotZ0
Workspace: /home/lubko/soring-fronts/eindex-collision-transfer-minimax-alln
Created: 1795157761178; updated: 1795159359767

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f7bd9ea3001CZ4A6OHySQKCUn)

I'll start by verifying the host and reading the key documents.

## Output 17 (msg_1f7bdadc8001pcs4L07LC98ZRn)

Confirmed on billy-dev. Now let me read the key documents in parallel.

## Output 36 (msg_1f7bdbc46001XJbBJcMWuQ2vix)

Now let me look at the board tools and my worktree state.

## Output 51 (msg_1f7bdce3f001sNWP1C2D0Cmu7y)

Let me get the full text of the key post and understand the Antonina posting mechanism.

## Output 75 (msg_1f7bdea7f001yPHt3hcGr2FhSY)

Let me fetch the full board JSON to a scratch file and check Antonina's post command.

## Output 99 (msg_1f7be168b0017Nmi5ObsTLzcFl)

I'll use the shell tool directly.

## Output 164 (msg_1f7bf9bd9001EUhHj12MZBzxE9)

I have a thorough understanding of the key post. Now let me check the ledger for this front and look at my scratch space, then build an independent solver.

## Output 175 (msg_1f7c0a3ae001F4ZAY03ndUMuH7)

Found a local verification draft — likely "my verification comment." Let me read it.

## Output 195 (msg_1f7c0ca96001O4xe4zrng8IZDB)

Now I'll write my own independent solver (different representation) and validate it against known S(n) values.

## Output 213 (msg_1f7c38957001vP5UKgOYRm8QBu)

F(A_8) is expensive. Let me reorder to compute the cheap gadget first and validate only small n.

## Output 231 (msg_1f7c454ef001ccOhojcUgR7qrk)

My solver independently confirms the finite inputs: e(U)=e(W)=56, F(U)=6, F(W)=7, F(A_n)=S(n) for n≤6, and e/F/V are all additive under ordinal sum. Now let me verify the full construction P_S, Q_S computationally and the reachability threshold.

## Output 249 (msg_1f7c6bd350015Z0TIW6IdC10W7)

Need a larger tool timeout.

## Output 357 (msg_1f7d57ffa001aqAxSZXuWKvOCx)

## Host / recovery / side effects
- **Host:** `billy-dev` (lubko). Sourced `/home/lubko/.profile` before every Antonina call.
- **Recovery audit (no duplicate external actions):** inspected conversation state, worktree, git, and board. Worktree `/home/lubko/soring-fronts/eindex-collision-transfer-minimax-alln` stayed clean on `billy-dev` at `6a96398` (no repo/Lean/CI/main/ledger changes). No commits, no pushes, no ledger edits. Checked board for prior posts by `SoringP1 frontier: eindex-collision-transfer-minimax-alln` before posting: none found. Posted **exactly once** to #301 (confirmed in `antonina board comment --json` result: `2026-11-20T07:21:53.380Z`, author `SoringP1 frontier: eindex-collision-transfer-minimax-alln`, id present in returned board state). Post payload/result saved to `/tmp/opencode/eindex-transfer/post_result.json`.
- **Scratch (own):** `/tmp/opencode/eindex-transfer/` — `my_solver.py`, `solver_fast.py`, `report_301.md`, board snapshot, post artifacts.

## Task 1 — independent recomputation of e, F, V [experiment]
From-scratch solver (`/tmp/opencode/eindex-transfer/solver_fast.py`: bitmask posets with transitive closure, subset-DP linear-extension counter, memoized unrestricted minimax `F`, memoized greedy max-e/worst-tie `V`; no prior/reporter code reused).

- Validation: `e(A_n)=n!` and `F(A_n)=S(n)=1,3,5,7,10` for `n=2..6` (matches OEIS A036604 / known values). OK.
- Gadget `U = (6-chain ⊔ 2 free), n=8`: `e(U)=56`, `F(U)=6`, `V(U)=6`.
- Gadget `W = (5-chain ⊔ 3-chain), n=8`: `e(W)=56`, `F(W)=7`, `V(W)=7`.
- Ordinal-sum spot checks on 15 pairs `A_a ⊕ A_b` (`a+b<=7`): `e(P⊕Q)=e(P)e(Q)`, `F(P⊕Q)=F(P)+F(Q)`, `V(P⊕Q)=V(P)+V(Q)` all held (15/15 each).

These confirm the stated base collision, including **F(U)=6, F(W)=7** for the unrestricted minimax value (not only greedy V). Finite computations, reproduced here but not kernel-checked / not hand case-analyzed.

## Tasks 2–4 — transfer to F, reachability, conclusion (paper proof + experiment)

**Construction [definition/paper proof].** For sufficiently large `n`, let `m=n-8`. For any set `S` of distinct primes with `sum(S)<=m`, let `C_S` be the disjoint union of chains of lengths `p∈S` plus `m-sum(S)` free elements (`e(C_S)=m!/∏_{p∈S}p!`). Define `P_S = U ⊕ C_S`, `Q_S = W ⊕ C_S`.

**e-collision and F-separation [paper proof, using Task 1 base values].**
- `e(P⊕Q)=e(P)e(Q)` (standard: linear extensions concatenate). Hence `e(P_S)=56*e(C_S)=e(Q_S)`.
- `F(P⊕Q)=F(P)+F(Q)` for the unrestricted minimax height: incomparable pairs of `P⊕Q` are exactly `Inc(P)∪Inc(Q)` (all cross pairs fixed by the ordinal sum); a comparison inside one summand yields children `(summand_child)⊕other`, preserving the other summand and all cross relations, so by induction `F(P⊕Q)=F(P)+F(Q)`. (Consistent with the 15/15 spot checks above.) Hence `F(P_S)=F(U)+F(C_S)=6+F(C_S) != 7+F(C_S)=F(W)+F(C_S)=F(Q_S)`.
- **Distinct e-values [paper proof].** For `S!=T`, let `q=max(S△T)`, wlog `q∈S\T`; `q` prime gives `v_q(p!)=0` for `p<q`, `v_q(q!)=1`, so `v_q(∏_{p∈S}p!)!=v_q(∏_{p∈T}p!)` and `e(C_S)` (thus `56*e(C_S)`) differ across distinct `S`.
- **Superpolynomial count [experiment + standard/prior #301 06:42Z L4].** DP count of prime-subsets with `sum(S)<=m`: `11, 89, 4687, 159061` for `m=10,30,100,200` (`2^{Omega(sqrt(m/log m))}`).

**Reachability and greedy-vs-unrestricted subtlety [paper proof + experiment] (task 3).**
Partition `A_n` into `L` (|8|) and `H` (|m|). Explicit consistent path:
1. `8m` cross comparisons `(l,u)`, each answered `l<u` (always consistent since no `u<l` is ever forced) ⇒ `A_8 ⊕ A_m`.
2. Realize `U`/`W` inside `L` by <= 6 chain-consistent comparisons ⇒ `U ⊕ A_m` / `W ⊕ A_m`.
3. Realize `C_S` inside `H` by `p-1` consistent comparisons per prime chain, total <= `m` ⇒ `P_S` / `Q_S`.
Steps inside one summand preserve the other and all cross relations. Total depth `d <= 8m+6+m = 9n-66`.
- **Unrestricted minimax reachability:** every answer is merely consistent, so this is a valid path in the unrestricted comparison game (no max-e/greedy condition required). For `n>=3000`, `10n-64 <= ceil(log2 n!) <= S(n)` (checked: `n=3000 -> 29936 <= 30332`; margin grows), hence `d <= S(n)` for all sufficiently large `n`. Therefore `P_S,Q_S` are depth-reachable from `A_n` within `S(n)` comparisons in the unrestricted sense.
- **Greedy-ball distinction:** 06:42Z additionally exhibited a greedy-legal (heavy-or-tie / max-e, via swap-injection) path of depth `<=10n-64` — a stronger per-move constraint. The F-transfer needs only the unrestricted consistent path above.
- **Important limit (feasibility):** this establishes ambiguity on states **depth-reachable** within `S(n)` comparisons. It does **not** claim `P_S,Q_S` lie on `S(n)`-optimal continuations (paths with `d + F(P) <= S(n)`); `F(P_S)=6+F(C_S)` and `F(C_S)` (order `log2 e(C_S)`) may be large, so optimal-feasibility is open.

## Conclusion (delivered to #301)
**[paper proof]** Yes — for all sufficiently large `n`, there are `2^{Omega(sqrt(n/log n))}` distinct extension counts each inherently ambiguous for exact `F` on states reachable from `A_n` within `S(n)` comparisons: `e(P_S)=e(Q_S)` but `F(P_S)!=F(Q_S)`. This extends the closed greedy e-index barrier (06:42Z) to the unrestricted minimax value `F` on the depth-bounded reachable set.

## Honest limits / scope (no overclaim)
- Barrier about **e-indexed evaluators** on that reachable set only; says nothing about non-e-indexed evaluators of `S(n)`. Not an ambiguity claim on `d+F(P)<=S(n)` optimal-feasible states.
- **No theorem completion for `S(n)` / `SORT-BOUND-U`; no class separation.** `SORT-BOUND-U` remains sparse, in `PSPACE` and in `P/poly` (per `docs/problem.md` / AGENTS.md).
- `F`-additivity under ordinal sum is a standard induction (paper proof, spot-checked); `F(U),F(W)` are finite solver computations (independently reproduced). Not kernel-checked; no Lean.
- No repo/CI/main/ledger/workflow changes; worktree left clean. Full report posted to #301 as above.
