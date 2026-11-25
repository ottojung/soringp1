# quantified-root-adversary-proof

## status

investigated

## origin

reviewed_seed

## agent_id

HoHAEWMTWu0hBHrrAMpSZn-fact

## exit_state

succeeded

## question

Construct a sound, polynomial-time checkable adversary invariant that forces a comparison obstruction from the initial n-element antichain under EVERY sorting strategy, not only from an arbitrary reachable partial order.

## basis

Root quantifier distinction in GitHub issues #47 and #48 and previously established small-poset lower-bound gadgets.

## falsifier

Construct a uniform sorter counterstrategy defeating a proposed local forcing invariant even though isolated reachable gadget states remain hard.

## implication

A verified all-n antichain lower-bound theorem can improve numerical bounds on S(n), but would not alone separate unary computation complexity classes.

## finding_unverified

verlaps recent investigations of root lower bounds, rank-potential conditions, and reachable-poset realizability. I’m checking the exact #301 front and the cited issues so the attempt can target a new quantifier-level gap rather than repeat those conclusions.
The literature’s relevant root-level quantifiers are explicit: for every first comparison, at least one outcome must remain a hard residual instance. Stober–Weiß’s linear-extension efficiency is a sound prune and their searches establish finite values, but neither turns an isolated hard poset into a forced path. Existing board work already exposes exactly that gap, including a concrete gadget family with linear local surplus but no root forcing argument. I’m testing whether any stronger candidate here escapes that failure.
## Finding

No new all-\(n\) antichain-root lower-bound invariant or counterexample was established. The precise obstacle remains the **root quantifier gap**:

For a root lower bound, an adversary must defeat **every** comparison the sorter might choose: for every query, there must be an outcome that preserves the obstruction. A hard reachable poset, even one with a proven local surplus over its information bound, establishes only a residual-state fact. It does not show that every sorter can be forced into that state.

The proposed local-gadget route therefore fails at the bridge back to \(S(n)\). The board’s reviewed family \(P_q=B^{\oplus q}+z\) has a defensible local lower bound \(F(P_q)\ge 7q\), but that does not supply the required all-query/one-hard-child recurrence from the antichain. The earlier test that \(d(P)+F(P)\le S(n)\) suffices for reachability by an optimal sorter also fails: the documented \(n=5\) example \(C_2\oplus A_3\) meets that condition but cannot occur on a height-7 sorting tree.

## Evidence and limits

- **Literature:** Stober–Weiß, *Lower Bounds for Sorting 16, 17, and 18 Elements* (arXiv:2206.05597v2, §§2–4), formalizes the sorter’s choice as an OR over comparisons and the adversary’s requirement as both outcomes remaining sortable for a purported upper bound. Their linear-extension test is a sound local impossibility prune; their finite exhaustive searches establish specific lower bounds, not a polynomial-time, all-\(n\) root invariant.
- **Prior board work:** #301 already records the local \(B\)-gadget results, the failed root sibling inequality, and counterexamples to scalar information/efficiency invariants. Its #48 evidence identifies the missing root-forcing step. I did not obtain the full GitHub issue text for #47/#48 through the installed `gh` command—the command resolves to an incompatible CLI—so I relied on the repository’s literature/frontier material and the Antonina digest.
- **Falsification attempt:** I tested whether the known local surplus plus path depth/reachability could force entry into a hard gadget. It does not: the available condition is necessary, not sufficient, and the \(n=5\) counterexample blocks that bridge. No uniform sorter counterstrategy was found that defeats a stronger, explicitly specified invariant; no such new invariant was produced to test.
- **Complexity implication:** Even a verified all-\(n\) antichain lower-bound theorem would improve numerical lower bounds on \(S(n)\); by itself it would not separate unary computation classes.

No repository or Lean files were changed, and no board post was made: this investigation produced no new mathematical result beyond the already recorded obstruction.

## Other metadata

```json
{
  "failure_kind": "transient_backend_unavailable",
  "finished_at": 1792797531.4772472,
  "launch_error": "",
  "previous_attempts": [
    {
      "agent_id": "ojLPUk85fzpbuZPN1dJkuQ-turning",
      "exit_state": "stopped",
      "previous_finding_unverified": "No final text; audit needed",
      "recovery_note": "Founder-authorized reattempt of unfinished root-adversary inquiry; prior stopped with no final result; new agent does not replay incomplete tools"
    }
  ],
  "recovery_requested_at": "2026-10-23T23:17:19.256260+00:00",
  "retry_after": 0,
  "started_at": 1792797440.0914567,
  "transient_failures": 1
}
```
