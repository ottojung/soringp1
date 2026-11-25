# e-count-tie-optimal-move-barrier-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

xySs1elM8GBycVKlKSm6Mf-toil

## exit_state

clearexit

## question

For infinitely many n, must there exist a poset state reachable on a height-S(n) optimal play where two incomparable pairs have identical linear-extension-count statistics (same child-e multiset and same max-child e) yet only one is minimax-optimal, so no tie-break function of extension counts alone can select an optimal move?

## basis

The 13:41Z/13:47Z #301 optimal-strategy-circuit-size result and referee report a 6-element witness where three tied pairs share child-e multiset (14,14); ledger greedy/tie-break fronts concern the adversary's answer, not the sorter's move selection.

## falsifier

Either prove that for all sufficiently large n every reachable optimal-play state admits some e-count tie-break selecting a minimax-optimal move, or exhibit an infinite family of states with unavoidable e-tied non-optimal moves; the reported n=6 witness alone is not an all-n result.

## implication

A positive answer rules out the whole family of extension-count-greedy optimal-move selectors and framed-certificate move choices as a route to an e-oracle-free evaluator for S_unary, sharpening the known #P-hardness of exact e(P) into a structural barrier.

## finding_unverified

e is still clean.
Done. Here is the mathematical report (also posted once to #301 at 14:25Z; worktree clean at `6a96398` on `billy-dev`, no repo/Lean/CI/ledger changes).

## Verdict

The FRONT is **not established**, and its offered witness **does not support its own conclusion**. I proved a genuine local disproof of the "no e-count tie-break" implication and isolated the exact obstruction to an all‑n verdict.

## Finding 1 — the witness's implication is false (verified two ways, incl. brute force)

The n=6 witness reproduces exactly: `e(P)=28`, `F(P)=5`, 7 comparabilities, three pairs tied at child‑e multiset `(14,14)`. But the tie is **breakable by extension counts alone**:

- `(3,5)` (optimal): both children have grandchild‑e multiset of **length 14**, specifically `(1,2,3,4,5,5,6,8,9,9,10,11,12,13)`.
- `(1,3)`, `(1,5)` (suboptimal): their children have multisets of **length 12** — `(1,4,4,4,5,5,9,9,10,10,10,13)` and `(3,3,4,4,5,6,8,9,10,10,11,11)`.

So a tie‑break function of extension counts alone *does* select the optimal move here. The same refinement holds on the two established #301 witnesses (`S=(0,21,0,33,5,0)`: `(0,5)` vs `(1,3)` at `{10,16}` are separated by M1‑lengths `(10,14)` vs `(12,10)`; `W6=(30,16,8,0,0,0)`: `(0,5)` vs `(1,3)/(2,4)` at `{6,30}` separated by `(16,8)` vs `(16,10)`). The prior barriers are correctly **narrow** — they rule out *one‑step child‑e scoring*, not all e‑count tie‑breaks.

## Finding 2 — exhaustive n=6

- All **129,303** reachable posets enumerated; **19,320** have a one‑step mixed e‑tie, and in **all 19,320** the depth‑1 e‑signatures separate optimal from non‑optimal pairs (0 failures).
- Stronger: grouping every state by `(e(P), M1(P))` yields **154 keys, zero with differing F(P)**. Hence `F` is a function of extension counts (one step deep) throughout n=6, and an e‑only optimal‑move selector exists at *every* n=6 state. This is a concrete disproof of the front's conclusion for n=6.

## Failed approach / exact obstruction to all‑n

- Ordinal sum preserves the tie and F‑gap (`e` multiplicative, `F` additive; verified `P6⊕A₂`: child‑e `(28,28)`, F‑gap `(6,5)` vs `(5,5)`). But it **cannot pump to infinite n**: `P6` has 3 maximal elements, so `P6⊕A_q` forces `3q` cross comparisons; `d+F ≥ 10+3q+S(q) > S(q)+6⌈log₂(q+6)⌉ ≥ S(6+q)` for `q≥2`, so those states are off every optimal play. Only `q=1` (n=7) is budget‑feasible.
- The general lemma needed to disprove the front (equal `(e,M1)` ⇒ equal `F`, or depth‑1 signatures always separating different‑optimality tied pairs) is proved only at n=6. The n=7 cospectral sampling that could probe it was killed by the backend failure and I did not blindly restart it.
- No explicit all‑n height‑`S(n)` strategy exists and `S(n)` is open for `n≥23`, so neither the front nor its universal negation is derivable today.

## Honest limits

Nothing here is a theorem about `S(n)`/`SORT-BOUND-U`: no new value, bound, class placement, or general‑poset transfer (Brightwell–Winkler #P‑hardness and general decision‑tree hardness do not become completeness results for the fixed antichain family). Soundness of choosing an optimal move is trivial; completeness of e‑count selectors is the open crux, and all n=6 evidence resolves it positively. The genuinely new, independently checkable content is the refutation of the front's implication on all offered witnesses and all 129,303 n=6 states, plus the ordinal‑sum budget obstruction. My only external write is the single #301 comment.

## Other metadata

```json
{
  "finished_at": 1795443971.110661,
  "started_at": 1795442091.6261866
}
```
