# antonina-fGSrJaWmS4sS2IAHQ2f82l-limbs

Session: ses_e5288a7f8ffePCGMIVZ8HXX0Xm
Workspace: /home/lubko/soring-fronts/recovery-steward-sibling-budget-20261105
Created: 1793911642122; updated: 1793911680729

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 90 (msg_1ad77d435001FvWYqSDkCmDLbr)

I don’t have a defensible positive decomposition or a falsifying witness yet. In particular, I can’t identify the referenced verified `n=7` root-reachable collisions in the repository materials I checked, so I can’t use them as constraints without risking inventing their details.

A viable candidate summary would need to retain enough information about a prefix state to determine, for every next comparison, the pair of successor summaries up to relabelling. That is exactly the two-child congruence obligation; a summary that only predicts `F` is insufficient. The known `n=7` comparability-graph collision already rules out that coarse summary, while the existing exact quotient by poset isomorphism remains at `2^{Θ(n²)}` states. I found no proof that a first-`k`-comparison boundary summary improves this bound, nor a smallest-instance falsification of a precisely defined such summary.

For the asymptotic connection: an all-`n` state bound `2^{o(n²)}` with polynomial-per-state transitions would improve the current `2^{O(n²)}` numeric-`n` evaluator; a bound `2^{O(n log n)}` would yield `2^{O(n log n)}` time. No such bound is established here. No repo edits, posts, or commits were made.
