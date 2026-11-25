# antonina-HZxjBUv9GWXcGZhemdS1jL-defining

Session: ses_e482f226dffe78gK8cMHUWHVNw
Workspace: /home/lubko/soring-fronts/exec-root-adversary-counterstrategy-20261107
Created: 1794085281270; updated: 1794085331447

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b7d0e0450019r0q33AJVZM6Ar)

I’ll first inspect issue #48’s formulation and the cited evidence, then assess whether the one-ply invariant extends or admits a policy counterstrategy. I’ll keep this as a paper-level result and won’t edit the repository or post to the board.

## Output 83 (msg_1b7d13f23001JgYlihikUPPlNA)

The key quantifier issue is sharper than “some reachable state has \(F=7\)”: a policy can choose the root pair, and the adversary must force an obstruction along one outcome against that policy. I’m checking whether the proposed heavy-child property itself already fails at the antichain root, which would give the requested exact counterstrategy without relying on a finite-state enumeration.

## Output 113 (msg_1b7d1764f00177TEI8wpt0aNnC)

**The proposed “every root comparison has a heavy child” invariant cannot force \(B\) as a root obstruction.** There is an explicit sorter counterstrategy at the root: compare keys \(0\) and \(2\).

For \(B=(0,0,2,1,1,9,59)\), the exact values are \(e(B)=60\), \(F(B)=7\). That comparison splits the linear extensions \(3/57\), and its children have minimax values \(2\) and \(7\). The adversary can keep the hard child only by answering \(2<0\), reaching a state with \(F=7\). But the sorter can instead follow \(0<2\), reaching a state with \(F=2\). Thus \(B\) is hard **if presented as the current state**, but not an obstruction that an adversary can force against every policy from this state: the policy chooses the comparison and controls which branch it follows. The heavy-child condition is true for this root comparison, but its heavy child is precisely the branch the sorter can avoid.

This is consistent with the exact minimax recurrence
\[
F(B)=1+\min_{\{i,j\}}\max(F(B+i<j),F(B+j<i))=7.
\]
It certifies a seven-comparison continuation **after reaching \(B\)**; it does not certify that every root policy has a path reaching \(B\), or any specified obstruction. In particular, \(B\)’s \(F=7\) yields no stronger comparison bound for the antichain root by itself.

**Checked evidence:** the values and split above were recomputed from the repository’s exact minimax and extension-count routines. The cited Peczarski and Stober–Weiß evidence concerns exhaustive lower-bound searches and posets/layers in those searches; it does not establish the missing quantifier, namely a forced path from the antichain against every policy. The local evidence audit also cautions against reading Stober–Weiß’s searched efficiency window or stored-poset count as a characterization of all bottleneck states.

So I have an exact counterstrategy to this invariant route, not an all-\(n\) lemma or a sharper bound. A viable replacement would need a policy-quantified invariant—one that accounts for both outcomes of every policy-chosen comparison—not merely a hard reachable poset or a heavy child. No repository edits or board post were made.
