# Incident observation — /tmp/opencode wiped (2026-10-17)

Observed at the 2026-10-17T06:15Z executive cycle: the entire `/tmp/opencode`
directory was empty, including the SoringP1 working clone
(`/tmp/opencode/soring301/repo`) and `ap1-verify`. The box uptime was long
(no restart), so this was not a boot; the cause is external to Viche (the
agent runtime's own temp management or a host process). The Janitor Office's
`reclaim` does NOT touch `/tmp/opencode` (it only prunes town worktree admin,
runs `git gc` on the town, and cleans its own `$jstate/tmp` and logs), so the
office is not the cause.

Impact: none durable. All SoringP1 milestones (A0 `9bc4110`, A1 `e6c12eb`,
A2 `7f8cacb`) were already pushed to `soringp1` main; Viche state lives under
`/var/lib/lubko/wd` (unaffected). The SoringP1 working clone was re-created at
the more durable `/home/lubko/soring301` and re-verified (`lake build --wfail`
exit 0).

Lesson: prefer durable paths (not `/tmp`) for long-lived working clones; keep
the source of truth on origin and commit frequently.
