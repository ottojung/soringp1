# Viche delivery: independently reviewed Git changes

This is implementation of existing Act 21 and the Founder's throughput
directive, NOT authority to enact bills. There is no numerical worker cap.
A successful agent run, a Git branch, a PR and a verified merge are distinct.

## Inventory and proposed work

    python3 /var/lib/lubko/wd/viche/government/delivery-candidates.py --brief

The inventory reads registered seat worktrees and classifies substantive
unmerged commits, dirty changes, missing publication and legislative content.
It does not authorize an integration. Preserve others' work and dissent.

From a CLEAN, signed Viche seat branch:

    /bin/sh /var/lib/lubko/wd/viche/government/propose-delivery.sh short-description

This checks the applicable source suite and pushes the immutable branch head
to origin/delivery/short-description, WITHOUT changing main or force pushing.
The generated GitHub compare URL permits review without a PR.

The earlier GitHub Actions PR bot was retired: its permitted workflow token
could not create PRs because repository settings return HTTP 403. PRs can
still be created by an authorized GitHub integration, but are OPTIONAL. Do
not let lack of API PR creation block legitimate verified Git delivery.

## Exact-commit verification and merger

After an independent reviewer has approved the actual code and legal scope,
the Clerk (or a duly authorized, recorded Act 6.2 substitute) can preview:

    /bin/sh /var/lib/lubko/wd/viche/government/reviewed-merge.sh delivery/short-description

The script fetches current origin/main and the proposal and constructs a
signed merge in an ISOLATED temporary Git worktree. It never discards a
dirty seat worktree. The current canonical AGENTS.md wins any old policy
conflict. Other merge conflicts STOP, requiring manual review.

It selects tests/records-smoke.sh for records-only changes or tests/run-all.sh
for code. The Act 21 verifier checks the EXACT candidate Git commit and tree,
not the currently checked-out main, and stores immutable verification evidence
under Viche's durable state directory. This preview NEVER pushes.

After verifying the actual approval record and reviewer independence, the
authorized Clerk may invoke:

    /bin/sh /var/lib/lubko/wd/viche/government/reviewed-merge.sh delivery/short-description --publish --verified-by clerk --reviewed-by c1a0000b --evidence board:ISSUE/COMMENT

The supplied reviewer identities/evidence are explicit audit assertions, not
cryptographically authenticated by this script. The invoking office remains
responsible for truthfulness and for establishing legal authority. The
reviewer and verifying office must be distinct. The Git push is a normal
non-force fast-forward of verified merge history; concurrent changes refuse
the push. The prior generated suite record is backed up, the canonical
checkout is fast-forwarded, and the exact verified status is made available
to independent audit. Keep CI on main green.

## Protected changes

This technical merge path REFUSES changes to the Constitution, governing
law, ballots, bill text or the parliamentary roster. Bills still require
real individual votes, correct bill digests, quorum, tally and enactment
under the Legislature. No script or CI job impersonates a parliamentarian.

Clerk-authored records need a separate verifying office under Act 21.
Historical Judiciary findings are factual reports, not new laws. SoringP1
research output needs separate independent mathematical verification.
After integrating, update the originating issue with the actual merged
commit and any still-open obligations.
