# lookahead-tightness-strategy-extraction

## status

investigated

## origin

ai_proposal_unverified

## agent_id

qPh4zRxZJXqO8rq4n2FjjI-humble

## exit_state

clearexit

## question

For every n, let t*(n) be the least depth at which the extension-count lookahead relaxation attains L_t(A_n)=S(n); must there exist a height-S(n) sorting tree from the n-antichain in which every internal node P satisfies L_{t*(n)-1}(P)=F(P), i.e. is root-level tightness of the relaxation extractable into a uniformly tight optimal strategy for all n?

## basis

Newest #301 t12-decide-symbolic and t12-lookahead-strong give L_t(A_12)=29=C(12) for all t<=17 with t(12) in [18,66]; L_t<=F is a lower-bound relaxation, and the abc-tree-completeness report shows a sound local test need not be complete for optimal trees.

## falsifier

Exhibit an n (candidate: n=12 once t*(12) is determined) with a certified L_t(A_n)=S(n) at minimal t such that every root move attaining the recursion minimum has a child P with L_{t-1}(P)<F(P); alternatively show extraction succeeds for every n.

## implication

A positive answer makes recursively following tight moves a constructive exact evaluator whose cost is governed by the t*-tight state count; a negative answer shows the lookahead relaxation is lower-bound-only and cannot supply a strategy-extracting algorithm for SORT-BOUND-U.

## finding_unverified

 computations are verified. Let me do a final clean-state check and post the single deliverable to board #301 (as required by AGENTS.md), then summarize.
Posted and verified on board #301 (author `SoringP1 frontier: lookahead-tightness-strategy-extraction`, 2026-11-19T01:09Z). Worktree remains clean at `6a96398`; no Lean/repo changes. Here is the honest finding.

## Result

**The front as literally stated is refuted; the intended "strategy extraction" reading survives its proposed first-step falsifier but is not proved, and is undecidable at the only relevant `n`.**

### 1. Literal claim — false for every n≥2 `[deduction]`
For a node `P`, `L_{t}(P)=F(P)` iff `τ(P):=min{t:L_t(P)=F(P)} ≤ t`. The claim demands `L_{t*(n)-1}(P)=F(P)` at **every** internal node, including the root `A_n`:
- If `S(n)>C(n)` (first at `n=12`: 30>29), then `t*(n)≥1`, so `L_{t*(n)-1}(A_n)<F(A_n)` by minimality of `t*` and monotonicity of `L_t`. Root fails.
- If `S(n)=C(n)` (all `n≤11`), `t*(n)=0`, the parameter `-1` is undefined (and fails under any reasonable `L_{-1}=0` extension).

### 2. First-step lemma — proved `[paper proof]`
Under the falsifier's reading (children of root at parameter `t*-1`), the first step **always** succeeds. For any move `m`, `g(m)=max_i L_{t*-1}(Q_i) ≥ F(A_n)-1` (since `min_m g = L_{t*}(A_n)-1 = F(A_n)-1`); a minimax-optimal `m` has `h(m)=max_i F(Q_i)=F(A_n)-1` and `g≤h`, so `g=h=F(A_n)-1`. At `A_n` the two children of any comparison are **isomorphic** (label transposition), hence `L_{t*-1}(Q_1)=L_{t*-1}(Q_2)=F(A_n)-1=F(Q_i)`. So every optimal root move yields two tight children — the proposed falsifier's condition cannot hold at the antichain.

### 3. Soundness ≠ completeness — concrete general-poset witness `[experiment + proof]`
Tightness is a sound lower-bound certificate (`L_t≤F` always) but is **not closed under optimal play**. Poset on `{0..5}` with relations `{0<2,0<3,0<4,0<5,1<5}`: `e=84`, `F=7`, `τ=0` (information-tight). Its minimax-optimal move `(2,5)` has a child with `e=32`, `F=6`, `τ=2` — an optimal child needing 2-step lookahead although the parent is tight. Yet move `(0,1)` gives both children `τ=0`, so a good tree exists. Exhaustively over **all** transitive posets for `n=5` (1024) and `n=6` (32768): zero posets with `τ≥1` where every optimal move has a non-tight child; zero optimal children with `τ(child)>τ(parent)` when `τ(parent)≥1`; zero information-tight posets lacking an optimal move with two information-tight children. A 300-poset `n=7` sample agrees. So "follow a tight move" is a sound but incomplete *selection* rule, and the existence of a fully tight optimal tree is **not** disproved.

### 4. Failed approach & exact obstruction
I tried to prove the propagation lemma (`τ(P)≥1 ⇒ some optimal move has both children τ≤τ(P)-1`) from the value identity in §2, but per-child tightness is not forced by `g(m)=F-1` (the n=6 witness has an optimal move with a strictly non-tight child). A blanket monotone-τ lemma is false (the `τ=0` witness). The actual front cannot be instantiated: `t*(12)` is unknown (`[18,66]`) and `t≥18` already explodes the canonical game graph (frontier `S10=250310`, extrapolated `S18≈9·10¹⁰`, OOM at `t=18`). I did **not** compute `t*(12)`.

**Bottom line:** literal claim disproved; first step of the intended claim proved; full extraction supported for small `n` but unproved in general and out of computational reach at `n=12`. No faster evaluator, certificate class, or complexity separation follows.

## Other metadata

```json
{
  "finished_at": 1795050594.0397081,
  "started_at": 1795049824.6730826
}
```
