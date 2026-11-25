# antonina-3WGGurhKpizBSxHYLcVgS3-wright

Session: ses_e042e5e54ffeonesiFhBVqCnyF
Workspace: /home/lubko/soring-fronts/exec-du-asymmetric-structured-search-20261121
Created: 1795226182130; updated: 1795228520598

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fbd1a3ca001TApHfrnsfUEQ6W)

I'll start by exploring the repository structure and reading the key docs to understand the research setup, the F-model definition, and how research results get posted.

## Output 21 (msg_1fbd1d168001xb34HJAYC10Cv1)

Now let me read the problem definition and look at the scripts directory for existing search tooling.

## Output 36 (msg_1fbd1dd0c001IAQqmVYDg2XbZb)

Let me get the context of board issue #301 via the digest tool, and look at the probe scripts relevant to the asymmetric decomposition hypothesis.

## Output 68 (msg_1fbd2581e001iC5IdXzZTpi1wb)

Let me find the exact #301 post about the hypothesis, and read the board digest tool plus the obstruction probe script.

## Output 87 (msg_1fbd3243d001I1KptTcb09c415)

The grep found nothing because the digest truncates at 850 chars by default. Let me list recent board messages by timestamp and then pull the full text of the posts about the hypothesis.

## Output 894 (msg_1fbf5354d001LS9k1ngjpd0VYN)

Done. Here is the summary of the work.

**What was run (scratch only, no repo changes; git worktree clean).**

A bounded exact search for the disjoint-union defect hypothesis
`F(A⊔B) ≥ F(A)+F(B)+min(|A|,|B|)+1`, using the standard memoized
minimax evaluator over transitively-closed posets (same model family as
`scripts/obstruction_probe.py`), with surplus = `F(A⊔B) − F(A) − F(B) − min − 1`
(violation iff surplus < 0).

| Search | Scope | Checks | Min surplus | Violations |
|---|---|---|---|---|
| S1 complete (2,5) | A: 2 unlabelled 2-posets; B: all 63 unlabelled 5-posets (canonical reps of 4231 labelled). 2×63=126 inequality checks, exact. | 126 | 1 | 0 |
| S3 complete (3,3) | A,B: all 5 unlabelled 3-posets. 5×5=25 checks, exact. | 25 | 0 | 0 |
| S2 targeted (2,10) | 8 specific B: antichain(5/10), chain(10), antichain(10)+one relation 0<1; both A classes. | 8 evals | 4 (evaluated) | 0 |
| S2 bounded BFS from antichain₁₀ | 240 s global, 200k step/B cap, gen cap 20000. | 30 generated, 0 fully evaluated (all hit cap) | n/a | 0 |

**Methods.** F(P)=1+min over incomparable pairs of max(F(P+ij),F(P+ji)), F(total)=0;
A⊔B has no cross relations. F is isomorphism-invariant, so unlabelled class
representatives suffice. `(1,1)` excluded per prior work. No Lean/repo changes.

**Outcomes.** No counterexample in any searched scope. The hypothesis is not
refuted through (2,5) complete, (3,3) complete, nor in the evaluated (2,10)
cases (chain and antichain: surpluses 4). The all-n claim stays OPEN.

**Precise obstruction (incomplete part).** For (2,10), naive memoized minimax
is infeasible for B with many incomparable pairs: the superposet state space
`{Q ⊇ A₂⊔B}` exceeds the 200k-step cap (antichain/one-relation B's time out;
only chain-like B's with few incomparable pairs complete). BFS generated 30
posets (seen 2251 labelled states) with 0 fully evaluated, stop reason
`global_deadline`.

**Evidence posted to Antonina issue #301** at 2026-11-21T02:35:00Z
(id `sha256:fusqqlMF…`), under author tag
`exec-du-asymmetric-structured-search-20261121`. Scratch artefacts:
`/tmp/opencode/du_defect_search.py`, `/tmp/opencode/du_defect_results.json`,
`/tmp/opencode/du_search.log`. No duplicate post made.
