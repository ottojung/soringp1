# n32-power-of-two-increment

## status

investigated

## origin

manual_executive

## agent_id

DHyq36CCOOuMQO5XYTraOw-reckless

## exit_state

failed

## question

For n=32 (first power of two beyond known exact values through n=22), determine d(32)=S(32)-S(31) relative to ceil(log2 32)=5 - does the strict two-phase increment equal k for powers of two, or does optimal play beat S(2^k - 1)+k?

## basis

power-of-two-increment-exactness front was investigated but n=32 remains undecided (exact values not known through 32).

## falsifier

Establish either S(32) <= S(31)+4 (beating two-phase) with a constructive argument/certificate, or prove S(32)=S(31)+5 via a sound adversary lower bound, using known values where possible and credible bounds otherwise.

## implication

Resolves a concrete open endpoint of the two-phase/dyadic excess question with implications for the O(n) miss-mass structure.

## finding_unverified

Resolved on Antonina #301 (2026-10-30T01:46:17Z): for n=2^k, d(n)=S(n)-S(n-1)>=ceil(log2 n)=k (insertion lower bound, rank among n positions) and two-phase gives equality; hence d(32)=5, S(32)=S(31)+5.

## Other metadata

```json
{
  "finished_at": 1793323637.6809304,
  "started_at": 1793317539.4014623
}
```
