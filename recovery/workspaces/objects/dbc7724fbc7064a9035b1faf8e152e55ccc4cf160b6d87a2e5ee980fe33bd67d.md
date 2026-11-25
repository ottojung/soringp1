# Antonina CLI contract — Viche Executive

This is a verified interface map for the **installed Billy Antonina CLI**
(rechecked 2026-10-23). It is guidance, not a second scheduler or a source of
authorization. **Consult `antonina <area> <verb> --help` before using a
previously unfamiliar command. CLI `--help` and returned JSON are authoritative
if this reference becomes stale.** Do not guess option names or JSON fields.
Commands shown here are read-only unless explicitly marked MUTATING.

## Board — read-only

- `antonina board list --page 1 --json` → **JSON array** of issue records;
  each has `number`, `title`, `state`, `hasBody`, `messageCount`,
  `createdAt`, `updatedAt`, `lastActivityAt` (camelCase).
  `--state open` filters issues. **NO `--limit` on `board list`.**
- `antonina board show --id 301 --page 1 --json` → **JSON object**
  with `body` (issue description), `messages` (**array of comments**),
  `number`, `state`, `title`, `createdAt`, `updatedAt`, `review`.
  Each message has `author`, `body`, `createdAt`, `id`.
  **There are no `description`, `comments`, or `created_at` fields.**
- `antonina board feed --page 1 --json` → JSON object with
  `entries` array, `limit`, `nextCursor`, `total`.
  This is **not** an array, and `feed` or `items` are not its entry fields.
  Here `--limit 50` is supported.
- `antonina board queue list --page 1 --json` → **array of issue numbers**.
  There is no `--limit` option on `board queue list`.
- All board page numbers start at **1**. `board show` yields the latest
  messages first on page 1. Read additional pages if the returned page
  contains 50 messages or if history matters. Don't claim there are no
  messages without inspecting `messages`.

Minimal correct example (read-only):

```sh
antonina board show --id 301 --page 1 --json |
  python3 -c 'import json,sys; x=json.load(sys.stdin); print(x["title"],len(x["messages"])); print([(m["author"], m["body"][:100]) for m in x["messages"][:3]])'
antonina board list --state open --page 1 --json |
  python3 -c 'import json,sys; a=json.load(sys.stdin); print([(i["number"],i["title"]) for i in a])'
```

## Agents — read-only

- `antonina agent list --running --page 1 --limit 100 --json` → object
  `{"agents": [...], "unreadable": [...]}`. Agents have `id`,
  `state`, `title`, `cwd`, `prompts`, `last_activity_at` etc.
  Here `--limit` **is** supported. Page numbers start at 1; continue while
  a full page is returned, or otherwise if the response indicates more data.
  Filters: `--running`, `--finished`, `--clearexit`,
  `--failed`, `--stopped`, `--killed`. Inspect `unreadable`:
  do not interpret an unreadable registry as zero work.
- `antonina agent status --id <ID> --json` → object with `state`,
  `alive`, `model`, `variant`, `cwd`, `backend_error`,
  `started_at`, `finished_at`, `prompts`.
  `state == "running"` is the running-count source. Do **not** inspect
  output logs to reinterpret the runtime's run-state classification.

Correct pool-count example (read-only):

```sh
antonina agent list --running --page 1 --limit 100 --json |
  python3 -c 'import json,sys; d=json.load(sys.stdin); assert not d["unreadable"], "agent registry unreadable"; a=d["agents"]; print([(x["id"], x["title"]) for x in a if (x.get("cwd") or "").startswith("/home/lubko/soring301")])'
```

## Agents — MUTATING: use only when dispatching authorized work

- `antonina agent new --cwd <ABSOLUTE_WORKTREE> --title <TITLE>`
  creates an **idle** managed agent and prints its generated ID. Agent new --id is unsupported. Keep appointees in the runtime appointments.tsv using government/appointments.sh ensure|resolve|replace KEY. A new agent does not begin research until run.
- `antonina agent run --id <ID> --cwd <ABSOLUTE_WORKTREE> --prompt <TEXT> --detach`
  sends work. Every invocation must use the intended `--cwd`; it is **not**
  inherited from the shell. Create separate worktrees for independent writers.
  Verify `state` with `agent status` or `agent list` after dispatch.
- `antonina agent run ... --steer` **preempts** an existing run. Only use
  with explicit operational reason/authorization, not to increase the pool.
  Stopping/deleting/running agents are similarly consequential mutations.
- `antonina agent log --id <ID> --lines 100` reads output; do not treat it
  as a substitute for `agent status` for liveness.
- All agents run through Antonina. Antonina selects providers, models, variants and fallbacks. Viche must never impose a model or variant pin, nor call model providers directly. Unused agents correctly have a null model and empty models_used; status of executed agents reports only models actually used.

## Fail-closed and anti-patterns

- Never turn a JSON parser error, unsupported CLI option, or missing field
  into a conclusion like “zero comments,” “no eligible work,” or “zero agents.”
  Fix the query/parser; only trust an actually returned, validated value.
- To avoid empty or misleading issue summaries, read `body` and `messages`
  from `board show`; the `board list` summary has `hasBody` and
  `messageCount` rather than the full content.
- CLI help differs **between board and agent commands**. No global `--limit`
  assumption. Use correct camelCase board and snake_case agent field names.
- Stdout of `--json` should be parsed as one complete JSON value. CLI may
  print Node warnings to stderr; keep stderr separate, but do not discard
  CLI failures or parse truncated `head -c` output.
- For SoringP1 #301: standing target five independent unary researchers on
  billy-dev; independently choose worthwhile fronts and dispatch before
  unrelated monitoring work. Never require a registry or standalone refill task.

This contract describes interface behavior, not policy precedence. Follow the
Founder's constitution, mandates, host assignment and `executive-agenda.md`.
