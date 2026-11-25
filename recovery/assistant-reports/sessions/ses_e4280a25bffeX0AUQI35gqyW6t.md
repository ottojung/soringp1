# antonina-YjCoxTdvcXNtLdNKbpPvit-apartment

Session: ses_e4280a25bffeX0AUQI35gqyW6t
Workspace: /home/lubko/soring-fronts/bounded-excess-self-reduction
Created: 1794180603443; updated: 1794181154634

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 276 (msg_1bd873db7001eAgV7vb2eHEjf5)

**Recovery first.** I inspected the worktree, Git state, board #301, and the durable ledger before acting. The worktree was clean at `6a96398` on `billy-dev`; there was no prior `bounded-excess-self-reduction` board post and no repository change from the interrupted turn. I posted exactly one comment (`2026-11-08T23:38:30Z`) and made no duplicate external effect. The ledger still shows `running`, which is the expected state while this session is active; I did not hand-edit it.

## Mathematical finding

The proposed self-reduction has an unconditional **information-theoretic obstruction as a black-box reduction**, although it does not disprove a reduction for the actual sequence `S`.

Let `C(n)=ceil(log2 n!)`, `E(n)=S(n)-C(n)`, and `F(n)` be the Ford–Johnson count.

**Concrete `d=0` counterexample at `n=25`.** Define profile A by matching the published exact `S` through `21`, then `S_A(22..24)=71,76,81`, and `S_A(n)=C(n)+1` for all `n≥25`. Define profile B by `S_B(m)=S_A(m)` except `S_B(25)=86` (so `S_A(25)=85`). Both satisfy:

- `C(n) ≤ S(n) ≤ F(n)`,
- `S(n+1) ≥ S(n)`,
- `S(n+1) ≤ S(n)+ceil(log2(n+1))`,
- all published exact values through 22 and certified ranges through 47.

I verified the inequalities exactly to `n=8000`. At `n=25`, `E_A(25)=1` and `E_B(25)=2`, while `E_A(m)=E_B(m)` for every `m≠25`. Hence the tightness sets `{m:E(m)≤0}` are identical, yet `S_A(25)≠S_B(25)`. Since `S(25)` is open inside `{84,85,86}`, both are legal candidates.

**Every fixed `d` fails.** Call `n` cheap if `C(n)-C(n-1)=floor(log2 n)`; there are infinitely many such indices. Starting from the admissible `E=1` profile, one can increase `E` by one exactly at cheap indices until it reaches `d+1`, using the one-bit insertion slack each time. Then choose a later cheap `n` where `E` is constant at `d+1` and `F(n)-C(n)≥d+2`, and raise `S(n)` by one. The result is two admissible profiles with `E(n)=d+1` versus `d+2`, identical at every other `m`. Thus the entire oracle `{m:E(m)≤d}` — padded sizes included — is identical, while `S(n)` differs. I checked the construction for `d=0,…,25` up to `m=8000`.

## Exact complexity obstruction

The front’s positive direction is correct: if the fixed-`d` oracle is in `P`, then `S_unary∈FP`.

But the negative direction is not available as stated. If `S_unary∈FP`, a polynomial-time reduction exists trivially by ignoring the oracle. Therefore proving that **no** polynomial-time reduction exists is at least as strong as proving `S_unary∉FP`, which implies `SORT-BOUND-U∉P` and hence `P≠PSPACE`, since `SORT-BOUND-U∈PSPACE` is already established. So the profile theorem is a black-box/relativized barrier, not a separation.

There is also a sharp model boundary: if `d` were allowed to vary, binary search over `0≤E(n)≤F(n)-C(n)=O(n)` would compute `E(n)` exactly with `O(log n)` queries. The fixed-`d` restriction is precisely what discards all excess information above `d`.

## Soundness versus completeness, general posets

A query `E(m)≤d` is a sound upper-bound certificate for `S(m)≤C(m)+d`; its negation is a sound lower bound. It is not complete: a true answer leaves `d+1` possible values, and only `d=0` pins `S(m)=C(m)`. General-poset excess results about `C_m ⊔ A_{n-m}` or bulk-insertion states concern `F(P)` at intermediate states, not the antichain root, and do not transfer to `E(n)`. The board’s `E≤1` promise is the exact repair: under that promise, one tightness query gives `S=C+1_{n∉T}`. Without it, `T` does not encode `S`.

## Honest limit

This is a paper proof of **non-identifiability of the fixed-`d` oracle over profiles consistent with all published constraints**, plus a complexity-theoretic obstruction to the claimed negative implication. It is not a proof that the actual `S` is not reducible to bounded-excess queries; that would require a new lower bound on `S`. No Lean, repository, test, or PR change was made.

## Output 315 (msg_1bd87b6680014Rratgsck9hP62)

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
