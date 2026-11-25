# antonina-fcqagr9sn5sv5FPhrdqiYY-exalt

Session: ses_e14795e0dffe0KXSc15ypr7hzX
Workspace: /home/lubko/soring-fronts/sergeev-compatible-polynomial-state-grammar
Created: 1794952831699; updated: 1794953624896

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 341 (msg_1eb92b351001adbf9FgLj43m3A)

Posted a concise finding to board #301 (no repository/Lean changes).

**Finding.** The natural Sergeev container-state compilation does **not** give a polynomial-size framed DAG with sound joins and `o(n)` surplus: sound joins of histories with different container occupancies/insertion orders forget container assignment and shifted interval boundaries, and keeping state count polynomial forces `Ω(1)` bits of forgetting per merged pending element, i.e. `Ω(n)` total surplus. This is a failed approach for the natural grammar, not a proved lower bound for all grammars.

**Limits.** No explicit constant; no proof that an unrelated quotient grammar cannot achieve sublinear forgetting; no Lean formalization. General-poset state counting alone is insufficient because sound joins can merge exponentially many histories cheaply, so the obstruction is specific to Sergeev’s container coupling and the mass/forgetting tradeoff. The decisive open question remains whether any polynomial `S_n`-quotient framed DAG with sublinear forgetting exists.
