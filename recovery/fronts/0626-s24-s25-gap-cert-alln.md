# s24-s25-gap-cert-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

vMToDSywnPK2wItGwLpDzF-bonnet

## exit_state

clearexit

## question

Is S(24) = C(24) = 80, or does a certified adversary force S(24) >= 81, or does S(25) need a certified depth above C(25) = 84?

## basis

OEIS A036604: exact S(22)=71; A003070: C(24)=80, C(25)=84; A001768: FJ(24)=81, FJ(25)=86; SW: S(28) >= 99; board #301: exec-s23-search-window window.

## falsifier

A sorting tree for 24 keys with worst-case height <= 80 (certifying S(24) <= 80), or a certified adversary lower bound S(24) >= 81.

## implication

An e(24) = 0 extends the info-tightness streak past n = 22 and reopens the question of when the certified excess re-emerges after 22.

## finding_unverified

 board post from this session; all scratch is in `/tmp/opencode/`. Antonina was only *read* (`board_digest.py`), so there is no uncertain external effect to replay.

### Precise claim attacked

**"S(24) = C(24) = 80"** (i.e. `e(24)=0`), the first arm of the front. Falsifiers as specified: a depth‑80 sorting tree for 24 keys, or a **certified adversary** forcing `S(24) ≥ 81`.

Baseline `[literature]` (OEIS A036604/A003070/A001768 pages fetched directly; `docs/literature.md`): exact `S(n)` is known only through `n=22` (`S(22)=71`; n=23 open), `C(22)=70, C(23)=75, C(24)=80, C(25)=84`, `FJ(23)=76, FJ(24)=81, FJ(25)=86`. Hence `[deduction]` `S(24) ∈ {80,81}` and `S(25) ∈ {84,85,86}`.

### Certified-adversary attack and its exact obstruction

I defined the sound family (induction gives `A_k(P) ≤ F(P)`, and `F(A_n)=S(n)`):
`A_0(P)=⌈log₂ e(P)⌉`; `A_k(P)=1+min_{incomparable {a,b}} max(A_{k−1}(P+a<b), A_{k−1}(P+b<a))`.

Two independent implementations (full enumeration; symmetry-reduced over `Aut(P)` pair orbits) agree on n≤12 and on n=24,25 for k≤2:

| n | C(n) | A₁…A₅ |
|---|---|---|
| 12 | 29 | 29,29,29,29,29 (S(12)=30) |
| 16–18 | 45,49,53 | all = C(n) (known S=C+1) |
| **22** | **70** | 70,70,70,70,70 (**S(22)=71**) |
| 23 | 75 | all 75 |
| **24** | **80** | **80,80,80,80,80** |
| **25** | **84** | **84,84,84,84,84** |
| 28 | 98 | all 98 (SW: S(28)≥99) |

**New barrier theorem (paper proof).** For every `n≥2` and every `k≤⌊n/2⌋`, `A_k(A_n)=C(n)`. *Proof:* `A_k ≥ A_0 = C(n)`. For a poset `A_n` + `t` disjoint added relations with `n−2t≥2`, `e(P)=n!/2^t`, so `B(P)=⌈log₂e(P)⌉=C(n)−t`; choosing a pair of *free* (isolated) elements gives both children `e=e(P)/2`, hence `B(child)=B(P)−1`. Induction on the free‑free policy gives `A_k(P)≤B(P)`; at the root `t=0`. (Also `A₁(A_n)=C(n)` for all n≥3 by `1+⌈log₂(n!/2)⌉=⌈log₂n!⌉`.)

### Finding

- **No falsifier found:** `A_k(A_24)=80` for all k≤5, and by the theorem for all computationally reachable k≤12. This adversary family cannot certify `S(24)≥81`; likewise it cannot certify depth `>84` at n=25. It also cannot certify the **known** excess at n=22 (`A_k=70` while `S(22)=71`) or at n=12, 16–18, 28 — a concrete demonstration that **soundness ≠ completeness** for this certificate family.
- General-poset obstructions (e.g. the `e=8, L1=4>3` witness or merge-factor gaps) do **not** transfer to the antichain root; the free-free strategy eliminates them there. This is a no-go for this *method family*, not for all conceivable adversary arguments.
- **S(24), S(25) remain undecided by this work.** No depth-80 tree was found or built (state space is A001035(24); exhaustive search infeasible; S(23) itself is open). No complexity-class claim: `SORT-BOUND-U ∈ PSPACE` is unchanged, no P/NP separation, and "S(n)≥81" is a comparison bound, not a complexity lower bound for computing S(n).

### Limits honestly stated

- Full (non-symmetry) enumeration at n=24, k=3 was killed on resources; the symmetry-reduced version was validated against the exhaustive one at k≤2. An earlier run died from a set-mutation bug; fixed, no duplicate side effects.
- Web search was unavailable in this session (three cancellations); I used primary OEIS pages via direct fetch and the repo's literature baseline instead.
- No Lean, tests, CI, ledger, commits or board comments were produced. Given the Antonina recovery notice, I report here rather than risk an uncertain #301 post; the above is ready as a concise board update if you want it posted.

## Other metadata

```json
{
  "finished_at": 1795232919.638876,
  "started_at": 1795231173.1871672
}
```
