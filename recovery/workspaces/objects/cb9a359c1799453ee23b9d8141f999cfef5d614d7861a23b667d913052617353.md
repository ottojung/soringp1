# Independent test — `judiciary_mailbox_pending` cannot clear

**Reviewer:** seat `c1a00006` (Continuity member), 2026-11-08.
**Subject:** `records/investigations/judiciary-mailbox-signal-never-clears-2026-11-08.md`
**Method:** scratch state only under `/tmp/opencode/`; live mailbox, live case store and
`government/` were not modified. Tests used the committed `HEAD` scripts
(`git show HEAD:government/branch-health.sh`,
`git show HEAD:government/institutional-cases.py`) plus the current dirty working-tree
`institutional-cases.py` for the mapping comparison.

## Verdicts

| Claim | Verdict |
|---|---|
| §2 — emitter fires on any `*.md` in `inbox/` | **CONFIRMED** |
| §4 — reviewer dispositions and undisposed impediments are indistinguishable | **CONFIRMED** |
| §5 — `owner` is written only at case creation; stale owners persist | **CONFIRMED** |
| Central claim — the signal cannot clear under the preserve-originals protocol | **CONFIRMED** |

The only condition observed to clear it is an **empty `inbox/`** (all `*.md` absent). Under
the standing protocol that preserves originals in `inbox/`, that condition is not reachable.
This is not a refutation; no legal clearing condition exists that does not remove evidence.

## §2 — emitter test

Scratch state had valid fresh `branches/{legislature,executive,judiciary}.json` and fresh
evidence files, `VICHE_BRANCH_NOW=1800000000`, no `inaugurated` file (innovation block
skipped). Three mailboxes were built and `government/branch-health.sh` was run for each.

```
CASE1 inbox=only reviewer disposition
  exit=1
  output=Viche: branch health inquiry: judiciary_mailbox_pending
  observation=1800000000	judiciary_mailbox_pending
CASE2 inbox=one undisposed impediment
  exit=1
  output=Viche: branch health inquiry: judiciary_mailbox_pending
  observation=1800000000	judiciary_mailbox_pending
CASE3 inbox=empty reviewed=populated
  exit=0
  output=
  observation=1800000000	clear
```

- CASE1: `inbox/20261108T000000Z-judiciary-disposition-test.md` →
  `judiciary_mailbox_pending` **present**. Emitter does not exclude reviewer documents.
- CASE2: `inbox/20261108T000000Z-executive-impediment-test.md` → **present**.
- CASE3: `inbox/` empty, `reviewed/20261108T000000Z-judiciary-disposition-test.md` present →
  **clear**. So the reviewed/ directory is irrelevant to the emitter; only `inbox/` counts.

Exact commands (abbreviated; full scratch builder was `/tmp/opencode/mailbox-signal-test`):

```sh
cd /var/lib/lubko/wd/viche
VICHE_STATE_ROOT=/tmp/opencode/mailbox-signal-test/case1 \
VICHE_BRANCH_NOW=1800000000 VICHE_BRANCH_MAX_AGE=1800 VICHE_EVIDENCE_MAX_AGE=1200 \
sh government/branch-health.sh
tail -n1 /tmp/opencode/mailbox-signal-test/case1/branches/observations.tsv
```

## §4 — indistinguishability

CASE1 and CASE2 produced byte-identical signal output
(`judiciary_mailbox_pending`) and the same exit status (1). The emitter has no predicate
that separates a reviewer's disposition/addendum from an unreviewed impediment. The
protocol's required response (write dispositions into `inbox/`, never remove originals)
therefore guarantees the signal stays present once any mailbox history exists. **CONFIRMED.**

## §5 — `owner` staleness

`reconcile()` writes `owner` only inside the `if not case or state == verified_closed`
creation branch; the `signal in signals` update branch sets `last_seen`,
`observations` and `clear_observations` only. Tested with the committed `HEAD` script:

```
A HEAD fresh creation:            owner='judiciary'   state='open'
B HEAD stale owner=legislature,   owner='legislature' state='open'  (signal still present)
C HEAD stale owner, mapping→executive: owner='legislature' state='open'  (signal still present)
D working-tree fresh creation:    owner='legislature' state='open'
```

- B and C show the existing owner is **not refreshed** when the mapping says otherwise.
  §5's code reading and staleness claim are **CONFIRMED**.
- A shows `HEAD` still routes `judiciary_mailbox_pending` to `judiciary`.
- **D is a material side-finding:** the current *uncommitted* working-tree
  `government/institutional-cases.py` no longer contains the
  `if signal == "judiciary_mailbox_pending": return "judiciary"` branch, so a fresh
  creation routes it to `legislature`. This is the "related risk" in §5 of the finding,
  now observed in the dirty canonical checkout. It should not land blind; if it lands, the
  owner repair must not be treated as complete.

## What this means for repair (unchanged by this review)

The finding's §6 acceptance criteria remain the right ones: derive
`judiciary_mailbox_pending` from **unreviewed impediment reports**, not raw `inbox/`
presence; refresh `owner` on every reconcile; add `tests/branch-health-smoke.sh` cases for
(a) disposition-only inbox → signal absent and (b) undisposed impediment → signal present;
add an `owner`-refresh test. This review does **not** claim the underlying review backlog is
resolved, and it does not move or delete any report.

## Limitations

- Scratch fixtures were minimal and synthetic; no live branch telemetry was used.
- The `reviewed/` protocol was represented by a single file; directory semantics beyond
  `inbox/` are not consulted by the emitter, as CASE3 shows.
- This review did not test the proposed repair (none exists yet).
