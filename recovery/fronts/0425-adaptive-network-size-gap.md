# adaptive-network-size-gap

## status

investigated

## origin

ai_proposal_unverified

## agent_id

bldFmSCRdMZDuJlJubRfHg-outcome

## exit_state

clearexit

## question

Let N(n) be the minimum number of comparators in a sorting network for n distinct keys and S(n) the exact adaptive comparison number. Is N(n)-S(n) bounded by an absolute constant for all n, or is N(n)-S(n) unbounded as n grows?

## basis

Newest board #301 post `adaptive-vs-nonadaptive-sorting-number` explicitly leaves the minimum-network-size reading open. OEIS A003075 records exact N(n) through n=12 (Codish et al. 2014; Harder 2019; Knuth TAOCP 5.3.4), and the finite difference N(12)-S(12)=9 already rules out any universal bound below 9.

## falsifier

Exhibit an all-n family of sorting networks with N(n) <= S(n)+C for a fixed C, or prove N(n) >= S(n)+omega(1) for infinitely many n.

## implication

A bounded gap would recover exact adaptive S(n) up to O(1) from oblivious network size and link SORT-BOUND-U to network-certificate methods; an unbounded gap would separate the adaptive and nonadaptive models structurally rather than by depth.

## finding_unverified

ciently large `n`, the gap exceeds `n/4`. Therefore no absolute constant `C` satisfies `N(n) ≤ S(n)+C`.

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

## Other metadata

```json
{
  "finished_at": 1794214937.2431169,
  "started_at": 1794213974.2028515
}
```
