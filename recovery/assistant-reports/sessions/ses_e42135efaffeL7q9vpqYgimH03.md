# antonina-ubk3PekEmZkZU5VdfJuY1v-period

Session: ses_e42135efaffeL7q9vpqYgimH03
Workspace: /home/lubko/soring-fronts/information-theoretic-gap-unboundedness
Created: 1794187764078; updated: 1794187777409

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 45 (msg_1bdecb21b001DOKilGgeqRl2g6)

## Mathematical finding

**Status: OPEN — neither boundedness nor unboundedness of `E(n)=S(n)−⌈log₂ n!⌉` is established.**

What is known (literature):
- Information lower bound: `E(n) ≥ 0` for all `n`.
- Sergeev (ECCC TR20-096, Theorem 3): `S(n) = log₂(n!) + O(n/(log n)^(1/5))`, so `E(n)=o(n)` (sublinear upper bound).
- Exact values show `E(12)=1` (since `S(12)=30`, `⌈log₂ 12!⌉=29`), and other small `n` have `E=0` (e.g. `n≤11`, `n=20,21`). No infinite family with `E(n)` bounded by a constant is known; no infinite family with `E(n)→∞` is known.

Attempted attack: The only available handle on unboundedness would be a lower bound showing that some fixed bias/entropy deficit accumulates. Sergeev's construction shows the *upper* side can keep excess sublinear, but provides no matching lower bound. The entropy identity (`k−log₂(n!) = E[k−D] + Σ q_v(1−h₂(p_v))`) bounds expected bias in terms of excess, not conversely; it cannot force growth. Hyafil–Rivest/Laber–Nogueira results concern arbitrary decision trees/posets and do **not** reduce to the fixed family `S(n)` (per AGENTS.md model fidelity), so they yield no unboundedness theorem for `S(n)`.

Exact obstruction: There is no known technique to prove `E(n)→∞` for the adaptive comparison model; the gap between the information bound and the best sorting tree could in principle be `O(1)` or grow like `n/(log n)^{1/5}` or slower. Conversely, bounded excess would require a uniform near-information-optimal adaptive strategy for all `n`, which is not known.

Honest limit: The question remains a genuine open problem; this front produces no new theorem or counterexample. No repository/Lean changes are warranted.
