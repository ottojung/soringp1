#!/bin/sh
# Deterministic TERM interruption while appointments.sh owns its lock.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
mkdir -p "$d/bin" "$d/town/government" "$d/state/appointments" "$d/seats/branches/executive"
printf 'other\tOther\tother\n' > "$d/town/government/seats.tsv"
printf 'executive\told-id\n' > "$d/state/appointments/appointments.tsv"
git -C "$d/seats/branches/executive" init -q
git -C "$d/seats/branches/executive" -c user.name=test -c user.email=test@example.test commit --allow-empty -qm baseline
export VICHE_STATE_ROOT=$d/state VICHE_TOWN_ROOT=$d/town VICHE_SEATS_ROOT=$d/seats

cat > "$d/bin/antonina" <<'MOCK'
#!/bin/sh
set -eu
if [ "$1 $2" = 'agent new' ]; then echo new-id
elif [ "$1 $2" = 'agent status' ]; then
  if [ "$4" = old-id ]; then echo '{"state":"stopped"}'
  else echo '{"state":"idle"}'; fi
else exit 2
fi
MOCK
chmod +x "$d/bin/antonina"
PATH=$d/bin:$PATH; export PATH

for sh in /bin/sh "$(command -v dash)"; do
  for sig in TERM HUP; do
    printf 'executive\told-id\n' > "$d/state/appointments/appointments.tsv"
    rm -rf "$d/state/appointments/replacement-intents"
    rm -f "$d/state/appointments/replacement-provenance.jsonl"
    gate=$d/gate-$(basename "$sh")-$sig
    rm -f "$gate" "$gate.release"
    # A private session makes setsid's child PID the script process; signal
    # only that PID, not its process group (which also contains gate sleeps).
    setsid env VICHE_TEST_APPOINTMENT_GATE="$gate" \
      VICHE_STATE_ROOT="$d/state" VICHE_TOWN_ROOT="$d/town" VICHE_SEATS_ROOT="$d/seats" \
      PATH="$PATH" \
      "$sh" "$repo/government/appointments.sh" replace executive old-id signal-test fixture test \
      >"$d/out" 2>&1 &
    child=$!
    i=0
    while [ ! -e "$gate" ] && [ "$i" -lt 100 ]; do i=$((i+1)); sleep 0.05; done
    if [ ! -e "$gate" ]; then echo "appointment gate not reached under $sh/$sig" >&2; kill -TERM "$child" 2>/dev/null || :; wait "$child" 2>/dev/null || :; exit 1; fi
    kill -"$sig" "$child"
    rc=0; wait "$child" || rc=$?
    expected=0
    case "$sig" in TERM) expected=143;; HUP) expected=129;; esac
    [ "$rc" -eq "$expected" ] || { echo "expected $sig exit $expected under $sh, got $rc" >&2; exit 1; }
    [ ! -d "$d/state/appointments/lock" ] || { echo "appointment lock leaked under $sh/$sig" >&2; exit 1; }
    [ "$(cat "$d/state/appointments/appointments.tsv")" = "executive$(printf '\t')old-id" ] || { echo "registry changed under $sh/$sig" >&2; exit 1; }
    result=$(env VICHE_STATE_ROOT="$d/state" VICHE_TOWN_ROOT="$d/town" VICHE_SEATS_ROOT="$d/seats" \
      PATH="$PATH" "$sh" "$repo/government/appointments.sh" replace executive old-id signal-test fixture retry)
    [ "$result" = new-id ] || { echo "retry did not complete under $sh/$sig" >&2; exit 1; }
  done
  # Simulate lock-path replacement while the owner is paused. Its EXIT cleanup
  # must not erase a different PID's lock, even if its in-memory flag is yes.
  printf 'executive\told-id\n' > "$d/state/appointments/appointments.tsv"
  rm -rf "$d/state/appointments/replacement-intents"
  rm -f "$d/state/appointments/replacement-provenance.jsonl"
  gate=$d/gate-replaced-$(basename "$sh")
  rm -f "$gate" "$gate.release"
  setsid env VICHE_TEST_APPOINTMENT_GATE="$gate" \
    VICHE_STATE_ROOT="$d/state" VICHE_TOWN_ROOT="$d/town" VICHE_SEATS_ROOT="$d/seats" \
    PATH="$PATH" \
    "$sh" "$repo/government/appointments.sh" replace executive old-id signal-test fixture replaced \
    >"$d/out" 2>&1 &
  child=$!
  i=0
  while [ ! -e "$gate" ] && [ "$i" -lt 100 ]; do i=$((i+1)); sleep 0.05; done
  [ -e "$gate" ] || { echo "replacement gate not reached under $sh" >&2; exit 1; }
  rm -f "$d/state/appointments/lock/pid"
  rmdir "$d/state/appointments/lock"
  mkdir "$d/state/appointments/lock"
  printf '99999999\n' > "$d/state/appointments/lock/pid"
  kill -TERM "$child"
  rc=0; wait "$child" || rc=$?
  [ "$rc" -eq 143 ] || { echo "replaced-lock termination status under $sh: $rc" >&2; exit 1; }
  [ "$(cat "$d/state/appointments/lock/pid")" = 99999999 ] || { echo "cleanup erased foreign lock under $sh" >&2; exit 1; }
  [ "$(cat "$d/state/appointments/appointments.tsv")" = "executive$(printf '\t')old-id" ] || { echo "registry changed after replacement under $sh" >&2; exit 1; }
  rm -rf "$d/state/appointments/lock"
  result=$(env VICHE_STATE_ROOT="$d/state" VICHE_TOWN_ROOT="$d/town" VICHE_SEATS_ROOT="$d/seats" \
    PATH="$PATH" "$sh" "$repo/government/appointments.sh" replace executive old-id signal-test fixture retry-replaced)
  [ "$result" = new-id ] || { echo "replacement retry did not complete under $sh" >&2; exit 1; }
done
echo 'Act 19 signal trap smoke passed'
