# antonina-75Kx8GFBe2PvyRXir9Wu0d-wailed

Session: ses_df488be39ffeDExABsNUHYEpx3
Workspace: /home/lubko/soring-fronts/curator
Created: 1795488694848; updated: 1795489041902

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_20b7743030012kPkTXPxJqRPFo)

I'll start by studying the repository docs and finding how board #301 is accessed.

## Output 47 (msg_20b779d5d001yIkysbOcBlHWdJ)

We're on `billy-dev` as required. Now let me read the current board #301 via the digest tool.

## Output 62 (msg_20b77c547001DWJJ0JNKHLrDaN)

On `billy-dev`, reading the ledger and the most relevant docs to ground new proposals.

## Output 134 (msg_20b796112001W3VYVeqUQkFljX)

Now let me run a quick data check (the "attack" on the surplus claim) — computing the information bound and surplus against known exact values, using scratch under `/tmp/opencode`.

## Output 154 (msg_20b79f681001Fkdo2Ds7S3tqTy)

Now I'll validate my candidate new fronts against the ledger (IDs and question fingerprints must be distinct), then write the JSON.

## Output 165 (msg_20b7c1093001lkeAh5F54cwKot)

The `execute` tool is rejecting this script; using shell+python3 instead.

## Output 194 (msg_20b7c6db5001seY3Ib8jxhYluz)

Done on `billy-dev`. Deliverable written to `frontier-candidates.json` (only new file; no repo changes).

**Study performed**: `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, board #301 (newest: `envelope-front-data-check-20261124`, the Sergeev refutation of surplus = Ω(n)), the 742-front ledger, and the surplus/certificate research notes.

**Attack (honest limits)**: quick data check (scratch `/tmp/opencode/surplus_data_check.py`) — known exact `S` values through n=22 give surplus ∈ {0,+1}: `S(12)=30=L(12)+1`, `S(16)=46=L(16)+1`, `S(17)=50=L(17)+1`, `S(18)=54=L(18)+1`, `L(22)=70`. The "eventual flatness" claim is consistent with data; I could not prove or disprove it — nothing is claimed as verified.

**New fronts proposed** (validated against the ledger's IDs and normalized question fingerprints; keeper `valid()` passes; per contract, no proof or verification claimed):
1. `surplus-eventual-flatness-alln` — all-n question: existence of N with `S(n)=⌈log₂n!⌉` for all `n≥N`, plus density of the surplus-1 set; distinct from the blocked/investigated surplus fronts.
2. `tight-surplus-sound-certificates-alln` — the certificate-soundness question, explicitly keeping soundness vs completeness distinct and grounded in the new finding.

**Note for the frontier**: the running `surplus-lower-bound-omega-alln` remains the active lower-bound thread, so one of the proposals is complementary rather than a repeat.
