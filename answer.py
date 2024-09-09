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
import math, sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**7)
_int = lambda x: int(x)-1
MOD = 998244353
INF = 1<<62
Yes, No = "Yes", "No"

