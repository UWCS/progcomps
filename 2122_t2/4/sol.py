import numpy as np
from numpy import ndarray

char_map = {"X": -1, "O": 1, ".": 0}

def freq_diff(grid: ndarray):
    return sum(grid)

def find_chains(grid: ndarray, n: int, k: int):
    # Horizontal and Vertical
    x_chains = []
    o_chains = []
    for i in range(n):
        for j in range(n-k+1):
            # Horizontal
            slice = grid[i, j:j+k]
            slice_sum = sum(slice)
            slice_coords = [(i, b) for b in range(j, j+k)]
            if slice_sum == k:
                o_chains.append(slice_coords)
            elif slice_sum == -k:
                x_chains.append(slice_coords)

            # Vertical
            slice = grid[j:j+k, i]
            slice_sum = sum(slice)
            slice_coords = [(a, i) for a in range(j, j+k)]
            if slice_sum == k:
                o_chains.append(slice_coords)
            elif slice_sum == -k:
                x_chains.append(slice_coords)
    
    # Diagonal chains
    diff = n - k
    for i in range(-diff, diff+1):
        diag = np.diag(grid, i)
        antidiag = np.diag(np.flipud(grid), i)

        start_r = max(0, -i)
        start_c = max(0, i)

        for j in range(n - abs(i) - k + 1):
            slice = diag[j:j+k]
            slice_sum = sum(slice)
            slice_coords = [(start_r + a, start_c + a) for a in range(j, j+k)]
            if slice_sum == k:
                o_chains.append(slice_coords)
            elif slice_sum == -k:
                x_chains.append(slice_coords)
            
            slice = antidiag[j:j+k]
            slice_sum = sum(slice)
            slice_coords = [(n - 1 - start_r - a, start_c + a) for a in range(j, j+k)]
            if slice_sum == k:
                o_chains.append(slice_coords)
            elif slice_sum == -k:
                x_chains.append(slice_coords)

    return x_chains, o_chains


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

    x_chains, o_chains = find_chains(grid, n, k)
    if x_chains and o_chains:
        print("!")
        continue

    if not x_chains and not o_chains:
        if freq_diff == 1:
            print("O")
        elif freq_diff == -1:
            print("X")
        else:
            print("?")
        continue
    
    # Detect if there is a single, shared chain
    
    shared_chain = set.intersection(*map(set, x_chains + o_chains))
    if shared_chain:
        if (x_chains and freq_diff == -1) or (o_chains and freq_diff == 0):
            print("X")
        elif (o_chains and freq_diff == 1) or (x_chains and freq_diff == 0):
            print("O")
        else:
            print("!")
    else:
        print("!")
