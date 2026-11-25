# antonina-qV98zh8cEwaGegBtza2GRL-corrupt

Session: ses_e3ffdc5f6ffexgwlua0v92GZli
Workspace: /home/lubko/soring-fronts/ford-johnson-first-defeat
Created: 1794222733927; updated: 1794226354856

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1c0023d190013OJYHmcnUlsYRk)

I'll start by studying the repository contract, problem definition, and the current research board.

## Output 1246 (msg_1c037bad2001czIlaJp0TAMZIW)

## Verdict

**The front’s question is open. The least `n0` is not known to be 47.** What is actually established is

\[
23 \le n_0 \le 47,
\]

and `n0 = 47` is equivalent to the open statement

\[
S(n)=FJ(n)\quad\text{for every }23\le n\le 46.
\]

The key correction is that **Peczarski’s IPL 2007 theorem does not prove this**. Its abstract and Peczarski’s own homepage state the quantifier precisely: for `n < 47` there is no algorithm of the form “sort `m` and `n-m` elements by Ford–Johnson, then merge the two sorted lists” that beats Ford–Johnson. That is a theorem about a restricted split-and-merge architecture, not about arbitrary adaptive comparison trees. The paper title “still unbeaten” is therefore weaker than it sounds.

## What is proved

- `n0 >= 23`: exact values `S(n)=FJ(n)` are known for all `n <= 22` (Peczarski, Stober–Weiss, OEIS A036604).
- `n0 <= 47`: the 200-comparison sort is real. Split `47=5+42`; `FJ(5)=7`, `FJ(42)=171`, and Schulte Mönting’s five-element merge gives `M(5,42) <= 22`. Total `7+171+22=200 < 201=FJ(47)`.
- The n=47 witness is **not** Manacher’s. Manacher (JACM 1979) proves Ford–Johnson is not optimal for all sufficiently large `t` (abstract: `t > 189`); the n=47 200 witness comes from Schulte Mönting’s 5-element merge results, as cited explicitly by Bui–Mai (BIT 1985): “we can merge 5 elements to 42 elements in 22 comparisons.”
- The lower bound at 47 is only `C(47)=198`; the published range is `S(47) in {198,199,200}`.

For `23 <= n <= 46`, the published exact knowledge is only `C(n) <= S(n) <= FJ(n)`. Only `n=28` has a lower bound above `C`, namely `S(28) >= 99` while `C(28)=98`. Thus no general lower bound reaches `FJ(n)` anywhere in the open interval.

## Falsification attempt

I attacked the split-merge family first, since that is exactly Peczarski’s scope. For a split `a+b=n`, the information lower bound is

\[
L(n,a)=FJ(a)+FJ(b)+\lceil \log_2 \binom na\rceil,
\]

and the exact merge number is at least the last term.

Exact finite computations give:

| n | only splits with `L < FJ(n)` | exact merge fact | total |
|---:|---|---|---:|
| 23 | 2+21 (`L=75`) | `M(2,21)=9` | 76 = `FJ(23)` |
| 24 | 3+21 (`L=80`) | `M(3,21)=12` | 81 = `FJ(24)` |
| 44 | 2+42 (`L=182`) | `M(2,42)=11` | 183 = `FJ(44)` |
| 45 | 2+43, 3+42 (`L=188`) | `M(2,43)=11`, `M(3,42)>=15` | 189 = `FJ(45)` |
| 46 | 3+43, 4+42, 5+41 (`L=194`) | `M(3,43)>=15` blocks 3+43 | 195 = `FJ(46)` for that split |

For `35 <= n <= 43`, exact arithmetic shows `L(n,a) >= FJ(n)` for **every** nontrivial split, so the information bound alone rules out any split-merge improvement in that interval, independent of Peczarski’s exhaustive merge search. The remaining n=46 cells `4+42` and `5+41` were still undecided in my running searches; Peczarski’s theorem says both must miss their information bounds, otherwise a 194-comparison sort at n=46 would exist.

These computations are finite, exhaustive interval-state minimax searches over nondecreasing insertion-position tuples; queries `A_i` vs `B_j` are the thresholds `c_i < j`. They were validated on the known values `M(2,21)=9` and `M(2,42)=11`. They are not a paper proof and not Lean-checked.

No general (non-split-merge) counterexample below 47 was found.

## Exact obstruction

Let `delta(n)=FJ(n)-C(n)`. In `[23,46]`, `delta` is 1, 2, or 3:

- `delta=1`: `n = 23,24,40,41,42,43`
- `delta=2`: `n = 25,26,27,36,37,38,39,44,45`
- `delta=3`: `n = 28..35,46`

Here `delta` is the **room above the information bound**, not the number of comparisons a defeat must save. Every defeat saves at least 1. At `delta=1`, a defeating height would have to be exactly `C(n)` — an information-tight sort. At `delta=2` or 3 there is one or two comparisons of extra room above `C(n)`, but no method reaches even that.

The standard efficiency/leaf-count potential cannot exclude height `FJ(n)-1`, because

\[
n! \le 2^{C(n)} \le 2^{FJ(n)-1}.
\]

So the root is not pruned by leaf counting. Any proof of `S(n)=FJ(n)` for the open interval needs a genuinely stronger invariant or an exhaustive decision-tree search. At n=23, the exhaustive search is far beyond this host: Stober–Weiss needed about 89 hours on 24 threads/768 GB for n=18; this host has 4 cores/15 GB, and n=23 at height 75 is much larger.

## Honest limits

- I did **not** prove `n0=47`.
- I did **not** disprove it by finding a better sort below 47.
- I refuted only the stronger epistemic claim that Peczarski’s IPL 2007 result settles the general question; its quantifier is split-and-merge only.
- `n0` is a finite record question. A certified improvement below 47 would be a new exact upper bound for an open `S(n)`, but it would not by itself give a uniform algorithm or a complexity-class separation.
- The 200-comparison witness at 47 is an upper-bound certificate only; it does not establish `S(47)=200`.

The finding, including two corrections, is posted on board #301 under `SoringP1 frontier: ford-johnson-first-defeat`. Host `billy-dev`; worktree clean at `6a96398`; no repository or Lean changes.

## Output 1316 (msg_1c03931760015P1CXpNIa0cBOg)

## Recovery inspection complete

**Host:** `billy-dev`  
**Repository:** `/home/lubko/soring-fronts/ford-johnson-first-defeat`  
**Git:** clean worktree at `6a96398`; no commits, branches, or repository/Lean changes.

### External effects that actually happened

Exactly three board #301 comments exist under `SoringP1 frontier: ford-johnson-first-defeat`:

1. `2026-11-09T12:08:50Z` — main finding: `n0` is open, `23 <= n0 <= 47`; Peczarski’s theorem is split-and-merge-only; 200-comparison witness at n=47.
2. `2026-11-09T12:09:45Z` — correction: only 5+42 is certified to give 200; the other `L=200` splits were not claimed as certified.
3. `2026-11-09T12:10:23Z` — correction: `delta = FJ - C` is the room above the information bound, not the number of comparisons a defeat must save.

There is exactly one main post and two corrections. **No duplicate main post was made.** The ledger entry remains `status: running`; it is keeper-managed and was not edited.

### Unfinished side work

The two optional independent merge searches from the prior turn were killed by the backend failure:

- `searchfast 4 42 18` — output file contains only the initial `N=163185 h=18` line, no result.
- `searchfast 5 41 21` — output file contains only the initial `N=1370754 h=21` line, no result.

No result was recorded, so I am **not** claiming either computation completed. They were independent cross-checks, not gaps in the mathematical conclusion: Peczarski’s split-and-merge theorem already implies `M(4,42) >= 19` and `M(5,41) >= 22` at n=46. I did not blindly rerun them, to avoid creating another uncertain long-running effect.

### Mathematical conclusion unchanged

- `n0` is **not known to be 47**.
- The proved range is `23 <= n0 <= 47`.
- `n0 = 47` is equivalent to the open statement `S(n)=FJ(n)` for all `23 <= n <= 46`.
- Peczarski’s IPL 2007 result rules out improvements only for split-and-merge algorithms using Ford–Johnson halves, not arbitrary adaptive comparison trees.
- The 200-comparison construction at n=47 is real: `47=5+42`, `FJ(5)=7`, `FJ(42)=171`, merge in 22, total `200 < 201=FJ(47)`.
- No counterexample below 47 was found.

No further post, commit, or external action was made.
