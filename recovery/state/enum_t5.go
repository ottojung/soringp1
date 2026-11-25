package main

import (
	"fmt"
	"os"
	"strconv"
)

var LIM = 20
const NMAX = 20
var nodesByDepth [NMAX + 2]int64
var coreCountByE = map[int]int64{}
var maxMByE = map[int]int{}
type badRec struct{ e int; pred []int }
var bad []badRec
var totalCores int64
var calls int64

type key struct { s [20]uint32; n int }

func minimax(succ [20]uint32, n int, memo map[key]int) int {
	calls++
	k := key{n: n}
	for i := 0; i < n; i++ { k.s[i] = succ[i] }
	if v, ok := memo[k]; ok { return v }
	type pr struct{ i, j int }
	var inc []pr
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if (succ[i]>>uint(j))&1 == 0 && (succ[j]>>uint(i))&1 == 0 {
				inc = append(inc, pr{i, j})
			}
		}
	}
	if len(inc) == 0 { memo[k] = 0; return 0 }
	best := 1000
	for _, p := range inc {
		i, j := p.i, p.j
		var t, u [20]uint32
		for x := 0; x < n; x++ { t[x] = succ[x]; u[x] = succ[x] }
		dj := t[j] | (1 << uint(j))
		t[i] |= dj
		for x := 0; x < n; x++ { if x == i || (t[x]>>uint(i))&1 == 1 { t[x] |= dj } }
		a := minimax(t, n, memo)
		di := u[i] | (1 << uint(i))
		u[j] |= di
		for x := 0; x < n; x++ { if x == j || (u[x]>>uint(j))&1 == 1 { u[x] |= di } }
		b := minimax(u, n, memo)
		mx := a; if b > mx { mx = b }
		v := 1 + mx
		if v < best { best = v }
		if best == 1 { break }
	}
	memo[k] = best
	return best
}

func connectedInc(pred []int, k int) bool {
	seen := make([]bool, k)
	seen[0] = true
	st := []int{0}
	for len(st) > 0 {
		i := st[len(st)-1]; st = st[:len(st)-1]
		for j := 0; j < k; j++ {
			if !seen[j] && (pred[i]>>uint(j))&1 == 0 && (pred[j]>>uint(i))&1 == 0 {
				seen[j] = true; st = append(st, j)
			}
		}
	}
	for i := 0; i < k; i++ { if !seen[i] { return false } }
	return true
}

func dfs(k int, pred []int, ext [][]int) {
	nodesByDepth[k]++
	if k >= 1 && len(ext) <= LIM && connectedInc(pred, k) {
		e := len(ext)
		totalCores++
		coreCountByE[e]++
		var succ [20]uint32
		for i := 0; i < k; i++ { for j := 0; j < k; j++ { if (pred[i]>>uint(j))&1 == 1 { succ[j] |= 1 << uint(i) } } }
		memo := map[key]int{}
		m := minimax(succ, k, memo)
		if old, ok := maxMByE[e]; !ok || m > old { maxMByE[e] = m }
		if m > 5 && len(bad) < 30 { cp := append([]int(nil), pred...); bad = append(bad, badRec{e, cp}) }
	}
	if k == NMAX { return }
	var Ds []int
	var gen func(x, D int)
	gen = func(x, D int) {
		if x < 0 { Ds = append(Ds, D); return }
		if (D>>uint(x))&1 == 1 { gen(x-1, D); return }
		gen(x-1, D)
		gen(x-1, D|pred[x]|(1<<uint(x)))
	}
	gen(k-1, 0)
	for _, D := range Ds {
		var ne [][]int
		ok := true
		for _, w := range ext {
			maxpos := -1
			if D != 0 { for p := k - 1; p >= 0; p-- { if (D>>uint(w[p]))&1 == 1 { maxpos = p; break } } }
			for pos := maxpos + 1; pos <= k; pos++ {
				v := make([]int, len(w)+1)
				copy(v, w[:pos]); v[pos] = k; copy(v[pos+1:], w[pos:])
				ne = append(ne, v)
				if len(ne) > LIM { ok = false; break }
			}
			if !ok { break }
		}
		if ok { np := append(append([]int(nil), pred...), D); dfs(k+1, np, ne) }
	}
}

func main() {
	if len(os.Args) > 1 { LIM, _ = strconv.Atoi(os.Args[1]) }
	dfs(0, []int{}, [][]int{{}})
	fmt.Println("limit", LIM)
	fmt.Print("nodes by depth:")
	for i := 0; i <= NMAX; i++ { fmt.Printf(" %d:%d", i, nodesByDepth[i]) }
	fmt.Println()
	fmt.Println("total connected-core representations:", totalCores, "minimax calls:", calls)
	fmt.Println("counts by e:")
	for e := 0; e <= LIM; e++ { if c, ok := coreCountByE[e]; ok { fmt.Printf("  e=%d count=%d maxM=%d\n", e, c, maxMByE[e]) } }
	fmt.Println("bad (m>5):", len(bad))
	for _, b := range bad { fmt.Printf("  e=%d pred=%v\n", b.e, b.pred) }
}
