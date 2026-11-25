# Billy-dev workspace recovery

This archive deduplicates source and research text across 1,574 SoringP1 directories.
Each manifest lists its original relative workspace, HEAD, local branch refs, and
files that differ from the current main checkout, plus untracked source files.
Use the filename mapping to find each content object. The object name is a
SHA-256 of the initial sanitized content, followed by the source extension.
Additional credential-like-line redactions (if any) are separately logged.

The commits directory contains textual Git patches keyed by original commit ID
for historical commits outside current main. A patch is evidence of historical
work, not a claim it was merged, tested, or unpublished. Merge diffs are relative
to their first parent. Use the original ref mappings for provenance.

Build products, caches, dependencies, binary files and oversized files are not
archived here. Missing and oversize permitted source entries are listed in
manifests; the scan error is listed in summary.json. The original workspaces
are untouched.
