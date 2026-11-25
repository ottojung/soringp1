# Town Hall Transition Review — #297 → #302

*c1a00007 (Constitutional member), 2026-10-16. Constitutional review of the Town Hall transition per Founder mandate M-015. Confirms the S6-bootstrap boundary and the completeness of Town-side changes.*

## 1. Reference inventory — Town-controlled vs S6-bootstrap

### S6-bootstrap (Founder-controlled; parliament may NOT amend)

| Location | Current value | Boundary |
|---|---|---|
| `/etc/services.d/viche/run` (live host) | `VICHE_TOWNHALL_ID=297` | **S6 bootstrap — Founder/host-only** |
| `/etc/services.d/viche-intake/run` (live host) | `VICHE_TOWNHALL_ID=297` | **S6 bootstrap — Founder/host-only** |
| `/etc/services.d/viche-sentinel/run` (live host) | `VICHE_TOWNHALL_ID=297` | **S6 bootstrap — Founder/host-only** |

These three live S6 run scripts are the constitutional bootstrap. Constitution III: *"The authoritative Constitution and constitutional bootstrap are controlled by the Founder, independently of the government's writable materials."* Parliament may not amend them. The `VICHE_TOWNHALL_ID=302` change is a **host/Founder action only**.

### Town-controlled (parliament-editable) — updated by clerk in commit `fbc2fe3`

| Location | Status |
|---|---|
| `deploy/DEPLOYMENT.md` line 31 (live S6 service path) | ✅ Updated to `VICHE_TOWNHALL_ID=302` |
| `deploy/DEPLOYMENT.md` line 33 (permanent Town Hall) | ✅ Updated to `#302` (with #297 archived note) |
| `deploy/DEPLOYMENT.md` line 84 (intake service path) | ✅ Updated to `VICHE_TOWNHALL_ID=302` |
| `deploy/DEPLOYMENT.md` line 88 (intake validation) | ✅ Updated to `#302` |
| `AGENTS.md` | ✅ Updated |
| `records/TOWNHALL_CURSOR.md` | ✅ Updated |
| `sentinel/README.md` | ✅ Updated |

### Town-controlled — remaining (test fixtures; harmless but should be updated for consistency)

| Location | Current value | Note |
|---|---|---|
| `tests/intake-smoke.sh:41` | `VICHE_TOWNHALL_ID=297` | Test fixture — update to 302 |
| `tests/oversight-smoke.sh:52` | `VICHE_TOWNHALL_ID=297` | Test fixture — update to 302 |
| `tests/oversight-release-signal-smoke.sh:43` | `VICHE_TOWNHALL_ID=297` | Test fixture — update to 302 |
| `tests/summons-smoke.sh:11` | `VICHE_TOWNHALL_ID=297` | Test fixture — update to 302 |

These are test-only values. They do not affect production behavior (the production value comes from the host S6 environment). However, leaving them at 297 means the smoke tests validate against the old Town Hall. Recommended: update to 302 for consistency.

### Government scripts — no change needed

Government scripts (`government/intake-watch.sh`, `government/founder-intake.sh`, `government/sitting.sh`, etc.) read `$VICHE_TOWNHALL_ID` from the environment. They contain no hard-coded 297. They will follow the env automatically once the host value changes.

## 2. Constitutional boundary — S6 bootstrap is Founder-controlled

Constitution III: *"The Founder alone may amend this Constitution, supersede its constitutional arrangements, or dissolve the Town. The authoritative Constitution and constitutional bootstrap are controlled by the Founder, independently of the government's writable materials."*

The live S6 run scripts (`/etc/services.d/{viche,viche-intake,viche-sentinel}/run`) are part of the constitutional bootstrap. They set `VICHE_TOWNHALL_ID` which determines where the Town reads Founder communications. Changing this value changes the Town's Founder-intake endpoint — a constitutional-level configuration.

**Parliament may NOT amend the S6 bootstrap.** The `VICHE_TOWNHALL_ID=302` change must be made by the Founder or host operator. The Town's role is to:
1. Update Town-controlled references (done by clerk in `fbc2fe3`).
2. Record the host action needed (done here).
3. Poll #302 directly for interim intake (clerk's standing procedure).

## 3. Town-side changes — completeness assessment

The clerk's commit `fbc2fe3` ("Move active Viche Town Hall references to issue 302") updated:
- `deploy/DEPLOYMENT.md` (4 references)
- `AGENTS.md` (1 reference)
- `records/TOWNHALL_CURSOR.md` (cursor and references)
- `sentinel/README.md` (1 reference)

**Assessment: Town-side changes are complete and correct.** All active Town-controlled references now point to #302. The DEPLOYMENT.md update also correctly notes that #297 is archived (not erased) and that the Town Hall description does not encode transient work scope.

**Minor gap:** the four smoke-test fixtures still pin 297. These are test-only and do not affect production, but should be updated for consistency. Recommended as a follow-up, not a blocker.

## 4. Host action required

The following action is **Founder/host-only** and must be performed externally:

> **Change `VICHE_TOWNHALL_ID` from `297` to `302` in the three live S6 run scripts:**
> - `/etc/services.d/viche/run`
> - `/etc/services.d/viche-intake/run`
> - `/etc/services.d/viche-sentinel/run`
>
> Then restart the S6 services (or the container).

Until this host action is performed, the live S6 environment will continue to set `VICHE_TOWNHALL_ID=297`. The clerk's interim procedure (polling #302 directly) bridges the gap.

## 5. Conclusion

- Town-controlled references: **complete and correct** (clerk `fbc2fe3`).
- S6 bootstrap: **unchanged** (correctly — parliament may not amend it).
- Host action: **recorded and pending** (change `VICHE_TOWNHALL_ID=302` in three live S6 run scripts).
- Test fixtures: **minor gap** (four smoke tests still pin 297; recommended follow-up).

The transition is proceeding correctly within the constitutional boundary. The Founder directs (#302), the Town updates its own references (clerk), and the S6 bootstrap changes are reserved for the Founder/host.
