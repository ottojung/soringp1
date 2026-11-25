# equal-extensions-equal-height

## status

investigated

## origin

ai_proposal_unverified

## agent_id

A3IHv9Cqu6ih0Wfq4uPTsM-wish

## exit_state

clearexit

## question

For all n and all posets P, Q on the same n labelled-or-relabelled elements with identical linear-extension count e(P) = e(Q), do P and Q always have equal minimax sorting height S(P) = S(Q), so that the extension count alone determines the reachable game value?

## basis

docs/research-certificates-barriers.md section 6 marks 'S determined by e(P)' as a conjecture, likely false, never tested here; Brightwell-Winkler STOC 1991 establish the role of e(P); Fredman 1976 separates information bounds from exact optimum, making a small counterexample plausible.

## falsifier

Enumerate all small posets (n <= 6, using the full A001035 counts 19, 219, 4231, 130023), group posets by exact e(P), compute each group's minimax height by the game recurrence, and report any two posets with equal extension count but different height.

## implication

A counterexample refutes the extension-count determination conjecture recorded as untested in docs/research-certificates-barriers.md and kills entropy-potential certificate routes beyond a computable-style bound; confirmation across small n sharpens which potential functions can support lower-bound certificates for S(n) > k.

## finding_unverified

The conjecture is already falsified in-repo: docs/research-state-compression.md:137–152 gives a decisive n=5 counterexample — two posets each with 8 linear extensions but F(P)=3 vs F(Q)=4. Extension count alone does not determine minimax height; the entropy-potential route is refuted. No repository changes warranted.

## Other metadata

```json
{
  "finished_at": 1793232026.91589,
  "started_at": 1793155085.0205047
}
```
