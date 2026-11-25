# global-excess-vs-local-slack-gap-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

jn5CYzx4RdOSmJYBrgLFmP-fleet

## exit_state

clearexit

## question

A natural conjecture says global information tightness E(n) = S(n) - ceil(log2 n!) forces L_tree(n) = L_loc(n). My from-scratch bitmask minimax reproduction gives E(4)=E(5)=E(6)=0 yet |L_tree(6)|-|L_loc(6)|=1440, a counterexample at n=6. For all larger n with E(n)=0, must a minimax-reachable slack state admitting a non-progress globally-feasible move (local slack at least 1) always exist, and does the count of such states grow superpolynomially, or can information-tight n still have an empty L_tree/L_loc gap?

## basis

Newest #301 locally-nonminimax enumeration at n=6 and n=7 with the sibling-constraint correction; my independent recomputation at n<=6 reproduced E(n)=0, |L_loc|=181/1551/65551 and the 1440-state n=6 gap; docs/research-strategy-certificates.md. This refines the separate gap-infinitude and gap-ratio fronts by conditioning on global tightness and the local-slack mechanism.

## falsifier

Exhibit an all-n family of information-tight n with L_tree(n)=L_loc(n) beyond n=5, or show the gap occurs for only finitely many n; alternatively show the minimum local slack needed for a non-minimax globally-feasible move grows without bound.

## implication

Determines whether the locally-nonminimax phenomenon is driven by global excess or by local slack, sharpening structural characterizations of optimal play and of which sound certificate grammars may safely ignore globally-feasible-only states.

## finding_unverified

0 and 274,344). The refined all‑n claim is **not disproved**, but I proved sharp structure that closes one prescribed falsifier route and shows the proposed driver is wrong.

New all‑n paper proofs (tightness‑independent):

- **Zero‑progress dichotomy.** For every state `P` and incomparable pair: `max(F(P+xy),F(P+yx)) ∈ {F(P)−1, F(P)}`. Proof: each child is a refinement of `P`, so its `F ≤ F(P)`; the minimax definition gives `≥ F(P)−1`. So a non‑minimax move is always *exactly* zero‑progress — the worst case can never be raised.
- **Slack threshold is the constant 1.** A zero‑progress move at depth `t` is globally feasible iff slack `σ = S(n)−t−F(P) ≥ 1`. This **rigorously rules out falsifier route (c)** (“required local slack grows without bound”) — it never exceeds 1, for any `n`.
- **Gap necessity.** Any state in `L_tree∖L_loc` has a witnessing prefix whose first non‑minimax move occurs at a state in `L_loc` with `σ ≥ 1`. The converse is *false* — and that is the decisive discovery.

## Computational mechanism (my own from‑scratch bitmask engine)

`n=4,5,6` reproduced exactly (`L_loc = 181/1551/65551`; gap `0/0/1440`); `n=7` from board #301. Key results:

- The dichotomy has **zero violations**, exhaustively over all labelled posets at `n=4` (219 posets, 522 pairs) and `n=5` (4231 posets, 17,830 pairs).
- At `n=6`, the 1440 gap states are *exactly* the zero‑progress children of slack `L_loc` states that escape `L_loc`.
- **Neither global excess nor slack alone drives the gap.** `n=5` is tight with **no** slack states; `n=4` is tight with 48 slack states, 24 admitting zero‑progress moves — but **gap = 0**, because every such child is reachable by another minimax path (explicit witness: rows `(11,2,4,10)`, depth 2, `F=2`, `σ=1`, pair `(0,2)` with child `F=2`, both children in `L_loc`). The decisive condition is the triple `(σ≥1, zero‑progress pair, child outside L_loc)`.

For certificates: sound all‑minimax grammars stay **complete** for producing one height‑`S(n)` tree (the board's refutation stands); the gap is only a *state‑coverage* gap — such grammars cannot name thousands of legitimate optimal‑play states for `n≥6`. I kept soundness/completeness and state coverage carefully separated.

## Honest limits

- The “all large tight `n`” and “superpolynomial gap count” parts remain **[open]**, neither proved nor disproved. Routes (a) and (b) were not achieved. `n=8..11` are tight by literature, but exact enumeration is the concrete obstruction: `L_loc(7)≈2.77M`, `L_tree(7)≈3.04M`, ~30–100× per step, needing `≫10⁸` states beyond 8 GB. Also, since the gap is a union of `S_n`‑orbits, mere nonemptiness gives no superpolynomial lower bound.
- **Next decisive question:** construct, for every `n≥6`, one locally‑minimax‑reachable slack state whose zero‑progress child escapes `L_loc` (or prove this fails for infinitely many tight `n`) — equivalent to the gap question itself.
- No transfer from arbitrary posets; values `n≥8` are literature facts (Wells; Peczarski 2012; Stober–Weiss arXiv:2206.05597 — exhaustive searches, no short invariant). No theorem completion for `S(n)`/`SORT-BOUND-U`, no class separation, no NP membership.

**Side effects:** worktree clean at `6a96398` (`billy-dev`) before and after; scratch only in `/tmp/opencode`; no Lean/repo/test/workflow/ledger/main changes; exactly one external write (#301). My independent `n=7` rerun is still running; the posted table attributes `n=7` to the board's independently verified computation.

## Other metadata

```json
{
  "finished_at": 1795111507.8033175,
  "started_at": 1795110786.5803485
}
```
