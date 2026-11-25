# Founder clarification — host assignment vs GitHub Actions CI

*Clerk c1a00001, triage 2026-10-16T20:53Z. Founder communications (author exactly `Vitalik`), highest-priority intake: issue **#302** comment sha256:`iNp3MraPNZdQx-FE8cLFEEkIYct2IE6vE5WS1F1wYUc` and issue **#301** comment sha256:`haxQiOXZX2vs1OsiVsZV8YRdRTd8cVIFLrfrhU3DHRI` (both 2026-10-16T20:52Z).*

## Verbatim (combined)

- Assigning an issue to `billy-dev` means **Viche/Antonina agents** must perform their development work and run their worktrees **on `billy-dev`**. This does **NOT** restrict ordinary GitHub infrastructure.
- **GitHub Actions may execute CI, tests, builds, Lean kernel checks, and other verification on GitHub-hosted runners for any repository, including SoringP1.** GitHub-hosted CI is **not** an alternative Viche agent execution host.
- **Never delete or disable working GitHub Actions workflows merely because an issue is assigned to `billy-dev`.**
- The contrary interpretation in **SoringP1 commit `785e31d3` is wrong and is being reverted.**
- **Correct the executive guidance, audits, and any conflicting ordinary-law interpretation; keep the Constitution unchanged. Require verified passing CI when applicable.**
- #301: SoringP1 agents still may not be relocated away from `billy-dev`.

## Triage

1. **Scope of the rule.** `billy-dev` assignment governs **agent execution and substantive development work** (where Viche/Antonina agents run and where their worktrees live). It does **not** govern ordinary GitHub infrastructure: CI/tests/builds/Lean verification on **GitHub-hosted runners** is **expressly authorized** and must remain **enabled** for any repo (incl. SoringP1).
2. **A Viche/Antonina agent** (per the executive's "discover all open issues assigned to billy-dev, regardless of project" mandate) worked SoringP1 (#301) and produced the wrong interpretation (commit `785e31d3`, disabling/altering workflows) — contrary to this clarification. It is **being reverted**.
3. **Conflicting ordinary-law interpretation:** `government/LAWS.md` **Act 9** (assignment rule) does **not** itself mention CI; the error was an *interpretation* by the executive, not the law text. The law therefore does not need amendment; the **executive guidance** does. (A clarifying interpretation note is added to Act 9; the operative text is unchanged — no law is enacted without a vote.)
4. **Constitution unchanged.**

## Owner and next action

- **Owner — executive (c1a00002):** (a) **revert SoringP1 commit `785e31d3`** so the GitHub Actions workflows are re-enabled and passing; (b) apply the clarified rule in all SoringP1/Antonina work; (c) **require verified passing CI when applicable** (a green workflow run, not a claim); (d) audit its own guidance/records for the conflicting interpretation and correct them.
- **Owner — clerk (this record):** update `government/executive-agenda.md` and `government/executive-cycle.sh` with the clarified rule; add the interpretation note to Act 9; record the mandate (M-016); write acks.
- **Owner — audit (c1a00008, on summons if needed):** check for any other guidance/record asserting CI must run on `billy-dev`, and confirm the SoringP1 workflows are re-enabled.

## In-flight work preserved

Scope By Assignment Act (enacted); M-013 (Kawun residual C) pending Founder decision. No duplicate SoringP1 workers.

## Acknowledgement

Founder-inbox ack receipts written: `661b13ec884c7054767e6b4d319b3d319a5a14de080d2bf88686fbbe70876693` (#302) and `9027fe2be7802fd518413541b17ff091aa678a439fa2d1ecd3dd2c99979e6836` (#301). Triage posted to #302.
