# Founder mandate M-019 — SoringP1 is exploration-first (2026-10-17T21:16Z)

*Clerk c1a00001, urgent Founder intake. Author of the source comment is exactly
`Vitalik` (Constitution IX). Relayed by an authorized ChatGPT session; the Town
treats the `Vitalik` label as the Founder, without further verification. This is an
ordinary priority/mandate change; it does not amend the Constitution (III, IX).*

## Source

- Antonina issue **#301** comment 2026-10-17T21:16:05Z, author **`Vitalik`**,
  message id `sha256:mDxYFYlP65XhmVX-gutDFu4hf1QQdEhiiGnu70Sww4E`; founder-inbox
  event key `2594b8f1b0bd41b944d4c3d65d2c6eb6dfa7edbef3e9fdc9da73d4ff6999d9ba`.
- The #301 description was updated with the same "exploration first" direction.
- Operative contract: SoringP1 main commit `7ebe94db` (PR #4, signed, merged; PR CI
  and post-merge CI green) — `AGENTS.md`, `docs/exploration-agenda.md`,
  `docs/research-plan.md`, `docs/formalization-plan.md`.

## Mandate (as directed)

1. **SoringP1 is now exploration-first.** Preserve the checked Lean foundation and
   CI. **Pause serial theorem/auxiliary-lemma milestones** (the routine Lean
   milestone queue). Discovery comes first.
2. **Assign meaningful Phoebe-only research work** — not a queue of routine Lean
   lemmas. Prioritize independent, literature-grounded mathematical exploration:
   - structural compression of the minimax state space;
   - succinct certificates / complexity barriers (the unary threshold language is
     sparse — Mahaney);
   - the known `n = 12` non-tight information bound (`S(12) = 30 > ceil(log2(12!)) = 29`).
   Falsifiable hypotheses, small computational experiments, concise written
   arguments, and honest negative results count as deliverables.
3. **minimaxTree height correspondence:** one short, bounded attempt only if a
   genuinely small fix works; otherwise record the precise Lean blocker and move to
   mathematics. Do not launch a parade of auxiliary Lean milestones.
4. **Preserve in-flight work.** The Executive's uncommitted `a24-height` work
   (`/home/lubko/soring301`, branch `executive/a24-height`, 68-line change to
   `SoringP1/Minimax.lean` adding `minimaxTree_height`) must be preserved, not
   discarded.
5. **No duplication.** Avoid duplicate agents; report verified results and actual
   research progress on #301; progress is judged by insight, not Lean-commit count.
6. **Host/model unchanged.** All SoringP1 Viche agent execution and local builds
   stay on **phoebe-dev**; GitHub-hosted CI remains permitted (M-016). The pinned
   free model (`opencode-go/longcat-2.5-preview-free`, variant `low`) is unchanged.
   **Do not amend the Constitution.**

## Relation to prior law

- Supersedes the **routine Lean milestone schedule** (the A-series cadence) as the
  executive's SoringP1 priority. Act 9 (scope by assignment) is unchanged; #301
  remains explicitly assigned to `phoebe-dev`.

## Owner and next action (triage)

- **Owner:** the independent **Executive** (Act 2) — office `c1e00002`, liaison
  `c1a00002`. Update the executive plan/priority for exploration-first and dispatch
  a focused, non-duplicative Phoebe-only research work plan on #301.
- **Next action:** executive updates `government/executive-agenda.md` + dispatches
  the exploration-first work (structural compression; certificates/barriers; n=12
  obstruction), preserving the `a24-height` work.
- **Obstacle recorded:** the three branch offices (`c1e00002` executive,
  `c1e00008` judiciary, `c1e00011` innovation) were `failed` with
  `unrecognized_backend_failure` ("This API key has expired"); the standard
  `branch-bootstrap.sh` recovery only handles `upstream_endpoint_unavailable`, so
  the clerk performed a manual session reset (continuity). Parliamentary seats were
  running normally, confirming the key works for fresh sessions.

**Status:** triaged; owner assigned; work plan delegated to the Executive. Ack
written. Recorded in `records/MANDATES.md` (M-019).

## Verification (2026-10-17T23:24Z)

- **Receipt confirmed:** the founder-inbox watcher moved the event to `sent/` and the
  ack `founder-inbox/ack/2594b8f1…` is present, so no further retry occurs.
- **Owner executing (verified):** the Executive office `c1e00002` is **running** and
  performing the single permitted **bounded** `minimaxTree`-height attempt on the
  preserved `a24-height` work (`/home/lubko/soring301`). Branch offices `c1e00002`
  (executive) and `c1e00008` (judiciary) are running; Innovation Centre ready.
- **Delegation decision:** the Clerk delegated to the single Executive owner rather
  than summoning separate research parliamentarians (SoringP1 has one working
  checkout; the Founder warned against duplicate agents). If the Executive does not
  produce independent mathematical results (vs. Lean churn), the Clerk will convene a
  research seat at the next sitting.
