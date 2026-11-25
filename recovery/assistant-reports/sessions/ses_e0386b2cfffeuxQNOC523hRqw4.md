# antonina-mwl35JghKJ1bfH4XfHHd2X-dinners

Session: ses_e0386b2cfffeuxQNOC523hRqw4
Workspace: /home/lubko/soring-fronts/effective-sergeev-finite-bound-20261121
Created: 1795237170542; updated: 1795237308624

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 222 (msg_1fc7b5cd80018xQ7aBadnC1DvQ)

Posted the result to Antonina issue #301 (author `SoringP1 researcher: effective-sergeev-finite-bound-20261121`).

Summary:
- Table n=12..22: exact S(n), C(n)=⌈log₂ n!⌉, gap is 0/1 only (1 at 12–19,22; 0 at 20,21).
- Candidate finite envelope (unproved, fitted): `S(n) ≤ C(n) + ⌈(1/8) n/(ln n)^{1/5}⌉`; gives slack 2 at n=12 and 3 at n=22, not tight.
- Falsification: n=12 gap=1 leaves no slack for a uniform `gap≤1` claim; n=22 stays at 1 but the envelope remains loose. Sergeev’s o(n) term is ~10–18 in this range, so it is asymptotic, not visible; Ford-Johnson already gives a sharper finite bound (gap 0/1/2 for n=12..25).
- Conclusion: no effective finite Sergeev bound narrows the small-n threshold window; no repo/Lean changes.
