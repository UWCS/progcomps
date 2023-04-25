import sys
import os
import math

# Read in the input and output files 
input_path = os.path.join(sys.argv[1], "input", sys.argv[2])

with open(input_path) as file:
    file.readline()
    input_lines = file.read().splitlines()

with open(sys.argv[3]) as file:
    output_lines = file.read().splitlines()

# Get the final variable state after running a uwpl program
def parse_maybe_uwpl(script: list[str]) -> dict[str, int]:
    vars = {}
    stack = [1]
    curr = 0
    while curr < len(script):
        if script[curr] == "}":
            stack.pop()
            if len(stack) == 0:
                return {}
        elif script[curr].startswith("repeat "):
            try:
                rep = int(script[curr][7:])
            except ValueError:
                return {}
            stack.append(rep)
            curr += 1  # skip past opening {
            if script[curr] != "{":
                return {}
        elif script[curr][-2:] == "++":
            var_name = script[curr][:-2]
            if var_name not in vars:
                vars[var_name] = 0
            vars[var_name] += math.prod(stack)
            if vars[var_name] > 1_000_000:
                return {}
        else: # must be increment
            return {}
        curr += 1
    return vars

def get_score(num_vars, num_lines):
    return 4 * num_vars - num_lines

var_names = input_lines[1::3]
var_vals = input_lines[2::3]
# print(var_names)
# print(var_vals)


score = 0
idx = 0
for vn, vv in zip(var_names, var_vals):
    var_line_names = vn.split()
    var_line_vals = [int(i) for i in vv.split()]
    required_output = set(zip(var_line_names, var_line_vals))
    try:
        m = int(output_lines[idx])
    except ValueError:
        break
    idx += 1
    var_dict = parse_maybe_uwpl(output_lines[idx:idx+m])
    idx += m
    actual_output = set(zip(var_dict.keys(), var_dict.values()))
    if required_output != actual_output:
        score -= 20
        continue
    score += get_score(len(var_line_names), m)

print(score)