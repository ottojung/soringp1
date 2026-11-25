# antonina-G6kXbWEkts11Q1dK3zID70-scrape

Session: ses_e48269d7cffeGjbQdLjx0YCBPp
Workspace: /home/lubko/soring-fronts/exec-adversary-certificate-format-20261107
Created: 1794085839596; updated: 1794085866008

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 47 (msg_1b7d9825b0011wkjhtC3zRpthW)

The proposed recurrence gives a sound certificate system for `S(n)>k`, but polynomial-time checking does **not** establish that every no-instance has a polynomial-size certificate. I found no proof that these certificates are polynomially bounded; coNP membership therefore remains open.

Let `F(P)` be the minimum worst-case number of further comparisons needed from transitively closed poset `P`. Use the recurrence
\[
F(P)=0\quad(P\text{ total}),\qquad
F(P)=1+\min_{\{x,y\}\text{ incomparable}}\max(F(P_{xy}),F(P_{yx}))
\]
otherwise, where each child is the transitive closure after adding the indicated orientation. A certificate for `F(P)>h` should exhibit, for **every** incomparable pair, a chosen feasible orientation whose child has value greater than `h−1`. Starting at the antichain with `h=k`, this is precisely the adversary’s existential response after each sorter query.

A concrete certificate grammar is a rooted DAG of records `(P,h)`:

- **State:** `P` is an `n×n` relation matrix. The checker verifies irreflexivity, transitivity, and that its entries encode exactly the stated relation.
- **Budget:** `h` is an integer from `0` to `k`, encoded in binary.
- **Coverage:** For every unordered incomparable pair `{x,y}` in `P`, there is exactly one record edge naming that pair and choosing one feasible orientation, `x<y` or `y<x`.
- **Child:** The edge names a child record `(Q,h−1)`. The checker computes the oriented transitive closure `P′`; it must be consistent, and `Q` must equal `P′` up to the child’s specified relabelling frame.
- **Frame/canonicalization:** A frame is an explicit permutation of the `n` labels. The checker verifies that applying it to `P′` gives the child’s stored `Q`. For canonical sharing, a state may instead store a canonical representative plus a permutation witness; canonicality and the witness must be checked. Sharing records is valid only when the represented `(P,h)` states agree under that checked relabelling.
- **Base cases:** A non-total state at `h=0` is a losing leaf and needs no query edges. A total state is *not* losing and cannot appear as a losing record, at any `h`. Reject inconsistent or cyclic records; along every edge `h` decreases.

The root must represent the `n`-element antichain at budget `k`. These checks take polynomial time in the **explicit certificate length** and in `n`. Soundness follows by induction on `h`: each possible sorter query has a certified adversarial orientation to a child that remains losing, so no strategy can finish within the budget. Conversely, if `F(P)>h`, the recurrence supplies a losing orientation for every legal query; recursively expanding these choices yields a finite certificate. This proves completeness as an unrestricted certificate system, not polynomial-size completeness.

The unresolved issue is size. A record can store its relation in `O(n²)` bits, and each query edge and permutation frame costs polynomially many bits. But the recursive expansion can have exponentially many records, and the specification gives no bound on DAG sharing. Quotienting by isomorphism does not by itself prove a polynomial bound. Thus this establishes verifier soundness and unrestricted existence—not coNP membership.

The obvious exact-value falsification is `n=12`: `S(12)=30`, so at `k=29` the recurrence must have a losing adversary certificate; at `k=30` it must not. For `n≤11`, the known equality `S(n)=⌈log₂ n!⌉` similarly puts the first losing threshold at one below that value. These checks validate the quantifiers and off-by-one base case, but cannot establish an all-`n` size bound. The literature notes report exhaustive searches for exact values through `n=22` and `S(28)≥99`; those computations are not evidence of polynomial-size certificates.

I could not inspect the GitHub issue bodies for #47/#48 from the local repository: the notes link to them but do not reproduce their full discussion. The local notes do confirm the essential distinction: a hard reachable poset is not by itself an adversarial lower bound from the antichain root; the root certificate must cover every sorter query. No code, Lean, board post, or class-separation claim was made.
