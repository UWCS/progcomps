import sys
import os

sample_path_in = os.path.join(sys.argv[1], "input", sys.argv[2])

with open(sample_path_in) as file:
    file.readline()
    sample_in_lines = file.read().splitlines()

sample_path_out = os.path.join(sys.argv[1], "output", sys.argv[2])

with open(sample_path_out) as file:
    sample_out_lines = file.read().splitlines()

with open(sys.argv[3]) as file:
    output_lines = file.read().splitlines()

# Find all start and end indicies of the shortest substrings containing all of the letters "M", "I", "L" and "K"
def has_milk(string: str) -> list[tuple[int, int]]:
    return "M" in string and "I" in string and "L" in string and "K" in string

# Marking Style: Check validity of solution from input
# Alternatively, could pre-compute possible answers and check for any

max_score = len(sample_in_lines)
score = 0

for in_line, sample_out, out_line in zip(sample_in_lines, sample_out_lines, output_lines):

    x, y = [int(n) for n in sample_out.split()]
    try:
        a, b = [int(n) for n in out_line.split()]
    except ValueError:
        continue

    if b - a == y - x and has_milk(in_line[a:b+1]):
        score += 1

print(score, max_score)