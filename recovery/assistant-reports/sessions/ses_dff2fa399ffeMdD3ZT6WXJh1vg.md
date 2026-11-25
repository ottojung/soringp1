# antonina-s9CSxRuhWdifgaeFF4sl5D-antipathy

Session: ses_dff2fa399ffeMdD3ZT6WXJh1vg
Workspace: /home/lubko/soring-fronts/n23-exact-search-attack-alln
Created: 1795309984962; updated: 1795314122725

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 154 (msg_200d5bba7001rTKrFiKSGUZunL)

Now let me compute the known-value/information-bound table for the claims, and check the other repo scripts and board tooling.

## Output 228 (msg_200dbdce7001kNGMrhQdf0eiWF)

The helpers are validated by brute force (my hand-computed "expect" values in the sanity test were wrong; the DP agrees with brute force on random posets). Now the real run — bounded backward BFS from the antichain of 23 keys:

## Output 270 (msg_200e42efa001ZHf5rK1ip2hDac)

Continuing after the restart. Let me check where the wall script stands and restructure it to measure level counts first (with `e`-bucket computation as a separate, optional phase).

## Output 290 (msg_200e473d0001VvMIis2e4hv8op)

The `/tmp` got wiped on restart — I need to recreate the wall script (helpers already validated by brute force earlier).

## Output 324 (msg_200eb3eaa001RyfVAMA43HfNMO)

Level counts: level 1 = 506 states, level 2 = 127,512 (growth ≈ 252/level). Now let me (a) try the repo's closest existing exact evaluator at n=23, and (b) measure the information buckets for the measured levels.

## Output 361 (msg_200fc4b65001dY7soQbjqREpRx)

Even one `e_of_state` call on a level-1 state exceeded 120s — the DP must be exploding. Let me instrument it.

## Output 408 (msg_201059303001ORwACqOQGbdjxy)

Let me check the level-3 BFS run status and write the scratch report.

## Output 437 (msg_2010d8726001fmxs3sT7xcDTFB)

Level 3 completed: **21,322,840 states** at depth 3 (602s). Now update the report and post the result to the board.

## Output 464 (msg_2010ebabd001HlTLEyVOkqnsI9)

The board comment is posted. Here is the final report.

## 1. Studied
AGENTS.md contract, `docs/problem.md`, board #301 digest (`--recent 7`), `docs/research-plan.md`, `docs/research-obstruction-next.md`, `docs/literature.md`, `docs/research-certificates-barriers.md`, `docs/research-frontier.json`. No prior s23 computation of mine was found; I made no repo or Lean changes (scratch only in `/tmp/opencode/`).

## 2. Known values and what is open about S(23)
From literature (`research-certificates-barriers.md` + OEIS A036604): `S(1..22) = 0,1,3,5,7,10,13,16,19,22,26,30,34,38,42,46,50,54,58,62,66,71` (S(13)=34 Kasai; S(15)=42, S(19)=58 Jing; S(16)=46, S(17)=50, S(18)=54 Stober–Weiss 2023). **S(23) is open** (OEIS lists through 22; Knuth errata: n=23 open). Lower bound: `C(23) = ceil(log2 23!) = 75` (23! = 25852016738884976640000, log₂ = 74.453), so `S(23) ≥ 75`.

## 3. Claim attacks (precise all-n falsifiable claims; seriously tried to disprove)
- **Claim A: "S(n) ≥ C(n) + 1 for all n ≥ 13" → FALSIFIED.** Counterexamples from the literature value table (C(20)=62, C(21)=66 verified numerically): **S(20) = 62 = C(20)** and **S(21) = 66 = C(21)** (gaps S(n)−C(n): 1,1,1,1,1,1,1,0,0,1 for n=13..22).
- **Claim B: "S(n) ≤ C(n) + 1 for all n ≥ 13" → survives on all literature data** (gaps ≤ 1). **Honest limit:** a disproof needs the exact S(n) for some n ≥ 23 or a new structural argument; see §4 — the state-count wall shows no feasible computational route to decide S(23).

**Soundness vs completeness (general-poset vs certificate):** the Hanamura–Iwata result (e(P) ≤ 7 ⇒ sortable in 3) is a *sound general-poset base* — no poset with ≤7 extensions lacks a 3-comparison sort, and this holds for every n. The wall shows the *completeness* of the search is what fails at n=23: the backward search must reach depth ≥ 75 and the measured state population explodes by depth 3.

## 4. S(23) front: state-count wall of the backward search
Bounded backward BFS from the antichain P₀ of 23 keys (state = poset on 23 labelled keys as a transitively-closed bit matrix; expansion: add one incomparable pair {a,b} in both orientations — the AND-OR state space of `Sortable(P,k) = ∃{a,b}: Sortable(P+a<b,k−1) ∧ Sortable(P+b<a,k−1)`). Script: `/tmp/opencode/s23_backward_wall.py`; full log `/tmp/opencode/wall_l3.out`.

**Information buckets** (e(P) = #linear extensions): root = "hard" (e = 23! > 2^74: the info bound does not fire at k=74); level-1 states: e = 23!/2 ≈ 1.29e22 ≤ 2^74 → "auto"; level-2 states: e ∈ [23!/4, 23!/3] ≈ [6.5e21, 8.6e21] ≤ 2^74 → "auto"; "base7" bucket: 0 at depths ≤ 3 (e ≥ 23!/6 ≈ 4e20 ≫ 7); total: 0 at depths ≤ 3.

**Measured wall:**
| level | states | growth |
|---|---|---|
| 0 | 1 (P₀, hard at k=74) | — |
| 1 | 506 | — |
| 2 | 127,512 | 252.0/level |
| 3 | **21,322,840** | 167.2/level (602 s) |
| 4 | projected ≈ 3×10⁹ (not enumerable feasibly) |

The search must descend to depth ≥ 75 (S(23) ≥ C(23) = 75). Even level 4 at ≈3×10⁹ is far beyond feasible exact searches at n=18 (Stober–Weiss took 89 h for S(18)=54). The e ≤ 7 base (Hanamura–Iwata) becomes usable only at depth ≳ 72 (posets with d relations have e ≈ 23!/2^d; 23!/2^72 ≈ 2.7 ≤ 7) — i.e. the search cannot use it on the way down. **Repo's closest method:** `scripts/evaluate.py` (exact poset minimax DP) at n=23: no output after 120–150 s (killed); sanity: it computes S(6)=10 correctly.

## 5. Honest limits
- **S(23) is not advanced.** The wall is an *obstruction of the backward-search method at n=23* (specific form: "the backward search needs ≈21.3M states at depth 3 and ≈3×10⁹ at depth 4 against a needed depth of ≥75 — infeasible by state counts").
- The wall is a bounded measurement (depths 0–3); it is not a proof that no smarter search exists.
- Disproof of Claim B is not computable here without exact S(n) for n ≥ 23.
- Result posted to board #301; nothing created in the repo or Lean.
