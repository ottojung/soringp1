# antonina-vSU5wXIo1AdwsmbytIVaKH-glossy

Session: ses_e0979ab65ffegnQY736d5n5CCS
Workspace: /home/lubko/soring-fronts/tight-n-state-gap-alln
Created: 1795137361075; updated: 1795138119817

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 416 (msg_1f68db2f6001YhEIpkNNSVs1GF)

Let me run the independent gap engine to get fresh numbers, and fetch primary literature in parallel.

## Output 495 (msg_1f69124ab001TvPIgUPTUstqZK)

The n=7 independent engine is still running in the background; meanwhile the attack is complete enough to report. Here is the turn's deliverable.

---

# Turn report — front `tight-n-state-gap-alln` (Antonina #301), billy-dev

## 1. What was attacked, precisely

**Claim under attack (falsifier arm 1 of the front):** *For all sufficiently large information-tight n, the local-optimal reachable state set and the globally feasible optimal state set coincide* — i.e. for all sufficiently large n with `E(n) = S(n) − ⌈log₂ n!⌉ = 0`, one has `L_loc(n) = L_tree(n)`.

**Falsifier arm 2:** *construct an explicit infinite family of tight n with a nonempty optimal-state gap* `G(n) := L_tree(n) ∖ L_loc(n) ≠ ∅`.

**Definitions used (fixed by the board's own 16:51Z local-vs-global correction and re-verified here):**
- `L_loc(n)`: states reachable from the n-antichain via paths of **locally minimax-optimal** moves (each move satisfies `1 + max(F(c₀),F(c₁)) = F(P)`).
- `L_tree(n)`: states occurring in some correct decision tree of height `S(n)` from the antichain (= reachable via budget-feasible paths, each move satisfying `1 + max(F(c₀),F(c₁)) ≤ S(n) − d − 1` at depth `d`).
- `L_loc ⊆ L_tree`; the gap is `L_tree ∖ L_loc`.

**Rigorous backbone (deduction):** with slack `σ(P) = S(n) − t − F(P) ≥ 0` at depth-`t` state `P`, an optimal move keeps children feasible and may leave slack ≥ 1 via an *easy outcome* (F-drop ≥ 2); a zero-progress move at slack `σ ≥ 1` is feasible and burns slack. Hence gap states are exactly states reached via feasible-but-locally-suboptimal moves.

## 2. Attack results this turn (fresh, independent computation)

From-scratch bitmask minimax + L_loc/L_tree BFS (`/tmp/opencode/mech_engine.py`, no repo/predecessor code):

| n | S(n) | C(n)=⌈log₂n!⌉ | E(n) | tight? | L_loc | L_tree | G(n) |
|---|---|---|---|---|---|---|---|
| 5 | 7 | 7 | 0 | **yes** | 1551 | 1551 | **0** |
| 6 | 10 | 10 | 0 | **yes** | 65,551 | 66,991 | **1,440** |

- **n=6 re-confirmed**: gap **1,440** reproduced independently (board-verified value); all 1,440 gap states are *direct* zero-progress children of slack states in `L_loc`; slack distribution among `L_loc` states: σ = 1 (11,700), σ = 2 (6,840), σ = 3 (720).
- **n=7** (ledger/board: `L_loc`=2,769,663, `L_tree`=3,044,007, G=274,344) — independent rerun still in flight.

## 3. Mathematical finding

At **information-tight n=6** (E=0) the locally-optimal reachable set **does miss states that lie on height-10 optimal trees** (1,440 of them), mechanistically via slack-burned zero-progress moves. The same holds at tight n=7 (G=274,344). The phenomenon is therefore **not refuted** by tightness.

Sharper: tightness does **not** determine the gap — tight n=5 has G=0 (no slack states at all), tight n=6,7 have G>0. So the falsifier's arm-1 proposition cannot be a theorem of tightness alone, and the "coincide for all sufficiently large tight n" arm is at minimum unresolved (the data refute coincidence *below* any threshold that includes 6,7, and force any true threshold to be >7).

## 4. Disproof attempts — outcome (honest)

- **Attempt: prove `L_loc = L_tree` for all sufficiently large tight n.** Failed/abandoned at this depth: the existence of slack-ged gap states at tight n=6 (E=0) means a coincidence theorem would have to exclude slack-burned optimal trees specifically at large n; no such exclusion was derived, and the small-n data (G=0 at tight n=5, G>0 at tight n=6,7) leave the all-n structure open rather than refuted.
- **Attempt: infinite tight-n family with nonempty gap.** Blocked: the tight set is only finitely known (S=C at n≤11 and n=20,21), infinitude is an open front (`info-tightness-infinite`, `fredman-eventual-delta-obstruction`), and n≥8 enumeration is beyond budget.

## 5. Failed approaches / exact obstruction

- The "gap needs slack" reduction is now complete at n≤6; the remaining obstruction is purely **all-n**: whether G(n)>0 recurs at larger tight n and whether the tight set is infinite.

## 6. Complexity implication — status

The front's implication (infinite information-tight gap ⇒ locally-optimal reachable sets can miss legitimate optimal states at the info-tight optimum ⇒ constrains sound evaluator designs) is **consistent with and sharpened by** the reproduced n=6/7 gaps; but it is **conditional** on infinitude of relevant tight n and remains unproven. No P/NP/PSPACE consequence follows (Mahaney sparsity, tally barriers, general-poset transfer caveats respected).

## 7. Honest limits

- No all-n theorem proved or disproved here; no new S(n); no Lean/repo/commit changes this turn; host billy-dev respected.
- n=7 independent rerun in flight; gap at known-tight n=8–11 and n=20,21 not computed.
- Soundness (checker) vs completeness (state coverage) kept distinct, as required.

**Bottom line:** the locally-optimal-vs-globally-feasible gap at information-tight n is real at tight n=6 and n=7 (reproduced at n=6; gap=1,440 all via slack-burned zero-progress moves; n=7 gap=274,344), while tight n=5 shows coincidence. The all-n falsifier (coincidence for all sufficiently large tight n, or infinite tight-n gap family) therefore remains **open but actively narrowed**: tight n=6,7 refute coincidence at small tight n, and no mechanism forces the gap to vanish at large tight n.

No process success is being claimed; no proof of any all-n statement is being reported.
