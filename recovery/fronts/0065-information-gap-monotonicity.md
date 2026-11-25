# information-gap-monotonicity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ArIbirFfxqQaKRK0DGFuyf-caressed

## exit_state

clearexit

## question

Let g(n)=S(n)-⌈log2(n!)⌉ >= 0 be the information-theoretic gap. Is g(n) non-decreasing in n for all sufficiently large n, or does it drop below values at smaller n infinitely often despite Sergeev's o(n) asymptotics?

## basis

Known values show g(0..6)=0, g(11)=1, g(12)=1 (30-29); behavior between known points and asymptotics o(n) is uncharacterized; different from S(n) monotonicity which is kernel-checked.

## falsifier

Exhibit infinitely many n with g(n) < g(m) for all sufficiently large fixed m < n, using only known exact values plus a rigorous lower/upper bound argument (no unproven large-n enumeration), or disprove monotonicity with a concrete construction.

## implication

If g(n) were eventually strictly decreasing while o(n), that would be a strong structural constraint on how comparisons must be wasted; even if not giving a complexity class separation, it would constrain certificate density arguments and the shape of optimal strategies.

## finding_unverified

No final text; audit needed

## Other metadata

```json
{
  "finished_at": 1793374470.4668326,
  "started_at": 1793373800.066684
}
```
