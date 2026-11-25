# antonina-jRZ2Or27XrdCLX2UXmUJTc-glaring

Session: ses_e01147a62ffe93UpoH5z2gpVZ9
Workspace: /home/lubko/soring-fronts/antichain-superadditivity-minplusone-alln
Created: 1795278210505; updated: 1795279380468

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_1fef2f4ca001JBMUwcNBH7jl2N)

I'll start by carefully inspecting the current state, since the previous turn may have performed side effects. Let me gather information in parallel.

## Output 28 (msg_1fef307f5001kcohJDcSDb5cs6)

I'm on `billy-dev` with a clean working tree. Let me locate the board #301 and durable task records, and read the core docs.

## Output 47 (msg_1fef31842001o72SEvD3lq9Xk7)

Let me check the board digest, the durable ledger, and any prior work/side effects from the interrupted turn.

## Output 62 (msg_1fef3370c001E6fLLkNZhLNV5g)

Let me read the primary literature doc, the relevant prior research notes, and the full T1 finding from the board.

## Output 77 (msg_1fef398f1001IYDVTy232XneJ5)

Let me check for prior scratch work and the board script options to read full findings.

## Output 124 (msg_1fef406cf001lbsXsT5Pj3kU41)

Let me read the structural lower bounds notes and search the primary literature for the superadditivity theorem.

## Output 139 (msg_1fef468ad001i8qQhzRb82vC6Y)

Web search is unavailable; I'll use direct fetches and local computation. Let me get authoritative S(n) values and check the literature directly.

## Output 198 (msg_1fef6b51c00158vX1z4SsNrksb)

Let me test whether the information bound plus a rigorous mergesort upper bound already proves the claim for a large range of splits.

## Output 209 (msg_1fef7178d001Pfd7qlqv4dmyIG)

Let me get the Ford–Johnson upper-bound values to test whether known bounds can settle all splits.

## Output 256 (msg_1fef94188001YU2gHy1S0fkdlM)

I have a genuine new result. Let me verify the posting mechanism and check for any prior post on this exact front before writing to the board.

## Output 310 (msg_1fefbbd07001jS7n1skvXRGqm1)

I've established a genuine new result. Let me record the finding in scratch and post a concise report to board #301 (no prior post covers this front).

## Output 337 (msg_1fefc82c2001wZojDxfaLJdOwX)

The post is live (verified at 16:42:03Z). Let me create the referenced reproducible scratch script and confirm the worktree is untouched.

## Output 355 (msg_1fefccfdb001Z3mQY89c3Keu5N)

## Report — antichain-only defect inequality (billy-dev)

**Claim attacked.** For all \(a,b\ge 1\), \(a+b\ge 3\): \(S(a+b)\ge S(a)+S(b)+\min(a,b)+1\).

**Recovery check first.** Inspected git state (clean, `billy-dev`, HEAD `6a96398`), reflog, ledger and board before acting. The latest prior posts (16:29–16:31Z) concern the *general* defect \(F(C_a\sqcup B)\) and the potential-route no-go; nothing covered this antichain-only front, so no side effect was duplicated.

### Mathematical finding

- **No counterexample exists within any certified range.** Exhaustive check of every split with \(a+b\le 22\) (exact values from OEIS A036604 / Stober–Weiss): the inequality holds for all \(a+b\ge3\); the only violating pair is the excluded \((1,1)\). Tight cases are \((1,2),(1,3),(2,2),(1,4),(2,3),(3,3)\) and reverses. Published explicit sorters (Ford–Johnson count \(F(a+b)\)) never fall below the target, so no known upper bound refutes the claim; for \(a+b=23\) the information bound alone (75) already exceeds the largest split target (68).

- **New unconditional theorem (finite range), from literature bounds + exact integer computation.** With \(C(n)=\lceil\log_2 n!\rceil\le S(n)\) and the Ford–Johnson upper bound \(F(n)=\sum_{k=1}^{n}\lceil\log_2(3k/4)\rceil\ge S(n)\) (Knuth 5.3.1 / OEIS A001768), and exact \(S\) for \(n\le22\), define \(U(n)=\min\)-safe upper bound. The exact-integer check \(C(a+b)\ge U(a)+U(b)+\min(a,b)+1\) holds for **every split with \(3\le a+b\le50\)**, hence the claim is *proved* on that range — extending the certified range from 22 to 50 using only published bounds. For balanced splits \(a=b\) it holds for every \(a\le5000\) checked (slack grows \(\approx0.87a\)); it likewise holds when the two sides are within a factor of ~100. Script: `/tmp/opencode/antichain_defect_check.py`.

### Exact obstruction to the all‑\(n\) claim

- The sufficient condition provably **fails first at \((a,b)=(1,50)\)**: \(C(51)=220 < U(1)+U(50)+2=221\). Then it fails at every \((1,b)\), \(b\ge50\), and first at \((2,104),(3,196),(4,211),(5,250),(6,398)\). So the residual open region is *extremely unbalanced* splits; any proof there needs a lower bound on \(S(a+b)\) strictly stronger than leaf counting — the information bound plus the best general upper bound known (Ford–Johnson) cannot reach it.
- Necessary-but-insufficient fact re-derived: fixing internal orders, only cross comparisons distinguish the \(\binom{a+b}{a}\) interleavings, forcing \(\ge\lceil\log_2\binom{a+b}{a}\rceil\ge\min+1\) cross comparisons on some path. This cannot be added to \(S(a)+S(b)\): a cross comparison plus an existing relation creates new within-group relations by transitivity (blue \(x<\) red \(y<\) blue \(z\Rightarrow x<z\)), so cross comparisons sort inside groups "for free." This is the same transitivity coupling that closed the general-\(D\) potential routes.

### Honest limits

The all‑\(n\) claim is **neither proved nor refuted**. The \(n\le50\) result is finite-range and uses no new algorithm; it yields **no new uniform complexity result** for evaluating \(S(n)\) and no class membership for `SORT-BOUND-U`. No general-poset hardness or certificate soundness was conflated with completeness. No Lean/repository/CI/main/ledger changes were made; worktree remains clean.

A concise finding was posted to board **#301** at 16:42:03Z (verified), with `--json` redirected to a file as required. `S(n)`, `SORT-BOUND-U` and general \(D\) remain open.

## Output 380 (msg_1fefd309a001J9I59b17gxHyiu)

**Recovery inspection (no repeated side effects).**

- **Git/worktree:** `/home/lubko/soring-fronts/antichain-superadditivity-minplusone-alln` is clean on `billy-dev` at `6a96398`. No commits, PRs, Lean/repo changes, or ledger/main changes.
- **External side effect already performed:** board #301 comment exists and was verified: `[2026-11-21T16:42:03.436Z] SoringP1 researcher: exec-antichain-defect-infofj-20261121`. I did **not** repost it. Post stderr was empty; JSON output was redirected to `/tmp/opencode/antichain_defect_post.json`.
- **Durable/scratch artifacts present:** `/tmp/opencode/antichain_defect_finding.txt`, `/tmp/opencode/antichain_defect_check.py`, `/tmp/opencode/antichain_defect_post.{json,err}`. The check script runs and reproduces the finite-range result and first failure.

**Already-completed work (not repeated):** attacked the antichain-only defect front \(S(a+b)\ge S(a)+S(b)+\min(a,b)+1\), \(a+b\ge3\). No counterexample found in certified ranges. Proved the claim for all splits with \(3\le a+b\le 50\) by exact-integer check using published bounds \(C(n)=\lceil\log_2 n!\rceil\le S(n)\le U(n)\) (exact \(S\) for \(n\le22\), Ford–Johnson \(F\) otherwise). Identified the precise obstruction: the cheap info+FJ sufficient condition fails first at \((1,50)\) (\(C(51)=220 < 221\)) and on extremely unbalanced splits; a cross-comparison count \(\ge\lceil\log_2\binom{a+b}{a}\rceil\ge\min+1\) is necessary but cannot be added to \(S(a)+S(b)\) because cross comparisons create within-group relations by transitivity.

**Unfinished/open:** the all-\(n\) antichain defect inequality remains **unproved and unrefuted**. No new uniform complexity result for \(S(n)\)/`SORT-BOUND-U` was obtained; no further external action is pending from this turn.
