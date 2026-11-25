#!/bin/sh
# Hermetic: autonomous legislative office, cadence, model-neutrality, health inquiry.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
mkdir -p "$scratch/town/government" "$scratch/town/records" "$scratch/bin" "$scratch/state/branches"
printf 'c1a00001\tClerk\tlegislature\n' > "$scratch/town/government/seats.tsv"
printf '%s\n' c1e00011 > "$scratch/town/records/SUMMONED.txt"
printf 'Founder test constitution, model neutral\n' > "$scratch/constitution"
touch "$scratch/state/inaugurated"
cat > "$scratch/town/government/branch-bootstrap.sh" <<'BOOT'
#!/bin/sh
mkdir -p "$VICHE_SEATS_ROOT/branches/innovation-centre"
BOOT
chmod +x "$scratch/town/government/branch-bootstrap.sh"
cat > "$scratch/bin/antonina" <<'MOCK'
#!/bin/sh
set -eu
case "$1 $2" in
 "agent status")
  printf '{"state":"%s","model":"%s","variant":"%s","last_activity_at":%s}\n' "$MODE" "$MODEL" "$VARIANT" "$ACTIVITY" ;;
 "agent run")
  case "$*" in *"INNOVATION CENTRE"*"cannot originate or authorize external projects"*"Parliament alone"*) : ;;
   *) echo "Required scope/authority missing from prompt" >&2; exit 1;; esac
  case "$*" in *"seriously investigate EXISTING software"*"Do NOT assume existing software must be adopted"*) : ;;
   *) echo "Missing balanced existing-software evaluation guidance" >&2; exit 1;; esac
  case "$*" in *"HIGHEST EXPECTED MARGINAL RETURN ON INVESTMENT"* ) : ;;
   *) echo "Missing high-return Founder priority" >&2; exit 1;; esac
  case "$*" in *"Opportunity cost matters"* ) : ;;
   *) echo "Missing marginal-benefit baseline" >&2; exit 1;; esac
  printf 'sent\n' >> "$DISPATCHES" ;;
 *) echo "Unexpected mock: $*" >&2; exit 1 ;;
esac
MOCK
chmod +x "$scratch/bin/antonina"
PATH=$scratch/bin:$PATH
mkdir -p "$scratch/town/government"
cp "$repo/tests/appointment-id-stub.sh" "$scratch/town/government/appointments.sh"
cp "$repo/government/AGENT-REPORTING-POLICY.md" "$scratch/town/government/AGENT-REPORTING-POLICY.md"
cp "$repo/government/delivery-candidates.py" "$scratch/town/government/delivery-candidates.py"
cp "$repo/government/agent-state.sh" "$scratch/town/government/agent-state.sh"
# Fixture law, deliberately WITHOUT the Executive Innovation Office heading.
# Four scripts grep LAWS.md for that heading to choose the office model; this
# fixture asserts the LEGISLATIVE path, so it supplies a minimal law that does
# not contain it. This is fixture data, not a claim about enacted law.
cat > "$scratch/town/government/LAWS.md" <<'LAWS'
# Laws of Viche (fixture)

## Act 1 — Parliament

Fixture law used only by this smoke test. It intentionally does not contain an
Executive Innovation Office enactment heading, because this test exercises the
legislative Innovation Centre path.
LAWS
VICHE_TOWN_ROOT=$scratch/town
VICHE_SEATS_ROOT=$scratch/seats
VICHE_STATE_ROOT=$scratch/state
VICHE_CONSTITUTION=$scratch/constitution
VICHE_INNOVATION_NOW=1000
MODE=idle MODEL=test-provider/example VARIANT=low ACTIVITY=1000
DISPATCHES=$scratch/runs
export PATH VICHE_TOWN_ROOT VICHE_SEATS_ROOT VICHE_STATE_ROOT VICHE_CONSTITUTION
export VICHE_INNOVATION_NOW MODE MODEL VARIANT ACTIVITY DISPATCHES
cp "$repo/government/INNOVATION-CENTRE.md" "$scratch/town/government/INNOVATION-CENTRE.md"
cp "$repo/government/AGENT-REPORTING-POLICY.md" "$scratch/town/government/AGENT-REPORTING-POLICY.md"
# A pre-transfer fixture has no Executive Innovation Office Act enacted.
printf '# Historic Act 14 pilot; no Act 25\n' > "$scratch/town/government/LAWS.md"
mkdir -p "$scratch/state/institutional-outcomes" "$scratch/state/institutional-cases"
printf '{"observed_at":23000}\n' > "$scratch/state/institutional-outcomes/latest.json"
printf '{"observed_at":23000,"count":0}\n' > "$scratch/state/institutional-cases/index.json"
printf '{"observed_at":23000}\n' > "$scratch/state/branches/judiciary-measurements.json"
# Standing written mandate must agree with the dispatch prompt.
grep -Fq "Existing-software evaluation (Founder guidance)" "$scratch/town/government/INNOVATION-CENTRE.md"
grep -Fq "neither mandatory nor presumptively superior" "$scratch/town/government/INNOVATION-CENTRE.md"
grep -Fq "Highest-marginal-return focus (Founder guidance)" "$scratch/town/government/INNOVATION-CENTRE.md"
grep -Fq "opportunity cost" "$scratch/town/government/INNOVATION-CENTRE.md"
/bin/sh "$repo/government/innovation-centre-cycle.sh"
[ "$(wc -l < "$DISPATCHES")" -eq 1 ]
jq -e '.legislative_branch==true and .voting_seat==false and .separate_summons==true and .readiness=="dispatched"' "$scratch/state/legislature/innovation-centre/health.json" >/dev/null
# Even a summons listing this ID cannot block the independent office.
MODE=running
/bin/sh "$repo/government/innovation-centre-cycle.sh"
[ "$(wc -l < "$DISPATCHES")" -eq 1 ]
MODE=idle
VICHE_INNOVATION_NOW=1200
export MODE VICHE_INNOVATION_NOW
/bin/sh "$repo/government/innovation-centre-cycle.sh"
[ "$(wc -l < "$DISPATCHES")" -eq 1 ]
VICHE_INNOVATION_NOW=23000
export VICHE_INNOVATION_NOW
/bin/sh "$repo/government/innovation-centre-cycle.sh"
[ "$(wc -l < "$DISPATCHES")" -eq 2 ]
MODEL=other-provider/other-model
export MODEL
/bin/sh "$repo/government/innovation-centre-cycle.sh"
[ "$(wc -l < "$DISPATCHES")" -eq 2 ]
# Checks are mandatory after inauguration, and must not confuse this office
# with a fourth branch or parliamentary voting seat.
for branch in legislature executive judiciary; do
 printf '{"branch":"%s","readiness":"ready","observed_at":23000}\n' "$branch" > "$scratch/state/branches/$branch.json"
done
## branch-health.sh also requires fresh monitoring evidence, not just branches.
## Supply fixture evidence stamped at the same clock so only the innovation
## signal under test can fire.
mkdir -p "$scratch/state/institutional-outcomes" "$scratch/state/institutional-cases"
printf '{"observed_at":23000}\n' > "$scratch/state/institutional-outcomes/latest.json"
printf '{"observed_at":23000,"active":[]}\n' > "$scratch/state/institutional-cases/index.json"
printf '{"observed_at":23000}\n' > "$scratch/state/branches/judiciary-measurements.json"
VICHE_BRANCH_NOW=23000
export VICHE_BRANCH_NOW
/bin/sh "$repo/government/branch-health.sh"
rm "$scratch/state/legislature/innovation-centre/health.json"
if /bin/sh "$repo/government/branch-health.sh" 2>/dev/null; then exit 1; fi
jq -e '.signals | index("innovation_missing")' "$scratch/state/branches/incident.json" >/dev/null
echo 'Independent legislative Innovation Centre smoke checks passed'
