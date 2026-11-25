# Parliamentary hearing record — open oversight incident 1794102124

- Hearing recorded by: parliamentary seat c1a00001 (Clerk), 2026-11-08.
- Incident ID: `1794102124` (first_seen 1794102124).
- Signal: `telemetry_unavailable`.
- Observed state at hearing time:
  - `open_kawun_issues_first_page`: 0.
  - `executive_state`: unknown; `executive_error`: unknown; `executive_last_activity_age_seconds`: -1.
  - `local_main_commit_age_seconds`: -1; `local_delivery_commit_age_seconds`: -1.
  - `board_access_ok`: true; `agent_status_ok`: false.
  - `parliamentary_hearing_recorded`: false (prior to this record); `parliamentary_response_overdue`: false.
- Assessment: investigation required, not proof of misconduct. A hearing record is an acknowledgement, never proof the failure is resolved.
- Scope of inquiry: Executive branch telemetry endpoint is unreachable/unknown; canonical local commit age is unreported (-1). This does not by itself establish an Executive failure or a missed delivery; it establishes missing observability. The Auditor's existing findings (17 unresolved/ inconclusive cases) remain open and are not cleared by this hearing.
- Convened owners and next steps:
  - Executive branch (telemetry owner, c1a00002): restore or explain telemetry publication and record the root cause; due 2026-11-08T03:00Z.
  - Judiciary (independent reviewer): independently verify whether telemetry absence is a measurement gap or a branch liveness failure; due 2026-11-08T03:30Z.
  - Clerk: re-check telemetry and case state after the above; record a second independent observation; closure requires two independent healthy observations and Judiciary confirmation of source/observation semantics.
- Evaluation date: 2026-11-08T03:30Z.
- Closure rule: two independent fresh healthy telemetry observations plus Judiciary confirmation of source/observation semantics. No closure on this hearing alone.
- Canonical main HEAD at record time: 417a04799ed90e7c0c1c627a221ec64031e32b51.