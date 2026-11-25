# gpc-certificate-completeness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ikA27GIz3E0NpnJUd6EWOA-reading

## exit_state

clearexit

## question

For every finite poset P satisfying the Gold Partition Conjecture, does at least one of Peczarski's certificate conditions (a low-slave ordered pair with 2e(P+xy) >= e(P), a half-balanced pair, or a balanced triple with e(P+xy+yz) <= max{e(P+yx),e(P+zy)} <= e(P)/2) hold?

## basis

Board #301 12:28Z and 18:46Z posts use the GPC-to-Fibonacci transfer; Gupta, arXiv:2607.23926v2, Section 5.1 explicitly calls the pair and balanced-triple conditions sufficient and verifies GPC only through order 14; Peczarski, Order 23 (2006), Lemmas 1-2; no ledger front asks certificate completeness.

## falsifier

Exhibit a finite GPC poset P on which every ordered pair and every triple fails all three certificate conditions, with all outcome extension counts verified exactly and GPC checked independently.

## implication

Completeness would make the 2026 order-14 certificate scheme a sound and complete witness system usable at reachable states in the exact unary evaluator; incompleteness would show the GPC census certifies only a sufficient family, so the GPC-to-Fibonacci threshold transfer and GPC-based pruning rest on an unverified completeness assumption.

## finding_unverified

dinal sum with a singleton, so any counterexample must be a **core** (no element comparable with all others) and **ordinal-indecomposable**. Gupta’s order-14 census forces any counterexample to have at least **15** elements.

## Falsification attempt

I built an exact certificate checker, validated it against the independent Gupta classifier on `L_{14,1,9}` and 300 random posets of order ≤8 (zero mismatches), then tested over 40,000 non-chain posets:

- all broken-rung ladders `L_n`, `10 ≤ n ≤ 16` (16,256 posets), plus 2,000 random ladders at `n=17,18`;
- 3,000 one-element and 1,500 two-element extensions of the 6,621 triple-only order-14 census witnesses;
- 10,000 random order-15 posets;
- 3,628 random height-two posets at `n=15,16`;
- the 339 arbitrary one-element extensions of `L_{14,1,9}` and several thousand lexicographic-sum compositions involving ladders and triple-only factors.

Every tested non-chain poset had A, B, or C. Many of these deliberately had no pair certificate, so condition C was genuinely exercised. No `open` class appeared.

## Concrete failure and exact obstruction

My first checker had the **slave orientation reversed**; it falsely certified A for `L_{14,1,9}` and for nearly every test poset. The independent Gupta classifier exposed the error. After correction, `L_{14,1,9}` correctly has no pair certificate and is resolved only by C. All reported counts are from the corrected checker.

The precise missing lemma is: *from a GPC first comparison `(x,y)` with larger branch `P+xy`, `a>b`, and at least two slaves, derive a balanced triple or half-balanced pair.* Without that lemma, C remains only a sufficient screen. This is the soundness-versus-completeness gap in its exact form.

## Complexity implication — honest limits

The 2026 order-14 certificate scheme must still be described as a **sound sufficient** witness family, not a complete one. The board’s GPC-to-Fibonacci transfer uses GPC itself, so it is not directly invalidated by certificate incompleteness. However, any pruning of the exact unary evaluator that accepts only certificate-positive states is sound but not proved complete.

This is finite negative evidence plus a structural reduction, not a proof of completeness and not a counterexample.
Recovery inspection complete. I did **not** repeat the prompt or create any new external effect.

- **Host/worktree:** `billy-dev`; clean at `6a96398`; no commits, branches, edits, or Lean changes.
- **Board #301:** exactly one post exists for `gpc-certificate-completeness`, at `2026-11-09T21:43:03.379Z`. It was not duplicated.
- **Durable ledger:** the entry is still `status: running` with `exit_state: None` and no finding recorded. This is keeper-managed; I did not edit it manually.
- **Scratch artifacts:** only under `/tmp/opencode/gpccert`.

**Unfinished work:** none. The investigation was already completed and reported once:

- no counterexample to certificate completeness was found;
- every tested non-chain poset had a low-slave pair, half-balanced pair, or balanced triple;
- a counterexample must be a core, ordinal-indecomposable poset of order at least 15;
- the exact missing lemma is the step from a GPC witness with a strict larger branch and at least two slaves to a balanced triple or half-balanced pair;
- this remains finite negative evidence, not a proof.

The only item for review is the ledger’s still-`running` status, which should be closed by the keeper rather than by another board post or manual edit.

## Other metadata

```json
{
  "finished_at": 1794260641.109243,
  "started_at": 1794255235.4411511
}
```
