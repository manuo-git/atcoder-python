from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
from atcoder.fenwicktree import FenwickTree
from atcoder.segtree import SegTree
from atcoder.lazysegtree import LazySegTree
from atcoder.dsu import DSU
from atcoder.scc import SCCGraph
from atcoder.string import suffix_array
from itertools import permutations, combinations
from functools import cmp_to_key, cache
from more_itertools import distinct_permutations
from heapq import heappop, heappush
_int = lambda x: int(x)-1
MOD = 998244353
INF = 1<<60
Yes, No = "Yes", "No"

N, Q = map(int, input().split())
l, r = 1, 2
ans = 0
for _ in range(Q):
    h, t = input().split()
    t = int(t)
    if h == "L":
        if l == t: continue
        a, b = l, t
        if a > b: a, b = b, a
        if a < r < b:
            ans += N+a-b
        else:
            ans += b-a
        l = t
    else:
        if r == t: continue
        a, b = r, t
        if a > b: a, b = b, a
        if a < l < b:
            ans += N+a-b
        else:
            ans += b-a
        r = t
print(ans)