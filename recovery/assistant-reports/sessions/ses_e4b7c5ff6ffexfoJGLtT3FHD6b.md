# antonina-4EN8AdYF7E2al1AO6Uiea1-daylight

Session: ses_e4b7c5ff6ffexfoJGLtT3FHD6b
Workspace: /home/lubko/soring-fronts/exec-act19-prepared-provenance-20261107
Created: 1794029887567; updated: 1794029957688

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b483a211001JNof7tSFQ9NbUv)

I’ll verify the current policy and Act 19 requirements first, then inspect the copied candidate and its exact initial diff hash before making any changes. I’ll keep all edits inside this worktree and won’t commit or publish anything.

## Output 78 (msg_1b484032b001hhkztr602Z1sgm)

The crash semantics are clear: `appointments.sh` atomically replaces `appointments.tsv` with `mv` at the commit point, then publishes committed provenance separately. So requiring `state=="committed"` would strand a genuine post-swap crash. I’m checking whether a prepared intent can be correlated more strongly than merely matching the current successor before tightening this recovery predicate and its regression.

## Output 123 (msg_1b4849623001HsS7pCoVjH0gqS)

**Blocker: there is no safe discriminator in the current format for the ambiguous state.** I made no net changes. The copied candidate’s diff hash is unchanged: `1b5930a340ec65fc1b5f4921188fd322e774a66dab96a800b383a484dfa2789f` (initial hash: `5d1de3bedcdc6bf495a88a3689a6eaf744616d536ccf5d527a28e8afb8dd9faa`).

In `appointments.sh`, the registry’s atomic `mv` is the replacement commit point; committed provenance is published afterward and can be absent if the process crashes. Thus a matching prepared intent plus the current successor handles that crash window, but does not prove the swap occurred: a pre-existing registry containing that same successor is observationally identical if no committed provenance exists. Requiring committed state would reject a real committed replacement after that crash; accepting prepared state based on the matching row could authorize cleanup without proof. The current integration test covers an unrelated successor and the post-swap/pre-provenance case, but not the indistinguishable pre-existing-same-successor case.

I did not guess or alter the candidate. A safe fix needs a discriminator persisted atomically with the registry swap, or a policy/operational decision that explicitly accepts the residual ambiguity. No tests were run. `git diff --check` passed. **Focused `/bin/sh` and `dash` tests and the Act 21 full-suite gate remain outstanding.**
