# antonina-UrYqi07hSJBUp3EXsf7Okx-swelling

Session: ses_e3d69224effe8YPARiuzzM1vyM
Workspace: /home/lubko/soring-fronts/recursive-certificate-disjoint-union-closure
Created: 1794266029709; updated: 1794271378926

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 683 (msg_1c2e7c597001jg6Xs2DSvwxq4v)

The 3+4 strict union run was OOM-killed again (`u34_strict.txt` is empty), and the concurrent `solve33` batch is still holding ~7 GB, so no further n=7 exhaustive work is feasible right now. This matches the intended fallback: document the limit honestly and post exactly one report. Board check confirms no post exists under this front's author name, so there is no duplication risk.

## Output 712 (msg_1c2e85f29001PGURG4ovEc8p99)

The single report is posted and verified (exactly one comment, timestamp `2026-11-10T00:42:36Z`, author `SoringP1 frontier: recursive-certificate-disjoint-union-closure` — no pre-existing post under that name existed, so no duplication).

**Summary of this recovery turn:**

- **State check:** worktree clean at `6a96398` on `billy-dev`, no repo/Lean changes were ever made; the only durable artifacts are scratch files under `/tmp/opencode/reccert`. Confirmed the 3+4 strict trio batch (`u34_strict.txt`) was OOM-killed empty again, and `solve33` is still holding ~7 GB — so n=7 exhaustive coverage stays out of reach this turn.
- What survived and stands as the finding:
  - **All 318 unlabeled n=6 posets and all 87 n≤5:** optimistic `G_ABC = F` and strict `G_STRICT = F` everywhere.
  - **All 286 disjoint unions with |A|,|B|≤5 (|A|+|B|≤6):** no counterexample to recursive certificate closure under either reading; 187 items are A/B certificate-starved and none stay starved once balanced triples are admitted — C is load-bearing exactly where needed (e.g. C₆⊔C₃, cross-pair split 84/84).
  - **Two-chain merges through n=10:** `G_ABC = F` throughout, including C₅⊔C₅ (e=252) where A/B-only fails at the root.
  - A 38-poset n=7 extension batch completed clean; the rest of n=7 is documented as an honest memory limit.
- **The obstruction made precise in the report:** "C" is a node-level condition (Peczarski spends two comparisons there), so "a move meets C" is undefined in the literature; the strict all-n claim is falsifiable only after that two-comparison semantics is fixed from Lemma 2's proof. Plus the recursion-layer gap: no composition from summand certificates to union certificates, and any counterexample can only live where A⊔B's root move is certified while a certificate-starved summand is still F-optimal — precisely the shape the solver targets.
- **Status:** front reported as **inconclusive — failed-approach/obstruction report**, explicitly not a proof; no commits, PRs, or Lean files, per the publication gate.
