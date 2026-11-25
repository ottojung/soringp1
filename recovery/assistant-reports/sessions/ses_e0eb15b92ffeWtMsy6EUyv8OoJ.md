# antonina-qPh4zRxZJXqO8rq4n2FjjI-humble

Session: ses_e0eb15b92ffeWtMsy6EUyv8OoJ
Workspace: /home/lubko/soring-fronts/lookahead-tightness-strategy-extraction
Created: 1795049825426; updated: 1795050586051

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f14ea77f001OUWJIj3BwOBZVy)

I'll start by understanding the environment: git state, worktrees (the task says "billy-dev ONLY"), and the key documents.

## Output 25 (msg_1f14eb4e3001EHeJDR4nM19wpX)

I'm on `billy-dev` in the correct worktree. Now let me study the research board #301 (via digest), the literature, and inspect the current worktree for any earlier work.

## Output 44 (msg_1f14ec79d001FGzt3z5Kp5JSMd)

Let me read the full board posts on the key reports and understand the lookahead definitions. Let me check the board tooling and search relevant docs.

## Output 72 (msg_1f14efef5001Tb5xzAUKq9GiZ2)

I now have a clear picture of the definitions and prior work. Let me set up a scratch computation (no repo changes) to analyze the tightness-index propagation, which is the mathematical crux of the front.

## Output 170 (msg_1f151cac6001BFDIyRBrUlMtTE)

I found a bug in my scratch closure routine (dead placeholder code polluting `add`). Let me fix and re-validate against the known count of labeled posets (4231 for n=5, 130023 for n=6).

## Output 199 (msg_1f1530162001TiLeqMAZRUSxAq)

I've verified a key empirical pattern on all posets up to n=6. Let me now probe n=7–8 by random sampling to look for a counterexample to the propagation property.

## Output 249 (msg_1f15766d90013XFWbC8ciZG7qh)

Let me decode and verify the concrete counterexample (poset 268 on n=6) into human-checkable terms, and also confirm the n=5 example.

## Output 292 (msg_1f1591a7a001G3sUjycl5Vc4YY)

I have solid mathematical findings. Let me check the board-posting interface and scan for any prior posts by this front to avoid duplicates (recovery audit).

## Output 303 (msg_1f1595d200015PA7ZIKMGEQW31)

All computations are verified. Let me do a final clean-state check and post the single deliverable to board #301 (as required by AGENTS.md), then summarize.

## Output 339 (msg_1f15a1903001S3bRd5lOGauqvD)

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
