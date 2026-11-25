# antonina-GJ1IjKWZes9nDHmfpngVIi-followers

Session: ses_df6874459ffecSmiVuT3ZUL71b
Workspace: /home/lubko/soring-fronts/reachable-depth-two-profile-f-completeness-alln
Created: 1795455237086; updated: 1795461640095

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_20978bd58001gjzc14BzaIDLSG)

I'll start by exploring the repository structure and understanding the context, including what "billy-dev" refers to.

## Output 17 (msg_20978d2c00015OVnxuSYtyBTqw)

I'm on branch `billy-dev`, working tree clean. Let me study the key documents and find board #301.

## Output 45 (msg_20978e7fa001RsAHiMfkEk8KbL)

Let me look at the research board #301 digest and the AGENTS.md file directly.

## Output 56 (msg_20978fd160014mkh0uICW3sOu3)

Let me query the research board for entries relevant to this front.

## Output 67 (msg_209791223001ciGTKYPwXEcIe5)

Let me search the board specifically for this front and related keywords across pages.

## Output 78 (msg_2097a2eb3001WKOxTnMddu0fqz)

I need the full text of the key prior results. Let me fetch the full board JSON and extract complete message bodies.

## Output 114 (msg_2097a934b0014SyDcahXwpyAGf)

I now understand the commissioned front and the prior results. Let me check whether a general "defect-0 reachable states are information-tight" theorem is already on the board, and read the e-count-tie result.

## Output 134 (msg_2097c6a180012RKI8fJasemgpc)

There's a prior post that seems to touch this. Let me read it fully to check for consistency with a theorem I'm deriving.

## Output 152 (msg_2097cb53f001yCRyrLQP3BHu9e)

I have a promising structural theorem. Let me first rigorously check it computationally and compute the depth-two profile for the n=7 counterexample pair. I'll write from-scratch code.

## Output 170 (msg_2097d21d5001qWmqBuGMXNrcpA)

Key finding: M2 strictly separates the n=7 M1-counterexample pair. Let me now verify my structural theorem computationally and search for M2-conflicts. I'll write efficient C++ from scratch.

## Output 999 (msg_209ccd80a0012kqUzWXaszQkGk)

No external side effects from this front: git clean, no board post for this slug, no commits. I can proceed. I need to finish the mathematical work. The C++ compile failed due to container gcc header issues; I can compute in Python (n<=7 is feasible with efficient enough code, or just check the key cases) or fix compile. Easier to use Python with a careful implementation. I also need the M2 n=7 full conflict search - n=7 all 6.1M posets in pure Python is slow, but maybe doable with pypy? Or optimize. Alternatively, compile with system headers via a different approach.

Let me try compiling with `-nostdinc` and providing needed headers, or find system gcc. Another option: use python and focus on the theorem (which is a paper proof) + the M2 counterexample separation I already have. The theorem is the main deliverable. Let me verify it computationally in Python for n<=6 reachable, and n=7 reachable. Also get n=7 M2 full conflict via Python with efficient bitmask DP - 6M states might take minutes, borderline. I'll do a targeted Python check.

## Output 1221 (msg_209d93374001LN8HvGE0r0FUbT)

## Audit (recovery, no external side effects)

- Host/repo: `billy-dev`, `/home/lubko/soring-fronts/reachable-depth-two-profile-f-completeness-alln`, branch `billy-dev`, HEAD `6a96398`, clean worktree (`git status` clean, no new commits). No prior board post for slug `reachable-depth-two-profile-f-completeness-alln` found on board #301 pages 1-3.
- Durable state: frontier ledger `~/.local/state/soringp1/frontier-ledger.json` has this front `running` (`agent_id=GJ1IjKWZes9nDHmfpngVIi-followers`, started 2026-11-23T… per ledger). I did **not** post to #301, commit, PR, or change repo files. Scratch only in `/tmp/opencode`.
- Prior art read (not duplicated): `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, `docs/operations.md`; board results `e-count-tie-optimal-move-barrier-alln` (Lemma D holds n=6, 154 keys), `lemmaD-cospectral-n7-20261123` (general M1 counterexample at n=7; R_7 has 3,044,007 states; that F=6 mate unreachable), `optimal-play-lemma-d-restricted-n7-20261123` (restricted Lemma D on R_7: 392 (e,M1) keys, 0 conflicts, accepted by Viche), `oneply-flatness-certificate-gap-alln`.

## Front

- Question: on height-`S(n)` optimal-play reachable states, does depth-two extension-count profile `M2(P)` determine `F(P)`? Does the n=7 general M1 counterexample admit any reachable M2-cospectral mate?
- Falsifier: two height-`S(n)` optimal-play reachable states with identical `(e,M2)` but different `F`.
- Complexity implication: M2-completeness on real `S(n)` state graph + polynomial-description extension-count oracle => poly-size complete certificate / faster exact evaluator for `S(n)` (oracle-relative; e is #P-hard in general). Reachable M2-cospectral pair blocks the bounded-depth extension-count certificate family on the real state graph. Soundness != completeness.

## Definitions (used explicitly)

- `P` finite poset on `n` labeled elements; `e(P)=#LE(P)`. `F(P)=0` if total, else `1+min_{i~j} max(F(P+i<j),F(P+j<i))` (minimax, numeric `n`). `S(n)=F(A_n)`.
- `M1(P)` = sorted multiset of `e(C)` over all 1-step children `C` (both orientations of every incomparable pair), as in Lemma D.
- `M2_struct(P)` = sorted multiset of `(e(C), M1(C))` over 1-step children `C` (structured depth-two profile).
- `M2_flat(P)` = sorted multiset of `e(G)` over all 2-step descendants `G` (grandchildren, flat).
- Refinement [deduction]: `M2_struct(P)` determines `M1(P)` by first projection, and determines `M2_flat(P)` as the sorted union of `M1(C)` components. Thus `(e,M2_struct)` refines `(e,M1)`; `(e,M1)` refines `e`.

## Mathematical findings

### 1) M2 separates the known n=7 general M1 counterexample (experiment, from scratch)

Using the exact counterexample from `lemmaD-cospectral-n7-20261123` (recomputed independently in `/tmp/opencode/m2_n7.py`; e by subset-DP, F by memoized minimax, transitive closure by Warshall; no repo artifacts):

- `P = succ [0x3e,0x0c,0x00,0x00,0x04,0x08,0x3e]`, `e=32, F=5`
- `Q = succ [0x3e,0x0c,0x00,0x00,0x0c,0x04,0x1e]`, `e=32, F=6`
- `M1(P)=M1(Q)=(4,4,14,14,16,16,16,16,16,16,18,18,28,28)` (confirms prior result)
- `M2_flat(P) != M2_flat(Q)`: first difference at index 44 in sorted 140-multiset, `P` has `7`, `Q` has `6`; P tail includes `10,10,10,10,12,12,12,...`, Q has `10,10,10,10,10,10,10,10,10,10,12,...` (full tuples computed; lengths 140).
- `M2_struct(P) != M2_struct(Q)`: e.g. P has child `(14,(2,4,6,6,7,7,8,8,10,12))` twice while Q has `(14,(2,6,6,6,7,7,8,8,8,12))` twice; P has `(16,(4,6,6,8,8,8,8,10,10,12))` while Q has `(16,(4,4,6,6,8,8,10,10,12,12))`, etc.

Thus this specific general-state M1 collision is **not** an M2 collision (neither flat nor structured). This refutes “M2 is no stronger than M1 on this witness”, but does **not** prove M2-completeness.

### 2) n=7 reachable R_7: no (e,M2_struct) conflict, by deduction from accepted restricted Lemma D (deduction + literature/board)

- `optimal-play-lemma-d-restricted-n7-20261123` (accepted by Viche 2026-11-23T16:44:55Z) reports: on R_7 (k-safe BFS, `k=S(7)=13`), `|R_7|=3,044,007`, 392 distinct `(e,M1)` keys, **0 conflicts**.
- Since `M2_struct` refines `M1`, any two states with identical `(e,M2_struct)` have identical `(e,M1)`, hence identical `F` on R_7. Therefore there are **0 `(e,M2_struct)` conflicts on R_7** (and also 0 `(e,M2_flat)` conflicts only if one additionally checks flat; but structured already suffices). 
- The F=6 general mate `Q` is not in R_7 (prior reachability argument: `e=32` at depth `d` implies `d >= ceil(log2(5040/32))=8`, viability `d+F<=13` forces `F<=5`). The reachable `F=5` witness `R` has the same `(e,M1,M2_struct,M2_flat)` as `P` and `F=5`, consistent with no conflict.

**Answer to the front’s n=7 subquestion:** the n=7 general M1 counterexample does **not** admit a reachable M2-cospectral mate in R_7; the unreachable F=6 mate is separated by M2 anyway, and restricted M2-completeness holds on R_7 as a consequence of restricted M1-completeness.

### 3) Small-n sanity / global status (experiment/deduction)

- `n<=6`: Lemma D holds globally over all posets (`e-count-tie-optimal-move-barrier-alln`, accepted), hence M2_struct/M2_flat also determine `F` globally by refinement. I also ran an independent reachable check: `n=6, S=10, reachable=73051` k-safe states, `(e,M1)` keys = 73, `(e,M2_struct)` keys = 73, 0 conflicts (`/tmp/opencode/check_m2_reachable.py`).
- `n=7` global: M1 has exactly 1 conflicting key (prior accepted result). M2 separates that known pair (finding 1). A **full n=7 global `(e,M2)` conflict census was not completed here**: C++ compile was obstructed by the container toolchain/header/sysroot layout (object compiled but link failed on libc_nonshared path; I did not spend further time fighting the environment). Python exhaustive enumeration over 6,129,859 states is expensive in this environment. Therefore I do **not** claim “no global n=7 M2 conflict exists”.

## Failed approach / obstruction

- **Failed/blocked computational attempt:** tried to compile `/tmp/opencode/verify_reachable.cpp` (from-scratch C++17) with the container-overlay `g++-14`; compilation succeeded to `.o` after include-path fixes, but linking failed because the toolchain expects absolute `/usr/lib/x86_64-linux-gnu/libc_nonshared.a` outside the ad hoc sysroot. This blocked the planned full n=7 `(e,M2)->F` conflict census. Not a mathematical obstruction.
- **Plausible theorem refuted locally:** I briefly considered “`D(n)=0 => every k-safe reachable state is information-tight`”. Python k-safe BFS at `n=6, D(6)=0` found `reachable=73051, defective(F!=ceil log2 e)=4440` (e.g. succ `(2,0,3,0,0,0)`, `e=120, L=7, F=8, d=2, d+F=10<=10`). So D(n)=0 does not force information-tightness on all k-safe reachable states; optimal-play reachability is stronger than k-safe reachability and must be treated separately.
- **Exact mathematical obstruction for the front:** M2 is a strict refinement of M1 and resolves the only known n=7 general M1 collision, but this is only evidence, not a completeness proof. The all-n M2-completeness question remains open. A proof would need a structural argument that depth-two extension counts determine minimax value on the actual `S(n)`-optimal-play state graph; a disproof needs an explicit reachable `(e,M2)`-cospectral F-split pair (none found for n<=6 globally, none in R_7 by deduction, n=7 global M2-census incomplete).

## Complexity/model caveats

- All computations are numeric `n`; unary input is `N=n+k+1` as usual. No claim about `SORT-BOUND-U` membership/separation, no NP/circuit lower bound, no new `S(n)` value. Extension counts `e(·)` are #P-hard on general posets (Brightwell–Winkler 1991), so any “M2 + oracle => faster evaluator/certificate” consequence is oracle-relative / conditional, and soundness of M2 as a lower-bound test is not completeness.
- “Optimal-play reachable” should be read carefully: k-safe (`d+F<=S(n)`) is necessary for being on some height-`S(n)` continuation but is weaker than being selected by an F-optimal move; the R_7 result cited uses the k-safe/optimal-play frontier as stated in prior accepted posts. My n=6 k-safe defective example is k-safe but not claimed F-optimal-reachable.

## Status

**Honest inconclusive on the all-n front, with a concrete finite separation of the known n=7 M1 counterexample by M2 and a deduction that R_7 has no (e,M2_struct) conflict.** No theorem completion for `S(n)` or `SORT-BOUND-U`. No repo/Lean/test/CI/ledger/main change. No board post made by me.
