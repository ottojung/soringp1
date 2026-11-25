# antonina-qIbzQ8lejXLJvElPfWnuSV-sportsman

Session: ses_df4828485ffezP63EKr9Js1GH7
Workspace: /home/lubko/soring-fronts/tight-surplus-sound-certificates-alln
Created: 1795489103170; updated: 1795489914259

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_20b7d860f001x9nnotyYK1t7sz)

I'll start by studying the repository: the contract, problem doc, operations doc (board #301), and the certificates/barriers literature.

## Output 29 (msg_20b7db676001kQql6V0LD7UzVf)

Now let me study the research board (#301) via the digest tool and check the frontier ledger:

## Output 44 (msg_20b7dcda3001nSDagivVjRPQbo)

I'm now studying board #301's relevant posts and the framed-certificate checker. Let me gather the evidence.

## Output 59 (msg_20b7e97a4001Lc69l9NL8TgCW2)

I'm on billy-dev. The digest tool only reads page 1 by default; let me search more of the board and read the framed-certificate checker.

## Output 74 (msg_20b7ea70c001ygz21gsTQf36Ia)

Let me read the board digest tool and the framed-certificate checker/probe scripts.

## Output 89 (msg_20b7eb7cb00171CTnHLgLmmVQa)

I'm on billy-dev as required. Now let me read the remaining relevant docs and probes, and find the two board posts the EVIDENCE mentions.

## Output 104 (msg_20b7faa3b001ITZxvFNk1Qtg1b)

Now let me read the strategy-certificates doc, the strategy DAG probe, the research plan, and check the frontier ledger.

## Output 123 (msg_20b7fb8a30017JllpI2qDrY6PG)

Now let me compute the information bounds L(n) and find known S(n) values through n=22 in the repo data/docs.

## Output 138 (msg_20b808dd20014A5Kmn4Aj4eao7)

L(22)=70, and board data says S(22)=71 → surplus +1. Let me find the S(n) table through n=22 (known values).

## Output 153 (msg_20b80a0f0001TefhDiEzzQOimU)

Let me read the research plan, literature, and the surplus/structural-lower-bound docs.

## Output 168 (msg_20b80b263001Bf3G7IE4CiH552)

Let me find remaining S(n) values through 22 and read the structural-lower-bounds and time-exponent notes.

## Output 183 (msg_20b80cd1e0019EFUib6qh5QHyJ)

Let me read the time-exponent, one-ply obstruction, and literature docs, and do broader board searches for the two named posts.

## Output 202 (msg_20b8171a1001rx2ZQnkPheQNUy)

I now have a good picture of the research landscape. Let me check the working tree state (recovery audit) and build the surplus-data experiment.

## Output 217 (msg_20b823080001coyBOyvtq4kMJc)

Worktree clean on billy-dev. Let me find the board posts for the data-check and the excess-two soundness post to complete the evidence base.

## Output 228 (msg_20b8288d0001RQoRdP0yXkTANO)

Let me read the Sergeev asymptotic note and literature.md (they discuss Fredman and the surplus/envelope).

## Output 243 (msg_20b82b39e001Lwz5FwthFHYFVf)

Now let me run the experiments. First: a fresh minimax computation of S(n) for n ≤ 9 (independent re-derivation, scratch in /tmp/opencode).

## Output 396 (msg_20b89d08f0017wcSVQFQZm724P)

# Mathematical finding: near-tight sound certificate family (NT) — status

## Claim attacked (precise, all-n, falsifiable)

**NT:** ∃C ≥ 0 such that ∀n ≥ 1 there exists a *sound framed comparison certificate* (grammar of `scripts/check_framed_strategy.py`, root at the antichain) sorting n distinct labelled keys, with depth ≤ ⌈log₂(n!)⌉ + C.

## Deduction: NT ⇔ surplus bounded

[d eduction] A sound framed certificate of depth k implies a correct sorting tree of height ≤ k (follow the path consistent with each real input order; acyclic forward edges; permutations are bookkeeping), so S(n) ≤ k. Conversely, an optimal tree of height S(n) yields a sound framed certificate of depth S(n) (standard construction; cf. `research-framed-certificate-frontier.md` §2). Hence NT holds iff ∃C: S(n) ≤ ⌈log₂(n!)⌉ + C ∀n, i.e. the surplus s(n) = S(n) − ⌈log₂(n!)⌉ is bounded. The certificate question therefore reduces to boundedness of the surplus.

## Data (through n = 22)

[experiment] Fresh minimax DP (`/tmp/opencode/minimax_s.py`) independently re-derives S(n) = L(n) + 0 for n ≤ 6, with reachable-state counts 1, 3, 19, 219, 4231, 130023 = A001035. Board `envelope-front-data-check-20261124`: surplus ∈ {0,+1} for all n ≤ 22 (e.g. S(20)=62=L(20), S(22)=71=L(22)+1). **NT is not refuted by any data through n = 22.**

## Falsification attempts

- **F1 (soundness obstruction):** no explicit n found where every sound certificate of depth L(n)+1 is super-polynomial in n. For n with S(n)=L+1 (12, 13, 15–19, 22), depth-L+1 certificates exist as trees; poly-size framed DAG existence is the open `framed-dag-n12-exact-optimum` front (inconclusive even at a 10000-node threshold for n=12).
- **F2 (poly-size family):** not constructed. The merge-sort O(n²)-node DAG has height n log n − n + 1, not exact S(n); rank-envelope insertion is unverified through recursion.
- **Computational:** `strategy_dag_probe` through n=5: DAG(all) = 1, 3, 19, 181, 1551; quotient = 1, 2, 5, 12, 19; log₂(nodes)/n increasing — consistent with super-polynomial growth but n too small. OPT(n) (= quotient(all)) = 1, 2, 5, 12, 19 for n ≤ 5. Checker sanity: `check_framed_strategy.py` accepts a sound certificate of depth 1 for n=2 and rejects depth 0 (depth exceeds budget).
- **Soundness vs completeness distinguished:** soundness (this target) implies S(n) ≤ k; completeness (poly-size existence) remains OPEN. General-poset results (cospectral, ordinal sums) do not transfer to the antichain root (board #301 referee dispositions).

## Honest limits

- **No new theorem or counterexample obtained.** NT remains open and data-consistent through n = 22.
- **No Lean or repository changes made** (publication gate unmet).
- Refuting NT requires unbounded surplus. The running `surplus-lower-bound-omega-alln` front claims Ω(n/(log n)^(1/5)) surplus for large n, which if proved would refute NT, but it is itself open and the board data check states the disproof path is obstructed at moderate n.
- Proving NT requires a poly-size tight certificate family; none is known.

A concise update was posted to board #301 (comment `sha256:2BEmaRd7RscO2GeE7l6_IVNMBqUu6DOtUsiQhO-uUE8`, 2026-11-24T03:11:42Z). Worktree remains clean at `6a96398`.
