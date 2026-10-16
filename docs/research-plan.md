# Research roadmap

The long-term goal is deliberately ambitious. These are independent research
fronts, not assertions that a separation can be obtained by brute force.

## A. Definition and exact upper bound

Produce a Lean theorem identifying S with optimal sorting decision-tree
height, prove feasibility for every n, and kernel-check a compact
partial-order minimax evaluator. Separate correctness from a machine-level
2^{O(n²)} running-time proof; establish the unary EXPTIME consequence.

## B. Faster characterization

Seek transformations of arbitrary optimal decision trees into canonical forms
that sharply reduce the state space. Explore partial-order symmetries,
orbit representatives, entropy/linear-extension relaxations, and structural
decompositions. Any proposed exact recurrence must be adversarially checked
against established small-n sorting numbers.

## C. P/NP framing and certificates

Analyze the unary threshold language. A sorting tree has many leaves, so it
is *not* an obvious polynomial-size NP witness. Study whether succinct
certificates exist, whether they can be verified efficiently, and whether
one can compute S from an NP predicate or vice versa. Never conflate an
NP-hard general optimal-decision-tree problem with this one-parameter family.

## D. Lower bounds / reductions

Explore reductions from established problems, diagonalization barriers,
and the limits of finite-instance enumeration. A reduction must preserve
the uniform family, fixed query type, worst-case minimax objective,
parameter encoding, and answer threshold. Seek unconditional reductions
only; avoid circular consequences of assumed P≠NP.

## E. Independent literature and computational audits

Review exact-comparison sorting, decision-tree complexity, comparison sorting
with partial information, the difference from sorting networks, and known
finite-n certificates. Use small cases to test *definitions and conjectures*,
not as evidence for a superpolynomial complexity separation.

## Deliverable standards

Record source, statement, encoding, proof status, and falsification attempt.
Promote a result through: conjecture → convincing notes proof → Lean formal
statement → kernel-checked proof → external-to-Lean correspondence audit.
If a proof direction stalls, document the exact barrier.
