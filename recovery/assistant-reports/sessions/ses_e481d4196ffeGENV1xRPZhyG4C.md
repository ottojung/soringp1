# antonina-OzI62yPb9STg7h0xQR3Ebp-trees

Session: ses_e481d4196ffeGENV1xRPZhyG4C
Workspace: /home/lubko/soring-fronts/exec-optimal-framed-completeness-20261107
Created: 1794086452915; updated: 1794087207384

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 46 (msg_1b7e2e77e001Ru2idGtIn6XOLS)

## Deliverable: the framed-grammar question remains open

I do **not** have a sound construction of polynomial-size permutation-framed DAGs at height \(S(n)\) for a nontrivial infinite optimal family, nor an unavoidable obstruction for the stated grammar. The current evidence does not justify either conclusion. In particular, the entropy and forgetting identities are necessary conditions, not a lower-bound method by themselves.

### What the cited results establish

- **[Literature]** Sergeev, *On the Asymptotic Complexity of Sorting*, ECCC TR20-096 (2020), Theorem 3, gives
  \[
  S(n)=\log_2(n!)+O\!\left(n/(\log n)^{1/5}\right).
  \]
  This is a comparison bound for a sorting algorithm, not a compact certificate bound. The project’s summary correctly notes that the asymptotic statement alone gives neither a finite effective bound for every \(n\) nor polynomial-size certificates.
- **[Literature]** Ford–Johnson/MergeInsertion has comparison bound
  \[
  F_{\rm FJ}(n)=\sum_{j=1}^n\left\lceil\log_2(3j/4)\right\rceil.
  \]
  Its known optimality for \(n\le 11\) does not extend to all \(n\): \(S(12)=30\), while the information lower bound is 29; exact values through 22 are finite results, not an infinite family.
- **[Paper theorem, as recorded in the frontier note]** The permutation-framed grammar has a polynomial-time soundness checker for explicit DAGs. A polynomial-size DAG of height \(S(n)\) for every \(n\) would imply unary `SORT-BOUND-U ∈ NP`. That completeness claim is open.
- **[Paper construction, with audit caveat]** The note gives an \(O(n^2)\)-node construction for Ford–Johnson-style rank-envelope insertions, but explicitly leaves the complete recursive frame construction and odd-element case for independent audit. Even if that audit succeeds, its height is \(F_{\rm FJ}(n)\), not generally \(S(n)\).

### Why the tempting obstruction does not follow

The certificate entropy identity is
\[
\mathbb E\!\left[\sum_{\rm queries}(1-H+\lambda)\right]
 =\mathbb E[D]-\log_2(n!)\le k-\log_2(n!),
\]
where the walk resamples a compatible order at each annotation. Thus a near-information-height certificate has small *expected total* imbalance and forgetting under that auxiliary walk. It does **not** force every path to have small loss, and it does not bound the number of distinct annotations or DAG nodes. The majority-path telescoping identity has the same limitation: it constrains a path’s accumulated quantities, but does not show that histories requiring different annotations are adversarially forced.

Likewise, the frontier note’s \(2^r\) nonisomorphic insertion histories with only
\[
\log_2\prod_{j=1}^r\frac{4j}{4j-1}
=\tfrac14\log_2 r+O(1)
\]
bits of forgetting cost is a warning against counting state types as a lower bound. It is not a lower bound on any certificate DAG: those histories have not been shown to be forced against every height-optimal root strategy.

### Independently checkable conclusion

**[Deduction]** The cited entropy and history-count facts alone yield no scoped grammar no-go. A valid obstruction would need, at minimum, a family of histories that an adversary can force against *every* height-\(S(n)\) root strategy, plus a proof that sound joins must preserve enough distinctions among those histories to exceed polynomial DAG size. Neither ingredient is supplied by the cited identities or by counting nonisomorphic reachable posets.

Conversely, the Ford–Johnson rank-envelope sketch does not yet deliver the requested positive result: its full lifted-frame/join audit is pending, and the stated cost is not an infinite optimal-family theorem. Sergeev’s group-insertion bound also does not currently provide the missing polynomial-state grammar with sound joins and exact optimal height.

**Result:** no theorem-level progress on #301/#47 is established by these sources. The decisive next step is either (i) finish a complete Ford–Johnson frame audit and prove an infinite subfamily’s exact optimality independently, or (ii) derive a genuine forced-history lower bound for the specified grammar. The existing material establishes neither. No repository files were changed and no board post was made.

## Output 314 (msg_1b7ecff74001xaFoXTMeDp4uGx)

I inspected the environment before doing any further work. Here is the effect audit and the completed (previously unstarted) research deliverable.

## 0. Side-effect audit

- `git status --porcelain` is empty; `HEAD` is detached at `c865b23`; no new commits, no untracked files, no stash changes. I created nothing in the repository.
- The only 2026-11-07 board entries are two **Viche Executive** messages (21:11 and 21:21). The 21:21 one is the dispatch of this front (`OzI62yPb9STg7h0xQR3Ebp-trees`). There is **no** post from this research agent, so nothing was duplicated.
- The previous turn performed only reads plus one PDF fetch (unsupported) and one cancelled web search — no external side effects.
- All artefacts below live in `/tmp/opencode/`, not the repo.

**Conclusion: the interrupted turn produced no effects to undo. The unfinished part was the actual mathematics, which follows.**

## 1. Sharpening the question

**[definition]** A certificate is the checker grammar of `scripts/check_framed_strategy.py`: a DAG with forward arcs, each arc = (comparison outcome, slot permutation); node annotation is the transitive closure of guaranteed relations, intersected over all *feasible* incoming arcs; leaves must be total; height = longest feasible path.

**[deduction] Equivalence lemma.** A framed certificate of height `k` exists for `n` **iff** `S(n) ≤ k`.
*Proof.* (⇐) Unfold any height-`k` adaptive tree; no joins occur, so the checker accepts. (⇒) For each input permutation, its outcome is never a logically impossible branch, so it follows one path of length ≤ `k`; every reached leaf is total, hence sorted. That path is an adaptive comparison strategy of worst case ≤ `k`. ∎

**Consequence.** "Can certify a height-optimal sorter for every `n`" is *trivially true without a size bound* (take a tree). The entire frontier is the **polynomial-size** qualifier. Any statement that the grammar "cannot certify optimality" must be a size statement.

## 2. The literal constructive arm is blocked by the state of knowledge of `S(n)` itself

**[deduction] Scoping theorem.** If `{D_n}` is an infinite family of certificates with `height(D_n) = S(n)`, then `S(n)` is exactly determined for infinitely many `n` (namely, all `n` in the family). In particular, any *verified* infinite height-optimal family must supply, for each `n`, a matching lower bound `S(n) ≥ height(D_n)`; a certificate only gives the upper half. ∎

**Current facts [literature].**

- Exact `S(n)` is known only for `n ≤ 22`: `0,1,3,5,7,10,13,16,19,22,26,30,34,38,42,46,50,54,58,62,66,71` (OEIS A036604; Peczarski 2004; Stober–Weiß ALENEX 2023 for 16–18 and the 19–22 values). `n = 23` is open.
- Whether `S(n) = ⌈log₂ n!⌉` for infinitely many `n` is open. The only unconditional all-`n` lower bound used here is `⌈log₂ n!⌉`; all larger lower bounds are finite case results.

So **there is no known infinite family of `n` with `S(n)` determined**, and therefore no currently verifiable "infinite height-optimal family beyond the known small values". This is a limitation of the state of knowledge about `S(n)`, *not* a property of the grammar. It is the first thing any proposed infinite family must address.

**Consequence for the obvious candidate.** The rank-envelope/Ford–Johnson architecture has exact cost `F_FJ(n)=Σ_{j=1}^n ⌈log₂(3j/4)⌉`. Computed against the exact sequence:

| n | 1–11 | 12 | 13–19 | 20–21 | 22 | 23 |
|---|---|---|---|---|---|---|
| `F_FJ(n)` | = S(n) | 30 | = S(n) | = S(n) | 71 | 76 |
| `S(n)` | = | 30 | = | = | 71 | unknown |

`F_FJ(n) = S(n)` for **every** `n ≤ 22` [literature: FJ is minimum-comparison for `n ≤ 22`, Peczarski 2004 + Stober–Weiß 2023; formula from Knuth/Hadian]. But Manacher (JACM 26(3), 1979, *The Ford–Johnson sorting algorithm is not optimal*) gives a better algorithm for all large `n`; Peczarski (IPL 101(3), 2007, *… still unbeaten for less than 47 elements*) locates the boundary. Hence `F_FJ(n) > S(n)` for all sufficiently large `n`. **Therefore even a complete, correct all-`n` rank-envelope DAG at height `F_FJ(n)` — the construction the frontier note flags as "plausible, audit pending" — is provably not height-optimal beyond a finite range.** This is a scoped no-go for the FJ architecture, not for the grammar.

## 3. What *is* constructible and verifiable: a polynomial-size family with exact cost

**[paper construction + machine-checked for small `n`]** Binary-insertion framed DAG. State at stage `m` (`1 ≤ m ≤ n−1`): slots `0..m−1` a guaranteed sorted chain, slot `m` the element to insert, rest inert. Binary-search the rank of slot `m` among the `m+1` gaps; every search leaf applies the insertion permutation placing slot `m` at its rank; **all leaves join at the next stage root**, whose annotation is exactly the chain `0<…<m`.

- **Soundness/joins:** each leaf guarantees the full chain `0<…<m` on the new slots, so the join intersection is exactly that chain. Comparisons never involve inert slots, so recursion/insertion frames are sound.
- **Exact cost:** `B(n) = Σ_{k=2}^{n} ⌈log₂ k⌉`.
- **Exact size:** `1 + n(n−1)/2` nodes (a tree with `m+1` leaves has `m` internal nodes per stage, plus one final leaf).

I generated the certificates and checked them two independent ways: the repository checker `check_framed_strategy.py`, and a brute-force simulator over all `n!` inputs (following the unique outcome, applying the frame, asserting the final slot array is sorted and the path length ≤ budget).

```
n   nodes  depth B(n)  F_FJ  S(n)   B−F
5      11      8        7     7     +1
6      16     11       10    10     +1
7      22     14       13    13     +1
8      29     17       16    16     +1
9      37     21       19    19     +2
10     46     25       22    22     +3
11     56     29       26    26     +3
12     67     33       30    30     +3
...
19    172     64       58    58     +6
22    232     79       71    71     +8
```

Checker: `ACCEPT` for all `n = 1..12`; brute force: `OK` for all `n = 1..8`. Artifact: `/tmp/opencode/gen_insertion_dag.py`.

**Interpretation.** This proves the grammar is not the obstacle to polynomial-size all-`n` certificates and gives a clean exact-cost baseline. But `B(n) − S(n)` already equals 1 at `n = 5` and grows, so this family is **not** height-optimal (see the table). It is not the requested infinite optimal family; it is the constructive calibration point.

## 4. Why the entropy/forgetting identities cannot supply the missing obstruction

The frontier identity (for the auxiliary resampling walk, path length `D`) is
`E[Σ_queries (1 − H + λ_b)] = E[D] − log₂(n!) ≤ k − log₂(n!)`,
with forgetting `λ_b = log₂(e(Q)/m_b) ≥ 0`.

**[deduction] It constrains paths, not node counts.** It is an identity about the *average total* imbalance/forgetting over a path measure; it contains no term measuring the number of DAG nodes or annotations. A DAG with `M` nodes has at most `M` distinct annotations by definition, so "exponentially many histories" only ever referred to **tree paths**, and a single node can absorb exponentially many of them.

**[deduction] The over-approximation lemma (the precise reason).** For a node `v`, let `R_v` be the set of current orders actually reaching `v`, and `Ext(P_v)` the orders consistent with its annotation. Soundness needs the shared suffix to sort `R_v`, *not* `Ext(P_v)`; in general `R_v ⊊ Ext(P_v)`. Consequently the minimax value `F(P_v)` of the annotation **need not** bound the suffix height, and `λ` is exactly the bookkeeping of this over-approximation. Any lower-bound argument that treats the annotation as the true state (local-minimax normalisations, "number of nonisomorphic reachable posets", naive `F(P_v) ≤ remaining` claims) is invalid for the stated grammar. The bubble-sort chain is the smallest witness: one terminal node, `O(n²)` nodes, all `n!` inputs sharing node paths but taking different arc frames.

**[literature/paper, as recorded in `research-framed-certificate-frontier.md` §3]** There are explicit rank-envelope schedules with `2^r` nonisomorphic insertion histories and total forgetting only `¼ log₂ r + O(1)` bits — a model of *small* `λ` despite exponential history diversity. It is explicitly **not** proved forced along any optimal root strategy, so it is a warning, not a lower bound.

Therefore, for the stated forgetful grammar, the entropy/forgetting route yields only:
`expected total (1−H)+λ ≤ S(n) − log₂(n!) = o(n)` (Sergeev), i.e. a necessary condition on a near-information-height certificate. It gives **no** node-count lower bound.

## 5. Scoped no-gos that do exist (and are clearly not the stated grammar)

- **Exact-reset / no-forgetting fragment.** The odd-`n` antichain→star obstruction (`research-exact-reset-realizability.md`) is a genuine scoped no-go: exact reset requires integral multiples of `e(F')`, which the root split violates. The stated grammar allows intersection/forgetting and already escapes it, so this does not transfer.
- **Minimax-exact normalisation.** Restricting to certificates where every node is on a critical path and the shared suffix is optimal for the *whole* annotation `Ext(P_v)` forces no genuine joins and yields `2n!−1` nodes. But this hypothesis is an added strengthening, and bubble/insertion certificates violate it (they are sound only on `R_v`, not `Ext(P_v)`). It is **not** a no-go for the stated grammar.

## 6. Verdict and the decisive next step

- **Constructive arm:** not achievable with current knowledge. The literal "infinite height-optimal family" needs `S(n)` determined infinitely often; only `n ≤ 22` is known. The FJ/rank-envelope architecture is provably non-optimal for all large `n` (Manacher). What *is* available is a verified `O(n²)`-node family at the exact non-optimal cost `B(n)=Σ⌈log₂ k⌉` (Section 3).
- **Obstruction arm:** no scoped no-go for the forgetful grammar is obtained, and the entropy/forgetting identities provably cannot yield one by themselves (Section 4). A valid obstruction must be a **forcing** statement: an infinite family of posets that every height-`S(n)` root strategy is forced to traverse, together with a proof that any sound join must preserve enough of the reached-set distinctions to exceed polynomial node count. That is exactly the unresolved "adversarial root forcing" target (issue #48), and it requires an adversary theorem, not a count of nonisomorphic states.
- **Distinctions preserved:** Section 2/5 is scoped to the constructive route or to restricted fragments, never "all proof systems"; the `F_FJ = S` statement is finite (`n ≤ 22`); the insertion family is machine-checked only for small `n` but proved for all `n`; no complexity separation or NP/coNP claim is made.

Reproduction: `python3 /tmp/opencode/gen_insertion_dag.py` (checker) and the brute-force block in this session (all `n!` inputs). No repository files, Lean files, or board posts were created or modified.

## Output 348 (msg_1b7ee2c340014FkfkZ1uBGMUp5)

## Recovery audit complete

- **Git:** The worktree remains clean at detached `c865b23`; no commit or repository edit occurred.
- **Board:** Recent #301 entries are Viche dispatch/curation messages. There is no post from the interrupted research turn, so no board post needs to be deduplicated.
- **Durable records:** The ledger shows the assigned front and several related fronts already marked investigated. The exact assigned agent ID was not found in the ledger; I can’t determine from these records whether its run has a separate completion record. The board records its dispatch as running at 21:21, not its later completion.
- **Temporary artifact:** `/tmp/opencode/gen_insertion_dag.py` exists. It is outside the repository; its presence and the preceding conversation show the binary-insertion DAG check was performed. No further research or external actions were needed.

Nothing was posted, committed, or left unfinished in the repository. **Review item:** if you need confirmation that the dispatched agent itself exited, that status remains uncertain in the records I inspected.
