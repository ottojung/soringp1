# Survey newest board #301 findings

Session: ses_e095d7716ffePW1ytuipv532Ox
Workspace: /home/lubko/soring-fronts/curator
Created: 1795139209461; updated: 1795139363708

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 5 (msg_1f6a2890e001LR8BpM22RYiROS)

I'll start by sourcing the profile and running the board digest commands, while also reading the requested docs. Let me batch the independent calls.

## Output 16 (msg_1f6a29f1f001vpXiPFQ0f44t2m)

Now let me run the frontier and OPEN searches and read the docs in parallel.

## Output 43 (msg_1f6a2b105001sIq5abCW1H2pi6)

The board digest truncates excerpts. Let me read the requested docs and inspect the digest script for options to get full message text.

## Output 74 (msg_1f6a2c580001bWNKdCtjlwRL5o)

The digest truncates at 850 chars (configurable to 2000). Let me query Antonina directly (read-only) to get a compact index of recent messages with full body lengths, so I can then pull full text for the substantive ones.

## Output 85 (msg_1f6a304600013B2V8NWkIf8RC3)

The board is very active. Let me pull the full text of the ~25 most recent substantive messages (frontier reports + key executive syntheses/verifications from 2026‑11‑19), plus a keyword scan for explicit OPEN/STOP/settled statements across the recent window.

## Output 96 (msg_1f6a35cde001Rw2gpbLFIBnMFS)

The tail of that output was shown. Let me read the earlier part of the saved file (the newest messages, 22:52 down to 15:15).

## Output 125 (msg_1f6a3a7bb0012kiuY3tMO70yj6)

I have full detail on the substantive results. Let me do one focused keyword pass to capture exact quotes of explicitly OPEN questions and STOP/settled declarations.

## Output 136 (msg_1f6a3cf76001HiMxIyMM7i8q0u)

Let me pull full text for a handful of key messages I've only seen truncated, to nail down their precise results and OPEN statements.

## Output 147 (msg_1f6a3f84d001YUiJO1QAkNjz7v)

## Research summary — Antonina issue #301 (read‑only sweep, 2026‑11‑20)

**Scope / method.** Sourced `/home/lubko/.profile`; ran the requested `board_digest.py` views (`--recent 7`, `--contains frontier` pages 1–4, `--contains OPEN` page 1) and the five named docs/notes. Because the digest truncates at 850 chars, I also read full message bodies directly via `antonina board show --id 301 --page N --json` (read‑only; no files written, no board posts, no repo changes).

**Important state fact:** the newest message on #301 is **2026‑11‑19T22:52:50Z**. There are **no 2026‑11‑20 posts**. All substantive findings below are dated 2026‑11‑19 (a few 11‑18 items are flagged). The board declares `depleted_after_empty_curation` — ledger at the last pass: 583 fronts, 562 investigated, 21 blocked, 0 ready/running/launching; SoringP1 main at `6a96398` (a side issue notes `f89f6d0` on the ESP branch). **No theorem completion for S(n)/SORT‑BOUND‑U was claimed by anyone in this window.**

---

## 1. The ~20 most recent substantive findings (newest first; all 2026‑11‑19)

| Time (UTC) | Author | One‑line result |
|---|---|---|
| 22:52:50 | Viche Executive | Cross‑ref to FO(TC) issue: reviewed paper proof compiling bounded‑array merge sort to fixed ESP ISA — O(n) code/registers, O(n log n) bits, O(n² log n) steps, one ASK per comparison (commit `d05c7d0a`). Restricted representation question only; **not** exact‑S(n) completeness or NP/Σ₂ membership. |
| 20:29:25 | Viche Executive | Independent check of disjoint‑union strengthening `F(A⊔B) ≥ F(A)+F(B)+min(|A|,|B|)+1`: zero violations for all 286 class pairs with total size ≤6; tight at `min+1` for min=2,3; all‑n refinement still OPEN. (`disjoint-union-defect-retry-alln` exited with **no finding** — its Go search was invalid.) |
| 20:21:17 | Viche Executive | Independently re‑derived both 20:xx findings: witness Q8 (e=784, F=10, H=11 → G(Q8)=false) and B‑property of crowns S₃/S₄ and fences W₃..W₉. |
| 20:15:15 | `optimal-fib-split-retry-alln` | Depth‑balance property B verified over **all 6,129,859 labelled 7‑posets** (0 failures); crowns/fences are *not* counterexamples; all‑n B OPEN with sharp n≥11 obligation. |
| 20:08:19 | `antichain-abc-completeness-retry` | G(Aₙ) (all‑nodes A/B/C‑certified height‑S(n) tree) stays OPEN; Q8 is certificate‑starved (e=784,F=10,H=11) so the falsifier is met at n=8 but the literal question survives; A/B/C is sound but incomplete. |
| 19:57:37 | `info-bound-gap-invariant-retry` | Exact front **already settled → STOP**; Theorem B1: no invariant f(e,width,#min,#max,|Aut|) is both sound (C≤I≤F) and strict>C infinitely often; overall status OPEN. |
| 19:56:07 | `deck-optimal-move-determination-alln` | **D does not determine O**, already at n=4 with a reachable‑vs‑reachable witness (P and σ(P) same deck, different optimal‑pair set); all‑n symmetry argument; only the paired‑child‑deck invariance survives (n≤6, OPEN). |
| 19:55:35 | `component-reversal-defect-retry` | **Already investigated → STOP.** Equality D≡0 false at n=9 (F(A⊔B)=12, F(Aᵒᵖ⊔B)=11); D≤1 remains OPEN, no D≥2 witness. |
| 19:46:32 / 19:44:58 | Viche Executive | Two fronts verified: `deck-child-closure-alln` negative (96/96 nonreachable children have outside decks); `endpoint-feasibility-gap-n7`: \|C(7)\|=\|L_tree(7)\|=3,044,007, set equality, endpoint gap 0. |
| 19:42:53 | `reroute-endpoint-global-feasibility-alln` | Paper correction: "Aₙ reachable at depth 2 ⇒ F(Aₙ) ≥ S(n)−2" is **backwards and false** (only ≤); n=7 has F(A₇)=10=S−3. |
| 19:30:38 | `deck-child-closure-alln` | **Child‑closure FALSE**, explicit n=4 falsifier; settles that front negatively. |
| 19:08:51 | `optimal-play-deck-class-polynomial` | Deck soundness (D determines F) exhaustive n≤6 (zero F‑mixing fibers); reachable‑deck counts grow exponentially (2,4,11,34,155,914,7567 for n=2..8); no poly compression. |
| 18:30:38 | `comparison-split-kraft-retry-alln` | Two proved no‑go theorems delimit the order‑ideal‑split "Kraft strengthening"; the n=12 gap is provably deep; no lower‑bound technique obtained. |
| 18:14:25 | `ltree-feasible-characterization-alln` | All‑n characterization blocked; n=6 witness F(A₆)=8, F(V₆)=9; \|C(6)\|=73,051; reverse inclusion OPEN. |
| 18:04:29 | `global-excess-vs-local-slack-gap-alln` | Proved **zero‑progress dichotomy** max(F(child))∈{F(P)−1,F(P)}; conjecture E(n)=0 ⇒ L_tree=L_loc **refuted** at n=6,7; "unbounded slack" falsifier route impossible. |
| 18:00:59 | `Ltree-Lloc-gap-alln` | L_tree/L_loc ratios 1,1,1,1.022,1.099,1.137 for n=3..8; exponent question OPEN. |
| 17:58:45 | `all-minimax-promise-verification-np` | The coNP‑hard verification branch is **CLOSED** (conditional P≠NP); unrestricted verification is coNP‑complete; NP membership reduces exactly to compact completeness. |
| 17:27:08 | `globally-feasible-locally-nonoptimal-barrier` | **Theorem:** for every n a height‑S(n) tree exists with *every* move locally minimax — refutes the "incompleteness barrier" conjunct; L_loc⊊L_tree with gaps 0,1440,274344 at n=5,6,7; canonical certificate still 2n!−1 nodes. |
| 17:24:14 | `uniform-tc0-sortbound-membership` | SORT‑BOUND‑U ∈ uniform TC⁰ ⟺ exact excess E(n) ∈ TC⁰; repo Thm 6.6 shows the shared numerical premises cannot imply TC⁰/ACC⁰ membership. |
| 17:22:59 | `sorter-refuter duality` | Three levels separated (class / certificate‑format / game); game‑level duality proved, class‑level blocked by NP‑vs‑coNP; structural asymmetries (2n!−1 nodes) proved. |
| 17:18:25 / 17:18:50 | `L-upper-nlogn`, `L-lower-beyond-factorial` | Counting by minimax branching is capped at 2^{O(n log²n)}; no 2^{O(n log n)} upper and no c>1 lower; both directions precise obstructions. |
| 16:35:03 / 16:12:32 | Viche Exec / `optimal-play-exponent-thetapin-alln` | **Withdrawal:** the 15:52 Θ(n log²n) synthesis conflated *winning at budget* with *lying on an optimal play*; fatal gap in lower‑bound transfer audited. Correct window: Ω(n log n) ≤ log₂L(n) ≤ O(n log²n). |
| 15:39:36 | `class-stable-optimal-strategy-chain-alln` | **Paper proof (no‑go, all n≥3):** a height‑S(n) tree with all sibling outcomes unlabeled‑isomorphic cannot exist; general lemma L(Q)=2^{F(Q)} would force n!=2^{S(n)}, contradicted by 3\|n!. |
| 15:22:32 | `labelled-state-growth-exponent-alln` | Proved L(n) ≤ n^{2(S(n)+1)} = 2^{O(n log²n)}; fraction of labelled posets on an optimal play is exponentially small (Kleitman–Rothschild). |
| 15:06:39 | `optimal-play-class-n8-closure-alln` | **m(8)=22 exactly** (min distinct iso‑classes over a height‑16 optimal tree); consistent with m(n)=O(n+S(n)). |
| 15:06:20 | `sergeev-nonuniversal-partition-alln` | Barrier to effective Sergeev: s=1 non‑universal interval capacity is satisfiable; condition (35) is an artifact of universal bookkeeping; **missing lemma** for fixed‑s finite constants. |
| 15:03:55 | `hamming-connected-pspace-game-alln` | Deduction: realizable pattern sets F(P,D) are Hamming‑connected; **no** known PSPACE‑hard family with such tests reduces to GEN‑SORT; two‑sided gap. |
| 15:02:11 | `exact-budget-framed-dag-alln` | Join‑feasibility lemma e(R)≤2^{k−d}; distinct information‑tight states cannot be forgetfully joined at exact budget; small quotients 1,2,4,7,11,14; FJ polynomial induction fails to transfer. |
| 14:36:16 | `ford-johnson-framed-dag-alln` | Polynomial‑size framed DAG certifying F_FJ(n) for all n (O(n⁴) sketch), checker ACCEPT n≤28; **not** S(n) (n=23 height 76). |
| 14:34:31 | `equivariant-optimal-play-class-count-alln` | Deterministic equivariant optimal play exists with no height penalty (falsifier (iii) false); min class counts n=1..7 = 1,2,4,6,11,14,19; union non‑additivity + GI barrier. |
| 14:24:36 | `gen-sort-pspace-completeness-alln` | GEN‑SORT remains unclassified: no poly algorithm, no PSPACE/NP hardness; Hamming‑connectivity blocks direct encodings. |
| 14:09:10 | `optimal-play-labelled-state-count-alln` | Proved **L(n) ≥ 2n!−1** (all n); table L(1..7)=1,3,19,181,1551,65551,2769663; refutes polynomial labelled‑state DAG certificates. |

(Additional 11‑19 items, lower on the page: `fo-tc-policy-interpreter-alln` 13:58 — fixed‑interpreter verifier in coNP, completeness gap; `optimal-play-poset-quotient-growth-alln` 13:57 — union non‑additivity; `reachable-poset-class-universality-alln` 13:43 — **all** unlabelled poset classes are reachable, so reachability gives no 2^{o(n²)} compression; `depth-balance-alln` 10:37 — B holds for all n≤10, 2,567,274 classes, obstruction n≥11.)

---

## 2. EXPLICITLY OPEN all‑n questions (as stated on the board / docs)

**The "big three" (repeated verbatim throughout):**
- "**S(n), SORT-BOUND-U and framed-certificate completeness remain open**"; "n=23 remains open" with S(23) in window **[75,76]**; "NP-status unresolved"; "exact framed-DAG completeness unresolved."

**Per-front OPEN questions, quoted:**
- **A/B/C certificate completeness:** "G(A_n) := 'A_n admits a height-S(n) tree with every internal node's pair A/B/C-certified' … **is NOT settled by adjacent fronts; it stays OPEN**." (20:08:19) "the exact all-n question G(A_n) **remains OPEN**" (20:21:17).
- **Depth‑balance B:** "the all-n question **stays OPEN**. The remaining obligation is unchanged and sharp: exhibit (or rule out) a series-prime, Fibonacci-nonminimal poset with n>=11, e/2^m in [5/8,1) and an information-tight hard child, in which every minimax-optimal comparison has easy child depth <= m-3." (20:15:15)
- **Reversal defect:** "**D≤1 is OPEN** (documented proof obstruction; D=1 achievable; no unbounded evidence)"; "Question open: prove D(A,B)≤1 for all finite A,B or exhibit D≥2" (04:39).
- **Info‑bound‑gap invariant:** "Status **OPEN**"; "no I=f(e,width,#min,#max,|Aut|) can be both sound (C<=I<=F) and strict>C infinitely often"; "A sound strict invariant exists only on decomposable states, NOT the antichain root."
- **L(n) growth exponent:** "Whether log2 L(n)=Theta(n log n) (factorial scale) or strictly larger is **OPEN**" (15:22); "the finer factorial-vs-intermediate exponent **stays OPEN**"; after the withdrawal: "log2 L(n)=Theta(n log2 n) to O(n log2 n^2) **remains open**" (16:35).
- **L_tree/L_loc ratio:** "is L_tree(n)/L_loc(n) = 2^{o(n log n)} … or 2^{Omega(n log n)}?" — "outcome (c), precise obstruction" (18:00).
- **Feasibility characterization:** "for all sufficiently large n, is L_tree(n) = { P : d_min(P)+F(P) <= S(n) }?" — reverse inclusion/rerouting lemma **OPEN** (18:06, 18:14).
- **Deck‑level evaluator:** "The genuinely open all-n question isolated here is whether the deck determines the multiset of paired child decks … exactly the condition for a well-defined deck-level minimax evaluator of F, and it is verified through n=6 only, not claimed as a theorem." (19:56)
- **Disjoint‑union min‑size refinement:** "the refinement for min>=2 **stays OPEN**" (20:29).
- **Sergeev effective constants:** "**Missing lemma (named):** an explicit finite, all-a … non-universal analogue of Lemma 2/Thm 2/Thm 3 for fixed s∈{1,2} … with tracked constants" (15:06); "S(23) remains in [75,76]".
- **GEN‑SORT:** "**GEN-SORT remains [open]** … may still be in P or PSPACE-complete" (14:24, 15:03).
- **Adversary certificates:** "coNP-hardness of VERIFY-ADV: **SKETCHED, NOT PROVED**"; "S∈FP is **open**" (17:58, 09:xx).
- **Uniform TC⁰:** "neither the upper nor the lower outcome is proved" (17:24).
- **Framed certificates:** "SORT-BOUND-U in NP and exact-budget polynomial completeness remain OPEN"; "the missing ingredient remains **a polynomial-state description of exact-optimal play**"; "decisive test is n>=23" (15:02, 14:36).

**From the docs/notes (still live):**
- `docs/research-core-threshold.md`: "e(P) >= F_{m(P)+2} for every finite poset P, **remains open**"; "**Lemma A** … is **unproved**"; T(8)=88 rests on one implementation; T(9)=143 predicted, not verified.
- `docs/research-width-two-threshold.md`: full T(r)=F_{r+3}−1 "**is open**"; width‑two case conditional on GPC (Peczarski 2006); no S(n) consequence since antichain root has width n.
- `notes/research-realizability-window.md`: Conjecture W **refuted** at n=5,6; Conjecture K ("for all n and all P in R_n, F(P) is a function of (e(P),covers(P))") — "**all-n status open**" as of 11‑04, **but see §4: a finite n=7 counterexample was posted 11‑19**.
- `docs/research-plan.md`: "Shrinking the exponent" (2^{O(n log n)} or 2^{O(n)}), "Certificates" (optimal‑size completeness open), "Space" (O(N log N) → O(N)/polylog), "The bound gap" (effective finite Sergeev), "Descriptive complexity" (explicit FO(LFP)/ESO definition).
- `docs/research-fo-tc-strategy-programs.md`: completeness half is "the hard part"; combined‑complexity obstacle is "the central open technical point"; §7 next experiment was executed on 11‑19 09:13 (`fotc-program-vs-dag-size`).

---

## 3. New structural facts / theorems that could seed fresh questions

**Optimal play / state counts (minimax game).**
- **Proved:** L(n) ≥ 2n!−1 for all n (every node of a reduced optimal tree carries a distinct labelled poset); refined root‑layer bound L(n) ≥ 2n!−1 + n(n−1)−2. (14:09, 16:37, 16:44)
- **Proved:** L(n) ≤ (n(n−1))^{S(n)+1} ≤ n^{2(S(n)+1)} = 2^{O(n log²n)}; Kleitman–Rothschild ⇒ exponentially small fraction of labelled posets lie on an optimal play. (15:22)
- **Proved theorem (no‑go):** all‑sibling‑isomorphic optimal tree impossible for n≥3 (general lemma L(Q)=2^{F(Q)}; boundary exactly 3\|n!). (15:39)
- **Proved theorem:** a height‑S(n) tree with all moves locally minimax **always exists**; hence any verifier accepting all‑minimax strategies of height ≤k is complete for SORT‑BOUND‑U — but the canonical certificate is the 2n!−1‑node tree, so NP membership is not obtained. (17:27)
- **Proved (zero‑progress dichotomy):** max(F(child))∈{F(P)−1,F(P)}; a ZP move is globally feasible iff local slack σ≥1; first non‑minimax move on a feasible path to a gap state is ZP from a slack L_loc state. (18:04)
- **Proved (equivariance):** deterministic Sₙ‑equivariant optimal play exists with no height penalty — pick one Aut(P)-orbit of optimal pairs per class and lift. (14:34)
- **Finite, checkable:** m(8)=22; min equiv‑class counts 1,2,4,6,11,14,19; L_loc/L_tree tables through n=8 (L_tree(8)=166,205,369, L_loc(8)=146,143,257, gap 20,062,112 — reported, not independently re‑derived). \|C(7)\|=3,044,007 with gap 0; n=6 \|cand\L_tree\|=6060.

**Decks / F summary invariants.**
- D(P) **determines F(P)** exhaustively n≤6 (zero F‑mixing fibers); **does not** determine the labelled optimal‑pair set O(P) (all‑n symmetry argument); **does** determine the iso‑invariant optimum signature through n≤6 (OPEN all‑n).
- Deck child‑closure is false at n=4; number of decks is itself 2^{Θ(n²)} in general. (19:08–19:56)
- `(e,covers)` is refuted as a sound/complete memo key for optimal‑play continuation cost by an **n=7** reachable counterexample (08:13:42) — this is a finite refutation of Conjecture K's key, though no all‑n family was constructed.

**Excess / gap bounds.**
- E(n)=S(n)−⌈log₂n!⌉ = 1 at n=12,16,17,18; E(n)=o(n) by Sergeev; SORT‑BOUND‑U ∈ uniform TC⁰ iff E(n) ∈ TC⁰. (17:32)
- Ford–Johnson excess δ_FJ=FJ−⌈log₂ n!⌉ fits n≤22 but is provably not exact (Manacher: S<FJ for some n≥47; δ_FJ=Θ(n) vs g=o(n)). (19:57, 00:58)
- Ordinal‑sum/module composition of all known sound base scores cannot produce strict excess at the antichain root (compositional‑antichain‑strict‑excess refuted).

**Fibonacci thresholds / GPC / width two.**
- T(r)=F_{r+3}−1 for 2≤r≤8: 4,7,12,20,33,54,88; staircase W_n has e(W_n)=F_{n+1} (proved all n), m(W_n)=n−1 verified n≤10 only.
- Width‑two theorem: e(P)≥F_{m(P)+2} for width ≤2, conditional on GPC (Peczarski 2006), equality for r≤8. GPC proved for width two, semiorders, posets with ≤11 elements (Peczarski) and verified through order 14 (Gupta, arXiv:2607.23926v2).
- Depth‑balance B (some optimal move with easy child depth ≥m−2) is a sufficient local ingredient for the Fibonacci induction; verified for **all posets n≤10** (2,567,274 iso classes).
- Core reduction (cores, generation by maximal insertion + ordinal sum, e(P)≥|P|) is a paper proof; dual generator agrees at E=33 and E=54; E=88 has only one implementation.

**Framed DAGs / certificates.**
- Polynomial‑size framed DAG for F_FJ(n) for all n (O(n) pairing + Q(⌊n/2⌋) + O(n³) insertion states ⇒ ~O(n⁴)); soundness checker ACCEPT through n=28.
- **Join‑feasibility lemma (proved, all n):** in a sound height‑k framed DAG a node at depth d with relation R satisfies e(R)≤2^{k−d}; hence two distinct information‑tight states at equal depth can **never** be forgetfully joined at exact budget. (15:02 + Executive strengthening 15:15)
- Exact‑budget isomorphism quotients are tiny (n=1..6: 1,2,4,7,11,14), so small‑n falsifier (iii) is FALSE; FJ's O(n³) insertion states rest on a rank‑window invariant tied to fixed pairing/Jacobsthal order, exactly the structure Manacher/Sergeev show is not exactly optimal.
- Framed optimal certificate exists at n=7: 19 nodes, height 13 = S(7), checker ACCEPT.

**Minimax‑game reachability.**
- Hamming connectivity: F(P,D) (designated‑pair outcome patterns over linear extensions) induces a connected subgraph of the t‑cube — a real structural restriction on which Boolean solution sets comparison tests can realize; this is why arbitrary‑test PSPACE‑hardness machinery does not transfer to GEN‑SORT. (15:03; independently confirmed 15:19)
- Realizability window (doc, 11‑04): covers(P) ≤ d ≤ S(n)−max(F(P),π(P)); star exclusion for all n≥4; Conjecture W refuted.
- `reachable-poset-class-universality-alln`: **every** unlabelled poset class is reachable, so reachability alone gives no compression.

---

## 4. Topics declared exhausted / closed / STOP / settled negatively

| Topic | Declaration (date) |
|---|---|
| `component-reversal-defect-retry` | "the exact question is **ALREADY INVESTIGATED; report precise status and STOP**" (19:55); no re‑dispatch warranted; equality D≡0 false at n=9, D≤1 open but natural approaches "already investigated/blocked families" (04:45). |
| `info-bound-gap-invariant-retry` | "the exact FRONT is **ALREADY SETTLED** by adjacent fronts, so **STOP**" (19:57); "re-running duplicates settled work." |
| `disjoint-union-defect-retry-alln` | "**exhausted with NO finding**; ledger `running` is stale" — agent's counterexample search was invalid (F(C₂)=3), results discarded (20:29). |
| Deck child‑closure | "child-closure is **FALSE**, with an explicit n=4 falsifier… **SETTLES the front's question negatively**" (19:30). |
| Deck determines labelled optimal move O | "**D does NOT determine O**, already at n=4 … this **decides the front's question NO**" (19:56); closes the literal "D names the labelled minimax pair" certificate route. |
| Class‑stable optimal strategy chain | "**FRONT REFUTED** / proved no-go, all n≥3" (15:39). |
| `(e,covers)` as memo key | "**no-go for this specific key**" — finite n=7 counterexample (08:13); Conjecture K's former finite support withdrawn in that form. |
| `join-reduced-canonical-strategy-alln` | "**FRONT REFUTED** by a universal 2n!−1 reachable-state count" (11‑18 19:44). |
| `fredundancy-confluence-corrected-criterion` | "the front's all-n claim is **FALSE**, and 'confluence remains open' is a **false distinction**" (11‑18 19:24). |
| `lossless-merge-confluence-canonical-form` | Per‑edge confluence at budget‑tight states refuted at n=5,6,7 (11‑18 19:07). |
| Comparison‑split/Kraft strengthening | "**two proved no-go theorems** delimit the program"; "the n=12 gap is provably *deep*" (18:30). |
| Compositional strict excess at root | "The FRONT's proposed mechanism is **refuted**" (01:46). |
| Uniform TC⁰ membership route | "the FRONT's stated reasoning is **REFUTED as insufficient**" (17:24). |
| Sorter/refuter duality | Class level **blocked** by open NP‑vs‑coNP separations; "neither the FALSIFIER's decoupling nor a duality theorem is provable with current techniques" (17:22). |
| "Incompleteness barrier" for all‑minimax grammars | "**REFUTATION** of the 'incompleteness barrier' conjunct" (17:27). |
| Depth‑balance falsification by brute force/random | "brute-force/random falsification is **not a viable route**; any n≥11 counterexample must come from structural construction" (20:15). |
| Θ(n log²n) exponent synthesis | "**withdrawn**" as erroneous (16:35); the 15:52/16:11 posts are explicitly superseded. |
| SAT + group‑theoretic symmetry breaking | "terminal outcome **(b)** — a precise STRUCTURAL OBSTRUCTION" (11‑19 07:29); no gain over DP/budgeted DFS. |
| Selection‑number sorting lower bounds | "**Stop condition reached; no further instance enumeration**" (06:53). |
| Repeatedly flagged duplicates / do not re‑dispatch | `universal-fibonacci-threshold-all-r`, `root-tight-all-tight-tree-existence`, `universal-abc`, `adversary-cert-completeness-conp`, `info-bound-gap-invariant-alln`, `optimal-fibonacci-split-alln`, `component-reversal-defect-bound`, `disjoint-union-defect-min-size`, `antichain-reachable-abc-tree-completeness` — all "already investigated/blocked" with final reports. |

**Net for a curator:** the frontier is saturated (583 fronts, 562 investigated, 21 blocked, 0 running at 20:36). Fresh research must clear a high bar: the only live mathematical obligations with a concrete bridge back to S(n) are the L(n) exponent window, polynomial‑state description of exact‑optimal play / framed‑DAG completeness at exact budget, effective finite Sergeev constants, space reduction, and the GPC/Fibonacci inequality (the latter being a general‑poset theorem with no antichain bridge unless a reduction is found). Most general‑poset structural refinements (reversal defect, disjoint‑union defect, decks) were explicitly abandoned for lack of a reduction back to the antichain root, in line with AGENTS.md.
