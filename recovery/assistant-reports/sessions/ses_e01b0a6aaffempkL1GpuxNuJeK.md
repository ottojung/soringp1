# antonina-cxkQCxbZZbB6rbu5HwK5YI-pakhra

Session: ses_e01b0a6aaffempkL1GpuxNuJeK
Workspace: /home/lubko/soring-fronts/power2-host-insertion-universality-alln
Created: 1795267975528; updated: 1795270159501

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fe4f5d7a001TykXriJVSqJgJv)

I'll start by understanding my environment and the research setup.

## Output 17 (msg_1fe4f75e0001IKRLAqavJHvzkF)

I'm on billy-dev as required. Let me explore the repository structure and read the key documents.

## Output 46 (msg_1fe4f9eb40015SSQlhPECLIoUv)

Let me check the research board digest and the ledger front.

## Output 57 (msg_1fe4fad20001E8zu0Kwrfj0juw)

Let me get the full text of the key board entries, especially the 12:09Z one.

## Output 77 (msg_1fe4fff87001ZAEMZ6AvU8dvyx)

Let me look at earlier scratch work to avoid repeating side effects, and read the literature + relevant research notes.

## Output 122 (msg_1fe51610e001r4c7nQIYQgI2pB)

Let me check available Python graph tooling and read a couple of relevant prior scratch notes.

## Output 133 (msg_1fe524987001798SUDHpYQ1uNE)

Let me study the primary literature with targeted searches while I plan the computation.

## Output 162 (msg_1fe52e56c001AuzqyWVsTUl5dr)

Now let me write my own from-scratch evaluator and search for a counterexample at b=7.

## Output 180 (msg_1fe535bec001MgsVyoxWtniRE6)

The plain evaluator is too slow for n=8. Let me implement a much faster decision-version minimax with information-bound pruning.

## Output 207 (msg_1fe54e737001gOqkKvP2a5U3gk)

Excellent — the decision-version evaluator is ~100× faster. Now let me generate all non-isomorphic posets up to n=8 and validate the generation.

## Output 225 (msg_1fe55a8db00132hrYOjKv1tdLG)

Generation validated against the known poset counts. Now let me search all 2045 non-isomorphic 7-element hosts for a shortfall.

## Output 243 (msg_1fe59088d001GIhrHvUwXpzkih)

I found a clean reformulation. Let me verify it and test a stronger structural conjecture computationally.

## Output 295 (msg_1fe6ff4af001yWKM6KptRhuV05)

## Scope / hygiene

- **Host**: `billy-dev` (checked). Git worktree `/home/lubko/soring-fronts/power2-host-insertion-universality-alln` clean on `billy-dev...origin/billy-dev` at `6a96398` before and after; no repo files changed, no commits, no Lean, no tests, no board post.
- **Recovery check**: inspected git state and `/tmp/opencode` scratch. Prior scratch files from other agents exist; I created only `/tmp/opencode/p2hostscratch/{eval.py,eval2.py,gen.py,search7.py,gapcheck.py}` and ran local computations. No external side effects.
- **Board**: read recent #301 digest; newest relevant post is `exec-tight-insertion-invariant-alln` (2026-11-21T12:09:32Z) and Viche disposition (12:15:19Z). They report the tight-host power-of-two fact, exhaustive b=4/5, sampled b=6, and no all-b invariant. I did **not** post.

## Front attacked

> For every b with b+1 a power of two and EVERY b-element host poset B, including information-excess non-tight hosts, is the one-key insertion defect delta(A_1,B)=F(B ⊔ A_1)-F(B) exactly ceil(log2(b+1)), or can a non-tight host fall strictly below that chain insertion value at some b=2^m-1?

Labels: `B` b-element poset, `e(B)` linear extensions, `F(B)` exact adaptive-comparison minimax, `delta(B)=F(B⊔A_1)-F(B)`, `c(b)=ceil(log2(b+1))`, information gap `g(B)=F(B)-ceil(log2 e(B))>=0`.

## Proved reduction (paper deduction, small)

Let `b+1=2^m`, so `c(b)=m`. For the disjoint union with an isolated key, `e(B⊔A_1)=(b+1)e(B)=2^m e(B)`, hence

`ceil(log2 e(B⊔A_1)) = m + ceil(log2 e(B))`.

Therefore

`delta(B) = F(B⊔A_1)-F(B) = m + g(B⊔A_1)-g(B) = c(b) + g(B⊔A_1)-g(B).    (*)`

Combining (*) with the universal upper bound `delta(B) <= c(b)` (sort B optimally, then binary-insert the isolated key into the b+1 slots; standard, and this is the same upper argument used in the board posts) gives

`g(B⊔A_1) <= g(B)` for all B when `b+1` is a power of two, equivalently `delta(B) <= c(b)`.

The information lower bound gives `delta(B) >= ceil(log2((b+1)e(B))) - F(B) = c(b)-g(B)`. Thus

`delta(B) in {c(b)-g(B), ..., c(b)}` in general, and the power-of-two shortfall question is exactly:

> can adjoining an isolated element strictly decrease the information gap at a power-of-two multiple, i.e. `g(B⊔A_1) < g(B)`?

This is a **sound reduction**, not a proof of the front. It distinguishes power-of-two sizes: when `b+1` is not a power of two, `ceil(log2((b+1)e))` can be `m+ceil(log2 e)-1`, so `delta=c-1` is possible even with `g'=g` or can coexist with gap decrease.

## Independent scratch computation (experiment, not proof)

From-scratch evaluator in `/tmp/opencode/p2hostscratch/` (no project code/board tables/prior evaluator reused). It represents closed posets as bitmask rows, recomputes full transitive closure on each comparison, counts linear extensions by subset DP, and computes `F` by decision minimax `feasible(P,t)` with information-bound pruning and child-count ordering. 

**Validation**: `S(n)=F(A_n)=0,0,1,3,5,7,10` for n=0..6; `F(C_n)=0` for n=1..8; also `S(7)=13, S(8)=16` (1m19s, matching literature). Unlabelled-poset generator (incremental maximal-element/ideal construction, WL-hash + NetworkX isomorphism dedupe) reproduces OEIS-style counts 1,1,2,5,16,63,318,2045,16999 for n=0..8.

### Exhaustive power-of-two sizes

| b | b+1 | unlabelled hosts | non-tight | shortfalls delta<=c-1 | delta distribution on non-tight | gap change g' vs g |
|---:|---:|---:|---:|---:|---|---|
| 1 | 2 | 1 | 0 | 0 | - | 0/0/1 dec/inc/same |
| 3 | 4 | 5 | 0 | 0 | - | 0/0/5 |
| 7 | 8 | 2045 | 391 (all gap g=1) | **0** | all delta=3 | **0/0/2045** |

For b=7 I computed `F(B)` and `F(B⊔A_1)` for every non-tight host (391 hosts); all had `delta=3=c`. I also checked all 2045 hosts for gap change: `g(B⊔A_1)-g(B)=0` for every host, tight or non-tight.

### Non-power-of-two controls (same evaluator)

| b | b+1 | hosts | gap dec | gap inc | gap same | note |
|---:|---:|---:|---:|---:|---:|---|
| 4 | 5 | 16 | 0 | 0 | 16 | all tight |
| 5 | 6 | 63 | 1 | 13 | 49 | gap decrease exists |
| 6 | 7 | 318 | 6 | 46 | 266 | gap decreases exist |

The b=5 gap-decrease example: `e=8, F=4, g=1`, union gives `e'=48, F'=6, g'=0, delta=2`, while `c(5)=3`. This is **not** a power-of-two shortfall (b+1=6); it shows gap can decrease, so the identity (*) alone does not force `g'>=g`.

## Result on the front

- **Falsifier not found.** Exhaustive search found **no** b=2^m-1 non-tight host with `delta <= c-1` for b=1,3,7.
- **All-b claim not proved.** I do **not** claim `delta(B)=c(b)` for every host at every power-of-two size. The b=15 case is computationally out of reach by this exact enumeration (n=16 poset count / 32768 unlabelled 15-posets is borderline but 16-element union minimax per host is expensive; I did not attempt it). More importantly, there is no proof ruling out gap decrease at larger 2^m-1.
- **Structural obstruction to a naive proof**: the obvious strengthening "adjoining an isolated element never decreases the information gap" is false (b=5,6 counterexamples above). Any all-b proof must use the power-of-two multiple condition essentially.

## Status / honest limits

- **Proved here**: exact reduction `delta=c+g'-g` at b+1=2^m; universal bracket `delta in {c-g,...,c}`; exhaustive confirmation for b=1,3,7.
- **Not proved**: the universal all-b power-of-two host-insertion formula. No certified all-b theorem, no counterexample.
- **Not a complexity consequence**: this does not change known bounds for exact unary `S(n)` / `SORT-BOUND-U`; it is a small structural front about insertion defects.
- **Certificate soundness vs completeness**: the upper strategy (sort then binary insert) is a sound upper certificate; exact minimax values used here are exhaustive decision-tree computations on the finite poset game, not heuristic lower bounds. The reduction (*) is a deduction from definitions.
