# antonina-0BFPxdff8VSG4laxaXSPWS-doll

Session: ses_dff29bcdcffe4GEvJm3l4naFnI
Workspace: /home/lubko/soring-fronts/curator
Created: 1795310371621; updated: 1795310875244

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_200d64343001pxkscr8C3XOvdK)

I'll start by studying the repository docs and locating board #301.

## Output 29 (msg_200d6ee3b001eC3RoqsYusJKue)

Now let me check the host, read board #301 via the digest tool, and study the literature and current frontier ledger.

## Output 56 (msg_200d72ce2001IMtjhAgLCSLsHi)

I'm on `billy-dev`. Let me get a fuller current view of board #301, the rest of the ledger, and the existing front directories.

## Output 75 (msg_200d76209001rakSRrnJ9sY0Vd)

Now let me get the full ledger ID list (to avoid duplicates), read the remaining ledger, and see what evaluation tooling exists.

## Output 103 (msg_200da56e80011btv9WJ4aShSpU)

The ledger is extremely dense. Let me check the tail (the very newest fronts), and inspect the text of a few ledger entries I want to be sure are distinct from (or duplicates of) my proposed questions.

## Output 139 (msg_200dc937b001Qq3788IOBWSqfF)

Now I have the full picture: 672 existing fronts in the ledger. I have an attack result (mostly inconclusive), so let me finalize genuinely new, non-duplicate proposals and verify their required length bounds before writing the JSON.

## Output 159 (msg_200ddd0a9001WFiMH5hgKtH5iE)

Study, attack, and proposal complete. Deliverable written to `/home/lubko/soring-fronts/curator/frontier-candidates.json` (valid JSON; schema lengths verified; no ids duplicate any of the 672 ledger entries or the user's previous fronts).

**Study.** On `billy-dev` I read `docs/problem.md`, `docs/literations` (literature baseline), the digest of Antonina issue #301, and the full frontier ledger. Key recent ground: the Nov-22 refutations (`framed-certificate-total-forgetting-loss-linear-alln`, `run-decomposition-selective-summary-size-alln`), `space-reduction-budgeted-dfs`, and the Nov-29 entry `sort-bound-u-pspace-complete` (sparse ⇒ not PSPACE-hard many-one; Turing hardness open).

**Attack (disproof attempt).** Attacked the claim “Δ(n) ≤ 1 for all n” (negation of the ledger’s `excess-at-most-one-alln`): computed exact `ceil(log2(n!))` in `/tmp/opencode/attack_excess.py`. Known data: Δ=0 for n≤11, +1 at n=12; board says Δ=0 at n=20,21, +1 at n=22; S(28) ≥ 99 with `ceil(log2 28!) = 98` so Δ(28) ≥ 1 — no counterexample found, claim not refuted. Honest limits: no refuted claim; attack on “Δ(n)=0 at some n≥23” requires computing S(23…28), outside current reach.

**Proposed new fronts** (new, falsifiable, all-n):
1. `poly-reachable-exact-height-gap-alln` — is the minimal height among *polynomial-reachable* trees equal to S(n)?
2. `tightness-density-zero-alln` — is the tight-information set {n : S(n)=⌈log₂n!⌉} of asymptotic density 0?
3. `winning-frontier-peak-at-exact-budget-alln` — does the winning frontier (winning count per depth) always peak at t = S(n)?

No Lean/repo changes; no claims of proof or verification — these are proposals awaiting independent research.
