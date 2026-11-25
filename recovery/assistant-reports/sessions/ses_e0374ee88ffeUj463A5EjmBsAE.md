# antonina-dlUhW8jdevHE930bc9q8fT-unite

Session: ses_e0374ee88ffeUj463A5EjmBsAE
Workspace: /home/lubko/soring-fronts/exec-space-milestone-proof-20261121
Created: 1795238334914; updated: 1795238537132

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 197 (msg_1fc8e1db6001Tls5z3k1pmoV9R)

Posted the finding as a single comment to Antonina board issue #301 (comment id `sha256:c6uYurpn5hYzCqPYY7faDKx1mTZBPoBYLLgmVQiol0A`). No repository, Lean, test, CI, ledger, or workflow changes were made.

Result: precise obstruction. Step 2 of the milestone argument cannot be proved as stated because it assumes an arbitrary uniform machine's accepting computation must be semantically equivalent to a depth-`t` game state. Arbitrary machines may decide `SORT-BOUND-U` by global methods without constructing or storing `P_t`; the pigeonhole argument over possible game states does not apply to one machine on one input. The winning-frontier count is also not a direct lower bound because `SORT-BOUND-U` has one input per `n` and is not PSPACE-hard as a sparse tally set. Alternative routes proposed: restricted-model barriers, general poset-evaluation lower bounds, and continued upper-bound search. The `O(N log N)` space question remains open.
