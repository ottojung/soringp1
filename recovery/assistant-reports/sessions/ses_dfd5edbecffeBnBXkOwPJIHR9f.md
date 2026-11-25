# Find related load/balance results

Session: ses_dfd5edbecffeBnBXkOwPJIHR9f
Workspace: /home/lubko/soring-fronts/per-key-load-additive-gap-alln
Created: 1795340444698; updated: 1795340539194

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 5 (msg_202a1242d001gxMhtd8JECXLYA)

I'll conduct a thorough search. Let me start by understanding the repository structure and running several independent searches in parallel.

## Output 24 (msg_202a14935001d5F4PdfhVF4Uo8)

Now let me run broad parallel searches across docs and scripts for all the requested themes.

## Output 47 (msg_202a1584e001s9Qz4553lqiluT)

Let me search more specifically for the per-key load theme and related terms across all file types, plus check git context.

## Output 70 (msg_202a16887001BQZZBriVwj7Mod)

Interesting — I found references to "average-depth obstruction", "imbalance", and "degree-based move identification is unsound". Let me dig into these and the JSON research files.

## Output 93 (msg_202a17e1d001mmwa4ddzPGzvet)

Let me dig into the most relevant detailed passages: the soundness/completeness doc, general-poset hardness boundaries, the one-ply obstruction, and the degree-unsoundness script.

## Output 116 (msg_202a198a30011YFrSdkkJty0vI)

Let me do additional thorough searches: external path length, average-related terms, and the full hardness boundaries / strategy certificate docs.

## Output 139 (msg_202a1b64d001aCzqQfiRDR6BPH)

Let me examine the balanced-tree/greedy passages and the additive-gap (Sergeev) material, plus the problem statement's path-length framing.

## Output 162 (msg_202a1d550001izKUo9g27xnDes)

Let me read the Sergeev asymptotic note in full (it has per-node/expected-depth analysis) and the sublinear-surplus barrier section.

## Output 181 (msg_202a1f01c0010V6jRKDaPkiEAJ)

Let me do final verification searches: per-key O(log n), README indexing, and soundness/completeness across scripts.

## Output 204 (msg_202a212ff001dl2r6k5C6N8nF1)

Let me read the two final relevant passages in the scripts (research_frontier.py curator prompt and check_framed_strategy.py header).

## Output 219 (msg_202a2218e001m8Pz5vht9plusa)

I have completed a very thorough search of all `docs/*.md`, `scripts/*`, plus supporting files (`README.md`, `AGENTS.md`, `SoringP1/`, `tests/`, JSON research files). Here are my findings.

---

## 1. Headline result: the per-key-load topic is essentially absent from the repository

There are **no matches anywhere** for the literal terms:
- `Lambda(n)` / `Λ(n)` / `λ(n)` (the only `λ` hits are `lambda_b` — a *forgetting loss*, see §2 below),
- `ceil(2S(n)/n)` or any `2S(n)/n` variant,
- `per-key load`, `per key load`, `load-balanced optimal sorting tree`, `worst-case load per element`, `maximum comparisons per key`, `fairness` of comparison trees, `O(log n) per-key load`.

The only string containing `per path` is unrelated: `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-encoding-consequences.md:478` — "`O(n²)` per path. Since the tree itself is exponential (unary) or doubly …". All other `load` hits are `json.loads`, `workload`, or `load_packet_plan` in scripts/tests. The branch name `per-key-load-additive-gap-alln` has no corresponding note or script yet.

The single closest repository artifact is a *roster entry naming an active agent/worktree*, with no accompanying document in this repo:
- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/scripts/agent_pool_keeper.py:38`:
  `('z8FIxKzTS8NklpFKEez6hS-equality', 'soring301-new-avgdepth-obstruction-20261022', 'External-path/average-depth obstruction to exact sorting'),`
  This is the only trace of "average depth / external path length" work; no `docs/research-avgdepth*.md` or script exists here.

---

## 2. Closest related material: per-path maximum vs. average/entropy accounting

- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/problem.md:11-13`: "`S(n) = min { height(T) : T correctly sorts every permutation of n keys }`. Height is the **maximum number of comparisons on any execution path**." — the model counts only path maximum; per-key load is not part of the defined objective.

- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-framed-certificate-frontier.md:145-185` — §4 "Entropy and information loss across joins" is the nearest thing to an average-load analysis. Per-query quantities `q_b`, `m_b`, `H`, and `lambda_b`:
  - line 154: `lambda_b = log₂(e(Q)/m_b)` (explicitly the *forgetting loss*, not a per-key load),
  - line 164: "For its path length D <= k,",
  - line 166: `E[sum_over_queries (1 - H + lambda_b)] = E[D] - log₂(n!) <= k-log₂(n!).`,
  - lines 180-182: "A near-information-bound certificate therefore has only `o(n)` **expected total imbalance** and forgetting under the auxiliary walk; linear information loss would falsify that particular compression scheme."

- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-sergeev-asymptotic.md:25-54` — the strongest per-node/expected-depth decomposition in the repo (this is the natural tool for any per-key/average-load question):
  - lines 29-32: "For each internal node `v`, let `q_v` be its reach probability and `p_v` the fraction of reachable permutations giving one outcome. … let `D` be the random depth of the output leaf."
  - line 37: `log₂(n!) = Σ_v q_v h₂(p_v)`, `E[D] = Σ_v q_v`.
  - line 41: `k−log₂(n!) = E[k−D] + Σ_v q_v(1−h₂(p_v))`.
  - lines 43-48: an expected-count bound on comparisons of conditional bias ≥ δ and `E[Σ_(v visited) (p_v−1/2)²] ≤ (ln 2)/2 · (k−log₂(n!))`.
  - lines 52-54 caveat: "This is NOT a bound for every adversarial branch."

---

## 3. "Balanced" trees / balance–optimum tension (no load-balancing lemma exists)

- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-state-compression.md:154-163` — the decisive negative result: "**A restricted class of decision trees does not preserve the optimum.** … the deterministic **balanced-greedy** class: at every state compare a pair minimizing the larger child's linear-extension count. This class is optimal for small `n` — it returns `S(3..8) = 3,5,7,10,13,16` — but **fails at `n=9`**: it returns `20` while `S(9)=19`." This directly bears on any hope that optimal trees are automatically load-balanced.

- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-compression-next.md:282`: "balanced-greedy restricted tree class returns `S(9)=20 > 19`." and line 313: "staging balanced-greedy counterexample".

- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-n12-nontightness.md:213-231` — **H4 (forced balanced prefix)**: "a comparison is admissible only if its heavier child fits `2^(h-c-1)`"; lines 221-226: for `n=12, h=29` "only `1/2` splits are admissible … the *second* comparison is forced to pair two free elements"; line 230-231: "the forced-prefix phenomenon is real but **not sufficient**".

- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-hardness-boundaries.md:183-186`: "Kahn–Saks (1984) gave a `3/11`–`8/11` **balanced** pair, hence `O(log e(P))` comparisons with exponential running time"; source listed at line 386 (`J. Kahn, M. Saks, Every poset has a good comparison, STOC 1984 … (3/11–8/11 balanced pair.)`).

- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-obstruction-next.md:233-236, 255`: literature on "`M(m,m) = 2m-1` (Graham–Karp; Stockmeyer–Yao …) … extended to `n <= 1.52 m` … For unbalanced sizes the tape bound is **not** optimal."

- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-framed-certificate-frontier.md:70-71`: "O(n²) comparison nodes and, for balanced merges, O(n log n) **path length** (not O(n²))" — the repo's only explicit "balanced ⇒ small per-path length" statement.

---

## 4. Comparison-graph degree on a path — an explicit no-go finding

- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/scripts/benchmark_symmetry_quotients.py:25`: "* degree-based move identification is **unsound** (n=6 witness);"
- Same file, `falsify_degree_move`, lines 318-320: "Two incomparable pairs whose endpoints have matching (in,out) degrees but whose move values differ: **degree is not a sound move invariant**." The signature used is `sig = (min(deg[i], deg[j]), max(deg[i], deg[j]))` (line 333), with `deg = list(zip(indeg, outdeg))` (line 330) — i.e., exactly a per-key comparison-degree summary, shown insufficient to predict the minimax value.
- Lines 407-427 (`falsify_comparability_graph`): "Two posets with isomorphic comparability graphs but different F … witness n=7"; lines 430-433 (`falsify_graph_transition`): "the graph transition is not well defined, so the graph cannot serve as a DP state."

This is the strongest repository evidence against a degree/load-based structural theorem.

---

## 5. "Additive gap" material (branch-name context): it is about `S(n) − log₂(n!)`, not per-key load

- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-sergeev-asymptotic.md:8-13`: "`S(n) = log₂(n!) + O(n/(log n)^(1/5))` … `0 ≤ S(n)−L(n) = O(n/(log n)^(1/5)) = o(n)`."
- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-n12-nontightness.md:280`: "**Smallest global gap:** `n = 12`, `S(12) = 30 > C(12) = 29` (Wells)." Lines 248-276 document the merge gap `M(a,b)` vs `ceil(log2 e)` with table `M(2,4)=5 > 4`, `M(5,5)=9 > 8`, `M(6,6)=11 > 10`.
- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-structural-lower-bounds.md:31-38`: "the *merge gap* is `delta(a, b) := M(a, b) - ceil(log2 C(a+b, a))`"; lines 70-75: `F(P) ≥ Σ_i ceil(log2 e(P_i)) + Σ_i delta_i`.
- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-winning-frontier-barrier.md:134-162` — §3.1 "Extension to sublinear budget surplus, including `S(n)`": "The `d(n)=o(n)` increment changes only lower-order terms … This specializes to `k=S(n)` because `C(n)≤S(n)` and Sergeev … `S(n)-C(n)=o(n)`." Lines 160-162: "asymptotic and supplies no effective finite threshold … an enumeration barrier only, not a general running-time lower bound."
- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-framed-certificate-frontier.md:74-80`: "This exceeds `log₂(n!)` by `(log₂(e)-1)n + O(log n)`; Sergeev's `S(n) = log₂(n!) + o(n)` therefore excludes this architecture from exact optimality … Improving DAG sharing alone cannot repair this comparison deficit."

---

## 6. General-poset minimax hardness results and their non-transfer (highly relevant)

- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-hardness-boundaries.md:120-153` — §2 "Hyafil–Rivest is about arbitrary tests, not pairwise comparisons": "each test `T_i` is a **subset** of `X` … cost is the **expected** number of tests"; line 137: "**Why it does not transfer.** … The comparison-poset model is a strict restriction of the test family … NP-completeness of a more general problem does **not** imply NP-completeness of a restriction. Concretely, the EC3 gadget uses 3-element subset tests, which do not exist in the pairwise-comparison model." Lines 148-153 extend the caveat to Laber–Nogueira minimum-height decision trees (arbitrary tests, no `o(log n)` approximation unless P=NP).
- Same file, §3 lines 157-197: Cardinal et al. give `O(log n · log e(P))`, `(1+ε) log e(P) + O_ε(n)`, `O(log e(P))` comparisons; lines 175-181: "They approximate the information bound `log e(P)` up to a **constant factor**. They do **not** compute the exact value `S(P)` … the exact optimum may be strictly larger than `log e(P)`."
- Same file, §5 lines 283-329: Proposition 5.1 — "There is no function `f` with `S(P) = f(e(P))` for all posets"; lines 319-323: "the `#P`-completeness of `e(P)` (Brightwell–Winkler 1991) is **not** the reason exact `S(P)` is hard: the antichain has `e = n!`, trivially computable, yet `S(n)` is not known to be polynomial-time computable."
- Same file, §6 table lines 337-351: e.g. line 344 "`Hyafil–Rivest NP-completeness applies to GEN-SORT/SORT-BOUND` — **does not transfer** (arbitrary subset tests)"; line 349 "`GEN-SORT` NP-hard / PSPACE-complete / in P — `[open]`; no primary source found"; lines 353-360 "World status … no NP-hardness result is known for the pairwise comparison model."
- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-one-ply-obstruction.md:52-60`: "**Theorem 1 (soundness).** `[deduction]` For every poset `P`, `L1(P) <= F(P)`" — proof uses "the same recurrence with `F` in place of `L0`"; line 31-36: "It does **not** prove … any complexity-class statement. A comparison lower bound on `S(n)` does **not** imply a complexity-theoretic lower bound for *computing* `S(n)`."
- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-framed-certificate-frontier.md:200-203`: "distinguish a bad reachable poset from one an adversary can **force against every height-k root strategy**"; `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-frontier.json:34`: "Construct a sound, polynomial-time checkable adversary invariant that forces a comparison obstruction from the initial n-element antichain under EVERY sorting strategy, not only from an arbitrary reachable partial order."

---

## 7. "Soundness vs completeness" of certificate restrictions (explicitly codified)

- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-framed-certificate-frontier.md:16-46` — §1 "Certificate grammar, soundness, and missing completeness": line 27: "**[Paper theorem; implemented checker]** This is sound and checkable in time polynomial in the *explicit* graph length and n"; lines 32-34: "If, for every n, **some** graph of polynomial size attains height `S(n)`, then `SORT-BOUND-U ∈ NP`. No such all-n polynomial-size completeness theorem is known." Lines 36-39: "An arbitrary correct comparator network need **not** be accepted if its comparison outcomes are joined immediately"; lines 43-46: Parberry's coNP-completeness caveat.
- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-strategy-certificates.md:110-128`: "The verifier is a **certificate checker**, not a **certificate existence proof**"; lines 115-124: "**Remark 1.3 (no NP membership without a size bound).** … (a) a proof that a polynomial-size DAG always exists for yes-instances (certificate existence) … No condition on no-instances is needed for NP membership: the verifier's soundness ensures that no-instances are correctly rejected … `coNP` membership would require *separate* polynomial certificates of unsortability, not merely the nonexistence of a DAG."
- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/scripts/check_framed_strategy.py:7-9`: "This is polynomial in n and the explicit graph size; for SORT-BOUND-U the number n is already supplied in unary. **Polynomial-size completeness for *optimal* sorting strategies is not asserted.**"
- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/scripts/research_frontier.py:11-16` — curator/agent prompt: "attack a precise all-n falsifiable mathematical claim about complexity of EXACT unary S(n) … **Distinguish general-poset results and certificate SOUNDNESS from completeness.** Do not create Lean or repository changes without a genuinely substantive … new theorem or counterexample."
- `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-compression-next.md:153,159,336`: "orbit reduction is sound but possibly conservative … it is not needed for soundness … sound but not maximally coarse"; `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-state-compression.md:22`: "This note answers the soundness question exactly for permutation symmetry"; `/home/lubko/soring-fronts/per-key-load-additive-gap-alln/docs/research-bidirectional-advice.md:94-97`: "## Soundness … same minimax recurrence (test `TestSoundness`)".

---

## 8. Bottom line for the spawning session

- A per-key-load / `Lambda(n) = ceil(2S(n)/n)` / O(log n)-per-key-load hypothesis would be a **new line** in this repository: no definition, lemma, or experiment for it exists. No claim about it can be verified against prior notes, and there is no prior negative finding to repeat.
- The relevant prior negative findings that constrain it: balanced-greedy does not preserve the optimum (`research-state-compression.md:154-163`), comparison-degree signatures are unsound invariants (`benchmark_symmetry_quotients.py:25,318-339`), and information/surplus accounting is controlled only in expectation, not per adversarial branch (`research-sergeev-asymptotic.md:43-54`, `research-framed-certificate-frontier.md:180-185`).
- The only named artifact hinting at prior work on average per-path depth is the agent-pool roster entry at `scripts/agent_pool_keeper.py:38`; its output is not in this repo.

No files were modified (verified: `git status --short` was empty; current branch `billy-dev`).
