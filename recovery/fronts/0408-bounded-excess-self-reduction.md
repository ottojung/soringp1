# bounded-excess-self-reduction

## status

investigated

## origin

ai_proposal_unverified

## agent_id

YjCoxTdvcXNtLdNKbpPvit-apartment

## exit_state

clearexit

## question

Is exact S(n) polynomial-time Turing reducible to the bounded-excess predicates E(m)<=d for a fixed d, where E(m)=S(m)-ceil(log2 m!) and m ranges over n together with polynomially many padded sizes?

## basis

Board #301 single-bit-excess-dichotomy and info-tightness-set-complexity, bulk-insertion-information-defect, and the unary threshold equivalences in docs/problem.md; unlike those fronts, no boundedness of E is assumed here.

## falsifier

Construct a polynomial-time reduction with explicit query and correctness bounds, or prove that two admissible excess profiles agree on every bounded-excess query at all padded sizes yet give different S(n).

## implication

If the reduction exists, a polynomial-time decider for constant excess yields exact S(n) and hence SORT-BOUND-U in P; if not, bounded-excess evaluation is provably weaker than exact evaluation.

## finding_unverified

e oracle `{m:E(m)≤d}` — padded sizes included — is identical, while `S(n)` differs. I checked the construction for `d=0,…,25` up to `m=8000`.

## Exact complexity obstruction

The front’s positive direction is correct: if the fixed-`d` oracle is in `P`, then `S_unary∈FP`.

But the negative direction is not available as stated. If `S_unary∈FP`, a polynomial-time reduction exists trivially by ignoring the oracle. Therefore proving that **no** polynomial-time reduction exists is at least as strong as proving `S_unary∉FP`, which implies `SORT-BOUND-U∉P` and hence `P≠PSPACE`, since `SORT-BOUND-U∈PSPACE` is already established. So the profile theorem is a black-box/relativized barrier, not a separation.

There is also a sharp model boundary: if `d` were allowed to vary, binary search over `0≤E(n)≤F(n)-C(n)=O(n)` would compute `E(n)` exactly with `O(log n)` queries. The fixed-`d` restriction is precisely what discards all excess information above `d`.

## Soundness versus completeness, general posets

A query `E(m)≤d` is a sound upper-bound certificate for `S(m)≤C(m)+d`; its negation is a sound lower bound. It is not complete: a true answer leaves `d+1` possible values, and only `d=0` pins `S(m)=C(m)`. General-poset excess results about `C_m ⊔ A_{n-m}` or bulk-insertion states concern `F(P)` at intermediate states, not the antichain root, and do not transfer to `E(n)`. The board’s `E≤1` promise is the exact repair: under that promise, one tightness query gives `S=C+1_{n∉T}`. Without it, `T` does not encode `S`.

## Honest limit

This is a paper proof of **non-identifiability of the fixed-`d` oracle over profiles consistent with all published constraints**, plus a complexity-theoretic obstruction to the claimed negative implication. It is not a proof that the actual `S` is not reducible to bounded-excess queries; that would require a new lower bound on `S`. No Lean, repository, test, or PR change was made.
Recovery audit complete — I did **not** repeat the prompt or create any new external effect.

## Effects that actually happened

- **Board #301:** exactly **one** post from this front exists, at `2026-11-08T23:38:30Z`, author `SoringP1 frontier: bounded-excess-self-reduction`. No duplicate.
- **Repository:** worktree clean on `billy-dev` at `6a96398`; no commits, edits, stashes, Lean files, or tests.
- **Scratch only:** `/tmp/opencode/bounded-excess-self-reduction-post.md`, `...-post-result.json`, and `profile_check.py`, outside the repository.
- **Durable ledger:** `bounded-excess-self-reduction` remains `status: running`, `exit_state: None`, `finding_unverified: None`. This is the expected keeper-managed active-agent state; I did not edit it manually.

## Unfinished work

None. The mathematical investigation and the single board report were already completed before the interruption.

The recorded result stands:

- for every fixed `d`, two profiles satisfying all published necessary constraints can have identical entire bounded-excess oracles `{m:E(m)≤d}` but different `S(n)`;
- concrete `d=0`, `n=25` witness: profiles with `S(25)=85` and `S(25)=86` have the same tightness set `T`;
- padding cannot help, since the oracle sets agree at every `m`;
- the claimed negative implication “no reduction ⇒ bounded-excess evaluation weaker than exact” would require at least `S_unary∉FP`, hence `P≠PSPACE`;
- this is a black-box non-identifiability/barrier result, **not** a proof that the actual `S` is non-reducible.

No uncertain external effect remains.

## Other metadata

```json
{
  "finished_at": 1794181186.58504,
  "started_at": 1794180602.5725496
}
```
