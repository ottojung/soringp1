# antonina-BiYX4wNDsOzH783P1kcxgZ-bohemia

Session: ses_e3e0dc9b4ffeBJRiQIA0p7UFcB
Workspace: /home/lubko/soring-fronts/height-two-endpoint-excess-conjecture
Created: 1794255238908; updated: 1794258195537

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 595 (msg_1c21ebe2c001nFIS1a1xUQiO0x)

## Result

**The endpoint conjecture is not refuted by the board’s n=11 witness.** Its claimed exact value rests on a false disjoint-union identity. I did not prove the conjecture or find a replacement counterexample.

### Recovery / side effects

- Host: `billy-dev`; worktree `height-two-endpoint-excess-conjecture` clean at `6a96398`.
- No prior post existed for this front. I posted **one** update to #301 at `21:02:06Z`, verified as a single unique match.
- No repository, Lean, ledger, commit, or PR changes.

### Mathematical finding

The 19:29Z witness is

\[
P=(A_3\oplus A_6)\sqcup A_2,
\]

with the claimed value

\[
F(P)=F(A_3\oplus A_6)+I(9,2)=13+8=21.
\]

The step `F(K ⊔ A_2)=F(K)+I(|K|,2)` is not a valid “disjoint-union independence” theorem. Comparisons involving an isolated key can reveal a relation inside `K` by transitivity, so they can replace an internal comparison.

**Explicit counterexample to the identity** `[definition + exact computation]`: take `K=A_1⊕A_3` (`K_{1,3}`) and add `A_2`. On 6 elements,

\[
F(K)=3,\qquad I(4,2)=6,\qquad F(K\sqcup A_2)=8,
\]

so the claimed identity would give `9`, not the exact value `8`. I reproduced `F=8` with the Python exact minimax recurrence and with an independent nauty-canonicalised C++ solver.

Consequences:

- The supplied argument for `F(P)=21` is invalid, so the n=11 excess-2 witness is **not certified**.
- Direct exact evaluation of `P` did not finish: the n=11 run timed out at 20 minutes, and the natural n=10 analogue at 10 minutes. A longer run is still in progress, but it is not part of the certified result.
- The conjecture’s RHS simplifies to `1 + max_{0≤a≤n}(E(a)+E(n−a))`; at `n=11` it is exactly `1`, since Peczarski (2012) gives `S(m)=ceil(log₂ m!)` for all `m≤11`. A certified height-two excess-2 example would still refute it, but none is currently certified.

### Literature and soundness vs. completeness

- Peczarski, *Towards optimal sorting of 16 elements* (2012): `S(n)=ceil(log₂ n!)` for `n≤11`.
- Stober–Weiß, *Lower Bounds for Sorting 16, 17, and 18 Elements* (2023): `S(16)=46`, `S(17)=50`, `S(18)=54`, and `S(28)≥99`.
- The information bound `F(P)≥ceil(log₂ e(P))` is sound, and `I(9,2)=8>7` is a genuine completeness failure of that certificate. That does **not** transfer into a height-two endpoint counterexample; exact minimax completeness remains the missing ingredient.

### Honest limit

The precise obstruction is the missing certified inequality `F(P)≥21`, or a different explicit height-two poset with exact excess at least 2 at `n=11`. General-poset SUPI results and certificate soundness do not supply it.

## Output 624 (msg_1c21f3ccf001582nhPUZjR4Iv5)

The extended exact run ended without a result: it was **killed by SIGKILL**, almost certainly by memory pressure (the host was already using ~11 GB of 15 GB with several concurrent research jobs). The output file is empty, so there is still no certified value for `F((A_3⊕A_6)⊔A_2)`.

Status is unchanged:

- **Board #301:** exactly one post from this front, at `21:02:06Z`, still a single unique match.
- **Repository:** clean at `6a96398`; no commits, Lean files, or ledger edits.
- **Mathematical result unchanged:** the n=11 witness is not certified because the claimed disjoint-union identity is false; the explicit counterexample `F((A_1⊕A_3)⊔A_2)=8` versus `F(A_1⊕A_3)+I(4,2)=3+6=9` remains valid.
- **Obstruction:** a direct exact evaluation of the 11-element candidate needs more memory than was available here, or a lower-bound proof `F(P)≥21` not relying on the false decomposition.

I did not post again, since the existing board update already records the missing exact value as the obstruction and a duplicate addendum would add no mathematical content.
