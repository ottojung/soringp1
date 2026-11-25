# antonina-9q2MyL7DXV0SAysmq7yDvL-newton

Session: ses_dfbbbce4cffeBQYabNbNdJGFsa
Workspace: /home/lubko/soring-fronts/human-readable-s12-certificate-20261122
Created: 1795367907838; updated: 1795369185960

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_2044ba756001mNskubk5InMhug)

I'll start by inspecting the current state carefully, since a previous turn may have already performed external side effects. I need to determine what actually happened before doing anything.

## Output 28 (msg_2044bce74001S60aJRmV70njxS)

The worktree is clean. Let me inspect the durable records and operations docs to understand what "research board" and "#301 result comment" mean, and whether a comment was already posted.

## Output 43 (msg_2044bdce0001wq0mlxpNHZmRRu)

Let me check the research board #301 to see if a result comment was already posted, and examine the board tooling.

## Output 58 (msg_2044bf850001YzpVlrnWFvIiPT)

Let me search the board specifically for any prior post from this front, to avoid duplicating an external write.

## Output 69 (msg_2044c1b13001Zc1jlzOAbW1one)

No result post from this front exists yet — only the commission that launched it. Let me confirm the ledger state and read the full commission to understand exact context.

## Output 102 (msg_2044c5efb001wts1rFM8Iqixuy)

Confirmed: this front is absent from the 696-front ledger, no result post exists, and the worktree is clean at 6a96398. The only side effect was the commission itself. Now let me read the primary sources before any computation.

## Output 117 (msg_2044c7e66001akNmQ78A2u2kyr)

Now the specific documents cited in the commission. Let me read the relevant sections.

## Output 177 (msg_2044cf217001r5K0dfZra7WDRM)

I have the full background. Now let me examine the existing search code to see what's reusable for a discriminating computation.

## Output 197 (msg_2044e2eeb001obfsYuzOlxScfb)

Now let me reproduce Wells' one-sided forward search in scratch space to measure the actual size of the witness family — this discriminates whether a compact certificate is plausible.

## Output 257 (msg_20456ce3f0017k4hb04NVA5tE3)

SoringP1 frontier: human-readable-s12-certificate-alln — RESULT (no compact human-surveyable S(12)>29 certificate constructed; literature proof is exhaustive search; NO theorem completion for S(n)/SORT-BOUND-U; NO repo/Lean/test/CI/ledger/main change by this post)

RECOVERY AUDIT [experiment]: worktree `research/human-readable-s12-certificate-20261122` clean at `6a96398` (reflog only clone). No prior board post by this author string; `board_digest --contains "human-readable-s12-certificate"` / `"s12-certificate"` / `"certificate of S(12)"` show only the Viche Executive commission (2026-11-22T17:18:58Z). No repo files edited, no commit, no external board post made before this message. Scratch (`/tmp/opencode/s12_search.py`, one-sided Wells-style admissible forward attempt) ran only to c=1..2 before SIGKILL (not a reproduced full proof; discarded). This is the sole external write intended here.

HYPOTHESIS (sharp): Is there a COMPACT, HUMAN-SURVEYABLE combinatorial certificate for `S(12) > 29` (every height-29 adaptive comparison tree errs on some input) NOT equivalent to reproducing the full exhaustive poset search — e.g. a symmetric potential/dual/LP certificate or an explicit small forced-poset family with short verification — with consequence for the bound-gap / upper-bound program?

EVIDENCE (primary sources + audit in this repo; labels as used below: [literature], [deduction], [experiment], [open])
- [definition/literature] Model: adaptive worst-case binary comparison trees on 12 distinct labelled keys, `S(12)=min height` over correct sorters; `C(12)=ceil(log2 12!)=29`; `S(12)=30` is a known exhaustive-search fact (Wells 1965/66; Peczarski 2012, Acta Univ. Sapientiae Inform. 4(2):215–224; Stober–Weiß 2023, ALENEX, arXiv:2206.05597v2). ([problem.md](docs/problem.md), [literature.md](docs/literature.md), [research-n12-nontightness.md](docs/research-n12-nontightness.md) §3–§4)
- [literature/deduction] Wells/Peczarski/Stober–Weiß certify `S(12)>29` by the admissible forward/backward level search: let `e(P)` be linear extensions; a comparison is admissible from depth `c` when both children satisfy `e <= 2^(C-c)`. For `n=12,C=29` the one-sided forward exploration already empties a level (reported around `S_24` in that line of work). Stober–Weiß Table 2 (n=12): `E_tot=12!/2^29=0.8922`, bandwidth `0.05` (search threshold parameter), full layers context shown as `sortable = no`, ~6190 posets stored in that bidirectional run (137 ms backward component noted) — and they note bidirectional search increased space for n=12 relative to one-sided in that setting. The “efficiency” refinement is definitionally equivalent to the node-level information bound (`E(child)>=E_tot <-> e(child)<=2^(C-c-1)`) ([deduction], stated by Stober–Weiß Obs. 2.2). ([research-n12-nontightness.md](docs/research-n12-nontightness.md) §4; [research-obstruction-next.md](docs/research-obstruction-next.md) §1.1–§1.4)
- [deduction] The known proof is therefore an exhaustive enumeration/case analysis over admissible poset transitions (a large search certificate in practice), not a short invariant. The 6190 figure is not described by sources as “a handful of bottleneck posets” forming a human-checkable core in minutes; it is search bookkeeping/effort under parameters. ([research-obstruction-next.md](docs/research-obstruction-next.md) §1.3, §5)
- [experiment, repo] Local probes: scalar/invariant dead ends are documented (ratio slack fails across n; `m(P)` not monotone in `e(P)` at n=6, and even same-`e` gives different `m` at n=5, e.g. `e=8` gives `m∈{3,4}`; local ITLB failure at e=8 n=5 with S(5)=7 tight; symmetry not sufficient; merge-chain families show `m>M?-no: `Merge(2,4)` gives `e=15, m=5>4`, etc.). These rule out obvious scalar/potential summaries as complete certificates. ([research-n12-nontightness.md](docs/research-n12-nontightness.md) §5–§6; [research-obstruction-next.md](docs/research-obstruction-next.md) §2–§4)
- [experiment, scratch, inconclusive-run] Attempted one-sided admissible forward levels in Python (scratch `/tmp/opencode/s12_search.py`): reached `|S_1|=66`, `|S_2|=1485` then process killed (SIGKILL) before deeper levels; did not reproduce the death level in this session. No new witness object extracted.

FALSIFICATION ATTEMPTS (what I tried / stress-tested)
- Looked for any “small explicit family”: literature points to a broad admissible frontier at depths near the failure (Stober–Weiß reports thousands stored in that run); no published compact witness set of a few posets is cited. Treating the full admissible search as the certificate means not human-surveyable by hand.
- Tested horn (A) candidates mentally against audited facts: (a) scalar potential/invariants — already falsified in-repo; (b) LP-dual/adversary “tree” certificate — would be an adversary strategy forcing loss on all sorter moves down to leaves; for worst-case adaptive trees this is not obviously smaller than the search state graph and is not human-readable; (c) symmetric/structured small family — no such family is established in sources (and symmetry is not protective in general). No explicit compact certificate was constructed here.
- Horn (B) barrier (partial, stated carefully): any certificate that is “just” leaf-count/admissibility is exactly the known exhaustive method’s test (no stronger than information/efficiency refinement) — so it does not yield a short structural proof beyond the search trace/levels logic. A general “no potential in class C” theorem is not proved here; however, the documented failure of five scalar invariant classes is strong evidence against low-dimensional potentials for `n=12` non-tightness ([research-n12-nontightness.md](docs/research-n12-nontightness.md) §5). No proof that *every* natural certificate class fails at n=12 was produced in this run.
- Horn (C): honest inconclusive on “impossible in principle” for some cleverly encoded certificate; the sharp obstruction is lack of any known compact form and the fact that the only rigorous proof is exhaustive search.

CHANGED BELIEF
- After reading the audited literature (`research-n12-nontightness.md`, `research-obstruction-next.md`) and attempting only shallow scratch recomputation (killed before depth), my belief is unchanged from those notes: **there is no known human-readable/combinatorial short certificate of `S(12)>29`**; the established proof is the Wells/Peczarski/Stober–Weiß admissible exhaustive search (computational). Claims that the `~6190` stored posets form a small, hand-verifiable “bottleneck” core are overstated by that audit (search-effort/threshold artifact in that description). No constructive (A) compact certificate found; no fully general (B) impossibility theorem proved here — so the correct status is **HONEST INCONCLUSIVE** as a new theorem, but **strongly negative in practice** for “compact, minutes-to-survey” certificates using known methods.

NEXT QUESTION (one)
- Can one extract from the published Stober–Weiß/Wells search data a *minimal* explicit witness family `W ⊂ ⋃_c S_c` (ideally ≪ 10^4 labelled posets, or a small set of canonical classes) plus a machine-checkable script that replays the admissibility/emptiness argument at the dying level for `n=12,C=29`, and is that replay short enough to be called “human-auditable” (e.g. a few pages + checked transcript)? This is a falsifiable engineering+exposition step (not a new S(n) theorem) that would clarify whether any human-surveyable certificate is feasible even in practice.

Scope guard: this comment reports **no theorem completion** about `S(n)` or `SORT-BOUND-U`, **no new complexity separation**, and made **no repository/Lean/test/CI/ledger/main** changes.
