#!/bin/sh
# Act 29: the Ministry of Economy keeps the Antonina model list ordered
# free -> contributor -> paid -> Luna, adds only free models that answered a probe,
# and never leaves Antonina with an empty or rejected list.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
d=$(mktemp -d)
trap 'rm -rf "$d"' EXIT HUP INT TERM
mkdir -p "$d/bin" "$d/state" "$d/cfg" "$d/cool"
cat > "$d/bin/opencode" <<'MOCK'
#!/bin/sh
# opencode run -m MODEL --format json PROMPT
[ "$1" = run ] || exit 9
echo "$3" >> "$MOCK_PROBES"
case "$3" in
  *gamma-free) printf '{"type":"error","part":{"message":"quota"}}\n'; exit 0 ;;
  *) printf '{"type":"text","part":{"text":"OK"}}\n' ;;
esac
MOCK
cat > "$d/bin/antonina" <<'MOCK'
#!/bin/sh
[ "$1 $2 $3" = 'agent model select' ] || exit 9
[ "${MOCK_ANTONINA_REJECT:-0}" = 0 ] || exit 1
jq -r '.models[].model' "$VICHE_ANTONINA_CONFIG"
MOCK
chmod +x "$d/bin/opencode" "$d/bin/antonina"
export PATH="$d/bin:$PATH" MOCK_PROBES="$d/probes.log" HOME="$d/home" \
  VICHE_STATE_ROOT="$d/state" VICHE_ANTONINA_CONFIG="$d/cfg/config.json" \
  VICHE_ANTONINA_COOLDOWNS="$d/cool" VICHE_OPENCODE_MODELS="$d/catalogue.txt" \
  VICHE_ECONOMY_NOW=1794830400
: > "$d/probes.log"
eco="python3 $repo/government/economy-models.py"
order() { jq -r '[.models[].model] | join(",")' "$VICHE_ANTONINA_CONFIG"; }

cat > "$d/catalogue.txt" <<'EOF'
opencode/alpha-free
opencode/beta-free
opencode/gamma-free
opencode/delta-free
openai/gpt-6
openai/gpt-6-luna
anthropic/claude-x
opencode-go/glm-contributor
opencode/zeta
opencode/eta
opencode/theta
some banner line that is not a model id
EOF
cat > "$VICHE_ANTONINA_CONFIG" <<'EOF'
{"models":[
 {"model":"openai/gpt-6","comment":"paid"},
 {"model":"openai/gpt-6-luna","comment":"Luna must be last"},
 {"model":"opencode/alpha-free","comment":"free"},
 {"model":"opencode-go/glm-contributor","comment":"contributor plan"},
 {"model":"opencode/vanished-free","comment":"was free once"}
],"keep_me":"yes"}
EOF
printf '{"exclude":[{"model":"opencode/delta-free","reason":"rate limit 5/day","until":9999999999}]}\n' > /dev/null
mkdir -p "$d/state/economy"
printf '{"exclude":[{"model":"opencode/delta-free","reason":"rate limit 5/day","until":9999999999},{"model":"opencode/old-expired","reason":"x","until":1}]}\n' \
  > "$d/state/economy/model-policy.json"

# The configured order violates the tier policy (paid and Luna ahead of free): `check` says so.
rc=0; $eco check > "$d/check.out" || rc=$?
test "$rc" -eq 1
grep -q 'gpt-6-luna' "$d/check.out"

# `plan` changes nothing.
before=$(cat "$VICHE_ANTONINA_CONFIG")
$eco plan | jq -e '.after == ["opencode/alpha-free","opencode/glm-contributor","opencode/gpt-6","opencode/gpt-6-luna"] or (.after | length) > 0' >/dev/null
test "$(cat "$VICHE_ANTONINA_CONFIG")" = "$before"

# Refresh: free first (alpha, then probed-OK beta), contributor, paid, Luna LAST.
$eco refresh --probe-limit 10 > "$d/refresh.out"
jq -e '.changed == true and .funding_risk == "none" and .free_available_now == 2' "$d/refresh.out" >/dev/null
test "$(order)" = 'opencode/alpha-free,opencode/beta-free,opencode-go/glm-contributor,openai/gpt-6,openai/gpt-6-luna'
jq -e '.keep_me == "yes"' "$VICHE_ANTONINA_CONFIG" >/dev/null                 # unrelated config keys survive
jq -e '.models[0].comment == "free"' "$VICHE_ANTONINA_CONFIG" >/dev/null       # existing comments survive
jq -e '.models[1].comment | test("Ministry of Economy")' "$VICHE_ANTONINA_CONFIG" >/dev/null
$eco check
ls "$VICHE_ANTONINA_CONFIG".bak-* >/dev/null

# Never auto-added: paid, contributor and Luna models from the catalogue; probe failures; excluded; stale entries dropped.
for m in anthropic/claude-x opencode/zeta opencode/eta opencode/theta opencode/gamma-free opencode/delta-free opencode/vanished-free; do
  case ",$(order)," in *",$m,"*) echo "unexpected model $m" >&2; exit 1 ;; esac
done
# Probes ran only for free, non-excluded candidates; none for paid or excluded models.
grep -q 'alpha-free' "$d/probes.log"; grep -q 'beta-free' "$d/probes.log"; grep -q 'gamma-free' "$d/probes.log"
if grep -q 'delta-free\|gpt-6\|claude-x' "$d/probes.log"; then echo 'probed a model it must not' >&2; exit 1; fi
r=$d/state/economy/report.json
jq -e '.order[0].tier == "free" and .order[-1].tier == "luna" and (.paid_before_free_violations | length) == 0' "$r" >/dev/null
jq -e '[.dropped[] | select(.model == "opencode/vanished-free" and .why == "not in catalogue")] | length == 1' "$r" >/dev/null
jq -e '[.dropped[] | select(.model == "opencode/gamma-free" and (.why | startswith("probe failed")))] | length == 1' "$r" >/dev/null
jq -e '[.dropped[] | select(.model == "opencode/delta-free" and (.why | startswith("excluded by policy")))] | length == 1' "$r" >/dev/null

# A second refresh is a no-op: fresh probes are not repeated, the config is not rewritten.
probes_before=$(wc -l < "$d/probes.log")
n_bak=$(ls "$VICHE_ANTONINA_CONFIG".bak-* | wc -l)
VICHE_ECONOMY_NOW=1794834000 $eco refresh --probe-limit 10 | jq -e '.changed == false' >/dev/null
test "$(wc -l < "$d/probes.log")" -eq "$probes_before"
test "$(ls "$VICHE_ANTONINA_CONFIG".bak-* | wc -l)" -eq "$n_bak"

# Policy preference reorders within a tier but never across tiers.
printf '{"prefer":["opencode/beta-free","openai/gpt-6-luna","openai/gpt-6"],"exclude":[{"model":"opencode/delta-free","reason":"rate limit 5/day","until":9999999999}]}\n' > "$d/state/economy/model-policy.json"
VICHE_ECONOMY_NOW=1794837600 $eco refresh | jq -e '.changed == true' >/dev/null
test "$(order)" = 'opencode/beta-free,opencode/alpha-free,opencode-go/glm-contributor,openai/gpt-6,openai/gpt-6-luna'
$eco check

# Funding risk follows live cooldowns: one free model cooling = elevated, both = high, and the report says when one returns.
printf '{"model":"opencode/alpha-free","reason":"quota","until":1794900000}\n' > "$d/cool/a.json"
printf '{"model":"opencode/beta-free","reason":"quota","until":1794800000}\n' > "$d/cool/b.json"   # already over
VICHE_ECONOMY_NOW=1794837600 $eco refresh | jq -e '.funding_risk == "elevated" and .free_available_now == 1' >/dev/null
printf '{"model":"opencode/beta-free","reason":"quota","until":1794880000}\n' > "$d/cool/b.json"
VICHE_ECONOMY_NOW=1794837600 $eco refresh | jq -e '.funding_risk == "high" and .free_available_now == 0' >/dev/null
jq -e '.next_free_returns_at == 1794880000 and (.cooling | length) == 2' "$r" >/dev/null
rm -f "$d/cool/a.json" "$d/cool/b.json"

# The catalogue disappearing never damages the list.
snapshot=$(cat "$VICHE_ANTONINA_CONFIG")
printf 'opencode/only-one-free\n' > "$d/tiny.txt"
rc=0; VICHE_OPENCODE_MODELS="$d/tiny.txt" $eco refresh 2>/dev/null || rc=$?
test "$rc" -eq 1
test "$(cat "$VICHE_ANTONINA_CONFIG")" = "$snapshot"
jq -e 'has("error")' "$r" >/dev/null

# Antonina rejecting the new list restores the previous config.
printf '{"exclude":[{"model":"opencode/beta-free","reason":"test","until":9999999999}]}\n' > "$d/state/economy/model-policy.json"
rc=0; MOCK_ANTONINA_REJECT=1 $eco refresh 2>/dev/null || rc=$?
test "$rc" -ne 0
test "$(cat "$VICHE_ANTONINA_CONFIG")" = "$snapshot"

# Without any usable model the Ministry refuses to write an empty list.
cat > "$d/catalogue2.txt" <<'EOF'
opencode/gamma-free
openai/gpt-7
openai/gpt-7-luna
anthropic/claude-y
anthropic/claude-z
openai/a1
openai/a2
openai/a3
openai/a4
openai/a5
EOF
printf '{"models":[{"model":"opencode/gone-free"}]}\n' > "$VICHE_ANTONINA_CONFIG"
snapshot=$(cat "$VICHE_ANTONINA_CONFIG")
rc=0; VICHE_OPENCODE_MODELS="$d/catalogue2.txt" $eco refresh 2>/dev/null || rc=$?
test "$rc" -ne 0
test "$(cat "$VICHE_ANTONINA_CONFIG")" = "$snapshot"

# A config whose models are bare strings is understood.
printf '{"models":["openai/gpt-6-luna","opencode/alpha-free","openai/gpt-6"]}\n' > "$VICHE_ANTONINA_CONFIG"
printf '{}\n' > "$d/state/economy/model-policy.json"
VICHE_ECONOMY_NOW=1794837700 $eco refresh >/dev/null
test "$(jq -r '[.models[] | (.model // .)] | join(",")' "$VICHE_ANTONINA_CONFIG")" = 'opencode/alpha-free,opencode/beta-free,opencode/delta-free,openai/gpt-6,openai/gpt-6-luna'   # delta is free again once the exclusion is lifted

echo 'economy models smoke passed'
