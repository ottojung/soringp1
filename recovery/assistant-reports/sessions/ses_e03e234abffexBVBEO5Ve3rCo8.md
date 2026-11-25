# antonina-vMToDSywnPK2wItGwLpDzF-bonnet

Session: ses_e03e234abffexBVBEO5Ve3rCo8
Workspace: /home/lubko/soring-fronts/s24-s25-gap-cert-alln
Created: 1795231173529; updated: 1795232906754

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fc1dcda2001hLLiq6l2xgrYRM)

I'll start by understanding the environment: where billy-dev is, the repo state, and the docs/board the user mentioned.

## Output 29 (msg_1fc1def67001vQIxD9DousrnXi)

I'm on branch `billy-dev` (the required host). Let me get the board digest (#301 context) and read the core docs.

## Output 52 (msg_1fc1e5dcf001QZnfvAbpsDNtU4)

The board digest errored — let me check why, and inspect the earlier board artifacts in `/tmp/opencode` (the "resuming after infrastructure failure" hint).

## Output 71 (msg_1fc1e8c10001bIZA8QVdkfKc3p)

Board digest uses no `--json`; there are also pre-fetched OEIS b-files and earlier board artifacts. Let me get the digest, the OEIS data, the literature doc, and the earlier search.

## Output 94 (msg_1fc1ec376001nH0wpXYp7dJ1gF)

Board digest works; I have the key data. Let me verify the info-theoretic numbers and launch the primary-literature search for exact values near n=23–25, plus survey the repo's certificate/adversary machinery.

## Output 142 (msg_1fc209fa1001eLMMxcCSByXHwr)

Web search appears unavailable in this environment (two cancellations). Let me try fetching the OEIS pages directly, and inspect earlier work artifacts (`s23.py`, `sorting_dp.py`, earlier prompts, board search) to avoid repeating claims.

## Output 341 (msg_1fc354310001vrLgV5Icc5UN3P)

The fast symmetry-reduced solver works and cross-checks the earlier exhaustive implementation on n≤12. Let me probe the pattern at other n (including known-gap n=16–18, 22, 28) and cross-check n=24 with the exhaustive (non-symmetry) code.

## Output 361 (msg_1fc375111001vL1Qy9hHsnUeAv)

## Report — billy-dev, worktree clean (6a96398), no repository/Lean/board writes

I checked state first after the interruption: no commits, no Lean files, no PR, no board post from this session; all scratch is in `/tmp/opencode/`. Antonina was only *read* (`board_digest.py`), so there is no uncertain external effect to replay.

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
