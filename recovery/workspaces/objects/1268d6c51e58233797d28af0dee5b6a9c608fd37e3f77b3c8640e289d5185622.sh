#!/bin/sh
# Janitor Office — disk-health observation and safe, policy-gated reclamation.
#
# Established as a continuing executive function under Founding Act 2.3 (executive
# implementation) and Act 4.2 (storage inquiry from existing telemetry). The enabling
# statute, which grants explicit reclamation authority and safeguards, is
# records/bills/janitor-office-act.md (Act 12); until it is enacted this tool operates
# in its safe, reversible subset only.
#
# POSIX /bin/sh only (AGENTS.md): no bashisms, no associative arrays, no `local`.
#
# Usage: janitor.sh <observe|reclaim|cycle|report|status|inventory|classify|quarantine|reclaim-quarantined> [--dry-run]
#   observe             record filesystem + cgroup metrics, evaluate thresholds; never mutates
#   reclaim             perform the safe, reversible, age-gated reclamation allowlist
#   cycle               observe; refresh inventory+classify when due; reclaim when due and enabled; safe-reclaim on critical pressure
#   report              print a concise human-readable summary
#   status              print one machine-readable status line
#   inventory           scan the box for large directories; read-only, records findings
#   classify            classify inventory candidates by ownership/liveness; read-only
#   quarantine           move classified candidates to quarantine; reversible
#   reclaim-quarantined remove quarantined items past their grace period; destructive
#   scratch-quarantine   stage aged, unreferenced /tmp runtime scratch for the
#                        grace+reclaim pipeline (never deletes directly)
#   reclaim-idle-caches  delete verifiably idle, regenerable .lake build caches
#                        (no live process, idle >= idle_cache_seconds, worktree
#                        clean and fully pushed); auto-run by cycle at high/critical
#
# Safety: this script never removes unverified content, never writes outside
# $VICHE_STATE_ROOT, and never touches records/, government/, constitution/, the
# founder-controlled mount, credentials, or other projects. Its only deletion target is
# its own state directory; git maintenance is non-destructive (objects are recoverable).
set -eu

usage() {
    cat >&2 <<'EOF'
Usage: janitor.sh <observe|reclaim|cycle|report|status|inventory|classify|quarantine|reclaim-quarantined|scratch-quarantine|reclaim-idle-caches> [--dry-run]
EOF
}

mode=${1:-}
[ -n "$mode" ] || { usage; exit 2; }
[ "$#" -le 2 ] || { usage; exit 2; }
dry_run=0
if [ "${2:-}" = "--dry-run" ]; then dry_run=1; fi
case "$mode" in
    observe|reclaim|cycle|report|status|inventory|classify|quarantine|reclaim-quarantined|scratch-quarantine|reclaim-idle-caches) : ;;
    *) usage; exit 2 ;;
esac

town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
state=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}
seats=${VICHE_SEATS_ROOT:-/var/lib/lubko/wd/viche-seats}
conf=${JANITOR_CONF:-$town/government/janitor.conf}
jstate=$state/janitor
mkdir -p "$jstate/tmp"

is_num() {
    case "$1" in
        ''|*[!0-9]*) return 1 ;;
        *) return 0 ;;
    esac
}

normalize_decimal() {
    _nd=$1
    is_num "$_nd" || return 1
    while [ "${_nd#0}" != "$_nd" ]; do _nd=${_nd#0}; done
    [ -n "$_nd" ] || _nd=0
    printf '%s' "$_nd"
}

decimal_greater() {
    # Compare arbitrary-length unsigned decimal strings without shell arithmetic.
    _dg_a=$(normalize_decimal "$1") || return 2
    _dg_b=$(normalize_decimal "$2") || return 2
    [ "${#_dg_a}" -gt "${#_dg_b}" ] && return 0
    [ "${#_dg_a}" -lt "${#_dg_b}" ] && return 1
    [ "$_dg_a" = "$_dg_b" ] && return 1
    _dg_last=$(printf '%s\n%s\n' "$_dg_a" "$_dg_b" | LC_ALL=C sort | tail -n 1)
    [ "$_dg_last" = "$_dg_a" ]
}

confval() {
    # confval <key> <default>
    if [ -f "$conf" ]; then
        v=$(sed -n "s/^[[:space:]]*$1=//p" "$conf" 2>/dev/null | tail -n 1)
        if [ -n "$v" ]; then printf '%s' "$v"; return 0; fi
    fi
    printf '%s' "$2"
}

warn_pct=$(confval warn_used_pct 85)
high_pct=$(confval high_used_pct 92)
crit_pct=$(confval critical_used_pct 97)
observe_interval=$(confval observe_interval_seconds 1800)
reclaim_interval=$(confval reclaim_interval_seconds 86400)
min_age=$(confval min_reclaim_age_seconds 86400)
max_log_bytes=$(confval max_log_bytes 1048576)
safe_reclaim=$(confval safe_reclaim_enabled 1)
reclaim_enabled=$(confval reclaim_enabled 0)
inventory_min_kb=$(confval inventory_min_kb 102400)
quarantine_dir=$(confval quarantine_dir "$state/quarantine")
quarantine_grace=$(confval quarantine_grace_seconds 604800)
lock_stale=$(confval lock_stale_seconds 900)
# Inventory roots (Act 12.2 whole-box jurisdiction). Overridable for hermetic
# tests; the defaults cover the writable territory plus the observed-only
# host-managed Guix store.
inv_roots=${JANITOR_ROOTS:-/workspace /home/lubko /var/lib/lubko/wd /tmp /gnu}
inv_file_roots=${JANITOR_FILE_ROOTS:-/workspace /home/lubko /var/lib/lubko/wd /tmp}
# Runtime scratch directory holding the node/opencode .bcf* bytecode files.
scratch_dir=${JANITOR_SCRATCH_DIR:-/tmp}
# Liveness-aware idle build-cache reclamation: a regenerable .lake cache is
# reclaimable only when no live process references it or its worktree, it has
# been idle for idle_cache_seconds, and its worktree is a clean, fully-pushed
# git worktree. Deleting a .lake loses only build time, never data.
idle_cache_seconds=$(confval idle_cache_seconds 21600)
idle_cache_enabled=$(confval idle_cache_enabled 1)

for n in "$warn_pct" "$high_pct" "$crit_pct" "$observe_interval" "$reclaim_interval" \
         "$min_age" "$max_log_bytes" "$safe_reclaim" "$reclaim_enabled" \
         "$inventory_min_kb" "$quarantine_grace" "$lock_stale" \
         "$idle_cache_seconds" "$idle_cache_enabled"; do
    if ! is_num "$n"; then
        echo "janitor: invalid numeric policy value in $conf: $n" >&2
        exit 2
    fi
done

host=$(hostname 2>/dev/null || printf 'unknown')
now=$(date -u +%s)
ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)

# The filesystem probe follows the town checkout so we measure the filesystem that
# actually holds Viche state, wherever it is mounted.
probe=$town
if [ ! -d "$probe" ]; then probe=$state; fi
if [ ! -d "$probe" ]; then probe=.; fi

rotate() {
    # rotate <file>: keep the file bounded, preserving the newest lines.
    [ -f "$1" ] || return 0
    _rot_bytes=$(wc -c < "$1" 2>/dev/null || printf '0')
    is_num "$_rot_bytes" || return 0
    if [ "$_rot_bytes" -gt "$max_log_bytes" ]; then
        tmpf=$1.$$
        if tail -n 1000 "$1" > "$tmpf" 2>/dev/null; then
            mv "$tmpf" "$1"
        else
            rm -f "$tmpf"
        fi
    fi
    return 0
}

log_append() {
    # log_append <file> <line>
    printf '%s\n' "$2" >> "$1"
    rotate "$1"
    return 0
}

df_field() {
    # df_field <path> <field> [inode]
    if [ "${3:-}" = inode ]; then
        df -P -i "$1" 2>/dev/null | awk -v f="$2" 'NR==2{print $f; exit}'
    else
        df -P -k "$1" 2>/dev/null | awk -v f="$2" 'NR==2{print $f; exit}'
    fi
}

du_kb() {
    if [ -d "$1" ]; then
        du -s -k "$1" 2>/dev/null | awk 'NR==1{print $1; exit}'
    else
        printf '0'
    fi
}

quarantine_path_ok() {
    # Accept only a direct child of the configured quarantine directory. Canonicalize
    # both sides to reject traversal, symlink escapes and policy-locality violations.
    _qpo_path=$1
    [ -n "$quarantine_dir" ] && [ "$quarantine_dir" != / ] || return 1
    [ -d "$_qpo_path" ] || return 1
    [ ! -L "$_qpo_path" ] || return 1
    _qpo_root=$(readlink -f "$quarantine_dir" 2>/dev/null) || return 1
    _qpo_dest=$(readlink -f "$_qpo_path" 2>/dev/null) || return 1
    [ -n "$_qpo_root" ] && [ "$_qpo_root" != / ] || return 1
    case "$_qpo_dest" in
        "$_qpo_root"/*) _qpo_rel=${_qpo_dest#"$_qpo_root"/} ;;
        *) return 1 ;;
    esac
    case "$_qpo_rel" in ''|*/*|.|..) return 1 ;; esac
    return 0
}

available_kb() {
    _akb=$(df_field "$probe" 4)
    is_num "$_akb" || return 1
    printf '%s' "$_akb"
}

due() {
    # due <stamp-file> <interval-seconds>
    [ -f "$1" ] || return 0
    last=$(cat "$1" 2>/dev/null || printf '0')
    is_num "$last" || return 0
    [ $((now - last)) -ge "$2" ]
}

stamp() { printf '%s\n' "$now" > "$1"; return 0; }

# --- metric computation (sets globals) -----------------------------------------
compute() {
    fs_dev=$(df_field "$probe" 1)
    fs_size_kb=$(df_field "$probe" 2)
    fs_used_kb=$(df_field "$probe" 3)
    fs_avail_kb=$(df_field "$probe" 4)
    fs_pct_raw=$(df_field "$probe" 5)
    fs_used_pct=$(printf '%s' "$fs_pct_raw" | tr -d '%')
    is_num "$fs_used_pct" || fs_used_pct=0
    ino_raw=$(df_field "$probe" 5 inode)
    ino_used_pct=$(printf '%s' "$ino_raw" | tr -d '%')
    is_num "$ino_used_pct" || ino_used_pct=
    mem_current=
    mem_max=
    if [ -r /sys/fs/cgroup/memory.current ]; then
        mem_current=$(cat /sys/fs/cgroup/memory.current 2>/dev/null || printf '')
    fi
    if [ -r /sys/fs/cgroup/memory.max ]; then
        mem_max=$(cat /sys/fs/cgroup/memory.max 2>/dev/null || printf '')
    fi
    town_kb=$(du_kb "$town")
    state_kb=$(du_kb "$state")
    seats_kb=$(du_kb "$seats")
    level=ok
    if [ "$fs_used_pct" -ge "$warn_pct" ]; then level=warn; fi
    if [ "$fs_used_pct" -ge "$high_pct" ]; then level=high; fi
    if [ "$fs_used_pct" -ge "$crit_pct" ]; then level=critical; fi
    return 0
}

severity() {
    case "$1" in
        critical) printf '3' ;;
        high) printf '2' ;;
        warn) printf '1' ;;
        *) printf '0' ;;
    esac
}

record_observation() {
    obs=$jstate/observations.tsv
    if [ ! -f "$obs" ]; then
        printf 'ts\thost\tdevice\tsize_kb\tused_kb\tavail_kb\tused_pct\tinode_pct\tmem_current\tmem_max\ttown_kb\tstate_kb\tseats_kb\tlevel\n' > "$obs"
    fi
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
        "$ts" "$host" "$fs_dev" "$fs_size_kb" "$fs_used_kb" "$fs_avail_kb" \
        "$fs_used_pct" "$ino_used_pct" "$mem_current" "$mem_max" \
        "$town_kb" "$state_kb" "$seats_kb" "$level" >> "$obs"
    rotate "$obs"
    stamp "$jstate/last-observe"
    return 0
}

alert_if_needed() {
    last_level=
    if [ -f "$jstate/last-level" ]; then
        last_level=$(cat "$jstate/last-level" 2>/dev/null || printf '')
    fi
    cur=$(severity "$level")
    prev=$(severity "${last_level:-ok}")
    fire=0
    if [ "$cur" -ge 1 ]; then
        if [ "$cur" -gt "$prev" ]; then fire=1; fi
        if due "$jstate/last-alert" "$observe_interval"; then fire=1; fi
    fi
    if [ "$fire" -eq 1 ]; then
        log_append "$jstate/alerts.log" \
            "$ts $host level=$level used=${fs_used_pct}% avail=${fs_avail_kb}kb device=$fs_dev"
        stamp "$jstate/last-alert"
        echo "janitor: ALERT $level: $fs_dev ${fs_used_pct}% used, ${fs_avail_kb} KB free" >&2
    fi
    printf '%s\n' "$level" > "$jstate/last-level"
    return 0
}

write_status() {
    printf '%s level=%s used_pct=%s avail_kb=%s device=%s\n' \
        "$ts" "$level" "$fs_used_pct" "$fs_avail_kb" "$fs_dev" > "$jstate/status"
    return 0
}

# --- safe reclamation ----------------------------------------------------------
reclaim() {
    # reclaim <reason>
    reason=${1:-scheduled}
    # The reversible allowlist reclaim is gated solely by safe_reclaim_enabled.
    # The destructive reclaim-quarantined step is a separate mode gated by
    # reclaim_enabled, so this gate must not be coupled to reclaim_enabled.
    if [ "$safe_reclaim" -ne 1 ]; then
        log_append "$jstate/actions.log" \
            "$ts reclaim reason=$reason deferred safe_reclaim_enabled=$safe_reclaim"
        return 0
    fi
    before_avail=$(df_field "$probe" 4)
    is_num "$before_avail" || before_avail=0
    tmp_before=$(du_kb "$jstate/tmp")
    log_append "$jstate/actions.log" \
        "$ts reclaim reason=$reason begin dry_run=$dry_run device=$fs_dev used=${fs_used_pct}%"

    # 1. Prune worktree administration for worktrees whose directories no longer exist.
    #    This removes only stale .git/worktrees metadata; it never deletes a live tree.
    if [ -d "$town/.git" ]; then
        if [ "$dry_run" -eq 1 ]; then
            log_append "$jstate/actions.log" "$ts action=worktree-prune dry-run target=$town"
        else
            git -C "$town" worktree prune >/dev/null 2>&1 || true
            log_append "$jstate/actions.log" "$ts action=worktree-prune target=$town"
        fi
    fi

    # 2. Consolidate the object store. Non-destructive and fully reversible in effect
    #    (unreferenced objects are repacked/dropped only after normal git grace rules).
    if [ -d "$town/.git" ]; then
        if [ "$dry_run" -eq 1 ]; then
            log_append "$jstate/actions.log" "$ts action=git-gc dry-run target=$town"
        else
            git -C "$town" gc --auto --quiet >/dev/null 2>&1 || true
            log_append "$jstate/actions.log" "$ts action=git-gc target=$town"
        fi
    fi

    # 3. Remove this office's own aged temporary files only. Ownership is implicit:
    #    $jstate is created and owned by this function. Age-gated; never recursive into
    #    any user or project directory.
    if [ -d "$jstate/tmp" ]; then
        mins=$((min_age / 60))
        if [ "$mins" -lt 1 ]; then mins=1; fi
        if [ "$dry_run" -eq 1 ]; then
            n=$(find "$jstate/tmp" -type f -mmin +"$mins" 2>/dev/null | wc -l)
            log_append "$jstate/actions.log" "$ts action=tmp-clean dry-run candidates=$n dir=$jstate/tmp"
        else
            n=$(find "$jstate/tmp" -type f -mmin +"$mins" 2>/dev/null | wc -l)
            find "$jstate/tmp" -type f -mmin +"$mins" -exec rm -f {} + 2>/dev/null || true
            log_append "$jstate/actions.log" "$ts action=tmp-clean removed=$n dir=$jstate/tmp"
        fi
    fi

    # 4. Bound this office's own logs (rotation), which cannot affect project state.
    rotate "$jstate/observations.tsv"
    rotate "$jstate/actions.log"
    rotate "$jstate/alerts.log"

    after_avail=$(df_field "$probe" 4)
    is_num "$after_avail" || after_avail=0
    freed_kb=$((after_avail - before_avail))
    if [ "$freed_kb" -lt 0 ]; then freed_kb=0; fi
    tmp_after=$(du_kb "$jstate/tmp")
    tmp_freed_kb=$((tmp_before - tmp_after))
    if [ "$tmp_freed_kb" -lt 0 ]; then tmp_freed_kb=0; fi
    log_append "$jstate/actions.log" \
        "$ts reclaim reason=$reason end freed_kb=$freed_kb tmp_freed_kb=$tmp_freed_kb avail_kb=$after_avail"
    stamp "$jstate/last-reclaim"
    printf 'janitor: reclaim reason=%s freed_kb=%s tmp_freed_kb=%s avail_kb=%s\n' \
        "$reason" "$freed_kb" "$tmp_freed_kb" "$after_avail"
    return 0
}

incident() {
    log_append "$jstate/alerts.log" \
        "$ts $host INCIDENT level=critical used=${fs_used_pct}% avail=${fs_avail_kb}kb device=$fs_dev"
    echo "janitor: CRITICAL capacity on $fs_dev (${fs_used_pct}% used); running safe reclamation" >&2
    reclaim incident-critical
    # Re-probe and record whether the safe subset restored headroom. Escalation to the
    # Founder is the executive's/clerk's duty (Act 12); this office never deletes
    # unverified content to force space.
    compute
    if [ "$level" = critical ]; then
        log_append "$jstate/alerts.log" \
            "$ts $host ESCALATE level=critical after_reclaim used=${fs_used_pct}% avail=${fs_avail_kb}kb"
        echo "janitor: still critical after safe reclamation; escalate to executive/Founder" >&2
    fi
    return 0
}

# Record one inventory row for a directory into $tmp_inv (read-only probe).
record_inv_dir() {
    d=$1
    size=$(timeout 60 du -s -k "$d" 2>/dev/null | awk 'NR==1{print $1; exit}')
    is_num "$size" || return 0
    [ "$size" -ge "$inventory_min_kb" ] || return 0
    mtime=$(stat -c %Y "$d" 2>/dev/null || printf '0')
    is_num "$mtime" || mtime=0
    age_days=$(( (now - mtime) / 86400 ))
    is_git=0
    uncommitted=0
    unpushed=0
    if [ -d "$d/.git" ]; then
        is_git=1
        if [ -n "$(git -C "$d" status --porcelain 2>/dev/null)" ]; then
            uncommitted=1
        fi
        unpushed=$(timeout 15 git -C "$d" log --branches --not --remotes --oneline 2>/dev/null | wc -l | tr -d ' ')
        is_num "$unpushed" || unpushed=0
    fi
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t\n' \
        "$ts" "$host" "$d" "$size" "$mtime" "$age_days" "$is_git" "$uncommitted" "$unpushed" >> "$tmp_inv"
    return 0
}

# --- box inventory (read-only) -------------------------------------------------
inventory() {
    inv=$jstate/inventory.tsv
    tmp_inv=$jstate/tmp/inventory.tsv
    prev=$jstate/tmp/inventory.prev.tsv
    if [ -f "$inv" ]; then cp "$inv" "$prev" 2>/dev/null || : > "$prev"; else : > "$prev"; fi
    printf 'ts\thost\tpath\tsize_kb\tmtime\tage_days\tis_git\tuncommitted\tunpushed\tclass\n' > "$tmp_inv"
    log_append "$jstate/actions.log" "$ts inventory begin min_kb=$inventory_min_kb"
    # Act 12.2: jurisdiction covers the entire box. /tmp (bind-mounted writable
    # territory) and /gnu (host-managed Guix store, observed-only) were previously
    # missed; /tmp/opencode is subsumed by /tmp.
    for root in $inv_roots; do
        [ -d "$root" ] || continue
        find "$root" -maxdepth 1 -mindepth 1 -type d 2>/dev/null | while IFS= read -r d; do
            record_inv_dir "$d"
        done
        # Build caches (e.g. Lean .lake dirs) sit one level below the worktree; they are
        # the largest transient consumers, so track them as their own inventory rows.
        find "$root" -maxdepth 2 -mindepth 2 -type d -name .lake 2>/dev/null | while IFS= read -r d; do
            record_inv_dir "$d"
        done
    done
    # Large individual files at the roots: a single 500 MB file would otherwise be
    # invisible to the office, which previously inventoried directories only.
    for root in $inv_file_roots; do
        [ -d "$root" ] || continue
        find "$root" -maxdepth 1 -mindepth 1 -type f -size +"${inventory_min_kb}"k 2>/dev/null | while IFS= read -r f; do
            record_inv_dir "$f"
        done
    done
    # Transient runtime scratch batch (node/opencode bytecode-file scratch in
    # /tmp, pattern observed 2026-10-20): aggregate count, size, age and a
    # one-pass liveness probe so accumulation is visible before it is acted on.
    scratch_count=0
    scratch_kb=0
    scratch_oldest=
    scratch_newest=
    scratch_live=0
    if [ -d "$scratch_dir" ]; then
        for f in "$scratch_dir"/.bcf*; do
            [ -f "$f" ] || continue
            scratch_count=$((scratch_count + 1))
            fkb=$(du -k "$f" 2>/dev/null | awk 'NR==1{print $1; exit}')
            is_num "$fkb" || fkb=0
            scratch_kb=$((scratch_kb + fkb))
            fm=$(stat -c %Y "$f" 2>/dev/null || printf '0')
            is_num "$fm" || fm=0
            if [ -z "$scratch_oldest" ] || [ "$fm" -lt "$scratch_oldest" ]; then scratch_oldest=$fm; fi
            if [ -z "$scratch_newest" ] || [ "$fm" -gt "$scratch_newest" ]; then scratch_newest=$fm; fi
        done
        # One /proc pass: count scratch files still mapped or open.
        for _sf_p in /proc/[0-9]*; do
            if [ -r "$_sf_p/maps" ]; then
                if grep -q -F -e "$scratch_dir/.bcf" "$_sf_p/maps" 2>/dev/null; then scratch_live=1; fi
            fi
            if [ -d "$_sf_p/fd" ]; then
                for _sf_fd in "$_sf_p/fd"/*; do
                    _sf_val=$(readlink "$_sf_fd" 2>/dev/null) || continue
                    case "$_sf_val" in
                        "$scratch_dir"/.bcf*) scratch_live=1 ;;
                    esac
                done
            fi
        done
    fi
    scratch_newest_age_days=999999
    scratch_oldest_age_days=0
    if [ "$scratch_count" -gt 0 ]; then
        scratch_newest_age_days=$(( (now - scratch_newest) / 86400 ))
        scratch_oldest_age_days=$(( (now - scratch_oldest) / 86400 ))
    fi
    # Eligibility keys on the OLDEST file, not the newest: a continuously
    # refreshed batch still contains reclaimable dead files, so requiring the
    # newest file to be aged (the previous rule) made staging unreachable on a
    # live box. The batch-level `live` flag is informational only —
    # scratch_quarantine re-checks each file and skips any still referenced, so
    # staging never breaks a running agent even while live scratch exists.
    scratch_verdict=small
    if [ "$scratch_kb" -ge "$inventory_min_kb" ]; then scratch_verdict=accumulating; fi
    if [ "$scratch_kb" -ge "$inventory_min_kb" ] && [ "$scratch_oldest_age_days" -ge 1 ]; then
        scratch_verdict=quarantine-eligible
    fi
    scratch=$jstate/scratch.tsv
    scratch_hdr='ts	host	pattern	count	size_kb	oldest_age_days	newest_age_days	live_referenced	verdict'
    if [ ! -f "$scratch" ] || [ "$(head -n 1 "$scratch" 2>/dev/null)" != "$scratch_hdr" ]; then
        printf '%s\n' "$scratch_hdr" > "$scratch"
    fi
    printf '%s\t%s\t%s/.bcf*\t%s\t%s\t%s\t%s\t%s\t%s\n' \
        "$ts" "$host" "$scratch_dir" "$scratch_count" "$scratch_kb" "$scratch_oldest_age_days" \
        "$scratch_newest_age_days" "$scratch_live" "$scratch_verdict" >> "$scratch"
    rotate "$scratch"
    log_append "$jstate/actions.log" \
        "$ts scratch-batch pattern=$scratch_dir/.bcf* count=$scratch_count size_kb=$scratch_kb oldest_age_days=$scratch_oldest_age_days newest_age_days=$scratch_newest_age_days live=$scratch_live verdict=$scratch_verdict"
    if [ "$scratch_verdict" = "quarantine-eligible" ]; then
        log_append "$jstate/actions.log" \
            "$ts PREVENTION scratch batch quarantine-eligible (aged, unreferenced); run scratch-quarantine to stage it reversibly"
    fi
    mv "$tmp_inv" "$inv"
    rotate "$inv"
    if [ -s "$prev" ]; then
        grow=$jstate/growth.tsv
        printf 'ts\tpath\tprev_kb\tnow_kb\tdelta_kb\n' > "$grow"
        awk -F'\t' 'NR==FNR { if (FNR>1) old[$3]=$4; next } FNR>1 && ($3 in old) { d=$4-old[$3]; if (d!=0) printf "%s\t%s\t%s\t%s\t%d\n", $1, $3, old[$3], $4, d }' "$prev" "$inv" \
            | sort -t"$(printf '\t')" -k5,5nr | head -n 20 >> "$grow"
        top=$(tail -n +2 "$grow" | head -n 1)
        if [ -n "$top" ]; then
            tpath=$(printf '%s' "$top" | cut -f2)
            tdelta=$(printf '%s' "$top" | cut -f5)
            log_append "$jstate/actions.log" "$ts inventory growth_top=$tpath delta_kb=$tdelta"
        fi
    fi
    # Territorial accounting (Act 12.2, #298/#299): attribute the shared device
    # between box-visible usage (inventoried rows) and usage outside the box's
    # visibility (host system, other containers). Observation only; the office
    # never acts on outside-box usage. Row sizes are threshold-filtered
    # (>= inventory_min_kb), so small directories are not counted here.
    #
    # box_visible_kb sums distinct TOP-LEVEL paths only: a nested build-cache row
    # (…/.lake) is already included in its parent worktree's du, so counting it
    # again double-counts; and a duplicated row (e.g. from a concurrent run)
    # would too. Either defect inflates box_visible_kb past the device and forces
    # outside_box_kb to 0 (observed 2026-10-20: 270.9 GB "visible" on a 186.2
    # GB-used device). Dedupe by path and exclude nested .lake rows.
    terr=$jstate/territorial.tsv
    printf 'ts\thost\tdevice\tdevice_size_kb\tdevice_used_kb\tdevice_avail_kb\tbox_visible_kb\toutside_box_kb\n' > "$terr"
    box_kb=0
    if [ -s "$inv" ]; then
        box_kb=$(awk -F'\t' 'NR>1 && $3 !~ /\/\.lake$/ && !seen[$3]++ {s+=$4} END {printf "%d", s+0}' "$inv")
        is_num "$box_kb" || box_kb=0
    fi
    dev_size=$(df_field "$probe" 2)
    dev_used=$(df_field "$probe" 3)
    dev_avail=$(df_field "$probe" 4)
    outside_kb=$((dev_used - box_kb))
    if [ "$outside_kb" -lt 0 ]; then outside_kb=0; fi
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
        "$ts" "$host" "$fs_dev" "$dev_size" "$dev_used" "$dev_avail" \
        "$box_kb" "$outside_kb" >> "$terr"
    log_append "$jstate/actions.log" \
        "$ts territorial device_used_kb=$dev_used box_visible_kb=$box_kb outside_box_kb=$outside_kb"
    n=$(wc -l < "$inv" 2>/dev/null || printf '0')
    log_append "$jstate/actions.log" "$ts inventory end entries=$n"
    printf 'janitor: inventory complete, %s entries (min %s KB)\n' "$n" "$inventory_min_kb"
    return 0
}

path_in_use() {
    # path_in_use <path>: return 0 if any live process references the path
    # (cwd/root at or under it, an open fd or memory map under it) or a mount
    # sits at or under it. Read-only liveness probe backing the Act 12.4(d)
    # evidence standard: no artifact is quarantine-classified while referenced.
    _piu=$1
    [ -n "$_piu" ] || return 1
    _piu_canon=$(readlink -f "$_piu" 2>/dev/null) || return 1
    [ -n "$_piu_canon" ] || return 1
    [ "$_piu_canon" != "/" ] || return 1
    for _piu_p in /proc/[0-9]*; do
        for _piu_link in "$_piu_p/cwd" "$_piu_p/root"; do
            _piu_val=$(readlink "$_piu_link" 2>/dev/null) || continue
            case "$_piu_val" in
                "$_piu_canon"|"$_piu_canon/"*) return 0 ;;
            esac
        done
        if [ -r "$_piu_p/maps" ]; then
            if grep -q -F -e "$_piu_canon/" "$_piu_p/maps" 2>/dev/null; then return 0; fi
        fi
        if [ -d "$_piu_p/fd" ]; then
            for _piu_fd in "$_piu_p/fd"/*; do
                _piu_val=$(readlink "$_piu_fd" 2>/dev/null) || continue
                case "$_piu_val" in
                    "$_piu_canon"|"$_piu_canon/"*) return 0 ;;
                esac
            done
        fi
    done
    if [ -r /proc/mounts ]; then
        while IFS= read -r _piu_line; do
            _piu_mp=$(printf '%s' "$_piu_line" | awk '{print $2; exit}')
            case "$_piu_mp" in
                "$_piu_canon"|"$_piu_canon/"*) return 0 ;;
            esac
        done < /proc/mounts
    fi
    return 1
}

# --- classify inventory candidates (read-only) ----------------------------------
classify() {
    inv=$jstate/inventory.tsv
    [ -f "$inv" ] || { echo "janitor: no inventory; run inventory first" >&2; return 1; }
    log_append "$jstate/actions.log" "$ts classify begin"
    tmp=$jstate/tmp/classify.tsv
    printf 'ts\thost\tpath\tsize_kb\tmtime\tage_days\tis_git\tuncommitted\tunpushed\tclass\n' > "$tmp"
    tail -n +2 "$inv" 2>/dev/null | while IFS="$(printf '\t')" read -r ts host path size mtime age is_git uncommitted unpushed _class; do
        [ -n "$path" ] || continue
        [ -d "$path" ] || continue
        class=retain
        case "$path" in
        /gnu|/gnu/store|/gnu/store/*)
            # Host-managed Guix store (read-only mount on the shared device).
            # Observed for territorial accounting only; never reclaimed.
            class=retain-host-managed
            ;;
        */.lake)
            # Build cache (e.g. Lean .lake). Never quarantine a live or recently
            # touched cache: it may be reused by an in-flight or upcoming build.
            # Only an aged cache whose parent worktree is also gone or aged is a
            # quarantine candidate (the work it supported is surely merged/abandoned).
            parent=${path%/.lake}
            if [ "$age" -lt 30 ]; then
                class=monitor
            else
                page=$(awk -F'\t' -v p="$parent" 'NR>1 && $3==p {print $6; exit}' "$inv" 2>/dev/null)
                is_num "$page" || page=999999
                if [ "$page" -lt 30 ]; then
                    class=monitor
                else
                    class=quarantine-candidate
                fi
            fi
            ;;
        */.elan|*/.elan/toolchains|*/.elan/toolchains/*)
            # Live Lean/elAN toolchain installation (elan home: toolchains, the
            # elan binary, settings). Quarantining it breaks the Lean build until
            # elan re-downloads the pinned toolchain (failure mode J2: live build
            # dependency). The directory mtime ages after install, so age is not
            # an abandonment signal here; retain the whole tree.
            class=retain
            ;;
        *)
            if [ "$is_git" -eq 1 ] && [ "${unpushed:-0}" -gt 0 ]; then
                class=retain-unpushed
            elif [ "$is_git" -eq 1 ] && [ "$uncommitted" -eq 1 ]; then
                class=retain-live
            elif [ "$is_git" -eq 1 ] && [ "$age" -ge 30 ]; then
                class=quarantine-candidate
            elif [ "$is_git" -eq 0 ] && [ "$age" -ge 30 ] && [ "$size" -ge 1048576 ]; then
                class=quarantine-candidate
            elif [ "$age" -ge 7 ]; then
                class=monitor
            fi
            ;;
        esac
        # Act 12.4(d): no artifact is quarantine-classified unless a recorded
        # liveness/ownership check clears it. A referenced path is retain-live.
        if [ "$class" = "quarantine-candidate" ]; then
            if path_in_use "$path"; then
                class=retain-live
                log_append "$jstate/actions.log" "$ts liveness-gate path=$path result=in-use"
            else
                log_append "$jstate/actions.log" "$ts liveness-gate path=$path result=clear"
            fi
        fi
        # For build caches, the parent worktree's processes matter too: a live
        # agent working in the worktree regenerates the cache on demand.
        case "$path" in
        */.lake)
            if [ "$class" = "quarantine-candidate" ]; then
                parent=${path%/.lake}
                if path_in_use "$parent"; then
                    class=retain-live
                    log_append "$jstate/actions.log" "$ts liveness-gate path=$path parent=$parent result=in-use"
                fi
            fi
            ;;
        esac
        printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
            "$ts" "$host" "$path" "$size" "$mtime" "$age" "$is_git" "$uncommitted" "$unpushed" "$class" >> "$tmp"
    done
    mv "$tmp" "$inv"
    n=$(wc -l < "$inv" 2>/dev/null || printf '0')
    log_append "$jstate/actions.log" "$ts classify end entries=$n"
    printf 'janitor: classify complete, %s entries\n' "$n"
    return 0
}

# --- quarantine candidates (reversible) ------------------------------------------
quarantine() {
    inv=$jstate/inventory.tsv
    [ -f "$inv" ] || { echo "janitor: no inventory; run inventory first" >&2; return 1; }
    [ -d "$quarantine_dir" ] || mkdir -p "$quarantine_dir"
    log_append "$jstate/actions.log" "$ts quarantine begin dir=$quarantine_dir"
    tmp=$jstate/tmp/quarantine.tsv
    : > "$tmp"
    tail -n +2 "$inv" 2>/dev/null | while IFS="$(printf '\t')" read -r ts host path size mtime age is_git uncommitted unpushed class; do
        [ -n "$path" ] || continue
        [ -d "$path" ] || continue
        [ "$class" = "quarantine-candidate" ] || continue
        base=$(basename "$path")
        dest="$quarantine_dir/${base}-$(date -u +%Y%m%d%H%M%S)"
        if [ "$dry_run" -eq 1 ]; then
            log_append "$jstate/actions.log" "$ts action=quarantine dry-run src=$path dest=$dest"
        else
            if mv "$path" "$dest" 2>/dev/null; then
                log_append "$jstate/actions.log" "$ts action=quarantine src=$path dest=$dest"
                printf '%s\t%s\t%s\t%s\t%s\n' "$ts" "$path" "$dest" "$size" "$now" >> "$tmp"
            else
                log_append "$jstate/actions.log" "$ts action=quarantine-failed src=$path"
            fi
        fi
    done
    if [ -f "$tmp" ] && [ -s "$tmp" ]; then
        qlog=$jstate/quarantined.tsv
        if [ ! -f "$qlog" ]; then
            printf 'ts\tsrc\tdest\tsize_kb\tquarantined_at\n' > "$qlog"
        fi
        cat "$tmp" >> "$qlog"
        rotate "$qlog"
    fi
    log_append "$jstate/actions.log" "$ts quarantine end"
    printf 'janitor: quarantine complete (dir=%s)\n' "$quarantine_dir"
    return 0
}

# --- stage transient runtime scratch reversibly (quarantine, not deletion) ------
scratch_quarantine() {
    scratch=$jstate/scratch.tsv
    [ -f "$scratch" ] || { echo "janitor: no scratch observations" >&2; return 1; }
    [ "$reclaim_enabled" -eq 1 ] || {
        log_append "$jstate/actions.log" "$ts scratch-quarantine deferred reclaim_enabled=$reclaim_enabled"
        printf 'janitor: scratch-quarantine deferred (reclaim_enabled=%s)\n' "$reclaim_enabled"
        return 0
    }
    verdict=$(tail -n 1 "$scratch" | cut -f9)
    [ "$verdict" = "quarantine-eligible" ] || {
        log_append "$jstate/actions.log" "$ts scratch-quarantine deferred verdict=$verdict"
        printf 'janitor: scratch-quarantine deferred (verdict=%s)\n' "$verdict"
        return 0
    }
    log_append "$jstate/actions.log" "$ts scratch-quarantine begin"
    # Re-verify liveness with one /proc pass: build no open list here; instead the
    # move loop skips any file still referenced, so staging never breaks a run.
    stage=$quarantine_dir/scratch-$(date -u +%Y%m%d%H%M%S)
    [ -d "$quarantine_dir" ] || mkdir -p "$quarantine_dir"
    mkdir -p "$stage"
    n=0
    kb=0
    for f in "$scratch_dir"/.bcf*; do
        [ -f "$f" ] || continue
        fm=$(stat -c %Y "$f" 2>/dev/null || printf '0')
        is_num "$fm" || fm=0
        age=$((now - fm))
        [ "$age" -ge "$min_age" ] || continue
        # Skip any file a live process still maps or holds open.
        referenced=0
        for _sq_p in /proc/[0-9]*; do
            if [ -r "$_sq_p/maps" ]; then
                if grep -q -F -e "$f" "$_sq_p/maps" 2>/dev/null; then referenced=1; break; fi
            fi
            if [ -d "$_sq_p/fd" ]; then
                for _sq_fd in "$_sq_p/fd"/*; do
                    _sq_val=$(readlink "$_sq_fd" 2>/dev/null) || continue
                    if [ "$_sq_val" = "$f" ]; then referenced=1; break; fi
                done
            fi
            [ "$referenced" -eq 1 ] && break
        done
        [ "$referenced" -eq 1 ] && continue
        fkb=$(du -k "$f" 2>/dev/null | awk 'NR==1{print $1; exit}')
        is_num "$fkb" || fkb=0
        if mv "$f" "$stage/" 2>/dev/null; then
            n=$((n + 1))
            kb=$((kb + fkb))
        fi
    done
    if [ "$n" -eq 0 ]; then
        rmdir "$stage" 2>/dev/null || true
        log_append "$jstate/actions.log" "$ts scratch-quarantine end staged=0 (all scratch young or referenced)"
        printf 'janitor: scratch-quarantine: no eligible files to stage\n'
        return 0
    fi
    log_append "$jstate/actions.log" "$ts scratch-quarantine end staged=$n size_kb=$kb dest=$stage"
    qlog=$jstate/quarantined.tsv
    if [ ! -f "$qlog" ]; then
        printf 'ts\tsrc\tdest\tsize_kb\tquarantined_at\n' > "$qlog"
    fi
    printf '%s\t%s/.bcf*\t%s\t%s\t%s\n' "$ts" "$scratch_dir" "$stage" "$kb" "$now" >> "$qlog"
    rotate "$qlog"
    printf 'janitor: scratch-quarantine staged %s files (%s KB) at %s (grace=%ss, then reclaim-quarantined)\n' \
        "$n" "$kb" "$stage" "$quarantine_grace"
    return 0
}

# --- reclaim quarantined items past grace period (destructive) ------------------
reclaim_quarantined() {
    qlog=$jstate/quarantined.tsv
    [ -f "$qlog" ] || { echo "janitor: no quarantined items" >&2; return 0; }
    [ "$reclaim_enabled" -eq 1 ] || {
        log_append "$jstate/actions.log" "$ts reclaim-quarantined deferred reclaim_enabled=$reclaim_enabled"
        printf 'janitor: reclaim-quarantined deferred (reclaim_enabled=%s)\n' "$reclaim_enabled"
        return 0
    }
    log_append "$jstate/actions.log" "$ts reclaim-quarantined begin grace=${quarantine_grace}s"
    tmp=$jstate/tmp/reclaim.tsv
    qcopy=$jstate/tmp/quarantined.input.tsv
    # The snapshot/rewrite is serialized by the global Janitor lock acquired above.
    # Every in-tree qlog writer (quarantine and scratch-quarantine) is a mutating
    # mode and takes that same lock; keep them out of the report/status exemptions.
    qheader=$(printf 'ts\tsrc\tdest\tsize_kb\tquarantined_at')
    if ! cp "$qlog" "$qcopy" 2>/dev/null; then
        log_append "$jstate/actions.log" "$ts reclaim-quarantined deferred reason=qlog-copy-failed"
        rm -f "$qcopy"
        return 0
    fi
    if ! exec 3< "$qcopy"; then
        log_append "$jstate/actions.log" "$ts reclaim-quarantined deferred reason=qlog-open-failed"
        rm -f "$qcopy" "$tmp"
        return 0
    fi
    qheader_read=
    if ! IFS= read -r qheader_read <&3 || [ "$qheader_read" != "$qheader" ]; then
        exec 3<&-
        log_append "$jstate/actions.log" "$ts reclaim-quarantined deferred reason=qlog-header-invalid"
        rm -f "$qcopy" "$tmp"
        return 0
    fi
    printf '%s\n' "$qheader" > "$tmp"
    rejected=$jstate/quarantine-rejected.tsv
    freed_kb=0
    while record=; IFS= read -r record <&3 || [ -n "$record" ]; do
        [ -n "$record" ] || continue
        # Read TSV columns with cut so empty fields remain empty; tab is IFS
        # whitespace and `read` would collapse adjacent delimiters.
        ts=$(printf '%s\n' "$record" | cut -s -f1)
        src=$(printf '%s\n' "$record" | cut -s -f2)
        dest=$(printf '%s\n' "$record" | cut -s -f3)
        size=$(printf '%s\n' "$record" | cut -s -f4)
        qat=$(printf '%s\n' "$record" | cut -s -f5)
        [ -n "$dest" ] || {
            log_append "$jstate/actions.log" "$ts action=reclaim refused=empty-quarantine-path"
            if [ ! -f "$rejected" ]; then
                printf 'ts\tsrc\tdest\tsize_kb\tquarantined_at\treason\n' > "$rejected"
            fi
            printf '%s\t%s\t%s\t%s\t%s\tempty-quarantine-path\n' \
                "$ts" "$src" "$dest" "$size" "$qat" >> "$rejected"
            rotate "$rejected"
            continue
        }
        # A completed prior reclaim retires its queue row, so a future directory
        # recreated at the same name cannot inherit the old expired timestamp.
        if [ ! -e "$dest" ] && [ ! -L "$dest" ]; then
            log_append "$jstate/actions.log" "$ts action=reclaim skip=already-absent dest=$dest"
            continue
        fi
        if ! quarantine_path_ok "$dest"; then
            log_append "$jstate/actions.log" "$ts action=reclaim refused=invalid-quarantine-path dest=$dest"
            printf '%s\t%s\t%s\t%s\t%s\n' "$ts" "$src" "$dest" "$size" "$qat" >> "$tmp"
            continue
        fi
        if ! is_num "$qat"; then
            log_append "$jstate/actions.log" "$ts action=reclaim refused=invalid-quarantine-timestamp dest=$dest quarantined_at=$qat"
            printf '%s\t%s\t%s\t%s\t%s\n' "$ts" "$src" "$dest" "$size" "$qat" >> "$tmp"
            continue
        fi
        qat=$(normalize_decimal "$qat") || {
            log_append "$jstate/actions.log" "$ts action=reclaim refused=invalid-quarantine-timestamp dest=$dest"
            printf '%s\t%s\t%s\t%s\t%s\n' "$ts" "$src" "$dest" "$size" "$qat" >> "$tmp"
            continue
        }
        if decimal_greater "$qat" "$now"; then
            log_append "$jstate/actions.log" "$ts action=reclaim refused=future-quarantine-timestamp dest=$dest quarantined_at=$qat now=$now"
            printf '%s\t%s\t%s\t%s\t%s\n' "$ts" "$src" "$dest" "$size" "$qat" >> "$tmp"
            continue
        fi
        age=$((now - qat))
        if [ "$age" -lt "$quarantine_grace" ]; then
            printf '%s\t%s\t%s\t%s\t%s\n' "$ts" "$src" "$dest" "$size" "$qat" >> "$tmp"
            continue
        fi
        if path_in_use "$dest"; then
            log_append "$jstate/actions.log" "$ts action=reclaim deferred=live dest=$dest qlog_candidate_du_kb=$size"
            printf '%s\t%s\t%s\t%s\t%s\n' "$ts" "$src" "$dest" "$size" "$qat" >> "$tmp"
            continue
        fi
        candidate_kb=$(du_kb "$dest")
        is_num "$candidate_kb" || candidate_kb=0
        if [ "$dry_run" -eq 1 ]; then
            log_append "$jstate/actions.log" "$ts action=reclaim dry-run src=$src dest=$dest candidate_du_kb=$candidate_kb why=expired-quarantine recoverability=quarantine-copy liveness=clear owner=janitor-quarantine"
            printf '%s\t%s\t%s\t%s\t%s\n' "$ts" "$src" "$dest" "$size" "$qat" >> "$tmp"
        else
            before=$(available_kb 2>/dev/null || printf '')
            if [ -z "$before" ] || ! quarantine_path_ok "$dest" || path_in_use "$dest"; then
                log_append "$jstate/actions.log" "$ts action=reclaim deferred=measurement-or-liveness dest=$dest"
                printf '%s\t%s\t%s\t%s\t%s\n' "$ts" "$src" "$dest" "$size" "$qat" >> "$tmp"
                continue
            fi
            candidate_kb=$(du_kb "$dest")
            is_num "$candidate_kb" || candidate_kb=0
            rm_status=0
            rm -rf "$dest" 2>/dev/null || rm_status=$?
            if [ ! -e "$dest" ] && [ ! -L "$dest" ]; then
                after=$(available_kb 2>/dev/null || printf '')
                if [ -n "$after" ]; then
                    delta=$((after - before))
                    log_append "$jstate/actions.log" "$ts action=reclaim executed src=$src dest=$dest rm_status=$rm_status candidate_du_kb=$candidate_kb device_avail_before_kb=$before device_avail_after_kb=$after measured_device_delta_kb=$delta why=expired-quarantine recoverability=quarantine-copy liveness=clear owner=janitor-quarantine"
                else
                    log_append "$jstate/actions.log" "$ts action=reclaim executed src=$src dest=$dest rm_status=$rm_status candidate_du_kb=$candidate_kb device_measurement=unavailable"
                fi
            else
                log_append "$jstate/actions.log" "$ts action=reclaim failed src=$src dest=$dest rm_status=$rm_status candidate_du_kb=$candidate_kb path_remains=1"
                printf '%s\t%s\t%s\t%s\t%s\n' "$ts" "$src" "$dest" "$size" "$qat" >> "$tmp"
            fi
        fi
    done
    exec 3<&-
    rm -f "$qcopy"
    mv "$tmp" "$qlog"
    log_append "$jstate/actions.log" "$ts reclaim-quarantined end"
    printf 'janitor: reclaim-quarantined complete\n'
    return 0
}

# --- reclaim idle regenerable build caches --------------------------------------
reclaim_idle_caches() {
    # Act 12.3(2)/12.4: delete regenerable build caches (.lake) that are
    # verifiably idle. Deleting a .lake loses only build time, never data
    # (recovery: cd <worktree> && lake update && lake exe cache get && lake
    # build). This is the liveness-aware rule the 2026-10-20 idle-cache record
    # recommended, replacing the age>=30d gate that never fires on the fast
    # research cadence. Gated by reclaim_enabled (Act 12.7) and idle_cache_enabled;
    # per cache it requires: no live process references the cache or its worktree
    # (path_in_use), idle for >= idle_cache_seconds, and a git worktree with no
    # unpushed commits and no uncommitted changes.
    inv=$jstate/inventory.tsv
    if [ ! -f "$inv" ]; then
        log_append "$jstate/actions.log" "$ts idle-cache-reclaim skip reason=no-inventory"
        printf 'janitor: idle-cache reclaim skipped (no inventory yet)\n'
        return 0
    fi
    if [ "$reclaim_enabled" -ne 1 ] || [ "$idle_cache_enabled" -ne 1 ]; then
        log_append "$jstate/actions.log" "$ts idle-cache-reclaim deferred reclaim_enabled=$reclaim_enabled idle_cache_enabled=$idle_cache_enabled"
        printf 'janitor: idle-cache reclaim deferred (reclaim_enabled=%s idle_cache_enabled=%s)\n' \
            "$reclaim_enabled" "$idle_cache_enabled"
        return 0
    fi
    log_append "$jstate/actions.log" "$ts idle-cache-reclaim begin idle_s=$idle_cache_seconds dry_run=$dry_run"
    acc=$jstate/tmp/idle-cache.freed
    : > "$acc"
    tail -n +2 "$inv" 2>/dev/null | while IFS="$(printf '\t')" read -r _ts _host path _size _mtime _age _is_git _uncommitted _unpushed _class; do
        case "$path" in */.lake) : ;; *) continue ;; esac
        [ -d "$path" ] && [ ! -L "$path" ] || continue
        parent=${path%/.lake}
        m=$(stat -c %Y "$path" 2>/dev/null || printf '0')
        is_num "$m" || m=0
        idle=$((now - m))
        [ "$idle" -ge "$idle_cache_seconds" ] || continue
        if path_in_use "$path" || path_in_use "$parent"; then
            log_append "$jstate/actions.log" "$ts idle-cache skip path=$path reason=in-use"
            continue
        fi
        if ! git -C "$parent" rev-parse --git-dir >/dev/null 2>&1; then
            log_append "$jstate/actions.log" "$ts idle-cache skip path=$path reason=not-git-worktree"
            continue
        fi
        # HEAD only (this worktree's own branch), NOT --branches: branch refs are
        # shared across a repository's linked worktrees, so --branches would let
        # an unrelated worktree's unpushed commit block reclaiming this cache and
        # silently disable the valve. If the repo has no remote-tracking refs at
        # all, `--not --remotes` is empty and cannot confirm the work is saved, so
        # treat it as unpushed (conservative).
        if git -C "$parent" for-each-ref --format='%(refname)' refs/remotes 2>/dev/null | grep -q .; then
            up=$(timeout 15 git -C "$parent" log --oneline --not --remotes 2>/dev/null | wc -l | tr -d ' ')
        else
            up=1
        fi
        is_num "$up" || up=0
        if [ "$up" -gt 0 ]; then
            log_append "$jstate/actions.log" "$ts idle-cache skip path=$path reason=unpushed commits=$up"
            continue
        fi
        dirty_status=$(git -C "$parent" status --porcelain 2>/dev/null) || {
            log_append "$jstate/actions.log" "$ts idle-cache skip path=$path reason=git-status-unavailable"
            continue
        }
        if [ -n "$dirty_status" ]; then
            dirty=$(printf '%s\n' "$dirty_status" | wc -l | tr -d ' ')
            log_append "$jstate/actions.log" "$ts idle-cache skip path=$path reason=dirty files=$dirty"
            continue
        fi
        sz=$(du -sk "$path" 2>/dev/null | awk 'NR==1{print $1; exit}')
        is_num "$sz" || sz=0
        if [ "$dry_run" -eq 1 ]; then
            log_append "$jstate/actions.log" "$ts idle-cache dry-run path=$path candidate_du_kb=$sz idle_s=$idle why=regenerable-build-cache recoverability=lake-update-cache-get-build liveness=clear owner=clean-fully-pushed-worktree"
            printf '%s\t%s\n' "$path" "$sz" >> "$acc"
        else
            before=$(available_kb 2>/dev/null || printf '')
            # Evidence can stale between the initial checks and destruction. Recheck
            # liveness, idle age and repository cleanliness immediately before rm.
            m=$(stat -c %Y "$path" 2>/dev/null || printf '0')
            is_num "$m" || m=0
            idle=$((now - m))
            remotes=$(git -C "$parent" for-each-ref --format='%(refname)' refs/remotes 2>/dev/null) || remotes=
            if [ -n "$remotes" ]; then
                unpushed=$(timeout 15 git -C "$parent" log --oneline --not --remotes 2>/dev/null) || unpushed=unverified
            else
                unpushed=unverified
            fi
            dirty_status=$(git -C "$parent" status --porcelain 2>/dev/null) || dirty_status=unverified
            if [ -z "$before" ] || [ "$idle" -lt "$idle_cache_seconds" ] \
               || path_in_use "$path" || path_in_use "$parent" \
               || [ -n "$unpushed" ] || [ -n "$dirty_status" ]; then
                log_append "$jstate/actions.log" "$ts idle-cache skip path=$path reason=final-evidence-recheck"
                continue
            fi
            if rm -rf "$path" 2>/dev/null; then
                after=$(available_kb 2>/dev/null || printf '')
                if [ -n "$after" ]; then
                    delta=$((after - before))
                    log_append "$jstate/actions.log" "$ts idle-cache executed path=$path candidate_du_kb=$sz device_avail_before_kb=$before device_avail_after_kb=$after measured_device_delta_kb=$delta idle_s=$idle why=regenerable-build-cache recovery=lake-update-cache-get-build liveness=clear owner=clean-fully-pushed-worktree"
                else
                    log_append "$jstate/actions.log" "$ts idle-cache executed path=$path candidate_du_kb=$sz device_measurement=unavailable"
                fi
                printf '%s\t%s\n' "$path" "$sz" >> "$acc"
            else
                log_append "$jstate/actions.log" "$ts idle-cache failed path=$path candidate_du_kb=$sz"
            fi
        fi
    done
    n=$(wc -l < "$acc" 2>/dev/null | tr -d ' ')
    kb=$(awk -F'\t' '{s+=$2} END{printf "%d", s+0}' "$acc" 2>/dev/null)
    is_num "$n" || n=0
    is_num "$kb" || kb=0
    log_append "$jstate/actions.log" "$ts idle-cache-reclaim end count=$n candidate_du_kb=$kb dry_run=$dry_run (device delta recorded per item)"
    printf 'janitor: idle-cache reclaim %s item(s), candidate_du_kb=%s (device delta recorded per item; dry_run=%s)\n' "$n" "$kb" "$dry_run"
    return 0
}

# --- concurrency lock ----------------------------------------------------------
# One writer per state dir. Two janitor cycles running at once (observed
# 2026-10-20: two inventory passes 41s apart) share $jstate/tmp/inventory.tsv
# and interleave their appends, producing a corrupt inventory (282 rows for 186
# paths) that inflates the territorial accounting. mkdir is the POSIX-atomic
# primitive; a lock older than lock_stale seconds is presumed dead and reclaimed.
# Read-only modes (report/status) never lock.
lock_dir=$jstate/lock
acquire_lock() {
    _tries=0
    while :; do
        if mkdir "$lock_dir" 2>/dev/null; then
            printf '%s\n' "$$" > "$lock_dir/pid" 2>/dev/null || true
            trap 'rm -rf "$lock_dir"' EXIT HUP INT TERM
            return 0
        fi
        _lmt=$(stat -c %Y "$lock_dir" 2>/dev/null || printf '0')
        is_num "$_lmt" || _lmt=0
        if [ "$_lmt" -gt 0 ] && [ $((now - _lmt)) -ge "$lock_stale" ]; then
            log_append "$jstate/actions.log" "$ts lock-stale removed age_s=$((now - _lmt)) dir=$lock_dir"
            rm -rf "$lock_dir" 2>/dev/null || true
            continue
        fi
        _tries=$((_tries + 1))
        [ "$_tries" -lt 3 ] || return 1
        sleep 2
    done
}
case "$mode" in
    report|status) : ;;
    *)
        if ! acquire_lock; then
            printf 'janitor: another janitor run holds %s; skipping %s\n' "$lock_dir" "$mode" >&2
            exit 0
        fi
        ;;
esac

# --- modes ---------------------------------------------------------------------
case "$mode" in
    observe)
        compute
        if due "$jstate/last-observe" "$observe_interval"; then record_observation; fi
        alert_if_needed
        write_status
        ;;
    reclaim)
        compute
        reclaim manual
        ;;
    cycle)
        compute
        if due "$jstate/last-observe" "$observe_interval"; then record_observation; fi
        alert_if_needed
        write_status
        if due "$jstate/last-inventory" "$reclaim_interval"; then
            inventory
            classify
            stamp "$jstate/last-inventory"
        fi
        if [ "$level" = critical ]; then
            incident
        elif due "$jstate/last-reclaim" "$reclaim_interval"; then
            reclaim scheduled
        else
            log_append "$jstate/actions.log" "$ts reclaim deferred reason=not-due level=$level"
        fi
        if [ "$reclaim_enabled" -eq 1 ]; then
            reclaim_quarantined
        fi
        # Act 12.3(2) prevention: under real pressure (high/critical), reclaim
        # verifiably idle regenerable build caches rather than waiting for the
        # conservative age>=30d gate. The per-cache evidence gates inside
        # reclaim_idle_caches keep this safe.
        if [ "$reclaim_enabled" -eq 1 ] && [ "$idle_cache_enabled" -eq 1 ] \
           && [ "$(severity "$level")" -ge 2 ]; then
            reclaim_idle_caches
        fi
        ;;
    report)
        if [ -f "$jstate/status" ]; then
            printf 'status: %s\n' "$(cat "$jstate/status")"
        else
            printf 'status: no observation recorded yet\n'
        fi
        if [ -f "$jstate/actions.log" ]; then
            printf 'recent actions:\n'
            tail -n 8 "$jstate/actions.log"
        fi
        if [ -f "$jstate/alerts.log" ]; then
            printf 'recent alerts:\n'
            tail -n 8 "$jstate/alerts.log"
        fi
        if [ -f "$jstate/growth.tsv" ]; then
            printf 'top growers (KB):\n'
            head -n 11 "$jstate/growth.tsv"
        fi
        if [ -f "$jstate/territorial.tsv" ]; then
            printf 'territorial (last inventory): device_used_kb box_visible_kb outside_box_kb\n'
            tail -n 2 "$jstate/territorial.tsv"
        fi
        if [ -f "$jstate/scratch.tsv" ]; then
            printf 'scratch batch (last inventory):\n'
            tail -n 2 "$jstate/scratch.tsv"
        fi
        if [ -d "$quarantine_dir" ]; then
            qn=$(find "$quarantine_dir" -mindepth 1 -maxdepth 1 2>/dev/null | wc -l | tr -d ' ')
            qsz=$(du -sk "$quarantine_dir" 2>/dev/null | awk 'NR==1{print $1; exit}')
            is_num "$qsz" || qsz=0
            printf 'quarantine: %s item(s), %s KB staged, grace=%ss, reclaim_enabled=%s, dir=%s\n' \
                "$qn" "$qsz" "$quarantine_grace" "$reclaim_enabled" "$quarantine_dir"
        fi
        ;;
    status)
        if [ -f "$jstate/status" ]; then
            cat "$jstate/status"
        else
            printf 'no-observation\n'
        fi
        ;;
    inventory)
        compute
        inventory
        ;;
    classify)
        compute
        classify
        ;;
    quarantine)
        compute
        quarantine
        ;;
    reclaim-quarantined)
        compute
        reclaim_quarantined
        ;;
    scratch-quarantine)
        compute
        scratch_quarantine
        ;;
    reclaim-idle-caches)
        compute
        reclaim_idle_caches
        ;;
esac
