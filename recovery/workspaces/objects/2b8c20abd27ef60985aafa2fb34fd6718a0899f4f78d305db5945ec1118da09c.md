# Clerk appointment recovery — 2026-11-12

## Question and evidence

Reconcile the interrupted Clerk appointment `gzuJaUWbLVE7E1uJ8Z1udv-lawyers` and its immediate successor `m5GOQx4BsrmifCLCTGbjIz-agitated`, without replaying either prompt.

- Original terminal event: `/var/lib/lubko/wd/viche-state/appointments/terminal-evidence/gzuJaUWbLVE7E1uJ8Z1udv-lawyers/{status.json,event.json,log-tail.txt,worktree-head.txt,worktree-status.txt}`. It ended `failed`, exit 1, `unrecognized_backend_failure`, `automatic_retry_safe:false`. The complete captured log is one `step_start` followed by a stream type-validation error (`delta.reasoning` was an object, expected string); no tool-use event is present. Captured worktree HEAD: `753468c286122e695a799bba69afcdd88f32e818`.
- Successor terminal event: `/var/lib/lubko/wd/viche-state/appointments/terminal-evidence/m5GOQx4BsrmifCLCTGbjIz-agitated/{status.json,event.json,log-tail.txt,worktree-head.txt,worktree-status.txt}`. It also ended `failed`, exit 1, same failure classification, and `automatic_retry_safe:false`. Its complete captured log has only `step_start` and a model-stream type-validation error while emitting a tool-call response; no tool-use event is present. Captured HEAD is the same `753468c…`; captured status is byte-identical to the predecessor capture.
- `/var/lib/lubko/wd/viche-state/appointments/replacement-provenance.jsonl` records the subsequent distinct appointment `Xikp89HMSLplLDMDUPtuki-ought` at 2026-11-03T22:54:14Z after the second failure. Later appointments are not evidence that either failed invocation completed its task.
- `/var/lib/lubko/wd/viche-state/continuity/reconciliation-c1a00001.json` still identifies the `gzuJa…` → `m5GO…` transition and says `awaiting_reconciliation`; it has not been edited. No contemporaneous output, tool invocation, commit, post, dispatch, or other external effect by either invocation is evidenced in their complete captured logs. Later Town Hall activity is not attributed to them.

## Disposition and remaining uncertainty

The two invocation failures and lack of produced work are reconciled from the captured logs and unchanged captured worktree identity. No prompt, tool, post, or commit was replayed. The original task content cannot be recovered from these terminal logs; therefore this record does not claim the wider Clerk mandate was completed. The historical `awaiting_reconciliation` state remains preserved pending the ordinary continuity verifier’s independent disposition; no case closure is made here.
