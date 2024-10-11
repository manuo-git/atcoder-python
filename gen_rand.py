from random import randint

N, X = randint(1, 10), randint(1, 1000)
print(N, X)
for _ in range(N):
    a = randint(1, 100)
    b = randint(1, 100)
    p = randint(1, 100)
    q = randint(1, 100)
    print(a, p, b, q)