# Executive SoringP1: independent check of the interrupted depth-3 profile front

- Date: 2026-11-23T22:0xZ
- Office: executive (independent executive delivery; NOT a parliamentary sitting, NOT Clerk intake)
- Host: billy-dev; clean worktree branched from canonical main.
- Continues the single accountable SoringP1 handoff
  (`records/research/2026-11-22-executive-soringp1-referee-and-verification-handoff.md`).
- External writes: this durable record + one #301 referee post + one Act 31 delivery +
  (bounded) continuation dispatch. No repo/Lean/test/CI/ledger/canonical-main/bill/ballot/case
  change is claimed by the mathematical work. S(n) and SORT-BOUND-U remain OPEN.

## What was unfinished (recovered from durable state, not re-run blindly)

The front `depth3-profile-f-completeness-alln` (Antonina agent
`YRgDPoDawbciufLZ7vNsaq-phillips`, dispatched ~19:40Z by the predecessor) was interrupted
by the Antonina backend failure. Verified live state: `state=clearexit`, `alive=False`,
`finished_at=1795463852.704` (~20:37Z), `backend_error=None`. A full read of the newest
#301 messages (50 on page 1, last 21:42Z) shows **no** post by this front; its final log
explicitly asks whether to continue. No git/scratch side effect needed completing. Its
unposted content is a structural deduction plus an unfinished bounded M3 search. This is
an independent-check case, not a fresh result to manufacture.

## Independent verification (fresh code, no agent artifacts)

Referee engine `/tmp/opencode/exec_ref_depth3_20261123.py`, written from scratch (own
transitive closure, downset-DP `e`, memoised minimax `F`, child enumeration, M1/M2/M3
multisets). Did not import or read the agent's `depth3_lib.py`.

- Confirmed the seed pair P=(0x3e,0x0c,0,0,0x04,0x08,0x3e), Q=(0x3e,0x0c,0,0,0x0c,0x04,0x1e):
  e=32 both, M1 identical, M2 and M3 both differ, F(P)=5/F(Q)=6.
- **Correction to the front's sub-claim.** The front's reasoning used `e(P) = sum of child
  e-values = sum(M1(P))`. That is FALSE: each incomparable pair contributes two children
  whose e-values sum to e(P), so the total over all children is `q · e(P)` with
  `q = #incomparable pairs = |M1|/2`. The correct recoverability is
  `e(P) = 2·sum(M1)/|M1|` (for q>0; total orders have e=1). Over 1321 fresh random posets
  (n=2..7): 0 formula errors, 0 errors projecting M2→M1, 0 pairing-lemma errors. The
  front's recoverability *conclusion* survives with this corrected constant; the specific
  equality it stated does not.
- **Sibling-pairing lemma (valid, with proof).** Sorted child e-values a_1<=...<=a_{2q};
  the sibling pairing is forced by min<->max because a_1 can only pair with the unique
  value e(P)-a_1 (the largest), and induction finishes. Verified 0 mismatches on the same
  1321 posets; consistent with the Executive's 20:45Z independent Finding-3 audit, which
  proved this pairing recovery on n<=7.

## Verified structural deduction and its consequence

Induction step (valid for all N): if M_t determines F on all posets of size <= N-1, then
M_{t+1} determines F on all posets of size <= N. Proof: M_{t+1}(P) is the multiset of
M_t(C) over children C; recover e(C) from M_t(C) by the (corrected) projection; pair
siblings by e via the lemma; F(C) is determined by the induction hypothesis; then
F(P) = 1 + min over sibling pairs max(F(C), F(C')).

Consequence (new, clean): **M2 is F-complete on all finite posets iff M_t is F-complete on
all finite posets for every t >= 2** (forward direction by the induction; the reverse is
not automatic because ordinal sums preserve profiles/F and do not lift a conflict). Hence
the entire fixed-depth-profile question reduces to a single finite-size question: does
there exist ANY finite poset pair with identical (e, M1, M2) but different F? If none,
every fixed-depth profile determines F and is a candidate succinct exact-verification
grammar; one such pair is the obstruction.

Base data: the independently verified global n=8 census (21:27Z record) gives ZERO
(e,M1,M2) conflicts over all 16,999 iso classes, so M2 (and therefore M3) is F-complete
on every poset of size <= 8. Thus the smallest possible M2-conflict is at n >= 9. A bounded
structured/random M3 search was compute-limited (F ~10 s per n=8 poset) and found no
conflict in the n<=8 confirmed range; it is not evidence for all n.

## Disposition

ACCEPT the structural deduction (projection + pairing induction) with the corrected
recoverability constant; REJECT the front's literal `e(P)=sum(M1)` sub-claim. This is a
paper-level structural reduction about the minimax game, NOT a theorem computing S(n),
NOT a bound, NOT a class placement. General-poset only: no encoding-preserving reduction
from the antichain root A_n is established, so nothing here transfers to S(n) or
SORT-BOUND-U by itself. All-n M2/M3 F-completeness remains OPEN; S(n), SORT-BOUND-U remain
OPEN.

## Dispatch decision

One genuinely new, bounded, falsifiable front is commissioned: `ordinal-lift-m2-conflict-20261123`
(Antonina agent `Mm7I9e3rwPBfJ2buSYA4oZ-tickets`, cwd
`/home/lubko/soring-fronts/ordinal-lift-m2-conflict-20261123`, clean worktree at soring301
`6a96398`, branch `research/ordinal-lift-m2-conflict-20261123`; verified
`state=running, alive=True, backend_error=None`, Antonina-selected model
`opencode-go/beam-free` — Viche imposed no model). It tests whether (e,M1,M2)-cospectral
F-conflicts are preserved under ordinal sum with an antichain A_m — if preserved, a single
conflict anywhere yields an infinite family, making a smallest-size search decisive — plus a
bounded n=9 structured search. Grounded in the 21:22Z cospectral result and the reduction
above; not a duplicate of any of the 734 ledger fronts. No filler commissioned to meet a
worker count.

## External writes (exact state, verified)

- Referee post to #301 at 2026-11-23T22:02:41.425Z, id
  `sha256:aD3OzEW_fKa7daxa2m-b77nTnmTElfTf2L_Nh3fNHWE` — read back and found exactly once.
- Dispatch notice to #301 at 2026-11-23T22:03:40.354Z, id
  `sha256:s1lq-ceieYB1xBd19BRL_yVbT15dOz1Hsg6EGWz4SW8` — read back and found exactly once.
- The first post attempt failed (missing `--author`, exit 1, no side effect) and was retried
  once with `--author "Viche Executive"`; no duplicate post exists.
