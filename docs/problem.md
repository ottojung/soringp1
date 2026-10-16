# Exact research problem

## Sorting numbers

For each n ≥ 0, let a *deterministic adaptive comparison sort* be a finite
binary decision tree whose internal vertices compare two of n distinct,
labelled input keys, and whose leaves return their increasing order.

Let

  S(n) = min { height(T) : T correctly sorts every permutation of n keys }.

Height is the maximum number of comparisons on any execution path. Comparison
selection may adapt to previous outcomes. Algorithms are uniform only when
we investigate a procedure that *computes* S(n); the individual sorting tree
being minimized over is not required to be described uniformly in n.

The Lean model in `SoringP1/Model.lean` encodes comparison trees and the
minimization specification. Its existence and correctness correspondence
obligations are *not yet proven*.

## Encodings and exact questions

### Function evaluation

- `S_unary(1^n)` returns the binary representation of S(n).
- `S_binary(bin(n))` returns the binary representation of S(n).

Ask independently whether either function is in FP (deterministic
polynomial-time computation, measured in its actual input length). The
parameters are mathematically the same but the complexity questions differ.

### Threshold decision problems

- `SORT-BOUND-U = { 1^n # 1^k : S(n) ≤ k }`.
- `SORT-BOUND-B = { bin(n) # bin(k) : S(n) ≤ k }`.

These are canonical *decision* questions for P, NP, EXPTIME. Both n and k
are encoded as indicated. Fixed delimiters, zero conventions, and standard
well-formedness checks are polynomial-time equivalent and do not matter for
the stated classes.

`SORT-BOUND-U ∈ P` is equivalent to `S_unary ∈ FP`: one direction is a
comparison after function evaluation; the other uses binary search on k over
a known O(n log n) comparison-sorting upper bound, calling the threshold
decider polynomially many times with polynomial-size unary k.

For binary encoding, the same equivalence applies because the merge-sort
bound and all binary-search probes have O(log n) bits.

NP membership of a threshold language is not established by exhibiting a
sorting decision tree: such a tree may require exponentially many nodes
relative to the input length.

## What is known initially

- Standard sorting algorithms and the decision-tree information bound give
  `ceil(log2(n!)) ≤ S(n) ≤ O(n log n)`.
- A partial-order minimax recurrence gives **time 2^{O(n²)} measured in numeric n**
  to compute S exactly, assuming ordinary polynomial-cost finite-state
  bookkeeping. See [the derivation](upper-bound.md).
- Thus `SORT-BOUND-U ∈ EXPTIME`. This does *not* imply
  `SORT-BOUND-B ∈ EXPTIME`: its proven bound from this algorithm is
  `2^{2^{O(m)}}` where m is the bit length of binary n, hence in 2-EXPTIME.
- Neither `SORT-BOUND-U ∈ NP` nor `SORT-BOUND-U ∉ NP` is being claimed.
  Similarly, no separation from P is established.

## What would count as success?

A kernel-checked theorem connecting an explicitly encoded machine/resource
model to the exact S or threshold language, with an ordinary mathematical
correspondence argument relating the formal object to adaptive comparison
sorting. Meaningful complete results include:

- a polynomial-time exact evaluator, with a checked correctness and time bound;
- a proved NP (or other complexity-class) upper bound under the fixed encoding;
- an unconditional lower bound excluding P, NP, or a precisely named class;
- a tighter deterministic upper bound, with a checked cost model.

A statement `SORT-BOUND-U ∈ NP\P` would in particular imply P ≠ NP, and
should not be presented as a routine route. Excluding NP is stronger still
than merely showing an individual algorithm takes exponential time.

Open questions are hypotheses to investigate, not planned deliverables that
can be guaranteed in advance.
