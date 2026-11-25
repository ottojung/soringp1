# antonina-IVh02KRbtzjyOMkrf3ouxC-unwounded

Session: ses_e414d0da1ffegthwUgxq3K5wVx
Workspace: /home/lubko/soring-fronts/adaptive-vs-nonadaptive-sorting-number
Created: 1794200760997; updated: 1794200991155

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 82 (msg_1beb4478d001J2la1VNB5inLk7)

## Mathematical finding

**Front attacked:** `adaptive-vs-nonadaptive-sorting-number` — does adaptive decision-tree depth S(n) equal nonadaptive sorting-network depth up to O(1)?

**Result: the front as posed mixes incomparable complexity measures; no nontrivial separation or collapse can be established without first fixing the model. No repository/Lean changes.**

### The obstruction

- `S(n)` (docs/problem.md) is the **height of an adaptive comparison decision tree**: worst-case number of *sequential* comparisons along one root-to-leaf path. It is Θ(log n) in n (information bound ceil(log₂ n!)).
- A **sorting network's "depth"** is the number of *parallel layers* (longest chain of dependent comparators). It is also Θ(log n) in n, but a network of depth d performs up to Θ(n·d) total comparisons, and its per-input evaluation path uses d comparisons *only along dependency chains*, not an arbitrary adaptive sequence.

These are not the same measure: one counts total sequential comparisons on a path; the other counts parallel layers. Comparing them up to an additive O(1) is not well-defined without stating whether "nonadaptive number" means (a) parallel depth, (b) total comparators on the longest path, or (c) a nonadaptive decision tree height (a fixed comparison schedule independent of outcomes, which is exactly a sorting network with one comparator per layer — depth = comparison count).

### What follows honestly

- If "nonadaptive number" means a **nonadaptive decision tree** (fixed comparison sequence, height = comparison count), then it is ≥ S(n) trivially, and the gap D_nonadapt(n) − S(n) is a genuine question. But then it is not "sorting-network depth"; it is nonadaptive comparison complexity, which is known to be Θ(log n) both ways, and additive O(1) equality is not established or refuted by the cited sources (literature.md gives only exact adaptive values and network depth sequences; no theorem on additive gap).
- If it means **sorting-network parallel depth**, the "gap" is definitional (sequential vs parallel), not a separation of adaptive power.
- No single n in the known exact-value tables (n ≤ 22 for S; network depth tables) is accompanied by a verified nonadaptive optimum under a stated definition, so the falsifier (one n with nonadaptive depth > S(n)+C) cannot be honestly exhibited here.

### Classification

- **Conjecture/open:** under the nonadaptive-decision-tree reading, whether the gap D(n) − S(n) is O(1) is open and not settled by available literature.
- **Model-fidelity issue:** the front's wording ("sorting-network-depth") does not match the defined S(n) model; per AGENTS.md model-fidelity rules, this must be resolved before any theorem.

### Next decisive step

Reformulate the front with an explicit nonadaptive model (fixed comparison schedule vs. network depth) and a stated measure (comparison count vs. layers), then either exhibit a verified small-n counterexample or prove the two coincide up to O(1). Until then, no Lean or repository change is warranted.

## Output 246 (msg_1beb5ff88001DP9mgs1wYh1ohQ)

## Recovery status (checked before acting)

- **Worktree:** clean at `6a96398`; no commits, no files added/modified.
- **Durable record:** ledger entry `adaptive-vs-nonadaptive-sorting-number` was still `running`, with **no** `finding_unverified`. So the prior turn completed only reading, not the board report.
- **Board #301:** searched pages 1–3 for the front ID — **no prior post existed**. I posted exactly once (message `sha256:Tr-CU3YI…`, 2026-11-09T05:09:10Z). No duplicate.

## Mathematical finding

**The front as written is a model mismatch; under its literal depth reading the additive-O(1) claim is false, with the gap diverging in the opposite direction.**

- `S(n)` is a **sequential** worst-case comparison count: `S(n) ≥ log₂(n!) = Ω(n log n)`.
- Sorting-network **depth** `D(n)` is **parallel layers**: an explicit Batcher odd-even mergesort has depth `O(log² n)`.
- Therefore `S(n) − D(n) → ∞`; a depth-`d` network also does at most `(n/2)d` comparators total and compares each element at most `d` times. So "nonadaptive depth exceeds `S(n)` by a constant" is false for large `n`, not true.

**Well-posed reading remains open.** If "nonadaptive number" means minimum network **size** `N(n)` (length of a fixed oblivious comparison sequence), then `N(n) ≥ S(n)` trivially and `N(n) − S(n) = O(1)?` is a genuine all-`n` question. I did **not** prove or refute it. The verified data (OEIS A036604/A003070) tabulate adaptive `S(n)` and `⌈log₂ n!⌉`, not `N(n)`; finite small-`n` gaps cannot establish unboundedness.

## Honest limits

- No new theorem about `S(n)` itself; this is a **model-fidelity deduction** plus a front reformulation, not a separation of adaptive vs nonadaptive power.
- No counterexample or all-`n` proof for the size reading.
- No Lean, repo, commit, or test changes; only one board comment. The ledger stays `running` for the keeper to close on agent exit.

## Output 274 (msg_1beb66b74001jLGHf7ZWRvpgls)

## Recovery check complete — no further action

- **Worktree:** clean at `6a96398`; no uncommitted changes.
- **Board #301:** exactly **one** post for this front exists (the 05:09:10Z message `sha256:Tr-CU3YI3hnq9c291wOapiq0w6Jp3grorn6H8O6fprc` by `SoringP1 frontier: adaptive-vs-nonadaptive-sorting-number`). No duplicate to make.
- **Ledger:** still `running` with no `finding_unverified`; the keeper records completion on agent exit. This is expected and not something to edit by hand.
- **No repo/Lean/commit changes** were made at any point.

The investigation is already reported; nothing remains unfinished. Reporting only, no repeated side effects.
