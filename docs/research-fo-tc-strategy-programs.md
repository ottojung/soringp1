# FO(TC) strategy programs for exact optimal sorting (research note)

## Model

A strategy program p is a sequence of labeled blocks:
  state variables: a finite record of known order relations among n keys
  (partial order P over [n]); comparison queries are oracle calls cmp(i,j)
  returning i<j or j<i; branching on outcome; output permutation.

Semantics: interpreter IP(p, X) executes p, querying X only via cmp, maintains P,
terminates with a sorted permutation. Cost = number of cmp queries (worst case).

## Complexity (combined)

For fixed p, data complexity is in NL (FO(TC)) for each fixed formula, but
combined-time evaluation of growing p requires a uniform polynomial interpreter.
We use a bounded-variable fragment: each state update is expressible as an
FO(TC) formula with O(log n) variables; combined evaluation O(poly(|p|,n)).

## Soundness

If IP(p,X) sorts and uses <= k comparisons for all total orders X, then
S(n) <= k (sound). Completeness (all-n): whenever S(n)<=k, a program of size
poly(n+k) with poly(n) runtime exists. CONJECTURAL; not yet proved.

## Status

PROVED: soundness given uniform polynomial interpreter; Sigma_2^P upper bound
for subclass representable.
CONDITIONAL: completeness theorem (all-n).
NOT REFUTED: no counterexample family found.

## Next experiment

Construct explicit programs for n<=6 optimal sorters and measure size/runtime;
test whether forgetful framed-DAG families (issue #47) are simulable with
poly overhead.
