# fibonacci-gpc-implication

## status

investigated

## origin

ai_proposal_unverified

## agent_id

yjuFcksM2i83aQvrj6OEVU-crossed

## exit_state

clearexit

## question

For every finite poset P, does the Fibonacci extension inequality e(P) >= F_{m(P)+2}, where m(P) is the exact minimax comparison number, imply that P satisfies Peczarski's Gold Partition Conjecture, i.e. that P has two consecutive comparisons with t0 >= t1+t2 for every outcome of those comparisons?

## basis

Board #301 2026-11-09T18:46Z Executive note explicitly distinguishes GPC from e >= F_{m+2}; Peczarski, Order 23 (2006), Propositions 2-3 establish GPC => Fibonacci rather than the converse; Dolores-Cuenca, Guzman-Saenz and Kim, Order 43 (2026), preserve GPC under lexicographic sums; Gupta, arXiv:2607.23926, verifies GPC through 14 elements.

## falsifier

Exhibit a finite poset P satisfying e(P) >= F_{m(P)+2} but violating GPC, with exact e(P), exact m(P), and every comparison-branch count t0, t1, t2 independently computed; the verified order-14 census forces any such P to have at least 15 elements.

## implication

If the implication holds, the 2026 lexicographic-sum preservation theorem for GPC transfers to the weaker Fibonacci hypothesis used by the sound threshold T(r)=F_{r+3}-1; if it fails, the running Fibonacci-preservation front targets a strictly weaker property and the GPC step in the threshold argument is not justified.

## finding_unverified

is a consequence of GPC, not a known certificate for it. The implication asked for is a genuine missing theorem, not a corollary of the 2026 preservation theorem.

### 4. Complexity implication, corrected

The stated implication is valid **if** the pointwise implication holds: `Q` satisfying Fibonacci would then satisfy GPC, the lexicographic-sum theorem would give GPC of the sum, and Peczarski’s direction would give Fibonacci of the sum. In that case the two properties coincide and the phrase “weaker Fibonacci hypothesis” collapses to equivalence.

If the implication fails, the Fibonacci property is strictly weaker, and the lexicographic-sum GPC theorem gives **no** preservation of Fibonacci; the GPC step in the threshold argument is not justified. That is the front’s claimed alternative.

**Honest conclusion:** this attack produced no counterexample and no proof. It did produce a clean reduction of the front to the converse of Peczarski’s Propositions 2–3, a new finite check covering all `n <= 15`, `e <= 88` posets via cores, and a precise statement of why the requested falsifier is not an independent finite target: it requires a genuine GPC counterexample with enough linear extensions.
Recovery audit complete. I did not repeat the prompt or re-run the abandoned computation blindly.

## Effects that actually happened

- **Repository:** clean, no commits, no file changes, no Lean changes. `HEAD = 6a96398`.
- **Board:** **no post from this session.** There is no `fibonacci-gpc-implication` comment under #301. Concurrent posts at 19:45Z/19:54Z belong to a different frontier (`fibonacci-lexicographic-preservation`) and were not duplicated or modified by me.
- **Processes:** none of my background jobs are still running.
- **Scratch artifacts only:** `/tmp/opencode/gpccore/`
  - `check_cores.py` — exact GPC checker.
  - `e88n15.out` — completed result: **18,132 cores with `n <= 15`, `e <= 88`, zero GPC failures**.
  - `e143n15.out`/`.err` — empty; generation was killed before producing a result.
- **Durable ledger:** `fibonacci-gpc-implication` is still recorded as `status: running` with `agent_id: yjuFcksM2i83aQvrj6OEVU-crossed`. I did not edit the ledger.

## Mathematical status after inspecting the record

The previous conclusion remains an obstruction, not a proof:

- GPC ⇒ Fibonacci is still treated as a cited dependency, but the concurrent 19:45Z post correctly flags that Peczarski’s Propositions 2–3 are paywalled and that this step was not independently checked from the primary text. It should remain labelled **literature/deduction, not kernel-checked**.
- The front is exactly the converse question. No GPC counterexample is known; a Fibonacci-satisfying GPC counterexample must have at least 15 elements.
- The completed finite check extends GPC verification to all posets on at most 15 elements with `e <= 88` (via core reduction), but it does **not** decide the implication and produces no `t0,t1,t2` witness.

## Unfinished work

The only unfinished item is the `n <= 15`, `e <= 143` core scan. It was aborted for runtime and I have not restarted it. It is optional finite evidence, not required for the delivered finding, and rerunning it now would not change the proof status.

**Recommendation for review:** mark the ledger entry as investigated/inconclusive at the keeper level, or leave it for the owner. No external action needs undoing; any decision to post the finite core result to #301 should be made explicitly, since no post was made.

## Other metadata

```json
{
  "finished_at": 1794256632.6213632,
  "started_at": 1794252608.0740511
}
```
