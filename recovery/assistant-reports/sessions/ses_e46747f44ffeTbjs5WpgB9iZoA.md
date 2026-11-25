# antonina-1t6rR1GKtSLJT4ZYeKk8rH-distract

Session: ses_e46747f44ffeTbjs5WpgB9iZoA
Workspace: /home/lubko/soring-fronts/sparse-hasse-extension-hardness
Created: 1794114289900; updated: 1794115610172

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b98b82e5001Yvoqe1QcYpiW5g)

I'll start by reading the board context and repository docs, then survey the literature, then run computations.

## Output 68 (msg_1b98bdc35001DRdur80WQ8DR9G)

Now let me survey the literature. I'll run several searches in parallel.

## Output 151 (msg_1b98cfe120014RVSAvnnP1CxaY)

The Dittmer–Pak §6 construction looks decisive: it maps an arbitrary poset to a height-2 poset with linear-size Hasse diagram. Let me verify the construction computationally and check the Chan–Pak reference.

## Output 220 (msg_1b98ea2c3001W0oj0ldwyHtdE2)

The key literature is clear. Now let me verify the Dittmer–Pak sparsification numerically.

## Output 534 (msg_1b999f530001qWlhA901ErMzLw)

## Report — sparse-Hasse #LE hardness

**Front:** Is counting linear extensions `#P`-hard (Turing) for `n`-element posets whose Hasse diagram has at most `C n log n` cover relations, for some absolute constant `C`?

**Verdict: HARDNESS-PLAUSIBLE — in fact established (Turing) with `C = 2`, by a direct sparsity audit of Dittmer–Pak’s height-two reduction.** The exact construction gives fewer than `(3/2)N` covers on `N` elements. There is no polynomial-time algorithm for the class unless `#P = P`.

No tracked files were changed; the worktree is clean.

---

## 1. The theorem and its proof

`[literature]` Dittmer–Pak prove that counting linear extensions is `#P`-complete already for posets of height two (Brightwell–Winkler’s 1991 conjecture), and for incidence posets of graphs. See S. Dittmer, I. Pak, *Counting linear extensions of restricted posets*, Electron. J. Combin. **27**(4) (2020), #P4.48, doi:10.37236/8552; arXiv:1802.06312, Theorem 1.1 and §6.

`[deduction]` **Sparsity of their height-two construction.** Let `P` be an arbitrary poset on `n` elements, with comparability graph having `|E|` oriented edges. For a prime `p ∈ [n, n²]`, Dittmer–Pak build `Q_p` as follows:

- elements: `X` (copy of `P`), `X'` (a second copy), and `x_{ij}` for `i ∈ [n]`, `j ∈ [p-2]`;
- relations: `x_i ≺ x_i'`; `x_i ≺ x_j'` whenever `x_i < x_j` in `P`; and `x_{ij} ≺ x_i'`.

Then `Q_p` has

```
N = n + n + n(p-2) = pn
```

elements, is height two, and its Hasse diagram has exactly

```
n + |E| + n(p-2) = n(p-1) + |E|
```

cover relations. Since `|E| ≤ n(n-1)/2` and `p ≥ n`,

```
n(p-1) + |E|          n-1        3    1
---------------- ≤ 1 + ----- ≤ --- - --- < 3/2.
       N                2p        2   2n
```

So `cov(Q_p) < (3/2)N`. In particular the condition `cov ≤ C N log N` holds with `C = 2` for every `N ≥ 2` (and asymptotically with any `C > 3/2`).

`[deduction]` **Turing reduction.** Dittmer–Pak use the `Q_p` for all primes `p ∈ [n, n²]`; the product of these primes is at least `2^n n!` (their Proposition 3.4), while `e(P) ≤ n!`, so the Chinese Remainder Theorem reconstructs `e(P)` from the residues `e(Q_p) mod p`. Each query `Q_p` has `N = pn ≤ n³` elements and `< 1.5N` covers, and there are polynomially many primes. Hence

```
#LE  ≤_T^p  #LE restricted to posets with < (3/2)N covers.
```

Since general `#LE` is `#P`-complete, the sparse-Hasse restriction is `#P`-hard under polynomial-time Turing reductions. It is in `#P`, so it is `#P`-complete under Turing reductions.

The reduction is genuinely Turing, not many-one: it makes one query per prime and combines the answers by CRT. This matches the “Turing” qualifier in the front question. No parsimonious or many-one reduction is claimed.

---

## 2. Literature audit: dense or sparsifiable?

- `[literature]` **Brightwell–Winkler 1991** prove general `#LE` `#P`-complete (Order **8** (1991) 225–242, doi:10.1007/BF00383444; STOC 1991). Their published construction is not sparse; they explicitly wrote that height-two `#LE` was still suspected hard but “an entirely different construction is required” (quoted in Dittmer–Pak, §1). Their proof also uses the modulo-`p`/CRT scheme, so it is already a Turing-style reduction.

- `[literature]` **Dittmer–Pak 2018/2020** supply that different construction. The height-two `Q_p` is the sparsification: the `n(p-2)` new elements `x_{ij}` are leaves attached to the `x_i'`, and they dilute the potentially dense comparability graph of `P` to linear average degree. The paper does not advertise the `O(N)` cover count, but the count is immediate from their §6.

- `[literature]` **Chan–Pak survey**, *Linear extensions of finite posets*, EMS Surv. Math. Sci. (2025), doi:10.4171/EMSS/97; arXiv:2311.02743, §12.1, confirms the height-two/dimension-two/incidence-poset refinements. Its list of polynomial classes is: bounded width, skew Young diagrams, series-parallel, bounded decomposition diameter, cover graphs with disjoint cycles, `N`-free with bounded activity, bounded treewidth, and mobile posets. None of these covers all sparse-Hasse posets.

- `[literature]` **Kangas–Hankala–Niinimäki–Koivisto**, *Counting linear extensions of sparse posets*, IJCAI 2016, 603–609, is an **algorithmic** paper, not a polynomial-time algorithm for the class. Its two bounds are `O(2^n n)` and `O(n^{t+4})`, where `t` is the treewidth of the cover graph. The second is polynomial only for bounded treewidth. Their “sparse” is an experimental/heuristic notion. Dittmer–Pak’s introduction lists “sparse posets [EGKO16, KHNK16]” among polynomial cases, but that phrasing should not be read as the `O(n log n)`-cover class: the cited results are exponential in `n` or FPT in treewidth.

- `[literature]` **Eiben–Ganian–Kangas–Ordyniak**, *Counting linear extensions: parametrizations by treewidth*, Algorithmica **81** (2019) 1657–1683 (ESA 2016), is FPT in treewidth, not polynomial in `n` for unbounded treewidth.

No later work found in an arXiv search explicitly states sparse-Hasse `#LE` hardness; the result above is a corollary of the published Dittmer–Pak construction.

---

## 3. Computations

All scripts were run in `/tmp/opencode`; nothing in the repository was modified.

### 3.1 Verification of the `Q_p` identity

I implemented the Dittmer–Pak construction and counted linear extensions exactly by order-ideal DP.

| `n` | posets tested | `p` | `N` | mismatches for `e(Q_p) ≡ (-1)^n e(P) mod p` | max `cov/N` |
|---|---|---|---|---|
| 3 | all 19 | 5 | 15 | 0 | 1.000 |
| 4 | 73 of 219 | 5 | 20 | 0 | 1.100 |

For `n = 4`, the maximum ratio is attained by the chain: `cov = 4·4 + 6 = 22`, `N = 20`, ratio `1.1`. The identity check confirms both the construction and the implementation.

### 3.2 Cover-count ratio

For a chain (the densest comparability graph) the ratio is

| `n` | `p` | `N` | covers | ratio |
|---|---|---|---|---|
| 10 | 11 | 110 | 145 | 1.318 |
| 20 | 23 | 460 | 630 | 1.370 |
| 50 | 53 | 2650 | 3825 | 1.443 |
| 100 | 101 | 10100 | 14950 | 1.480 |
| 500 | 503 | 251500 | 375750 | 1.494 |

The ratio approaches `3/2` from below and never reaches it. Random dense posets and antichains give smaller ratios. This confirms the bound independently of the paper’s arithmetic.

### 3.3 Small-`n` census

I enumerated all labelled posets for `n = 4` (219) and `n = 5` (4231), computed cover counts, `e(P)`, width, and height.

- For `n = 4`, all 219 posets have at most 4 covers, while `2 n log₂ n = 16`; the sparsity filter is vacuous. There are 9 distinct values of `e(P)`. The class `(covers, width, height) = (3, 2, 3)` contains both `e = 2` and `e = 3`.
- For `n = 5`, all 4231 posets have at most 6 covers, while `2 n log₂ n ≈ 23.2`; again the filter is vacuous. There are 23 distinct values of `e(P)`. Eight `(covers, width, height)` classes contain more than one `e` value; for example `(4, 3, 3)` gives `e ∈ {6, 8, 10, 11, 12}` and `(4, 2, 3)` gives `e ∈ {4, 6, 7, 9}`.

`[experiment]` Conclusion: for small `n`, the `C n log n` restriction is vacuous (the maximum possible number of covers is `⌊n²/4⌋`, which is below `2 n log₂ n` until much larger `n`). Small-instance enumeration therefore cannot distinguish hard from easy; the hardness is asymptotic and comes from the Dittmer–Pak padding, not from a small-`n` pattern. The enumeration does show that `e(P)` is not determined by cover count, width, and height, so no simple formula in those invariants covers even the small sparse cases.

### 3.4 Sparse-Hasse does not imply bounded treewidth

`[experiment]` I built incidence posets of random 3-regular bipartite graphs. Their cover graph is the incidence graph; they have about `1.2 N` covers on `N` elements.

| `N` elements | covers | `cov/N` | min-fill treewidth upper bound |
|---|---|---|---|
| 297 | 354 | 1.192 | 21 |
| 498 | 596 | 1.197 | 37 |
| 749 | 898 | 1.199 | 57 |

The min-fill upper bound grows roughly linearly. `[literature]` Random 3-regular graphs have linear treewidth with high probability, so these are sparse-Hasse posets with unbounded treewidth. Consequently the `O(n^{t+4})` treewidth algorithm of Kangas et al. is not a polynomial-time algorithm on the class, and bounded-width/treewidth/series-parallel structural algorithms do not cover sparse-Hasse posets either.

---

## 4. Relation to board #301 and the reachable subclass

`[deduction]` The front question concerns **all** sparse-Hasse posets, and it is answered yes. There is a stronger consequence for the board’s “reachable states” discussion, conditional only on the elementary cover-comparison lemma:

> If `P` has `c` cover relations, then `P` is reachable from the antichain in exactly `c` comparisons: compare its covers one at a time. A cover of `P` cannot be transitively implied by other covers, so each such pair is incomparable when compared.

Applying this to `Q_p`: `cov(Q_p) < 1.5N`, while `S(N) ≥ log₂ N! > 1.5N` for `N ≥ 6`. Hence every `Q_p` is a state reachable within `S(N)` comparisons. So the same Turing reduction shows that `#LE` is `#P`-hard on the depth-`S(N)` reachable class as well. This does **not** prove `S(N)` is hard; it only says that any exact evaluator relying on a polynomial-time `#LE` oracle for reachable sparse states would imply `#P = P`.

`[experiment]` One caution about the 2026-11-08 correction on #301: I independently ran the BFS for small `n`. At `n = 3, k = 1`, reachable-at-most-`k` states = 7 and `{|cov| ≤ 1}` = 7. At `n = 4, k = 2`, reachable = 73 and `{|cov| ≤ 2}` = 73. The correction’s figures “7 vs 17” and “73 vs 209” do not reproduce: the cover-feasible counts are the reachable counts. The number 2045 at `n = 7` is the total number of **unlabelled** posets, not a cover-feasible count. This suggests the correction’s census conflated labelled/unlabelled or used a different definition. This side issue does not affect the sparse-Hasse theorem, but it matters for the reachability consequence and should be re-checked before the board relies on it.

---

## 5. Caveats and what is not claimed

- The result is about **exact counting of linear extensions** `e(P)`. It is not a hardness result for `S(n)`, `SORT-BOUND-U`, or the minimax comparison game.
- The reduction is **Turing**, via CRT. No many-one or parsimonious reduction is obtained; the existence of an FPRAS for `#LE` makes a parsimonious reduction unlikely.
- The encoding is the natural one: a poset given by its cover list / Hasse diagram of size `O(N log N)`. If the input is a dense `N × N` comparability matrix, the input length is `Θ(N²)` even when the poset has few covers; the sparsity statement is then about the poset, not the encoding length.
- `C = 2` is a safe absolute constant; the construction actually gives `< (3/2)N` covers. With log base 2 it satisfies `C = 3/2` for `N ≥ 2`.
- I did not find the sparse corollary stated explicitly in the literature; it is a deduction from the published Dittmer–Pak construction. The collector should verify the arithmetic against the published version’s §6 and, if posting, attribute it as a corollary rather than as a theorem of Dittmer–Pak.

---

## 6. References

1. G. Brightwell, P. Winkler, *Counting linear extensions*, Order **8**(3) (1991) 225–242, doi:10.1007/BF00383444; STOC 1991, doi:10.1145/103418.103441.
2. S. Dittmer, I. Pak, *Counting linear extensions of restricted posets*, Electron. J. Combin. **27**(4) (2020), #P4.48, doi:10.37236/8552; arXiv:1802.06312. Theorem 1.1, §6 (height-two construction).
3. S. H. Chan, I. Pak, *Linear extensions of finite posets*, EMS Surv. Math. Sci. (2025), doi:10.4171/EMSS/97; arXiv:2311.02743, §12.1.
4. K. Kangas, T. Hankala, T. Niinimäki, M. Koivisto, *Counting linear extensions of sparse posets*, IJCAI 2016, 603–609.
5. E. Eiben, R. Ganian, K. Kangas, S. Ordyniak, *Counting linear extensions: parametrizations by treewidth*, Algorithmica **81** (2019) 1657–1683.
6. S. Dittmer, *Counting linear extensions and contingency tables*, Ph.D. thesis, UCLA, 2019 (for parity and related refinements).

## Output 635 (msg_1b99f56d2001ytuvRpsGmWJ0dN)

Recovery check complete. I inspected the conversation, worktree, Git state, `/tmp` artifacts, board digest, and the durable frontier ledger. No external side effects were performed by this run.

**Verified state**

- **Worktree:** `/home/lubko/soring-fronts/sparse-hasse-extension-hardness` is detached at `f89f6d0`.
- **Git:** `git status --short` is empty; no modified, staged, or untracked files. No commits, pushes, or merges were made. The latest commit is still `f89f6d0 Add research note: FO(TC) strategy programs for exact optimal sorting`.
- **Board #301:** Recent digest shows no post from this run. The only relevant existing post is the older shallow-state correction by Viche Executive; no duplicate was created.
- **Durable ledger:** `~/.local/state/soringp1/frontier-ledger.json` has `sparse-hasse-extension-hardness` marked `status: "investigated"`, `exit_state: "clearexit"`, with `finding_unverified: "duplicate acknowledged, no external effects"`. I did not modify the ledger.
- **Local scratch only:** `/tmp/opencode/dp_sparse.py`, `/tmp/opencode/sparse_stats.py`, and downloaded reference files were created. These are not repository or board effects.
- **No Lean files, notes, tests, or scripts were added to the repository.**

**Unfinished work:** none. The substantive report was delivered in the immediately preceding assistant message. I have not repeated it here to avoid duplication. The ledger does not record that report’s findings beyond “duplicate acknowledged,” so if the collector relies on the ledger rather than the conversation, the report may need to be extracted from the preceding message or explicitly re-requested. No other action is outstanding.
