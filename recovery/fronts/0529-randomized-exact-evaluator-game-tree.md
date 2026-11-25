# randomized-exact-evaluator-game-tree

## status

investigated

## origin

ai_proposal_unverified

## agent_id

9RQTawMbJktgaZkvZncTnJ-silver

## exit_state

clearexit

## question

Can a randomized Las Vegas algorithm compute S(n) exactly on input 1^n in expected time 2^{o(n log^2 n)} or expected workspace o(n log^2 n), using coin-flip-guided minimax/game-tree pruning to beat the deterministic transcript- and state-storing barriers?

## basis

The only known uniform evaluator is deterministic at 2^{O(n log^2 n)} time / O(n log^2 n) space and the winning-frontier count rules out state enumeration (docs/research-*.md); no randomized evaluator or randomized lower bound appears anywhere in the 526-front #301 ledger.

## falsifier

Establish a Yao-style average-case lower bound: exhibit a distribution on adversary states/paths on which every correct randomized evaluator explores at least 2^{Omega(n log^2 n)} nodes in expectation or retains Omega(n log^2 n) bits, covering randomized pruning.

## implication

A positive result improves the uniform upper bound for exact unary S and places evaluation in a randomized subclass; a negative result extends the winning-frontier and space barriers from deterministic to randomized algorithms, requiring a genuinely new lower-bound method.

## finding_unverified

log² n)}` would give `SORT-BOUND-U ∉ P` and hence `P ≠ PSPACE` (problem.md), which AGENTS.md forbids pursuing.
4. **The claimed complexity implication is illusory:** a Las Vegas result entails an equally fast per-`n` deterministic procedure, and tally languages are already in P/poly.

I also separated the relevant models: Saks–Wigderson's `O(N^{0.753})` randomized AND-OR speedup relies on a distribution over leaf assignments (many inputs) and an explicit tree — both absent here — and general-poset hardness (Fibonacci threshold PP-hardness, `#LE` `#P`-hardness) does not transfer to the fixed family `S(n)` without a reduction; sound pruning rules are not complete certificates.

## Honest limits
This is a per-input-length model theorem, not a uniform deterministic algorithm (`r(x)=d(x)` pointwise does not build one procedure for all `n`; the nonuniform consequence is covered by P/poly). It assumes zero error, exactly the front's "exact" requirement. It does **not** prove that no faster deterministic evaluator exists — that remains the genuine, open upper-bound frontier. No repository changes were made.

Posted once to board #301 at `2026-11-17T23:58:38Z` under author `SoringP1 frontier: randomized-exact-evaluator-game-tree` (verified sole matching post, body matches local draft, no duplicate).
This is a re-injection of the backend-recovery guard, not new instructions to research. I must not repeat anything blindly. Let me re-verify the durable state to confirm exactly what already happened and that nothing is pending or duplicated.
**State re-verified — nothing pending, nothing duplicated, nothing to continue blindly.**

## Effects actually happening (confirmed durable)
- **Board #301:** exactly **one** comment posted by `SoringP1 frontier: randomized-exact-evaluator-game-tree` at `2026-11-17T23:58:38.059Z` (local draft `/tmp/opencode/rand_front_board.md` byte-identical to posted body; 5,509 chars). No duplicate post; the only other matching message is the earlier Viche Executive continuity pass at 23:53:19Z (not by me).
- **Post content:** rigorous `[deduction]` finding that a Las Vegas (zero-error) evaluator's expected cost on the **single input** `1^n` equals the best deterministic evaluator's cost at that input; Yao's distribution over inputs is vacuous here; the falsifier's lower bound collapses to a deterministic statement; a general-time version would imply `P ≠ PSPACE` (out of scope).

## Effects NOT happening now (confirmed absent)
- No re-post, no duplicate commit, no repository edit.
- `git status` clean on `billy-dev` at `6a96398`; **0** modified/untracked files; no new commits or stashes.
- No Lean/tests/scripts changes.

## Durable task-record state
- Ledger entry `randomized-exact-evaluator-game-tree`: `status: running`, `exit_state: null`, `started_at: 1794958715.88`, `origin: ai_proposal_unverified`. I did **not** edit it manually (claim-once reconciliation is the keeper's job); it should reconcile when the managed agent exits with a terminal state.

## Conclusion for this resume cycle
The interrupted turn's work **has already completed**: the attack was performed, the finding was written, and it was posted exactly once. There is no unfinished duplicate action. The only remaining lifecycle item is external/keeper-managed (agent exit → ledger reconciliation → keeper dispatch of the next front), which I should not touch manually.

**No new side effects were performed in this pass, and nothing was re-posted or re-committed.**

## Other metadata

```json
{
  "finished_at": 1794959986.0481358,
  "started_at": 1794958715.8787024
}
```
