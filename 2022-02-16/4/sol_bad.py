import numpy as np
from numpy import ndarray

char_map = {"X": -1, "O": 1, ".": 0}

def freq_diff(grid: ndarray):
    return sum(grid)

t = int(input())

for _ in range(t):
    n, k = [int(s) for s in input().split()]

    grid = [[char_map[x] for x in list(input())] for _ in range(n)]
    grid = np.array(grid)

    freq_diff = np.sum(grid)
    
    # Can't have 2 more of one symbol than another
    if abs(freq_diff) >= 2:
        print("!")
        continue

    print("?")
