# antonina-OZ9tTzL1c5H2Kb6A3Lk44V-records

Session: ses_e073ff044ffelFL2y5KgU0Q7Nx
Workspace: /home/lubko/soring-fronts/exec-root-forcing-l1-20261120
Created: 1795174698975; updated: 1795174754523

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 52 (msg_1f8c04387001HNW4NSDPDfRGig)

**[Paper proof]** The one-ply bound gives no improvement at the antichain root. For \(n\ge2\), every first comparison at the antichain splits its \(n!\) linear extensions evenly: each orientation fixes the relative order of one pair, leaving \(\binom n2\) choices of that pair’s positions and \((n-2)!\) orders of the other keys, hence \(n!/2\) extensions per child. Therefore
\[
L_1(A_n)=1+\left\lceil\log_2(n!/2)\right\rceil
=\left\lceil\log_2(n!)\right\rceil=L_0(A_n).
\]
The strict \(L_1>L_0\) witnesses at arbitrary posets consequently do not establish a stronger root bound.

The exact budgeted propagation is the game’s minimax recurrence, not a consequence of the local witness alone. Let \(B_h=\{P:L_1(P)>h\}\), a sound obstruction set since \(L_1(P)\le F(P)\). The states from which the adversary can force entry into \(B\) within \(r\) comparisons obey the attractor recurrence
\[
A_0=B,\qquad
A_{r+1}=B\cup\{P:\text{for every incomparable pair chosen by the sorter, some feasible child lies in }A_r\}.
\]
The quantifiers matter: the sorter chooses the pair first; only then may the adversary choose an outcome. A poset’s being reachable along *some* transcript establishes neither that it is in this attractor nor that the adversary can force it against every sorter policy. In particular, a bad reachable poset is not a forced state.

Backward propagation through this recurrence is sound, but proving that the antichain enters the attractor with a budget that beats \(\lceil\log_2(n!)\rceil\) is precisely the missing root-forcing theorem. At the root, the one-ply test itself cannot start such an improvement, as the equality above shows. No nontrivial all-\(n\) comparison lower bound or complexity-of-computing-\(S\) claim follows from this propagation alone.

## Output 70 (msg_1f8c0c7c7001ScqU1HzXKxz3Mn)

**[Literature]** Founder comment [#48, 6350140834](https://github.com/ottojung/soringp1/issues/48#issuecomment-6350140834) confirms Sergeev’s bound \(S(n)-\lceil\log_2(n!)\rceil=O(n/(\log n)^{1/5})=o(n)\). Thus any root-forcing argument yielding an \(\Omega(n)\) gap is ruled out. I make no such claim.

**[Precise obstruction]** A local one-ply witness \(P\) with \(L_1(P)>L_0(P)\) is only a sound bad state, not evidence that the adversary can force reaching it from the antichain. For a fixed budget, backward propagation requires that **for every pair chosen by the sorter**, the adversary has an outcome entering the prior attractor. The local witness supplies no such universal quantifier or root-to-witness budget. At the antichain, moreover, every first comparison splits extensions evenly, so \(L_1(A_n)=L_0(A_n)=\lceil\log_2(n!)\rceil\).

I found no proof of an unbounded sublinear root gap, nor a nontrivial uniform obstruction compatible with Sergeev’s upper bound. The remaining obstacle is a budgeted, all-sorter-policies forcing argument from the antichain—not reachability of locally bad posets. No claim about the complexity of computing \(S(n)\) follows.
