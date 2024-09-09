from random import randint

H, W = 5, 5
N = randint(5, 10)
print(H, W, N)
for _ in range(N):
    print(randint(1, H), randint(1, W))
