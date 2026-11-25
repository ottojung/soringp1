# antonina-SFc4eZsEcg9Quvc9yG3jvk-tolly

Session: ses_e145f9846ffea9q9YJS8e3Isau
Workspace: /home/lubko/soring301-exec-framed-dag-lb-20261117b
Created: 1794954520538; updated: 1794955152077

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 236 (msg_1eba9fa850014XPOsd6PDoUg3S)

Posted successfully to board #301 (comment id `sha256:TgGWcdWRVad2HA7QOLWmbNU7beQ10y5bfnDvoxcSVFQ`, 2026-11-17T22:39:04Z).

Exact state achieved: **stop condition (c)**. No all-n proof-system lower bound (a) and no polynomial-size complete family (b) was established; instead I posted a precise statement of the exact missing lemma — “No Cheap Coarsening Along Optimal Root Play” — that blocks both directions, together with the smallest concrete counterexamples to the tempting shortcuts (n=4: 9-node framed DAG at S(4)=5; n=7: 19-node framed DAG at S(7)=13, verified ACCEPT by `scripts/check_framed_strategy.py`). The post explains why the winning-frontier count does not imply (a) (cheap intersection-joins can merge exponentially many histories, per the hook-length warning), why the known polynomial constructions do not give (b) (bubble/merge/Ford-Johnson height mismatches), and why the missing lemma is exactly the open core. No repository, Lean, test, script, or PR changes were made; the worktree remains clean at HEAD 6a96398.
