#!/bin/sh
# Fail-closed shared verifier for Institutional Knowledge Act office activation.
#
# Exits 0 ONLY when both hold:
#   (a) exactly one Institutional Knowledge and Communications Act is enacted in
#       canonical LAWS.md (the Act number is parsed at runtime, never hardcoded);
#   (b) the named office has a live activation whose authorized_by binds BOTH
#       that exact enacted Act number AND this exact office, inside a bounded
#       and currently valid time window.
#
# A bare "act:" prefix, a different Act number, another office's authorization,
# a missing/malformed field, malformed JSON or an absent record all fail closed.
# boot.sh, appointments.sh and knowledge-office-cycle.sh all use this one file
# so their activation decisions cannot drift apart. POSIX sh; no bashisms.
set -eu

office=${1:-}
town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}

case "$office" in
  statistics|foresight|strategy|spying) ;;
  *) exit 1 ;;
esac

laws=$town/government/LAWS.md
[ -s "$laws" ] || exit 1

# Require exactly one distinct enacted IKCA Act number. Ambiguity fails closed.
act_nums=$(
  sed -n 's/^## Act \([0-9][0-9]*\) — Institutional Knowledge and Communications Act (enacted .*/\1/p' "$laws" |
    sort -u
)
[ -n "$act_nums" ] || exit 1
[ "$(printf '%s\n' "$act_nums" | wc -l)" -eq 1 ] || exit 1
act_num=$act_nums

activation=$town/records/knowledge/activation.json
[ -s "$activation" ] || exit 1
now=$(date +%s)

# authorized_by must be exactly "act:<ACT_NUMBER>:<OFFICE>". This binds the
# specific enacted Act and the specific office; it cannot be replayed for a
# different office or satisfy a forged/generic Act reference.
jq -e \
  --arg office "$office" \
  --arg expect "act:$act_num:$office" \
  --argjson now "$now" '
    .schema=="viche-knowledge-activation-v1" and
    (.offices[$office].enabled==true) and
    (.offices[$office].authorized_by|type=="string") and
    (.offices[$office].authorized_by==$expect) and
    (.offices[$office].not_before|type=="number") and
    (.offices[$office].expires_at|type=="number") and
    ((.offices[$office].expires_at - .offices[$office].not_before) > 0) and
    ((.offices[$office].expires_at - .offices[$office].not_before) <= 3888000) and
    (.offices[$office].not_before <= $now) and
    (.offices[$office].expires_at > $now)
  ' "$activation" >/dev/null
