#!/bin/sh
# Founder directive 2026-11-16: exactly ten lines, posted at most once a day,
# no model call, and unreadable sources are reported, never shown as zero.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
mkdir -p "$d/bin" "$d/town/government" "$d/town/records" "$d/state/institutional-cases" \
  "$d/xdg-state/antonina/agents/a1" "$d/xdg-state/antonina/agents/s1" "$d/xdg-state/antonina/model-cooldowns" \
  "$d/xdg-config/antonina" "$d/home"
cp "$repo/government/handoff-queue.sh" "$repo/government/daily-digest.py" "$d/town/government/"
git -C "$d/town" init -q -b main
git -C "$d/town" -c user.name=t -c user.email=t@example.test commit -q --allow-empty -m 'baseline'
mkdir -p "$d/town/government/x"; printf 'law\n' > "$d/town/government/x/law.md"
git -C "$d/town" add -A; git -C "$d/town" -c user.name=t -c user.email=t@example.test commit -q -m 'Repeal handoff preemption'
printf 'r\n' > "$d/town/records/r.md"
git -C "$d/town" add -A; git -C "$d/town" -c user.name=t -c user.email=t@example.test commit -q -m 'Clerk: record cursor'
/bin/sh "$d/town/government/handoff-queue.sh" add "$d/town" clerk evidence 'Judiciary: fact-find the reconciliation' >/dev/null
now=$(date +%s)
printf '{"id":"x:1","signal":"judiciary_mailbox_pending","state":"open","first_seen":%s,"owner":"judiciary"}\n' "$((now - 3 * 86400))" \
  > "$d/state/institutional-cases/judiciary_mailbox_pending.json"
printf '{"auto_closed":[{"id":"innovation_stale:5","closed_at":%s}]}\n' "$now" > "$d/state/institutional-cases/index.json"
printf '{"models":[{"model":"p/luna","comment":""},{"model":"p/beam","comment":""}]}\n' > "$d/xdg-config/antonina/config.json"
printf '{"model":"p/luna","reason":"rate_limited","until":%s}\n' "$((now + 7200))" > "$d/xdg-state/antonina/model-cooldowns/p@luna.json"
ms=$((now * 1000 - 1000))
printf '{"title":"Viche: Clerk","cwd":"/v"}\n' > "$d/xdg-state/antonina/agents/a1/meta.json"
printf '{"type":"step_finish","timestamp":%s,"sessionID":"ses_a","part":{"tokens":{"input":300,"output":0,"cache":{"read":0}}}}\n{"type":"error","timestamp":%s,"sessionID":"ses_a","error":{"type":"provider.rate-limit"}}\n' "$ms" "$ms" > "$d/xdg-state/antonina/agents/a1/output.log"
printf '{"title":"SoringP1 frontier: x","cwd":"/s"}\n' > "$d/xdg-state/antonina/agents/s1/meta.json"
printf '{"type":"step_finish","timestamp":%s,"sessionID":"ses_b","part":{"tokens":{"input":100,"output":0,"cache":{"read":0}}}}\n' "$ms" > "$d/xdg-state/antonina/agents/s1/output.log"
cat > "$d/bin/antonina" <<MOCK
#!/bin/sh
case "\$1 \$2" in
  'board list') if [ "\${BOARD_DOWN:-}" = yes ]; then exit 4; fi
    if [ "\$6" = 1 ]; then printf '[{"number":"9","title":"Done thing","updatedAt":"%s"}]\n' "\$(date -u +%FT%TZ)"; else printf '[]\n'; fi ;;
  'board show') printf '{"messages":[{"author":"Viche Clerk","createdAt":"%s","body":"Agenda\\\\nNEEDS-FOUNDER: approve paid quota for the research fleet"},{"author":"Vitalik","createdAt":"%s","body":"NEEDS-FOUNDER: ignored, from the Founder"}]}\n' "\$(date -u +%FT%TZ)" "\$(date -u +%FT%TZ)" ;;
  'board comment') printf '%s\n' "\$*" >> "$d/comments" ;;
  'agent list') printf '{"agents":[{"id":"a1","state":"running","finished_at":null},{"id":"s1","state":"failed","finished_at":%s}],"unreadable":[]}\n' "$now" ;;
  *) echo "unexpected: \$*" >&2; exit 9 ;;
esac
MOCK
chmod +x "$d/bin/antonina"
export PATH="$d/bin:$PATH" VICHE_TOWN_ROOT="$d/town" VICHE_STATE_ROOT="$d/state" HOME="$d/home" \
  XDG_STATE_HOME="$d/xdg-state" XDG_CONFIG_HOME="$d/xdg-config" VICHE_DIGEST_REPOS= VICHE_TOWNHALL_ID=302
python3 "$d/town/government/daily-digest.py" > "$d/out"
test "$(wc -l < "$d/out")" -eq 10
grep -Fq 'Shipped (Viche main): 1 law/code change(s), 1 records-only commit(s) — Repeal handoff preemption' "$d/out"
grep -Fq 'board issues closed (whole board): 1 — Done thing' "$d/out"
grep -Fq 'Agent runs finished: 1 (0 clean, 1 failed, 0 stopped/killed); 1 running now' "$d/out"
grep -Fq 'Blocked (handoffs): 1 open' "$d/out"
grep -Fq 'Blocked (cases): 1 open, oldest 3d (judiciary_mailbox_pending, owner judiciary); auto-closed in window: 1' "$d/out"
grep -Fq 'Quota split (context+output tokens): town 75%, SoringP1 25%' "$d/out"
grep -Fq 'Models: 1/2 usable now — luna rate limited for' "$d/out"
grep -Fq '0 quota, 1 rate' "$d/out"
grep -Fq 'Needs you: approve paid quota for the research fleet' "$d/out"
if grep -Fq 'ignored, from the Founder' "$d/out"; then echo 'Founder text must not be echoed as a request' >&2; exit 1; fi
# An unreadable source is named as unavailable, never shown as zero.
BOARD_DOWN=yes python3 "$d/town/government/daily-digest.py" > "$d/out2"
test "$(wc -l < "$d/out2")" -eq 10
grep -Fq 'Shipped (elsewhere): unavailable' "$d/out2"
# Every model cooling is something only the Founder can fix.
printf '{"model":"p/beam","reason":"quota_exhausted","until":%s}\n' "$((now + 7200))" > "$d/xdg-state/antonina/model-cooldowns/p@beam.json"
python3 "$d/town/government/daily-digest.py" | grep -Fq 'every configured model is rate-limited or out of quota'
# Posting: not before the configured hour, then once per UTC day.
noon=$(( (now / 86400) * 86400 + 16 * 3600 ))
VICHE_DIGEST_HOUR=17 python3 "$d/town/government/daily-digest.py" --post --now "$noon" >/dev/null
test ! -e "$d/comments"
VICHE_DIGEST_HOUR=15 python3 "$d/town/government/daily-digest.py" --post --now "$noon" >/dev/null
test "$(grep -c 'board comment --id 302 --author Viche daily digest' "$d/comments")" -eq 1
test -s "$d/state/digest/$(date -u -d "@$noon" +%F).md"
VICHE_DIGEST_HOUR=15 python3 "$d/town/government/daily-digest.py" --post --now "$((noon + 600))" >/dev/null
test "$(grep -c 'board comment' "$d/comments")" -eq 1
echo 'Daily digest smoke passed'
