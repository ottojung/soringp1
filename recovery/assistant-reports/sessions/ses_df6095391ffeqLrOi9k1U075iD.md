# antonina-mDETFI9fgdJpgUWbvrSxxn-memorable

Session: ses_df6095391ffeqLrOi9k1U075iD
Workspace: /home/lubko/soring-fronts/reachable-defect-repair-frequency-alln
Created: 1795463490832; updated: 1795465002416

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_209f6b05e001XYUWD2JQJ5LhaV)

I'll start by understanding the repository structure, the current branch state, and the key documents.

## Output 17 (msg_209f6bd870010A1bErXcCdsmZE)

Let me read the key documents in parallel.

## Output 40 (msg_209f6c8300012j5sXmdDGD2vAW)

Let me check the board digest, the frontier definition, and any existing work in this directory.

## Output 94 (msg_209f7323f0011Lu33p6rCMQCJy)

Let me read the referenced research docs and search for the definition of the state tuple notation.

## Output 168 (msg_209f88952001ovVjvHUFIsnEmj)

Let me check for any existing scratch work and understand the state-tuple representation used on the board.

## Output 188 (msg_209f8f926001ny7lU3m6uSjcha)

Let me search the primary literature for whether the information gap S(n) − ceil(log2 n!) is known to occur infinitely often.

## Output 226 (msg_209f9d1a9001usNJ5WsNLXOhMm)

Now I have a clear picture of the definitions and prior art. Let me set up a from-scratch computation to validate the baseline data and probe n=7.

## Output 317 (msg_209fd89b3001CTc75GuyVYhEQ6)

I found a bug in my extension counter (off-by-one on the full mask). Let me fix it.

## Output 335 (msg_209fee853001E2aU1EmoTq2oau)

The baseline now matches the board (0 repairs at n=4,5; repairs appear at n=6). Let me make the search deduplicate states so I can reach n=7.

## Output 369 (msg_20a00ae200016YcJzLmDHilGU0)

The engine now exactly reproduces the board's n=5/n=6 counts, and n=7 shows abundant repairs. Let me extract a concrete witness to study the mechanism.

## Output 396 (msg_20a027b21001ZQynQDtCqLpQTD)

This is promising. Let me check whether the "unit drop" observation already exists on the board, to avoid rediscovering a known result.

## Output 432 (msg_20a0d12ce0015FH6URDA2oOZMP)

## Claim (front: `reachable-defect-repair-frequency-alln`)

**Precise question.** Let `P` be reachable from the `n`-antichain `A_n` along a height-`S(n)` optimal play, i.e. along a path where each step is an incomparable comparison whose outcome child `C` has `F(C)=F(P)-1` and depth increases by 1 (adversary follows a worst-case optimal child). Define
- `e(P)` = number of linear extensions, `L(P)=ceil(log2 e(P))`,
- `F(P)` = exact minimax comparison value,
- `delta(P)=F(P)-L(P) >= 0` [deduction, info bound].

A **repair** is such an optimal worst-case step with `delta(C) < delta(P)`. Can `delta` drop by more than 1 in one optimal worst-case comparison? Are repairs eventually impossible?

**Model fidelity.** Adaptive pairwise comparisons, distinct labelled keys, exact `F/e` from first principles. All sizes are numeric `n`; this is a structural theorem/certificate question, not a complexity-class placement (AGENTS.md: `SORT-BOUND-U ∈ PSPACE` already, unconditional lower bounds out of scope). Soundness is not completeness.

## From-scratch computation [experiment, independent]

I wrote a fresh C++17 engine (`/tmp/opencode/reachrepair.cpp`, GCC 15.2.0, no repo code): transitively-closed successor bitmasks, `e` by downset/subset DP, `F` by memoized minimax, `delta=F-L`; DFS follows only optimal worst-case children (`F(C)=F(P)-1`), states deduplicated. Sanity: `S(4..7)=5,7,10,13`, `e(A_n)=n!`. Results:

| n | S(n) | reachable states | defective reachable | repair events | 1->0 | drops>=2 | maxDrop |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 5 | 181 | 0 | 0 | 0 | 0 | 0 |
| 5 | 7 | 1551 | 0 | 0 | 0 | 0 | 0 |
| 6 | 10 | 65551 | 1440 | 7200 | 7200 | 0 | 1 |
| 7 | 13 | 2769663 | 340200 | 2265480 | 2265480 | 0 | 1 |

This reproduces the board's `n=5: 1551/0` and `n=6: 65551/7200` counts. An n=8 exhaustive run was killed by SIGKILL locally (memory/time; only scratch effect, no external side effect). Witnesses from scratch:
- n=6, depth 5, pair (0,5): `P=[30,16,8,0,0,18], e=16,F=5,delta=1` -> `C=[62,16,8,0,0,18], e=10,F=4,delta=0` (matches the front's example shape).
- n=7, depth 4, pair (0,5): `P=[30,16,8,0,0,0,0], e=252,F=9,delta=1` -> `C=[62,16,8,0,0,0,0], e=210,F=8,delta=0`.

## Mathematical findings

### 1. Unit-drop bound on optimal worst-case edges [deduction, paper proof]

**Proposition.** For any finite poset `P` and any incomparable comparison with outcome child `C` such that `F(C)=F(P)-1` (in particular, any optimal worst-case/adversary-followed step), 
`delta(C) >= delta(P)-1`.

*Proof.* Let `e=e(P), e'=e(C)`. The comparison partitions linear extensions, so `e' <= e-1 < e`, hence `log2 e' < log2 e`, hence `L(C)=ceil(log2 e') <= ceil(log2 e)=L(P)`. Therefore
`delta(C)-delta(P) = (F(C)-L(C)) - (F(P)-L(P)) = (L(P)-L(C)) - 1 >= -1`. ∎

**Corollary.** A repair on an optimal worst-case edge can never be larger than 1 unit: `delta(P)-delta(C) <= 1`. Also `delta` cannot increase along such an edge (`L(C)<=L(P)` gives `delta(C)<=delta(P)`, with equality when `L` stays the same).

This **falsifies the “drop >=2” horn** as stated: no single optimal worst-case comparison can erase two units of local excess, for any `n`, by an elementary inequality. The observed n<=7 data (all repairs 1->0) is consistent and the 1->0 form is forced because all observed defective reachable states had `delta=1`.

### 2. Repairs can exist on optimal worst-case edges [deduction + experiment]

The bound is tight in form: a drop of exactly 1 occurs iff `L(C)=L(P)` (the comparison does not cross a power-of-two information boundary) while `F` drops by 1. The n=6/n=7 witnesses are explicit instances. So “repairs persist / are possible” is true in the weak sense at finite n; the front's data already showed this.

### 3. The front’s complexity implication needs care [deduction, barrier]

The front suggested: “if repairs are eventually impossible, positive defect becomes a monotone locally checkable invariant propagating toward the root ... supporting a sound one-step defect certificate”. Proposition 1 already gives a stronger local fact: **on optimal worst-case edges `delta` is nonincreasing and can fall by at most 1**. But this is far from a useful sound NP-style certificate for `SORT-BOUND-U`:
- `delta(P)>0` is sound for `F(P)>L(P)`, but **not** for `S(n)>k` unless you also certify the edge is on an optimal-height play reaching a defect that forces the root. Soundness vs completeness (AGENTS.md) is the key obstruction.
- Certifying `delta`/`F` locally needs `e(P)`/`F(P)`, which are #P-hard / minimax-hard in general posets; `L1`-style one-ply tests are sound but incomplete (see `docs/research-one-ply-obstruction.md`).
- The antichain root has `delta(A_n)=D(n)=S(n)-ceil(log2 n!)`, which is 0 at the known tight n and 1 at the known non-tight n; a monotone-local defect invariant cannot by itself turn that into an NP witness without a global optimal-play certificate. An optimal tree is exponentially large (problem.md §61).
- Thus neither horn gives a complexity-class separation. At best it is a structural barrier/certificate-shape fact.

## Failed/blocked approaches

- **n=8 exhaustive enumeration**: killed by SIGKILL after the F memo filled; needs a memory-aware/out-of-core or stronger pruning design. I did not rerun it after the kill to avoid repeating an expensive effect.
- **Proving “no repair for all large n”**: refuted as a universal statement by n=6,7 and by the easy existence of local L-preserving F-drops; the live question becomes quantitative/frequency, which I did not settle for all n.
- **Turning monotonicity into SORT-BOUND-U certificate**: blocked by global optimal-play certification and #P/minimax cost of local predicates.

## Falsification attempt

I tried to falsify the unit-drop bound by searching for any `delta` drop >=2 in all reachable optimal worst-case edges through n=7 (2,769,663 reachable states at n=7). None found. I then looked for a paper counterexample shape; the partition inequality `e' < e => L' <= L` is unconditional, so no finite poset counterexample exists. The attempted falsification fails.

## Exact obstruction / honest limit

The mathematically strong content here is the **elementary one-ply unit-drop inequality** (Proposition 1), which settles the “drop by >=2?” subquestion negatively for all n. The remaining open content is the front’s asymptotic frequency question: is the set of `n` admitting *any* reachable optimal-play repair cofinite/infinite? My small-n data is `no,no,yes,yes` for n=4..7; n>=8 is uncomputed here. Settling “infinitely many n” would require an all-n construction of a reachable defective state on a height-`S(n)` play with an L-preserving optimal child — hard because optimal plays/`S(n)` are not explicitly characterized beyond small n. I make **no** theorem completion claim for S(n) or SORT-BOUND-U, no repo/Lean/test/CI/board change.
