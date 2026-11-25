# ply-kraft-comparison-constraint

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ic7Au9tlW83J97h5fK0cIf-snorted

## exit_state

clearexit

## question

For the antichain A_n and any binary comparison tree of height k sorting all permutations, let f_v be the branching/feasibility constraint from the partial-order comparability (not just leaf count); does the comparison-tree validity force a strict all-n strengthening of Kraft/leaf-sum inequalities beyond n! <= 2^k that is independent of linear-extension counts in some regimes?

## basis

Repo shows information bound is necessary but not sufficient (S(12)>29), ply/one-ply obstruction analysis exists, Kraft was mentioned in dispatched fronts but comparison-validity (not arbitrary prefix codes) remains underexplored as an all-n algebraic constraint.

## falsifier

Exhibit for arbitrarily large n some comparison-valid strategy family (or prove for all comparison trees) that satisfies all order-consistency constraints yet the 'ply' Kraft bounds coincide with the trivial 2^k >= n! bound with no all-n gap for the feasibility function, or construct a counterexample poset class where linear-extension counting already captures all constraints.

## implication

A true all-n comparison-validity strengthening of Kraft-type bounds would give a nontrivial lower bound route for S(n) distinct from the information bound log2 n! and from scalar invariants, potentially exposing new obstructions without reducing to arbitrary poset #P-hardness.

## finding_unverified

Let us look up the one-ply obstruction more - it shows L1 > L0 is possible due to split structure constraints. Also look up the script to understand.

Let us run the one-ply obstruction to see it in action.

Let us start by examining the full picture. I need to study the specific front more.

Let us look up "Kraft" more broadly - maybe in some notes or in how people phrase it. Also look up the full board digest around that front again - the front says "Kraft inequality and comparison model constraints; 1/3-2/3 literature notes feasibility is subtle but no universal all-n Kraft+feasibility gap theorem is recorded." Also "the comparison-realizable partition classes are dense enough that no fixed constant-factor information gap holds for all large n"

Let us think again about the Kraft inequality connection.

Let us understand the one-ply obstruction better and think about this front.

**Finding (paper deduction, no repo/Lean changes):** For a binary comparison tree that sorts all permutations from antichain A_n, Kraft inequality \(\sum_{\text{leaves}} 2^{-d_\ell}\le 1\) (hence \(n!\le 2^k\)) is necessary for *any* prefix code regardless of test type. Comparison-validity restricts which splits are admissible given the current poset, but this is a constraint on *which* binary trees exist, not an all-n strengthening of the Kraft/leaf-sum inequality form itself.

**On "ply Kraft bounds" / feasibility function f_v:** The one-ply obstruction \(L1\) (and recursive variants) does give strictly stronger local bounds than \(L0=\lceil\log_2 e(P)\rceil\) in some states (e.g. n=5 witness), but \(L1\) is computed entirely from linear-extension counts \(e(P)\) of children/split structure. Known results (e.g. \(S(12)>29\), non-monotonicity \(e(P)\nrightarrow F(P)\) functionally, same-e different-F) show split-admissibility matters, but I find no evidence of a comparison-validity constraint that is *independent of linear-extension counts*. The constraints reduce to poset structure as captured by \(e(P)\)-based split feasibility.

**Falsification attempt / honest limits:** I could not construct (and know of no known result establishing) an all-n strengthening of the Kraft inequality form beyond \(n!\le 2^k\) that is independent of \(e(P)\) counts. Counterexamples to "all-n +1 beyond rounding" already exist (n=20,21 tight). The natural strengthening candidates (one-ply/higher-ply) are \(e(P)\)-dependent. The most plausible disproof of the claimed *independent* strengthening is: comparison-validity obstructions are captured by linear-extension-counting/split-admissibility (the falsifier's option 2) rather than producing an inequality independent of \(e(P)\). No substantive new theorem/counterexample ready for integration; no Lean/repo changes proposed.

## Other metadata

```json
{
  "finished_at": 1793766725.3922966,
  "started_at": 1793760029.5995858
}
```
