#!/bin/sh
# Sample host metrics for one sitting. POSIX-compliant per AGENTS.md.
# Usage: sh sample-metrics.sh <sitting-id>
set -eu
sitting_id=${1:?usage: sample-metrics.sh <sitting-id>}
town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}

ram_total=$(free -m | awk '/^Mem:/{print $2}')
ram_used=$(free -m | awk '/^Mem:/{print $3}')
# Act 10 §1 (renewed): the binding constraint is the cgroup cap, not host RAM.
# cgroup v2 paths; fall back to 0/empty so the field is always present.
cgroup_mem_current=$(cat /sys/fs/cgroup/memory.current 2>/dev/null || echo 0)
cgroup_mem_max=$(cat /sys/fs/cgroup/memory.max 2>/dev/null || echo 0)
cgroup_max_hits=$(awk '/^max /{print $2}' /sys/fs/cgroup/memory.events 2>/dev/null || echo 0)
cgroup_oom_kill=$(awk '/^oom_kill /{print $2}' /sys/fs/cgroup/memory.events 2>/dev/null || echo 0)
load=$(uptime | sed 's/.*load average: //')
# pgrep -c prints 0 but exits 1 when no process matches. Do not echo a second
# 0: an embedded newline would corrupt this tab-separated row.
seat_agents=$(pgrep -c opencode 2>/dev/null || :)
seat_agents=${seat_agents:-0}
seat_rss=$(ps -eo rss,comm | awk '/opencode/{sum+=$1} END{printf "%.0f", sum/1024}')
cpus=$(nproc)
ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
ballots=$(cat "$town"/records/ballots/*.tsv 2>/dev/null | wc -l)
bills=$(ls "$town"/records/bills/*.md 2>/dev/null | wc -l)
deliverables=$(git -C "$town" log --oneline --since="24 hours ago" 2>/dev/null | wc -l)

printf 'sitting_id\tts\tram_total_mb\tram_used_mb\tload\tseat_agents\tseat_rss_mb\tcpus\tballots_on_main\tbills_on_main\tdeliverables_24h\tcgroup_mem_current\tcgroup_mem_max\tcgroup_max_hits\tcgroup_oom_kill\n'
printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$sitting_id" "$ts" "$ram_total" "$ram_used" "$load" "$seat_agents" "$seat_rss" "$cpus" "$ballots" "$bills" "$deliverables" \
    "$cgroup_mem_current" "$cgroup_mem_max" "$cgroup_max_hits" "$cgroup_oom_kill"
