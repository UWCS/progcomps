from random import randint

N_CASES = 100
MIN = 1
MAX = 10000
MULTI_MIN = 1
MULTI_MAX = 1

print(N_CASES)
for i in range(N_CASES):
    scaling = randint(MULTI_MIN, MULTI_MAX)
    coords = [
        (
        scaling * randint(MIN, MAX), 
        scaling * randint(MIN, MAX)
        ) 
        for _ in range(30000)
        ]
    x, y = zip(*coords)
    print(len(x))
    print(*x)
    print(*y)