from random import *

N = randint(1, 100)
A = [randint(1, 10) for _ in range(N)]
print(N)
print(*A)