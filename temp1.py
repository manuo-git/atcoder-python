from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
from atcoder.fenwicktree import FenwickTree
from atcoder.segtree import SegTree
from atcoder.lazysegtree import LazySegTree
from atcoder.dsu import DSU
from atcoder.scc import SCCGraph
from atcoder.string import suffix_array
from itertools import permutations, combinations, product
from functools import cmp_to_key, cache
from more_itertools import distinct_permutations
from heapq import heappop, heappush
import math, sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**7)
_int = lambda x: int(x)-1
MOD = 998244353
INF = 1<<62
Yes, No = "Yes", "No"

N, M = map(int, input().split())
P = list(map(_int, input().split()))
mtk = [1]
for i in range(N): mtk.append(mtk[-1]*M%MOD)
cum = [0]
for i in range(N+1): cum.append(cum[-1]+mtk[i])

seen = [0]*N
li = []
mul = 1
for i in range(N):
    if seen[i]: continue
    seen[i] = 1
    st = i
    k = 1
    while P[i] != st:
        i = P[i]
        seen[i] = 1
        k += 1
    cnt = M*(M-1)//2*cum[k-1]
    cnt %= MOD
    li.append(cnt)
    mul *= (cnt+M)
    mul %= MOD
ans = 0
for cnt in li:
    print(cnt)
    ans += mul*pow(cnt+2, -1, MOD)*cnt%MOD
    ans %= MOD
print(ans)