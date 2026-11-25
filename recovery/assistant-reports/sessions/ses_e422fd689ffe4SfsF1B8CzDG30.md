# antonina-LhmdXRHQDJVLXQ96pwWnC2-salary

Session: ses_e422fd689ffe4SfsF1B8CzDG30
Workspace: /home/lubko/soring-fronts/alternative-relaxation-farkas-support
Created: 1794185898422; updated: 1794186449557

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 66 (msg_1bdd061f5001XO08QLO2h7fcgd)

The ledger confirms my front (`alternative-relaxation-farkas-support`, status `running`). Let me study the prior results and literature.

## Output 81 (msg_1bdd0f515001rWKBZ71iJaErdH)

I'm operating the ledger front `alternative-relaxation-farkas-support`. I've studied the problem statement, literature baseline, and the n12-nontightness note. Next: get exact S(n) vs information-bound values through n=22 (OEIS indexes), since the crux of my attack will hinge on the tight vs. gap subfamilies. Also check the k at which certificates change character.

## Output 96 (msg_1bdd57462001hQtC7EdKM7CnDg)

OEIS gives the full picture through n=22. Combining A036604 (S values) with A003070 (information bound C):

- **Tight (S(n)=C(n)):** n = 1..11, **20, 21**
- **Gap (S(n)=C(n)+1):** n = **12–19, 22** — a contiguous block 12–19, not just 12 and 16–18
- n = 23 open

This redefines my attack precisely, and the answer is sharper than I expected. Let me verify the key arithmetic and check one potential objection numerically.

## Output 107 (msg_1bdd648c1001IfHKqgLxfCWoYQ)

The arithmetic is confirmed. The picture is now complete and decisive. One more check — the board posting interface before I write up:

## Output 175 (msg_1bdd79b4a0019SaATEm2vPJulT)

All analysis is done. Writing the board report now — the front's dichotomy is settled on a precise subfamily, and the residual is reduced exactly to a known classical open problem.

## Output 202 (msg_1bdd853160012yv2dKZ7HpOIhE)

Post succeeded. Verifying it landed and the worktree stays clean:

## Output 213 (msg_1bdd8665d001SWPRpYeNJcvABP)

## Report — front `alternative-relaxation-farkas-support`

**Verdict: the front's dichotomy is falsified on the tight subfamily; the residual collapses to a known classical open problem.** Full report posted to board #301 (01:07Z, verified landed); worktree clean, no Lean/repo changes.

**Main finding (paper proof, elementary; labeled [deduction]):** Using OEIS A036604 vs A003070 (exact S(n) known through n=22), the known instance split is:

- **Tight** S(n) = ⌈log₂n!⌉: n = 1..11, 20, 21
- **Gap** S(n) = C(n)+1: n = **12–19 (contiguous block!) and 22** (block 12–19 was not previously recorded in the repo's notes)
- n = 23 open

**Proposition T1:** for every tight n, the one-variable system {n! ≤ 2^k} is an *exact (feasibility-equivalent at every budget k)* faithful reformulation family, so at the boundary k = S(n)−1 it is infeasible with a **Farkas certificate of support 1** (soundness unconditional via the information bound; completeness exactly on tight n). At the flagship (4,4): the Viche-verified state-expanded dual (support 204) and a simple support-1 certificate **coexist on the same instance** — the (n−1)!! blow-up is demonstrably representational there, and horn B ("any separating relaxation needs support ≥ (n−1)!!") is false for those ten n.

**Key secondary results:**
- **Orbit quotient:** the (n−1)!! barrier is a labelled-coordinate phenomenon — all t-matchings at depth t are isomorphic, so the Sₙ-symmetrized dual (feasibility-preserving) collapses that multiplicity into one orbit coordinate. No dual-support lower bound is known for iso-class coordinates, so horn B has no proved content in symmetric encodings.
- **Gap interface:** for distance-1 instances, 2^k ≥ n!! at k=S(n)−1=C(n), so the one-coordinate provably cannot refute, and any poly-support dual certificate there **would be the first compact certificate of a "S(n) > C(n)" fact** — an open problem in the Wells→Peczarski→Stober–Weiß line (all known proofs exhaustive; transcripts exponential-size for n≥16 and not poly-time verifiable even at n=12 due to #P-hard linear-extension verification). So horn A cannot be executed there with current literature; it is exactly as hard as that classical open question.
- **Uniformity barrier:** a poly-time-constructible exact family would give SORT-BOUND-U ∈ P, so unconditional impossibility is out of scope per the project's own P-vs-PSPACE constraint; the front is meaningful only as a nonuniform existence question.

**Honest limits:** tightness values for n ≤ 22 come from literature, not from this front; infinitude of either subfamily is open (so no "infinite family" clause was executed in either direction); no poly-support certificate for a gap instance was constructed — none is known; §6 is a collapse observation, not a barrier proof. Recommended follow-up front recorded in the post: "compact δ=1 certificates."
