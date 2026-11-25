# Browse, search and verify the archive

The GitHub-native [catalogue](../catalog/README.md) requires no tooling.
Every index links to an original report or file; no knowledge depends on an
active service on billy-dev.

For faster search on a clone, use Python 3.10+ (standard library only).
Commands below are run from the repository root.

```sh
# All matching evidence, including full original text
python3 recovery/tools/search.py search cospectral minimax --limit 30

# Restrict search to board messages (includes exact message anchors)
python3 recovery/tools/search.py search "M2" census --kind board

# Search historical task texts or cross-project reports
python3 recovery/tools/search.py search certificate --kind commission --kind mixed

# Search archived GitHub issues
python3 recovery/tools/search.py search adversary --kind github

# Find an original source file by filename or workspace
python3 recovery/tools/search.py search verifyH8 --kind source --metadata

# Print a front, its question and all linked evidence
python3 recovery/tools/search.py front cospectral-gap-span-alln

# Print one original board message (full or unique partial ID)
python3 recovery/tools/search.py board gHz1R5CmcWW1

# List recovered files by their original paths
python3 recovery/tools/search.py workspace soring-fronts/cospectral-gap-span-alln

# Copy changed/additional files out of the archive (does not execute code)
python3 recovery/tools/search.py extract soring-fronts/cospectral-gap-span-alln /tmp/soring-extracted

# Validate source object hashes and catalogue references
python3 recovery/tools/search.py verify

# Rebuild the deterministic Markdown and JSON indices from archived data
python3 recovery/tools/build_catalog.py
python3 recovery/tools/build_catalog.py --check
```

Search uses case-insensitive substring matching; all words must match.
Quote an exact phrase. Repeat `--kind` to select multiple collections.
`--metadata` skips reading full file bodies. Results show the path and line
of an occurrence. The workspace extractor restores the archived changed
and additional files, not a full exact historical checkout. The docs collection includes canonical notes, Lean, scripts and tests. Compressed
experiment data are indexed by metadata rather than decompressed by search.

The archive is historical evidence, not executable trusted code. Read
original scripts before running them. Neither tool launches research agents,
contacts external services, or changes the Lean library. The build tool
only writes `recovery/catalog/`.

[Archive home](../README.md)
