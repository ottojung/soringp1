# antonina-LEJXDYJyPwrou8uAK4Dii6-liberal

Session: ses_e473b3f15ffezD4kSS7JNEuV08
Workspace: /home/lubko/soring-fronts/succinct-cert-complete-antichain
Created: 1794101264718; updated: 1794101276549

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 37 (msg_1b8c4d296001k0RyEkNvorM200)

## Verdict: TREE-REQUIRED (no polynomial-length complete certificate known; the only known sound/complete witness is the full optimal decision tree)

**1. What completeness must certify.** A certificate for `S(n) ≤ k` must certify the existence of a height-`≤k` correct adaptive comparison tree; equivalently, a winning strategy in `G(n,k)` (research-certificates-barriers.md §0/§1). It is not enough to guess `S(n)` itself — the verifier must check the strategy's correctness over all `n!` permutations. The only known sound+complete witness is the reduced optimal tree, which has exactly `n!` leaves and `2·n! − 1` nodes (Claim C, §4 Claim C; experiment §5, `nodes = 2·n! − 1` for `n ≤ 6`).

**2. Size lower bound.** Any correct tree distinguishes all `n!` permutations, so ≥ `n!` reachable leaves and ≥ `2n!−1` nodes (Claim C proof sketch). In unary input length `m = n+k+1 = Θ(n log n)` on informative inputs, `n! = 2^{Θ(m)}`, i.e. `2^{Ω(n log n)}`. The tree witness is therefore super-polynomial in `m`; it only yields a naive `NEXP` verifier, not `NP` (§4 Claim C table: "not polynomial").

**3. Can completeness be achieved without exhibiting such a tree?** Open. The note lists candidate succinct forms (DAG/branching-program compression, strategy program, inductive potential) and marks all `[open]` (§4 Claim C table; §6). No polynomial-size verifier is exhibited. The only known potential (`log₂ e(P)`) is not tight (§3, §8.2), and no compact canonical object describing optimal play is known (§8). Hence one cannot produce an explicit efficient verifier; the established evidence points to the tree being required, with the DAG optimal-play-state-count experiment (§8.1) flagged as the next decisive test.

**Evidence citations:** `docs/problem.md` §"NP membership of a threshold language is not established by exhibiting a sorting decision tree: such a tree may require exponentially many nodes relative to the input length." (lines 57–59); `docs/research-certificates-barriers.md` §4 Claim C (lines 206–242), §5 experiment (lines 286–323), §6 row "poly-size certificate … none known", §8.1.

**Conclusion:** TREE-REQUIRED (with the caveat that a succinct DAG/program certificate remains open, not disproven; no poly witness exists in the current record).
