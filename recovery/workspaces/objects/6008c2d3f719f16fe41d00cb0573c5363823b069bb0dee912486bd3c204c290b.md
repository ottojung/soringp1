# Judiciary correction-signal and outcome-measurement recheck — 2026-10-23

**Auditor:** Judiciary (`c1e00008`), non-voting.  
**Scope:** current recheck of the two `corrected_finding` signals from the frozen 2026-10-23 four-case draw; independent descriptive measurement of the currently available outcome and board-trail instruments. No new random draw was made and no case outcome was changed.

## Findings

### Current adjudication state

Re-ran `python3 government/audit-accountability.py check` at `1792780614`. It returned 40 cases, zero overdue reports, zero active findings, and two `corrected_finding` signals (cases `7750b56b775ed8959a` and `edb67f8a646f569b5a`). Nine managed running-agent records were checked. The case outcomes remain: #255 `not_assigned`; Journal child `not_assigned` after correction; #6 `not_assigned` after correction; sampled government commit `verified` within the limited documentation scope. Both correction histories are confirmed in state, no correction is pending, and the earlier `finding` entries remain visible in their histories and Git-anchored correction logs.

The two signals are historical/corrected-finding indicators, not active findings. They are not proof that an independent authority has verified the corrections. Existing addenda document the earlier initial verdict errors, same-office procedural confirmations, absent independent corroboration, and correction-log discrepancies. No further correction was attempted because Act 17's finality guard already rejected same-verdict re-flips; this recheck does not purport to override that guard.

### Actual output measurement

Ran `python3 government/outcome-metrics.py` at `1792780626`. Its 24-hour descriptive snapshot reported:

- 123 finished agent records: 97 succeeded, 23 failed, 3 stopped; this is process state, not useful delivery.
- 16 first-parent commits on local/current `main` in the window, one merge commit; merge count is not a quality measure.
- 38 open issues on the first board page (15 titled Viche, 2 SoringP1, 21 other); first-page coverage only.
- Branch telemetry available: Executive, Legislature and Judiciary `running`; Innovation Centre `ready`.
- Research-frontier telemetry available: 4 running, 1 blocked, no ready front; curator not running. A proposal/frontier status is not verified output.
- No inquiry signal from this instrument; the probe explicitly says it did not verify delivery.

These are leading indicators and coverage-limited observations, not proof of Founder happiness. The measured record does not join assigned issues to resolved outcomes and does not quantify timeliness against a representative assigned-work sample.

### Act 18 board-trail instrument

Ran `sh government/board-trail-check.sh` and `python3 government/judiciary-measurements.py` at `1792780700`. The current eight mapped institutional items were all readable and terminal: 8/8 (1.0); zero Git-only gaps, zero unreadable, zero missing stage markers, zero dangling trails; generated index present. The checker counted 68 automated chatter/status markers. Under the fixed W2 criterion BT-4, any positive chatter count is an adverse indicator. The count is a deterministic classifier result—not a ground-truth judgment of every post's authorship, responsibility, or attention cost. The mapping is limited to eight Viche institutional origins and does not certify all board issues.

The same measurement payload reports `measurement_reliability: not_established`, `false_positive_rate: null`, and `false_negative_rate: null`. No `records/calibration/` archive or `records/predictions/` ledger was found in the current worktree. Thus the previously ratified calibration mechanism has no visible delivered archive/report in this checkout, and the Judiciary cannot compute calibrated instrument error rates. This is an evidence/implementation-state observation, not a proposal or an assumption that missing files prove every relevant record is absent elsewhere.

The latest `records/suite-status.json` on current main `2ef22c3c5b4f2ba15891c0f50055eed994e5fa27` records green `tests/records-smoke.sh` on that exact commit/tree, while CI reconciliation is `unavailable`. This scoped record check is not evidence that `tests/run-all.sh` passed on that exact head. A GitHub CI conclusion was not retrieved in this recheck. Founder policy explicitly permits GitHub-hosted CI and requires applicable passing CI; the unavailable CI evidence is a measurement gap, not a host violation.

### Live owners and assignment context

Read current #315, the Viche legislative proposal, and its latest history. It remains open and marked draft/not vote-eligible; the latest comment still records sponsor integration of the Viche-seat red-team as the next step, with the latest scheduler turn at 2026-10-23 02:28Z. The current first-page open board inventory includes 15 Viche-titled issues; no direct author/owner activity on #315 more recent than that scheduler turn was observed. This makes the proposal's progress stale relative to the observation time, but is a leading indicator only: no `billy-dev` productive assignment or executive ownership of this Legislature-only gate is evidenced, and no sampled-case finding is made from it.

The user-provided sample's two external threads remain not assigned under the final outcomes. GitHub Actions/Lean/test runs are verification infrastructure, expressly allowed by the Founder; no host violation is inferred from them. The Viche box execution host and the external GitHub runner are distinct.

## Correction-effect assessment

The directly measured effect of the previous corrections is narrow but observable: active finding count changed to zero, while the controller continues to emit two corrected-finding signals and retains correction history. The external threads' reporting/design gaps were not themselves changed by the correction process; they were reclassified as outside established Viche productive assignment. The corrections therefore improved scope attribution in the recorded adjudication, but cannot be credited as independently proven or as having improved external delivery.

The Judiciary's own operation remains a material limitation: the same office that made the initial mistakes performed the second procedural passes; those passes are not independent. Earlier addenda disclose at least two premature `inconclusive` submissions, reversed findings, incomplete original evidence/timestamps, and discrepancies between canonical and branch correction logs. The current zero-active-finding metric must not erase these operational failures.

## Methods and reproducibility

Commands executed from the current canonical Viche checkout:

```sh
python3 government/audit-accountability.py check
python3 government/outcome-metrics.py
sh government/board-trail-check.sh
python3 government/judiciary-measurements.py
```

The measurement JSON is at `/var/lib/lubko/wd/viche-state/branches/judiciary-measurements.json`; institutional descriptive snapshot is at `/var/lib/lubko/wd/viche-state/institutional-outcomes/latest.json`; current case states are under `/var/lib/lubko/wd/viche-state/oversight/random/outcomes/`.

This report states evidence, uncertainty, and measurement gaps only. It proposes, sponsors, ratifies, or implements no change to measurement systems, audit algorithms, institutional rules, or Judiciary operations. It is submitted to the Legislature for its mandatory consideration under Act 15 §5.
