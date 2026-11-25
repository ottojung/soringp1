# antonina-pCzohAehAmmPI0TDh1tQDv-carcinoma

Session: ses_e47b8f00affeNzuNzH7oBqcLkC
Workspace: /home/lubko/soring-fronts/exec-core33-independent-gen-20261107
Created: 1794093027376; updated: 1794094173658

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b847120f001wvaGvlEsjrAmuj)

I'll start by examining the comparison target and understanding the project's setup.

## Output 57 (msg_1b847621e001SF0iKopKhIwiAs)

Let me inspect the target generator's output structure and determine the level sizes, then design the dual enumeration.

## Output 77 (msg_1b849cc0f001D3IPhiNXgvCvYS)

The target's level data is clear: cores exist at every size up to E (chain-plus-isolated families), so canonicalization must handle n up to 54. I'll now write my own dual generator with independent canonicalization.

## Output 133 (msg_1b84c1983001V0vLxnXyr6aXxD)

Counts match at every level for E=12, 20, 33, and 54. Now I'll do the actual set comparison against the candidate generator.

## Output 151 (msg_1b84c6de3001EZP2EDsSFxO0cv)

Now the exhaustive full-poset census for n ≤ 8. I'll build all unlabeled posets with an independent maximal-insertion census (validated against the known unlabeled-poset counts) and filter cores.

## Output 171 (msg_1b84d0c87001ufDcx002aRy8Iz)

I made an error in the census: I passed ideals to the minimal-insertion helper, which is only valid for filters. I'll fix the census to use the standard maximal-insertion primitive and rerun.

## Output 207 (msg_1b84d8a68001bI6LGXMhDmbeCC)

The pruned census now agrees exactly. Now I'll run the full (unpruned) census through n=8 to validate the census machinery against the known unlabeled-poset counts.

## Output 218 (msg_1b84df85e001ez98ubBfQ2MFNu)

The full census matches all known unlabeled-poset counts, and both core sets agree with it for n≤8. Now I'll validate the canonical form independently and verify set equality with an exact isomorphism test (not relying on canonical keys).

## Output 238 (msg_1b84fe0620011eW3ydRWsdBgAF)

The canonical refinement is invariant (0 mismatches under relabelling) and the exact isomorphism check passes for all 1,053 E=33 classes. I'll also compare the full E=54 sets, not just counts.

## Output 276 (msg_1b85285cd001vy5qUvfdFNk5nX)

Since a missing core at n=9 would be the highest-value finding, I'll also run the independent e≤33 full-poset census through n=9 and compare.

## Output 305 (msg_1b854aac5001beCEtSmxrB73Pk)

Now I'll record exact memory measurements and script hashes for the final report.

## Output 316 (msg_1b857528f001ycu4tnM1ATO4bj)

## Independent dual cross-check — SoringP1 #301

No repository, Lean, or board files were touched. All work is under `/tmp/opencode`; `core_only.py` was imported only as the comparison target.

### 1. Dual recursion and completeness

Let \(P^d\) be order reversal. Comparability is preserved, so \(P\) is a core iff \(P^d\) is; \((A(+)B)^d=B^d(+)A^d\); maximal elements of \(P\) are minimal in \(P^d\); and \(e(P)=e(P^d)\). The primal lemma (“every ordinal-indecomposable core \(P\), \(|P|\ge2\), has a maximal \(x\) with \(P-x\) a core”) dualises exactly: apply it to \(P^d\), get a maximal \(y\) with \(P^d-y\) core; the corresponding \(x\) is minimal in \(P\), and \((P-x)^d=P^d-y\), so \(P-x\) is a core. The elements above \(x\) form a proper filter \(F\) of \(P-x\) (if \(F=P-x\), then \(P=\{x\}(+)(P-x)\) is decomposable), so \(P\) is obtained by (i′). Thus the lemma transfers by duality.

Where it does **not** transfer: the primal implementation inserts above **proper ideals**; the dual must insert below **proper filters**, and the filter must be represented as such. In particular the empty filter must be allowed, matching the primal’s empty ideal; omitting it loses \(A_3\) and the chain-plus-isolated families. Also the lemma itself is an input assumption, not proved by this check: if it were false, primal and dual could fail in a dual-symmetric way.

### 2. Counts by \(n\) and totals

All runs start from the 2-antichain, use dual insertions and ordinal sums, prune \(e>E\), and dedupe with my own canonical form (brute force over \(n!\) for \(n\le6\); independent colour-refinement/individualisation for larger \(n\)).

| \(E\) | counts for \(n=2,3,\ldots\) | total |
|---|---|---|
| 12 | 1, 2, 7, 15, 21, 10, 3, 1, 1, 1, 1 | **63** |
| 20 | 1, 2, 7, 27, 54, 63, 44, 23, 13, 5, 3, 1, 1, 1, 1, 1, 1, 1, 1 | **250** |
| 33 | 1, 2, 8, 31, 106, 201, 244, 172, 99, 52, 32, 24, 19, 18, 19, 5, 5, then 1 for each \(n=19,\ldots,33\) | **1053** |
| 54 | 1, 2, 8, 33, 151, 446, 819, 928, 763, 469, 297, 216, 134, 112, 62, 55, 46, 32, 31, 26, 25, 26, 27, 28, 29, 30, 5, 3, then 1 for each \(n=30,\ldots,54\) | **4829** |

The E=12 and E=20 totals match the stated external census values 63 and 250 exactly.

### 3. Set comparison at E=33

The candidate `core_only.enumerate_cores(33)` gives 1,053 classes. My dual set also gives 1,053. Per-\(n\) comparison found:

- only in mine: **0**
- only in candidate: **0**
- shared classes with different \(e\): **0**

An additional exact backtracking isomorphism test on every one of the 1,053 matched pairs—not relying on canonical keys—found **0** problems. Therefore there are no missing or spurious classes and no relation matrices or \(e\)-values to report. As an extra check, the same set comparison at E=54 also gives 4,829 classes with **0** differences; all 4,829 exact-iso pairs pass.

### 4. Exhaustive census checks

I built all unlabeled posets by the independent standard maximal-insertion census. It reproduced the known unlabeled-poset counts for \(n=0,\ldots,8\): 1, 1, 2, 5, 16, 63, 318, 2045, 16999.

Filtering cores with \(e\le33\) for \(n\le8\) gave counts 1, 2, 8, 31, 106, 201, 244 (total 593) for \(n=2,\ldots,8\). My set and the candidate set both agree exactly with this true set: 0 only-true, 0 only-mine, 0 only-candidate, at every \(n\).

As a stronger extra check, the same sound \(e\le33\)-pruned census through \(n=12\) (pruning is valid because adjoining an element cannot decrease \(e\)) gave true core counts 172, 99, 52, 32 at \(n=9,10,11,12\), again with 0 differences between the true set, my set, and the candidate set.

### 5. What this does not establish

- It does **not** prove the primal completeness lemma for all \(n\). Exhaustive census evidence is complete only through \(n=12\) for \(e\le33\) (and full through \(n=8\)); beyond that, set equality with the candidate is evidence, not proof. A counterexample with \(n>12\) could evade this check, and if the lemma failed, the dual recursion would fail in the dual way.
- It says nothing about cores with \(e>54\), or \(E>54\).
- It does not validate the core reduction to \(S(n)\)/minimax values, the binary encoding, or non-core posets.
- It does not certify the project’s canonical form or extension-set code; I used my own canonicalisation and exact isomorphism tests.
- Both generators share the same definition of “core” and the same completeness assumption; a definitional error would not be detected. The census is independent of the core recursion but not of the core predicate.

### 6. Scripts, hashes, timing and memory

Scripts (scratch only):

- `/tmp/opencode/dual_core_enum.py` — `55bc7b154477114553b5d886d14a1711a29f017873836f0a396e00e47115e30d`
- `/tmp/opencode/compare_sets.py` — `773a98450c249042e49174e40880ccd130259889909c74245ba9ccd0d61b1bc2`
- `/tmp/opencode/census_check.py` — `5c032e557c2ff1fd4c58e17040a15ab0db35dd52081b1c257ee527772b1e00c2`
- `/tmp/opencode/validate.py` — `0fa0dac12bca9576daff050aeea4df06ab27887cf9f78c8b9d39fe6ac5f800f5`

Measured wall time / peak RSS on this 4-core machine:

| run | wall | peak RSS |
|---|---:|---:|
| dual E=12 | 0.16 s | 13.6 MB |
| dual E=20 | 0.64 s | 14.0 MB |
| dual E=33 | 3.49 s | 15.4 MB |
| dual E=54 | 30.65 s | 20.7 MB |
| full census \(n\le8\) | 34.0 s | 36.5 MB |
| set compare E=33 | 6.1 s | 36.5 MB |
| set compare E=54 | 39.8 s | 46.6 MB |
| canonical/iso validation | 78.6 s | 46.6 MB |

**Bottom line:** no discrepancy was found. The dual enumeration matches the external census at E=12/20, matches the candidate’s 1,053 classes exactly at E=33, and matches an independent exhaustive census through \(n=8\) (and the \(e\le33\) census through \(n=12\)).
