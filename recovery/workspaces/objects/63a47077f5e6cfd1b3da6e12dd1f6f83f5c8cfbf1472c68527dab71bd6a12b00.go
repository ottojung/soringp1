// Self-contained reproduction for T(5)=20.  Run: go run t5_threshold.go
package main

import (
	"fmt"
	"sort"
)

const LIMIT = 20
const NMAX = 20

type Ext struct {
	w [30][21]uint8
	e int
}

func extensions(n int, pred []uint32) Ext {
	var out Ext
	var rec func(done uint32, word [21]uint8, k int)
	rec = func(done uint32, word [21]uint8, k int) {
		if done == (1<<uint(n))-1 {
			for i := 0; i < n; i++ { out.w[out.e][i] = word[i] }
			out.e++
			return
		}
		for x := 0; x < n; x++ {
			if (done>>uint(x))&1 == 0 && pred[x]&^done == 0 {
				word[k] = uint8(x)
				rec(done|1<<uint(x), word, k+1)
			}
		}
	}
	rec(0, [21]uint8{}, 0)
	return out
}

func splitMasks(E *Ext, n int) []uint32 {
	e := E.e
	full := uint32((1 << uint(e)) - 1)
	set := map[uint32]bool{}
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			var mask uint32
			for r := 0; r < e; r++ {
				pi, pj := -1, -1
				for p := 0; p < n; p++ {
					if E.w[r][p] == uint8(i) { pi = p } else if E.w[r][p] == uint8(j) { pj = p }
				}
				if pi < pj { mask |= 1 << uint(r) }
			}
			if mask != 0 && mask != full { set[mask] = true }
		}
	}
	out := make([]uint32, 0, len(set))
	for a := range set { out = append(out, a) }
	sort.Slice(out, func(a, b int) bool { return out[a] < out[b] })
	return out
}

func minimax(E *Ext, n int) int {
	e := E.e
	if e <= 1 { return 0 }
	full := uint32((1 << uint(e)) - 1)
	splits := splitMasks(E, n)
	memo := map[uint32]int{}
	var f func(uint32) int
	f = func(S uint32) int {
		if S&(S-1) == 0 { return 0 }
		if v, ok := memo[S]; ok { return v }
		best := 999
		for _, a := range splits {
			x, y := S&a, S&^a
			if x == 0 || y == 0 { continue }
			v := 1 + max(f(x), f(y))
			if v < best { best = v; if best == 1 { break } }
		}
		memo[S] = best
		return best
	}
	return f(full)
}

func splitBothAtMost(E *Ext, n, lim int) bool {
	e := E.e
	for _, a := range splitMasks(E, n) {
		x := popcount(a)
		if x <= lim && e-x <= lim { return true }
	}
	return false
}

func popcount(x uint32) int {
	c := 0
	for x != 0 { x &= x - 1; c++ }
	return c
}

func connected(n int, pred []uint32) bool {
	seen := uint32(1)
	stack := []int{0}
	for len(stack) > 0 {
		i := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		for j := 0; j < n; j++ {
			if (seen>>uint(j))&1 == 0 &&
				(pred[i]>>uint(j))&1 == 0 && (pred[j]>>uint(i))&1 == 0 {
				seen |= 1 << uint(j)
				stack = append(stack, j)
			}
		}
	}
	return seen == (1<<uint(n))-1
}

var pred []uint32
var cur Ext

func main() {
	// Sharp witness: predecessor masks in a natural-extension labelling.
	W := []uint32{0, 0, 1, 3, 7, 15, 31}
	ex := extensions(7, W)
	fmt.Printf("Witness W pred=%v: e=%d m=%d\n", W, ex.e, minimax(&ex, 7))

	// Merge(2,6) from the brief.
	mergePred := func(a, b int) []uint32 {
		p := make([]uint32, 0, a+b)
		for x := 0; x < a+b; x++ {
			if x < a { p = append(p, (1<<uint(x))-1) } else { p = append(p, ((1<<uint(x-a))-1)<<uint(a)) }
		}
		return p
	}
	p26 := mergePred(2, 6)
	e26 := extensions(8, p26)
	fmt.Printf("Merge(2,6): e=%d m=%d\n", e26.e, minimax(&e26, 8))

	// Natural-extension DFS.  New labels are maximal; predecessors form an ideal.
	// e is nondecreasing, so pruning at e>20 is safe.  Connected cores satisfy n<=e.
	checked := [21]int{}
	fail := [21]int{}
	maxm := [21]int{}
	var visit func(int)
	cur.e = 1
	cur.w[0][0] = 0
	visit = func(k int) {
		e := cur.e
		if k >= 2 && e <= LIMIT && k <= e && connected(k, pred) {
			if e >= 18 {
				checked[e]++
				if !splitBothAtMost(&cur, k, 12) { fail[e]++ }
			}
			m := minimax(&cur, k)
			if m > maxm[e] { maxm[e] = m }
		}
		if k == NMAX { return }

		var ideals []uint32
		var gen func(int, uint32)
		gen = func(x int, D uint32) {
			if x < 0 { ideals = append(ideals, D); return }
			if (D>>uint(x))&1 != 0 { gen(x-1, D); return }
			gen(x-1, D)
			gen(x-1, D|pred[x]|(1<<uint(x)))
		}
		gen(k-1, 0)

		for _, D := range ideals {
			var ne Ext
			ne.e = 0
			ok := true
			for r := 0; r < cur.e; r++ {
				maxpos := -1
				if D != 0 {
					for p := k - 1; p >= 0; p-- {
						if (D>>uint(cur.w[r][p]))&1 != 0 { maxpos = p; break }
					}
				}
				for pos := maxpos + 1; pos <= k; pos++ {
					if ne.e >= LIMIT { ok = false; break }
					dst := &ne.w[ne.e]
					for p := 0; p < pos; p++ { dst[p] = cur.w[r][p] }
					dst[pos] = uint8(k)
					for p := pos; p < k; p++ { dst[p+1] = cur.w[r][p] }
					ne.e++
				}
				if !ok { break }
			}
			if !ok { continue }
			save := cur
			cur = ne
			pred = append(pred, D)
			visit(k + 1)
			pred = pred[:len(pred)-1]
			cur = save
		}
	}
	visit(0)

	for e := 18; e <= 20; e++ {
		fmt.Printf("e=%2d: connected cores n<=e checked=%d, lacking a <=12+<=12 split=%d\n", e, checked[e], fail[e])
	}
	fmt.Print("max exact m over connected cores by e (13..20): ")
	for e := 13; e <= 20; e++ { fmt.Printf("%d:%d ", e, maxm[e]) }
	fmt.Println()
}
