# antonina-w1AI5wddb1K5G5jcIAhyqe-darker

Session: ses_e3be6f3c9ffeRZC23d96FHYzXA
Workspace: /home/lubko/soring-fronts/curator
Created: 1794291338367; updated: 1794294227964

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 234 (msg_1c4212a2f001wPpg50XGXwxZ8a)

I have a good picture of the ledger and board. Let me now attack a precise claim from the newest board's explicit "next question" — the Sidon circulant balanced-pair question — with an independent computation.

## Output 489 (msg_1c43c8910001GxVw5R7k30HL5B)

The three candidate questions are confirmed non-duplicate against the 492-entry ledger. Let me write the deliverable JSON now, then continue monitoring the independent computations.

## Output 603 (msg_1c444d66f001VV76wBO6iQ4TfF)

Done. The deliverable is written to `/home/lubko/soring-fronts/curator/frontier-candidates.json` (3 fronts, keeper-schema-valid, confirmed non-duplicate against all 492 ledger fingerprints). No repository, Lean, or board changes; worktree clean at `6a96398`.

## Curator fronts proposed

1. **`good-comparison-cover-destruction-lemma`** — the GC lemma explicitly named as the next question in board #301 02:20Z (`upper-inequality-structural` §6). Precise all-`n` falsifier: a non-total poset where every incomparable pair has an orientation that creates a cover without lowering ψ and has extension probability ≥ 2^(−1−C).
2. **`sidon-circulant-balanced-pair-nonvanishing`** — the exact next question in 02:07Z (`abc-witness-decidability-alln` §6): does the Sidon circulant `D={0,1,3}` have `e(P+xy) ≠ e(P+yx)` for every ordered pair at every prime `q ≥ 11`?
3. **`upper-inequality-height-two-restriction`** — the (U) inequality restricted to height-two posets, including the one-comparison state `Q_n = C₂ ⊔ A_{n−2}` with `F(Q_n)=S(n)−1`.

## Attack and honest limits

- **(U) inequality (general posets).** Independent exact check over **all 2,045 unlabeled posets at n=7 and all 16,999 at n=8** (exact `e`, exact `F`, exact covers/m/M, exact integer form `15^D·2^{8F} ≤ e^8·2^{5D}`): **0 counterexamples**. The claim survives; this is evidence, not a proof.
- **Sidon circulant balanced pairs.** Independent exact computation reproduces the board's `e(P₁₁)=16,174,936,626,710,400` and finds **no balanced pair at q=11 or q=13** (all min–max, min–min, max–max residue classes). The q=17 run was started but stopped under heavy host load (2.8M order ideals, ~2.8 GB RSS); **q≥17 is untested**. The claim is not disproven.
- **Distinction enforced.** These are general-poset and certificate-completeness statements. They do **not** change `S(n)` bounds: (U) at the antichain gives `E(n) ≤ 0.273n`, weaker than Sergeev's `O(n/(log n)^{1/5})`; A/B/C are sound for GPC, not for `S(n) ≤ k` (the ledger's `abc-certificate-checking-complexity` finding). The implications in the JSON state this explicitly.

No defensible new direction was omitted; the remaining newest-board items (starvation propagation, single-deletion η, fan-family excess) are already `running` ledger fronts and were refused as duplicates.
