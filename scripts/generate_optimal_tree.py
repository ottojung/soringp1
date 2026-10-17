import itertools, sys
from functools import lru_cache

def perms(n): return list(itertools.permutations(range(n)))
def sorted_positions(r): return tuple(sorted(range(len(r)), key=lambda p: r[p]))

def solve(n):
    allp = perms(n)
    @lru_cache(maxsize=None)
    def best(state):
        if len(state) <= 1: return (0, ('leaf', next(iter(state))))
        bestv = None
        for i in range(n):
            for j in range(n):
                if i == j: continue
                yes = frozenset(p for p in state if p[i] < p[j])
                no  = frozenset(p for p in state if p[i] > p[j])
                if not yes or not no: continue
                dy, ty = best(yes); dn, tn = best(no)
                v = 1 + max(dy, dn)
                if bestv is None or v < bestv[0]:
                    bestv = (v, ('node', i, j, ty, tn))
        return bestv
    return best(frozenset(allp))

def swap_expr(l, n):
    tau = list(range(n)); swaps = []
    for i in range(n):
        target = l[i]
        j = tau.index(target)
        if j != i:
            swaps.append((i, j)); tau[i], tau[j] = tau[j], tau[i]
    if not swaps: return f"(Equiv.refl (Fin {n}))"
    expr = f"(Equiv.swap {swaps[0][0]} {swaps[0][1]})"
    for (a, b) in swaps[1:]:
        expr = f"((Equiv.swap {a} {b}).trans {expr})"
    return expr

def emit(tree, n, ind):
    pad = '  ' * ind
    if tree[0] == 'leaf':
        return f"{pad}(.leaf {swap_expr(sorted_positions(tree[1]), n)})"
    _, i, j, yes, no = tree
    return (f"{pad}(.compare {i} {j}\n" + emit(yes, n, ind+1) + "\n" + emit(no, n, ind+1) + ")")

if __name__ == '__main__':
    n = int(sys.argv[1])
    depth, tree = solve(n)
    print(f"-- n={n} depth={depth}", file=sys.stderr)
    print(emit(tree, n, 1))
