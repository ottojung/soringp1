# antonina-ukAopFuIOhg443Nr00DGLd-surprise

Session: ses_e3fb06c34ffeRtqSc9saxeLvtp
Workspace: /home/lubko/soring-fronts/coverage-dual-uniform-time-dichotomy
Created: 1794227803166; updated: 1794228329993

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 241 (msg_1c056bc7c001K2UaxXJc9cbq24)

## Finding

I studied `AGENTS.md`, `docs/problem.md`, board #301 (the `partial-sorting-coverage` post and its corrections), `research-budgeted-dfs.md`, and `research-winning-frontier-barrier.md`.

The front’s **state-space negative is true in a strong form**, but it does **not** establish a running-time lower bound for arbitrary coverage-based evaluators.

### 1. New height-two extension lemma

Let `P` be a height-two poset with minimal part `A`, maximal part `B`, and exactly `t` relations, all of the form `a < b`. Then

\[
e(P)\ \ge\ \frac{n!}{2^t}.
\]

**Proof.** A uniformly random permutation of `A ∪ B` extends `P` exactly when all `t` edge-events `a` before `b` hold. Condition on the global minimum:

- if it is a non-isolated maximal element, some relation fails;
- if it is a minimal element `a`, all edges incident to `a` are automatically satisfied, leaving `P-a`;
- if it is an isolated maximal element, delete it.

Hence, with `deg` in the bipartite graph,

\[
\Pr[\text{all edges hold}]
=\frac1n\left(\sum_{a\in A}\Pr[G-a]+\mathrm{iso}(B)\Pr[G-b]\right).
\]

Induction gives

\[
\ge \frac{2^{-t}}n\left(\sum_a 2^{\deg(a)}+\mathrm{iso}(B)\right)
\ge \frac{2^{-t}}n\left(|A|+t+\mathrm{iso}(B)\right)
\ge 2^{-t},
\]

using `2^d ≥ 1+d` and `t ≥ |B|−iso(B)`. ∎

I also exhaustively checked all bipartite graphs with parts up to `4 × 4` by subset DP: no violations; equality occurs at matchings.

### 2. The antichain-rooted coverage frontier is `2^{Ω(n log² n)}`

Fix any `c < 1`, and put `t = floor(c n log₂ n)`. Using Sergeev’s theorem `S(n)=C(n)+d(n)` with `d(n)=o(n)`, we have `t < S(n)` for all sufficiently large `n`.

Construct height-two posets as the disjoint union of:

- `m = d(n)+1` copies of the 3-edge star `K_{1,3}`; each has ratio  
  `e·2^3/4! = 2`;
- one bipartite graph `H` on `n−4m` vertices with `t−3m` cross edges, chosen from `≈(n−4m)²/4` possible edges.

Ratios `e·2^t/n!` multiply over disjoint unions, so the lemma gives

\[
e(P)\ \ge\ 2^m\,\frac{n!}{2^t}\ >\ 2^{S(n)-t}.
\]

Thus at depth `t`, the sound extension cap

\[
m_b(P)\le \min(2^b,e(P))
\]

is **vacuous**: these states have more than enough linear extensions to fill the remaining `S(n)−t` levels.

Each constructed poset is reachable from the antichain in exactly `t` comparisons, since every edge is a cover and there are no length-two paths, so no added edge is ever implied. The number of choices is

\[
\binom{\lfloor (n-4m)^2/4\rfloor}{t-3m}
=2^{(c-o(1))\,n(\log_2 n)^2}.
\]

Dividing by at most `n!` isomorphic relabellings leaves

\[
2^{(c-o(1))\,n(\log_2 n)^2}
\]

pairwise nonisomorphic states.

So for every `c<1`, the full exact-coverage recurrence at the exact optimal budget `S(n)` contains `2^{c n log² n}` antichain-reachable subposets, and the extension-count prune cannot remove them.

### 3. What this does and does not prove

**Proved:** the natural `2^{O(n log² n)}` state frontier of the exhaustive coverage recurrence is tight in exponent. This extends the winning-frontier barrier from *winning* states at the information budget to *coverage-cap* states at the exact optimum.

**Not proved:** a `2^{Ω(n log² n)}` time lower bound for every coverage-based algorithm. A symbolic or selective evaluator need not enumerate the recurrence DAG. The proposed dichotomy is therefore not exhaustive: a `2^{O(n log n)}` evaluator could coexist with this state explosion.

The `e(P)` cap is a **soundness** fact, not a completeness or algorithmic-reduction theorem. General-poset hardness and counting results still do not transfer to the antichain root.

### 4. Failed/obstructed route

The direct route from the extension cap to the algorithmic negative fails exactly at the step “many subproblems ⇒ many necessary evaluations.” The height-two family gives exponentially many sound, cap-unprunable states, but does not show that any must be evaluated by a non-enumerative method. Proving the universal negative would be an unconditional super-polynomial lower bound for a sparse unary problem in `PSPACE`, beyond present technique.

I posted this concise finding to board #301 under the front ID. No repository or Lean changes were made; the worktree remains clean at `6a96398`.

## Output 312 (msg_1c05781df001USf9XvhW7H2Kto)

Recovery inspection complete. I did not repeat the research task or repost anything.

### State observed

- **Working directory:** `/home/lubko/soring-fronts/coverage-dual-uniform-time-dichotomy`
- **Git:** clean worktree on `billy-dev` at `6a96398`; no commits, no modified or untracked repo files.
- **Scratch artifacts:** only `/tmp/opencode/board_post.md` and the two small lemma-check scripts remain. No repository changes.
- **Board #301:** exactly **one** post exists under `SoringP1 frontier: coverage-dual-uniform-time-dichotomy`, timestamped `2026-11-09T12:44:02.116Z`, body length 4409 chars. No duplicate was created.
- **Durable ledger:** `~/.local/state/soringp1/frontier-ledger.json` still records `coverage-dual-uniform-time-dichotomy` as `status: "running"` for agent `ukAopFuIOhg443Nr00DGLd-surprise`.

### Effect assessment

The only completed external effect was the single board #301 post. The mathematical result and its honest limits were already delivered in the prior turn:

- height-two extension lemma `e(P) ≥ n!/2^t`;
- `2^{Ω(n log² n)}` antichain-reachable nonisomorphic coverage states at the exact optimal budget;
- extension-cap pruning is vacuous on that family;
- this is a state-space frontier result, **not** a universal running-time lower bound, so the proposed `2^{O(n log n)}` algorithmic positive remains open.

No unfinished mathematical or repository work remains.

The ledger entry still being `running` appears to be a keeper/agent-lifecycle record rather than a research action. I did not change it, because editing the agent-pool ledger is an operational step outside the research task and the recovery instruction says not to guess at uncertain effects. That status should be reconciled by the keeper or reviewed operationally.
