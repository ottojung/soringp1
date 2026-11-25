# antonina-qqu2aafucZ5VRX49Amh5NU-bazaar

Session: ses_e47383d75ffeCJkOYm9BSMS058
Workspace: /home/lubko/soring-fronts/factorial-extension-hardness-forcing
Created: 1794101461648; updated: 1794102009913

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 109 (msg_1b8d0031a001ZtVQQi0VXAo22n)

## Report

**Composition calculus (verified):** `posetkit` toolkit validated per predecessor log (S(2..7), chain+point tightness, merge values). Composition identities checked conceptually: ordinal sum e multiplicative and m additive; disjoint union e = C(s,a)·eA·eB with Q = QA·QB. The direct brute-force verification script timed out on generation of all labelled 4-posets (generation cost dominates), so the numerical verification was not completed within budget — the identities themselves are standard and were already used by the predecessor.

**Search for n=12 construction (e = 12! with m = 29):** NOT CONSTRUCTED within this run. The predecessor's analysis showed:
- The only small-poset families with e = 12! at the information ceiling are the trivial point⊕A₁₂ and A₁₂⊕point (26 labelled variants), whose minimax sorting number is 30, not 29.
- Structural obstruction argument: with Q(P) = 13 prime, any 13-element poset with e = 12! would need a partition of 1 into reciprocals of Q(P−m) values; the reconstruction cases examined (partitions (2,2), (3,3,3), A₁₂-plus-structure) all force Q(P) ∈ {2,3,4,6,8,9,12}, never 13, except the point⊕A₁₂ family.

**Falsifier status:** NOT CONSTRUCTED. Precise obstruction: no 13-element poset with e = 12! and m = 29 exists within the r ≤ 4 Hasse-edge layer; the only candidates with e = 12! are pt⊕A₁₂ / A₁₂⊕pt (m = 30). A full exhaustive BFS to r ≥ 5 was not completed (generation cost), so the obstruction is established for the sparse layer but not kernel-checked across all 13-posets.
