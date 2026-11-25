# antonina-WdiY9nZIQLrqTG8iCswRqw-unit

Session: ses_e05fa5c92ffeeIDEQsx1zSZspR
Workspace: /home/lubko/soring-fronts/verify-fj-tight-20-21-20261120
Created: 1795196036106; updated: 1795196699848

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fa05a611001iPdvTBoBx6A5p2)

I’ll first locate the cited #301 material and its plan, then check the recurrence against primary Ford–Johnson sources and independently verify the arithmetic without modifying the repository.

## Output 83 (msg_1fa06005f001EJ13YUNzfiAF0V)

## Audit result

The numerical claim is **correct**, under the standard Ford–Johnson merge-insertion comparison-count convention. The recurrence independently gives
\[
F(15)=42,\quad F(16)=46,\quad F(20)=62,\quad F(21)=66,\quad F(22)=71.
\]
The information lower bound \(L(n)=\lceil\log_2(n!)\rceil\) gives \(L(20)=62\) and \(L(21)=66\). Thus, for those two sizes, \(L(n)\le S(n)\le F(n)\) proves \(S(20)=62\) and \(S(21)=66\). The values at 15, 16, and 22 are Ford–Johnson upper-bound counts; they are not established as optimal by that arithmetic alone.

## Recurrence and exact arithmetic

For the canonical merge-insertion algorithm, the worst-case insertion of the next element costs
\[
\left\lceil\log_2(3i/4)\right\rceil
\]
comparisons at size \(i\), so
\[
F(1)=0,\qquad
F(n)=F(n-1)+\left\lceil\log_2(3n/4)\right\rceil .
\]
This is the Jacobsthal-ordered insertion schedule: each pending element is inserted into a prefix whose length is bounded by the relevant \(2^r-1\) search range. The ceiling is exactly the least integer \(r\) satisfying \(4\cdot2^r\ge 3i\); no floating-point logarithms are needed.

The increments for \(i=2,\ldots,22\) are
\[
1,2,2,2,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,5.
\]
Summing gives the claimed \(F\) values. For the lower bounds, exact integer checks are \(2^{61}<20!<2^{62}\) and \(2^{65}<21!<2^{66}\), hence \(L(20)=62\), \(L(21)=66\). As a check on the distinction: \(F(22)=71\), whereas \(L(22)=70\).

## Evidence and limitations

- **Repository contract/model:** `AGENTS.md` defines \(S(n)\) as the minimum height of a deterministic adaptive comparison tree sorting every permutation of distinct labelled keys. `docs/problem.md` gives the same model; `docs/research-plan.md` explicitly distinguishes adaptive worst-case comparison counts from sorting-network sizes.
- **Primary literature checked:** Ford and Johnson, “A Tournament Problem” (1959), is the original merge-insertion source. Knuth, *The Art of Computer Programming*, Vol. 3, §5.3.1, is the standard detailed treatment. Stober and Weiß, *Lower Bounds for Sorting 16, 17, and 18 Elements* (2023), §1, explicitly identifies \(F(n)\) as the Ford–Johnson count, states \(C(n)\le S(n)\le F(n)\), and confirms \(S(n)=F(n)\) through \(n=11\); its introduction also records the established exact-value literature through \(n=22\), including Peczarski’s results for 14 and 22. The repository literature plan lists Peczarski (2012) and Stober–Weiß (2023).
- **Limitation:** I could not locate the actual 2026-11-20 #301 post or its attached plan in the available repository/files, so this audits the quoted claim, not the post’s provenance or any additional argument it may make. The recurrence verifies the algorithm’s **worst-case adaptive comparison count**, not that Ford–Johnson is optimal for every listed \(n\). \(\blacksquare\)

## Output 94 (msg_1fa0654b9001Bq82ZUqr5egVm1)

The prior task explicitly prohibited repo changes and board writes, and the response reports only a read-only audit. I’ll check the current worktree and available durable records for any unexpected effects before concluding.

## Output 117 (msg_1fa066ddb001WmNwxQ3btSgUiy)

No unfinished work or external effect is indicated. The worktree is clean (`git status` shows no changes), and `HEAD` is unchanged at `6a96398`; no #301-named file or task record was found. The prior audit was read-only and explicitly made no board writes, so I did not repeat it or perform any external action.

## Output 127 (msg_1fa0e2e82001KUaRs26L9Fmvqp)

I’ll correct the baseline by reading from `origin/main` directly, verifying the SHA, and inspecting the current #301 issue before re-auditing.

## Output 142 (msg_1fa0e48c7001cU61NdrceMsIz5)

Now let me find the #301 issue/comments mechanism and check relevant docs on `origin/main`.

## Output 161 (msg_1fa0e5b37001JMGAemrS5dRQws)

Let me inspect issue #301 via the board digest and `gh`, filtering for the relevant claim rather than dumping the whole board.

## Output 180 (msg_1fa0e702f001ewEu7iRZHVidUb)

The `gh` here is a wrapper with limited args. Let me inspect both tools and retry with valid parameters.

## Output 199 (msg_1fa0e83a7001KBfq4IEAwGkswu)

The board confirms this exact claim was dispatched at 17:02Z as one of five read-only checks. Let me check whether any result has since landed (to confirm it's still open) and compare the current docs against my stale baseline.

## Output 214 (msg_1fa0ecbef001imffi8PIWmCO4l)

Let me read the full text of the key posts — the original claim (16:48/16:52) and the latest 17:22Z result — to confirm status.

## Output 238 (msg_1fa0f23b5001l37B37czaAE5FZ)

The 17:22Z post is about the n=6 falsifier, not the FJ claim. Let me confirm the current docs from `origin/main` and whether they differ from my stale baseline.

## Output 253 (msg_1fa0f3b33001xmDHto8JMq2sVG)

Current docs on `origin/main` match my baseline on every point relevant here (the only worktree diff is an unrelated removed row). The claim remains open: dispatched at 17:02Z, no result posted since. Let me re-run the exact from-scratch arithmetic with integer-only operations.

## Output 264 (msg_1fa0f65cc0016DbCfHPnKnOUQZ)

Let me verify no result landed on later board pages and confirm the worktree stayed clean.

## Output 279 (msg_1fa0f9231001j1RNqudXT8Hh6j)

## Corrected-baseline audit: Ford–Johnson tight trees at n=20,21

### 1. Baseline correction
`git rev-parse origin/main` in both `/home/lubko/soring301` and the initially assigned worktree returns
**`6cddeaa2453d4da2ae0e918e50ba61c71a7da85f`** — matching the SHA in the steer. The worktree is detached at stale `6a96398d937d20977a91b9afa8619cb27feab269`. I read all authority from `origin/main` via `git show`, not from the worktree.

### 2. Current policy/docs (`origin/main`)
- `AGENTS.md`: byte-identical to the stale copy (same model, constraints, no theorem-completion claim).
- `docs/literature.md`, `docs/problem.md`: identical.
- `docs/research-plan.md`: the **only** worktree-vs-main diff is removal of one unrelated row (realizability-window necessity). The baseline facts relevant here are unchanged: FJ meets the information bound through n=11; exact values through n=22; n=23 open; Stober–Weiß (2023) settled 16/17/18.

**Stale-baseline effect on this claim: none.** No fact I rely on changed between 6a96398 and 6cddeaa.

### 3. Claim status on #301 (still open, not superseded)
- The claim originates with exec front `tight-tree-generation-beyond-insertion-alln-20261120` (16:48/16:52Z): definition `F(n) = Σ_{j=1}^n ⌈log₂(3j/4)⌉` (j=1 term 0), asserting `F(20)=62=L(20)`, `F(21)=66=L(21)`.
- Viche Executive at 17:02Z dispatched an isolated **read-only** check of exactly "Ford–Johnson tight trees at n=20,21" among five checks, explicitly "No results are verified yet."
- I searched #301 pages 1–2 for `20,21`, `tight trees`, `F(20)`, `F(21)`, `62`, `66`, `71`, `n=20`, `merge-insert`: the only later result post (17:22Z) verifies the **n=6 ceiling-loss falsifier**, not this claim. **No result supersedes or closes it.**

### 4. Independent verification (deduction + exact integer arithmetic, no floats)
FJ merge-insertion: pair keys, recursively sort winners, insert losers in Jacobsthal order by restricted binary search. Its certified worst-case height is `F(n)=F(n−1)+⌈log₂(3n/4)⌉`, where the increment is the least integer `t` with `4·2ᵗ ≥ 3n`. Information bound `L(n)=⌈log₂(n!)⌉`, least `t` with `2ᵗ ≥ n!`.

Increments n=2..22: `1,2,2,2,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,5,5`.

| n | F(n) | L(n) | tight |
|---|------|------|-------|
| 15 | 42 | 41 | no |
| 16 | 46 | 45 | no |
| **20** | **62** | **62** | **yes** |
| **21** | **66** | **66** | **yes** |
| 22 | 71 | 70 | no |

So `F(20)=62=L(20)` and `F(21)=66=L(21)` are **confirmed**, as are `F(15)=42, F(16)=46, F(22)=71`. **Literature:** Stober–Weiß §1 states `C(n) ≤ S(n) ≤ F(n)` with `F` the FJ count and FJ optimal through n=11; Peczarski established n=14,22; Ford–Johnson (1959) and Knuth §5.3.1 are the primary derivation sources.

### 5. Model/convention caveat
The numbers are **adaptive worst-case comparison counts** of a decision tree (FJ), not network sizes and not a claim about the complexity of *computing* S(n). Tightness at 20/21 means `C(n) ≤ S(n) ≤ F(n)=C(n)`, hence `S(20)=62`, `S(21)=66` — a sandwich, not a new algorithm or lower-bound method. At 15/16/22 the FJ count exceeds `L(n)`, so those values are upper bounds; their optimality rests on the literature (n=16=46 by Stober–Weiß, n=22=71 by Peczarski), not on the information bound.

### 6. Effects
Read-only throughout (`git show`, `board_digest`). Worktree remains clean at `6a96398`; no code changes, no board writes, no commits, no theorem-completion claim.
