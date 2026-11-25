# antonina-0qkpoH0fn8AUUREo22wGl0-supplying

Session: ses_df7fc8dedffeHUwP4hMqOd4sGQ
Workspace: /home/lubko/soring-fronts/sortboundu-conp-certificate-20261123
Created: 1795430773346; updated: 1795431129810

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 113 (msg_20807e839001JaNM5qADwYv7jv)

## What I did (constraints honored)
- Read: `/home/lubko/soring301/AGENTS.md`, `/home/lubko/soring301/docs/problem.md`, `/home/lubko/soring301/docs/research-plan.md`, `/home/lubko/soring301/docs/research-certificates-barriers.md` (plus `git remote -v` in that repo). No changes to repo/Lean/tests/CI/ledgers/main, no branches/PRs/commits. All scratch work done under `/tmp` (draft at `/tmp/comment_301.md`). 
- External write requested: **exactly one GitHub issue comment on `ottojung/soringp1#301`**. I attempted to post via `gh` but the `gh` on this system is `v0.0.4` (a GitHub-page opener), not GitHub CLI; no `gh issue comment`/token path available here. **I could not programmatically post the comment.** The full comment text to post is below (verbatim content I prepared).

---

## Full comment text to post on `ottojung/soringp1#301` (ready to paste)

**Title line (optional):** Front `sortboundu-conp-certificate-20261123` (billy-dev, fresh session) — co-SORT-BOUND-U / SORT-BOUND-U ∈ coNP? (report)

**Body:**

```
## Front: sortboundu-conp-certificate-20261123 (billy-dev, fresh session) — report for #301

**Scope/precision (required).** Analysis done only in /tmp scratch; this is intended as the single external write (one GitHub comment on ottojung/soringp1#301). No repo/Lean/tests/CI/ledger/main changes, no PR/commits. Labels below: [definition], [literature], [deduction], [experiment], [open]. No theorem/completion claim beyond what is stated as independently checkable from cited sources.

### Definitions (fixed)
- [definition] S(n) = minimum worst-case number of adaptive pairwise comparisons of a deterministic comparison decision tree that sorts all permutations of n distinct labelled keys (height = worst-case #comparisons). (docs/problem.md)
- [definition] Unary threshold: SORT-BOUND-U = { 1^n # 1^k : S(n) ≤ k }, N := |1^n # 1^k| = n + k + 1. Binary variants noted in docs but out of scope here.
- [definition] Complement (question): co-SORT-BOUND-U = { 1^n # 1^k : S(n) > k } ⊆ {0,1}^* (same encoding).
- [definition] NP/coNP: standard polynomial-time verifier classes for decision languages (deterministic polytime V(x,w), |w| ≤ poly(|x|); existential for NP, dual for coNP). “Polynomial-size existential certificate verifiable in poly(N)” means ∃p,V with x∈L ⇔ ∃w,|w|≤p(N),V(x,w)=1, N=|x|.
- [deduction] Game G(n,k) (docs/problem.md, docs/research-certificates-barriers.md): state = transitively closed partial order on n labelled elements (start empty). While not total and budget < k: sorter picks an incomparable pair {x,y}; adversary answers x<y or y<x; take transitive closure. Sorter wins iff a total order reached within k. S(n) ≤ k ⇔ sorter has a winning strategy in G(n,k) (sorter OR over pairs, adversary AND over the two answers per move) — distinct from “give one tree checked once”.

### What is known (relevant)
- [deduction/literature, Chandra–Kozen–Stockmeyer JACM 1981] SORT-BOUND-U ∈ PSPACE via ATM on G(n,k): n×n poset matrix O(n^2) space, each round existential pair + universal two outcomes + O(n^2) closure, depth k ≤ poly(N), hence ATIME(poly(N))=APTIME=PSPACE. Thus co-SORT-BOUND-U ∈ co-PSPACE=PSPACE. (Repo notes this improves earlier EXPTIME sketches; see docs/research-certificates-barriers.md Claim A.) [deduction] SORT-BOUND-B ∈ EXPSPACE by the same view (n=2^{Θ(m)}).
- [literature + deduction, Mahaney JCSS 1982; Ogiwara–Watanabe SICOMP 1991] SORT-BOUND-U is sparse (≤ O(N^2) strings of length ≤ N). Many-one NP-hardness ⇒ P=NP; polynomial-time Turing NP-hardness ⇒ PH collapses to Δ2^P. [deduction] SORT-BOUND-B is not sparse (dense family of guaranteed-yes inputs), so Mahaney barrier does not apply to binary threshold.
- [literature] Exact S(n): S(n)=⌈log2 n!⌉ for n≤11,20,21; S(12)=30>29 (Wells); exact through n≤22 with S(16)=46,S(17)=50,S(18)=54 (Stober–Weiß arXiv:2206.05597) and related (Peczarski etc.; see docs/literature.md, docs/research-plan.md). Sergeev gives S(n)-log2 n!=o(n). Adaptive worst-case comparisons (not sorting networks).
- [literature] Model-distinct hardness/verification: Hyafil–Rivest IPL 1976 (optimal decision trees, arbitrary tests, NP-complete); Laber–Nogueira DAM 2004 (min-height, arbitrary tests, o(log n)-approx hardness); Parberry MST 1990/LNCS 1991 (fixed sorting-network verification/NONSORT coNP-complete, zero-one principle). [deduction, docs/research-certificates-barriers.md Claim D] No transfer to S(n)/SORT-BOUND-U without a reduction; unary many-one NP-hard routes blocked by sparsity.
- [deduction + experiment, docs/research-certificates-barriers.md] Reduced correct comparison tree: exactly n! leaves, 2n!-1 nodes. Informative unary N=Θ(n log n) ⇒ n!=2^{Θ(N)}; informative binary m=Θ(log n) ⇒ n!=2^{2^{Θ(m)}}. Verifying an explicit tree is poly in its size but not a poly(N) witness in general. [literature, Kleitman–Rothschild Trans AMS 1975; A001035] Labelled posets 2^{Θ(n^2)}; small-n DP visits all labelled posets (cited note), illustrating DAG/state-space scale.

### (A) Concrete polynomial-size existential certificate + polytime verifier (for co-SORT-BOUND-U)?
Honest: none exhibited / not known from cited sources.

- Trivial info cutoff (no external witness needed): if k < ⌈log2 n!⌉ then S(n)>k [deduction from S(n)≥⌈log2 n!⌉]. A verifier can check ⌈log2 n!⌉ in time polynomial in the relevant numeric representation given n in unary (part of N). This fails in hard cases where bound is tight/below S(n): e.g. n=12,k=29 gives ⌈log2 12!⌉=29 but S(12)=30>29 (true) established by exhaustive search in literature [Wells 1965; Peczarski; Stober–Weiß lineage in docs], not by an NP-style short existential witness.
- Not “a single counterexample permutation π”: co-SORT-BOUND-U means every height-≤k sorter strategy loses on some input (possibly different per strategy); ∃π alone is wrong quantifier.
- Not an explicit sorter tree as a general NP upper-bound witness (size/exponential-in-N issues above; wrong direction).
- Adversary winning strategy in G(n,k) ⇔ S(n)>k [deduction]. Natural witness family: describe adversary strategy τ (answers as function of current poset/state and sorter’s chosen incomparable pair) beating every height-≤k sorter strategy. Concrete obstructions to this being poly(|x|), polytime-checkable existential witness are in (B). No polynomial representation/checking method is known in the analyzed material.

Conclusion (A): no concrete (p,V,w) for general instances is produced here; only the info-cutoff subcase is certificate-free/easy and insufficient in hard regimes.

### (B) Concrete obstructions / barriers for natural certificate families
1. [deduction, Claim C] Explicit (reduced) sorter decision-tree witnesses are exponentially large in informative cases (n!=2^{Θ(N)} unary), so not poly(N) certificates.
2. [deduction] Quantifier mismatch: need “all sorter strategies fail”; a single π (or small fixed set without encoding strategies) is insufficient.
3. [deduction] Universal refutation/proof tree over all sorter choices: OR nodes branch over incomparable pairs from current poset; fixing adversary replies gives a tree covering every sorter branch ⇒ up to ∏ d_j ≤ (n(n-1)/2)^k = 2^{Θ(k log n)} nodes in depth ≤k (informative unary Θ(N log N)), exponential in N. DAG compression merges identical poset states but [literature Kleitman–Rothschild 1975; A001035 / experiments cited in docs] labelled posets are 2^{Θ(n^2)}=2^{Θ(N^2)} in general with no established polynomial bound for all adversarial/optimal-play state sets.
4. [deduction] Alternation/game form ⇒ PSPACE view (CKST 1981), not an NP existential witness; no known succinct form converts “∀ sorter strategies ∃ adversary replies” into a single poly(N) existential w.
5. [literature+deduction, Mahaney; Ogiwara–Watanabe] SORT-BOUND-U sparse ⇒ many-one NP-hardness would imply P=NP (limits reductions). This does not imply co-SORT-BOUND-U∉NP (sparse languages can be in NP); it is not an obstruction to membership.
6. [literature, Brightwell–Winkler STOC 1991] e(P) counting is #P-complete and greedy/minimax-e heuristics are not known polytime complete potentials; no known complete polytime-checkable potential certifies S(n)>k beyond trivial cases (info bound can fail, e.g. n=12,k=29).

### (C) Honest inconclusive (classification)
- Open: is co-SORT-BOUND-U ∈ NP (equiv. SORT-BOUND-U ∈ coNP) via any explicit poly(N)-size existential certificate verifiable in poly(N)? (A),(B) show none known and concrete obstructions for natural families, but this is not a non-membership proof.
- Known: SORT-BOUND-U ∈ PSPACE, co-SORT-BOUND-U ∈ PSPACE [CKST]. Consequences (model-precise): co-SORT-BOUND-U ∈ NP ⇒ SORT-BOUND-U ∈ NP∩coNP (within PSPACE). co-SORT-BOUND-U ∉ NP ⇔ SORT-BOUND-U ∉ coNP; together with SORT-BOUND-U∈PSPACE this means SORT-BOUND-U ∉ NP would imply NP ⊊ PSPACE (hence P!=NP, NP!=PSPACE) — a major open separation (out of scope as a target here per docs/problem.md, AGENTS.md). Membership in NP/coNP below PSPACE would be a genuine upper-bound/certificate result but is not established.
- No theorem/completion claimed. Sources cited inline: Chandra–Kozen–Stockmeyer 1981; Mahaney 1982; Ogiwara–Watanabe 1991; Hyafil–Rivest 1976; Laber–Nogueira 2004; Parberry 1990/1991; Wells 1965; Peczarski 2004,2012; Stober–Weiß arXiv:2206.05597; Kleitman–Rothschild 1975; Brightwell–Winkler 1991; and repo docs/problem.md, docs/research-certificates-barriers.md, docs/research-plan.md, AGENTS.md.

Bottom line: no known polynomial-size existential certificate for co-SORT-BOUND-U (N=n+k+1); natural families hit exponential/state-space/quantifier obstructions; status ∈NP?/∈coNP? is open, while ∈PSPACE is established.
```
```

---

## If you want me to proceed now
If you provide a GitHub token (e.g. `GITHUB_TOKEN`/`GH_TOKEN`) in the environment and tell me to post, I can try via the GitHub API (`curl` to `POST /repos/ottojung/soringp1/issues/301/comments`). Otherwise, please copy the body block above into a comment on https://github.com/ottojung/soringp1/issues/301 .
