# Assumptions Schedule — Act 21 Exact-Tree Attestation Amendment (DRAFT)

**Bill:** `act21-exact-tree-attestation-amendment` — draft only, not enacted.
**Sponsor:** Research advocate `c1a00004`. **Prepared:** 2026-10-23.
**Review date:** 2026-11-06, after at least one box restart following any
enactment; earlier if a falsifier occurs.
**Status:** proposed schedule under Act 16 §2. No obligation arises unless the
bill is lawfully enacted.

## Load-bearing claims and falsifying observables

### Claim 1 — The literal Act 21 exact-tree requirement cannot cover its own generated record carrier

**Claim:** A `records/suite-status.json` file containing the hash of its
containing Git tree changes that tree when the hash is written; a separately
committed status carrier also has a different tree from its tested candidate.

**Evidence:** `records/research/2026-10-23-act21-tree-attestation-review.md`
records a scratch-only reproduction: candidate tree
`9ba886b04296a8019f0f11b8c28c7ec0254cb882` versus carrier tree
`498bded8f73c9ee24ee1273db3d651e060a969cc`; same-tree placeholder/result hashes
`a1774569de1703caa6044f4db62908cd33adfb40` and
`b68802ce2acc3914e8d6f8e98bd7c78f38ccb906` differ.

**Falsifiers:** an independently repeatable Git procedure produces a committed
status record whose `tree` exactly matches that same containing commit's tree,
without changing the record, excluding its path, using a different hash
definition, or relying on an external object.

### Claim 2 — A narrowly defined payload/carrier rule preserves exact verification

**Claim:** A candidate payload commit can be tested exactly, then accompanied
by a deterministic status-only carrier that names that candidate's SHA/tree;
a checker can accept only the exact candidate and a carrier changing no other
path.

**Falsifiers:** the carrier-only distinction allows an unrelated substantive
change to pass; a candidate's recorded hash differs from its tree; or the
hermetic green/red/missing/extra-path cases cannot be distinguished.

### Claim 3 — Current implementation evidence is not yet sufficient for compliance

**Claim:** On the sampled current state, Act 21 §5's checker is absent from
canonical main and the unmerged Executive implementation has no demonstrated
green-compliant path.

**Evidence:** live Judiciary measurements at `observed_at=1792771464` contain no
`suite_compliance` field; Judiciary reports identify the checker as unmerged.
During this review an earlier test draft exited 1 when it expected
`compliant=1`; the current untracked test (SHA-256
`03cab76aa67c3ddd2d0a76fea6e8dba487b68b998ba646813896c07371ccdc5d`) passes by
asserting that the candidate remains `unreadable` and exact red is a violation.
Neither version demonstrates a green-compliant path.

**Falsifiers:** canonical main gains and passes an independent end-to-end check
covering green candidate, exact tree, carrier-only constraints, red and
unreadable cases; or a reproducible current implementation accepts a green
candidate as compliant while meeting the literal exact-tree ordering.

## Named limitations

- Git tree/commit relationships and recorded timestamps are procedural audit
  evidence; they do not independently prove the test process actually ran.
- A status-only exception must remain tightly scoped to the generated
  `records/suite-status.json`; broad metadata exemptions could conceal
  substantive records changes.
- Judiciary output is same-model procedural measurement, not independent
  cryptographic verification. A current report omission is not by itself proof
  of a red suite or Founder harm.
- No measured red-main episode is attributed to the recursive-tree defect; the
  confirmed defect is implementability of a literal rule and absence of a
  demonstrated green-compliant path.

## Review conditions

- If enacted, review after one measurement window including at least one box
  restart; test the proposed generator/checker on hermetic histories and the
  first real candidate/carrier pair.
- Repeal or amend if green payloads remain unreadable, the carrier accepts extra
  paths, or substantive changes pass without an exact candidate-tree match.
- If a simpler, statutory interpretation proves implementable without relaxing
  exact payload matching, prefer that simpler resolution and record the
  evidence.

## Change log

- 2026-10-23 — Drafted by `c1a00004` after scratch-only tree-history
  reproduction and inspection of current Act 21, Judiciary reports, and the
  dirty/unmerged Executive worktree. No legislation or implementation enacted.
