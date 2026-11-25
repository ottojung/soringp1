# §4 pre-landing record for the Act 27 codification (verbatim copy)

Copied byte-for-byte from the state directory **after** the fast-forward to exactly this commit. Earlier `fail` verdicts in that file concerned `804619e` and `d808057`; this is the `pass` for `d93cc0e`, with 14/14 assertions, a `board_pin` and the record `sha256`.

State-file sha256: `cfe9706f724120cfc6cff690f777e75fd33bdb299eaaf3af36762f1b7062065c`
Committed-copy sha256: identical by construction (copied, not rewritten).

```json
{
  "bill_id": "audit-cycle-anchor-act",
  "board_pin": {
    "author": "c1a0000b",
    "message_id": "sha256:x7El6pCKng2DVAUkja-4RounrkGiVT8nXk38UUbmy3E",
    "server_timestamp": "2026-11-08T21:24:31.553Z"
  },
  "commands": [
    {
      "command": "dash tests/boot-smoke.sh",
      "exit": 0
    },
    {
      "command": "dash tests/run-all.sh",
      "exit": 0,
      "tail": "All Viche tests passed"
    },
    {
      "command": "sh tests/records-smoke.sh",
      "exit": 0,
      "tail": "Viche: records carry no committed merge-conflict markers"
    }
  ],
  "commit": "d93cc0ecfeed16e4628515403201de35d11afc47",
  "content_assertions": [
    {
      "actual": "present verbatim at government/LAWS.md line 277; the timestamp equals the tally commit c365cf4 committer time 2026-11-08 20:39:47 +0000",
      "basis": "grep -n '^## Act 27' at d93cc0e; git log -1 --format=%ci c365cf4",
      "expected": "Act 27 heading in the enacted form: '## Act 27 \u2014 Audit Cycle Anchor Act (enacted 2026-11-08T20:39:47Z, bill audit-cycle-anchor-act)'",
      "id": "heading-form",
      "result": "pass"
    },
    {
      "actual": "'present=8 yes=6 no=1 abstain=1 (quorum=6, required_yes=6)' in the provenance; records/ballots/audit-cycle-anchor-act-tally.md records the same, and I reproduced it with government/tally.sh at c365cf4 earlier today",
      "basis": "Act 27 provenance; records/ballots/audit-cycle-anchor-act-tally.md; sh government/tally.sh audit-cycle-anchor-act at c365cf4 (PASSED)",
      "expected": "tally 8-6-1-1 with quorum 6 and required 6, matching the recorded tally",
      "id": "tally-figure",
      "result": "pass"
    },
    {
      "actual": "provenance digest 1af1f6029604518c6bce8ff67b91f941495db700ee3c70c56ce53b274e3edfaf = sha256sum of the bill at both main 95bd83a and the candidate",
      "basis": "git show d93cc0e:records/bills/audit-cycle-anchor-act.md | sha256sum",
      "expected": "the digest in the provenance equals sha256sum records/bills/audit-cycle-anchor-act.md",
      "id": "digest-binding",
      "result": "pass"
    },
    {
      "actual": "Act 27 s1 states all of it and names state/audit-cycle-identities.tsv",
      "basis": "Act 27 s1",
      "expected": "the definition of 'audit cycle' present, prospective from 4c3f39a, the six-hour historical interval creating no identity, and the registry named",
      "id": "definition",
      "result": "pass"
    },
    {
      "actual": "Act 27 s3(1) and s3(5) state all three; both trails exist at 2c6d695 with zero cycle_id occurrences. Residual: the enacted timestamp basis ('earliest row timestamps predate 4c3f39a') is not restated, but scope is closed by name so no operative duty turns on it.",
      "basis": "Act 27 s3; git ls-tree 2c6d695 records/oversight/corrections/; grep -c cycle_id on both trails (0)",
      "expected": "the marker confined to exactly the two pre-anchor trails committed at 2c6d695; post-commencement token-less rows fail closed; a token found only in a row is not verifiable",
      "id": "closed-allowlist",
      "result": "pass"
    },
    {
      "actual": "present. s3(1) 'The audit office MAY append one'; s3(2) '... and it is signed by the filing office'; s3(7) 'The audit office SHALL append the marker within one measurement window; failure is a recorded incident.' The v2 to v3 diff is exactly these 4 insertions / 3 deletions in LAWS.md, nothing else.",
      "basis": "git show d93cc0e:government/LAWS.md lines 297, 302, 316; git diff --stat d808057 d93cc0e",
      "expected": "enacted s2.3(1): 'the audit office MAY append one legacy_no_identity marker ... and is signed by the filing office'; enacted s2.3(7): 'The audit office SHALL append the marker'",
      "id": "marker-filer-and-signature",
      "result": "pass"
    },
    {
      "actual": "Act 27 s3(2) and s3(3) carry all of it",
      "basis": "Act 27 s3(2)-(3)",
      "expected": "enacted s2.3(1)/(3): every pre-anchor row by position, introducing commit and SHA-256 at that commit; the pre-anchor/no-identity statement; the Clerk as default reviewer with the Judiciary on recorded unavailability; filing office and sponsor excluded; independence basis recorded; the three confirmations; a marker without that review has no effect",
      "id": "marker-content-and-reviewer",
      "result": "pass"
    },
    {
      "actual": "Act 27 s3(4) states this in substance and names used_cycle_tokens(). Residual: the enacted closing sentence 'the ordinary Act 17 rules then apply' is not restated, but s5 preserves those rules.",
      "basis": "Act 27 s3(4), s5",
      "expected": "enacted s2.3(4): an effective marker makes the checker treat marked rows as legacy_no_identity and permits at most one correction per case in the token cycle of the new correction; no cycle until that filing",
      "id": "current-cycle-definition",
      "result": "pass"
    },
    {
      "actual": "Act 27 s4 states all of it, sunset 2027-11-08 or the next Act 17 review",
      "basis": "Act 27 s4",
      "expected": "operational irregularity, not a retrospective breach; one operative consequence; sunset; Judiciary reliance report; non-precedent",
      "id": "irregular-but-preserved",
      "result": "pass"
    },
    {
      "actual": "Act 27 s6 enumerates seven and names state/audit-cycle-identities.tsv in (vii)",
      "basis": "Act 27 s6",
      "expected": "seven hermetic tests (i)-(vii), with (iii) against the introducing commit and (vii) against the named registry",
      "id": "seven-tests",
      "result": "pass"
    },
    {
      "actual": "Act 17 carries item 7, 'added by Act 27', stating the term is supplied by Act 27 s1 and the finality provisions of s2.6 are read subject to Act 27 ss2-4, ending 'No other provision of this Act is modified'. Items 1-6 unchanged.",
      "basis": "sed -n '/^## Act 17/,/^## Act 18/p' at d93cc0e; diff shows only the added item 7",
      "expected": "the amendment note inside the Act 17 entry, referencing Act 27 ss1-4, without altering Act 17's operative items",
      "id": "act17-amendment-note",
      "result": "pass"
    },
    {
      "actual": "exactly one row, tally 8-6-1-1, digest 1af1f602...",
      "basis": "grep -c '| audit-cycle-anchor-act |' records/ENACTMENT-STATUS.md = 1; git diff 95bd83a d93cc0e",
      "expected": "ENACTMENT-STATUS has exactly one Act 27 row",
      "id": "status-row",
      "result": "pass"
    },
    {
      "actual": "two paths: government/LAWS.md (63 insertions, 0 deletions \u2014 the new Act 27 entry plus the single Act 17 item 7 amendment note; no deletion, no other Act line altered) and records/ENACTMENT-STATUS.md (1 insertion, 0 deletions). The diff contains no removed content line.",
      "basis": "git diff --name-only 95bd83a d93cc0e; git diff --numstat -> '63 0 government/LAWS.md', '1 0 records/ENACTMENT-STATUS.md'",
      "expected": "no other Act changed in substance; list every changed path",
      "id": "no-other-act-changed",
      "result": "pass"
    },
    {
      "actual": "on main 95bd83a it reads 'enacted (Act 27)', seven tests i-vii, 'operational irregularity', the s2.3 + Act 17 s1 route, and 'Review date: 2027-11-08, or the next Act 17 review, whichever is earlier'",
      "basis": "git show 95bd83a:records/assumptions/audit-cycle-anchor-act.md",
      "expected": "Act 16 s2: the cited assumptions schedule describes the enacted text and carries an explicit review date",
      "id": "assumptions-schedule",
      "result": "pass"
    }
  ],
  "created_at": "2026-11-08T21:25:13Z",
  "independence_basis": "Audit member c1a0000b: not the sponsor (c1a00007), not the drafter (the Clerk c1a00001), and not the red-teamer (c1a00009). Disclosed interest: I wrote the Act 17 remedy investigation that prompted the bill and I am the audit office that the Act now names as filer; I did not vote on the bill (the ballot closed before my seat voted) and my recorded assessment was yes on the text. I failed two earlier candidates on substantive grounds, so the interest runs toward strictness here, not leniency.",
  "landing_authorisation": "fast_forward_main_to_this_exact_commit_only",
  "main_at_verification": "95bd83a9a62b5e05a9cd6b71da9c7e2db3992f0f",
  "parent": "95bd83a9a62b5e05a9cd6b71da9c7e2db3992f0f",
  "phase": "Phase 3 \u2014 pre-landing verification of the corrected Act 27 codification (candidate d93cc0e). Supersedes Phase 2 (d808057, fail) preserved at act27-codification-prelanding-c1a0000b-candidate-d808057.json, internal sha256 6fd583f327b4c6e14657b53a9c415b4d2363262c19e50bb875d5aeda410801d1, and Phase 1 (804619e, fail) preserved at act27-codification-prelanding-c1a0000b-candidate-804619e.json, internal sha256 9e6623166f5cd4a05574c41000e91c7bde91d9fd82c59dfb84e6c105f57c56b7. Neither is overwritten.",
  "reviewer": "c1a0000b",
  "schema": "act26-prelanding-record/v1",
  "sha256": "52ffe0398075e9349621208c829241e12b7a7513164391b3017e4d69f60a40b5",
  "tree": "32dd2def6f4fe061d21faea55c095c75b003dd30",
  "verdict": "pass"
}
```
