#!/bin/sh
# The launcher must provide a fresh general investigator after a terminal
# failure, without replaying the old tools or depending on failure classes.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
mkdir -p "$d/bin" "$d/home" "$d/town/government" "$d/seats" "$d/state" "$d/mock"
git init -q "$d/town"
git -C "$d/town" -c user.name=fixture -c user.email=fixture@example.com commit --allow-empty -qm start
cp "$repo/government/RECOVERY-STEWARD.md" "$d/town/government/"
cp "$repo/government/AGENT-REPORTING-POLICY.md" "$d/town/government/"
cp "$repo/government/delivery-candidates.py" "$d/town/government/"
printf 'test-authoritative-charter\n' > "$d/charter"
printf 'old-agent\n' > "$d/mock/registry"
cat > "$d/town/government/appointments.sh" <<'MOCK'
#!/bin/sh
case "$1" in
  ensure|resolve) cat "$MOCK_ROOT/registry" ;;
  replace)
    test "$2" = recovery-steward
    test "$3" = old-agent
    echo "$*" >> "$MOCK_ROOT/replacements"
    printf 'new-agent\n' > "$MOCK_ROOT/registry"
    printf 'new-agent\n' ;;
  *) exit 2 ;;
esac
MOCK
cat > "$d/bin/antonina" <<'MOCK'
#!/bin/sh
case "$1 $2" in
  'agent status')
    case "$4" in
      old-agent) echo '{"state":"failed","alive":false,"backend_error":{"classification":"unknown","transient":false,"automatic_retry_safe":false}}' ;;
      new-agent) echo '{"state":"clearexit","alive":false}' ;;
      *) exit 2 ;;
    esac ;;
  'agent run') printf '%s\n' "$@" >>"$MOCK_ROOT/runs" ;;
  *) exit 2 ;;
esac
MOCK
chmod +x "$d/bin/antonina" "$d/town/government/appointments.sh"
export PATH="$d/bin:$PATH" MOCK_ROOT="$d/mock"
export VICHE_TOWN_ROOT="$d/town" VICHE_SEATS_ROOT="$d/seats"
export VICHE_STATE_ROOT="$d/state" VICHE_CONSTITUTION="$d/charter"
# Exercise the service's actual profile/strict-mode prefix. Both errexit and
# nounset must remain disabled while the login profile initializes.
export HOME="$d/home"
awk '
  /^export VICHE_TOWNHALL_ID=/ { exit }
  /^\. \/home\/lubko\/\.profile$/ { print ". \"$HOME/.profile\""; next }
  { print }
' "$repo/government/recovery-steward-service.sh" > "$d/service-init.sh"
# A profile may reference variables that are absent from the supervisor env.
printf ': "$PROFILE_OPTIONAL"\nexport PROFILE_LOADED=yes\n' > "$HOME/.profile"
unset PROFILE_OPTIONAL PROFILE_LOADED
sh "$d/service-init.sh"
# A non-final failed profile command must not abort before later setup runs.
printf 'false\nexport PROFILE_LOADED=yes\n' > "$HOME/.profile"
unset PROFILE_LOADED
printf 'test "$PROFILE_LOADED" = yes\n' >> "$d/service-init.sh"
sh "$d/service-init.sh"
sh "$repo/government/recovery-steward-cycle.sh"
test "$(cat "$d/mock/registry")" = new-agent
test "$(wc -l < "$d/mock/replacements")" -eq 1
grep -Fq 'Fresh recovery investigator' "$d/mock/replacements"
grep -Fq 'general-purpose' "$d/mock/runs"
grep -Fq 'test-authoritative-charter' "$d/mock/runs"
test -d "$d/seats/branches/recovery-steward"
sh "$repo/government/recovery-steward-cycle.sh"
test "$(wc -l < "$d/mock/replacements")" -eq 1
test "$(grep -cx 'agent' "$d/mock/runs")" -eq 1
# Finished healthy session gets the next independent recovery cycle without
# replacing the appointment or replaying a prior invocation.
rm "$d/state/recovery-steward/last-dispatch"
sh "$repo/government/recovery-steward-cycle.sh"
test "$(wc -l < "$d/mock/replacements")" -eq 1
test "$(grep -cx 'agent' "$d/mock/runs")" -eq 2
echo 'Recovery steward fresh-session and non-replay smoke passed'
