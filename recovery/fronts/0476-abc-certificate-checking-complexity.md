# abc-certificate-checking-complexity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Kzb8WYKQUfD57IZWHe7HbX-hunted

## exit_state

clearexit

## question

Given a height-two poset P and a candidate Peczarski A/B/C witness, can the three exact linear-extension-count inequalities be verified in polynomial time, or is that verification #P-hard even when the witness elements are supplied and no count table is trusted?

## basis

Peczarski, Order 23 (2006) 89-95, facts restated in Contrib. Discrete Math. 12 (2017); Gupta arXiv:2607.23926 sec. 5.1; Dittmer-Pak arXiv:1802.06312 (#P-complete height-two extension counting); board #301 certificate-disjoint-union-closure (22:37Z).

## falsifier

A polynomial-time exact verifier for the A/B/C count inequalities on all height-two posets, or a #P-hardness reduction from counting height-two linear extensions to those inequalities given the witness.

## implication

A polynomial-time verifier would turn the A/B/C family into a locally checkable certificate route toward NP membership for SORT-BOUND-U; #P-hardness would show that GPC certificate soundness does not imply polynomial-time checkability and would block that route.

## finding_unverified

1)=−4`. The refined guess "the 1-slave incomparable regime is always negative" is also false (`D=12` example). Both signs genuinely occur in the only residual regime.

**4. The exact obstruction to hardness.** The standard route from `#H2LE` (Dittmer–Pak) to the sign is blocked: ordinal sum and disjoint union multiply both `e(P+xy)` and `e(P+yx)` by the same positive factor, so `sign(D)` is invariant and padding/duplication can never expose a count through the sign. Same invariance holds for the whole A/B/C inequality.

## Honest verdict
- **No** polynomial-time exact verifier was found; **no** #P-hardness reduction was found. The front's dichotomy remains open, now sharply localised to `|U(x)\U(y)|=1`, `U(y)⊄U(x)`.
- The claimed complexity implication is **invalid independently of the counting question**: A/B/C are sufficient conditions for **GPC** (a good opening comparison), not for `F(P)≤k` or `S(n)≤k`; even a poly verifier plus completeness would not yield an NP certificate for `SORT-BOUND-U`. A/B/C are also still not known complete.
- Process success is not a proof: the only unconditional new theorem is the nested-upper-set result; everything else is exact-computation evidence or a barrier.
I'll verify state before doing anything, since the previous turn already posted. No new external actions will be taken unless something is genuinely unfinished.
Git is clean and the board has exactly one post for this front. Let me confirm that post was not truncated by the backend failure (read-only).
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

## Other metadata

```json
{
  "finished_at": 1794270380.6336095,
  "started_at": 1794268451.9693656
}
```
