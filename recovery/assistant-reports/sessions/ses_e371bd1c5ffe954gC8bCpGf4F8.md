# antonina-zjVQRmitlypy9hQ2fIt5jo-hide

Session: ses_e371bd1c5ffe954gC8bCpGf4F8
Workspace: /home/lubko/soring-fronts/disjoint-union-defect-20261111
Created: 1794371759738; updated: 1794382620982

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 437 (msg_1c989565a0012MbXa7clgvcxdR)

**Prior-state / side-effect check (no duplication):** Started in an empty, non-git cwd (`/home/lubko/soring-fronts/disjoint-union-defect-20261111`, only created during this run). Found a read-only SoringP1 reference at `/home/lubko/soring301-new-surplus-parameter-20261022` (docs/scripts) but made **no repo/Lean/PR/workflow changes**. Attempted to inspect issue #301 for any prior post to avoid duplication: `gh` in PATH is a browser-opener shim (v0.0.4, not GitHub CLI), real `gh` binaries exist under `/gnu/store/*github-cli*/bin/gh` but are unauthenticated (`gh auth login`/`GH_TOKEN` required), and `lubko-board` reports removed; no GitHub token/config found in env or `~/.config/gh`. I could not view or post to #301, so **no external post was made/duplicated** (posting remains uncertain from this environment and must be reviewed).

**Computation completed (scratch only).** Exact exhaustive study for disjoint-union defect `δ(A,B)=F(A ⊔ B)-F(A)-F(B)` vs bound `b(A,B)=min(|A|,|B|)+1`.

- **Model/defs:** Poset = transitively closed strict partial order on `[n]`, successor bitmasks (`succ[i]` has bit `j` iff `i<j`). `F(P)=0` if total else `1+min_{i‖j} max(F(P+i<j),F(P+j<i))` (`S(n)=F(∅)`; cf. `docs/problem.md`/`SoringP1/Model.lean`). `A ⊔ B` = disjoint union on `|A|+|B|` with B block shifted (`list(A)+[m<<|A| for m in B]`), no cross relations. Margin `m=δ-b`.
- **Enumeration:** Unlabelled posets as isomorphism classes via refined-colour lex-min canonicalization over reachable states (`quotient_classes`), A000112 counts reproduced n=0..8 → 1,1,2,5,16,63,318,2045,16999. All unordered-by-component-size class pairs `(A,B), 1<=|A|<=|B|, |A|+|B|<=8`: **3933 pairs** (splits: (1,2):2,(1,3):5,(1,4):16,(1,5):63,(1,6):318,(1,7):2045,(2,2):4,(2,3):10,(2,4):32,(2,5):126,(2,6):636,(3,3):25,(3,4):80,(3,5):315,(4,4):256). `genposetg`/`digengraph` not found; own enumeration.

**Result (boundary evidence, no all-`n` claim):** **No violation found.** `δ(A,B) >= min(|A|,|B|)+1` holds for every checked pair (`3 <= |A|+|B| <= 8`).
- Minimum defect overall: `min δ = 2`. Violations: **0** / 3933. Tight (`m=0`, `δ==b`): **38**.
- Margin distribution `m=δ-b`: `0:38, 1:2690, 2:1097, 3:108`.
- Min defect by total size s=3..8: `2,2,2,2,2,3` (max observed δ up to 7 at s=8).
- Min (δ,m) by split: (1,2):(2,0),(1,3):(2,0),(1,4):(2,0),(1,5):(2,0),(1,6):(2,0),(1,7):(3,1),(2,2):(3,0),(2,3):(3,0),(2,4):(4,1),(2,5):(4,1),(2,6):(4,1),(3,3):(4,0),(3,4):(5,1),(3,5):(5,1),(4,4):(6,1).
- **Witnesses (exact, bitmask class reps):** min-defect/tight examples include (1,2): `A=(0,),B=(0,1),F=0,0,2,δ=2,b=2` and `B=(0,0),F=0,1,3,δ=2`; tight with min>=2: (2,2) e.g. `A=(0,1),B=(0,1),F=0,0,3,δ=3,b=3` / `A=(0,1),B=(0,0),F=0,1,4`; (2,3) e.g. `A=(0,1),B=(0,0,2),F=0,2,5,δ=3,b=3`; (3,3) e.g. `A=(0,0,2),B=(0,0,2),F=2,2,8,δ=4,b=4`. (Decoding: `(0,1)` 2-chain, `(0,0)` 2-antichain, `(0,0,2)` 3-poset with `2<1`.) **No disproof pair found.** Not extended to 9–10.

**Solvers & cross-check agreement (two exact implementations):**
- **S1 (labelled-state memo):** plain minimax from a state with memo keyed by reachable successor-bitmask tuples (`F_plain`).
- **S2 (iso-canonical quotient DP / class table):** same recurrence but every state canonicalized to refined-colour lex-min representative, giving `class_rep -> F` for all classes of size n and `F(P)=table[canon(P)]` (`quotient_classes`/`make_refined_canon`).
- Agreement: spot cross-check S1 vs S2 on **168** class representatives across n<=7 (all for n<=5, 40 random each for n=6,7): **0 mismatches**. Per-union S1 spot checks during pair scans (1 in n<=7 run, 4 sampled in n<=8 run): **0 mismatches**. S2 reproduced A000112 counts for n<=8 exactly. Transitive closure/extend and disjoint-union shift consistent with `scripts/benchmark_symmetry_quotients.py` / `scripts/parallel_module_probe.py`.

**Code paths / artifacts (scratch, cwd only):**
- `solve_fast.py` — main enumeration + pair scan + S1 spot checks (runs: `python3 -u solve_fast.py 7/8`)
- `solve_defect.py` — heavier per-pair S1 variant (superseded)
- `fast7.log`, `fast8.log` — full outputs
- `report_issue301.md` — ready-to-post comment body with full details (definitions, scope, witnesses, cross-checks, limits, blocker)
- Read-only refs consulted: `/home/lubko/soring301-new-surplus-parameter-20261022/docs/problem.md`, `docs/research-plan.md`, and script patterns in `scripts/benchmark_symmetry_quotients.py`, `scripts/parallel_module_probe.py`.

**Posting blocker (cannot satisfy "post ONE comment to #301"):** No authenticated GitHub posting mechanism available here (PATH `gh` is non-CLI shim; store `gh` CLIs unauthenticated; `lubko-board` removed; no token). The full intended #301 comment is prepared in `report_issue301.md`. Per instructions, reporting blocker with prepared content; **no #301 post was made**. (Nonzero completion condition applies because the required post could not be completed.)
