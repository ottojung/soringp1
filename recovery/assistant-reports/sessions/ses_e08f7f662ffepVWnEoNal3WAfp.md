# antonina-pOjCUf9Wt99KvAoKroFpJc-tracts

Session: ses_e08f7f662ffepVWnEoNal3WAfp
Workspace: /home/lubko/soring-fronts/minimal-v-fotc-optimal-program-fragment
Created: 1795145861770; updated: 1795146188424

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f7080c07001Jbd9aY4ySoFP63)

I'll start by understanding the repository state, the relevant documents, and what "billy-dev" refers to.

## Output 21 (msg_1f7081897001S5PrpGW6CEQ0gQ)

I'm on branch `billy-dev` with a clean worktree. Let me read the core documents and locate the research board #301 and the FO(TC) note.

## Output 62 (msg_1f7085bae001YO4ZF81itfscXb)

Let me locate the FO(TC) strategy-program note on main and the assigned research issue.

## Output 119 (msg_1f708a59f001aWBrJaxY2w2XEy)

Let me verify the evidence claims (ledger search), look at how to post to the board, and check the primary literature on FO(TC) variable hierarchies.

## Output 163 (msg_1f70a59b00016ZjpTDRC1QgZsO)

Let me research the primary literature on bounded-variable transitive-closure logic to make sure my analysis is sound.

## Output 178 (msg_1f70a6dba001reB926X1AH3I7n)

Let me read the winning-frontier barrier note — it may bear directly on whether state-compressed optimal programs can be polynomial.

## Output 189 (msg_1f70b29c6001hJl4BX7OXbm8bV)

Let me retry the literature check with a single query.

## Output 218 (msg_1f70ba2a7001ku66gBf6P0yrvl)

I have enough context. Let me verify one more time that this front is the only one on this topic and check the exact model constraints around vocabulary, then I'll report.

## Output 254 (msg_1f70c71f5001911QVSdt9Q41Mi)

The board post succeeded. Let me verify it landed and that my worktree stayed clean.

## Output 269 (msg_1f70c883e001fTRO0G66HQ3ouD)

## Report — front `minimal-v-fotc-optimal-program-fragment` (billy-dev)

**Status:** one finding posted to Antonina issue #301. No Lean, repository, test, workflow, or ledger changes; worktree clean. No theorem completion for `S(n)`/`SORT-BOUND-U` claimed.

### What I studied
`AGENTS.md`, `docs/problem.md`, the current #301 digest, the refereed FO(TC) strategy-program note on main (`research-fotc-strategy-programs.md`, commits `9018729`/`6cddeaa`), the split-schema barrier and publication record, the winning-frontier barrier, and the 587-front ledger (confirming this is the only front on minimal `v`). I distinguished single-formula expressiveness from program expressiveness, and certificate **soundness** from **completeness**.

### Mathematical finding (paper proof / deduction)
The parameter `v` **collapses** for strategy programs. In the fixed-interpreter model with `|p_n| = poly(n+k)` and a fixed polynomial clock `L^d`, for every fixed `v, v' ≥ 2` the solvable class satisfies `C_v = C_{v'}`.

Proof idea (`v=3 → v=2`): a `v=3` guard uses names `{x,y,z}`; each free context variable `z` is unrolled into `O(N)` rules with `z` replaced by each constant `c ∈ [N]`, `N = Θ(n+k+1)` being known to `p_n`. Quantification over `z` becomes a sequential scan of `O(N)` control labels with early accept/reject (no auxiliary memory needed). A context-dependent node `[TC_{x,y} θ(x,y,z)](s,t)` with `m=1,a=1` becomes, per constant `c`, the `v=2` node `[TC_{x,y} θ(x,y,c)](s,t)` (`a+2m=2≤2`). Higher `a`/`m` unrolls into `O(N^k)` rules (fixed `k`); wider relations are encoded by families of binary relations plus unary index relations. Overhead `N^{O(v)}` is absorbed by a fixed clock exponent. `C_2 ⊆ C_3` is syntactic.

**Consequence:** the requested falsifier is **impossible** — there is no infinite family where `FO(TC)_2` fails at budget `S(n)` but `FO(TC)_3` succeeds (or conversely), and "context width must grow with `n`" cannot hold as an expressiveness phenomenon. The weakest fragment sufficient for Conjecture C, if any fixed fragment suffices, is `FO(TC)_2` — vacuously: if any fixed fragment admits a polynomial-size optimal family, so does `v=2`. The `Σ₂^P` accounting is automatically robust to `v ≥ 2`.

### Serious falsification attempt
I tried context-dependent reachability with externally quantified `z`, nested `TC` carrying `z`, and endpoint width `m=2`; each has a polynomial `v=2` simulation. No counterexample found. The genuine scope caveat: the collapse holds for **programs** (multi-rule control flow, polynomial clock), not single fixed-size formulas — for single formulas `FO(TC)_2` and `FO(TC)_3` genuinely differ, so the note's Section 2.3 statement is correct in its own scope but does not transfer.

### Honest limits
This is a deduction, not kernel-checked. It does **not** prove Conjecture C, `SORT-BOUND-U ∈ Σ₂^P`, any lower bound, or construct a `v=2` optimal sorter. The real obstruction to exact optimality is unchanged: computing the minimax-optimal next comparison in polynomial time (linear-extension counting is #P-complete; the winning-frontier bound is explicitly an enumeration barrier, not a time lower bound). The front should be reframed around Conjecture C / polynomial-time minimax selection rather than `v`. Web literature search was unavailable here, so I relied on the note's cited primary sources (Immerman, *Descriptive Complexity* ch. 7) and did not independently confirm a published statement of this collapse.

## Output 294 (msg_1f70cdc58001XmwlX5M0n3DQ9X)

**Recovery check (billy-dev, inspected now):**
- **Git:** clean worktree at `6a96398` (`billy-dev`); no commits or repository changes made.
- **Board #301:** my comment **already posted** and present — `[2026-11-20T03:42:25.997Z] SoringP1 frontier: minimal-v-fotc-optimal-program-fragment` (id `sha256:LqOSH7lxPPV8zAArVRUs3XL2HkW65PRkbQ4GujwNxQg`), verified via `board_digest.py --contains "variable bound collapses"`.
- **Local artifacts:** `/tmp/opencode/board_post_vcollapse.txt` and `/tmp/opencode/board_post_result.json` exist (from that post).

**Conclusion:** the previous turn’s external side effect (the #301 post) completed successfully. There is **no unfinished work** and I will **not** repeat the post, commit, or other actions.

**Finding already reported:** in the fixed-interpreter FO(TC) strategy-program model, the variable bound collapses for programs — for every fixed `v,v' >= 2`, `C_v = C_{v'}` (so `v=2` suffices if any fixed fragment suffices; no `FO(TC)_2`-vs-`FO(TC)_3` separation or forced growth of `v`/context width is possible). This does **not** prove Conjecture C, `SORT-BOUND-U ∈ Σ₂^P`, any lower bound, or construct an optimal sorter (deduction, not kernel-checked). The real obstruction remains polynomial-time minimax/optimal-comparison selection. If you need anything further (e.g. a refined argument or reframing the front), I can continue from this state.
