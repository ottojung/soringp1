#!/bin/sh
# The sampler must produce exactly one TSV data row even when pgrep reports 0
# matches with exit status 1 (and when it is unavailable).
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
mkdir -p "$scratch/bin"
cat > "$scratch/bin/pgrep" <<'SH'
#!/bin/sh
printf '0\n'
exit 1
SH
chmod +x "$scratch/bin/pgrep"
PATH=$scratch/bin:$PATH
VICHE_TOWN_ROOT=$repo
export PATH VICHE_TOWN_ROOT
/bin/sh "$repo/records/research/sample-metrics.sh" no-running-agents > "$scratch/sample"
awk -F '\t' '
    NR == 1 { if (NF != 15) exit 1 }
    NR == 2 { if (NF != 15 || $6 != "0") exit 1 }
    END { if (NR != 2) exit 1 }
' "$scratch/sample"

cat > "$scratch/bin/pgrep" <<'SH'
#!/bin/sh
exit 127
SH
chmod +x "$scratch/bin/pgrep"
/bin/sh "$repo/records/research/sample-metrics.sh" pgrep-unavailable > "$scratch/sample"
awk -F '\t' '
    NR == 1 { if (NF != 15) exit 1 }
    NR == 2 { if (NF != 15 || $6 != "0") exit 1 }
    END { if (NR != 2) exit 1 }
' "$scratch/sample"
echo 'Sampler empty-process checks passed'
