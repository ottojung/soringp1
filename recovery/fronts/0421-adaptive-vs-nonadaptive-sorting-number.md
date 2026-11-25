# adaptive-vs-nonadaptive-sorting-number

## status

investigated

## origin

ai_proposal_unverified

## agent_id

IVh02KRbtzjyOMkrf3ouxC-unwounded

## exit_state

clearexit

## question

Does the adaptive comparison-sorting number S(n) equal the nonadaptive (sorting-network-depth) number up to an additive O(1) for all n, or does adaptation yield an unbounded per-n saving?

## basis

docs/problem.md distinguishes adaptive decision trees from sorting networks; prior fronts stayed within adaptive S(n).

## falsifier

A single n where the optimal nonadaptive network depth exceeds the adaptive S(n) by more than a fixed constant, or a proof that the gap is O(1) for all n.

## implication

An unbounded gap would separate adaptive decision trees from nonadaptive networks as complexity measures for S(n); O(1) would collapse the two models for exact evaluation.

## finding_unverified

wer.
- No single n in the known exact-value tables (n ≤ 22 for S; network depth tables) is accompanied by a verified nonadaptive optimum under a stated definition, so the falsifier (one n with nonadaptive depth > S(n)+C) cannot be honestly exhibited here.

### Classification

- **Conjecture/open:** under the nonadaptive-decision-tree reading, whether the gap D(n) − S(n) is O(1) is open and not settled by available literature.
- **Model-fidelity issue:** the front's wording ("sorting-network-depth") does not match the defined S(n) model; per AGENTS.md model-fidelity rules, this must be resolved before any theorem.

### Next decisive step

Reformulate the front with an explicit nonadaptive model (fixed comparison schedule vs. network depth) and a stated measure (comparison count vs. layers), then either exhibit a verified small-n counterexample or prove the two coincide up to O(1). Until then, no Lean or repository change is warranted.
## Recovery status (checked before acting)

- **Worktree:** clean at `6a96398`; no commits, no files added/modified.
- **Durable record:** ledger entry `adaptive-vs-nonadaptive-sorting-number` was still `running`, with **no** `finding_unverified`. So the prior turn completed only reading, not the board report.
- **Board #301:** searched pages 1–3 for the front ID — **no prior post existed**. I posted exactly once (message `sha256:Tr-CU3YI…`, 2026-11-09T05:09:10Z). No duplicate.

## Mathematical finding

**The front as written is a model mismatch; under its literal depth reading the additive-O(1) claim is false, with the gap diverging in the opposite direction.**

- `S(n)` is a **sequential** worst-case comparison count: `S(n) ≥ log₂(n!) = Ω(n log n)`.
- Sorting-network **depth** `D(n)` is **parallel layers**: an explicit Batcher odd-even mergesort has depth `O(log² n)`.
- Therefore `S(n) − D(n) → ∞`; a depth-`d` network also does at most `(n/2)d` comparators total and compares each element at most `d` times. So "nonadaptive depth exceeds `S(n)` by a constant" is false for large `n`, not true.

**Well-posed reading remains open.** If "nonadaptive number" means minimum network **size** `N(n)` (length of a fixed oblivious comparison sequence), then `N(n) ≥ S(n)` trivially and `N(n) − S(n) = O(1)?` is a genuine all-`n` question. I did **not** prove or refute it. The verified data (OEIS A036604/A003070) tabulate adaptive `S(n)` and `⌈log₂ n!⌉`, not `N(n)`; finite small-`n` gaps cannot establish unboundedness.

## Honest limits

- No new theorem about `S(n)` itself; this is a **model-fidelity deduction** plus a front reformulation, not a separation of adaptive vs nonadaptive power.
- No counterexample or all-`n` proof for the size reading.
- No Lean, repo, commit, or test changes; only one board comment. The ledger stays `running` for the keeper to close on agent exit.
## Recovery check complete — no further action

- **Worktree:** clean at `6a96398`; no uncommitted changes.
- **Board #301:** exactly **one** post for this front exists (the 05:09:10Z message `sha256:Tr-CU3YI3hnq9c291wOapiq0w6Jp3grorn6H8O6fprc` by `SoringP1 frontier: adaptive-vs-nonadaptive-sorting-number`). No duplicate to make.
- **Ledger:** still `running` with no `finding_unverified`; the keeper records completion on agent exit. This is expected and not something to edit by hand.
- **No repo/Lean/commit changes** were made at any point.

The investigation is already reported; nothing remains unfinished. Reporting only, no repeated side effects.

## Other metadata

```json
{
  "finished_at": 1794201013.5624647,
  "started_at": 1794200760.6425986
}
```
