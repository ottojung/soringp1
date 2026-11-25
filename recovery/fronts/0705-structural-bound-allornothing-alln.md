# structural-bound-allornothing-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

SjouAC029FIxXVOZkvFKNC-soldier

## exit_state

clearexit

## question

For every n and every state reachable on some height-S(n) optimal path from the n-antichain, is the project's Theorem B structural lower bound B(P) = sum_i ceil(log2 e(P_i)) + sum_i delta_i always either exactly F(P) or exactly ceil(log2 e(P)), i.e. can the certified series-decomposition merge gaps ever produce a bound strictly between the information bound and the exact minimax value?

## basis

An exhaustive n<=6 computation over optimal-play-reachable states classified 68611 with info=bound=F, 720 with info<bound=F, and 3720 with info=bound<F, with zero intermediate cases; see docs/research-structural-lower-bounds.md and the n=6 defect-witness posts on board #301.

## falsifier

Exhibit for some n a reachable optimal state with ceil(log2 e(P)) < B(P) < F(P): certified merge gaps that strictly beat leaf counting yet still fail to certify the minimax value.

## implication

If the dichotomy holds all-n, certified merge gaps are all-or-nothing lower-bound certificates and any complete polynomial invariant must encode prime-state defect directly; if it fails, partial gaps can be combined toward a succinct certificate bearing on SORT-BOUND-U.

## finding_unverified

ed: e(Q)=120, F(Q)=8, e(R)=15, F(R)=5, e(P)=1800, info=11, bound=12, F=13. Now let me check the posting procedure and do a final duplicate check on the board before reporting.
A recent related post appeared. Let me read it to check for overlap, and get the correct comment command.
I've independently confirmed a genuine counterexample. The related post is a different front and does not contain my finding. Let me prepare a concise board report.
The comment posted successfully. Let me verify it appears on the board exactly once.
## Result: the all‑n dichotomy is **false** — explicit n=12 falsifier

The front's claim (that Theorem B's bound `B(P) = Σᵢ⌈log₂ e(Pᵢ)⌉ + Σᵢδᵢ` is always either exactly `F(P)` or exactly `⌈log₂ e(P)⌉` on optimal‑play‑reachable states) is refuted. I found and independently verified a reachable state with

```
info = 11  <  B(P) = 12  <  F(P) = 13
```

### The witness
`P = Q ⊕ R` (ordinal sum), successor bitmasks (n = 12):

```
P = (4034, 4032, 4035, 4032, 4032, 4032, 128, 0, 3584, 3072, 2048, 0)
```

- **Q** on {0..5} `= (2,0,3,0,0,0)`: a 3‑chain disjoint‑union 3 free keys. A single incomparability component, **not** a certified merge ("other"). `e(Q)=120`, `⌈log₂120⌉=7`, `F(Q)=8` → prime defect **1**.
- **R** on {6..11} `= (2,0,56,48,32,0)`: `Merge(2,4)`, literature‑certified, `M=5`, `⌈log₂C(6,2)⌉=4`, **δ = 1**.

So `e(P)=1800`, `info=11`, `B=7+4+1=12`, `F=F(Q)+F(R)=8+5=13`. `F(P)=13` is rigorous without the general additivity theorem: all cross relations Q<R are known, so cross comparisons gain nothing; sorting Q needs ≥8 and R needs ≥5, and 13 is achieved. Two independent implementations (decision solver + separate memoised minimax and a from‑scratch downset extension counter) agree on every number.

### Reachability
An explicit legal 14‑comparison path reaches P: build Q via `(2,0),(0,1)`; build R via `(6,7),(8,9),(10,11),(9,10)`; then the cut via `(q,6),(q,8)` for q∈{1,3,4,5}. With `ℓ+F = 14+13 = 27 ≤ S(12)=30`, P lies on a height‑S(12) tree. This is the front's own convention — my enumerator reproduced its n=6 classification **exactly** (68611 / 720 / 3720 / 0).

### Why n≤6 showed zero intermediate
An intermediate state needs both a defective non‑merge block (first at size 6; all posets on ≤5 have defect 0) and a positive certified gap (smallest is `Merge(2,4)`, size 6) or a rounding gain whose partner must have `e` just above a power of two (first at size 6). These ingredients cannot coexist below n=12, and a single series block is never intermediate. I did **not** exhaustively classify n=7–12, so minimality of 12 is an observation, not a proved claim.

### Honest limits
- This refutes one structural conjecture only. It yields **no** P/NP/NP‑membership consequence, no faster evaluator, and no new S(n) value. S(n) and SORT‑BOUND‑U remain open.
- A genuine failed approach: exhaustive n=7 reachable‑state enumeration (my attempt and a sibling front's) was killed by memory exhaustion (~6.2M memo states); the counterexample was found constructively instead.
- Complexity update: partial certified gaps **do** exist, so "merge gaps are all‑or‑nothing certificates" is false; a complete polynomial lower‑bound certificate must additionally handle prime defects in "other" blocks.

**Side‑effect audit:** no commits, no repo/Lean/test changes (git clean at `6a96398` on `billy-dev`); exactly one board‑301 comment posted and verified (`structural-bound-allornothing-alln`, 06:30Z). Scratch work is confined to `/tmp/opencode`.

## Other metadata

```json
{
  "finished_at": 1795415502.5034704,
  "started_at": 1795414031.4229603
}
```
