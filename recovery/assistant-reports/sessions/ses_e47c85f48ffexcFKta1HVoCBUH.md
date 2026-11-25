# antonina-MA2p3F4AtqCjlIgU0CcPDL-female

Session: ses_e47c85f48ffexcFKta1HVoCBUH
Workspace: /home/lubko/soring-fronts/exec-core-deletion-lemma-proof-20261108
Created: 1794092015887; updated: 1794092025705

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 21 (msg_1b837ae0e0013ACbuREIEhBE2B)

I can’t provide a complete proof or a counterexample to Lemma C. The suggested map \(x\mapsto y_x\) does establish the following **deduction**:

For every maximal \(x\) of a finite core \(P\), there is an element \(y_x\) universal in \(P-x\), and \(y_x\parallel x\). Existence follows because \(P-x\) is not a core; if \(y_x\) were comparable with \(x\), it would be universal in \(P\), contradicting that \(P\) is a core.

This also yields a useful local constraint: for any \(z\ne x,y_x\), \(z\) is comparable with \(y_x\). But I do not have a proof that these constraints force a maximal \(x\) whose deletion is a core. In particular, I cannot close the case where the witnesses \(y_x\) are nonmaximal and vary with \(x\); nor can I rule out a reciprocal incomparable pair producing an ordinal decomposition in every remaining case. So no stronger lemma—and no conclusion about the census completeness claim—is established here.

I read `AGENTS.md`; `docs/research-core-reduction.md` is absent. I treated `/tmp/opencode/core_only.py` only as motivation, not proof. No code or repository files were changed.
