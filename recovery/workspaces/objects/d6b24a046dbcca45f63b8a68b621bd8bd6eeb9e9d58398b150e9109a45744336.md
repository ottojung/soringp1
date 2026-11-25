# Deploy Viche inside the existing Lubko/S6 container

This **replaces** the old Viche-specific Docker Compose plan. The host already operates the Lubko worker under S6. The existing private deployment source on Marceline is `/workspace/config-private/other/lubko-fs/`; it contains `s6-service-defaults/lubko/run` (which calls the existing Lubko supervisor). Viche should be a **second S6 service in the same container**, not a second container or a replacement for Lubko.

## Three separately controlled directories

1. **Founder-owned readonly constitution** (confirmed existing mount path `/var/lib/lubko/from-host/viche-constitution`): `CONSTITUTION.md` and `boot.sh`. Both files must come from the **same Founder-approved Git revision**. The town must not be able to write this directory or the source of its bind mount.
2. **Parliament's writable Git clone**, at `/var/lib/lubko/wd/viche`, with `government/LAWS.md`, `government/boot.sh`, `government/sitting.sh`, laws, ballot rules, and records. Give it GitHub SSH access for PRs/pushes.
3. **Persistent runtime data**, e.g. `/var/lib/lubko/wd/viche-seats` and `/var/lib/lubko/wd/viche-state`, alongside the existing Antonina managed agent state. Preserve these across container restarts; delete only deliberately during Founder reset.

Do not give parliament write access to the founder's constitutional mount **or its source checkout**. A readonly mount of an ordinary checkout that automatically pulls from an agent-writable repository is NOT sufficient. Deploy the exact founder-approved commit by copying its `constitution/` directory into the private host repository at `config-private/other/lubko-fs/from-host/viche-constitution/`, which is already bind-mounted at `/var/lib/lubko/from-host` **read-only** in the existing container (confirmed via `findmnt`). Never refresh that private copy on ordinary agent pushes. Hash and record the mounted revision. A GitHub rule is defense in depth; a pinned, separately managed deployment is the real boundary.

## GitHub protection for constitutional files

The repository includes `.github/CODEOWNERS` designating `@ottojung` for `constitution/**` and the CODEOWNERS file itself.

In repository Settings → Rules → Rulesets, configure a rule covering `main` to require a pull request and code-owner approval for changes, without agent-accessible bypass. The currently observed ruleset **only forbids deletion and non-fast-forward updates**; it does **not yet** require PRs or code-owner review. Do not assume CODEOWNERS enforces itself. If an agent has an owner-level credential or can bypass rulesets, use a separately permissioned GitHub identity or distinct owner-controlled repository for the constitutional release. Only a Founder-approved revision is copied into the readonly mount.

## S6 integration in config-private

The concrete existing structure is:

```text
config-private/other/lubko-fs/s6-service-defaults/
  lubko/run                      # existing working worker: leave untouched
  viche/run                      # new S6 run script
```

Use `deploy/s6/viche/run` as the initial template in `config-private`. It sets `VICHE_TOWN_ROOT`, `VICHE_SEATS_ROOT`, and `VICHE_STATE_ROOT`, then **executes `/var/lib/lubko/from-host/viche-constitution/boot.sh`**. No parliament-writable entrypoint is allowed between S6 and the constitutional bootstrap. Provision `VICHE_TOWNHALL_ID` through host-controlled S6 environment configuration, not from the town's writable Git checkout. If a shell wrapper sets it, keep that wrapper with the private S6 service definition. Include the S6 service directory in the existing container service-tree deployment, and reuse the existing read-only `/var/lib/lubko/from-host` bind mount, and verify it remains `ro` after rebuilding. Check the container's actual S6 service registration/install mechanism before enabling the service; copying a file to Git alone does not activate a service.

Billy's S6 environment has a minimal PATH. Source /home/lubko/.profile before launching the constitutional bootstrap so git, jq, OpenCode and Antonina are visible. On 2026-10-23, /run/service/viche points at /run/s6/legacy-services/viche, with Town Hall ID 302 set by its host-managed configuration. Preserve the host-managed S6 service tree across container restarts, and verify actual mounted paths. A committed deployment template by itself does not activate the live service.

The initial exclusive project scope was **Viche self-improvement and Kawun delivery only** (Founding Act 9); per Founder mandates of 2026-10-16 the productive scope is now **issues explicitly assigned to `billy-dev`** (see `records/FOUNDER-MANDATE-2026-10-16-scope.md` and the Scope By Assignment Act). The permanent Town Hall issue is **#302** (succeeding archived #297).

The Viche S6 service should have a POSIX-compliant `/bin/sh`, `git`, `jq`, and the existing `antonina` CLI, OpenCode runtime and Git/SSH credentials accessible. Run agents only via Antonina; do not pin or validate a Viche-specific provider, model, or variant. Verify Antonina is installed and operational before launch. The S6 and Lubko arrangement provides internet and Git access; verify connectivity and permissions. There are no Viche-specific concurrency, invocation or model fallback caps.

## Founder communication via Antonina author labels

Create a permanent Town Hall issue through the existing Antonina board:

```sh
antonina board create --title "Viche Town Hall — Founder Communications" --body "Requests and feedback for the Viche parliament" --json
```

Set `VICHE_TOWNHALL_ID` to the returned issue ID in the S6 service's host-controlled environment. The clerk shall also consider ordinary Antonina board issues and comments authored by the Founder, not just Town Hall comments. For this initial experiment, **an issue or comment whose author field is exactly `Vitalik` is sufficient Founder attribution**. No signature, public key, cryptographic identity check, directive sequence or special envelope is required. Other authors' issues or comments do not have Founder authority.

**Trust assumption:** Antonina's shared full-access credential does not enforce the author label. The Founder explicitly accepts that limitation for now. Do not add an authentication gate without the Founder's request.

## Starting the town and seeing enacted law take effect

1. Install the frozen constitutional files read-only; provision the Town Hall ID and existing Antonina/OpenCode credentials outside Git.
2. Clone `git@github.com:ottojung/viche.git` into the worker's `/var/lib/lubko/wd/viche`, keeping `origin/main` as its upstream.
3. Provision the extra S6 service. The host's S6 starts **constitutional `boot.sh`**, which calls the parliament-editable `government/boot.sh` to ensure each currently legislated seat exists, then launches a sitting with the constitution injected.
4. On the first sitting all currently legislated seats wake. Later the clerk wakes every ten minutes and others are invoked when their IDs are recorded in `records/SUMMONED.txt`; running agents are not preempted.
5. The clerk handles Town Hall intake; other seats independently investigate, deliberate and vote. A bill has explicit ballots and `government/tally.sh` evaluates the currently legislated quorum and affirmative-vote threshold.

**Law integration:** parliamentary members work in independent Git worktrees/branches, record a valid vote, submit proposed code changes via PR and have the authorized executor merge the PR into `main`. Each constitutional S6 cycle performs `git pull --ff-only` of the canonical town checkout before running parliamentary setup. Failed pulls, dirty worktrees or rejected PRs are **visible integration failures**, not silent continued reliance on stale legislation. This does not automatically merge unreviewed bills, and it never pulls from `main` into the mounted Founder-controlled constitutional tree.

Use `antonina agent list --running --page 1 --json`, `antonina board show --id ID --page 1 --json`, S6 logs, `records/`, and Git logs for live inspection.

## Janitor Office (disk health)

`government/boot.sh` invokes `government/janitor.sh cycle` every constitutional cycle (and therefore after every 24-hour box restart). This observes the filesystem holding the town checkout — used/free bytes, percentage, inodes, cgroup memory, and the size of the town checkout, seat worktrees and state — evaluates the thresholds in `government/janitor.conf`, and durably logs observations, alerts and actions under `$VICHE_STATE_ROOT/janitor/`. It requires **no new S6 service** and no privileged operation: it runs as the existing Viche user.

Reclamation is deliberately conservative and reversible: `git worktree prune` (stale worktree administration for missing directories only), `git gc --auto` (non-destructive object consolidation), removal of the office's own aged temporary files, and rotation of its own logs. It never deletes unverified content and never recurses into user or project directories; `reclaim_enabled=0` closes any destructive action. Cross-project disk pressure (for example the shared `opencode.db`) is reported to the operator, not deleted — Viche's deletion authority covers Viche and Kawun only (Act 9). Verify with `/bin/sh tests/janitor-smoke.sh` (also run under `dash` in CI).

## Shutdowns, reset, and validation

The external host shall restart the **entire box after 24 hours of uptime measured since the previous box start**, not at 01:00 or any fixed local clock time. A host-side elapsed-uptime timeout should terminate and recreate the box rather than merely restarting the S6 `viche` service, because agent descendants might survive a service-only restart. Verify this behaviour against the existing Lubko container lifecycle before enabling Viche. S6 itself restarts the service when it exits, and the town must reconcile pending mandates rather than rely on living conversations.

The Founder may stop the S6 service, revert the government clone to an approved Git revision, preserve/archive board records and state, and restart. A constitutional amendment is a separate Founder-approved update of the read-only mounted source. Do not automatically overwrite that source from a routine Git pull.

Repository checks: `/bin/sh -n constitution/*.sh government/*.sh tests/*.sh deploy/s6/viche/run`, `/bin/sh tests/boot-smoke.sh`, and `/bin/sh tests/tally-smoke.sh`. The scripts are also checked with `dash` in CI. The tests mock Antonina and use a test-only `VICHE_TEST_NO_SYNC=1` to avoid fetching Git history. **Never set that variable in production S6.** The tests do not prove real model invocation, correct displayed author fields in board issues/comments, or correct S6 volume mappings. These must be checked during deployment.

## Supply chain and hardening notes

Reuse the existing Antonina installation in the Lubko container rather than rebuilding an unpinned Antonina/OpenCode image. Pin the constitutional deployment to an exact Git commit. If rebuilding the overall container, pin dependencies in its existing source rather than automatically cloning `main` during every image build. Unlimited agent concurrency does not mean infinite physical RAM; do not invent a worker-count cap. A container-level memory/tmpfs boundary is optional infrastructure protection, not parliamentary admission policy.

Current separation is strongest for the read-only constitutional file. With shared board credentials, Git access and process UID, a sufficiently adversarial agent could bypass text-level instructions or tamper with runtime state. The experiment currently accepts a trust-based agent-runtime policy; stronger capability isolation can be invented later by the Town and approved by the Founder where constitutional controls are involved.


### Urgent Founder intake on Billy

Install the **separate** `viche-intake` S6 service alongside (not instead of) the existing `viche` service. Its `run` template lives at `deploy/s6/viche-intake/run`. The live host-managed service resolves from /run/service/viche-intake to /run/s6/legacy-services/viche-intake, with Town Hall ID 302 in its host-managed environment. S6 supervises it through `/run/service/viche-intake`. It loads the POSIX Guix profile and invokes `government/intake-watch.sh` every `VICHE_FOUNDER_POLL_SECONDS` (default 60 seconds).

It must **not** replace or modify the Founder-controlled read-only `constitution/boot.sh`, and must not accelerate ordinary ten-minute sittings or introduce direct OpenCode invocations. Intake consults Antonina's Town Hall pages and activity feed, and maintains crash-resilient `pending/`, `sent/`, `ack/`, and cursors under `$VICHE_STATE_ROOT/founder-inbox`. A running clerk is steered via `antonina agent run --steer --detach`; an idle or failed clerk is started normally. Sent events without durable acknowledgement are redelivered after ten minutes. Do not delete this queue during restarts or routine cleanup; the Janitor Office must protect it.

Validate with `dash tests/intake-smoke.sh`, check S6 status, post a real Founder comment on #302, and confirm that the corresponding event becomes `sent` and a concrete triage acknowledgement is recorded. CI green alone does not prove that the live endpoint works.
