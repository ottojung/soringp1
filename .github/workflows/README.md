# Workflows — none

SoringP1 project checks (the reference-evaluator unittest and the Lean build,
kernel replay, and unfinished-proof/axiom rejection) run **exclusively on
`phoebe-dev`**, the host running Viche, per the project's non-negotiable host
restriction (issue #301).

The previous `ci.yml` executed those checks on GitHub-hosted `ubuntu-latest`
runners, which violates that restriction, and has been removed. Do not
reintroduce GitHub-hosted execution of project checks, builds, tests, Lean
checking, or scripts.

On `phoebe-dev` the checks are:
- `python3 -m unittest discover -s tests -v`
- `lake exe cache get && lake build --wfail`
- `lake env leanchecker SoringP1`
- reject `sorry`/`admit`/`axiom` in `SoringP1` and `SoringP1.lean`
