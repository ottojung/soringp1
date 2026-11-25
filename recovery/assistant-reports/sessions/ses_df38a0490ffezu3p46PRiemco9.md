# antonina-4zBXNPisfxDvocXZuOtPO4-parotid

Session: ses_df38a0490ffezu3p46PRiemco9
Workspace: /home/lubko/soring-fronts/first-difference-info-bound-increment-alln
Created: 1795505388481; updated: 1795505806304

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_20c760066001CQfki6ubqAecGa)

I'll start by investigating the repository state and the required documents.

## Output 21 (msg_20c760ddb001uZgIQHCguIl5Hf)

I'm on `billy-dev`, clean tree. Let me locate board #301 and the literature/operations docs.

## Output 40 (msg_20c7618e10015ui2t5l4gDKphr)

Let me check the board digest and whether this front already has prior work (resuming after possible infrastructure failure).

## Output 55 (msg_20c762bcf001ZsYZIkSppjtrIJ)

Let me check the ledger and board for any prior work specifically on this increment/first-difference front.

## Output 70 (msg_20c7659d8001cwP9vbOL9t4DpA)

The exact front is `first-difference-info-bound-increment-alln` (status `running`, no prior post/side effects). Several adjacent fronts have attacked nearly the same claim. Let me get their full findings and do my own exact computation.

## Output 90 (msg_20c76c578001sEB2pK1LAFjjP5)

This front's claim is essentially identical to the adjacent `sorting-increment-spectrum` front. I need to independently verify the math and push the falsification. Let me compute exact information-bound structure and gather published bounds.

## Output 101 (msg_20c7712e3001O0jDlSidk7xuiX)

n=25 and n=28 are confirmed "danger" points: a surplus drop 1→0 there would give d(n)=3 < floor(log₂ n)=4, refuting the claim. Let me compute exact L, Ford–Johnson upper bounds, and gather published bounds.

## Output 112 (msg_20c77451e0019myWsXiVo81Kow)

The algebra is now clear. Let me verify the literature: exact/best bounds for S(23..30), whether Ford–Johnson is truly unbeaten below 47, and any known theorem on increments d(n).

## Output 149 (msg_20c77d942001RAOOY4aEO28179)

Primary source confirms: Ford–Johnson optimality is **open** for all n<47 (only some n certified). So exact values at 25/28 are genuinely unknown. Let me check OEIS and search for any known increment theorem.

## Output 164 (msg_20c7815be001JyHf3MBfD1zySN)

Let me search the repository docs and board for any existing theorem/refutation on increment lower bounds, and check the `whole board` for the specific claim.

## Output 188 (msg_20c785b92001DMxVwcb2QRRn0T)

I've confirmed the claim is open with known data. Before finalizing, let me check the board-posting mechanism and verify there's no prior post from this exact front.

## Output 226 (msg_20c7a8348001upI3oz0y72yKkF)

There's an existing "S(n) increment density theorem" on the board. Let me read it — it may be directly relevant.

## Output 244 (msg_20c7ab0ab001BowAs5MwxYrCh1)

Let me check the repo's table of known bounds for S(n) beyond 22, and the maximal-increment theorem's full context.

## Output 259 (msg_20c7afce40017v0nyi4IlOY3gc)

I have a complete analysis. Let me post one concise finding to board #301 (the required reporting channel), then verify no repo changes.

## Output 279 (msg_20c7bca5f001I5LIGN2GMe7G6g)

## Result: honest inconclusive — the claim is open, not refuted

I studied `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, `docs/operations.md`, board #301 (recent + keyword scans across all pages), the adjacent increment/surplus fronts, and primary sources (Stober–Weiß arXiv:2206.05597; OEIS A036604/A003070; the board's Sergeev-based increment-density theorem).

### Exact reduction (deduction)

With `C(n)=⌈log₂ n!⌉`, `D(n)=S(n)−C(n)≥0`, and `ΔC(n)=C(n)−C(n−1)∈{⌊log₂ n⌋,⌈log₂ n⌉}`:

- `d(n)=ΔC(n)+ΔD(n)`. The upper side `d(n)≤⌈log₂ n⌉` is a **theorem** (sort n−1, binary-insert the nth).
- Hence the claim ⇔ `d(n)≥⌊log₂ n⌋` ⇔ **no surplus drop at a "danger" n** (where `ΔC=⌊log₂ n⌋`, including powers of two) **and no drop of size ≥2 anywhere**.
- Danger n in [2,32]: `{2,4,5,8,9,10,12,16,17,18,19,21,22,25,28,32}`; asymptotic density `log₂e−1≈0.4427`.
- Exact-arithmetic check through n=22: invariant holds throughout. The only surplus drop is `D(19)=1→D(20)=0` at **safe** n=20 (`ΔC=5=⌈log₂20⌉`), giving `d(20)=4=⌊log₂20⌋`.

### Falsifier analysis — n=25, 28, 32 are exactly the decisive probes

Refutation requires precise, currently unknown value pairs:

| n | ΔC | refuting pair |
|---|---|---|
| 25 | 4=floor | `(S(24),S(25))=(81,84)` |
| 28 | 4=floor | `(S(27),S(28))=(96,99)` (S(28)≥99 is Stober–Weiß) |
| 32 | 5 (power) | surplus drop, e.g. `(S(31),S(32))=(114,118)` |

Stober–Weiß prove only `S(28)≥99` and explicitly state it is **not known** whether any `n<47` has `F(n)>S(n)`; Peczarski's "unbeaten below 47" is restricted to split-and-merge algorithms. So no published exact value refutes the claim.

### Concrete failed approaches / exact obstruction

- Aggregate deficit `Ω(N)` cannot localize a miss; the board's density theorem gives deficit `∈{0,1}` for ≥77.87% of large n with mean `→log₂e−1` — fully consistent with the claim (which only forbids deficit ≥2).
- Sergeev's `S(n)=log₂(n!)+o(n)` is too coarse at one integer step.
- General-poset results and one-ply certificate **soundness** do not transfer to the antichain root; no completeness certificate for the negation.
- **Correction of prior board claim:** "for n=2ᵏ, d(n)≥⌈log₂ n⌉ by insertion lower bound" inverts the argument — sort-then-insert yields the **upper** bound. `d(2ᵏ)=k` is open.
- The stated complexity implication is overstated: an increment law leaves Θ(n) bits of advice, weaker than the repo's existing `SORT-BOUND-U ∈ P/log`; soundness ≠ completeness.

### Reporting

Posted one finding to Antonina #301 (verified once). **No mathematical theorem or counterexample obtained**; no Lean, repository, test, CI, ledger or branch changes — worktree clean at `6a96398` on `billy-dev`. Process success (study + post) is not a proof.

## Output 291 (msg_20c7bf375001bQrwNlHTIGc4HB)

I'll re-inspect state before doing anything else — read-only checks only.

## Output 315 (msg_20c7c4347001POUo8x0i6OvNyv)

## Recovery inspection complete — no unfinished work, no duplicate actions

**State verified (read-only checks only this turn):**

| Check | Result |
|---|---|
| Git | Clean worktree, `billy-dev`, HEAD `6a96398` — unchanged from before the investigation. No commits, no repo/Lean/test files. |
| Board #301 | **Exactly one** comment from `SoringP1 frontier: first-difference-info-bound-increment-alln`, landed `2026-11-24T07:36:09.290Z`. No duplicate post. |
| Ledger | My front is `status: running`, `finding_unverified: ""` — untouched by me (status transitions belong to the keeper). |
| Scratch | Only `/tmp/opencode/fdid/{analyze.py, post.txt, post_result.json}` — outside the repo. |

**Conclusion:** The previous turn's single external effect (the #301 report) did happen and is durable. All other steps were read-only (study, exact arithmetic, webfetch, board scans). The mathematical finding was already delivered: the claim `d(n)∈{⌊log₂n⌋,⌈log₂n⌉}` remains **open**, blocked by unknown exact `S(n)` for `n≥23` (decisive probes n=25, 28, 32), with no theorem or counterexample obtained.

I have taken **no new external action** this turn and will not re-post or edit the ledger. The only loose end is the keeper-owned ledger status (`running` → `investigated`), which I am leaving to the normal recovery machinery rather than guessing at a manual edit.
