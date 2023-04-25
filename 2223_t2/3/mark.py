import sys
import os

sample_path = os.path.join(sys.argv[1], "output", sys.argv[2])

with open(sample_path) as file:
    sample_lines = file.read().splitlines()

with open(sys.argv[3]) as file:
    output_lines = file.read().splitlines()

# Marking Style: Get the number of sample/output lines that match
# Variant: The answers can be in any order, but must be in pairs.

sample_xs = sample_lines[::2]
sample_ys = sample_lines[1::2]
output_xs = output_lines[::2]
output_ys = output_lines[1::2]

score = 0
max_score = len(sample_xs)

for sns, svs, ons, ovs in zip(sample_xs, sample_ys, output_xs, output_ys):
    sample_line_names = [int(i) for i in sns.split()]
    sample_line_vals = [int(i) for i in svs.split()]
    try:
        output_line_names = [int(i) for i in ons.split()]
        output_line_vals = [int(i) for i in ovs.split()]
    except ValueError:
        continue
    
    sample_vars = set(zip(sample_line_names, sample_line_vals))
    output_vars = set(zip(output_line_names, output_line_vals))
    if sample_vars == output_vars:
        score += 1

print(score, max_score)