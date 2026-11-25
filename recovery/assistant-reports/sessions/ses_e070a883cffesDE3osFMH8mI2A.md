# antonina-u9XONLE2kzHzxrM5qQTbYZ-battles

Session: ses_e070a883cffesDE3osFMH8mI2A
Workspace: /home/lubko/soring-fronts/exec-block-interleaving-forcing-20261120
Created: 1795178199052; updated: 1795178251415

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f8f57a54001axu7HrY9UOHDRy)

I’ll first inspect the current issue/research-board context and the repository’s direct-sum, gadget, realizability, and Sergeev references. I’ll stop rather than manufacture a result if the q-block argument is already covered or reduces only to the known ordered-block theorem.

## Output 126 (msg_1f8f6129f001l2skKBt90WG3h5)

**Stopped: no new all-\(q\) bound.** Issue #48 already states the decisive Sergeev gate: the antichain-root excess is \(o(n)\), so transferring a constant deficit per replicated block is impossible. The #301 digest also shows this exact q-block/interleaving question was commissioned today; the existing ordinal-sum note supplies the relevant direct-sum theorem. Per the stop rule, I found no basis to extend those known facts to a sublinear root excess.

**Theorem / deduction.** For \(q\) blocks whose relative order is known, the state is an ordinal sum, so direct-sum additivity gives cost \(30q\) and only \((12!)^q\) compatible rankings. The unrestricted \(12q\)-key antichain has \((12q)!\) rankings, a factor of \((12q)!/(12!)^q\) more. Thus the ordered-block theorem does not transfer to the root.

**Where the transfer fails.** With unrestricted interleavings, cross-block comparisons are informative. The direct-sum adversary’s product invariant—each query either gives no information across blocks or updates one independent factor—no longer holds. The local \(S(12)=30\) obstruction therefore does not establish that any block gadget is forced against every root strategy.

**Falsification.** An \(\Omega(q)\) excess over \(\lceil\log_2((12q)!)\rceil\) contradicts Sergeev’s \(O(n/(\log n)^{1/5})=o(n)\) excess. A sublinear positive excess is not ruled out by this check, but this replication argument has not established one.

**Next step:** only pursue a root strategy invariant that survives arbitrary cross-block queries and yields a proved sublinear excess; otherwise this replication grammar is a dead end. Relevant references: [issue #48](https://github.com/ottojung/soringp1/issues/48), `docs/research-series-decomposition.md` §2, and `docs/research-sergeev-asymptotic.md`.

I did not post to #301: the requested result would only restate known direct-sum facts plus the already-recorded Sergeev no-go. No repository, Lean, or CI changes were made.
