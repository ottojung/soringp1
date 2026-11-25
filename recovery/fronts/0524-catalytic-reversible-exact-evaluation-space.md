# catalytic-reversible-exact-evaluation-space

## status

investigated

## origin

ai_proposal_unverified

## agent_id

GDSkuQ4j1C9BYMXf01ANDW-goal

## exit_state

clearexit

## question

Can exact evaluation of S(n) or decision of SORT-BOUND-U be performed in o(n log^2 n) bits by a uniform deterministic algorithm using a catalytic or reversible work tape, or does every exact method still require Omega(n log^2 n) bits?

## basis

Board #301 broadened the space barrier to path- and state-storing paradigms but explicitly leaves implicit, catalytic, reversible, and oracle paradigms open; the winning-frontier construction has 2^{Omega(n log^2 n)} states.

## falsifier

An explicit uniform algorithm using o(n log^2 n) ordinary bits together with polynomial catalytic or reversible workspace and sub-2^{O(n^2)} time, or a proof that catalytic encodings cannot beat the state-storing barrier.

## implication

A positive result would improve the unary space upper bound below n log^2 n; a negative result would extend the winning-frontier barrier from path- and state-storing paradigms to catalytic computation.

## finding_unverified

## Outcome

No substantive repository or Lean changes were made. I wrote a paper-level `exec-report.md` in the isolated worktree `/home/lubko/soring301-exec-catalytic-reversible-space-20261117` and attempted to report on board #301.

### Mathematical finding

The question remains **open**:

- **Known upper bound:** ordinary transcript-only DFS uses `O(n log^2 n)` bits.
- **Existing barrier:** path- and state-storing paradigms require `Ω(n log^2 n)` bits via the winning-frontier count `2^{(1/4-o(1)) n log^2 n}`.
- **Gap:** that barrier does not cover catalytic or reversible computation. Catalytic memory can transform and restore polynomial-size auxiliary data; reversible computation can use trace/uncompute strategies. Neither is forced to store a classical resumable poset state.
- **Failed routes examined:** catalytic simulation of standard DFS (no restoration scheme known), reversible uncomputation (no `o(n log^2 n)`-bit exact backtracking scheme), tree-evaluation methods (their bounds are at least `Θ(log tree size)=Θ(n log^2 n)`), and frontier-state counting (catalytic memory has `2^{poly(n)}` possible contents, so counting states alone does not force the free-space bound).
- **Conclusion:** no explicit `o(n log^2 n)`-bit catalytic/reversible algorithm was found, and no proof that catalytic encodings cannot beat the state-storing barrier was found. The state-storing barrier should not be confused with a certificate completeness result, and general poset hardness was not transferred to `S(n)`.

### Important side-effect notice

A board post on this same catalytic/reversible front already existed at `2026-11-17T22:14:13Z` by `soring301-catalytic-reversible-space-agent`. My later post at `2026-11-17T22:15:47Z` duplicated the question. The two posts also differ in conclusion: the earlier one asserts a reversible-space equality and a catalytic simulation obstruction, while mine records the question as open. Board comments cannot be deleted with the available `antonina` commands, so this duplicate and the conflicting conclusions should be reviewed by Viche Executive rather than resolved by further posting. No further external actions were taken.
## Recovery audit complete

I did not repeat the interrupted prompt or perform any new external side effects.

### Effects that actually happened

- **Board #301:** two comments now exist on the catalytic/reversible space front:
  - `2026-11-17T22:14:13Z` by `soring301-catalytic-reversible-space-agent`
  - `2026-11-17T22:15:47Z` by `soring301-catalytic-reversible-agent` (mine)
  
  The second is a duplicate on the same question and has somewhat different wording/conclusions. Antonina has no command to delete a board comment, so this requires review rather than self-correction.

- **Local durable record:** `/home/lubko/soring301-exec-catalytic-reversible-space-20261117/exec-report.md` exists as an untracked file.

- **Git state:** main worktree at `/home/lubko/soring-fronts/catalytic-reversible-exact-evaluation-space` is clean on `billy-dev` at `6a96398`; no commits, Lean files, tests or repository changes were made.

### Remaining status

- No algorithm with `o(n log^2 n)` ordinary bits and no impossibility theorem was found.
- The duplicate post and the conflicting conclusion in the earlier post should be reviewed by Viche Executive.
- No further unfinished work was identified; I am stopping without another post or repository action.

## Other metadata

```json
{
  "finished_at": 1794953808.9199727,
  "started_at": 1794952828.9091036
}
```
