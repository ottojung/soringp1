# Operations: execution host, research board and agent pool

How SoringP1 research is run day to day. The research rules themselves are
in [AGENTS.md](../AGENTS.md); this document only covers the machinery.

## Execution host

All Antonina/Viche agents, worktrees, manual development and experiments
run on **`billy-dev`** only (migrated from `phoebe-dev`; old host
references in archived notes do not authorize work elsewhere). GitHub
Actions CI, PR review and hosting are separate and permitted. Preserve
agent identities and research history across host migrations.

Before using Antonina on billy-dev, `source /home/lubko/.profile`.

## Research board

Findings, obstacles and negative results go to **Antonina issue #301**.
Do not print the whole board into an agent's context; use the digest:

    python3 /home/lubko/soring301/scripts/board_digest.py --recent 7
    python3 /home/lubko/soring301/scripts/board_digest.py --contains "frontier" --page 2

When posting with `--json`, redirect the output to a file. Post only when
something changed: a result, a falsification, or a precise obstacle.

## Continuous research frontier

The production keeper is `scripts/research_frontier.py`, invoked through
the existing `scripts/agent_pool_keeper.py` service entrypoint. The prior
finite per-agent packet mechanism is retained for historical tests only.

The plan is a **durable claim-once ledger** at
`~/.local/state/soringp1/frontier-ledger.json`, initially populated from
[research-frontier.json](research-frontier.json). Each front has a stable
ID, falsifiable all-n question, proposed falsifier, complexity implication,
and concrete research basis. Entries move through `ready` ->
`launching` -> `running` -> `investigated` or `blocked`.

The keeper launches **every independent ready question** in an isolated
checkout under `~/soring-fronts/ID`, using an independently created
Antonina agent. No numerical concurrency quota, old fixed roster, or
arbitrary filler work. Each front is claimed durably before execution:
restarts recover incomplete launches and never silently discard a result.
A process exit is explicitly only a recorded investigation, not a proof
or a verified final theorem.

When no fronts are ready or working, the keeper commissions one independent
research **curator**. It studies recent results, the board #301, and the
primary literature, and proposes precise nonredundant next fronts in
`~/soring-fronts/curator/frontier-candidates.json`. The deterministic
keeper checks the proposed schema, stable IDs, and exact textual duplicates
before importing them as `ai_proposal_unverified`; this is **not** a
mathematical novelty or quality guarantee. Weak or redundant fronts must
be challenged by research agents and Viche, not inflated into success.
If the curator cannot identify a useful front, an explicit empty outcome
is recorded and the next curation attempt is delayed, rather than
running repetitive work. Curators never create proofs by declaration.

The existing Viche Executive independently examines research quality and
commissioning. The Legislature and Judiciary remain independent; they
can read the ledger but do not need to authorize ordinary research.

## Operation

The `soringp1-agent-pool` s6 service runs on **billy-dev only**.
Its established entrypoint now invokes the continuous keeper. Restart
the service after merging code changes; a running Python interpreter
does not load updated code automatically.

    python3 scripts/research_frontier.py --once --dry-run

The dry run shows how many independent fronts are ready without launching
them. For actual operation use `python3 scripts/agent_pool_keeper.py`
(or let s6 supervise it). The exclusive lock prevents duplicate keepers.

The legacy `docs/research-packets.json` and finite-keeper helper functions
remain readable for historical tests, but their exhausted cursors no longer
constrain the live research frontier.

## Continuous mandate

Research continues until the actual founder-defined theorems have been
proved, independently checked, published, and the issues closed.
Neither an empty frontier nor a successful agent exit is completion.
No routine Lean formalization without a mature relevant theorem.
