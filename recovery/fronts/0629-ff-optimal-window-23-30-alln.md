# ff-optimal-window-23-30-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

xids7WsFCSre91YESzuNih-thrombo

## exit_state

clearexit

## question

Does there exist n in [23,30] with S(n) < FJ(n), i.e., a Ford-Johnson-optimality failure, or is the Ford-Johnson bound optimal for every n in this window?

## basis

Literature: Peczarski 2007 'The Ford-Johnson algorithm still unbeaten for less than 47 elements'; Manacher 1979; board #301 digest: FJ-C = 1 at {23,24}, 2 at 25, 3 at 28; A001768: FJ(23..30)=76,81,86,91,96,101; SW: S(28) >= 99.

## falsifier

A certified n in [23,30] with S(n) < FJ(n), or an optimal sorting tree for some n in [23,30] with height below FJ(n).

## implication

A small-n failure pins where optimal comparison counts first diverge from the FJ formula; consistent with Manacher's infinite failures (board #301: first at 47).

## finding_unverified

 | 1 | [75, 76] | iff S(23)=75 |
| 24 | 80 | 81 | 1 | [80, 81] | iff S(24)=80 |
| 25 | 84 | 86 | 2 | [84, 86] | iff S(25)∈{84,85} |
| 26 | 89 | 91 | 2 | [89, 91] | iff S(26)∈{89,90} |
| 27 | 94 | 96 | 2 | [94, 96] | iff S(27)∈{94,95} |
| 28 | 98 | 101 | 3 | [98,101] | SW: S(28)≥99 ⇒ S∈{99,100,101}; failure iff S∈{99,100} |
| 29 | 103 | 106† | 3 | [103,106] | iff S∈{103,104,105} |
| 30 | 108 | 111† | 3 | [108,111] | iff S∈{108,109,110} |

FJ digest: FJ(23..28)=76,81,86,91,96,101 (board #301 / A001768). † FJ(29), FJ(30) assumed by the +5 pattern — only 6 values are listed for the range "23..30".

**Consistency check:** FJ(n) ≥ info(n) at all n ∈ [23,30] — the claim is **not** contradicted by the info bound. Gaps FJ−info = 1 at {23,24}, 2 at {25}, 2 at {26,27}, 3 at {28} — matches the digest line "FJ-C = 1 at {23,24}, 2 at 25, 3 at 28" (interpretation: FJ-C = FJ − info).

## Attack on Claim C — attempts and outcomes
1. **Info-bound refutation:** fails — info(n) < FJ(n) everywhere in the window, so "S(n)=FJ(n)" is compatible with S(n) anywhere in [info, FJ]; no contradiction found.
2. **SW refutation at 28:** S(28) ≥ 99 (sound, exhaustive-search certificate per `docs/literature.md`) permits S(28) ∈ {99,100} < FJ(28)=101 — a *possible* failure, **not a certified one**.
3. **Literature refutation:** exact S values known for n ≤ 22 only; **S(23) is open** (literature.md). Cannot certify S(23)=75 or 76.
4. **Constructive disproof:** would need a certified S(n) < FJ(n) or a sorting tree below FJ(n) — requires computing S(n) for open n (infeasible; open problems).
5. **Literature cross-check:** consistent with Peczarski 2007 ("The Ford-Johnson algorithm still unbiased for less than 47 elements") and with the board's Manacher claim ("first at 47").

## Finding (honest)
No failure is certified in [23,30]; Claim C is **consistent with every certified bound** — consistent with "the Ford–Johnson bound is optimal for every n in this window." The window does not refute C.

## Exact obstruction / why disproving is hard
Certified bounds leave S(23)∈{75,76}, S(24)∈{80,81}, S(25)∈{84,85,86}, S(26)∈{89,90,91}, S(27)∈{94,95,96}, S(28)∈{99,100,101}; the gaps S(n)<FJ(n) are possible at the listed values but none is excluded. Disproof requires either (a) exact S(n) for an open n (n≥23, literature), or (b) a new lower bound below FJ(n) — only info bounds exist, and none dips below FJ.

## Honest limits
- S(23) is open (literature): truth of C at n=23 undetermined by available means.
- SW's gap at 28 ({99,100} below FJ(28)=101) is unclosed — C at 28 not certified either way.
- FJ digest values are taken from the board; not independently verified (no file/web access now).
- Absence of certified failure ≠ proof of optimality.
- No new Lean/repository theorem or counterexample created (per contract; clean worktree).

## Distinctions you asked for
- **General-poset vs. the S(n) family:** tournament/poset results (FJ, Manacher) don't transfer to the claim on the fixed family S(n) without a reduction (AGENTS.md model-fidelity rules).
- **Certificate soundness:** SW's S(28) ≥ 99 is sound; it *permits* a failure (99, 100 < FJ(28)=101) but doesn't *certify* one.
- **Completeness:** to prove C, need lower bounds ≥ FJ(n) for all n in the window — unavailable; "no counterexample found" is not completeness.

**Front-question answer:** No certified "S(n) < FJ(n) in [23,30]" exists; consistent with the alternative — "the Ford-Johnson bound is optimal for every n in this window."

## Other metadata

```json
{
  "finished_at": 1795232107.7095406,
  "started_at": 1795231174.7337236
}
```
