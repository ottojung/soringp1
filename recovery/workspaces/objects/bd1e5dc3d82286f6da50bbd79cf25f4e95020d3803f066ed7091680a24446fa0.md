# The four-comparison extension threshold

**Claim.** For every finite poset `P`, if `e(P) <= 12`, then its exact
worst-case comparison sorting depth `F(P) <= 4`; this is sharp because a
six-element poset with `e(P)=13` has `F(P)=5`. Thus `T(4)=12`.

**Evidence status.** The reductions below are paper deductions from cited
results and proved structural lemmas. The connected residual is closed by a
finite exhaustive Python enumeration plus an independently written validator;
this is reproducible computational evidence, not a Lean proof. The enumeration
and validator are included in `scripts/t4_threshold/` and their output data in
`data/t4-threshold-candidates.json`. The publisher abstract for Kahn–Saks was
checked. The small-extension base `T(3)=7` is independently established by the
separate finite edge-subset audit `scripts/t4_threshold/audit_t3_base.py`, so
the argument below does not depend on the inaccessible Hanamura–Iwata text.

## Definitions and known inputs

`e(P)` is the number of linear extensions of `P`; `F(P)` is the minimum
worst-case number of adaptive pairwise comparisons needed to identify one.
Write `T(r)=max{E: e(P)<=E implies F(P)<=r for every finite P}`.

Inputs:

1. **[Literature] Kahn–Saks (1984),** *Balancing poset extensions*, Order
   1(2), 113–126, DOI 10.1007/BF00565647: every non-total finite poset with
   `e` extensions has an incomparable pair whose two orientation classes each
   have size between `3e/11` and `8e/11`.
2. **[Independent finite computation] `T(3)=7`.** For a connected
   incomparability graph, `q<=e-1<=6` and `q>=n-1`, so `n<=7`. The separate
   edge-subset audit enumerates every `q`-edge subset of a fixed natural
   extension for `2<=n<=7`, checks transitivity and connectedness, and exactly
   evaluates every retained `e<=7` poset. It finds 49 such connected
   representations, all with `F<=3`. Disconnected posets factor as ordinal
   sums: with total `e<=7`, multiple nontrivial factors can only have extension
   counts `2·2` or `2·3`; these sort in at most `2` or `3` comparisons,
   respectively. The witness `(0,0,1,3,7)` has `e=8,F=4`, proving sharpness.
   This is reproducible finite computational evidence, not a Lean proof.
3. **[Deduction, proved at #301, 2026-11-06 13:53Z]**
   `e(P) >= 1 + |E(Inc(P))|`. The graph of linear extensions under adjacent
   swaps of incomparable elements is connected. For each incomparable pair,
   take extensions with opposite orientations; a spanning tree of this graph
   must contain a swap edge labelled by that pair. Different pairs label
   different edges, so the number of incomparable pairs is at most `e(P)-1`.
4. **[Deduction]** If `P` has width `w`, then `e(P)>=w!`: choose a maximum
   antichain `A`; every ordering of `A` is acyclic when added to `P`, since no
   two elements of `A` are comparable in `P`, and therefore extends to a
   linear extension. These `w!` extensions are distinct.
5. **[Literature/deduction]** Under ordinal sum, `e(A⊕B)=e(A)e(B)` and
   `F(A⊕B)=F(A)+F(B)`. The latter exact identity is proved in
   `research-series-decomposition.md`.

## Upper bound for `e(P)<=12`

### At most ten extensions

For `8<=e<=10`, Kahn–Saks supplies a comparison with larger child at most
`(8/11)e <= 80/11 < 8`; since child sizes are integers, both children have at
most seven extensions. The independently checked `T(3)=7` base sorts each
child in at most three more comparisons, so `F(P)<=4`. For `e<=7`, the same
base gives `F(P)<=3`.

### Connected incomparability graph, `e=11` or `12`

If `Inc(P)` is connected on `n` vertices, it has at least `n-1` edges. The
spanning-tree inequality gives `n<=e(P)<=12`; it also gives
`|E(Inc(P))|<=e(P)-1<=11`. The width inequality gives width at most three,
because `4!>12`.

It remains a finite class. Every poset has a natural linear extension; index
its elements in that order. For each pair `i<j`, encode whether the pair is
incomparable. The transitivity condition on each newly added column is local:
if `i` is incomparable with the new `k` and `i<j<k` in the natural extension,
then `j` must also be incomparable with `k`. The recursive generator tries
every subset of earlier vertices satisfying exactly this condition, pruning
only when the incomparable-edge budget cannot be met. Thus it enumerates every
poset representation in this fixed-extension encoding (without isomorphism
deduplication).

For `n<=11`, it enumerates connected incomparability graphs with between
`n-1` and 11 edges and filters by `e in {11,12}` and width at most three. For
`n=12`, the edge bound forces exactly 11 edges, hence a tree; a separate
generator enumerates every such tree representation while rejecting cycles.
The one-shot `enumerate.py` run did not finish within the available execution
window: the n=2..11 fixed-extension stages completed, but the n=12 stage was
interrupted. To close that completeness gap, the separate targeted audit
`scripts/t4_threshold/audit_n12_pruned.py` independently enumerates the n=12
residual by maintaining exact linear extensions at each prefix and pruning
only when the extension count exceeds 12 (it cannot decrease when a new
element is added). It independently checks the natural-extension transitivity
rule and incomparability-graph acyclicity; with 12 vertices and 11 edges, every
retained graph is a connected tree. This targeted enumeration finds exactly
12 representations and matches the saved Q encodings and exact extension
sets, then recomputes minimax and gets `F(P)=4` for all 12. The full saved list
has 144 residual representations, all with exact `F(P)=4`. The independent
validator additionally checks every saved record: it reconstructs the
complete extension set by topological-order DFS (including duplicate-free set
equality with saved permutations), re-counts extensions by an ideal
recurrence, recomputes width and connectedness, and recomputes minimax from the
reconstructed extension subsets.
The saved output has counts by `n`: `4:6, 5:11, 6:82, 7:22, 11:11, 12:12`;
the independent validator reports all 144 have `F=4`.

### Disconnected incomparability graph

The unique ordinal-sum decomposition has connected incomparability factors.
Their extension counts multiply. For total `e=11`, primality means at most
one nontrivial factor, which is covered by the preceding connected case. For
total `e=12`, the multiplicative partitions of nontrivial factor counts are
`12`, `6·2`, `4·3`, and `3·2·2`. For factors with counts at most ten, the
previous Kahn–Saks argument gives depth at most four, and more precisely gives
depth at most three for counts at most seven and at most two for counts at
most four. A factor with count two has depth one. Therefore the four cases
have total depth bounded respectively by `4`, `3+1`, `2+2`, and `2+1+1`, all
at most four. This also covers extra singleton factors (extension count one,
depth zero).

## Sharpness

**[Experiment, independently rechecked]** The witness successor-mask tuple
`(20,16,0,23,0,22)` has `e=13` and exact minimax depth `F=5`. The project
probe in `scripts/obstruction_probe.py` and the independent exact recursion
both return these values. Hence `T(4)<=12`; the upper bound proves equality.

## Reproduction

From the repository root:

```sh
python3 scripts/t4_threshold/audit_t3_base.py
python3 scripts/t4_threshold/enumerate.py
python3 scripts/t4_threshold/audit_n12_pruned.py
python3 scripts/t4_threshold/independent_validate.py
```

The T(3) audit is a separate edge-subset enumeration. The `enumerate.py`
command regenerates the n<=11 portion and attempts the original n=12 tree
generator; that one-shot n=12 stage may be expensive. The targeted n=12 audit
provides an independent completeness check for that residual class.
`independent_validate.py` verifies every saved representation. These finite
computations do not replace the paper reductions above, nor does the theorem
imply an improved complexity bound for evaluating `S(n)` or `SORT-BOUND-U`.
