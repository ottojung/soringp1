#!/bin/sh
# Records integrity smoke test: durable town records must never carry
# committed merge-conflict markers. Guards against a recurrence of the
# MODEL-COMPLIANCE-REVIEW.md / RESOURCE-2026-10-14.md defect (2026-10-14).
set -eu
root=$(git rev-parse --show-toplevel)
failed=0
for f in $(find "$root/records" "$root/government" "$root/constitution" -type f \( -name '*.md' -o -name '*.tsv' -o -name '*.sh' -o -name '*.conf' -o -name '*.txt' \) 2>/dev/null); do
    if grep -n '^<<<<<<<\|^=======$\|^>>>>>>>' "$f" >/dev/null 2>&1; then
        echo "CONFLICT MARKERS in $f" >&2
        failed=1
    fi
done
if [ "$failed" -ne 0 ]; then
    echo "Records integrity check FAILED: committed conflict markers present" >&2
    exit 1
fi
echo "Viche: records carry no committed merge-conflict markers"
