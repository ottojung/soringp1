# Founder clarification: GitHub Actions CI does not violate agent-host assignment

**Authority:** Founder-authored clarification, permanent Viche Town Hall #302 and
SoringP1 Antonina board issue #301, 2026-10-16. This is a clarification of
work scope, not an amendment to the Founder-controlled Constitution.

A `billy-dev` assignment restricts where Viche/Antonina agents execute
their development tasks, operate their worktrees, and run work-specific
experiments. It does not restrict GitHub's repository hosting, checks or CI
workers. GitHub-hosted Actions may build, test, run Lean and verify proofs
for the corresponding project. Keep CI operational; checks and reviews remain
important evidence, but do not replace actual agent work on the assigned host.

**Failure that prompted this clarification:** commit
[785e31d3](https://github.com/ottojung/soringp1/commit/785e31d3f9a775a7a43603e5cff766763f9ae3e3)
deleted the SoringP1 GitHub Actions workflow due to an overbroad reading
of the host restriction. Reverted through [SoringP1 PR #3](https://github.com/ottojung/soringp1/pull/3).
The SoringP1 board issue #301 was corrected; #302 contains the enduring
Founder interpretation. Executive, parliamentary and audit instructions must
implement this distinction consistently.

**Regression test:** Viche guidance must never interpret agent-host assignment
as grounds for preventing or removing hosted GitHub Actions CI.
