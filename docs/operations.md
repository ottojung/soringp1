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

## How many agents to run

Run one agent per **distinct, curated research question**, up to a target
of five. The number of questions decides the number of agents, not the
other way round: if only three questions are worth asking, three agents
run. Never invent work to fill a slot. Agent count is not a measure of
progress.

Each packet must state a precise all-`n` question, its consequence for the
uniform complexity of `S(n)`, permitted assumptions, non-goals, how it
could be falsified, and when to stop.

## The pool keeper

`scripts/agent_pool_keeper.py` runs on billy-dev (it refuses to run
elsewhere) and enforces the rule above:

- Every 10 seconds it counts running SoringP1 agents (title prefix
  `SoringP1` or a worktree under `/home/lubko/soring301`).
- If fewer than the target (default 5, `--target N` to change) are
  running, it relaunches roster agents with their **next curated packet**
  from [`research-packets.json`](research-packets.json), oldest first.
- An agent that finished in the last 4 minutes is not relaunched yet, so
  quick completions do not flood the board.
- An agent whose curated packets are all used is **awaiting curation**: it
  is not relaunched and not given a made-up task. The keeper logs how many
  tracks are waiting. The running count may stay below the target. **This
  does not complete or pause Viche's standing SoringP1 research mandate.**
- A running agent with no output for 30 minutes, or one that can return to
  the preferred model after a quota cooldown, is steered in place with its
  next curated packet (at most one per tick). Exhausted tracks are not
  steered.

Agents are reused by ID in the worktree they were created for; the keeper
refuses agents whose declared worktree is missing or different.

State lives in `/home/lubko/.local/state/soringp1/` (`agent-pool.json`
for last-launch times, `packet-cursors.json` for each agent's position in
its packet list). A lock file prevents two keepers from running.

Merging a keeper change to `main` does not update the running process:
pull on billy-dev and restart the keeper.

## Continuous research mandate (Founder, 2026-10-22)

Viche's Executive must continue work on SoringP1 until its final mathematical
theorems are actually proved, independently checked and published, and all
authorized SoringP1 work is genuinely resolved. A finished agent, exhausted
packet list, or temporarily empty keeper pool is **never** evidence of project
completion. The keeper is only an execution convenience for previously curated
questions, not a definition of the research frontier or its end.

The Executive shall regularly inspect the newest `main`, open issues,
`#301`, mathematical gaps and research results. It must actively identify
and commission nonredundant, falsifiable new mathematical approaches, including
after the keeper exhausts its finite plan, using the current research plan and
literature. Neither a fixed agent number nor adding duplicate packets is an
acceptable substitute for substantive progress. Formalization follows mature,
relevant theorems rather than becoming the main objective.

The current Antonina CLI requires `agent run --cwd <declared-worktree>` on
**every** run, including resuming an existing agent and `--steer`. The keeper
uses the verified declaration to specify that directory explicitly.

## Curating packets

To give a track new work, append a question to that agent's list in
`docs/research-packets.json` (format version 2: a shared `common`
preamble plus a list of packets per agent ID; each packet at least 60
characters, no duplicates). The keeper picks it up on its next tick
without a restart. To add a new agent, add it to `ROSTER` in the keeper
and give it packets.

Good packet sources: open obstacles reported on #301, the open questions
in [research-plan.md](research-plan.md), and independent review of a
recent central claim. Examples of distinct question families:

- tightness of the gap between computable lower and upper bounds;
- algorithms that avoid enumerating winning partial-order states;
- structural classification or compression without counting every
  isomorphism class;
- lower-bound mechanisms and the `n = 12` obstruction;
- threshold certificates and the cost of verifying them;
- encoding-faithful reductions for the fixed antichain `S(n)`;
- recurrences and subproblem composition;
- literature and model audits, and independent falsification of central
  arguments.

## Orchestrator's loop

1. Check `main` and open PRs, board #301, the agent pool, and recent
   results and failures.
2. Reconstruct the set of materially different open questions.
3. Curate packets only for questions that are distinct and falsifiable
   and have an explicit consequence for computing `S(n)`.
4. Collect results without waiting for every agent. Retry infrastructure
   failures without treating them as mathematical refutations.
5. Compare conflicting claims proposition by proposition; an independent
   review or bounded counterexample search beats voting.
6. Record durable findings on #301. Repository changes go through the
   publication gate in `AGENTS.md`; the orchestrator does final review.
