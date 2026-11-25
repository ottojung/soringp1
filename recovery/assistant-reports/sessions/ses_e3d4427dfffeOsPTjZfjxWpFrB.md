# antonina-Kzb8WYKQUfD57IZWHe7HbX-hunted

Session: ses_e3d4427dfffeOsPTjZfjxWpFrB
Workspace: /home/lubko/soring-fronts/abc-certificate-checking-complexity
Created: 1794268453153; updated: 1794270364856

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 23 (msg_1c2bc01a9001fMkzd0gYK0rEyO)

I'll start by inspecting the environment state before doing anything, per the recovery instructions.

## Output 32 (msg_1c2bc0ff4001iOYztP0rDuEYTr)

Code mode only exposes the opencode namespace here. Using the shell tool directly.

## Output 73 (msg_1c2bd2155001YtDQFBTJi1fOkF)

I have substantial prior context. Let me check whether the interrupted turn did work on *this* front (the A/B/C verifier question) before doing anything.

## Output 121 (msg_1c2c067d7001Sh2rJiMy6w3E63)

The ledger confirms this is front `abc-certificate-checking-complexity`, still `running`, with no finding recorded. Let me locate any scratch work from the interrupted turn (without grepping the whole tree).

## Output 132 (msg_1c2c08273001heL5AGFNQQTLDA)

No post or finding exists for `abc-certificate-checking-complexity`; the ledger marks it `running` with no scratch directory of its own. So no duplicate side effect to avoid — I'll do the work fresh. Let me read the primary sources I have locally while I set up experiments.

## Output 161 (msg_1c2c16985001g1rWdTHT6CBKyJ)

Both sources give exact definitions. Now let me set up a small exact linear-extension engine and start probing the core quantity: the sign of `e(P+xy) − e(P+yx)` for height-two `P`.

## Output 190 (msg_1c2c33aac001nhiM5tsWXt1y5r)

A candidate polynomial criterion emerged: score each minimal by `s(x)=Σ_{b∈U(x)} 1/|N(b)|`. Let me test it hard against exact counts.

## Output 210 (msg_1c2c42325001MqZ20menycR24X)

The naive score criterion fails at `n=6`. Let me check what is known about this comparison problem in the literature before committing to a direction.

## Output 256 (msg_1c2c5565e001G8tXVgkCFVtl2y)

The score heuristic fails. Let me test structural hypotheses (nesting, expected rank, cycles) at larger sizes to map the true behavior.

## Output 267 (msg_1c2c713ab0012GWEbfZO0qCekS)

Nesting is clean. Condition A only needs counting when the slave count is ≤1, which constrains the pair sharply. Let me analyze that restricted regime and the equality (`D=0`) case.

## Output 287 (msg_1c2c7a0a50011lrPg71ZDKJBeO)

I can prove the nested case rigorously. Let me test how far the "unlock score" `s(x)=Σ_{b∈U(x)}1/|N(b)|` goes — perhaps it is exact except on ties.

## Output 307 (msg_1c2cb3197001R21kewHZ1sC15U)

No majority cycles appeared. Let me test whether the sign order coincides with expected rank (a natural total order).

## Output 318 (msg_1c2cb83d2001O1JvDVsuH2MVOD)

A sharper conjecture: in the only hard regime for condition A (`|U(x)\U(y)|=1`, `U(y)⊄U(x)`), the sign may be forced negative. Testing exhaustively:

## Output 329 (msg_1c2cbec130015Bqx1D5wpJ3phV)

The regime conjecture is false too — so local criteria genuinely fail. Let me consolidate the rigorous parts and verify them with an independent brute-force script.

## Output 340 (msg_1c2d3a102001EoZEJE6fbiEAqK)

All rigorous pieces check out. Let me run a final bounded structural check and re-inspect the board before posting.

## Output 355 (msg_1c2d5676f001v2hjuTYRI4Mpzn)

A random scan found `D=0` without a swap automorphism — so I must not claim that. Let me capture an explicit example and confirm there is no existing post for this front.

## Output 426 (msg_1c2d6c7160010LzGzged8Yg6QO)

All claims verified. Writing the one board post (none exists for this front).

## Output 455 (msg_1c2d768c6001vCyTXpN5pyMEgv)

Posted exactly once to board #301 at `2026-11-10T00:24:25Z` for front `abc-certificate-checking-complexity` (single unique match confirmed). No repository, Lean, branch, or ledger changes; worktree remains clean at `6a96398`.

## What I actually established

**1. Exact reduction of condition A (rigorous).** For height-two `P` split into minimals `A` and maximals `B`, with `D(x,y)=e(P+xy)−e(P+yx)`:
- the slave set of a minimal–minimal pair `(x,y)` is exactly `U(x)\U(y)` (verified on all 13,888 pairs); for maximal–maximal it is `N(y)\N(x)`; for minimal–maximal nonincident it is `U(x) ⊔ N(y)`. So the slave test is linear time.
- condition A ("≤1 slave and `2e(P+xy)≥e(P)`") therefore reduces to the sign of a GapP difference, and only when `|U(x)\U(y)|≤1`.

**2. A new theorem (paper proof).** If `U(y)⊆U(x)` then `D(x,y)≥0`. Proof pairs each induced minimal-order `π` with `y` before `x` against `π'` swapping the two positions; all maximal release times weakly decrease, and the interleaving count is monotone in release times. Corroborated on 31,968 nested instances with zero violations. This settles a large part of condition A in polynomial time.

**3. Counterexamples to the natural polynomial criteria (exact counts).** The "unlock score" `s(x)=Σ_{b∈U(x)}1/|N(b)|` is false: a 6-element poset with equal scores but `D(0,1)=−4`, and an 7-element poset with `s(0)>s(1)` but `D(0,1)=−4`. The refined guess "the 1-slave incomparable regime is always negative" is also false (`D=12` example). Both signs genuinely occur in the only residual regime.

**4. The exact obstruction to hardness.** The standard route from `#H2LE` (Dittmer–Pak) to the sign is blocked: ordinal sum and disjoint union multiply both `e(P+xy)` and `e(P+yx)` by the same positive factor, so `sign(D)` is invariant and padding/duplication can never expose a count through the sign. Same invariance holds for the whole A/B/C inequality.

## Honest verdict
- **No** polynomial-time exact verifier was found; **no** #P-hardness reduction was found. The front's dichotomy remains open, now sharply localised to `|U(x)\U(y)|=1`, `U(y)⊄U(x)`.
- The claimed complexity implication is **invalid independently of the counting question**: A/B/C are sufficient conditions for **GPC** (a good opening comparison), not for `F(P)≤k` or `S(n)≤k`; even a poly verifier plus completeness would not yield an NP certificate for `SORT-BOUND-U`. A/B/C are also still not known complete.
- Process success is not a proof: the only unconditional new theorem is the nested-upper-set result; everything else is exact-computation evidence or a barrier.

## Output 488 (msg_1c2d8a118001ygfhGPKW9MmPQs)

I'll verify state before doing anything, since the previous turn already posted. No new external actions will be taken unless something is genuinely unfinished.

## Output 507 (msg_1c2d8bb15001IpGKcU3QrjHiUS)

Git is clean and the board has exactly one post for this front. Let me confirm that post was not truncated by the backend failure (read-only).

## Output 518 (msg_1c2d8dde9001QbJKd9NPcFExjH)

Recovery check complete. No unfinished work and no duplicate side effects.

## State verified
- **Git:** worktree clean at `6a96398` on `billy-dev`; no commits, branches, PRs, or repository/Lean changes were made.
- **Board #301:** exactly **one** message for `abc-certificate-checking-complexity`, at `2026-11-10T00:24:25.241Z` (7,630 chars). It matches the local draft exactly after trailing-newline normalization — **not truncated** by the backend failure.
- **No duplicate post** exists, so I did not repost.
- **Scratch:** only `/tmp/opencode/abcverify/` (reproduction script `verify.py`).

## One item for review (not touched)
The durable ledger entry `abc-certificate-checking-complexity` still shows `status: "running"` with no `finding_unverified`/`exit_state`. That lifecycle field is managed by the research keeper/agent exit, not by a research agent, so I deliberately did **not** edit it. If the keeper did not record the exit, that is an operational status lag, not an uncertain external side effect: the only external side effect (the board post) is confirmed present and complete, exactly once.

## Completed mathematical finding (already posted)
- **Theorem (rigorous):** for height-two `P` and minimal `x,y`, if `U(y)⊆U(x)` then `e(P+xy)≥e(P+yx)`; hence condition A is polynomial on the nested regime.
- **Exact reduction:** the slave set of a minimal–minimal pair is `U(x)\U(y)`, so condition A needs a count comparison only when `|U(x)\U(y)|≤1`.
- **Counterexamples:** two exact posets refute the natural unlock-score criterion (including sign reversal), and a third refutes the "1-slave regime is always negative" guess.
- **Obstruction:** ordinal sum and disjoint union scale both counts by the same positive factor, so `sign(D)` is composition-invariant — blocking the standard `#H2LE` padding reduction.
- **Honest limit:** neither a poly verifier nor `#P`-hardness was proved; the front's NP implication is invalid because A/B/C certify GPC, not `S(n)≤k`.
