import random

S = 2
N = 100000
cnt = 0
for i in range(N):
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 2.0)
    if y <= x ** 3 + x ** 2:
        cnt = cnt + 1
result = cnt / N * S
print(result)
