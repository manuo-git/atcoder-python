from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
from atcoder.segtree import SegTree
from atcoder.lazysegtree import LazySegTree
from atcoder.dsu import DSU
from atcoder.scc import SCCGraph
from itertools import permutations, combinations
from heapq import heappop, heappush
import math, sys
_int = lambda x: int(x)-1
MOD = 998244353
INF = 1<<62
Yes, No = "Yes", "No"

N, K = map(int, input().split())
S = input()
s = set()

ans = 0
for p in permutations(range(N)):
    st = "".join([S[p[i]] for i in range(N)])
    if st in s: continue
    s.add(st)
    ok = True
    for i in range(N-K+1):
        flag = False
        for j in range(K):
            if j == K-j-1: continue
            if st[i+j] == st[i+K-j-1]: flag = True
        if flag: ok = False
    if ok:
        ans += 1

print(len(s))
print(ans)
