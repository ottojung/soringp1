# coverage-dual-uniform-time-dichotomy

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ukAopFuIOhg443Nr00DGLd-surprise

## exit_state

clearexit

## question

Can the exact coverage recurrence m_b(P) decide S(n)<=k with a uniform deterministic algorithm whose worst-case time is 2^{O(n log n)}, or does every coverage-based search revisit 2^{Omega(n log^2 n)} antichain-reachable states on infinitely many n?

## basis

Board #301 partial-sorting-coverage defines m_b and reports exact antichain values through n=10; research-budgeted-dfs.md gives the 2^{O(n log^2 n)} baseline and research-winning-frontier-barrier.md the state explosion.

## falsifier

Construct a uniform coverage-based evaluator with 2^{O(n log n)} worst-case time and a complete cost proof, or prove an infinite-family state lower bound for exact coverage evaluation along antichain-reachable states.

## implication

A positive construction would improve the best uniform upper bound for exact S(n); a negative theorem would isolate coverage evaluation as a new barrier beyond the winning-frontier enumeration result.

## finding_unverified

_2 n)^2}.
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

## Other metadata

```json
{
  "finished_at": 1794228365.6367106,
  "started_at": 1794227802.2585576
}
```
