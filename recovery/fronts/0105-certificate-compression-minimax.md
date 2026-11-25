# certificate-compression-minimax

## status

investigated

## origin

ai_proposal_unverified

## agent_id

tuOjpF9jdg9JrEbkOSTyA2-spokesman

## exit_state

clearexit

## question

Can the exponential winning frontier be compressed by exploiting the exact minimax structure (not just symmetry/isomorphism) into a polynomial-size checkable certificate for all-n optimal strategies?

## basis

Winning frontier barrier shows 2^Omega(n log^2 n) nonisomorphic winning states; framed certificate frontier discusses polynomial completeness as open; sparsity blocks many-one NP-hardness but doesn't guarantee NP membership.

## falsifier

Show that optimal strategies for the sorting game have superpolynomial "certificate complexity" under all locally checkable proof systems (e.g. due to the 2^Theta(n log^2 n) frontier states), or construct a polynomial family.

## implication

Polynomial-size completeness would put SORT-BOUND-U in NP (new membership class); a barrier would rule out this route.

## finding_unverified

he move is present, children are valid, no cycles, and all leaves total within budget — this is poly in DAG size regardless of how many states exist in the full frontier. The “hard” part is *existence* of some polynomial-size DAG σ with this property. The frontier gives a lower bound on the *state space* size, not an obvious lower bound on the *description* of some compressed strategy.
3. **Barriers cut different directions.** `SORT-BOUND-U` is sparse ⇒ many-one NP-hardness would imply `P=NP` (Mahaney). The ATM gives `SORT-BOUND-U ∈ PSPACE`. Neither guarantees NP membership nor forbids it; they rule out a naive many-one hardness route. Also general-poset NP-hardness results (Hyafil–Rivest, Laber–Nogueira) don’t transfer to the fixed comparison-test family `S(n)`. These are soundness/completeness distinctions: certificate *soundness* is easy to check; *completeness* (a small witness exists for all yes-instances) is the open question.

**Concrete obstruction / failed/blocked approach:**

- **Pigeonhole on frontier states is insufficient.** To force superpolynomial size of *every* optimal strategy, you’d need that every optimal σ must branch differently on “most” frontier states and you can’t merge them. But adversary cannot force σ to query arbitrary pairs — σ chooses queries adaptively. An optimal σ could use a highly structured strategy (e.g. follow a fixed merge pattern, or use a decision rule based on some invariants like “sort by first difference in a canonical ordering”) that handles many different poset types by the same local rule while still achieving optimal height. The rectangular-chain family is a large family of posets, but optimal play might not require distinguishing them all if the strategy is global/recursive. Showing this is impossible for all locally checkable proof systems would require a stronger lower-bound technique (e.g. strategy complexity / branching program lower bounds) that doesn’t obviously follow from the combinatorial frontier count alone.
- **No obvious reduction from frontier to certificate lower bound.** The frontier is an existence of many winning states; to get a certificate lower bound you need a kind of “separating” family that forces the verifier/certificate to encode information. But with adaptive queries and the ability to use global structure, compression is plausible in principle. I don’t see a standard argument that turns “2^Θ(n log^2 n) winning states” into “every optimal strategy has superpolynomial DAG size” without additional assumptions about the strategy class.
- **Exact obstruction:** the combinatorial frontier is necessary but not obviously sufficient as a barrier to NP membership via strategy compression. The real obstruction is the lack of either (a) a polynomial strategy construction, or (b) a lower-bound technique for adaptive comparison strategies that survives compression by minimax structure. Neither is present in the cited material.

**Honest limits:** I cannot produce a proof ruling out polynomial-size certificates, nor a construction. The strongest defensible claim is: the frontier raises the burden (shows the naive tree is bad and the state space is large), sparsity blocks the easiest NP-hardness route, `PSPACE` is the best known upper bound, and a true barrier would need a strategy-complexity lower bound that exploits the *minimax/adaptive* structure rather than just counting reachable winning states. This is the precise gap. No repository changes are warranted by the above.

## Other metadata

```json
{
  "finished_at": 1793439369.5920038,
  "started_at": 1793438599.827097
}
```
