# antonina-0jKofSEh8iy2lleieXApTR-loyalists

Session: ses_e0021b30fffemioBIyl33r4g9Y
Workspace: /home/lubko/soring-fronts/alternation-trading-fixed-poly-sortbound
Created: 1795294121274; updated: 1795295427519

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_1ffe5bcee001O7wFy8yjF3yYdn)

I'll start by carefully inspecting the current state, since the prompt warns that a previous turn may have performed external side effects I must not duplicate. Let me gather information in parallel.

## Output 32 (msg_1ffe5caf9001DNb75SYj6l0H0L)

I'm on billy-dev (branch `billy-dev`), working tree is clean. Now let me check durable task records, any prior work in this directory, and the board digest to see what the interrupted turn may have already done.

## Output 51 (msg_1ffe5e78f0013oFJYgx5t8HUZX)

No alternation-trading result has been posted to the board yet, and the working tree is clean. Let me check the ledger entry for this specific front, search the board for any prior post on this exact tag, and look for scratch files from the interrupted turn.

## Output 70 (msg_1ffe5fc27001G6zh9QspkT6SIH)

Let me find the exact ledger entry for this front and check for any prior result file, plus read the key problem/literature docs.

## Output 85 (msg_1ffe614a1001GCovA6YXJj4QX3)

Let me find the exact ledger record for the current front by its ID, and check its status carefully — this determines whether a prior turn already started/posted.

## Output 96 (msg_1ffe6291c0019k2FhD4usTZlmA)

The current front `alternation-trading-fixed-poly-sortbound` is `running` (claimed at ~20:48Z), with **no finding recorded, no board post, no scratch files, and a clean tree** — so the interrupted turn did not complete any external side effect beyond the initial claim. I'll proceed with the research. Let me read the core docs and literature.

## Output 111 (msg_1ffe749630013kuT6McGZxg1zp)

Let me ground the complexity-theory claims in primary literature. I'll research alternation trading and sparse-hard-set collapses.

## Output 126 (msg_1ffe760970012JyzJXLWQK2lXP)

Web search is unavailable. Let me try direct fetches of known primary sources.

## Output 141 (msg_1ffe77201001OXw3xkN1LniLYg)

Let me fetch Ryan Williams' publications page and the specific alternation-trading paper from ECCC.

## Output 156 (msg_1ffe78774001IuT206P25jCCwj)

Let me verify the sparse-hard-set collapse facts from reference sources.

## Output 171 (msg_1ffe7b984001BULsUY81Ocg5Za)

Let me check the Complexity Zoo for the tally/sparse hardness facts, particularly for PSPACE, then finalize the analysis.

## Output 182 (msg_1ffe8484b0014gcLR4PzAWy7dc)

I have the literature grounding. Now let me understand the board-posting mechanism and how prior results were posted, so I can report correctly without duplicating side effects.

## Output 220 (msg_1ffe8ff94001eLMfJkALFlV2is)

I've confirmed the recovery state and gathered the literature. Let me now write up the full argument in a scratch file (outside the repo), then report to the board.

## Output 231 (msg_1ffe9791a001DbytHdBEiJKDdi)

Let me do a final verification that no post under this exact front tag exists, then post the result once.

## Output 242 (msg_1ffe99b6f001BzTOCcACMFOq9u)

No prior post exists. Now I'll post the finding to board #301 (once) and redirect the JSON output to a file as required.

## Output 260 (msg_1ffe9f8e8001b1kst1FLlVPEmn)

The post succeeded (exit 0). Let me verify it appears exactly once on the board and then update the ledger once.

## Output 271 (msg_1ffea23db001F2eyfXawy008DZ)

Exactly one post. Now I'll update the ledger entry once (running → investigated) with the finding.

## Output 282 (msg_1ffea4150001fCnD8FcfP8Y8gC)

Let me verify the ledger persisted correctly and the repository is still clean.

## Output 293 (msg_1ffea569d0011aV3TthwNOp4Tk)

## Recovery first

Inspected before acting: billy-dev, branch `billy-dev` clean at `6a96398`, empty stash, one worktree. The front `alternation-trading-fixed-poly-sortbound` was `running` (claimed ~20:48Z) with **no finding, no board post, and no scratch files** — the interrupted turn had produced no external side effect beyond the initial claim. I did not duplicate anything: I posted **one** board comment (21:01:19.716Z) and made **one** ledger status update (`running → investigated`/`clearexit`). Repository is still clean.

## Mathematical finding — method-scope NO-GO (negative horn)

**The front's question is, under full encoding fidelity, exactly the numeric-value question.** `SORT-BOUND-U ∈ DTIME(N^c)` for fixed `c` ⟺ `S(n)` computable in `poly(n)` time (binary search on `k`; each probe `1^n#1^k` has `N ≤ n²+n+1`). So this is the numeric route in decision clothing, not a new class separation.

**Alternation trading is a class-inclusion technique, and its engine necessarily needs a completeness handle.** Its invariant template (Williams, CCC 2007, on Chandra–Kozen–Stockmeyer + time hierarchies): (i) assume `L ∈ DTIME(n^c)`; (ii) use `L`'s `≤ᵐᵖ`-completeness for a class `C` to get `C ⊆ DTIME(n^{cr})`; (iii) trade alternations for time; (iv) contradict a hierarchy theorem. Step (ii) is the *only* place a single-language assumption becomes a class-wide statement — hierarchies assert a language in `C\C'`, never a property of one language. Every published instantiation uses such a handle (SAT/QBF/complete sets).

**SORT-BOUND-U has no usable handle:**
- **NP:** sparse `≤ᵐᵖ` NP-hard ⇒ P=NP (Mahaney). An NP handle is therefore tied to an open collapse, and `NP ⊄ DTIME(n^c)` is itself equivalent to P≠NP — no unconditional bound. (This is *not* the false "NP-hard ⇒ in P".)
- **PSPACE:** unconditionally unavailable — sparse/tally `≤ᵐᵖ`-hard ⇒ `PSPACE ⊆ P` (repo's established `sort-bound-u-pspace-complete` result), contradicting P ⊊ PSPACE. Turing-hardness gives only `PSPACE ⊆ P/poly`, no known contradiction.
- **Time classes:** the method needs a near-linear reduction exponent; no `≤ᵐᵖ`-completeness for any `DTIME(n^a)`/`NTIME(n^a)` is known, and sparse-hard collapses obstruct it.

**Why sparsity is the cause:** a tally language carries one bit per length, `b(N)=[S(n(N))≤k(N)]`; a completeness handle would have to compress a whole class into `poly(N)` bits — exactly what sparse-hard-set collapses forbid without a class collapse.

**Distinctions upheld:** general-poset hardness (Hyafil–Rivest, Laber–Nogueira, Parberry) uses different models and transferring it would itself require a handle — blocked above. Soundness (`framed DAGs`, `S_eq_adv_univ`, the ATM) is not completeness; it supplies no class reduction.

**Falsification attempts that failed to break the no-go:** minimax ATM (`Θ(N)` alternations but not complete); self-reduction in `k` (subproblems are arbitrary posets, not antichains — root-forcing failure); Turing handle (only `P/poly`); insertion recurrences (known insufficient).

## Honest limits (do not mistake this for a proof)

- This is a barrier about an **informal proof family**, not a theorem quantifying over all conceivable arguments — no one can prove "no variant ever works." Proved content: the template's structure requires a handle, and none exists.
- I did **not** prove `SORT-BOUND-U ∈` or `∉ DTIME(N^c)`; `S(n)`'s time complexity remains **open**. No class separation proved.
- The PSPACE step relies on the repo's established sparse-hard collapse (not re-derived here); the time-class step is strong evidence/analogy, not a universal theorem.

Net: alternation trading is closed as a route to this single tally language; it does not fill the "no known technique" gap for `SORT-BOUND-U ∉ DTIME(N²)`. No Lean or repository changes were made — a clean worktree is the correct outcome.

## Output 312 (msg_1fff1f279001TgYTh1YwXd4kyT)

I'll re-inspect the durable state rather than repeat any action. This is verification only — no posting, committing, or ledger writes.

## Output 335 (msg_1fff21fef001hbF2jVGZuNo3Tx)

## Recovery inspection complete — no unfinished work, no duplication needed

All effects from the previous turn are present exactly once:

| Effect | Verified state |
|---|---|
| Board #301 post | **Exactly 1** post by `SoringP1 researcher: alternation-trading-fixed-poly-sortbound`, at `2026-11-21T21:01:19.716Z` |
| Ledger front | `alternation-trading-fixed-poly-sortbound`: `status=investigated`, `exit_state=clearexit`, `finished_at=1795294904.61`, finding length 1640 chars |
| Scratch artifacts | Present in `/tmp/opencode/` (`alternation_trading_no_go.md`, post body, post result; empty stderr) |
| Git | Clean on `billy-dev` at `6a96398`; empty stash; single worktree |

The front's research task was **fully completed** in the previous turn: the mathematical finding (a rigorous method-scope no-go for alternation trading on this tally language), the falsification attempts, and the honest limits were all posted and recorded. The anti-duplication instruction in this message contains no new research prompt, so there is nothing to continue.

I performed **read-only inspection only** — no board comment, no ledger write, no commit, no new scratch file. Nothing further to do; if a new research front or a correction to the posted finding is wanted, please state it explicitly and I will verify the current state again before acting.
