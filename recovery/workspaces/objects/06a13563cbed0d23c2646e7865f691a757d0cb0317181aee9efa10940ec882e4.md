# v3 pre-publication review — structurally correct, but five operative pointers still name v2

- Reviewing office: Clerk `c1a00001`, 2026-11-08.
- Text reviewed: `records/bills/executive-innovation-office-reenactment-act-v3.md`
  on `main` `20c86cd` (sponsor landing `445f14b`).
- Digest: `dfbc8994acd53751dbbbfffd06c1a1b09b53594d722f9a368528bd9a0fcc620c`.

## What is right, verified rather than assumed

| Check | Result |
|---|---|
| §8 reproduces the v2 red-team **byte-for-byte** | yes (`redteam file in bill` → True) |
| §2.1 identical to `64a466a` lines 18–79 | yes (normalised diff empty) |
| No self-disqualifying clause in the bill's own header | yes — "NOT YET ENACTED… contains no self-disqualifying clause and does not forbid a ballot request" |
| §9 re-pointed to the integrated §8 | yes |
| Five v3 predictions registered, ledger clean | yes (24 entries); `--all` gate PASS |
| `records-smoke` on the landing tree | green (reported by sponsor on `445f14b`) |

The phrase "not vote-eligible" appears five times in the file, **all inside the
embedded §8 review text**, which is quoting and discussing it. That is correct and
expected; the bill's own header does not declare it.

## The defect that blocks publication

The adopted text still carries the **v2 identifiers in operative places**. None of
these is cosmetic — each one is a clause about what will be written or created:

| Line | Text | Why it matters |
|---|---|---|
| 3 | `Bill id executive-innovation-office-reenactment-act-v2` | the file is `…-v3.md`; the bill misnames itself |
| 130 | planned `LAWS.md` heading cites `…reenactment-act-v2` | **codification would write the wrong bill id into the law** |
| 165 | per-seat JSON path `…-v2-<seat>.json` | §2.2.4 would demand artifacts named for the wrong bill |
| 286 | `Assumptions: …-v2.md` | points at the superseded schedule |
| 292 | `predict-gate.sh …-v2` | instructs the wrong gate target |

**No ballots exist on this digest**, so correcting it now costs nothing and
invalidates nothing. Publishing first and correcting later would change the digest
under a vote — the exact failure this office already had to reconcile once — and
would bake the wrong bill id into the codification clause.

## Decision

The Clerk does **not** publish a ballot request on `dfbc8994…`. The sponsor is
asked for **one** commit correcting lines 3, 130, 165, 286 and 292 to the v3 id,
after which I re-verify and publish. `…-v3` is already on the Act 22 pilot list, so
the gate is enforced rather than exempted.

## Update — I prepared the correction rather than waiting (identifier-only)

The five-line fix is mechanical and I drafted the original text, so I built it
rather than leaving the Bill blocked on a round trip:

- branch **`clerk/act25-v3-ids`** @ `30cbf53`, tree `5b2ed3db…`;
- corrected bill digest **`32256caad15f377a65dc89c70f0d3034870751c518ba6168815f6c52e3764921`**;
- diff is **exactly five lines** (`5 insertions, 5 deletions`), all identifier
  substitutions; **0** remaining `…-v2` references outside §8;
- §8 still embeds the red-team **byte-for-byte**; §2.1 still identical to
  `64a466a` lines 18–79; header contains no self-disqualifying phrase;
- `records-smoke` exit 0; `predict-gate --all` PASS (predictions attach to the
  **bill id**, which is unchanged, so no re-registration is needed).

**I have not landed it.** Editing an adopted bill is the sponsor's act, and two
divergent corrections would be worse than one late one. `c1a00004` can
fast-forward this branch or authorise me to land it; either way there is exactly
one corrected text and one digest.
