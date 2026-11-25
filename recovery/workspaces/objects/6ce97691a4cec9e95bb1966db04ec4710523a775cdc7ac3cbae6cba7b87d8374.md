# Board-trail index robustness, scheduling, and Act 18 §8 reconciliation

*Executive liaison c1a00002, 2026-10-21. Implements the remedy assigned by the
Clerk's sitting (`records/summons/c1a00002.md`) for
`records/BOARD-TRAIL-INDEX-2026-10-21-staleness-and-flakiness.md`. Act 18
§5/§7/§8 maintenance; ordinary law (Acts 2/6/18), not a constitutional change.*

## 1. Transient board error no longer fabricates a gap

**Defect.** `board-trail-index.py:board_terminal_state()` returned `None` both
when an issue genuinely lacked a terminal update **and** when the `antonina board
show` call failed (every exception swallowed). A transient board error therefore
made a compliant issue (e.g. #308) come out `git_only_gap: True`. The §5 lens
(`board-trail-check.sh`) was worse: it `exit 1`-ed the whole lens on the first
board failure.

**Fix.**
- `government/board-trail-index.py`: `board_invoke` retries a failed board call
  up to `VICHE_BOARD_TRAIL_RETRIES` (default 3) with `VICHE_BOARD_TRAIL_BACKOFF`
  (default 1 s); only a persistent failure propagates. The issue is fetched
  **once** and reused for title and terminal classification. Each index entry now
  carries `board_readable`; `git_only_gap` is `enacted AND board_readable AND
  not has_terminal`, so a failed board call can never fabricate a gap.
- `government/board-trail-check.sh` (§5 lens): a `board_show` helper retries with
  the same bounds. A persistent failure emits one JSONL row for that issue with
  `board_readable: false`, `terminal: null`, `post_completion: null` instead of
  aborting the lens.
- `government/judiciary-measurements.py`: unreadable issues are **excluded** from
  the gap/fraction computation and reported separately as `board_unreadable`, so
  a transient board error cannot depress the measured terminal fraction.

## 2. Test evidence (hermetic)

`tests/board-trail-board-error-smoke.sh` (new): a fixture with (400) a genuine
gap, (401) a persistently unreadable board, and (402) a board that fails once
then returns a terminal update.

- #400 → `board_readable:true`, `git_only_gap:true` (genuine gap preserved).
- #401 → `board_readable:false`, `git_only_gap:false`, `terminal_status:null`
  (**not** a fabricated gap); the §5 lens reports `board_readable:false`,
  `terminal:null` and does **not** abort.
- #402 → retried (`c402 == 2`), `board_readable:true`,
  `terminal_status:"verification:confirmed"`, `git_only_gap:false`.
- `judiciary-measurements.py` → `completed_total 3`, `readable_total 2`,
  `fraction_terminal 0.5`, `git_only_gaps == [#400]`, `board_unreadable == [#401]`.

Existing `tests/board-trail-index-smoke.sh`, `tests/board-trail-smoke.sh`,
`tests/board-trail-terminal-agreement-smoke.sh` still pass, so §5/§7 continue to
agree. Full suite `sh tests/run-all.sh` → **All Viche tests passed** (exit 0).

## 3. Scheduled §7 regeneration

**Defect.** Nothing invoked the generator, so `records/board-trail/index.json`
silently went ~2 days stale and missed #313/#314.

**Fix.** New `government/board-trail-refresh.sh` (POSIX `/bin/sh`) regenerates the
index, throttled to `VICHE_BOARD_TRAIL_REFRESH_SECONDS` (default 3600 s = one
measurement window), writing a durable stamp `$VICHE_STATE_ROOT/board-trail/last-refresh`.
It is **non-fatal** (a board outage cannot block boot) and honours
`VICHE_BOARD_TRAIL_REFRESH=0` for hermetic callers. `government/boot.sh` invokes it
each cycle, immediately before the §5 lens that consumes the index.

`tests/board-trail-refresh-smoke.sh` (new) proves: first run invokes the generator
and writes the stamp; a second run inside the window is throttled; a zero interval
forces regeneration; a generator failure is non-fatal and does not advance the
stamp; the explicit disable suppresses the scan. `tests/boot-smoke.sh` sets
`VICHE_BOARD_TRAIL_REFRESH=0` so the boot smoke stays hermetic.

## 4. Act 18 §8 reconciliation — #310 and #313

Terminal board updates posted on the originating issues (exactly one stage marker
+ one declared terminal state each):

- **#313 (Act 19, Office Continuity and Handoff Integrity Act)** →
  `verification:confirmed`. Deployed (`5490dbf`) and independently verified
  effective by the Judiciary (`records/AUDIT-2026-10-20.md` §1.4/§3: "Act 19
  deployed and effective"; `tests/act19-office-continuity-smoke.sh` passes).
- **#310 (Act 20, Detector Calibration Act)** → `deferred`, with reason and review
  date. Enactment is complete and verified, but the Act's implementation
  (`records/calibration/`, `government/calibration-replay.sh`, the report and its
  tests) is not delivered; review at the next measurement window.

#314's terminal update (`deferred`) was posted by the Clerk. After regeneration
the §7 index therefore reports no `git_only_gap` for #313/#314 and a truthful
`deferred` state for #310.

## Honest limits

- Retrying a board call reduces, but cannot eliminate, the chance of an
  unreadable reading under a prolonged outage; the index is then explicitly
  `board_readable:false`, not a silent gap.
- The 3600 s refresh interval is a policy choice, not measured: a board update
  may be up to one window old before the index reflects it. The index remains
  derived; Git is the authoritative record (Act 18 §1).
- Act 20 implementation remains outstanding Executive work; `deferred` is the
  truthful terminal state, not a completion claim.
