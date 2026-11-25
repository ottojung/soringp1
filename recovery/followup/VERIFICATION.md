# Integration verification

Verified on 2026-11-25, following integration of the original 77 recovery
commits and the second-pass recovery into the GitHub default branch.

| Check | Outcome |
|---|---|
| Original recovery tip `3b76a8e3b0e143845e12946e2bae9570c3ccee13` is an ancestor of main | Yes |
| Default-branch HEAD observed on GitHub | `852fc194da749e0c7aeca44bb10d52b341e6e640` before this verification note |
| Non-main commit coverage across 49 remote branch references | No missing archived commit patches |
| Commit-object coverage across 784 local SoringP1 Git stores | No unaccounted commit objects |
| Archive integrity in the committed tree, extracted using `git archive` into a separate directory | Zero errors |
| Relative Markdown navigation in that extracted tree | 194 pages, 29,610 links, zero errors |
| Deterministic catalogue regeneration in that extracted tree | Exact match to committed catalogue |
| Existing Python unit tests (`python3 -m unittest discover -s tests`) | 182 tests run: 181 passed, one skipped; zero failures or errors (749.321 s) |
| Maintained Lean source, toolchain, scripts, tests and existing CI changes relative to pre-archive commit `6cddeaa` | None |
| Recovered workspace extraction and historical board-message lookup | Passed |

The catalogue contains 750 fronts, 3,725 board messages, 1,574 workspace
inventories, 2,291 original-name/source-version entries, 1,651 assistant
sessions and additional logs, 1,386 task texts, 1,540 mixed-session texts,
55 GitHub discussion records (issues and pull requests), and 4,952
historical commit patches. These are evidence counts, not theorem counts.

The mathematical library has not been independently re-proved or its Lean
kernel replay rerun in this archival pass. Historical claims retain their
original scope, proof status and corrections. See the [coverage audit](README.md)
for missing scratch paths and selection limits.

## Reproduce the archive checks

From a repository checkout:

```sh
python3 recovery/tools/search.py verify
python3 recovery/tools/verify_navigation.py
python3 recovery/tools/build_catalog.py --check
python3 -m unittest discover -s tests
```

The first three commands need only the checked-in archive and Python's
standard library. They do not rely on the original research host's files.
