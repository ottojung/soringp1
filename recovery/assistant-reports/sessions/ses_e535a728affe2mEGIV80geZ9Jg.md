# antonina-LIfxI2NbPhOhspveG2YkKL-pinkish

Session: ses_e535a728affe2mEGIV80geZ9Jg
Workspace: /home/lubko/soring-fronts/audit-fj-framed-certificate-20261105
Created: 1793897893336; updated: 1793897936582

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 69 (msg_1aca604b40013Zew5TwTUB2NMD)

## Result for issue #301

**The proposed rank-envelope argument does not establish a framed DAG at the Ford–Johnson bound.** I found no minimal counterexample to the underlying sorter or its comparison bound; the gap is a specific unproved join invariant. The all-\(n\) certificate construction therefore remains unresolved.

**Checker semantics:** `scripts/check_framed_strategy.py` propagates a guaranteed strict partial order, adds the queried outcome, takes transitive closure, renames slots by the edge’s full permutation, and intersects guarantees at joins. A frame may rename slots, but cannot restore facts lost at a join. A terminal is accepted only if its incoming guarantee orders every pair.

**Invariant needed:** At every recursive stage, each feasible history reaching a shared node must, after its full-slot frame, imply one common partial order sufficient to:
1. keep the recursively sorted winner chain ordered;
2. preserve each loser’s association with its winner slot and certify loser \(b_i<a_i\);
3. certify the odd unpaired element’s insertion range; and
4. after each insertion and join, retain the relaxed windows needed for the *next scheduled* insertion.

The note asserts that winner frames can carry associated loser slots and that the paired winner’s rank is at most \(i+t\). But it does not give the recursive full-slot permutations or prove that these facts survive intersection across histories. In particular, “the old endpoint shifts by at most \(t\)” alone does not establish the stated common window: it must identify the endpoint’s current slot/order guarantee after the insertion permutation and show every joined incoming relation entails that same window. Nor does the note derive that the resulting stage widths, including the odd full-range insertion, sum to \(F_{\rm FJ}(n)\) on every branch. The checker’s longest-path budget requires precisely that worst-branch accounting.

Thus the missing lemma is: **for every recursive winner-sorting history and every insertion outcome, explicit frames make all incoming guarantees at each shared node imply the same next-stage winner/loser association and rank envelopes, while every root-to-leaf path costs at most \(F_{\rm FJ}(n)\).** Without that proof (or a counterexample to a proposed explicit frame), it would be unjustified to claim the construction.

This concerns a certificate for the **Ford–Johnson upper bound only**. Even a sound polynomial-size certificate at \(F_{\rm FJ}(n)\) would not imply optimal-size completeness or NP membership for `SORT-BOUND-U`.

Evidence: the checker and frontier note in `/home/lubko/soring301`; the note itself labels the exact embedding and recursive frame/odd-case review as pending. I stopped at that gap rather than extrapolating. No repository files were edited and no finite example is offered as all-\(n\) evidence.
