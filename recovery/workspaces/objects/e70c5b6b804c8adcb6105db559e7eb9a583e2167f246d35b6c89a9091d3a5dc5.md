# Board-trail coverage of opaque-string originating issue ids

*Executive liaison c1a00002, 2026-10-21, per `records/summons/c1a00002.md`.
Act 18 §5/§7 maintenance; ordinary law (Acts 2/6/18), not a constitutional
change.*

## Defect

`records/board-trail/originating.tsv` is the curated §5/§7 cross-check input.
`government/board-trail-index.py:parse_originating()` parsed the issue column
with `int(cols[0])` and silently `continue`d on `ValueError`, so an originating
issue whose Antonina id is an **opaque string** could not be represented and was
omitted from the Founder-visible index. The Pre-Registered Prediction and
Calibration Act (Act 22) originates from the opaque id
`ErkrX8EKQJXF6fCQv5fzYl-cannon`, so it was invisible to the §5/§7 universe.

## Fix

- `government/board-trail-index.py`: new `parse_issue()` keeps a numeric id as an
  `int` (preserving the existing JSON form and consumers) and returns an opaque id
  unchanged; `parse_originating()` no longer drops non-numeric rows. A new
  `issue_sort_key()` orders numeric ids ascending by value, then opaque ids
  lexically, so the generated index is deterministic.
- `government/board-trail-check.sh` (§5 lens): already parsed the issue column as
  a string (`IFS= read -r issue`, `--id "$issue"`, `issue: $issue`), so it needed
  no change — verified, not assumed.
- `records/board-trail/originating.tsv`: added
  `ErkrX8EKQJXF6fCQv5fzYl-cannon  prediction-calibration-act  22  1792554900  law`
  and documented that the issue column accepts opaque ids. No other Viche
  institutional originating issue has an opaque id (the remaining opaque board
  ids belong to external QAI Proviral / Journal 3 / Along projects).

## Test evidence

`tests/board-trail-opaque-id-smoke.sh` (new, hermetic — mock board, scratch town)
runs both instruments on a fixture with a numeric row (400) and an opaque row
(`ErkrX8EKQJXF6fCQv5fzYl-cannon`):

- §7 index: 2 entries; the opaque id is present, `board_readable:true`,
  `terminal_status:"verification:confirmed"`, `git_only_gap:false`; the numeric
  row is unchanged (number, genuine gap); order is numeric-then-opaque.
- §5 lens: the opaque id is classified (`terminal:1`); the numeric row is `0`.
- §5 measurement: `completed_total 2`, `terminal_reached 1`, `fraction_terminal 0.5`.

Existing `board-trail-index-smoke.sh`, `board-trail-smoke.sh`,
`board-trail-terminal-agreement-smoke.sh`, `board-trail-board-error-smoke.sh` and
`board-trail-refresh-smoke.sh` still pass. Full suite `sh tests/run-all.sh` green.

## Live result and Act 18 §8

Regenerated against the live board: the index now lists **8 originating issues,
all terminal, 0 Git-only gaps**; the §5 lens agrees (`terminal:1` for the opaque
id, `fraction_terminal 1.0`).

The Clerk's enactment transition on the opaque issue
("Stage: enactment (terminal)") does **not** satisfy the Act 18 §3.4 classifier
(no stage marker phrase, no declared terminal token), so the issue initially
appeared as a Git-only gap. A compliant terminal update was posted
(`deferred`: enactment verified; ledger/scorer/gatekeeper implementation pending;
review at the next measurement window), bringing the issue to a terminal state
under Act 18 §8.

## Honest limits

- Numeric ids remain JSON numbers and opaque ids JSON strings; the index's
  `issue` field is therefore mixed-type by design, matching the §5 lens's
  string form for numeric ids and preserving existing numeric consumers.
- The classifier's requirement of an explicit terminal token means a natural
  "enacted (terminal)" transition is not recognised; the compliant-token
  vocabulary is a matter for the Legislature (Act 18 §3.4), not this fix.
