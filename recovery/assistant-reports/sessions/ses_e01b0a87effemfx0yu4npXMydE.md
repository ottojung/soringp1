# antonina-znXQTP5RiFXZOmsexRw6ud-neuralgic

Session: ses_e01b0a87effemfx0yu4npXMydE
Workspace: /home/lubko/soring-fronts/insertion-defect-ef-summary-sufficiency-alln
Created: 1795267975068; updated: 1795269841464

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fe4f5cea001sAG2rH056EN8zm)

I'll start by understanding the environment, the repository state, and the key documents. Let me explore in parallel.

## Output 25 (msg_1fe4f6ab20013OcsN8JRDG1UEb)

I'm on billy-dev. Let me read the board #301 digest, literature, and explore the repository structure.

## Output 44 (msg_1fe4f85670018f5DhVMkrRpAZM)

Let me get the full text of the key board messages and understand the precise definitions and prior work on this exact front.

## Output 68 (msg_1fe4fb0a1001LP8h7W9LMgUlaO)

This is a rich research history. Let me check the ledger entry for this front, existing scratch work (in case of interrupted session), and the existing evaluator code.

## Output 87 (msg_1fe5080c7001YWZDkSI72VtgMs)

I now have a comprehensive picture of the research history. This is the `insertion-defect-ef-summary-sufficiency-alln` front. Prior work exhaustively checked b=4,5 (no splits) and sampled b=6. Let me check the environment and start a serious independent attack. First, environment + a literature check in parallel.

## Output 115 (msg_1fe515132001xfzeSQbmXjzXuo)

No C compiler, but Python 3.12 with numpy/networkx is available. Let me write an independent, from-scratch exact minimax evaluator and validate it on known values before any enumeration.

## Output 140 (msg_1fe51d0f10019mLF8nrZY240iZ)

Evaluator validated (S(n) correct; N poset e=5,F=3, N+A1 e=25,F=5). Now let me build isomorphism-canonical poset enumeration (iso classes, not wasteful labelled enumeration) and verify against known counts.

## Output 165 (msg_1fe526676001PevRqdnnmExdPl)

Canonical enumeration matches all known iso-class counts through m=8. Now the actual search: compute (e, F, δ) per iso class and look for (e,F)-collisions with different δ.

## Output 183 (msg_1fe5472df001irsuWHXKpxPzkw)

b=4,5 match prior work exactly (b=5: 24 (e,F)-classes, zero splits). b=6 is expensive with fresh caches. Let me run b=6 in the background while I analyze the structure theoretically.

## Output 194 (msg_1fe54c094001DOAeGmejq2pVuw)

Let me dump the full b=5 table to understand the (e,F)→δ structure while b=6 runs.

## Output 205 (msg_1fe54fe47001wgt2WqSqY5pf1k)

Let me try the literature search again (primary sources on exact poset sorting complexity) while the computation runs.

## Output 261 (msg_1fe55b95a001Eu1BsPY30WHLp2)

Let me check the b=6 result now (one check after doing other work).

## Output 281 (msg_1fe5600b7001R44IGQXS9PR2Xi)

There's a `search7.py` process — possibly from an earlier interrupted session of this front. Let me inspect it (the task asks me to check for prior work).

## Output 292 (msg_1fe562263001NjOhL45bmjHT98)

Let me inspect that concurrent scratch (to avoid duplicating a sibling's angle) and check my b=6 progress.

## Output 303 (msg_1fe566f43001BPdNGKs8zPmykW)

Let me write an optimized search with a shared global minimax cache, processing dense posets first, so I can reach b=8.

## Output 321 (msg_1fe578831001Pp4baFPTtK1eMm)

**A split was found at b=6** — (e,F)=(60,7) with δ=2 and δ=3. This is exactly the falsifier. I must verify it rigorously before claiming anything. Let me cross-check with the independent per-call evaluator and a canonical/non-isomorphism check.

## Output 339 (msg_1fe57db7a001S5gyVvPjVpmHGi)

Both witnesses verified with the validated evaluator: valid, non-isomorphic, e=60 (DP + brute force), F=7, but F(B⊔A₁)=9 vs 10. Now I need a **completely independent** minimax (extension-set representation, no transitive closure) plus explicit tree/lower-bound certificates before claiming a theorem.

## Output 357 (msg_1fe5833b50018DFQuNkFP96irr)

Confirmed by a fully independent extension-set minimax. Let me extract explicit decision-tree upper bounds and independent budget-based lower bounds, and identify the posets' clean structures.

## Output 375 (msg_1fe58b01b001OU9YLsFq43sAzf)

Both witnesses now have full certificates: explicit height-9/height-10 trees with 420 singleton leaves, and height-8/height-9 infeasibility. This is a genuine counterexample. Now let me (a) certify F(B)=7 explicitly, and (b) test whether the collision extends to larger b (ordinal-sum / disjoint-union with chains).

## Output 393 (msg_1fe5ad7f7001TeD6PqXUb1i6Sv)

The extension test via extension-set repr was too slow. Let me test extensions with the fast transitive-closure minimax (shared cache) in the background.

## Output 404 (msg_1fe5aff5f0018ZxU0Ou6V6pQJD)

That background job imports a module with slow top-level code. Let me kill it and inline the helper functions.

## Output 442 (msg_1fe5ebcb7001Rm7dpTLOhvTlkr)

Let me check the original exhaustive b=6 run (independent per-B caches) and confirm the full set of splits.

## Output 463 (msg_1fe60bb2f0019WelCYBdHH7B76)

Let me run a fuller b=6 census and probe more extension lengths in the background, while I finalize the write-up.

## Output 475 (msg_1fe60edaf001w7Fz1LBJ77OB5E)

The independent b=6 run finished. Let me read its output.

## Output 486 (msg_1fe610521001TmO6CY2wpy9Eyr)

The fully independent exhaustive b=6 census (13 min, fresh caches) confirms **exactly 2 splits**, both among information-excess posets — explaining why prior tight-host searches found none. Let me verify the b=10 ordinal-sum extension with the independent method.

## Output 508 (msg_1fe630429001PjIvHQLtnKQnat)

Three independent computations now agree on the b=6 splits. Before posting, let me check the board for any prior post from this front (recovery requirement) and confirm the posting command.

## Output 519 (msg_1fe633a280010TN1CEmcw3rlcU)

No prior post from this front. Let me re-confirm the b=10 extension numbers (fast evaluator) before including them in the report.

## Output 530 (msg_1fe6390ae001KhDxnJ61RSqkmV)

Both extensions confirmed. Let me write and post the finding to board #301 (the contract's reporting channel).

## Output 548 (msg_1fe63ea33001DyoL0zfrMuvdDA)

Post succeeded. Let me verify it appears exactly once on the board.

## Output 559 (msg_1fe640d9c00141fv3lEFhyU3p1)

## Finding: the `(e,F)`-summary sufficiency claim is **false** — certified counterexample at `b = 6`

**Claim attacked.** For every `b`, do `e(B)=e(B′)` and `F(B)=F(B′)` force `δ(A₁,B) = F(B⊔A₁)−F(B)` to be equal? Answer: **no**.

### The counterexample

Two non-isomorphic 6-element posets, both with `e = 60` and `F = 7` (so both are *information-excess*, `F − ⌈log₂e⌉ = 7−6 = 1`):

| poset | structure | successor masks | `e` | `F` | `F(B⊔A₁)` | `δ` |
|---|---|---|---|---|---|---|
| `B_short` | `A₁ ⊔ C₂ ⊔ C₃` (isolated key + 2-chain + 3-chain) | `(0,8,48,0,32,0)` | 60 | 7 | **9** | **2** |
| `B_long` | `C₂ ⊔ K₂,₂` (2-chain + "2 minima below 2 maxima") | `(4,24,0,0,0,24)` | 60 | 7 | **10** | **3** |

Here `e(B⊔A₁) = 420`, `⌈log₂ 420⌉ = 9`, `c = ⌈log₂ 7⌉ = 3`. So `B_short⊔A₁` is information-tight (`δ=2=c−1`), while `B_long⊔A₁` acquires one unit of excess (`δ=3=c`).

### Verification (three independent methods, scratch only)

1. **From-scratch transitive-closure minimax**, validated first on `S(n)=0,0,1,3,5,7,10` and `F(C_b)=0`.
2. **`e=60` two ways**: subset DP *and* brute force over all `6! = 720` permutations.
3. **Structurally independent extension-set minimax** (surviving-linear-extension sets, no transitive closure): `F=7` for both, `F(B⊔A₁)=9` vs `10`.
4. **Explicit certificates**: a height-9 tree with 420 singleton leaves for `B_short⊔A₁` with height-8 *infeasible*; a height-10 tree with 420 singleton leaves for `B_long⊔A₁` with height-9 *infeasible* (budget DP).

An **exhaustive census of all 318 iso classes at b=6** (three independent runs agreeing) finds exactly two `(e,F)` splits — `(60,7)` and `(120,8)` — both with `δ∈{2,3}` and **all split members information-excess**. This is precisely why prior tight-host searches at b=4,5 (which I reproduce: 24 `(e,F)` classes, zero splits) missed it. Ordinal-summing each witness with a 4-chain gives b=10 posets still with `(e,F)=(60,7)` but `δ=3` vs `4`, so the collision is not isolated to b=6.

### Complexity implication (and its limit)

`δ` is not a function of `(e,F)` nor of `(b,e,F)`. Hence any state compression that records only `(e,F)` is **sound as a bound index but incomplete for exact insertion cost** — it cannot underwrite an exact unary `S(n)` evaluator via `F(A_a⊔A_b) ≥ F(A_a)+F(A_b)+min(a,b)+1`. This is a method-family soundness/completeness point, **not** a new `S(n)` bound or a complexity-class separation (`SORT-BOUND-U` is sparse and in PSPACE; general-poset minimax does not transfer to the antichain root without a reduction).

### Honest limits

No all-`n` theorem, no faster evaluator, no P/NP/PSPACE consequence. The result is one fully certified counterexample plus an exhaustive b=6 census and one b=10 extension; a clean infinite family is **not** established. `S(n)` and `SORT-BOUND-U` remain open.

Reported once to board #301; worktree clean at `6a96398` on `billy-dev`, no Lean/repository changes.

## Output 578 (msg_1fe6baf2e001vCMF9f7Elnmfyo)

No unfinished work to continue.

I inspected the durable state:

- **Board #301**: exactly **1** post authored `SoringP1 researcher: insertion-defect-ef-summary-sufficiency-alln` containing the falsifier result (`total matching posts: 1`). No duplicate post.
- **Git**: `/home/lubko/soring-fronts/insertion-defect-ef-summary-sufficiency-alln` is clean at `6a96398` on `billy-dev...origin/billy-dev` (`git status --short --branch` empty). No commits, no repo files changed.
- **Scratch only**: computations live under `/tmp/opencode/efsplit/` (not a repository side effect). `search7.py` seen in `/tmp/opencode/p2hostscratch` belonged to another cwd/process, not this front’s claimed result.
- **External effects**: only the single board comment is confirmed. Nothing uncertain.

The result stands as reported: the `(e,F)`-summary sufficiency claim is **refuted** at `b=6` by certified `(e,F)=(60,7)` witnesses with `δ=2` vs `3` (and a second `(120,8)` split), independently verified and exhaustively censused; `S(n)`/`SORT-BOUND-U` remain open.
