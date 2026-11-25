# antonina-pDL1gQIc4d2iQZ6k6KFrRv-however

Session: ses_e3eaf43afffeZjt4LoCg56kAU9
Workspace: /home/lubko/soring-fronts/curator
Created: 1794244656234; updated: 1794246497833

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_1c150c68b001z8t68Y8J9qJiCH)

I'll start by inspecting the current state: working directory, git, board, and prior scratch artifacts.

## Output 437 (msg_1c1643536001ykFKtdtEwxOGO2)

I have enough to decide. Let me write the candidate file and validate its schema/lengths.

## Output 455 (msg_1c164ca88001MtIu05HSTMJ39i)

State inspected before acting: host `billy-dev`; worktree clean at `6a96398`; no prior `frontier-candidates.json`; ledger has the newest fronts `merge-block-ratio-alln-inequality`, `universal-local-excess-cover-ratio`, and `height-two-excess-unbounded` still running; board #301 shows the 17:12Z KWŁ and 16:14Z merge-block n=9 posts as the newest results. I did not repeat any post, commit, or Lean action.

**Actual effects:** exactly one file was created, `frontier-candidates.json` (untracked, the curator deliverable). No board comment, branch, commit, or repository edit.

**Research attempt (honest).** I attacked the quantitative height-two excess law implied by the newest thread:
`F(P)-ceil(log2 e(P)) ≤ 1 + max_{a+b=n}(E(a)+E(b))`, with `E(m)=S(m)-ceil(log2 m!)`.
- Definition/deduction: ordinal-sum additivity gives `F(A_m (+) A_m)=2S(m)`, hence excess `2E(m)+floor(2·delta_m)`, where `delta_m=ceil(log2 m!)-log2 m!`. This reproduces the board’s `2` at `m=12` and `3` at `m=14`.
- Experiment: independent exact height-two enumeration through `n=6` (using the repository’s `minimax`/`linear_extensions`, not the board’s values) gives maximum excess `1`, attained at `n=6` where `E(6)=0`; the proposed bound is also `1`. No counterexample through `n=6`.
- Honest limit: the `n=7` labelled height-two enumeration contains `227,893` representatives and the exact-minimax pass did not finish inside the time budget, so I did **not** test the first possible small counterexample site. No all-`n` proof and no counterexample is claimed.

**Consequence for the running frontier.** The easy direction is already known: `A_m (+) A_m` shows unbounded `E` forces unbounded height-two excess. The proposed split bound would give the converse, so `height-two-excess-unbounded` would become equivalent to the blocked global excess question rather than an independent route. That is a reason not to propose another “height-two excess bounded?” front.

**Soundness vs completeness.** The leaf-count bound `ceil(log2 e(P))` is a sound lower bound, not a complete certificate; the split law is an incompleteness/extremal statement, not a completeness theorem. The F-versus-S front is a reduction question, not a certificate claim. General-poset facts are not asserted to transfer to the antichain root.

**Proposed fronts (new, non-duplicate):**
1. `height-two-excess-split-bound` — the quantitative split law above; falsifiable at any `n` by an exact height-two counterexample.
2. `height-two-f-s-turing-equivalence` — whether all-height-two exact `F` is polynomial-time Turing equivalent to the unary sequence `S`; the ledger’s own height-two finding names this two-way reduction as its next target, and `S(n)=1+F(C2 ⊔ A_{n-2})` supplies only one direction.

I deliberately did not propose more merge-block, 2-WL, or “height-two excess bounded/unbounded” fronts: those are covered by the running or investigated entries. No new external primary source was added; the literature used is the audited baseline in `docs/literature.md` and `docs/research-hardness-boundaries.md` (Peczarski, Stober–Weiß, Wells, Cardinal et al., Dittmer–Pak), and web lookup was unavailable this turn.

`frontier-candidates.json` is written and schema-validated (2 fronts, all field-length and slug constraints pass).

## Output 580 (msg_1c16cbc98001rGuJ2637fyYuv7)

Inspection complete; no duplicate effects were performed.

**What actually happened (verified)**
- Worktree: clean at `6a96398`, with the single untracked deliverable `frontier-candidates.json`.
- Board #301: no comment exists for either proposed front; the newest board message is the 17:22Z Executive check. No post was made or repeated.
- Ledger: 452 fronts; the curator entry is still `started_at`/`running` with no finding — keeper reconciliation state, not a missing research action. No manual ledger edit.
- No commit, branch, Lean file, or repository edit exists.

**Unfinished work continued: only the `n=7` check**
The previous turn left the `n=7` height-two enumeration unfinished. I completed it using `genbg` over normalized bipartitions plus the antichain: `163` normalized representatives, all exact-`F`/`e` checks run, with one safely pruned by `C(P) >= 12` because `F <= S(7)=13` then forces excess `<= 1`.
- Result: maximum excess at `n=7` is `1`, equal to the proposed bound `1 + max_{a+b=7}(E(a)+E(b)) = 1` since `E(7)=0`.
- No counterexample to `height-two-excess-split-bound` at `n<=7`; `n>=8` remains open. This is experiment only, not proof.

I updated the front’s `basis` from “through n=6” to “through n=7”. The JSON revalidated: two fronts, `height-two-excess-split-bound` and `height-two-f-s-turing-equivalence`, all schema and length constraints pass.

No further side effects are needed. The only durable-record item is the curator ledger entry still showing `running`, which should be reconciled by the keeper rather than hand-edited.
