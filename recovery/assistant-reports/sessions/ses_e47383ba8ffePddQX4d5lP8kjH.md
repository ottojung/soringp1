# antonina-RaxyIDJTGkUX1zRB824At8-occurred

Session: ses_e47383ba8ffePddQX4d5lP8kjH
Workspace: /home/lubko/soring-fronts/shallow-state-fibonacci-hardness
Created: 1794101462105; updated: 1794101924515

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 127 (msg_1b8ceaf38001gdYzrt3vxiDwAL)

## Independent verification report

**Environment:** ran the predecessor's repaired census (`/tmp/opencode/shallow_census.c`) to completion with `/gnu/store/...-gcc-14.3.0/bin/gcc`. Output captured in `/tmp/opencode/census_out.txt` (binary-padded; grep with `-a`).

### Check 1 — Reachability lemma (n ≤ 7, 2045 labeled posets at n=7)

The census performed BFS over comparison-states from the antichain `A_n` with budget `S(n)` and compared the resulting reachable class set (`R*`) against the cover-count condition `|cov(P)| ≤ S` (`R^cover`).

- n=7, S=13: **R^cover = 2045 classes (6,129,859 labeled)**, **R* = 907 classes (3,044,007 labeled)**.

**Result: DISCREPANCY with a naive equivalence.** If the reachability lemma claimed "reachable from A_n within k comparisons ⇔ |cov(P)| ≤ k", then R* should equal R^cover. The census shows R* is a **proper subset** (907 vs 2045 classes). The gap is concentrated in states reachable only via "wasted" comparisons that the BFS prunes unless `F(Q) ≤ b−1`; many cover-feasible posets are not actually reachable in the minimax game tree. Width-≤2 states: 225 vs 214 classes (close but not identical).

This is the kind of precise deviation the collector should flag: the correct reachability condition is stricter than pure cover-count; cover-count is necessary but not sufficient for game-tree reachability.

### Check 2 — Pumping inequality `cov(Q) ≤ S(N)`

The census's EFORM check (n=7, R^cover) found `e(P)·2^c = n!` for only **8** of 2045 classes; for **633** classes `e·2^c < n!` (violations of exact equality), with `floor(e·2^c/n!)` ranging 0–117. The claimed `e(Q)=c·e(P)` scaling was not uniformly witnessed; the EFORM relation fails broadly. Toy-scale reduction demo (P⊕A_2, P⊕V_3) shows ord-sum covers roughly doubles (`c_I ≈ 2c_P`), consistent with pumping only as an inequality, not equality.

### Check 3 — Interval-arithmetic 33 instances

Not independently reproduced in this run (no access to alien's instance file); the census does not contain the 33 end-to-end cases. Flagged as **INCONCLUSIVE** here — would need alien's artifact.

### Summary
- Reachability lemma as stated (iff cover-count): **DISCREPANCY** (R* ⊊ R^cover).
- Pumping equality: **DISCREPANCY** (only 8/2045 exact; 633 strict violations).
- 33-instance end-to-end: **INCONCLUSIVE** (artifact not available).
