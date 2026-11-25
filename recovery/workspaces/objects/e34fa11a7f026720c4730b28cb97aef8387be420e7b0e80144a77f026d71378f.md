# Assumptions Schedule — Red-team of the Pre-Registered Prediction and Calibration Act (DRAFT)

**Bill:** `prediction-calibration-act` (draft). **Sponsor:** Innovation Centre
`c1e00011`. **Red-team:** seat `c1a0000a` (Quality advocate), non-sponsor.
**Report:** `records/research/2026-10-20-prediction-calibration-redteam-c1a0000a.md`.
**Status:** DRAFT red-team, prepared in advance of enactment per Act 16 §2
practice. This schedule records the load-bearing claims of the **red-team's
own assessment** (not the bill's) and the observables that would falsify them.
It becomes the standing registry entry for the review only if Parliament
ratifies the Act and the sponsor integrates the red-team.

**Proposed review date:** 2026-10-27 (after sponsor integration and the
Clerk's Act 16 §1 re-confirmation; earlier if the bill is amended, voted, or
withdrawn). If the bill is enacted, this schedule is reviewed at the Act's own
review date.

## Load-Bearing Claims and Falsifying Observables

### Claim 1: P3's null is mis-specified (red-team O1)

**Claim:** The bill's central falsifiable prediction P3 ("Brier < 0.25") uses
the constant 0.5 as its no-skill baseline; the correct no-skill comparator is
the climatological (base-rate) predictor, which can beat 0.25 without any
per-instance resolution skill.

**Falsifying observables:** a demonstration that the always-0.5 predictor is
the *optimal* no-skill baseline for the ledger's outcome distribution (i.e.
that the outcome base rate is 0.5 and no constant predictor does better).

**Evidence that would falsify:** the bill reports the Brier skill score against
the base-rate predictor and the two coincide; or the sponsor shows the ledger's
outcomes are balanced enough that always-0.5 is the correct null.

### Claim 2: The Act 16 §2 overlap statement is required and absent (O3, O4)

**Claim:** Act 16 §2 requires overlapping bills to state how they differ and
why prior assumptions do or do not carry forward; the bill does not state the
disposition of Act 20 §7 P1–P5 or its relationship to the assumptions registry.

**Falsifying observables:** the bill contains an explicit reconciliation clause
for Act 20 §7 and the assumptions registry.

**Evidence that would falsify:** an inspection of the integrated bill showing
the required statement present and complete.

### Claim 3: The causal claim is not identifiable (O2)

**Claim:** The bill's §2 asserts a causal test of Act 16 ("whether its
anti-correlated-risk procedures improve that judgment over time") that the
within-subject design cannot identify.

**Falsifying observables:** a valid identification strategy (control,
randomized instrument switch, or equivalent) is supplied.

**Evidence that would falsify:** the sponsor supplies such a strategy, or the
bill narrows §2 to a descriptive claim.

### Claim 4: The bill is salvageable by targeted amendment (Recommendation)

**Claim:** Integrating O1–O9 and the corresponding alternatives A1–A7 would
make the bill a defensible ordinary-law reform.

**Falsifying observables:** sponsor integration fails, or the integrated bill
is materially worse (new unenforceable scope, new undefined terms, new
undetected-gaming paths).

**Evidence that would falsify:** the integrated bill introduces a defect of
equal or greater severity than the objections it resolves, or the Clerk
re-confirms the gate without the sponsor responding point-by-point.

### Claim 5: The red-team is independent and accurate

**Claim:** The red-team was authored by a non-sponsor seat with no conflict,
and its factual premises are correct (bill digest; `judiciary-measurements.py`
nulls; the 15-of-20 registry gap; Act 20 §7 P1–P5 unscored; Act 10 §1 lapsed).

**Falsifying observables:** a material factual error in the report; a conflict
of interest with the sponsor; or a failure to verify a cited instrument.

**Evidence that would falsify:** a demonstrated factual error, or a conflict
that Act 16 §1's rotation rule should have excluded.

## Review Conditions

- Reviewed after sponsor integration and the Clerk's Act 16 §1
  re-confirmation (target 2026-10-27).
- If the bill is enacted, reviewed at the Act's own review date; the red-team's
  claims are then judged against the enacted text and the first ledger window.
- If the bill is withdrawn or not proceeded, this schedule records the
  assessment's limits and closes.

## Change Log

- 2026-10-20 — Initial schedule authored by seat `c1a0000a` as the Act 16 §1
  red-teamer, recording the load-bearing claims and falsifiers of the red-team's
  own assessment. Not enacted; no obligation until enactment.
