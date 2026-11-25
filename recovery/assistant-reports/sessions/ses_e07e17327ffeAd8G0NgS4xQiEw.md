# antonina-AQeov5vTjHc4xGpFtTOGjC-empyema

Session: ses_e07e17327ffeAd8G0NgS4xQiEw
Workspace: /home/lubko/soring-fronts/greedy-value-multiplicity-per-extension-count-alln
Created: 1795164114357; updated: 1795165935095

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 506 (msg_1f83a0c98001mY4HMYo2DGwTIh)

Posted exactly one #301 report (no duplicates; this was the only external side effect taken).

- **Board:** Antonina issue #301, comment `sha256:35UPBSMrgpJnMIFsxgX3CZLoZMM9Rx8VzuAm_5mnOrY` (author `SoringP1 frontier: greedy-value-multiplicity-per-extension-count-alln`, 2026-11-20T09:11:51.978Z).
- **Claim attacked (all-n, falsifiable):** For all sufficiently large n, does a single linear-extension count e(P) support superpolynomially many distinct greedy max-extension values V(P) among states in the greedy ball B_{G(n)}(n)? (falsifier/implication as specified; barrier/compression scope only, no SORT-BOUND-U/S(n) separation claim.)
- **Definitions/solver (consistent with prior fronts, `/tmp/opencode/greedy_frontier.py`/`greedy_game.py`):** P = transitively closed strict poset (successor bitmasks), e(P)=#linear extensions (subset DP); greedy max-extension adversary with adversarial tie-break (larger-e child, ties maximize V); V(P)=0 if total else 1+min_pairs val(child); G(n)=V(A_n); B_{G(n)}(n)=states reachable from A_n in <=G(n) greedy transitions. Multiplicity per count = |{V(P): P∈B_{G(n)}(n), e(P)=c}|.
- **Search performed (finite, exact, unformalized scratch in `/tmp/opencode`):** exhaustive greedy-DAG BFS + bottom-up V for n<=6: n=2 (G=1,|B|=2,max mult 1), n=3 (3,11,1), n=4 (5,143,1), n=5 (7,3362,2 at e=8 → {3,4}), n=6 (10,119118,2, e.g. e=120/60/30/15/16). n=7: BFS reached 93,458 states (~34s) but full V/ball multiplicity did not complete within attempted time (runs timed out/killed); no complete n=7 figure. A chain-union partition probe was started but killed before output.
- **Partial finding / obstruction (not a theorem):** observed per-e multiplicity 1 (n<=4) and 2 (n=5,6) only—no support either way for superpolynomial growth in one e-fiber. Naive amplification fails algebraically: under ordinal sum V is additive and e multiplicative, so k independent copies of a fixed (e0,V0≠V1) collision with common padding give 2^k states at identical e but only k+1 distinct V values (linear-width range), not superpolynomially many pairwise-distinct V for one count. Opposite direction open (prior refutations of e, (e,h/profile), (e,width) as determining V do not imply/exclude a uniform poly(n) upper bound per e-fiber).
- **Honest limits:** **No theorem completion/proof/disproof** for all sufficiently large n; no all-n single-e superpolynomial construction and no polynomial per-e bound. n>=7 incomplete (performance). All finite values unformalized/not kernel-checked. Barrier/compression scope only (greedy V, greedy ball) — no S(n)/SORT-BOUND-U separation, no P/NP/PSPACE claim, no general-poset transfer, no unrestricted F result. No repo/Lean/test/CI/main/ledger changes. A decisive result would need either (a) one c_n with superpolynomially many P_i∈B_{G(n)}(n), same e, pairwise distinct V, with reachability/counting proved, or (b) a proved poly(n) bound on distinct V per e-fiber on B_{G(n)}(n).
