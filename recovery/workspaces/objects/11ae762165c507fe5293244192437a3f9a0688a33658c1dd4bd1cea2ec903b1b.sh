#!/bin/sh
# Sentinel Git-probe calibration (records/SENTINEL-CALIBRATION-2026-10-21-...).
# A load-induced read-only Git timeout must be retried before the Sentinel
# declares government_git_unreadable, and a timeout must be distinguishable from
# a genuine Git error. Hermetic: mock git/s6-svstat/antonina, scratch town, no
# board writes and no live service.
set -eu
root=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
export SCRATCH=$scratch
mkdir -p "$scratch/bin" "$scratch/town/.git" "$scratch/oversight" "$scratch/health"
# Fresh setup/oversight stamps so only the Git probe can produce a signal.
printf '200000\t0\tidle\t0\t0\tnone\tclear\n' > "$scratch/oversight/observations.tsv"
printf '200000\n' > "$scratch/health/government-setup.last"

cat > "$scratch/bin/s6-svstat" <<'MOCK'
#!/bin/sh
echo 'up (pid 10 pgid 10) 200 seconds'
MOCK
cat > "$scratch/bin/antonina" <<'MOCK'
#!/bin/sh
exit 1
MOCK
# Mock git: the `ls-files` probe times out on its first attempt (sleep longer
# than the 1 s probe timeout) and then succeeds, unless a flag makes it always
# time out or always error. `rev-list` always succeeds.
cat > "$scratch/bin/git" <<'MOCK'
#!/bin/sh
cmd=
for a in "$@"; do
    case "$a" in ls-files|rev-list) cmd=$a;; esac
done
case "$cmd" in
ls-files)
    n=0
    [ -f "$SCRATCH/ls_count" ] && n=$(cat "$SCRATCH/ls_count")
    n=$((n + 1))
    printf '%s\n' "$n" > "$SCRATCH/ls_count"
    [ -f "$SCRATCH/ls_error" ] && exit 1
    if [ -f "$SCRATCH/ls_always_timeout" ] || [ "$n" -eq 1 ]; then
        sleep 3
    fi
    exit 0 ;;
rev-list)
    printf '0\t0\n'
    exit 0 ;;
*)
    exit 0 ;;
esac
MOCK
chmod +x "$scratch/bin/s6-svstat" "$scratch/bin/antonina" "$scratch/bin/git"

PATH="$scratch/bin:$PATH"
VICHE_TOWN_ROOT=$scratch/town
VICHE_OVERSIGHT_STATE=$scratch/oversight
VICHE_GOV_HEALTH_STATE=$scratch/health
VICHE_TOWNHALL_ID=999
VICHE_SENTINEL_GIT_PROBE_ATTEMPTS=3
VICHE_SENTINEL_GIT_PROBE_TIMEOUT=1
VICHE_SENTINEL_GIT_PROBE_BACKOFF=0
export PATH VICHE_TOWN_ROOT VICHE_OVERSIGHT_STATE VICHE_GOV_HEALTH_STATE
export VICHE_TOWNHALL_ID VICHE_SENTINEL_GIT_PROBE_ATTEMPTS
export VICHE_SENTINEL_GIT_PROBE_TIMEOUT VICHE_SENTINEL_GIT_PROBE_BACKOFF

run() { VICHE_SENTINEL_STATE=$1 VICHE_SENTINEL_NOW=$2 /bin/sh "$root/sentinel/check.sh"; }

# 1. Slow first attempt, recovers on retry: no incident, git_status=ok.
rm -f "$scratch/ls_count"
run "$scratch/state1" 200000
[ ! -e "$scratch/state1/incident.json" ]
last=$(tail -n 1 "$scratch/state1/checks.tsv")
[ "$(printf '%s\n' "$last" | cut -f3)" = ok ]
[ "$(printf '%s\n' "$last" | cut -f8)" = clear ]
[ "$(cat "$scratch/ls_count")" -eq 2 ] # one retry after the timeout

# 2. Persistent timeout: unreadable AND a distinct timeout signal; all attempts used.
rm -f "$scratch/ls_count"
: > "$scratch/ls_always_timeout"
run "$scratch/state2" 200001
[ -s "$scratch/state2/incident.json" ]
jq -e '.git=="unreadable"
       and (.signals|index("government_git_unreadable"))
       and (.signals|index("government_git_probe_timeout"))' \
    "$scratch/state2/incident.json" >/dev/null
[ "$(cat "$scratch/ls_count")" -eq 3 ] # all attempts exhausted
rm -f "$scratch/ls_always_timeout"

# 3. Genuine Git error: unreadable but NOT a timeout signal, and no retry.
rm -f "$scratch/ls_count"
: > "$scratch/ls_error"
run "$scratch/state3" 200002
jq -e '.git=="unreadable"
       and (.signals|index("government_git_unreadable"))
       and ((.signals|index("government_git_probe_timeout"))|not)' \
    "$scratch/state3/incident.json" >/dev/null
[ "$(cat "$scratch/ls_count")" -eq 1 ] # a genuine error is not retried
rm -f "$scratch/ls_error"

echo 'Sentinel git-probe retry smoke passed'
