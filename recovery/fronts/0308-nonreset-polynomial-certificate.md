# nonreset-polynomial-certificate

## status

investigated

## origin

ai_proposal_unverified

## agent_id

yIwmEYjz7dTe2xN87FD9NG-directors

## exit_state

clearexit

## question

Does there exist an all-n uniform polynomial-size (in N) certificate system for SORT-BOUND-U with a polynomial-time checker that is not equivalent to any framed/reset-DAG certificate, provably escaping the exact-reset divisibility obstructions on optimal paths?

## basis

reset-divisibility-certificate-blowup and reset-obstruction families investigated; framed DAG checker exists but completeness/class of all certifiers remains open.

## falsifier

Prove that every polynomial-time checkable, sound and complete certificate for SORT-BOUND-U induces a partition structure equivalent (up to polynomial blowup) to some reset/framed partitioning and is thus subject to the same divisibility obstructions, or construct an explicit non-reset polynomial certificate.

## implication

A true escape would be a substantive route to NP membership via a new certificate class; a general equivalence would show reset structure is canonical and obstructions are broad.

## finding_unverified

joins, but a general equivalence between arbitrary polynomial certificates and framed partition structures is not established; no explicit non-reset polynomial certificate is known. The question remains open.

**Mathematical finding (billy-dev only):**

**What I attacked:** The claim that some all-n uniform polynomial-size (in N) certificate system for `SORT-BOUND-U` exists that is not equivalent to any framed/reset-DAG certificate and provably escapes exact-reset divisibility obstructions on optimal paths. Tried to disprove it via canonicality (equivalence up to polynomial blowup) or to construct an escape.

**Distinctions (soundness vs completeness, general posets vs this model):**
- **Exact-reset ≠ forgetful framed.** The odd-`n` antichain→star obstruction (root split gives `n!/2` orders/branch, need integer multiples of `(n-1)!`) is correct for *exact* resets. The framed DAG grammar used by `scripts/check_framed_strategy.py` allows **intersection/forgetting** at joins (guaranteed poset can only weaken). It does *not* require exact partition into fixed `e(F')` classes. The known bubble/merge witnesses use forgetting, so the specific exact-reset obstruction is already escaped by the forgetful framed model.
- **General poset results don't transfer.** Hyafil–Rivest/Laber–Nogueira (arbitrary tests) and Parberry (fixed sorting networks/coNP) don't imply hardness for adaptive `S(n)`. Mahaney's sparsity barrier constrains many-one NP-hardness of unary `SORT-BOUND-U` (would imply P=NP) but doesn't rule out some other certificate class or membership in NP.

**Canonicality argument (attempted falsifier):**
For any **sound**, polynomial-time checkable certificate against a universal adversary with pairwise comparisons, to remain sound you cannot ignore which orders are still consistent - the strongest local guarantee is the intersection (guaranteed poset) of all consistent linear extensions along verified histories. Up to slot relabeling (frames) and polynomial encoding, the induced equivalence classes are poset-annotated states; the verification structure is naturally representable as a framed DAG (with joins = meet). This suggests **equivalence up to polynomial blowup** is canonical for sound systems. If true, divisibility/counting obstructions on poset-state partitions would be broad (apply to all sound polynomial certificates), not just exact resets.

**Status of falsifier:**
- **Escape construction:** No explicit non-reset polynomial certificate found. P/poly advice is non-uniform (different model from uniform polynomial-time checker/NP). Algebraic/invariant proofs I considered cannot remain sound against adaptive universal adversary without effectively reconstructing a strategy.
- **Equivalence proof:** No general proof of equivalence exists. The canonicality is plausible but not established; "partition structure induced by any sound verifier" needs formal argument (how much can a non-poset representation hide without losing local checkability/soundness?).

**Honest limits:** The exact-reset obstruction is escaped by forgetful framed joins. I cannot prove general equivalence, and I cannot construct an escape. The question remains open. No Lean files, tests, notes, or repo changes were made. The next decisive step would be either (1) a formal canonicality theorem showing any sound polynomial verifier induces poset-guarantee states up to poly blowup, or (2) an explicit sound complete non-poset polynomial certificate - neither was achieved.


## Other metadata

```json
{
  "finished_at": 1793859389.625484,
  "started_at": 1793859044.2184322
}
```
