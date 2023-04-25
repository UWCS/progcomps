import sys
import os
from itertools import groupby

# Read in the input and output files 
input_path = os.path.join(sys.argv[1], "input", sys.argv[2])

with open(input_path) as file:
    file.readline()
    input_lines = file.read().splitlines()

with open(sys.argv[3]) as file:
    output_lines = file.read().splitlines()


def is_valid_block(n: int, k: int, blocked: list[tuple[int, int]]) -> bool:
    if k > n:
        return True

    # Horizontal
    blocked = sorted(blocked, key=lambda p: p[1])
    hori_groups = groupby(blocked, lambda p: p[1])

    # Check presence of necessary blocked lines
    if len(list(hori_groups)) != n:
        return False
    
    for _, v in hori_groups:
        hori = sorted(list(v), key=lambda p: p[0])
        if hori[0][0] > k or hori[-1][0] < n - k + 1:
            return False
        for i in range(len(hori)-2):
            if hori[i+1][0] - hori[i][0] > k:
                return False

    # Vertical
    blocked = sorted(blocked, key=lambda p: p[0])
    vert_groups = groupby(blocked, lambda p: p[0])

    # Check presence of necessary blocked lines
    if len(list(vert_groups)) != n:
        return False
    
    for _, v in vert_groups:
        vert = sorted(list(v), key=lambda p: p[1])
        if vert[0][1] > k or vert[-1][1] < n - k + 1:
            return False
        for i in range(len(vert)-2):
            if vert[i+1][1] - vert[i][1] > k:
                return False
            
    # Diag
    blocked = sorted(blocked, key=lambda p: p[1] - p[0])
    diag_groups = groupby(blocked, lambda p: p[1] - p[0])

    keys = set([k for k, _ in diag_groups])
    required = set([i for i in range(k - n, (n - k) + 1)])
    if len(required - keys) > 0:
        # print(required - keys)
        return False
    
    for _, v in diag_groups:
        diag = sorted(list(v), key=lambda p: p[0])
        if diag[0][0] > k and diag[0][1] > k or diag[-1][0] < n - k + 1 and diag[-1][1] < n - k + 1:
            return False
        for i in range(len(diag)-2):
            if diag[i+1][0] - diag[i][0] > k:
                return False

    # Anti-diag
    blocked = sorted(blocked, key=lambda p: p[0] + p[1])
    anti_groups = groupby(blocked, lambda p: p[0] + p[1])

    keys = set([k for k, _ in anti_groups])
    required = set([i for i in range(k + 1, (2 * n - k + 1) + 1)])
    if len(required - keys) != 0:
        # print(required - keys)
        return False

    for _, v in anti_groups:
        anti = sorted(list(v), key=lambda p: p[0])
        if anti[0][0] > k and anti[0][1] < n - k + 1 or anti[-1][0] < n - k + 1 and anti[-1][1] > k:
            return False
        for i in range(len(anti)-2):
            if anti[i+1][0] - anti[i][0] > k:
                return False
    
    return True

def get_score(n, k, b):
    subgrid = 2 * n * (n // k) - (n // k) * (n // k)
    # print(subgrid, "->", b, "( +", subgrid - b, ")")
    return subgrid - b

x_lines = output_lines[::2]
y_lines = output_lines[1::2]

score = 0
for input_line, x_line, y_line in zip(input_lines, x_lines, y_lines):
    n, k = [int(i) for i in input_line.split()]
    try:
        xs = [int(x) for x in x_line.split()]
        ys = [int(y) for y in y_line.split()]
    except ValueError:
        score -= 20
        continue
    coords = list(zip(xs, ys))
    if is_valid_block(n, k, coords):
        # print(n, k)
        score += get_score(n, k, len(coords))
    else:
        score -= 20

print(score)