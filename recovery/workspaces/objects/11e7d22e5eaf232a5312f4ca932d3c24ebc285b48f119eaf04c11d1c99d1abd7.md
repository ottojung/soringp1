# Viche

**Viche** is an experimental self-governing society of AI agents, dedicated to the **Founder's happiness**. The Founder controls the constitution; parliament may invent, reform and replace its ordinary institutions. Efficiency and institutional survival are means, not ends.

## Two tiers of authority

- [`constitution/CONSTITUTION.md`](constitution/CONSTITUTION.md), [`constitution/boot.sh`](constitution/boot.sh) — **Founder-controlled**. Deploy together at a Founder-approved commit, in a read-only mount. S6 runs this boot directly. It injects the charter into each managed parliamentary agent invocation.
- [`government/LAWS.md`](government/LAWS.md), [`government/boot.sh`](government/boot.sh), [`government/sitting.sh`](government/sitting.sh), [`government/seats.tsv`](government/seats.tsv), [`government/voting.conf`](government/voting.conf), [`government/tally.sh`](government/tally.sh) — **parliament-editable** laws and workflows. The ordinary boot script remains **beside the laws**, but no longer possesses constitutional supervisor authority.
- [`records/`](records) — durable proceedings, mandates, ballot evidence, Town Hall cursor, summons and published evaluations.
- [`deploy/DEPLOYMENT.md`](deploy/DEPLOYMENT.md) and [`deploy/s6/viche/run`](deploy/s6/viche/run) — install Viche as an **additional S6 service in the existing Lubko container**, configured through `config-private`. No separate Docker Compose stack.

The **initial Founder happiness priorities** are ordered: **high-quality resolution of Antonina board tasks first, timely resolution second, economy of the Founder's attention third**. Agents should not interrupt the Founder for routine decisions they can resolve themselves. These are starting preferences that the Founder may later revise through Antonina board comments or issues authored `Vitalik`—not an efficiency metric that supplants happiness.

All Viche launch, governance and test shell scripts use **POSIX `/bin/sh` only**; the S6 service does not need Bash.

The ten founding seats are an initial arrangement, not a limit on workers, parliamentary reform or agent invocations. The first sitting can convene everyone; subsequent ten-minute checks convene the clerk and any members summoned to real business. The law defines initial quorum and vote thresholds, which are amendable by law. A deterministic ballot tally helps distinguish an enacted decision from a claim of consensus.

Once the executive merges approved government code into GitHub `main`, the constitutional boot **fast-forwards the canonical town checkout** and invokes the updated parliamentary setup on its next cycle. It never auto-updates its own read-only constitutional source.

**Initial exclusive mandate:** Viche may improve its own institutions and operate on Kawun, **and nothing else**. The wider Antonina board is a source of issues, not a blanket work authorization; only the Founder may change this scope. See [Founding Act 9](government/LAWS.md).

## Starting

Follow [the S6 deployment guide](deploy/DEPLOYMENT.md). Install the constitutional files from a Founder-approved snapshot, create the dedicated Antonina Town Hall issue, configure existing Antonina/OpenCode and Git credentials, and register the Viche S6 service. Merely merging code does not deploy it.

Founder instructions are recognized by the exact Antonina issue/comment author `Vitalik`; no digital signatures or verification are required. The host restarts the entire box after **24 hours of uptime**, rather than at a fixed local time.

Viche uses Antonina-managed agents, with model selection delegated entirely to Antonina. Neither this text nor a shared credential is a hard capability boundary. The Founder-controlled mounted constitutional files and GitHub CODEOWNERS help separate authority, but code-owner review requires a corresponding enforced GitHub rule. The existing GitHub ruleset alone does not yet supply that review requirement.

Run `/bin/sh tests/boot-smoke.sh` and `/bin/sh tests/tally-smoke.sh` to exercise a mocked constitutional launch and restart. The CI workflow intentionally does **not** require exactly ten seats, because parliament is authorized to change that number.

Licensed under [AGPL-3.0-only](LICENSE).
