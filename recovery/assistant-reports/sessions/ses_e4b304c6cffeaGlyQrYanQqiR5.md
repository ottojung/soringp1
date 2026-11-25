# antonina-tgGeQVnWsaLSqkw3VamSoI-goes

Session: ses_e4b304c6cffeaGlyQrYanQqiR5
Workspace: /home/lubko/soring-fronts/exec-act19-prepared-provenance-20261107
Created: 1794034873238; updated: 1794034982656

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b4cfb3b40019aABIlKLHZoo3X)

I’ll inspect the isolated candidate’s exact diff and reviewer notes first, then make only the requested narrow changes without disturbing existing edits. I’ll verify the focused shell/dash integrations and report the resulting diff hash separately from any approval status.

## Output 71 (msg_1b4d0a2bf0010pFXfgFoZk2O5g)

The concrete recovery distinction is sound when the registry row includes the same transaction as the prepared intent, but the old registry format is two fields. I’m adding the explicit pre-swap case against that legacy row and keeping the strict three-field/transaction validation in recovery. I also found bootstrap startup was attempting stale-lock deletion in the PID-publication window; it now waits boundedly or fails closed instead.

## Output 101 (msg_1b4d1493b001aaJPEB5Bb1VdB5)

Implemented the requested narrow fixes in the isolated candidate:

- `appointments.sh` validates every registry row before any rewrite, rejecting malformed fields, empty required values, invalid IDs/transactions, and duplicate keys. Added regressions for malformed and duplicate unrelated rows.
- Bootstrap now fails closed on an ambiguous appointment lock and never removes a lock during the mkdir-to-PID publication gap.
- Recovery still requires a unique three-field registry row whose successor and transaction match durable intent/provenance. Added a pre-swap recovery refusal test; the existing post-swap crash recovery test still passes.

**Verification:** `/bin/sh` and `dash` syntax checks passed; appointment smoke, appointment recovery integration, Act 19 continuity, and continuity incident smoke passed; `git diff --check` passed.

Diff SHA-256: `749d3db969569bfed76b6704a49a97ea492dbf5bf39c6b335cc48ab812d5b56a`

No commit, post, or delivery was made. This reports test outcomes, not reviewer approval.
