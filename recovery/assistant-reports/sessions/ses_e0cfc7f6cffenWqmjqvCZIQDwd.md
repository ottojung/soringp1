# antonina-wvpCLXjmQVlqLp1vhLbr6J-purple

Session: ses_e0cfc7f6cffenWqmjqvCZIQDwd
Workspace: /home/lubko/soring-fronts/fotc-program-vs-dag-size-20261119exec
Created: 1795078455584; updated: 1795079662992

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f3038376001QI8CDcCv3ARvKi)

I'll start by reading the required documents and understanding the research context. Let me gather everything in parallel.

## Output 38 (msg_1f303ad5e001VFCQywvCR7s6nm)

The strategy-program note isn't in my worktree. Let me fetch it from origin/main at commit f89f6d0, and pull the board digest.

## Output 53 (msg_1f303bd85001i5g4eos1iZGJxP)

Now let me examine the framed-DAG certificate data (issue #47) and verify my environment/author identity.

## Output 72 (msg_1f303d69100161vq2N83hpaY17)

I'm on billy-dev, as required. Let me check my front's ledger entry, scan the full board for prior posts by my author, and look for issue #47's framed-DAG sizes.

## Output 100 (msg_1f3040c950019adGkbUSJkkZB0)

Let me do a full board scan for my exact author, fetch issue #47, and examine the relevant scripts/docs.

## Output 115 (msg_1f304cda4001zphU317Ppu9NR8)

Let me read the rest of issue #47 and the prior related FO(TC) board posts.

## Output 130 (msg_1f305b32a001Oga0pgKUeLQCF0)

I have the key documents. Now let me build the experiment in `/tmp/opencode`. First, the poset/minimax core with verification against known values and DAG node counts from the docs.

## Output 159 (msg_1f30749e6001qUQgCMRkp7VUJU)

Core verified exactly against the docs (S=5,7,10; DAG(1)=47,239,1439; DAG(all)=181,1551,65551). Now the decision-list program learner and the full measurement.

## Output 197 (msg_1f30d9a62001JdbFmYx1YJtbWG)

The naive learner confirms an important negative: label-specific decision lists don't compress (rule count approaches state count). The genuine compression comes from schema/symmetry rules. Let me implement that cleanly and produce the full measured table.

## Output 235 (msg_1f31123460019ClIK0hzWHoQ49)

The schema/symmetry program is verified correct (all n! orders sorted, max comparisons = S(n)). Let me check n=7 tractability and finalize the framed-DAG reference numbers.

## Output 246 (msg_1f3137ab2001fTODI0qzVqTTur)

n=7 is not tractable with my from-scratch minimax canonicalization (timed out), so I'll report n≤6 measured plus n=7 by known values. Let me verify the Antonina command syntax and draft the single report.

## Output 275 (msg_1f3141716001J9gm3Vgwoc7aF0)

Report drafted. Let me do the final exact-author scan once more (defensive) and then post exactly one comment.

## Output 293 (msg_1f3150d1d001z8U7IdRXNhcniv)

The post succeeded (id `sha256:7EihxIJrHqRuhRh3ZxJ3OhAGPgSrZQKTKWfFEGzpBVA`, timestamp 09:13:21Z). Let me confirm exactly one post by my author and a clean worktree.

## Output 304 (msg_1f315bdf9001wCyo9lHxjvKWrl)

Done. Here's a summary of the completed research front.

## What I did

Executed the explicit "Next experiment" from §7 of `docs/research-fo-tc-strategy-programs.md` (origin/main `f89f6d0`) on billy-dev only, with all scratch under `/tmp/opencode/fotc`.

**Verified core (independent implementation):** `S(4,5,6) = 5,7,10`; `DAG(1) = 47,239,1439` (= 2n!−1); `DAG(all) = 181,1551,65551`; quotient `q(all) = 12,19,134` — all matching the docs. Every one of the `n!` input orders was simulated for each program; output verified correct and max charged comparisons equalled `S(n)`.

**Measured table (worst case over all `n!` orders):**

| n | S(n) | schema-program rules / bits | naive rules | charged comps (max; dist) | framed DAG nodes (single/all/quotient) | bit gap |
|---|------|------------------------------|-------------|---------------------------|----------------------------------------|---------|
| 4 | 5 | 7 / 196 | 15 | 5; 4→8, 5→16 | 47 / 181 / 7,12 | 5.3× |
| 5 | 7 | 18 / 828 | 71 | 7; 6→8, 7→112 | 239 / 1551 / 11,19 | 9.5× |
| 6 | 10 | 66 / 3960 | ≥hundreds | 10; 7→16,8→32,9→96,10→576 | 1439 / 65551 / 27,134 | 16.0× |

**Direction:** `[conjecture]` state-rule (schema/symmetry) compression is more succinct — growing bit gap 5.3×→9.5×→16.0×. `[deduction]` against the alternative: unrolling a poly-size program into a framed DAG costs up to A001035(n)=2^{Θ(n²)} nodes, so a *polynomial*-overhead DAG simulation is false in general. `[experiment, negative]` label-specific decision lists don't compress (15/71 rules, near state count) — compression requires a rule language with variables/symmetry.

**Precise obstacle to all-n:** no known all-n poly-size, poly-time program of height exactly `S(n)` (Ford–Johnson optimal only to n=11; Sergeev asymptotic not exact; F-computation disallowed); n≤6 can't separate growth rates; counting FO(TC) formula length literally would erase the gain; n=7 not tractable with my from-scratch canonicalization. No completeness, class-membership, or optimality claims were made.

## Delivery

- Scanned all 60 pages of #301: **0** prior posts by my exact author.
- Posted **exactly one** report via `antonina board comment --id 301 --author "SoringP1 frontier: fotc-program-vs-dag-size-20261119exec" ... --json` (id `sha256:7EihxIJrHqRuhRh3ZxJ3OhAGPgSrZQKTKWfFEGzpBVA`, 09:13:21Z). Re-scan confirms exactly one post by that author.
- Worktree left clean (detached at `6a96398`); no repo/Lean/test/workflow/ledger changes.
