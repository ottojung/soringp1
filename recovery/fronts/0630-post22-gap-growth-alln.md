# post22-gap-growth-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

CbCNbrPSC2j0DG7V1XkgSX-sight

## exit_state

clearexit

## question

Define e(n) = S(n) - C(n). Prove or refute that e(n) <= 2 for all n >= 23, or exhibit a certified infinite ladder n_1 < n_2 < ... with e(n_i) >= i, i.e., the excess does not terminate.

## basis

Certified excess <= 1 through 22 (OEIS A036604 vs A003070); FJ-C = 3 at n = 28, 13 at n = 122 (board #301); Manacher 1979: FJ(n) > S(n) infinitely often; SW: S(28) >= 99, C(28)=98; Sergeev ECCC TR20-096: S(n) = log2(n!)+o(n).

## falsifier

A proof that e(n) <= 2 for all n >= 23 together with a certified n_i for every i with e(n_i) >= i, or a certified e(n) >= 3 for some n >= 23.

## implication

Bounded excess closes the 'excess ladder' route to certificate arithmetic; an infinite ladder gives a precise growth target for the gap between optimal counts and the information bound.

## finding_unverified

xists in certified data" and "Exact obstruction: a counterexample needs a certified lower bound above C(n)". My user front is e(n)≤2 for n≥23 — the falsifier needs certified e(n)≥3, i.e., S(28)≥101, i.e., FJA optimal at 28. Let me check the antonina board post interface.
Let me find the board issue ID for #301 to post my update.
## Finding: "e(n) ≤ 2 for all n ≥ 23" is **not refuted** within what I can certify; the precise obstacle is the unverified FJA-optimality-at-28 link.

### Certified data (verified by me, OEIS A036604 / A003070 / A001768)

- **e(n) = S(n) − C(n)**, C(n) = ⌈log₂ n!⌉. Certified excess ≤ 1 through 22: e=0 on {2..11,20,21}; e=1 on {12..19,22}.
- FJA(n) = A001768 (Ford-Johnson counts) — my formula reproduces the OEIS table exactly (n=1..56): FJA(28)=101, FJA(46)=195, FJA(47)=201, FJA(122)=688.
- C(n) = A003070 — verified: C(28)=98, C(46)=192, C(47)=198, C(122)=675.
- SW (board): S(28) ≥ 99 = C(28)+1 → **e(28) ≥ 1 (certified)**.
- FJA(28)=101, C(28)=98 → FJA−C = 3 at 28 → **e(28) ≤ 3 (upper bound; FJA is an algorithm, so S(28) ≤ FJA(28))**.

### Consequence for the claim

The claim e(n) ≤ 2 for all n ≥ 23 is refuted iff e(n) ≥ 3 for some n ≥ 23. The only candidates with a certified upper bound of 3 are n ∈ {28,29,30,31,32,33,34,35,46,47} (and FJA−C=13 at 122, but FJA is beaten at 47 per Manacher).

At n=28: **certified e(28) ∈ [1, 3]**. The claim e(28) ≤ 2 is consistent with all certified data. **No certified e(n) ≥ 3 found.**

### The would-be falsifier, and its certificate-soundness gap

The natural falsifier is **e(28) = 3**, certified if FJA is optimal at 28 (S(28)=FJA(28)=101):

- Literature: Manacher 1979, "The Ford-Johnson sorting algorithm is not optimal", JACM 26(3):441-456 — FJA beaten at infinitely many t. Board #301 records: "first at 47 (S(47) ∈ {198,199,200})" — i.e., FJA optimal at n ≤ 46 → S(28)=FJA(28)=101 → e(28)=3.
- Peczarski 2007, IPL 101(3):126-128: FJA+merge variants not beaten for n<47 (weaker — restricted to FJA-based algorithms).

**Exact obstruction (certificate soundness vs completeness):** FJA−C=3 at 28 is a sound certificate of the *upper* bound e(28) ≤ 3, but it does not certify the *lower* bound e(28) ≥ 3 needed for refutation. The lower bound S(28) ≥ 101 = FJA(28) requires FJA optimality at 28 — the Manacher beat-set minimum must be ≥ 28. I could not verify the Manacher paper text (dl.acm.org bot-blocked, sci-hub altcha, Semantic Scholar 429, DeepDyve 403). The DDG abstract gives the beat set as bands [u_k, u_k+l−1], u_k=⌊(4/3)2^k⌋, but not the minimum. So the "first at 47" claim — and hence the soundness of certifying e(28) ≥ 3 — is an unverified link. Per the user's instruction, this is the precise obstruction: **certifying e(28) ≥ 3 needs a verified FJA-optimality-at-28 or another certified S(28) ≥ 101**, neither of which I have.

### Honest limits

- No certified e(n) ≥ 3 found; no certified ladder exhibited.
- The prior front (excess-at-most-one-alln, board #301) records "no certified S(n) ≥ C(n)+2 exists in certified data; max certified excess is 1" — consistent with S(28) ≤ 100; my verification could not settle whether S(28) is 99, 100, or 101. The two researchers' views on FJA optimality at 28 differ; my verification could not resolve it.
- No repo/Lean changes made (no new independently checkable theorem or counterexample). Worktree remains clean on billy-dev.
- Posted the finding/obstruction to board issue #301 (author: "SoringP1 researcher: exec-excess-at-most-two-20261121").

## Other metadata

```json
{
  "finished_at": 1795232592.609548,
  "started_at": 1795231175.1983316
}
```
