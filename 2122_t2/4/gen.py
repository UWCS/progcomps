from random import choice, randint
from sys import stdin

n_examples = int(stdin.readline().strip())
print(1000)
print(stdin.read())

for i in range(n_examples, 1000):
    n = ((i + 5) // 20) + 1
    k = randint(1, n)

    print(n, k)

    flat_grid = ["."] * (n * n)
    
    times = randint(0, (n * k) // 2)
    for _ in range(times):
        r = randint(0, n * n - 1)
        flat_grid[r] = "X"
    for _ in range(times):
        r = randint(0, n * n - 1)
        flat_grid[r] = "O"

    flat_grid = "".join(flat_grid)
    grid = [flat_grid[j*n:(j+1)*n] for j in range(n)]
    for line in grid:
        print(line)