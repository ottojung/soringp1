# antonina-AQuy3Y3Sjq622ClLMmgHRi-reverie

Session: ses_e15f94dfcffeMSJoHo8vzTERbL
Workspace: /home/lubko/soring301-exec-space-recompute-20261117b
Created: 1794927669832; updated: 1794927787594

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 48 (msg_1ea0848bb001Z5WEamR1aXBm3M)

Wrote `exec-report.md` in `/home/lubko/soring301-exec-space-recompute-20261117b` (no other repo edits, no Lean/PR/comments).

**Question addressed (all-`n`, unary, `N=n+k+1`)**: can budgeted DFS / exact evaluation of `S(n)` or `SORT-BOUND-U` be done in `o(N log N)` space (e.g. `O(N)`/polylog `N`) via recomputation/pebbling/stack compression while remaining provably correct with a stated subexponential time bound?

**Report contents (`exec-report.md`, claims labelled [definition]/[literature]/[deduction]/[conjecture]/[open])**
- **Claim:** For known transcript-DFS methods the decisive state is the current comparison transcript/path of length `d<=k` with `Theta(d log n)=Omega(N log N)` bits on worst-case nontrivial unary instances, so standard transcript-only DFS is not `o(N log N)` (it is `DSPACE(O(N log(N+2)))`, per `docs/research-budgeted-dfs.md` §5.3). No concrete all-instance `o(N log N)` exact subexponential scheme found; no unconditional space lower bound claimed (method-specific obstruction only).
- **Concrete schemes/correctness sketch:** Scheme A — transcript DFS with on-demand reachability recomputation (closure recomputed, path stored), correct by minimax induction/backtracking invariant. Scheme B — same with Savitch reachability (correctness preserved). Scheme C — replay/recompute poset from stored path (cannot discard path).
- **Space/time analysis:** table over memoized DP, naive matrix-per-frame, Scheme A (`O((d+n)log(n+2)) <= O(N log(N+2))`, `2^{O(N log(N+2))}`), Scheme B (reachability workspace `O(log^2 n)` but path-dominant total still `O(N log(N+2))`, time `2^{O(N log(N+2))}` with larger exponent factor), hypothetical `o(d log n)` compression marked open. Explains additive path+workspace decomposition.
- **Falsification/limits:** path-description/information-theoretic obstruction `Omega(d log n)` for explicit move-path storing methods; why naive pebbling/recomputation of transcript doesn’t apply (path encodes dynamic branch choices); stack-compression/checkpoint-replay breaks subexponential time for AND/OR branching; possible non-DFS/succinct/canonical escape routes noted as open but not constructed.
- **Consequence:** `o(N log N)` space with subexponential exact time would require new structural control over reachable transcripts/states beyond closure/reachability recomputation; method-specific barrier only, no complexity-class separations.

**Sources:** `AGENTS.md`, `docs/problem.md`, `docs/research-plan.md`, `docs/research-budgeted-dfs.md`, `docs/upper-bound.md`; external literature fact: Savitch 1970 (`st-REACH ∈ DSPACE(log^2 n)`).
