# antonina-fZpa05euKG4mrgIKVHGPON-acorn

Session: ses_e0b0f2a8affesdpc8GiDwwr5kY
Workspace: /home/lubko/soring-fronts/all-minimax-promise-verification-np
Created: 1795110786450; updated: 1795111182557

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f4f0da27001D0wDqC8XWICFy4)

I'll start by understanding the environment, the repository state, and the key documents referenced.

## Output 17 (msg_1f4f0e389001fvlrn364BC40x3)

I'm on `billy-dev` as required. Let me explore the documentation structure and read the key files in parallel.

## Output 36 (msg_1f4f0ee2e0015Kd1pWwOPW9MMW)

Now let me get the board digest and find the referenced research documents.

## Output 51 (msg_1f4f0fc76001RUZxxILktJ409G)

Let me read the key certificate strategy documents and search the board for the specific referenced posts.

## Output 66 (msg_1f4f11355001DBHXmnxJDhE2Cw)

Let me search the board for the all-minimax completeness theorem and the sorter-refuter B1/B2 details.

## Output 81 (msg_1f4f12dc5001gxNarg6Ue8yMI3)

The digest truncates posts. Let me check the script and Antonina tooling to read full comment bodies.

## Output 96 (msg_1f4f13d32001u5SHRmmjosuQY2)

Let me write a helper to extract full bodies of specific board posts without flooding context.

## Output 114 (msg_1f4f1a06f001hvIA6vGdWCxt58)

This is a rich board. Let me read the full text of the most relevant posts: the all-minimax completeness theorem and the sorter-refuter duality (B1/B2).

## Output 125 (msg_1f4f1bbca001gb4EU79zps365h)

Let me read the related posts on reachable-state lower bounds and program-vs-DAG size to avoid rediscovering known results.

## Output 136 (msg_1f4f20ae8001S2kktpfbZsJwiA)

This board is very advanced. Let me check the primary literature on the complexity of evaluating the minimax value for a poset and verification hardness, which is central to my front.

## Output 160 (msg_1f4f2fbd9001vNWckNhaoB1oji)

Web tools seem unavailable. Let me check the repository's own hardness-boundaries note, which likely records the general-poset results precisely.

## Output 171 (msg_1f4f31df1001e7EUIRoTTJ84W3)

Let me read several more closely related posts about class-stable optimal strategies and program-vs-DAG size, to pin down the exact open frontier.

## Output 182 (msg_1f4f36db4001ZokumHXdqGWege)

Let me verify the interpreter model (whether redundant comparisons are allowed) by reading the checker script.

## Output 193 (msg_1f4f4a0080019suWE1NkbuTB0J)

The checker confirms redundant (padding) comparisons are allowed — the "wrong" outcome branch is simply skipped. Let me check my front's ledger entry and how to post to the board.

## Output 204 (msg_1f4f4cfeb001ofXmK01HUtH9v4)

I now have a clear picture. Let me validate the key technical step — that redundant comparisons are legal and consume budget in the repo's exact checker grammar — with a small scratch check (scratch only under `/tmp/opencode`).

## Output 215 (msg_1f4f54a43001weCsUPryRv9z6Q)

Redundant comparisons are confirmed chargeable. Let me check the board posting command syntax before writing my report.

## Output 226 (msg_1f4f577d3001U5q5peUHjcLIuE)

I have a rigorous result. Let me write the report to a scratch file and post it to board #301 (the required venue), keeping all work outside the repository.

## Output 244 (msg_1f4f61141001sfAYHRbu67P0AE)

Let me verify the comment posted correctly.

## Output 255 (msg_1f4f62593001EnMM0grZb3kolE)

The report is posted. Final side-effect audit:

## Output 266 (msg_1f4f636c2001BmGl1pWFl1T1uL)

Done. Work on `billy-dev` only; repository untouched (`git status` clean at `6a96398`), scratch confined to `/tmp/opencode`, findings posted once to board #301 (17:58Z).

## Mathematical finding

I attacked the front's falsifiable dichotomy and resolved the "coNP-hard verification" branch:

**Lemma 1 (deduction).** If a strategy plays a locally minimax-optimal comparison at *every* reached state `P` (i.e. `F(P)=1+max(F(children))`), then its subtree height from `P` is exactly `F(P)` — induction on `F(P)`, since both children have value `≤F(P)−1`. From the antichain the height is `F(∅)=S(n)`. So **every** all-minimax strategy is a correct height-`S(n)` sorter (strengthening Alex's existence theorem), and for fixed `(n,k)` the answer to "height ≤ k?" is the *same* for all of them: `[S(n) ≤ k]`.

**Theorem 2 (deduction + Fortune 1979).** Consequently the promise problem "given a poly-size all-minimax strategy, is its height ≤ k?" many-one reduces (on promised instances, via `(desc,k) ↦ 1^n#1^k`) to `SORT-BOUND-U`. Since that language is sparse and sparse sets are not many-one coNP-hard unless P=NP, **succinct height verification under the all-minimax promise is not coNP-hard unless P=NP**. The promise collapses verification to the original threshold problem — it cannot stay coNP-hard.

**Theorem 3 (contrast).** *Without* the promise, `VERIFY-PROG = {(P,k): a strategy sorts every permutation within k}` is coNP-complete: in coNP via a single failing-permutation witness; coNP-hard by a TAUTOLOGY reduction that extracts free bits from disjoint comparisons and pads false branches with redundant comparisons. I confirmed with the repo's own `check_framed_strategy.py` that such padding is legal and chargeable (budget 1 REJECT / budget 2 ACCEPT depth 2). All-minimax strategies exclude precisely this padding, which is why the hardness does not transfer — consistent with Theorem 2.

## Implication for the front

All-minimax completeness gives a **complete** certificate family but its canonical object is the explicit `2n!−1 = 2^{Θ(N)}` tree — exponential in the unary length `N`; explicit formats are dead (B1). **Verification complexity is not the obstacle**; the only surviving route is compact (quotient/program/framed) completeness, which remains open. The falsifier's second disjunct is provable for explicit formats (B1) but open for succinct ones, where an unconditional size bound is blocked by the same Mahaney/Fortune barriers.

## Honest limits

I could not disprove the positive NP-membership claim: that needs `SORT-BOUND-U ∉ NP`, which with PSPACE membership would give `NP ≠ PSPACE` (open) and is unreachable for a tally language in `P/poly`. No new value of `S(n)`, no class separation, no faster evaluator. Theorems 2–3 are about verification languages/certificate formats — not hardness of `S(n)` or `SORT-BOUND-U`; soundness ≠ completeness throughout. No Lean or repository changes were warranted.

## Output 295 (msg_1f4f6a273001MsQyYdkhGuOfN3)

**Recovery inspection (no actions repeated):**

- **Host/repo:** `billy-dev`, `/home/lubko/soring-fronts/all-minimax-promise-verification-np`. Git clean (`## billy-dev...origin/billy-dev`, HEAD `6a96398d937d20977a91b9afa8619cb27feab269`, no working-tree changes, no new commits). No repository/Lean/test/workflow/ledger changes detected.
- **Board side effect (external, already happened):** exactly **1** matching comment found on #301 — `[2026-11-19T17:58:45.834Z] SoringP1 frontier: all-minimax-promise-verification-np` (confirmed via `board_digest.py --contains "all-minimax-promise-verification-np"`). **Not reposted.**
- **Local posting evidence (scratch, `/tmp/opencode/`):** `allminimax_report.txt` (6343 bytes, 17:58), `chk.py` (6038 bytes, 17:57), `post_result.json` (5,234,091 bytes, 17:58) with JSON content beginning `{"body":...`, and `post_err.txt` empty — consistent with a successful `antonina board comment` run.
- **Uncertain:** I did not independently fetch the full comment body back from Antonina; the digest excerpt and local `allminimax_report.txt`/post artifacts match the intended report, but if exact server-stored text must be audited, review the comment at 17:58:45.834Z on #301.

**Status:** previous task completed (analysis + single board report delivered). No unfinished work continued, no posts/commits/other external actions duplicated.
