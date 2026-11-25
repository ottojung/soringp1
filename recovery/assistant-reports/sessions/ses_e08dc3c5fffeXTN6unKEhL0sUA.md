# antonina-ULJMdshZ8iUlm8Medyisi7-serene

Session: ses_e08dc3c5fffeXTN6unKEhL0sUA
Workspace: /home/lubko/soring-fronts/curator
Created: 1795147678635; updated: 1795148392335

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f723c3d2001zjklNL3doemt1a)

I'll start by understanding the environment, worktree state, and the key documents. Let me explore in parallel.

## Output 29 (msg_1f723dad1001jU2Fac47e29KF4)

I'm on `main` (host matters here: "billy-dev" is the execution host). Let me verify host, branches, and read the literature/frontier files and board digest.

## Output 48 (msg_1f723f07b0013hGnYbL0Jh3RF7)

I'm on `billy-dev` (correct host), on `main` at `f89f6d0` (behind origin by 1 — I won't change branches or commit). Let me read the board digest and key research notes, and check existing candidate/ledger state.

## Output 63 (msg_1f724142c001sL08nTP9QnM5n8)

Extensive prior work exists (583 ledger fronts). Let me study the core research notes to find genuine gaps and avoid duplicates.

## Output 86 (msg_1f724350f001miefTSw2CLtMdV)

Let me extract the ledger front IDs (to avoid all duplicates) and read more research notes.

## Output 97 (msg_1f7244e230016sJPP46TmY7gzm)

Let me read the "next"/frontier notes and the newest board messages to find genuinely open directions.

## Output 120 (msg_1f724b1a3001lg9sMKAhIQomWh)

Let me read the FO(TC) note's open questions and get more of the newest board, plus a few remaining notes.

## Output 144 (msg_1f7252058001otI8JJ3Ne2W0Or)

Let me check for novelty of a "restricted greedy adversary" angle and read the series-decomposition note.

## Output 159 (msg_1f72596a2001oOaGbso7NUOaTP)

I have a genuinely new angle to test: the value of the game when the adversary is restricted to always answer into the child with more linear extensions. A proved board fact (`L_k(A_n)=C(n)`) suggests this restricted value may be strictly below `S(n)` first at n=12. Let me attack this with a small computation.

## Output 170 (msg_1f726913d001bf5fwXnr02nCfl)

G(n)=S(n) through n=7 (where S(n)=C(n)). Now let me validate further and attempt n=12, where S(12)=30 > C(12)=29.

## Output 181 (msg_1f72880700013itpGA34ERQPxj)

The general DFS blows up; let me try a sharper search restricted to perfectly balanced splits (which suffice to hit C(n)), validated on small n first.

## Output 192 (msg_1f72a92fb001LRPpVWfXaYGbpA)

Perfect-halving is too restrictive (fails even at n=6 where G=C). Let me try a beam search for an explicit budget-29 greedy-adversary chain at n=12.

## Output 203 (msg_1f72cc48c001zMH1IuPht3P5Sv)

Let me verify these angles are truly absent from the ledger before writing.

## Output 241 (msg_1f72dd1cd001ZkP9MZcUBWBthP)

The greedy-adversary angle is genuinely absent from all 587 ledger fronts and the previous list. Let me write the two new fronts and validate the schema.

## Output 295 (msg_1f72e8b04001Aln12FBFQY6xrx)

Done. I worked on `billy-dev` (host confirmed), stayed on `main` at `f89f6d0`, made no commits/Lean/tests/board posts, and changed only the required deliverable file.

## What I studied
`AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, the core research notes (`research-certificates-barriers`, `research-hardness-boundaries`, `research-winning-frontier-barrier`, `research-state-compression`, `research-compression-next`, `research-obstruction-next`, `research-one-ply-obstruction`, `research-series-decomposition`, `research-fo-tc-strategy-programs`), the current #301 digest, and all 587 ledger IDs plus the 20 previously investigated fronts.

## The claim I attacked and tried to disprove
**Claim:** "The maximum-linear-extension (greedy) adversary is sufficient for exact sorting," i.e. the game value `G(n)` against an adversary forced to answer into the child with more linear extensions equals `S(n)`. This is a genuine gap: the board's proved `L_k(A_n)=⌈log₂ n!⌉` shows greedy *leaf-counting* lower bounds never exceed the information bound, yet `S(12)=30 > 29` — so `G(n)<S(n)` is plausible, which would rule out all larger-child-only lower-bound/certificate methods.

**Falsification attempts (honest limits):**
- Built an exact minimax/`e(P)` engine in `/tmp/opencode`. Found `G(n)=S(n)` for `n≤9` (no separation there — expected, since `S(n)=C(n)` in that range).
- A stronger "perfectly balanced split path" hypothesis is **false** already at `n=6` (it fails where `G(6)=S(6)=10`), so it is not a valid disproof route.
- The decisive candidate is `n=12` (`G(12)∈{29,30}`). General DFS (99 s at `n=9`) and beam search blew up before reaching `n=12`; I did **not** resolve it. No theorem, no `S(n)` value, no class separation claimed.

## New fronts (2, both absent from all 587 ledger IDs and the previous list)
- `greedy-adversary-sufficiency-alln` — the value-equality question above.
- `greedy-frontier-state-growth-alln` — whether the greedy-reachable state set is polynomially bounded (a distinct question about whether the restriction evades the enumeration barrier).

Wrote **only** the JSON object to `/home/lubko/soring-fronts/curator/frontier-candidates.json`; schema, field lengths, slug format and non-duplication all validated.
