#!/bin/sh
# Hermetic test for the CA-M delivery-age signal (oversight incident 1792107382).
#
# The watchdog's delivery signal must reflect the NEWEST commit across
# origin/main AND every origin/release/* ref, not origin/main alone. This proves:
#   (A) a fresh commit on origin/release/* suppresses the false positive even
#       when origin/main is stale (the 1792107382 measurement artifact);
#   (B) a genuinely idle repo (main AND release both stale) still triggers;
#   (C) origin/main alone is still measured (stale main, no release refs -> signal;
#       fresh main, no release refs -> no signal).
#
# POSIX /bin/sh only; no bashisms. Uses the same mock-antonina pattern as
# tests/oversight-smoke.sh.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM

mkdir -p "$scratch/bin" "$scratch/town/records" "$scratch/state"

# --- mock antonina (board list + agent status) ---
cat > "$scratch/bin/antonina" <<'MOCK'
#!/bin/sh
set -eu
case "$1 $2" in
"board list") printf '%s\n' "$MOCK_BOARD" ;;
"agent status") printf '{"state":"running","last_activity_at":%s,"backend_error":{"classification":"none"}}\n' "$LAST" ;;
*) exit 90 ;;
esac
MOCK
chmod +x "$scratch/bin/antonina"

MOCK_BOARD='[{"number":1,"title":"Kawun: delivery"}]'
LAST=2000000000
PATH=$scratch/bin:$PATH
export PATH MOCK_BOARD LAST

NOW=2000000000
VICHE_OVERSIGHT_NOW=$NOW
mkdir -p "$scratch/town/government"
cp "$repo/tests/appointment-id-stub.sh" "$scratch/town/government/appointments.sh"
VICHE_TOWN_ROOT=$scratch/town
VICHE_STATE_ROOT=$scratch/state
VICHE_KAWUN_REPO=$scratch/kawun
VICHE_TOWNHALL_ID=302
VICHE_OVERSIGHT_FETCH=0
export VICHE_OVERSIGHT_NOW VICHE_TOWN_ROOT VICHE_STATE_ROOT VICHE_KAWUN_REPO
export VICHE_TOWNHALL_ID VICHE_OVERSIGHT_FETCH

kawun=$scratch/kawun
incident=$scratch/state/oversight/incident.json

# build_case <main_epoch> <release_epoch|empty>
# Creates a Kawun-like repo. The release commit is a child of the main commit,
# mirroring the real repo where the release line is ahead of main.
build_case() {
    rm -rf "$kawun"
    git init -q "$kawun"
    GIT_AUTHOR_DATE="@$1 +0000" GIT_COMMITTER_DATE="@$1 +0000" \
        git -C "$kawun" -c user.email=t@t -c user.name=t commit -q --allow-empty -m m
    main_sha=$(git -C "$kawun" rev-parse HEAD)
    git -C "$kawun" update-ref refs/remotes/origin/main "$main_sha"
    if [ -n "${2:-}" ]; then
        GIT_AUTHOR_DATE="@$2 +0000" GIT_COMMITTER_DATE="@$2 +0000" \
            git -C "$kawun" -c user.email=t@t -c user.name=t commit -q --allow-empty -m r
        rel_sha=$(git -C "$kawun" rev-parse HEAD)
        git -C "$kawun" update-ref refs/remotes/origin/release/along-long-namespace "$rel_sha"
    fi
}

run_watch() {
    rm -rf "$scratch/state/oversight"
    /bin/sh "$repo/government/oversight-watch.sh" >/dev/null 2>&1
}

DAY=86400

# (A) fresh release line, stale main -> false positive SUPPRESSED.
#     main ~2.3 days old, release 60s old. delivery_age=60 (<DAY), main_age>DAY.
build_case $((NOW - 200000)) $((NOW - 60))
run_watch
if [ -e "$incident" ]; then
    echo "FAIL (A): fresh release line must suppress no_recent_main_commit" >&2
    exit 1
fi
echo "PASS (A): fresh origin/release/* commit suppresses the false positive"

# (B) genuinely idle: main AND release both stale -> still triggers.
#     main ~4.6 days, release ~2.3 days (newer than main, still >DAY).
build_case $((NOW - 400000)) $((NOW - 200000))
run_watch
jq -e --argjson now "$NOW" '.signals | index("no_recent_main_commit")' "$incident" >/dev/null
jq -e --argjson now "$NOW" '.local_delivery_commit_age_seconds >= 86400' "$incident" >/dev/null
echo "PASS (B): idle repo (main+release stale) still triggers; delivery_age>=86400"

# (C1) origin/main alone, stale, no release refs -> still triggers (no weakening).
build_case $((NOW - 400000)) ""
run_watch
jq -e '.signals | index("no_recent_main_commit")' "$incident" >/dev/null
jq -e '.local_main_commit_age_seconds >= 86400' "$incident" >/dev/null
echo "PASS (C1): stale origin/main with no release refs still triggers"

# (C2) origin/main alone, fresh, no release refs -> no signal.
build_case $((NOW - 60)) ""
run_watch
if [ -e "$incident" ]; then
    echo "FAIL (C2): fresh origin/main must not trigger" >&2
    exit 1
fi
echo "PASS (C2): fresh origin/main with no release refs does not trigger"

echo 'Oversight release-signal smoke checks passed'
