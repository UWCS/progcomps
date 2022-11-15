import sys
import os

sample_path_in = os.path.join(sys.argv[1], "input", sys.argv[2])
sample_path_out = os.path.join(sys.argv[1], "output", sys.argv[2])

with open(sample_path_in) as file:
    file.readline()
    sample_in_lines = file.read().splitlines()[1::2]

with open(sample_path_out) as file:
    sample_out_lines = file.read().splitlines()

with open(sys.argv[3]) as file:
    output_lines = file.read().splitlines()

# Marking Style: Check validity of solution from input

max_score = len(sample_out_lines)
score = 0

for in_line, sol_line, out_line in zip(sample_in_lines, sample_out_lines, output_lines):
    if sol_line == "Not Found":
        if out_line == "Not Found":
            score += 1
        continue

    s_nums = sol_line.split()
    if len(s_nums) != 2:
        continue

    # Do they actually exist in the original list?
    split = in_line.split()
    if s_nums[0] not in split or s_nums[1] not in split:
        continue
    # Same element twice?
    if s_nums[0] == s_nums[1] and len([i for i in s_nums if i == s_nums[0]]) < 2:
        continue
    
    try:
        a, b = [int(s_num) for s_num in s_nums]
    except ValueError:
        continue
    
    if a == 0 or b == 0 or a + b == 0 or a - b == 0:
        score += 1

print(score, max_score)