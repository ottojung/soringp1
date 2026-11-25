# antonina-teX4Q2YEwzQTZ9ghQuOkwQ-psoas

Session: ses_e01eb10a6ffe1GxyLeMUkyoj0f
Workspace: /home/lubko/soring-fronts/defect-a1-universal-floor-alln
Created: 1795264147352; updated: 1795266933813

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_1fe1c5dc10012us3PenF6Id6H2)

I'll start by inspecting the environment carefully, since the note warns about a possible interrupted turn with external side effects. Let me check git state, branch, and durable records first before doing anything.

## Output 28 (msg_1fe1c789f001ui5aKOyVLtIIvF)

Clean working tree on `billy-dev`. Let me read the key docs and discover how the research board is accessed, plus check for any durable task records from an interrupted turn.

## Output 51 (msg_1fe1cb1b1001Kq98J4vQ5zsji5)

No MCP board resource; the board is a script. Let me check the board digest, the ledger, and any durable records from a possible interrupted turn.

## Output 66 (msg_1fe1cd221001f1wkJH5lWujz3b)

The ledger was modified today at 12:37. Let me identify my front's record and agent tag, and check whether an earlier turn on this front already posted to the board or wrote records.

## Output 90 (msg_1fe1cf494001aGn1oDaU5TPT5B)

My front is `running` with agent_id `teX4Q2YEwzQTZ9ghQuOkwQ-psoas`. Let me check the board thoroughly for any prior post by this tag/front (to avoid duplicate side effects) and read the closely-related recent result.

## Output 112 (msg_1fe1d4671001Gff64bATkGxxey)

Let me inspect the board JSON structure and explicitly search all pages for my front/tag, to confirm no duplicate post happened.

## Output 130 (msg_1fe1d72db001b7naFkCgM2sIaT)

No prior board post by my tag. Let me check for scratch artifacts or durable records from an interrupted turn.

## Output 159 (msg_1fe1dc203001kaxvM53xlu4b4B)

I have a clear picture of the state. Let me read the full text of the most relevant prior board results (the bracket proofs and the tight-insertion investigation) to ground the mathematics before attacking it.

## Output 170 (msg_1fe1ea53d001Z8MbGCWb75xhvN)

I now have the full context. Let me check the primary literature for known results on insertion/comparison complexity of posets, while I set up an independent evaluator.

## Output 203 (msg_1fe2046be001NAxLak4vu1AEVV)

Web search is unavailable (fetch works). I'll proceed with primary reasoning plus my own independent computation. Let me build a from-scratch exact minimax evaluator and validate it before any poset claims.

## Output 221 (msg_1fe21157d001md1yINxgRUg7CM)

Evaluator validates on all anchors. Now let me search for a counterexample, focusing on the reformulation: a counterexample needs the excess `r` to DROP by ≥1 (when info-gap is c−1) or ≥2 (when info-gap is c) upon adding the free key.

## Output 337 (msg_1fe3ed56b001TlXZAYvUDXjSch)

## Recovery / side effects
- Inspected git (`billy-dev`, clean, at `6a96398`), board #301 pages 1-5, and ledger: front `defect-a1-universal-floor-alln` is `running` (agent `teX4Q2YEwzQTZ9ghQuOkwQ-psoas`), started 2026-11-21T12:29:07Z; no board post by this tag/agent was found. No commits, pushes, PRs, board writes, or repo changes were made by this session.
- Scratch only: `/tmp/opencode/myfront/` contains a fresh from-scratch evaluator and search scripts created this session; `/tmp/opencode/tightinv` and `ref_tight_insertion_20261121.py` are earlier interrupted-turn artifacts (not mine to post). A `search2.py` random run was killed by SIGKILL after partial output; no external side effect.

## Front
`defect-a1-universal-floor-alln` (board #301). Question: for all b>=1 and all b-posets B, is `delta(A_1,B)=F(B⊔A_1)-F(B) >= c-1`, `c=ceil(log2(b+1))`, or can an information-excess host give `delta <= c-2`?

## Model / definitions [definition]
`F(P)` = exact adaptive minimax comparisons to identify an unknown linear extension of finite poset `P`; `e(P)` = number of linear extensions; `A_1` isolated key; `B⊔A_1` disjoint union. `r(P)=F(P)-ceil(log2 e(P))>=0` is information excess (tight iff `r=0`). `delta = F(B⊔A_1)-F(B)`, `c=ceil(log2(b+1))`.

## Independent validation [experiment, scratch]
Fresh transitive-closure minimax + minimal-element subset-DP `e` count (`/tmp/opencode/myfront/eval.py`), no project code/board tables reused. Validated: `S(n)=F(A_n)=0,0,1,3,5,7,10` for `n=0..6`; `F(C_b)=0` for `b=1..8`; `Z_b`: `e=Fib(b+1), F=b-1` for `b=2..9`; N-poset witness `e=5,F=3,eU=25,FU=5,delta=2,c=3`.

## Mathematical finding (reformulation + obstruction, no all-n proof/counterexample)

### 1) Exact algebraic reformulation [deduction]
Let `gapinfo = ceil(log2((b+1)e(B))) - ceil(log2 e(B)) ∈ {c-1,c}`. Since `e(B⊔A_1)=(b+1)e(B)`,
`delta = gapinfo + r(B⊔A_1) - r(B)`.
Thus a `c-2` shortfall is equivalent to a **large excess drop**:
- `gapinfo==c-1` (the dangerous case): `delta <= c-2  <=>  r(B⊔A_1) <= r(B)-1`.
- `gapinfo==c`: `delta <= c-2  <=>  r(B⊔A_1) <= r(B)-2`.

With `r(B⊔A_1)>=0`, any counterexample requires `r(B)>=1` (or `>=2` in the second case). This recovers the known P2 fact [literature/board, Viche 11:19Z disposition]: information-tight hosts (`r=0`) give `delta∈{c-1,c}`. The open content is exactly whether adding one isolated key can collapse host excess by >=1 (or >=2) unit.

### 2) The naive disjoint-channel lower bound fails [deduction, failed approach]
A tempting argument is: B-comparisons and x-comparisons are disjoint channels, adversary forces `F(B)` B-comparisons and `c` x-comparisons, so `F(U)>=F(B)+c`, `delta>=c`. **This is false.** Counterexample: N-poset gives `delta=2 < c=3`. The flaw: a comparison `(bi,bj)` can become forced by transitivity through `x` (`bi<x` and `x<bj` imply `bi<bj`), so x-comparisons can resolve B-incomparabilities. The two comparison sets are disjoint as edges but not informationally independent; the adversary cannot fix a B-strategy independently of x-placement. This is the same mechanism behind the verified tight-host `c-1` cases.

### 3) Exhaustive small-n evidence [experiment]
Exhaustive over all forward-labeled closures (every isomorphism type represented by some topological labeling; deduped by closure) found **no** `delta <= c-2`:
- `n=4`: 40 distinct posets, max `r-rU = 0`, time 0.05s.
- `n=5`: 357 distinct posets, max `r-rU = 1` (witness `n=5,e=8,F=4,r=1; eU=48,FU=6,rU=0,c=3,gapinfo=3,delta=2`), no violation, 3.0s.
- `n=6`: 4824 distinct posets, max `r-rU = 1` (witness `n=6,e=240,F=9,r=1; eU=1680,FU=11,rU=0,c=3,gapinfo=3,delta=2`), no violation, 371s.

A partial random search (`n=5..8`, incomplete; killed) observed `n=5 mindelta=2 maxdrop=0 maxr=0`; `n=6 mindelta=2 maxdrop=1 maxr=1` before kill; `n>=7` not completed. These are finite experiments, not an all-n argument.

## Obstruction / what would decide it
- **Falsifier (still open):** an explicit excess host B with certified `F(B)>=ceil(log2 e(B))+r`, `r>=1`, and a certified upper strategy for `B⊔A_1` making `r(B⊔A_1)<=r-1` (in the `gapinfo=c-1` case) or `<=r-2`. The b=5 excess host `(e=8,F=4,r=1,gapinfo=3)` gives `delta=2=c-1` (drop 1, not enough) — it saturates the drop but has `gapinfo=c`.
- **Proof route obstruction:** one needs a general inequality `F(B⊔A_1) >= F(B)+ceil(log2(b+1))-1` even for excess B, i.e. “transitivity through one isolated key can save at most one comparison beyond the chain defect”. The disjoint-channel proof fails because of transitivity shortcuts; a valid proof must control how many B-forcing comparisons can be made redundant by x-placement. I did not find such an all-n argument.
- **Complexity significance [deduction]:** this is a structural minimax invariant. A proof would strengthen the a=1 defect envelope in disjoint-union superadditivity; a counterexample would refine it. Neither gives a new bound on `S(n)` or any complexity-class separation for `SORT-BOUND-U` (which is in PSPACE; tally/P/poly barrier applies).

## Honest limits
No all-n proof, no counterexample. n<=6 exhaustive and partial random n<=8 give no `c-2` case; max observed excess drop is 1. I did not construct a certified c-2 witness and did not prove the c-1 floor. S(n) and SORT-BOUND-U remain open. No repo/Lean/board/ledger changes made.
