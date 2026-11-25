# antonina-af5dRQwDAnkgZOmtlYljuS-stationed

Session: ses_e3ce73063ffeztvf264QoAm2n2
Workspace: /home/lubko/soring-fronts/abc-witness-decidability-alln
Created: 1794274545975; updated: 1794276495253

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 620 (msg_1c3367bad00162sniDUAwHLzjF)

Completed the front and posted once to #301.

**Recovery check:** inspected Git state, `/tmp/opencode`, and #301 before acting. This front had no prior comment; the previous interrupted turn left no board/commit side effects. The only prior work present was a different front's scratch. Posted exactly once.

**Board effect:** `#301`, comment id `sha256:CHaZYZMpwt2AiYrMPh_DSzOdXSqZGDiaL816u9cyWUc`, author `SoringP1 frontier: abc-witness-decidability-alln`, 02:07:52Z.

**Main results in the post:**
- **Proved infinite no-bilateral family:** for every `n >= 12`, a height-two poset with no bilateral pair. Construction: Sidon circulant with `D={0,1,3}` in `Z_q`, `q>=7`, plus isolated element for odd `n`; `P1` handles `n=12` and `P1`+isolated handles `n=13`.
- **No-pair obstruction beyond 12:** exact `n=13`, `n=14` extensions of `P2`, and a new `n=22` circulant with zero good-slave pairs and no balanced pair, but a C witness.
- **Structural characterisation:** exact `O(n^2)` matrix criterion for bilateral failure; showed it does not characterise no-pair-certificate.
- **Exhaustive n<=9 canonical census:** local criterion misses only balanced-B cases; all misses verified by exact DP.
- **Honest limit:** infinite no-pair-certificate family, polynomial decidability, and NP/#P-hardness remain open; precise missing reduction stated.

No repo, Lean, branch, or PR changes; worktree remains clean at `6a96398`.
