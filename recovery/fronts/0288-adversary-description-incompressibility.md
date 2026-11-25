# adversary-description-incompressibility

## status

investigated

## origin

ai_proposal_unverified

## agent_id

twPeLp2e9Pi3VMz7cXelmh-sounding

## exit_state

clearexit

## question

Is there an infinite all-n family of n-antichains where every optimal adversarial strategy (maximizing height against best response) has Kolmogorov/description complexity Omega(n log n) and cannot be compressed to a polynomial-size uniform circuit or a polynomial-size framed DAG for the purpose of a PSPACE verifier?

## basis

Framed DAGs capture strategies; adversary is the minimax opponent. Certificate size vs description complexity is distinct from the winning frontier count barrier.

## falsifier

Show that for all optimal adversary strategies on all n there is an equivalent polynomial-size uniform description checkable in polynomial time relative to N, or construct a universal compressor for optimal adversaries.

## implication

If optimal adversary strategies are incompressible for some all-n family, this would constrain the size of any "adversary certificate" below PSPACE without ruling out Turing reductions and while distinguishing soundness from completeness of succinct certificates.

## finding_unverified

vial encoding of n), which is < Omega(n log n). No infinite all-n family of n-antichains has optimal adversarial strategies that are incompressible; they are all compressible to the universal minimax description. Moreover, framed DAGs are a representation for sorter strategies (soundness checker exists), not for adversary strategies - conflating the two categories is mistaken; even if rephrased, the uniform minimax description is polynomial-size and PSPACE-checkable. The winning frontier count barrier is distinct (state count) and does not imply strategy incompressibility.

I should report this clearly, distinguishing soundness/completeness and categories, and say no repository changes needed.**Finding (obstruction / failed disproof):**

The claim is false in the relevant sense. Optimal adversarial strategies in the comparison-sorting (poset/minimax) game are **uniformly compressible** by definition.

- **Uniform description exists.** The adversary move is given by the minimax recurrence: at state $S$ (consistent permutations/partial order), an optimal adversary picks a comparison pair achieving $\max_{p\in\mathrm{splitPairs}(S)} \max(\mathrm{adv}(S|p<q), \mathrm{adv}(S|p>q))$ (cf. `SoringP1/Minimax.lean`, `bestPair`/`adv`). This is a fixed, constant-size recursive program; Kolmogorov/description complexity is $O(1)$ plus $O(\log n)$ to encode $n$ (and state representation), not $\Omega(n\log n)$.
- **Falsifier is trivially satisfied.** For all $n$ and all optimal adversary strategies induced by a minimax-optimal choice rule, there is an equivalent polynomial-size (constant-size program) uniform description checkable in polynomial time relative to $N$ by a PSPACE (in fact PTIME, with memoization or just the recurrence) verifier. A universal compressor is the recurrence itself.
- **Category error vs framed DAGs.** The “framed DAG” grammar in `scripts/check_framed_strategy.py` and `docs/research-framed-certificate-frontier.md` is a representation for **sorter strategies** (certificates of a sorting algorithm), with a polynomial-time soundness checker. The adversary is the dual minimax opponent. Conflating adversary strategies with sorter framed DAGs is mistaken; even if rephrased, the uniform minimax rule is far smaller than any explicit DAG and is the natural description. Certificate **soundness vs completeness** remains separate.
- **Distinct from winning frontier.** The large winning frontier (exponentially many reachable winning posets/states) is an **enumeration/search barrier** (can’t list all states), not evidence that the *strategy* (the move rule) is incompressible. A simple strategy can navigate an exponentially large state space. This matches the frontier doc’s explicit caveat: it excludes “algorithms whose method necessarily outputs all reachable winning partial orders…” but does not imply strategy incompressibility or NP/PSPACE hardness.

**Concrete obstruction:** There is no infinite all-$n$ family of $n$-antichains where every optimal adversarial strategy is incompressible $\Omega(n\log n)$; optimal adversarial strategies are compressible to the fixed minimax description. Any attempt to force incompressibility confuses state-space size with description complexity and confuses sorter certificates with adversary strategies.

**No repository changes warranted.** This is a category/complexity-theoretic obstruction, not a new theorem to formalize or a counterexample instance to add. The question’s falsifier is demonstrably true.

## Other metadata

```json
{
  "finished_at": 1793802767.9860327,
  "started_at": 1793801913.924538
}
```
