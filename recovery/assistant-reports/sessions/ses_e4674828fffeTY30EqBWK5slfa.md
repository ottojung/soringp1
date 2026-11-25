# antonina-eYzTqkPXMhGV6G7vPRYEWH-remarks

Session: ses_e4674828fffeTY30EqBWK5slfa
Workspace: /home/lubko/soring-fronts/gpc-maximal-insertion-preservation
Created: 1794114289085; updated: 1794116461664

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b98b7fa9001vWaAHoVeSlMwfl)

I'll start by reading the referenced materials and understanding the GPC statement precisely.

## Output 168 (msg_1b98d7f9b001n378BAK8PZbKNy)

Now I'll set up a computation using the existing audited census machinery. Let me write a probe in `/tmp` (untracked) that computes exact `m`, enumerates cores, inserts `x` above every proper ideal, and checks GPC/Fibonacci.

## Output 781 (msg_1b9ab02e5001ls66ZtnMsVMkU9)

# Report: maximal insertion above a proper ideal vs GPC

**Worktree:** `/home/lubko/soring-fronts/gpc-maximal-insertion-preservation` (read-only use).  
**No tracked files changed, no commits, no board post.** Scratch checks are in `/tmp/opencode`.

## Verdict

**INCONCLUSIVE — and structurally, the preservation statement is equivalent to GPC itself.**

No counterexample exists in the tested range, and none can exist with `|Q'| <= 14` by Gupta’s 2026 exhaustive verification of GPC through 14 elements. But the proposed preservation step is not an independent lemma:

> If maximal insertion above every proper ideal preserved GPC for every GPC core, then GPC would hold for every finite poset.

Consequently **PRESERVATION-PROVED would be a proof of GPC**, and **COUNTEREXAMPLE-FOUND would be a counterexample to GPC**. Since GPC is open, neither verdict is presently available. The same equivalence holds for the Fibonacci statement `e(P) >= F_{m(P)+2}`.

## 1. Precise formulation

Let `Q` be a core (nonempty, no element comparable with all others), `I ⊊ Q` a proper ideal, and `Q' = Q ∪ {x}` with `x` a new maximal element satisfying

```
x > q  for all q in I,      x incomparable with every q in Q \ I .
```

Use the operational GPC form from `docs/research-width-two-threshold.md §2`: there is a first comparison such that for each first-level outcome with a non-chain child, a second comparison inside that child can be chosen so that every grandchild has at most as many linear extensions as the other first-level child. Equivalently, with first children `a >= b` and second split `a = a_1 + a_2`, one needs `max(a_1,a_2) <= b`.

The two questions tested were:

- **GPC(Q,I):** does `Q'` satisfy GPC?
- **Fib(Q,I):** does `e(Q') >= F_{m(Q')+2}`?

## 2. Main structural result: equivalence with GPC

This is a paper deduction using Lemma 2 of `docs/research-core-threshold.md` and the Dolores-Cuenca–Guzmán-Sáenz–Kim lexicographic-sum theorem.

**Theorem A.** GPC holds for every finite poset iff GPC is preserved under every maximal insertion over every proper ideal of every GPC core.

*Proof.* (⇒) is immediate. For (⇐), suppose GPC fails and take a counterexample `P` of minimum `|P|`.

1. `P` has no universal element: if `u` were universal, then `P-u` is smaller and satisfies GPC by minimality; any GPC witness in `P-u` lifts to `P` because extensions of `P` are extensions of `P-u` with `u` inserted at a fixed position, so the `t`-counts are unchanged. Thus `P` is a core.
2. `P` is not a nontrivial ordinal sum `A (+) B`: both `A` and `B` are smaller, hence satisfy GPC by minimality, and Dolores-Cuenca et al. (Theorem 3, `Order 43, 34 (2026)`, arXiv:2410.12494v2) give GPC for lexicographic sums of a GPC block; applying this twice gives GPC for `A (+) B`, contradiction.
3. So `P` is an ordinal-indecomposable core with `|P| >= 3`. By Lemma 2, some maximal `x` has `Q = P-x` a core. Minimality gives GPC(Q). The set `I = {q in Q : q < x}` is a proper ideal of `Q` (proper because `P` is a core, so `x` is not universal). Therefore `P = Q ∪ {x}` is exactly a failing maximal insertion over a GPC core, contradicting the preservation hypothesis. ∎

**Theorem B.** The same equivalence holds with “GPC” replaced by the Fibonacci property `e(P) >= F_{m(P)+2}`.

*Sketch.* A minimal counterexample to the Fibonacci property is again a core with no universal element. If it were `A (+) B`, then `e(P)=e(A)e(B)`, `m(P)=m(A)+m(B)`, and the factors satisfy the Fibonacci property by minimality; the product inequality
`F_{a+2} F_{b+2} >= F_{a+b+2}`
follows from `F_{a+b+2} = F_{a+2}F_{b+1} + F_{a+1}F_b` and `F_{b+2}=F_{b+1}+F_b`. So the minimal counterexample is an ordinal-indecomposable core, and Lemma 2 again produces a failing insertion over a smaller core. ∎

**Corollary (same minimal size).** The smallest size of a GPC counterexample equals the smallest size of a failing insertion over a GPC core. Gupta’s census (`arXiv:2607.23926v2`, Theorem 5) verifies GPC through 14 elements, so any counterexample to preservation has `|Q'| >= 15` (`|Q| >= 14`). The analogous statement holds for the Fibonacci property.

This is the central finding: the frontier step singled out by board #301 is not an “uncovered small case”; it is exactly the open conjecture in minimal-counterexample form.

## 3. Exhaustive finite checks

I generated all core isomorphism classes through `n = 7` with the audited `core_threshold_census.py` machinery, enumerated **every proper ideal** of each core, adjoined `x` above it, and checked both properties.

| `|Q|` | core classes | proper ideals / insertions | GPC failures | Fib failures |
|---:|---:|---:|---:|---:|
| 2 | 1 | 3 | 0 | 0 |
| 3 | 2 | 12 | 0 | 0 |
| 4 | 8 | 72 | 0 | 0 |
| 5 | 35 | 459 | 0 | 0 |
| 6 | 203 | 3,692 | 0 | 0 |
| 7 | 1,447 | 35,939 | 0 | not required |
| **total n<=7** | **1,696** | **40,177** | **0** | — |
| **total n<=6 (Fib)** | — | **4,238** | — | **0** |

**GPC row.** The 40,177 `Q'` were checked with a bitset split-search implementation; the implementation was cross-checked against the slower brute-force checker for all cores with `n <= 5`. As noted, the fact that no failure occurs with `|Q'| <= 14` is forced by Gupta’s theorem; this row is a consistency check on the implementation, not evidence beyond order 14.

**Fibonacci row.** For each insertion I computed `r = max{r : F_{r+2} <= e(Q')}` and ran the exact bounded minimax `sortable(Q', r)`. A true result certifies `m(Q') <= r`, hence `e(Q') >= F_{m(Q')+2}`. All 4,238 insertions with `|Q| <= 6` passed. This was independently rechecked for `n <= 6` with exact unbounded `m` computation (3,538 cases required exact `m`): zero failures. Tight cases occur: the minimum ratio `e(Q')/F_{m(Q')+2}` is exactly `1.0`, e.g. `e(Q')=21, m(Q')=6` (`F_8=21`) from a staircase insertion. So the tested bound is sharp, not merely slack.

The Fibonacci check is the informative one: it is not implied by Gupta’s GPC census, and it covers some `e` values far beyond the repo’s verified `T(8)=88` range.

Extra check on a tight family: for the staircase cores `W_n`, `6 <= n <= 17`, every proper ideal was tested (264 insertions). All `Q'` satisfied GPC and had a GPC witness using only elements of `W_n`; no failure.

## 4. How the insertion interacts with the GPC comparison choices

The natural attempt — “reuse the exact GPC witness of `Q` in `Q'`” — is **false**. Examples occur already at small sizes:

- `Q =` 3-antichain, `I = {one point}`: some GPC witnesses of `Q` do not lift, although another witness does.
- `Q =` a 3-chain plus an isolated point (`e=4, m=2`), `I = {isolated point}`: `Q'` has `e=10`, and **no** GPC witness using only `Q`-elements works; the second comparison must involve `x`.

Exhaustively, the strong lifting property “`Q'` has a GPC witness entirely inside `Q`” held for all insertions with `|Q| >= 5` through `n=7` (40,090 cases) and for all tested staircase insertions through `n=17`, but failed for some insertions at `|Q| = 2,3,4` (all 3 at `n=2`; 5 of 12 at `n=3`; 1 of 72 at `n=4`). If that strong lifting property were proved for all `n`, it would prove GPC by Theorem A. So it is itself an open strengthening of the target, not a shortcut.

This explains the obstruction: the weights `w(L) =` number of slots for `x` after the last element of `I` vary across the extensions in a GPC child, so the unweighted inequality `t_0 >= t_1+t_2` for `Q` does not automatically survive the insertion. A proof would need a new selection or averaging argument for the two comparisons; simply transporting the witness is insufficient.

## 5. Evidence labels and limits

- **Paper proof:** the equivalence theorems A and B, using Lemma 2 (`[paper proof]` in the core-threshold note) and the Dolores-Cuenca et al. lexicographic-sum closure (`[literature]`).
- **Literature:** Peczarski, `Order 23 (2006) 89–95` (GPC, width two, <=11 elements); Dolores-Cuenca–Guzmán-Sáenz–Kim, `Order 43, 34 (2026)` (lexicographic-sum closure); Gupta, `arXiv:2607.23926v2` (GPC through 14 elements).
- **Experiment:** the 40,177 GPC insertions and 4,238 Fibonacci insertions above, conditional on the audited core generator/extension propagation and the exact bounded minimax.

**Limits.** No exhaustive `n = 15` search was attempted; it is far beyond the available enumeration. The staircase family through `n=17` is a check, not a proof. The equivalence theorem is the decisive result: absent a proof or disproof of GPC, the maximal-insertion question cannot receive an independent PRESERVATION-PROVED or COUNTEREXAMPLE-FOUND verdict.

## Output 796 (msg_1b9ab922400105b8noSvnKsY95)

Addendum on the two optional extended runs:

- The `n = 7` Fibonacci sweep and the partial `n = 8` GPC sweep were both killed by the host (SIGKILL) before completion. They are **not** used in the reported evidence.
- The reported Fibonacci result remains the completed exhaustive `n <= 6` check (4,238 insertions, two independent methods, zero failures).
- The reported GPC result remains the completed exhaustive `n <= 7` check (40,177 insertions, zero failures), including the fully-inside-`Q` witness counts.
- The staircase check through `W_17` was completed independently and is unaffected.

The verdict is unchanged: **INCONCLUSIVE, with the preservation statement equivalent to GPC itself.**

## Output 864 (msg_1b9ac7fe6001Csi0AOSl7XalCh)

Recovery inspection complete; no duplicate work performed.

## State found

- **Conversation/task:** The task was read-only research/reporting. The report was already delivered in the previous turn. No explicit posting/committing action was requested or performed.
- **Git:** Worktree `/home/lubko/soring-fronts/gpc-maximal-insertion-preservation` is at detached `f89f6d0`, `git status --porcelain` has **0 entries**, no stash created by this session, and the reflog shows no commit/checkout action from this session.
- **Board:** I only used `board_digest.py` for reading. I never called any posting API or wrote to Antonina issue #301.
- **Scratch effects:** Only untracked files under `/tmp/opencode` (`probe.py`, `gpc_struct.py`, `fib3.py`, logs). No repo files were written.
- **Processes:** The optional extended `n=7` Fibonacci and partial `n=8` GPC background runs were killed by the host; no scratch processes remain.

## Unfinished work

Nothing required remains. The main report stands as delivered; I did not repeat it. The only incomplete items are the **optional** extra sweeps (`n=7` Fibonacci, partial `n=8` GPC), which were explicitly not used as evidence and would need a fresh run if wanted.

## External effects

I cannot independently audit the backend beyond the tool history: within this conversation no commits, pushes, board posts, or tracked-file edits occurred. If the backend performed actions outside the recorded tool calls, that would need separate review; I see no evidence of any such action.
