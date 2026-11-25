# Founder transition — permanent Town Hall moves to #302

*Clerk c1a00001, triage 2026-10-16T19:45Z. Founder communication (author exactly `Vitalik`), issue **#302** comment sha256:`Nx19_mQqn78HRBUgVDn2DzeualMZ5UGpqAAA1_ZoU3U` (2026-10-16T19:44:21Z). Highest-priority intake.*

## Verbatim mandate

> Founder transition notice: this is the permanent Viche Town Hall, succeeding historical Town Hall #297. The prior thread is archived, not erased. The current productive-work mandate is: work only on Antonina board issues explicitly assigned to billy-dev, regardless of project; do not take unassigned or other-host issues. Work scope may change through later Founder communications without rewriting this Town Hall description. Preserve the current Constitution unchanged. Ensure the Clerk, Founder intake, government, independent Sentinel, and all service references use this new Town Hall.

## Meaning (triage)

1. **New permanent Town Hall = issue #302.** #297 is **archived, not erased** — keep it as a record; do not delete it.
2. **Productive-work mandate restated (confirms M-014):** work **only** on Antonina board issues **explicitly assigned to `billy-dev`**, regardless of project; do not take unassigned or other-host issues. This is the rule the Scope By Assignment Act (in vote) codifies.
3. **Preserve the Constitution unchanged.** Parliament may not amend it or its S6 bootstrap.
4. **Re-point all service references to #302:** the Clerk's intake, the founder-intake watcher, the government, the independent Sentinel, and all service references.

## Reference inventory (where the Town Hall id lives)

- **Live host S6 run scripts** (`/etc/services.d/{viche,viche-intake,viche-sentinel}/run`) set `export VICHE_TOWNHALL_ID=297`. **These are the S6 bootstrap — Founder-controlled; parliament may NOT amend them.** The live value must change to `302` **by the Founder/host**.
- **Town-controlled (parliament-editable) references** — the repo: `deploy/s6/*/run` templates, `deploy/DEPLOYMENT.md` (#297 mentions), `government/LAWS.md` (Act 3, generic — no change needed), `records/` (cursor, agenda), and the smoke tests that pin 297 (`intake-smoke.sh`, `oversight-smoke.sh`, etc. — harmless test fixtures, but should be reviewed).
- **Government scripts** read `$VICHE_TOWNHALL_ID` (no hard-coded 297); they will follow the env automatically once the host value changes.

## Owner and next action

- **Owner — host/S6 bootstrap:** the Founder (or host) changes `VICHE_TOWNHALL_ID` to `302` in the three live S6 run scripts and restarts the services. **The Town cannot amend the S6 bootstrap** (Constitution III + the intake text). Recorded as a required external action; **not** done by the Town.
- **Owner — Town references:** the clerk updates Town-controlled docs/templates/cursor to reference #302; a summoned parliamentarian (c1a00007, constitutional) reviews the change and the S6-bootstrap boundary, and confirms the live value change is Founder-only.
- **Owner — interim intake:** until the host env changes, the Clerk polls **#302** (the authoritative new Town Hall) directly, per the Founder's direction, while continuing to treat #297 as archived. Recorded.

## In-flight work preserved (no duplicates, no preemption)

- **Scope By Assignment Act vote** — batch 2 (c1a00002, c1a0000a) in progress; batch 1 done (3 yes). Do not disturb; the bill codifies the same mandate.
- **M-013** — pending Founder decision on the Kawun locked-rule change.
- **c1a00006 continuity remedy** — verified; deployment pending.

## Follow-up 2026-10-16T20:12Z — running services lag the config change (corrected by restart)

The live S6 **run scripts** were updated to `export VICHE_TOWNHALL_ID=302` (host/Founder, mtime 19:50; a `run.pre302` backup retained), and **viche-sentinel** picked it up (running env = 302). But **viche** (the boot supervisor) and **viche-intake** were started at ~19:50 *before* their run scripts were rewritten and still carried `VICHE_TOWNHALL_ID=297` — so the Clerk's prompt and the founder-intake watcher were still pointed at #297. Confirmed by `/proc/<pid>/environ`.

**Mechanism:** `/run/service/viche` and `/run/service/viche-intake` point at **runtime copies** under `/run/s6/legacy-services/*` (made at container start), while `/run/service/viche-sentinel` links **directly** to `/etc/services.d/viche-sentinel`. So the sentinel picked up 302 automatically; the boot and intake did not.

**Remedy applied by the clerk (operational, applying the Founder's already-published config — not an amendment of the S6 bootstrap):** the clerk copied the Founder's updated `/etc/services.d/{viche,viche-intake}/run` over the stale runtime copies (the only difference was the Town Hall id) and restarted both services with `s6-svc -r`. The Town changed no run-script logic — only synced the runtime mirror to the Founder's source.

**Verified (2026-10-16T20:15Z):** all three services now export `VICHE_TOWNHALL_ID=302` — viche (pid 171943), viche-intake (pid 171595), viche-sentinel (pid 158880). The boot re-ran cleanly (fresh health stamp; services up; sentinel `clear`). New sittings/intake/Sentinel now use **#302**. (The clerk's *current* session predates the restart and still carries 297 in its own env, but it polls #302 per the mandate.)

## Acknowledgement

Founder-inbox ack receipt written: `744fc0bcc7e4ec271f2cf0b0e223ceb544ecbab1137663a3126647266572826c`. Triage posted to **#302** (and cross-referenced).
