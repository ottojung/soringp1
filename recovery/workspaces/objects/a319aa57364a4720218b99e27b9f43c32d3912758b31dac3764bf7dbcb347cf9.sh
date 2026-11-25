#!/bin/sh
# Act 18 §5 — board-trail completeness cross-check (POSIX /bin/sh; no Bash).
#
# For each board-originated work item recorded in Git, this script confirms
# whether its originating Antonina issue carries a post-completion update that
# reaches a terminal state and/or a stage marker, and counts automated
# ("chatter") lines. Deterministic: the same board + Git inputs always yield
# the same output. It reports facts only; the independent Judiciary interprets
# them (Act 15 §2 — no reform proposals). Same-model / measurement-reliability
# limits are reported by the caller, not hidden.
#
# Terminal rule (Act 18 §3.3/§3.4), identical to government/board-trail-index.py
# §7: a terminal update carries a stage marker AND a DECLARED terminal state in a
# declaration position. Inline-code/quoted spans are stripped before matching, so
# a comment that merely QUOTES a declaration (e.g. the classifier's own fixture)
# cannot false-positive; automated [scheduler-turn]/[terminal-handoff]/
# [progress-checkpoint] lines are excluded (§3.3.4).
#
# Output: one JSON object per line (JSONL) on stdout, one per originating
# issue, with classified fields. The caller (government/judiciary-measurements.py)
# aggregates the §5 metrics and records the honest limitations.
#
# Input mapping: records/board-trail/originating.tsv (Git). When the Executive's
# generated records/board-trail/index.json (Act 18 §3.8) exists it is the
# preferred input; this mapping is the fallback.
set -eu

town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
map=$town/records/board-trail/originating.tsv
sep=$(printf '\t')
max_pages=20
if [ ! -f "$map" ]; then
    echo "board-trail-check: no cross-check mapping at $map" >&2
    exit 1
fi

# Bounded retry for a read-only board page. A transient board error is retried
# with a short backoff; a persistent failure marks that issue board_readable
# false instead of aborting the whole lens — a failed board call is not evidence
# of a missing terminal update (Act 18 §2/§7).
board_show() {
    tries=${VICHE_BOARD_TRAIL_RETRIES:-3}
    backoff=${VICHE_BOARD_TRAIL_BACKOFF:-1}
    case "$tries" in ''|*[!0-9]*) tries=3;; esac
    [ "$tries" -ge 1 ] || tries=1
    case "$backoff" in ''|*[!0-9]*) backoff=1;; esac
    n=0
    while [ "$n" -lt "$tries" ]; do
        n=$((n + 1))
        if out=$(antonina board show --id "$1" --page "$2" --json 2>/dev/null); then
            printf '%s' "$out"
            return 0
        fi
        if [ "$n" -lt "$tries" ]; then
            sleep "$backoff"
        fi
    done
    return 1
}

while IFS="$sep" read -r issue work act epoch type; do
    case "$issue" in ''|'#'*|issue) continue ;; esac
    case "$epoch" in ''|*[!0-9]*) epoch=0 ;; esac
    page=1
    all='[]'
    readable=1
    while :; do
        if data=$(board_show "$issue" "$page"); then :; else
            readable=0
            break
        fi
        msgs=$(printf '%s' "$data" | jq -c '.messages // []')
        n=$(printf '%s' "$msgs" | jq 'length')
        if [ "$n" -ge 50 ] && [ "$page" -ge "$max_pages" ]; then
            # A full final allowed page means more history may exist. Treat the
            # scan as incomplete rather than silently declaring a terminal gap.
            readable=0
            break
        fi
        # Keep page arrays on stdin: passing accumulated histories as jq argv
        # eventually exceeds ARG_MAX on high-volume originating issues.
        all=$(printf '%s\n%s\n' "$all" "$msgs" | jq -s -c '.[0] + .[1]')
        [ "$n" -lt 50 ] && break
        page=$((page + 1))
    done
    if [ "$readable" -eq 0 ]; then
        echo "board-trail-check: board unreadable for #$issue; recorded as unreadable, not a gap" >&2
        jq -cn --arg issue "$issue" --arg work "$work" --arg act "$act" \
            --arg type "$type" --argjson epoch "$epoch" \
            '{issue:$issue,work:$work,act:$act,type:$type,enacted_epoch:$epoch,
              comments_total:null,post_completion:null,terminal:null,
              stage_markers:"",chatter:null,latest_iso:"-",board_readable:false}'
        continue
    fi
    printf '%s\n' "$all" | jq -c \
        --arg issue "$issue" --arg work "$work" --arg act "$act" \
        --arg type "$type" --argjson epoch "$epoch" '
        def clean: (.createdAt // "") | sub("\\.[0-9]+Z$"; "Z");
        # Act 18 §3.3.4: automated scheduler/agent status lines are not updates.
        def automated: test("(?i)\\[(scheduler-turn|terminal-handoff|progress-checkpoint)\\]");
        # A terminal token counts only when DECLARED, never inside an inline-code
        # or quoted span: strip those before matching so a comment that merely
        # QUOTES a declaration (or the classifier own fixture) cannot false-positive.
        def unquoted: gsub("`[^`]*`"; " ") | gsub("\"[^\"\\n]*\""; " ");
        def stage_marker: test("(?i)stage\\s*marker[^\\n]{0,12}\\b(proposal|enactment|deployment|verification)\\b");
        def terminal_decl: test("(?m)(^|[.:;—-]\\s*|(?i:state|status|terminal|result|outcome|transition)\\s+)(verification:confirmed|verification:blocked|enactment:not_enacted|deferred)([.\\s,;:]|$)");
        ($epoch | if . > 0 then todate else "" end) as $since |
        [ .[] | {a:(.author // ""), b:(.body // ""), t:clean} ] as $c |
        (if $epoch > 0 then ($c | map(select(.t > $since))) else $c end) as $p |
        ($p | map(.b)) as $pb |
        {
          issue: $issue, work: $work, act: $act, type: $type,
          enacted_epoch: $epoch,
          comments_total: ($c | length),
          post_completion: ($p | length),
          terminal: (if ([ $pb[] |
                         select(automated | not) |
                         unquoted |
                         (stage_marker and terminal_decl)
                       ] | any)
                    then 1 else 0 end),
          stage_markers: ([$pb[] | scan("(?i)stage\\s*marker[^\\n]{0,12}\\b(proposal|enactment|deployment|verification)\\b")[0]] | unique | join(",")),
          chatter: ($pb | map(select(automated)) | length),
          latest_iso: (if ($c | length) > 0 then ($c | map(.t) | max) else "-" end),
          board_readable: true
        }'
done < "$map"
