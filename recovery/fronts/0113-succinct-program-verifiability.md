# succinct-program-verifiability

## status

investigated

## origin

ai_proposal_unverified

## agent_id

UBHs6UImsqEdh0VIIpUpBl-profits

## exit_state

clearexit

## question

For SORT-BOUND-U, is there an all-n obstruction showing that no polynomial-size uniform comparison program can have its worst-case sorting height verified in polynomial time without simulating exponentially many permutations, due to the comparison-based test restriction?

## basis

Hyafil–Rivest restriction to pairwise tests, distinction between explicit tree and succinct program, NP certificate size/verification constraints in docs/problem.md.

## falsifier

Give a polynomial-time verifier for some universal succinct class of comparison programs that certifies worst-case height <= k for all x in SORT-BOUND-U with a valid program, or construct such a class and verifier.

## implication

A general verifiability obstruction would rule out many natural NP-certificate forms for the unary threshold even if polynomial descriptions exist, tightening the certificate-soundness/completeness gap beyond quotient-specific arguments.

## finding_unverified

d program yet has no obvious poly-time certificate for “all-good”; worst-case adversarial search over partial orders is exponential in general and comparison structure gives no obvious collapse. Restricting the class to make verification easy tends to break universality for exact `S(n)`.

4. **Attempted falsifier construction.** Tried to find a universal succinct class with efficient verifier:
- **Recursive/adaptive strategy classes:** can encode any strategy, but to certify depth<=k without simulating you need a proof (e.g. minimax bound). Encoding such a proof succinctly is non-obvious and recomputing the bound is the original problem; no obvious polynomial-time verifier avoiding exponential search over the game tree.
- **Sorting networks / oblivious classes:** non-adaptive or restricted; worst-case depth easy to read but class not universal for adaptive `S(n)` (adaptive < oblivious in power). No.
- **Classes with “small test sets”:** 0-1 principle gives a necessary/sufficient test family, but its size is exponential in `n` and no polynomial-time reduction is known for arbitrary comparison programs. No way to exploit comparison restriction to get polynomial test sets in general.

No constructive class+verifier found. All universal candidates either lose succinctness in effect, lose universality for exact `S(n)`, or reduce back to exponential simulation/game-tree evaluation.

**Concrete failed/obstructed approach:** trying to get symbolic verification of an arbitrary adaptive comparison strategy is obstructed by (a) exponential state space of partial orders, (b) 0-1 principle requiring exponential test coverage with no known compression under comparison restriction, (c) Hyafil–Rivest-style separation between arbitrary tests (where construction/verification was structured differently) and comparison tests (structure helps algorithms but hurts succinct verifiability of arbitrary strategies). General-poset hardness does not transfer directly, but the “test restriction” creates a different barrier (the verification/soundness-completeness gap). 

**Finding (mathematical/obstruction):** There is a plausible all-`n` verifiability obstruction for the natural NP-certificate form: for any universal succinct class of adaptive comparison programs, polynomial-time certification of “worst-case height `<= k` for all inputs” appears obstructed by the comparison-based test restriction without simulating exponentially many permutations (coNP-hardness of the “all-good” property for fixed programs combined with universality; no known polynomial test set or structural verifier). I did **not** construct a counterexample/verifier; the obstruction is not disproved. Distinction is important: counterexample search is easy (coNP), all-input certification is hard – this is certificate *completeness* obstruction, not soundness.

**Honest limits:** This is a reasoned obstruction argument, not a formal proof of `SORT-BOUND-U ∉ NP`. It exploits comparison structure and the 0-1/minimax view; a clever class+verifier might exist. No repository/Lean changes made (no genuinely substantive independently checkable new theorem/counterexample). No repetition of known exact values/barriers beyond what’s cited.

**Next decisive question:** is “there exists a succinct comparison program of depth<=k” in `NP` under some non-obvious certificate (not the program+simulation), or is this a property that becomes PSPACE-hard to verify in this restricted class? That’s the gap to tighten.

## Other metadata

```json
{
  "finished_at": 1793480115.3505225,
  "started_at": 1793479714.748489
}
```
