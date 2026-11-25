# antonina-Wh5owj9bhXKUqdn37tzWKY-cavities

Session: ses_e05195a87ffeBMw5kO7J1x8SYH
Workspace: /home/lubko/soring-fronts/steep-drop-avoidance-optimal-play-alln
Created: 1795210782159; updated: 1795211434152

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fae6a7eb001dbQJ2FAq7m8dsy)

I'll start by exploring the repository structure and reading the key documents.

## Output 21 (msg_1fae6b2b70010HUfIcSuUIwYCS)

I'm on `billy-dev` as required. Let me read the core documents.

## Output 36 (msg_1fae6c000001tBdY5ByaMjJRej)

Now let me read the literature and the research board digest #301.

## Output 51 (msg_1fae6d07700152Q7mmf5mZ8yG2)

Let me look at the full board digest and check for any prior work from earlier sessions.

## Output 70 (msg_1fae6df9b001EjjghD4ZX7FBYK)

There's recent prior work (`attack_steep.py` at 21:36Z). Let me inspect it and related scratch work before doing anything.

## Output 115 (msg_1fae741a40011sqt7cZRXNep4b)

No prior board post from this front; only scratch work. Let me check the ledger front status and confirm worktree cleanliness, then run the existing solver to establish a baseline.

## Output 130 (msg_1fae7de0c001dCwNCb6O3LGcZR)

Baseline confirmed. Let me push the computation to n=8 while reading the full board posts for the n=9 witness details.

## Output 165 (msg_1fae87543001s4rlDcrrO62iUQ)

Now let me build a targeted analysis of the n=9 witness from board #301, checking whether it's a steep trap reachable under a steep-free prefix.

## Output 185 (msg_1fae8ccd8001Uql99jtouz7Cgo)

n=8 confirms steep-free strategy exists. Now the critical n=9 witness analysis.

## Output 196 (msg_1fae8dc8b0018CiSHaIH9g07yu)

While the n=9 computation runs, let me study the primary literature for relevant structural results.

## Output 229 (msg_1fae92e300017g3L0MH8orr5SE)

Key finding already: W9 is a genuine local trap (unique F-optimal comparison, one max-F child with π=2). Let me study the Peczarski paper while the full reachability computation runs.

## Output 249 (msg_1fae98738001JO4qo1ZZaxSN9O)

I've derived an important theoretical link. Let me check the computation progress.

## Output 287 (msg_1faeaec60001WgXBSGu6BIZKF0)

Let me record the rigorous deduction in scratch while the computation finishes.

## Output 307 (msg_1faeb3938001HueBvezY5owgKA)

Let me independently verify the W9 trap with a second from-scratch implementation (different data structures, no canon).

## Output 325 (msg_1faebc6ce001E88HvKlH1tG71B)

Independent verification confirms the W9 trap. Let me check the full A9 computation.

## Output 363 (msg_1faec54ef001q61PMKBDSi6R0o)

Let me run a lighter pure-extension-count all-clean search to independently confirm n=9 steep-freeness.

## Output 478 (msg_1faee050e001QuNc5sMSszGP0J)

Let me draft the board report while computations finish.

## Output 545 (msg_1faeef11d001C5DqL2ivdv7Pea)

n=9 all-clean tree confirmed (10684 states, 150s), which implies steep-freeness. Let me stop the redundant heavy computation and finalize.

## Output 608 (msg_1faef9fdc0014dde1EQ14IlFyV)

Now let me post the findings to board #301 as required by the research contract.

## Output 646 (msg_1faf02918001OhbtC6cyGaXilg)

## Result

**No counterexample found. The all‑n steep‑free claim is neither proved nor refuted; it is settled positively for n ≤ 9 and remains open from n = 10, especially at n = 12.** Worktree is clean, no Lean/repo/ledger changes; findings posted to board #301 at 21:49Z.

### What was established

**1. From‑scratch verification (n ≤ 8).** Exact minimax with transitive successor masks, subset‑DP extension counts, and 1‑WL + brute‑force canonicalization reproduced the known class counts (1, 2, 5, 16, 63, 318, 2045, 16999) and S(n) through n=8, and confirmed `T(A_n)=True`: steep max‑F paths exist from n=6 but a steep‑free optimal strategy always exists.

**2. n = 9 now settled.** A pure extension‑count all‑clean search found an all‑clean height‑19 tree for A₉ (10,684 canonical states, 150 s — consistent with the earlier unverified 9,875‑state claim). An all‑clean tree forces every step to drop b by exactly 1 on *every* path, so it is steep‑free. This independently confirms n=9 without needing full minimax.

**3. The n=9 witness is a genuine local trap — but not a counterexample.** Two independent implementations confirm W9 = `(0,0,1,2,10,11,26,59,95)` has e=173, b=8, F=8, eps=0 and **exactly one** F‑optimal comparison `(2,4)`, with max‑F children e=110 (π=1) and e=63 (π=2). So `T(W9)=False`: no avoiding comparison exists. But W9 is reachable only via a non‑max‑F outcome (the recorded certificate drops F 14→12), so the adversary never follows it. This is exactly the general‑poset vs. antichain‑reachability distinction.

**4. Paper‑proof deduction (soundness vs. completeness).** Along any max‑F path, `eps_t = eps_{t−1} + π_t − 1`, so with `N₀=#{π=0}` and `E₂=Σ_{π≥2}(π−1)`, we get `N₀ = eps(P₀) + E₂`. Since a π=0 step uses a nonclean comparison, every strategy's G‑score satisfies `G_σ ≥ eps + E₂`. Hence:

- **(A)** If *every* height‑S(n) strategy has a steep max‑F path, then `Δ(n)=G(A_n)−eps(A_n) ≥ 1` — a necessary condition linking this front to the exhausted root‑excess front.
- **(B)** If `Δ(n)=0`, a G‑optimal strategy has `E₂=0` on every path, hence is steep‑free.

The converse of (A) fails: extra nonclean steps can come from off‑path siblings. Kraft/clean counting is sound but not complete for steep‑freeness.

### Failed approaches / exact obstruction

- Exhaustive minimax at n=12 is infeasible here (the full n=9 run required ~650 MB and was stopped as redundant once the lighter all‑clean route settled it); n=12 has no tractable exact search with current resources.
- Ordinal‑sum amplification does not transfer: for `P=A⊕B`, `e=e(A)e(B)` and `b=b(A)+b(B)−δ` with δ∈{0,1}, so an internal drop shifts by at most 1, and such states are not antichain‑reachable (board 18:55Z, 21:02Z).
- A tempting shortcut ("L(n)=0 forbids steep steps") is **false** — the n=6 steep path already refutes it; steep steps are repaid by later π=0 steps, not forbidden.

### Honest limits

No new theorem about S(n) or SORT‑BOUND‑U; no complexity‑class consequence. n=10,11 were not attempted (prior all‑clean search was OOM‑killed); n=12 (first information‑loose case, eps=1) remains the decisive open case, and any counterexample there must satisfy Δ(12)≥1 by (A). The all‑n status is not resolved.

## Output 658 (msg_1faf05c00001394qR0Nbc3lyxm)

I’ll audit the prior run’s durable state first: repository status, the recorded board post, and any still-running scratch processes. I won’t repeat any external action that already completed.

## Output 681 (msg_1faf07d97001KHNcRWk50bM9uN)

Recovery audit complete. The prior work finished; no further side effects are needed.

- **Board #301:** The finding is already posted once, at 21:49:43Z. I did not repost it.
- **Repository:** On `billy-dev`, clean worktree at commit `6a96398`; no commit or repository change.
- **Scratch computations:** No related processes are still running.
- **Ledger:** The front remains marked `running`. I left it unchanged rather than infer authorization to update task records.

The previous report’s conclusion stands: steep-free strategies were confirmed through n=9; the all‑n question remains open, with no counterexample found.
