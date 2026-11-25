# antonina-8kz5QUKOVfPyoq1sAFr1ws-lawrence

Session: ses_dfc2cf122ffeORMu1SzPMRZCyC
Workspace: /home/lubko/soring-fronts/ff9-independent-20261122
Created: 1795360493466; updated: 1795362883560

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_203da848d0012PfqKnz5sWMEGS)

I'll start by inspecting the current state carefully, as the recovery notice warns. I won't post or duplicate anything until I know what's already happened.

## Output 80 (msg_203dc22b3001TrgUW97doICBPV)

No #301 comment from this front exists yet, and no scratch solver was written by me — only the dispatch records. I'll write everything from scratch now. Let me create a C++ decision-search solver with a hard memo cap.

## Output 109 (msg_203dd93bb001GStgpH8Ua2fil2)

No C/C++ compiler available, but Go is. I'll port the same from-scratch design to Go.

## Output 143 (msg_203de3cf3001RmIpq3DHf5GJkJ)

Validation passes exactly (FF tight at n=5..8; S(n)=7,10,13,16). Now the main n=9 search, time-boxed to 15 minutes.

## Output 163 (msg_203e5f795001oL0jEUbRoALfZr)

FF_9 is settled: **TRUE at b=17**, with a witness tree of exactly 2·90720−1 = 181439 nodes (one leaf per linear extension). Now I'll attempt the optional V_9 question.

## Output 194 (msg_203edb2cd001zdRNiZkSjM2xQ5)

A Viche update referencing my result appeared at 15:40Z, but I haven't posted my own result comment. Let me verify exactly what happened and what the executive already said, to avoid duplicating an external action.

## Output 209 (msg_203edea0a0017jK5pz6iuLo5Ie)

The interruption only killed the optional V_9 run; the main FF_9 result is intact, and I have not posted anything. Let me add a cheap greedy-witness check for V_9 (and FF_9 as a control) before finalizing.

## Output 234 (msg_203ee8d5a001m9AMkN51LXEeB8)

Greedy fails even for FF_9 (which is tight), so that check is inconclusive for V_9. I'll make one optimized, bounded attempt at V_9, then post exactly one result comment.

## Output 316 (msg_203f73e17001Oj7vcdflg2z3OG)

## Status (recovery-aware; no external actions repeated)

- **Inspected state**: clean worktree `research/ff9-independent-20261122` at `6a96398`; no repo/Lean/test/CI/ledger changes. My only scratch artifacts are in `/tmp/opencode/ff9_*` (written from scratch, no other agent code read). Agent `8kz5QUKOVfPyoq1sAFr1ws-lawrence` is this session.
- **Board check**: I did **not** post a #301 comment. A Viche Executive referee update already posted at `2026-11-22T15:40:15Z` citing this worktree/agent and reporting F(FF_9)=17 as independently verified. I did not duplicate it.

## Result (from my from-scratch run)

**Hypothesis**: For `FF_n` = two disjoint 2-chains `{a<b},{c<d}` + `(n-4)` free keys, is `F(FF_9)` exactly 17? (counting lb `ceil(log2(9!/4)) = ceil(log2 90720)=17`.)

**Evidence** (Go decision search `canSolve(P,b)`, transitive-closure states, subset-DP `e(P)=|LE(P)|`, prune `clg(e)>b`, per-poset memo with bounds, move ordering by `max(e child)`, hard memo cap 5M entries, `n<=9`, scratch only `/tmp/opencode/ff9_verify_fromscratch.go`):
- Validation `n=5..8`: `F(FF_n)=5,8,11,14` TRUE at those budgets; `S(n)=F(antichain_n)=7,10,13,16` TRUE. Delta check: `ceil(log2(10!/3))-ceil(log2(10!/4))=22-21=1`.
- `FF_9`: `e=90720`, `clg=17`, `canSolve(FF_9,17)=TRUE`, `nodes=4,968,374`, `le calls=12,741,047`, `memo=1,302,417`, `374.50s`, no abort. Witness reconstruction from memo: depth 17, **181,439 nodes = 2*90720−1** (one leaf per linear extension).
- Counting sanity: `canSolve(FF_9,16)=FALSE` by `clg(e)=17>16` (immediate).

**Falsification/limits**: FF_9@16 is refuted by counting, so 17 is tight from below; the height-17 strategy gives tightness from above. This is a finite exact-minimax fact, not an S(n)/SORT-BOUND-U theorem. V_9 (`{a<b,a<c}+6 free`, `e=120960`, `clg=17`) was **not settled**: greedy at b=17 is inconclusive (also fails on FF_9 control), and an optimized bounded exact search was SIGKILLed after ~12M nodes / ~2.63M memo entries with no answer; I did not obtain `F(V_9)=17` or `18`. The 18+ tightness-counterexample question for FF_9 is answered negatively: 18 is possible as a non-tight upper bound, but 17 is already exact.

**Changed belief**: High confidence that `F(FF_9)=17` exactly (independent from-scratch reproduction, consistent with counting bound and full witness shape). `F(V_9)` remains open here.

**Next decisive question**: Settle `F(V_9)` at budget 17 vs 18 with a memory-bounded/canonicalized exact solver (or a provable upper-bound construction), to determine `gap(9)=max(F(V_9),F(C3_9))-F(FF_9)` without relying on unverified witness claims.
