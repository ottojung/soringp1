# antonina-bldFmSCRdMZDuJlJubRfHg-outcome

Session: ses_e40836b36ffeFHzBviWLfY31p1
Workspace: /home/lubko/soring-fronts/adaptive-network-size-gap
Created: 1794213975361; updated: 1794214928368

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 20 (msg_1bf7ca98a001VBUumY86F2ZLCr)

I'll start by inspecting the existing state before doing anything external.

## Output 397 (msg_1bf8541ca001GxmXX9jtUJ7M88)

I found no prior board post for this front and no repository changes. Let me verify the key asymptotic ingredients numerically once more, then post a single scoped finding.

## Output 567 (msg_1bf89b58e001lNCvV04YJxeGgw)

## Recovery and side effects

- Host: `billy-dev`; worktree clean at `6a96398`; no commits or file changes.
- Board #301 pages 1–3 had **no prior post** for `adaptive-network-size-gap` (also searched `A003075`, `Van Voorhis`, `bounded gap`, `N(n)`).
- I posted exactly once: author `SoringP1 frontier: adaptive-network-size-gap`, `2026-11-09T08:58:58.730Z`, message `sha256:NC0G7TP…`. The ledger remains `running`; the keeper closes it on agent exit. No repo/Lean changes.

## Mathematical finding

The front’s bounded-gap hypothesis is **false**. In fact

```text
N(n) − S(n) ≥ 0.3289·n − O(log² n),
```

so `N(n) − S(n)` is unbounded, indeed linear. This is the **minimum-network-size** reading, not the depth reading.

The proof is a deduction from two published bounds:

1. **Van Voorhis (1972)**, *An Improved Lower Bound for Sorting Networks*, IEEE Trans. Computers C-21(6):612–613:
   ```text
   N(n) ≥ N(n−1) + ⌈log₂ n⌉.
   ```
   Iterating with `N(1)=0`,
   ```text
   N(n) ≥ V(n) := Σ_{k=1}^n ⌈log₂ k⌉.
   ```
   For `n ∈ (2^{m−1}, 2^m]`, `V(n)=mn−2^m+1`. Writing `x=n/2^m∈(1/2,1]`,
   ```text
   V(n) − (n log₂ n − n) = 2^m[x(1−log₂ x)−1] + 1 ≥ 1,
   ```
   because `x(1−log₂ x) ≥ 1` on `[1/2,1]`. Hence
   ```text
   N(n) ≥ n log₂ n − n + 1.        (1)
   ```

2. **Ford–Johnson (1959)**; Knuth, *TAOCP* Vol. 3, §5.3.1; OEIS A001768. Merge-insertion sort has worst-case comparison count
   ```text
   S(n) ≤ C(n) := Σ_{k=1}^n ⌈log₂(3k/4)⌉.
   ```
   Grouping `k` by `j=⌈log₂(3k/4)⌉` gives, with `m=⌈log₂(3n/4)⌉`, `B_j=(4/3)2^{j−1}`, and `θ=4·2^m/(3n)∈[1,2)`,
   ```text
   C(n) = mn − (4/3)2^m + O(log² n)
        = n[log₂ n + log₂ 3 − 2 + log₂ θ − θ] + O(log² n).
   ```
   Since `max_{θ∈[1,2)}(log₂ θ−θ) = −0.913929…` at `θ=1/ln 2`, and `2−log₂3=0.415037…`,
   ```text
   C(n) ≤ n log₂ n − 1.32896…·n + O(log² n).        (2)
   ```
   So
   ```text
   S(n) ≤ n log₂ n − 1.32896…·n + O(log² n).
   ```

Subtracting (2) from (1):

```text
N(n) − S(n) ≥ 0.32896…·n − O(log² n) → ∞.
```

For all sufficiently large `n`, the gap exceeds `n/4`. Therefore no absolute constant `C` satisfies `N(n) ≤ S(n)+C`.

## Finite corroboration

Using exact `N(n)` through 12 (OEIS A003075; Harder), exact `S(n)` through 22 (OEIS A036604; Peczarski, Stober–Weiss), and Van Voorhis lower bounds for `N(13)…N(22)`, the known gaps are

```text
n:      12 13 14 15 16 17 18 19 20 21 22
gap:     9  9  9  9  9 10 11 12 13 14 14
```

The finite data is consistent with the theorem but is not used in the proof; `N(12)−S(12)=9` alone only rules out constants below 9.

## Soundness vs completeness

- **Soundness:** a network of size at most `k` does certify `S(n) ≤ k`, since `S(n) ≤ N(n)`.
- **Completeness fails:** when `k=S(n)` but `N(n)>S(n)`, no network of size `k` exists. Since the gap is linear, this happens for every sufficiently large `n`. Thus network-size certificates are sound but linearly incomplete for `SORT-BOUND-U`.
- This is **not** an NP/coNP or P/PSPACE statement. Verifying that a candidate network sorts is itself a separate coNP-complete problem, and the result gives no new bound on computing `S(n)` or `N(n)`.
- This is not a general-poset result; it uses the fixed antichain/network model.

## Honest limits

The result is a **deduction** from two published bounds, not a new lower-bound technique, and the constant `0.3289` is not optimized. I did not reprove Van Voorhis’s one-step lemma; I checked its statement in the primary abstract and its finite consequences against exact network values. The attempted opposite route—converting an optimal adaptive tree into a network with only `O(1)` extra comparators—has no general construction, and the linear lower bound above rules it out. General decision-tree bounds such as `log₂(n!)` are insufficient here because they sit a linear amount below both `N(n)` and the Ford–Johnson bound in the needed direction.

## Output 638 (msg_1bf8b0371001WdcgKbcA84KFHy)

**Recovery check complete — no duplicate external action taken.**

Inspected state:

- Host: `billy-dev`; worktree clean at `6a96398`; no commits or file changes.
- Board #301: exactly **one** post for `adaptive-network-size-gap` on pages 1–3:
  - author `SoringP1 frontier: adaptive-network-size-gap`
  - `2026-11-09T08:58:58.730Z`
  - `sha256:NC0Gt7TPqshFTvtwcz5uO5cCVrNmx_zH8ns4eXgP62g`
- No second post under `Van Voorhis`, `0.3289`, `bounded-gap`, or `A003075`.
- Ledger entry remains `status: running` with no `finding_unverified`. That is keeper-managed and should be closed on agent exit; I did not edit it manually.
- No new durable note or repository change was created after the post.

The previous turn therefore completed its only external effect exactly once. The repeated recovery prompts require **no new work**, and I did not re-post.

**Mathematical status (already reported):**

The front’s bounded-gap hypothesis is false. Using

- Van Voorhis (1972): `N(n) ≥ N(n−1) + ⌈log₂ n⌉`, hence `N(n) ≥ n log₂ n − n + 1`;
- Ford–Johnson (1959) / Knuth §5.3.1 / OEIS A001768: `S(n) ≤ Σ_{k=1}^n ⌈log₂(3k/4)⌉ ≤ n log₂ n − 1.32896…·n + O(log² n)`,

we get

```text
N(n) − S(n) ≥ 0.32896…·n − O(log² n) → ∞.
```

So the gap is linear, not bounded. Network-size certificates are sound for `S(n) ≤ k` but linearly incomplete; this gives no NP/P/PSPACE result and no new algorithm for `S(n)`. The proof is a deduction from published bounds, not a new lower-bound technique.

Uncertainty for review: only the ledger’s `running` flag, which is expected to be resolved by the keeper rather than by another board post or manual edit.
