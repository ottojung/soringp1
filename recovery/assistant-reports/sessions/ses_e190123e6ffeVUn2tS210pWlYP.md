# antonina-HeyYer4earxYH4ZzSnnh4o-houses

Session: ses_e190123e6ffeVUn2tS210pWlYP
Workspace: /home/lubko/soring-fronts/antichain-reachable-abc-tree-completeness
Created: 1794876824619; updated: 1794880939890

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 422 (msg_1e718d645001VrvA9RwhxB01I4)

Recovery state assessed. **What already happened (no duplication needed):**
- Git: worktree clean at `6a96398`, branch `billy-dev`, no commits/PRs/Lean changes.
- Board: no post from me. The front `antichain-reachable-abc-tree-completeness` was **already investigated and posted** on #301 at `2026-11-10T02:10:21Z`, and Executive-verified at `2026-11-11T10:20Z`. Its ledger entry ("No final text; audit needed") is stale — the Executive already noted this.
- My interrupted turn only produced local scratch (`/tmp/opencode/hcompute.py`, board JSON reads); the n=8 test run was killed, no side effects.
- Key prior finding: reachability falsifier met at n=8/9 (starved state reachable at optimal depth), but the existential all-certified-tree claim is TRUE through n=9; all-n OPEN. **Unfinished work = extending past n=9.**

Plan: n=10 is the frontier (p10.txt is complete: 2,567,284 = A000112(10); the prior post's "3,238,100" figure was a miscount). I'll validate a parallel re-implementation of the F/H census against the Executive-verified n=8/9 outputs, then run n=10.

## Output 635 (msg_1e71e9959001uWw0E9mIGxRooh)

The prior `abc` binary has two problems I need to resolve before trusting any n=10 run — one I introduced (my refinement canon failed an isomorphism-invariance random test) and one I found **in the prior agent's validated binary itself**: `slaveCount` reads the global `downMask`, which has been clobbered by the last child's `ext()` call, so A-condition slave counts are computed against the wrong poset (undercounting slaves → possibly spurious A-certifications → H possibly under-estimated). The F columns are unaffected (they don't use slaves). Let me build a corrected parallel version with nauty canon (mutex-guarded) and locally-scoped downsets, validate F against the Executive-verified n=8/9 outputs, and see whether H changes.

## Output 692 (msg_1e720ac6c001K68BLXpARTXrV0)

The corrected binary **reproduces the F columns exactly** (0 differences across all 16,999 classes at n=8 — validating the recurrence and canon), but the **H columns differ in 382 states**: with correct slave counting, 434 classes have H>F, not the 52 reported on the board. The prior binary's clobbered-`downMask` bug was under-counting slaves, producing spurious A-certifications and under-estimated H. Crucially, `H(A_8)=16=F` still holds. Let me validate n=9 and then run n=10.

## Output 715 (msg_1e7237793001OLo23E99BoOsst)

The n=9 run was killed by the restart (no process, no output). Relaunching it detached with `nohup` so a restart can't lose it again:

## Output 733 (msg_1e7248240001j1m7evleEfkAsc)

While n=9 runs, let me prepare the comparison tooling:

## Output 769 (msg_1e726b41a001z8T1P4wAqw6sij)

The process died from the server restart. Relaunching fully detached with `setsid` so it survives restarts of my tool session:

## Output 787 (msg_1e7284c4e001HmPp3K3EnXK8cU)

Surviving the restarts now. Waiting for n=9 completion:

## Output 805 (msg_1e72d37e800177Xn94X81xhJV1)

n=9 corrected: **F columns match exactly (0/183,231 diffs)**, **H(A_9)=19 still holds**, but the corrected census shows **8,873 bad classes (H>F), not 839** — the prior binary's clobbered-`downMask` bug created spurious A-certifications that made 8,034 states look certifiable when they aren't. The antichain's positive claim survives at n≤9, but the board's bad-class counts were ~10× under-counted. Quick n=7 sanity check, then re-run the reachability analyses with corrected outputs, then launch n=10:

## Output 825 (msg_1e72d78f5001tK559z0SBg48MP)

Corrected reachability: n=8 bad-reachable 18→**146** (of 5102 optimal-reachable), n=9: 153→**2177** (of 33054). The starved-state phenomenon is real and ~10× more prevalent than posted; H(A_n)=S(n) still holds through n=9. Now the decisive extension — n=10:

## Output 836 (msg_1e72d9a09001dpb9gZAElO2tss)

While n=10 runs (~hours), an independent definitional cross-check of the corrected A/B/C logic — a from-scratch Python implementation (no shared code with either C++ binary), checked against n=6 classes and the specific n=8/9 states where old and new H differ:

## Output 854 (msg_1e72f3da0001VR0PN0uumVd4UT)

The independent implementation confirms the corrected logic and **resolves an internal inconsistency in the prior record**: the prior all-scan claimed the first bad class appears at n=7, yet the prior agent's own Executive-verified n=6 counterexample has H>F. With corrected slave counting, 2 bad classes appear at n=6. Let me confirm one of them is exactly the recursive-abc witness:

## Output 874 (msg_1e7323fe4001tD22MxmCxaW9TS)

Both bad n=6 classes found; the F=4/H=5 one is the Executive-verified recursive-abc witness. Let me also confirm Q8/Q9 (the prior starved-state witnesses) in the corrected n=8/9 outputs:

## Output 908 (msg_1e7345a79001O1tEKbpzrNehr5)

Q8/Q9 witnesses are robust under the correction. Checking n=10 progress:

## Output 919 (msg_1e7346a8a001b1hgD4qSNPSl33)

While n=10 grinds (est. ~3h), a determinism check of the parallel run (1 thread vs 3 threads on n=8) to rule out race-induced corruption:

## Output 930 (msg_1e7352448001b2gfePg1zI7ruN)

Deterministic. While n=10 runs, extract the depth profile of bad-reachable states at n=8/9 (earliest optimal-play depth where starvation can occur):

## Output 941 (msg_1e73554b8001Asw424DXLkDM3k)

n=8: starvation reachable after as few as **6 optimal moves**; n=9: after **4**. All consistent with S(n) totals. Now polling the n=10 run:
