// turner_s_n + is_terminal — Evens-type DP (documented interpretation of the spec):
//   W_k = {i in [0,N): s(i) <= k}; G(k) = (W_k ∩ [0,N), k);
//   is_terminal(W,N): W == [0,N).
// Operational game DP (documented interpretation of the spec):
//   terminal(W): W == FULL;
//   Evens move: choose pivot p ∉ W; W' = W ∪ [0..p]; k' = k + 1;
//   value V(W) = min k such that terminal reachable from (W, k).
//   turner_s_n(N, k_max) = V(∅).
function is_terminal(W, N) {
  const FULL = (1 << N) - 1;
  return W === FULL;
}
function turner_s_n(N, k_max) {
  const FULL = (1 << N) - 1;
  const V = new Map();
  function val(W) {
    if (W === FULL) return 0;
    if (V.has(W)) return V.get(W);
    let best = k_max + 1;
    for (let p = 0; p < N; p++) {
      if (!(W & (1 << p))) {
        const W2 = W | ((1 << (p + 1)) - 1);
        const v = 1 + val(W2);
        if (v < best) best = v;
      }
    }
    V.set(W, best);
    return best;
  }
  return val(0);
}
// Info-bound sanity values (LowerBound.lean: n! <= 2^S(n)):
function S_info(N) {
  let n = 1;
  for (let k = 2; k <= N; k++) n *= k;
  let s = 0;
  while (n > 1) { n = Math.ceil(n / 2); s++; }
  return s;
}
for (const N of [7, 10]) {
  console.log("turner_s_n(" + N + ", 26) =", turner_s_n(N, 26));
  console.log("is_terminal(FULL, " + N + ") =", is_terminal((1 << N) - 1, N));
  console.log("info-bound S(" + N + ") =", S_info(N));
}
