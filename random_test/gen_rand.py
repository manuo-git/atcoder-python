from random import *

# print(randint(1, 1000000))
Q = randint(1, 1000)
print(Q)
S = set()
M = (1<<30)-1
# M = 10

for _ in range(Q):
    if len(S) > 0:
        op = randint(0, 2)
    else:
        op = 0
    if op == 0:
        x = randint(0, M)
        S.add(x)
        print(op, x)
    elif op == 1:
        x = randint(0, M)
        S.discard(x)
        print(op, x)
    else:
        n = len(S)
        x = randint(0, M)
        print(op, randint(0, n-1), x)
