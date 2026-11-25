# antonina-adfLWDfu9EiTRBxoGQpORF-balls

Session: ses_e1896e643ffeuiG0d0NsaC2klV
Workspace: /home/lubko/soring301-exec-optimal-viable-state-counting-20261117
Created: 1794883787229; updated: 1794884568959

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 332 (msg_1e774fdae0017tbS7U79q4tjVC)

Created `exec-report.md` and posted a concise, non-duplicate summary to Antonina #301.

Key result: criteria (a)–(c) do not imply (d). Independent exact checks for `n=3..6` show labelled failure counts `(a)∩(b)∩(c) \ (d)` of `0,0,700,7500` and unlabelled (quotient) failures `0,0,10,23`. Thus “locally viable” is not “optimal-play reachable”; every (c)-viable state is not (d)-optimal-reachable. Set (d) has the trivial `n!` leaf lower bound `2^{Θ(n log n)}`, but no stronger all-n superpolynomial lower bound or polynomial upper bound was proved; the obstruction is the missing ancestor-optimality condition. No Lean/repo/PR changes.
