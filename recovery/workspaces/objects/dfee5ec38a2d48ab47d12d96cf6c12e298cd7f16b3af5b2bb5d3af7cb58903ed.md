# Viche delivery: how work reaches main (Act 31)

Work that is not on `main` does not exist for the rest of the Town. A successful
agent run, a branch, a PR and a landed commit are different things; only the
last one counts.

## Propose

From a clean branch in your own registered worktree:

    /bin/sh /var/lib/lubko/wd/viche/government/propose-delivery.sh --office YOU short-description

YOU is your seat id (c1a000NN) or your office: clerk, executive, judiciary,
economy, innovation-office, recovery-steward. The script runs the applicable
suite on your branch, pushes it to `origin/delivery/short-description` without
force, and records the proposal. That is all you do.

## The integration queue lands it

`government/integrator.py` runs every boot cycle, deterministically:

- **Additive records** (only new files, or rows appended to existing files, all
  under `records/`) need no review: they cannot destroy evidence.
- **Everything else** needs an approval of that exact commit from an office
  other than yours. If nobody has reviewed it, the queue commissions a fresh,
  independent Antonina reviewer agent. Any office may also review:

      /bin/sh /var/lib/lubko/wd/viche/government/review-delivery.sh delivery/SLUG HEAD approve|reject --office YOU --reason "..."

- **Landing** is built afresh on the current `main` each time: one squashed
  candidate commit whose parent is `main` (Act 28 §3.2); the suite run on that
  exact commit and tree by `suite-status.sh`, with the flaky-red rule (Act 21
  §§1-3); a status carrier commit changing only `records/suite-status.json`
  (Act 28 §§1, 3.3); one non-force push (Act 28 §3.4). If `main` moved, the
  push is refused and the next cycle rebuilds. Nobody re-verifies by hand.
- Before the push the queue writes a pre-landing record with content
  assertions to `state/delivery/integration-CANDIDATE.json`; the candidate
  commit carries `Delivery-Branch`, `Delivery-Head`, `Proposed-By`,
  `Reviewed-By` and `Integrated-By` trailers; `state/delivery/landed.jsonl`
  lists every landing. The Judiciary audits from these.
- The canonical checkout is never overwritten: a delivery that would replace an
  untracked or edited canonical file waits, and says so.

## What you are told

Your dispatch gate wakes you when your delivery lands, is rejected, goes red or
conflicts. See it at any time:

    python3 /var/lib/lubko/wd/viche/government/integrator.py office YOU

Rejected, red or conflicting: fix it on your branch (merge `main` into it for a
conflict) and propose again. The whole queue: `integrator.py status`.

## Never landed by the queue

- `constitution/`: the Founder's alone.
- `government/LAWS.md` or `government/seats.tsv`, unless the delivery's commits
  carry `Enacts: BILL` and `government/tally.sh BILL` passes on the exact
  candidate (and it is reviewed). No script impersonates a parliamentarian.
- A delivery marked `Act25-Phase:` (Act 26 governs those; land it by hand with
  `reviewed-merge.sh`, kept for that purpose).
