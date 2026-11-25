#!/bin/sh
# Resource-safety guard regression: defers a fresh seat when cgroup headroom is
# below the floor, passes when headroom is adequate, treats "max" (no limit) and
# unreadable cgroup as no-constraint (fail open), and logs every deferral.
# Headroom is measured against UNRECLAIMABLE memory (anon+slab+kernel_stack+sock),
# not memory.current (which includes reclaimable page cache). POSIX /bin/sh only.
# Mocks the cgroup; never touches the live cgroup.
set -eu
root=$(git rev-parse --show-toplevel)
d=$(mktemp -d)
trap 'rm -rf "$d"' 0
town=$d/town
state=$d/state
cgroup=$d/cgroup
mkdir -p "$town/government" "$state" "$cgroup"
cp "$root/government/resource-safety.sh" "$town/government/resource-safety.sh"
cp "$root/government/sitting.sh" "$town/government/sitting.sh"
cp "$root/government/seats.tsv" "$town/government/seats.tsv"
cp "$root/government/AGENT-REPORTING-POLICY.md" "$town/government/AGENT-REPORTING-POLICY.md"

export VICHE_TOWN_ROOT=$town
export VICHE_STATE_ROOT=$state
export RESOURCE_SAFETY_CGROUP_DIR=$cgroup

# set_cgroup MAX_BYTES ANON_BYTES: writes memory.max and a memory.stat whose
# unreclaimable total (anon) yields headroom = MAX - ANON.
set_cgroup() {
    printf '%s\n' "$1" > "$cgroup/memory.max"
    printf 'anon %s\nslab 0\nkernel_stack 0\nsock 0\nfile 0\n' "$2" > "$cgroup/memory.stat"
    # memory.current is present (realistic) but is NOT the headroom basis.
    printf '%s\n' "$2" > "$cgroup/memory.current"
}
MAX=8589934592

# 1. Adequate headroom (2 GiB) -> convene (exit 0), no deferral logged.
set_cgroup "$MAX" 6442450944            # headroom 2 GiB
/bin/sh "$town/government/resource-safety.sh" c1a00003
[ ! -f "$state/resource-safety/deferrals.log" ]

# 1b. Large reclaimable page cache does NOT defer (the bug being fixed).
printf 'anon 1073741824\nslab 0\nkernel_stack 0\nsock 0\nfile 6442450944\n' > "$cgroup/memory.stat"
printf '7516192768\n' > "$cgroup/memory.current"   # current shows only ~1 GiB free
/bin/sh "$town/government/resource-safety.sh" c1a00003   # must PASS (7 GiB unreclaimable-free)
[ ! -f "$state/resource-safety/deferrals.log" ]

# 2. Unreclaimable headroom below floor (1.5 GiB) -> defer (exit 1), low logged.
set_cgroup "$MAX" 6979321856            # headroom 1.5 GiB
if /bin/sh "$town/government/resource-safety.sh" c1a00003; then
    echo "Viche: FAIL - low headroom did not defer" >&2; exit 1
fi
[ -f "$state/resource-safety/deferrals.log" ]
grep -q 'seat=c1a00003' "$state/resource-safety/deferrals.log"
grep -q 'level=low' "$state/resource-safety/deferrals.log"

# 3. Headroom below critical (0.5 GiB) -> defer (exit 1), critical logged.
set_cgroup "$MAX" 8053063680            # headroom 0.5 GiB
if /bin/sh "$town/government/resource-safety.sh" c1a00003; then
    echo "Viche: FAIL - critical headroom did not defer" >&2; exit 1
fi
grep -q 'level=critical' "$state/resource-safety/deferrals.log"

# 4. No cgroup limit (memory.max = max) -> convene (exit 0), no new deferral.
before=$(wc -l < "$state/resource-safety/deferrals.log")
printf 'max\n' > "$cgroup/memory.max"
/bin/sh "$town/government/resource-safety.sh" c1a00003
[ "$(wc -l < "$state/resource-safety/deferrals.log")" -eq "$before" ]

# 5. Unreadable cgroup -> fail open (exit 0), no deferral.
rm -f "$cgroup/memory.max" "$cgroup/memory.current" "$cgroup/memory.stat"
/bin/sh "$town/government/resource-safety.sh" c1a00003
[ "$(wc -l < "$state/resource-safety/deferrals.log")" -eq "$before" ]

# 6. sitting.sh invokes the guard and defers on low headroom (integration).
# Under the real constitutional boot an appointed agent exists. Model that
# benign idle managed agent here so this test measures resource safety only.
mkdir -p "$d/bin"
cat > "$town/government/appointments.sh" <<'APPOINTMENT'
#!/bin/sh
printf 'fixture-agent\n'
APPOINTMENT
cat > "$d/bin/antonina" <<'ANTONINA'
#!/bin/sh
[ "$1" = agent ] && [ "$2" = status ] || exit 1
printf '{"state":"idle"}\n'
ANTONINA
chmod +x "$d/bin/antonina" "$town/government/appointments.sh"
PATH="$d/bin:$PATH"; export PATH
set_cgroup "$MAX" 6979321856            # headroom 1.5 GiB
if /bin/sh "$town/government/sitting.sh" c1a00003 >/dev/null 2>&1; then
    echo "Viche: FAIL - sitting.sh did not defer on low headroom" >&2; exit 1
fi
# 7. sitting.sh convenes (exit 0) when headroom is adequate.
set_cgroup "$MAX" 6442450944            # headroom 2 GiB
/bin/sh "$town/government/sitting.sh" c1a00003 >/dev/null 2>&1

printf 'Viche: resource-safety guard defers below floor, passes when adequate, fails open on unreadable cgroup, and sitting.sh enforces it\n'
