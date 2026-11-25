# antonina-VamXuC5ihMkWwnP8Yzwqim-bismuth

Session: ses_df6d58462ffe9554vTdB5UT7Mc
Workspace: /home/lubko/soring-fronts/min-double-drop-count-optimal-alln
Created: 1795450108865; updated: 1795452607285

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_20931e9df001xfh05feeK46hXQ)

I'll start by inspecting the current state carefully, as instructed — checking git state, the working directory, and any durable task records before doing anything else.

## Output 28 (msg_20931f7d80016ORJlEMfTW5n3v)

The working tree is clean. Now let me read the key documents and look for durable task records / any partial work from the interrupted turn.

## Output 43 (msg_20932095e001xlDjW1mmCxn3LY)

Working tree is clean on `billy-dev`. Let me read the problem statement, literature list, and check the research board and durable ledger for the state of this front (and any prior work from the interrupted turn).

## Output 58 (msg_209322160001fX6CkbDfCxtyTl)

Now let me check the research board (#301) and the durable frontier ledger for the state of this front, plus any prior work from the interrupted turn.

## Output 73 (msg_2093243600015sCvJ1SrOMa7Yz)

Let me look specifically for this front in the ledger and search board #301 for "double drop" / board #301's 14:04Z entry.

## Output 88 (msg_209325a370013vt61BJLqOWsqC)

This is a critical find: my front is `running`, and there's a closely related PRIOR front `f-drop-synchrony-optimal-play-alln` (14:04Z) that settled a related question. Let me read both posts in full to understand exactly what was proven, and check for any prior work/side effects from my own front.

## Output 103 (msg_209327c69001RQqSrV8jPJyjYI)

Let me get the full text of the closely-related 14:04Z `f-drop` result (what exactly was proven) and check for any prior side effects/scratch from my own front.

## Output 114 (msg_209328cb4001CC7m8kknrmxUAf)

This is a key finding: the prior `f-drop-synchrony` front proved only that M(n) ≥ 1 (at least one double drop in every optimal tree). My front asks the strictly finer quantitative question (constant vs. growing). Let me check for any prior side effects from my own front and read the relevant research notes on defect/slack before attacking.

## Output 138 (msg_2093411f0001Isq72v05ObT0t1)

I now have a clear picture. Key facts:
- Prior front `f-drop-synchrony` proved only M(n) ≥ 1 (one double drop forced in every optimal tree).
- My front asks the strictly finer quantitative question (constant vs. growing).
- `good-path-density` bounded δ-biased comparisons via Sergeev; I have a distinct potential-function idea for double drops themselves.

No prior post/side effects from my own front. Let me verify the mathematics with a from-scratch computation. First let me confirm the literature facts (Sergeev's bound) and set up scratch computation.

## Output 171 (msg_209353aca0011VfpL5VU4EJ773)

Sergeev's theorem is confirmed from the primary source (ECCC TR20-096: S(n) = log₂(n!) + o(n)). Now let me write a from-scratch exact computation for M(n) on small n to test the hypotheses.

## Output 189 (msg_209358d65001KLHKNZaj44tCaa)

The state counts look wrong (n=3 should give 19 labeled posets, not 7). Let me debug the enumeration.

## Output 200 (msg_20935bdaf001m9nVXb96j5Idfb)

Found the bug: I only added relations `i<j` for `i<j` numerically. Need all ordered pairs. Let me fix.

## Output 234 (msg_2093684510011Ps0gYwM7HHN6y)

The computation now matches known state counts (A001035) and S values. Results: M_path=1 for n≤6, M_global=2,2,8,48 — the two readings diverge. Let me verify my potential-function theorem numerically and check the board for novelty.

## Output 245 (msg_20937fd8c001jXqcV9QP1eUYJh)

The potential bound is verified numerically and tight at n=3,4. Now let me test whether the "≤1 double drop per path" reading extends beyond n=6 using a targeted recursion (avoids enumerating all states).

## Output 306 (msg_2094f0adf0011GGFTgI4RkTXNS)

## Recovery / side-effect audit

- **Git**: `billy-dev` at `6a96398`, `git status --short --branch` clean. No commits/branches/PRs created.
- **Board #301**: searched for `min-double-drop-count-optimal-alln`; no post from this front found. I have **not posted** to #301.
- **Scratch only**: `/tmp/opencode/mdd_compute.py`, `/tmp/opencode/good1_search.py` (exact small-n computations). No repo/Lean/test/CI/ledger/main changes.
- **Interrupted work**: an n=7/n=8 targeted `good1` search was killed by SIGKILL (no n=7/n=8 result produced). I did not repeat any external side effect; I stopped the heavy search and report what is established.

## Front (as given)

For n>=3 let M(n) be the minimum, over height-S(n) optimal adaptive comparison sorting trees of the n-antichain, of the number of comparisons that possess an outcome child Q with F(Q) <= F(P)-2 (a minimax double drop). Is M(n) bounded by one fixed constant for infinitely many n, or does M(n) grow without bound (in particular M(n)=Omega(n)) for all sufficiently large n?

## Definitions / model [definition]

- `F(P)` = exact adaptive minimax comparison-sorting value of finite poset `P`; `S(n)=F(A_n)`, `A_n` the n-antichain. `e(P)` = number of linear extensions. Information bound `F(P) >= ceil(log2 e(P))`; partition identity `e(P)=e(P1)+e(P2)`.
- A comparison at node `P` is a **minimax double drop** if its lighter minimax outcome has `F(Q) <= F(P)-2`. (The heavier outcome has `F <= F(P)-1` in any height-`S(n)`-feasible optimal move.)
- Two natural readings of "number of comparisons":
  - `M_global(n)`: minimum, over height-`S(n)` optimal trees, of the **total number of double-drop nodes** in the tree.
  - `M_path(n)`: minimum, over height-`S(n)` optimal trees, of the **maximum, over root-leaf paths, of the number of double-drop nodes on the path**.  
  The front states "number of comparisons..." (a tree count); I report both because they diverge sharply.

## Prior art (not rediscovered) [literature/board]

- `f-drop-synchrony-optimal-play-alln` (2026-11-23T14:04:48Z) + Viche referee (14:08Z): for every n>=3, every height-S(n) optimal tree has >=1 double drop; equivalently no F-synchronous optimal tree exists for n>=3. This gives `M_global(n)>=1`, `M_path(n)>=1`, but no growth/counting theorem.
- `good-path-density-alln` (06:55Z) gives an o(n) bound on expected δ-biased comparisons by the entropy/Kraft chain rule + Sergeev; different event (split-bias), different quantifier.
- Sergeev, ECCC TR20-096 (primary): `S(n)=log2(n!)+o(n)`. 
- Known `S`: `S(3..8,12)=3,5,7,10,13,16,30`.

## Independent small-n computation [experiment, scratch]

From-scratch exact DP (transitively-closed successor-bitmask states, exact `e` by subset DP, exact memoized minimax `F`, exact path/global DD minimization over height-`S(n)` trees). State counts match A001035 (19,219,4231,130023 for n=3..6); `F(A_n)` matches known S.

| n | S(n) | slack S-log2 n! | M_path | M_global | M_path_minimax-only |
|---|---:|---:|---:|---:|---:|
| 3 | 3  | 0.4150 | 1 | 2  | 1 |
| 4 | 5  | 0.4150 | 1 | 2  | 1 |
| 5 | 7  | 0.0931 | 1 | 8  | 1 |
| 6 | 10 | 0.5081 | 1 | 48 | 1 |

`M_path_minimax-only` restricts to locally minimax comparisons (`max child F = F(P)-1`) at every node; same result here. I also checked the "good1" property (exists a height-S(n) tree with <=1 dd on every path): **True for n<=6** (n=6 by the same exact computation; n=7/n=8 search killed before result).

## Main mathematical finding: o(n) expected double drops [deduction, paper proof]

**Theorem (slack-potential bound).** Let `T` be any correct comparison-sorting tree of height `h` for `A_n`. For a node `P` on a root-leaf path, let `p=e(Q1)/e(P)`, `r=F(P)-F(Q_light)>=1` in the light-child sense, and let `D(P)` be the indicator that `P` is a double drop (`r>=2` and the chosen comparison is minimax-feasible as used). Then, under the uniform distribution on the `n!` input permutations (equivalently, reach probability `q(P)=e(P)/n!`),

> `E_T[#double drops on a uniform random root-leaf path] <= (h - log2(n!)) / log2(4/3)`.

In particular for any height-`S(n)` optimal tree,

> `E_T[#dd] <= (S(n)-log2(n!)) / log2(4/3) = o(n)`,

using Sergeev `S(n)=log2(n!)+o(n)` [literature].

*Proof.* Define the defect potential `Phi(P)=F(P)-log2(e(P)) >= 0`. For a leaf `Phi=0`, and `Phi(A_n)=S(n)-log2(n!)` for a height-S(n) tree rooted at the antichain (equivalently `h-log2(n!)` for height h). For one comparison `P -> Q1,Q2`, `e=e1+e2`, `p=e1/e`, `F1=F(Q1)`, `F2=F(Q2)`:

`Phi(P)-E[Phi(child)|P] = F(P) - p*F1 - (1-p)*F2 - h2(p)`.

For a minimax-feasible comparison, `F1,F2 <= F(P)-1`. Writing `r1=F(P)-F1>=1, r2=F(P)-F2>=1`, this is

`= 1 + p*(r1-1) + (1-p)*(r2-1) - h2(p) >= 1-h2(p) >= 0`.

For a **double drop** (wlog `r2>=2`, `r1>=1`), it is

`>= 1 + (1-p)(r2-1) - h2(p) >= 2-p-h2(p)`.

The function `g(p)=2-p-h2(p)` has derivative `-1-log2((1-p)/p)=log2(p/(1-p))-1`, zero at `p=2/3`, and minimum `g(2/3)=4/3-h2(2/3)=log2(4/3)~0.415037`. Thus every double-drop node contributes at least `log2(4/3)` in this telescoping expectation, while every non-dd node contributes >=0. Telescoping over the random path gives `Phi(A_n)-E[Phi(leaf)] >= log2(4/3)*E[#dd]`, i.e. the stated bound. QED.

**Sanity check [experiment]**: exact `E[#dd]` by the same DP gives n=3:1.0 (bound 1.0), n=4:1.0 (1.0), n=5:0.2 (0.2243), n=6:0.6444 (1.2243) — all <= bound, tight at n=3,4.

## Consequences for the front [deduction]

1. **Omega(n) horn is refuted for the expected/path-typical reading.** Since `E_T[#dd]=o(n)` for every height-`S(n)` tree, no tree can force `Omega(n)` double drops on a uniform-random typical path; indeed Markov gives that all but an o(1) fraction of leaves have `o(n)` double drops (choose a threshold `t(n)` with `E[#dd]<<t(n)<<n`).
2. **It does NOT prove M_path is O(1).** The bound controls expectation, not the worst root-leaf path. A worst path could a priori be larger than E[#dd] while still o(n); my small-n data gives M_path=1 through n=6, but I have no all-n worst-path proof.
3. **It does NOT settle M_global.** Total dd-node count can be much larger than expected-per-path count: M_global=2,2,8,48 at n=3..6 while E[#dd] stays below 1. A global Omega(n) or omega(1) lower/upper bound on M_global remains open from this argument alone.
4. **Complexity implication (honest, limited).** The result is a structural theorem about the minimax game: optimal trees cannot dissipate the total `o(n)` information slack through `Omega(n)` expected double-drop events, because each such event has a uniform slack-potential cost >=log2(4/3). This rules out "many discrete slack-creating events on typical paths" as an Omega(n) phenomenon, but it does **not** give a new evaluator, no NP/coNP placement, no separation, and no succinct certificate. The argument is soundness-only in the usual sense (a bound on a quantity), not a completeness/certificate claim.

## Attempted falsification / failed routes [deduction/experiment]

- **Falsify by growing worst-path count**: tried to find n>=7 with M_path>=2. n<=6 gives M_path=1. n=7/n=8 targeted exact search (`good1`, using the `e(P)=2^F(P)` F-synchrony characterization for the zero-dd subtrees) was killed by SIGKILL before completion; no counterexample found, no confirmation obtained. **Inconclusive.**
- **Falsify by Omega(n) expected count**: impossible given the theorem above and Sergeev; a concentrating construction would need E[#dd]=Omega(n) but has only o(n) slack budget.
- **Use total global count as Omega(n)**: small-n global counts grow (2,2,8,48) but this is far from an asymptotic argument; no proof either way.

## Honest limits / exact obstruction

- The central open point is the **worst-path vs expectation gap**. The potential theorem gives `E[#dd]=o(n)` on every height-S(n) tree, which is strong and clean, but the front's M(n) is a minimax-over-trees count; if read as worst path it asks for a pathwise bound, if read as global node count it asks for a much stronger combinatorial quantity. I cannot prove M_path=O(1), cannot prove M_path unbounded, and cannot prove/disprove M_global=Omega(n).
- n=7 exact M_path/M_global is **unresolved here** (search killed; A001035(7)=6,129,859 states makes full enumeration feasible in principle but the targeted good1/F memoization run was interrupted in this environment).
- Sergeev's o(n) is ineffective, so the o(n) in the E[#dd] bound is qualitative.
- No general-poset hardness used; the antichain root / S(n) fixed family is essential.
- No claim about S(n) values, no faster evaluator, no complexity-class placement for `SORT-BOUND-U`.

## Status

**Partial structural result, not a full resolution of the front.** Proved: `E_T[#double drops on a uniform random path] <= (S(n)-log2(n!))/log2(4/3)=o(n)` for every height-`S(n)` optimal tree (paper proof, small-n exact sanity check). This refutes the Omega(n) horn for the expected/typical-path reading and constrains any global Omega(n) claim to be non-typical. Open: worst-path constant/growth (`M_path`) and total-node growth (`M_global`), especially at n>=7.
