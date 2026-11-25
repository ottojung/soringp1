# first-difference-info-bound-increment-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

4zBXNPisfxDvocXZuOtPO4-parotid

## exit_state

clearexit

## question

Is the exact sorting number increment d(n)=S(n)-S(n-1) always in {floor(log2 n), ceil(log2 n)} for all n>=2, i.e. does the surplus D(n)=S(n)-ceil(log2 n!) never drop by two, nor drop by one at an n where ceil(log2 n!)-ceil(log2(n-1)!) equals floor(log2 n)?

## basis

A fresh check of known S(1..22) values is consistent with the invariant; binary insertion gives the upper side; D(n)=o(n) (Sergeev) and the excess-sequence P-recursive collapse make the lower side nontrivial.

## falsifier

Find n>=23 where a surplus drop 1->0 (or of size >=2) at a dangerous n with information-increment floor(log2 n) forces d(n) <= floor(log2 n)-1; natural probes are n=25 and n=28, where S is still open.

## implication

If true this gives a local-update recurrence S(n)=S(n-1)+floor/ceil(log2 n), constraining any exact evaluator and enabling a compact increment certificate for the unary threshold language.

## finding_unverified

** (where `ΔC=⌊log₂ n⌋`, including powers of two) **and no drop of size ≥2 anywhere**.
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
I'll re-inspect state before doing anything else — read-only checks only.
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

## Other metadata

```json
{
  "finished_at": 1795505857.4248662,
  "started_at": 1795505387.602773
}
```
