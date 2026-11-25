# antonina-iXu1TSlX91S3E69xXlSFxn-grants

Session: ses_df4a4c450ffePQPi0Eswk5lOkW
Workspace: /home/lubko/soring-fronts/surplus-linear-dichotomy-alln
Created: 1795486858340; updated: 1795487415986

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 15 (msg_20b5d7cf0001MABI69HESV5vQ4)

Let me start by checking the environment and branch state.

## Output 30 (msg_20b5d850b001eS2XLvi5wvFEjL)

I'm on `billy-dev`. Let me read the key documents and find the board.

## Output 49 (msg_20b5d8f380016ChLzvFy3lKnHg)

Now let me find the board mechanism and read the research plan and operations docs.

## Output 64 (msg_20b5d9896001OCJoXeEFI5Oi8i)

I'm on `billy-dev` ✓, board is Antonina issue #301 with a digest tool. Note `research-plan.md` already mentions "Sergeev: `S(n) − log₂ n! = O(n/(log n)^{1/5})`" — sublinear — which directly interacts with the claim. Let me check the board and the relevant research docs.

## Output 87 (msg_20b5e6960001aIc0BNVZVNmxlx)

The project's own literature already states Sergeev `S(n) = log₂ n! + O(n/(log n)^{1/5})` — sublinear. The user's claim of Ω(n) linear excess sits in tension with that. Let me fetch Sergeev's actual paper and read the winning-frontier barrier doc, then verify.

## Output 102 (msg_20b5eaeb8001Eo7mGhiVIKvjTF)

The repo itself cites Sergeev **Theorem 3** (ECCC TR20-096): `S(n) = log₂ n! + O(n/(log n)^{1/5})` — sublinear surplus. The user's claim of Ω(n) would be refuted by that. I need to verify the paper argument. Let me hunt for the paper locally or fetch it.

## Output 121 (msg_20b5f21a8001wPLjfAd4TfdBhr)

The ECCC page loads. Abstract says: "This number is shown to be log₂(n!) + o(n)... improved over previously known upper bounds of the form log₂(n!) + Θ(n)". Now I need the actual PDF to read Theorem 3 and the group-insertion construction.

## Output 136 (msg_20b5f6285001DXm11x7h1bVLGL)

Got the PDF (31 pages). Let me extract its text to read Theorem 3 and the group-insertion algorithm.

## Output 151 (msg_20b5f94ce001aAHbXwL7CuH9jc)

We have `pypdf` and `fitz`. Let me extract the paper text with pypdf (saved to a file for reading).

## Output 162 (msg_20b5fbd8f0011ow8EmxyG939De)

The paper is extracted. Now let me find the theorem statements — especially Theorem 3 (p. 29 per the repo doc) and the group-insertion algorithm.

## Output 173 (msg_20b5ff60a001vMqEFMLilNl5MG)

Found it — **Theorem 1. S(n) ≤ log(n!) + 0.09n + o(n)** (line 786) and **Theorem 3 (line 1701)**. The user's "0.09n" matches Theorem 1; the tighter sublinear bound is Theorem 3. Let me read these sections and the group-insertion method.

## Output 188 (msg_20b605c84001Fp3WEdnVSDsaK0)

Theorem 1 matches the user's prompt. Now let me read **Theorem 3** (line 1701) and the group-insertion method description (§7, around line 1732+).

## Output 199 (msg_20b60715f001iaNuVTd2lSrIDt)

I have Sergeev's **Theorem 3**: `S(n) = log(n!) + O(n log^{-1/5} n)` — sublinear surplus, proven via the group-insertion algorithm (§7): pair-sorting + principal chain + group insertion via Corollary 2/gradient strategy, yielding the recurrence `s(n) ≤ s(n/2) + O(n log^{-1/5} n)`. This directly refutes the user's Ω(n) claim. Let me check the frontier ledger (bound-gap front) and the board tooling for reporting.

## Output 214 (msg_20b61851e001Yo2sGm2yrWm073)

I have everything needed for the mathematical assessment. Let me (a) compute the small-n surplus table (experimental consistency check) and (b) check how to post to board #301 per the repo contract.

## Output 229 (msg_20b624400001BRX6Wah2CuvzrX)

Let me check the board `comment` syntax so I can post the concise report per the repo contract (AGENTS.md: findings go to board #301).

## Output 240 (msg_20b626e50001SyDSdXLUCl8DIe)

Now I'll post the concise finding to board #301 (repo contract: report to the board), then verify.

## Output 251 (msg_20b62c677001WczbxxyTyVuWb0)

Let me verify the board post landed.

## Output 262 (msg_20b6355fe001weCM8dUaKtyOtw)

## Finding: the Ω(n) claim is **refuted** — the surplus is sublinear

**Result: `S(n) − ceil(log₂ n!) = O(n / log^{1/5} n) = o(n)`** — the excess of the exact sorting number over the information bound grows sublinearly, so there is no linear regime. The claim "surplus = Ω(n)" is false (assuming Sergeev's theorem, see limits below).

### The falsifier: Sergeev's group-insertion trees

Sergeev, *On the asymptotic complexity of sorting*, ECCC TR20-096 (2020), **Theorem 3** (p.29):

`S(n) = log₂(n!) + O(n log^{−1/5} n)`.

This is proven by an explicit sorting-algorithm family — the "group insertion" algorithm — whose trees are correct trees of height ≤ `log₂ n! + O(n log^{−1/5} n)`. Hence the surplus `S(n) − ceil(log₂ n!) ≤ O(n log^{−1/5} n) = o(n)` — exactly the requested exhibit (infinite family of correct trees with surplus o(n)), and it refutes the Ω(n) claim. Paper audit of the falsifier (§7): pair-sort `n/2 + S(n/2)`; insert `n/log n` α-elements via Ford–Johnson; insert the rest in groups of ≈`√n/log n` via the Corollary-2 gradient strategy (per-element excess `O(log^{−1/5} n)`); recurrence `s(n) ≤ s(n/2) + O(n log^{−1/5} n)` ⇒ `s(n) = O(n log^{−1/5} n)`.

### Note on the prompt's quoted "0.09n"

That is paper **Theorem 1** (p.16): `S(n) ≤ log₂(n!) + 0.09n + o(n)` — an *upper bound* on the excess in linear form; consistent with Ω(n) but not a refutation. The abstract of the paper states `log₂(n!) + o(n)`, and Theorem 3 gives the tighter sublinear bound. The repo's literature assessment (`research-plan.md`: "Sergeev — `S(n) − log₂ n! = O(n/(log n)^{1/5})`") agrees; the exact obstacle to a Ω(n) line of attack is Sergeev's bound itself.

### Honest limits

- The refutation stands on Sergeev's paper argument; I audited the theorem statement and the recurrence structure, but not every lemma (§4–§7, e.g. Corollary 2). The repo marks it "Primary theorem, not Lean-checked here."
- No new trees or experiments by me; small-n data consistent: surplus ≤ 1 through n=18 (S(12)=30 vs C=29; S(13)=33 vs 33; S(16)=46 vs 45; S(17)=50 vs 49; S(18)=54 vs 53).
- Certificate **soundness vs completeness**: Sergeev is a soundness statement (upper bounds on tree heights). Completeness (NP/coNP/PSPACE certificates of SORT-BOUND-U) is separate; the general-poset fronts on #301 (cospectral, ordinal-lift, reachable-profile) don't transfer — they concern arbitrary posets, not the antichain root of S(n). The winning-frontier barrier is about enumerating winning states, orthogonal to surplus.
- Per your instruction, no Lean/repo changes were made (clean worktree; scratch only in /tmp/opencode). A concise update is posted to board #301.

### Complexity implication (per your framing)

Since the surplus is `o(n)`, the exact value tracks the information bound to sublinear waste; envelope/excess-based lower-bound routes aimed at a linear excess are out of line with the current upper bound (any lower-bound front would have to be of order `O(n log^{−1/5} n)` or smaller to remain consistent).
