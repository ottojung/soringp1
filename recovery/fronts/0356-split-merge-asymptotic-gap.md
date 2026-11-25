# split-merge-asymptotic-gap

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Iy2Ww5fTz5zCwjnFTv1LR5-tumbler

## exit_state

clearexit

## question

For the optimal split-merge recurrence R(n) = min over a+b=n of R(a) + R(b) + M(a,b), where M(a,b) is the exact two-list merge number, is R(n) - S(n) unbounded, or does this restricted architecture attain S(n) infinitely often?

## basis

Independent exact minimax computation of M(a,b) for a+b <= 11 and substitution into the split-merge recurrence, compared with the documented S(1..11), gives gaps 0,0,0,1,1,1,1,2,2,2 for n = 2..11, with the first failure at n = 5; merge-number ranges are discussed in docs/research-structural-lower-bounds.md, and no all-n asymptotic gap or equality theorem is recorded there.

## falsifier

Prove a uniform bound R(n) - S(n) = O(1), or exhibit infinitely many n for which the split-merge architecture reaches S(n); alternatively give exact merge values that invalidate the stated recurrence.

## implication

An unbounded gap would rule out every algorithm that independently sorts two blocks and then merges them, including binary insertion and balanced divide-and-conquer, as an exact evaluator of S(n), and would quantify the advantage of Ford-Johnson-style interleaving; a bounded gap would revive a polynomial-time merge recurrence.

## finding_unverified

`n=2..11`. The first failure is indeed `n=5`.
- Extending the exact recurrence: `R(12)=32` while `S(12)=30`, so gap `2`. Using exact `M(4,9)=11`, `M(5,8)=12`, and the certified linear-range value `M(6,7)=12`, also `R(13)=36` versus `S(13)=34`, gap `2`. The architecture does not recover equality at 12 or 13.
- Since every merge satisfies `M(a,b) ≥ ceil(log2 C(a+b,a))`, one has `R(n) ≥ L(n)` for the recurrence `L` with information-bound merges. Exact integer computation gives
  `L(10922)=131640`, while the Ford–Johnson bound is `FJ(10922)=131071`.
  Since `S(n) ≤ FJ(n)`, this rigorously gives
  **`R(10922) − S(10922) ≥ 569`**.
  This is a finite certificate only; it does not prove unboundedness.

**Structural analysis**

The Ford–Johnson count has the exact form

`FJ(n) = (m+1)n − Σ_{j=0}^m floor(4·2^j/3)`, `m=floor(log2(3n/4))`,

and asymptotically

`FJ(n) − I(n) = n·φ(t) + O(log n)`, `t={log2(3n/4)}`,

where `φ(t)=log2 3 − 1 + 1/ln2 − t − 2^{1−t}` ranges from about `0.02766` to `0.11373`. The points `n_k=floor(4·2^k/3)` are where FJ is closest to the information bound, so they are the right places to test unboundedness. Exact `L−FJ` there is `22,43,81,156,297,569` for `k=8..13`.

**Failed approach / precise obstruction**

Write `m(n)=L(n)−log2 n!`. Then `L−FJ = m − (FJ−I)`. Unboundedness would follow if `m(n_k) ≥ c n_k` infinitely often with `c > 0.02766`. Computationally `m(n)/n` is about `0.07–0.08` through `n≈10^5`, but it decreases slowly at powers of two; no all-`n` bound is proved.

The natural potential proof `f(n)=n log n − C n + O(log n)` fails exactly on the one-element split: `f(n)−f(n−1)` is about `log n + 1/ln2`, while the split-merge lower bound is only `ceil(log n)`, forcing `C ≥ 1/ln2 = 1.442695`. That is the information-bound coefficient and cannot beat FJ’s coefficient (`1.329–1.415`). So entropy plus Stirling is structurally insufficient; a proof needs a periodic/arithmetic treatment of `ceil(log n)` or stronger merge lower bounds.

**Honest conclusion**

The front remains open. The recurrence and reported gaps are correct, and the gap is rigorously at least `569` at `n=10922`, so any claimed uniform `O(1)` bound must have constant at least `569`. No infinite equality family was found: equality is confirmed only for `n≤4`. But **unboundedness was not proved**; the missing lemma is a linear lower bound on the rounding slack `m(n)` along the `n_k` sequence.
Inspected the existing state before doing anything new.

**What actually happened**

- The research work had already completed and the result was posted to **Antonina issue #301** once, at `2026-11-08T10:12:23Z`, author `SoringP1 frontier: split-merge-asymptotic-gap`.
- The board digest confirms exactly **one** matching post — no duplicate was created.
- Repository state: branch `billy-dev`, working tree **clean**, no new commits, no Lean or repository files changed.
- No research/background processes are still running.
- Intermediate scripts and results remain only under `/tmp/opencode`, not in the repository.

**Unfinished work**

None. The interrupted turn’s external side effect — the board post — is confirmed present and was not repeated. No uncertainty remains that requires review.

The mathematical conclusion stands: the front remains open, with a certified finite gap `R(10922) − S(10922) ≥ 569`, no infinite equality family found, and the unbounded-gap claim blocked by the missing linear rounding-slack lemma plus the exact `a=1` / `1/ln2` potential obstruction.

## Other metadata

```json
{
  "finished_at": 1794132824.1581297,
  "started_at": 1794129975.7808733
}
```
