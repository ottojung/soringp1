#!/bin/sh
# Fail-closed activation-authority binding: forged/wrong Act references,
# wrong-office replay, expiry/bounds, and boot/appointment/cycle agreement on
# one shared verifier. Uses only temp fixtures; never touches canonical records.
set -eu
cd "$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)"
verify=$(pwd -P)/government/knowledge-activation-verify.sh
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
mkdir -p "$d/town/government" "$d/town/records/knowledge"
export VICHE_TOWN_ROOT="$d/town"
laws=$d/town/government/LAWS.md
activation=$d/town/records/knowledge/activation.json
printf '%s\n' '## Act 42 — Institutional Knowledge and Communications Act (enacted 2026-11-19)' > "$laws"
now=$(date +%s)
nb=$((now - 60))
exp=$((now + 3600))

# write_activation OFFICE AUTHORIZED_BY ENABLED NOT_BEFORE EXPIRES_AT
write_activation() {
  jq -n --arg off "$1" --arg auth "$2" --argjson en "$3" \
        --argjson nb "$4" --argjson ex "$5" \
    '{schema:"viche-knowledge-activation-v1",
      offices:{($off):{enabled:$en,authorized_by:$auth,not_before:$nb,expires_at:$ex}}}' \
    > "$activation"
}

# expect EXIT DESCRIPTION OFFICE  (0 = verifier must pass, 1 = must fail closed)
expect() {
  want=$1; desc=$2; office=$3
  if /bin/sh "$verify" "$office" >/dev/null 2>&1; then got=0; else got=1; fi
  [ "$got" -eq "$want" ] || {
    echo "FAIL: $desc (expected exit $want, got $got)" >&2; exit 1;
  }
}

# Correct binding: exact enacted Act number and this exact office.
write_activation statistics "act:42:statistics" true "$nb" "$exp"
expect 0 'valid act+office binding passes' statistics
expect 1 'verifier rejects an unknown office name' spying

# Forged / wrong Act references and cross-office replay all fail closed.
write_activation statistics "act:fake" true "$nb" "$exp"
expect 1 'bare forged act reference fails' statistics
write_activation statistics "act:" true "$nb" "$exp"
expect 1 'empty act reference fails' statistics
write_activation statistics "act:31:statistics" true "$nb" "$exp"
expect 1 'wrong (other) Act number fails' statistics
write_activation statistics "act:42:spying" true "$nb" "$exp"
expect 1 "another office's authorization cannot be replayed" statistics
write_activation statistics "act:42" true "$nb" "$exp"
expect 1 'authorization missing office binding fails' statistics
write_activation statistics "act:42:statistics:extra" true "$nb" "$exp"
expect 1 'authorization with extra suffix fails' statistics
write_activation statistics "act:42:STATISTICS" true "$nb" "$exp"
expect 1 'case-mismatched office fails' statistics

# Non-string and structurally absent fields fail closed.
write_activation statistics "act:42:statistics" true "$nb" "$exp"
jq '.offices.statistics.authorized_by=42' "$activation" > "$d/new" && mv "$d/new" "$activation"
expect 1 'non-string authorized_by fails' statistics
write_activation statistics "act:42:statistics" true "$nb" "$exp"
jq 'del(.offices.statistics)' "$activation" > "$d/new" && mv "$d/new" "$activation"
expect 1 'missing office record fails' statistics
write_activation statistics "act:42:statistics" true "$nb" "$exp"
printf 'not json' > "$activation"
expect 1 'malformed activation JSON fails' statistics

# Expiry and window bounds fail closed.
write_activation statistics "act:42:statistics" true "$((now - 7200))" "$((now - 60))"
expect 1 'expired activation fails' statistics
write_activation statistics "act:42:statistics" true "$((now + 60))" "$((now + 7200))"
expect 1 'not-yet-valid activation fails' statistics
write_activation statistics "act:42:statistics" true "$exp" "$nb"
expect 1 'inverted time window fails' statistics
write_activation statistics "act:42:statistics" true "$nb" "$((now + 3888001))"
expect 1 'over-long term fails' statistics
write_activation statistics "act:42:statistics" false "$nb" "$exp"
expect 1 'disabled office fails' statistics

# Enactment ambiguity / absence fails closed.
write_activation statistics "act:42:statistics" true "$nb" "$exp"
printf '%s\n' '## Act 99 — Some Other Act (enacted 2026-01-01)' > "$laws"
expect 1 'no enacted IKCA header fails' statistics
printf '%s\n' \
  '## Act 42 — Institutional Knowledge and Communications Act (enacted 2026-11-19)' \
  '## Act 43 — Institutional Knowledge and Communications Act (enacted 2026-11-20)' > "$laws"
expect 1 'ambiguous IKCA Act number fails' statistics

# Boot, appointments and the office cycle must all delegate to the one verifier
# and none may retain the weak startswith("act:") predicate.
for f in government/boot.sh government/appointments.sh government/knowledge-office-cycle.sh; do
  grep -q 'knowledge-activation-verify.sh' "$f" || {
    echo "FAIL: $f does not use the shared verifier" >&2; exit 1;
  }
  if grep -q 'startswith("act:")' "$f"; then
    echo "FAIL: $f retains the weak act-prefix predicate" >&2; exit 1
  fi
done
if grep -q 'startswith("act:")' government/knowledge-activation-verify.sh; then
  echo 'FAIL: shared verifier retains the weak act-prefix predicate' >&2; exit 1
fi

echo 'knowledge activation binding: forged/wrong-Act/wrong-office/expiry rejected; boot+appointments+cycle agree'
