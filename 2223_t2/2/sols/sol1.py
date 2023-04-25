import math

# Get the final variable state after running a uwpl program
def parse_uwpl(script: list[str]) -> dict[str, int]:
    vars = {}
    stack = [1]
    curr = 0
    while curr < len(script):
        if script[curr] == "}":
            stack.pop()
        elif script[curr].startswith("repeat "):
            rep = int(script[curr][7:])
            stack.append(rep)
            curr += 1  # skip past opening {
        else: # must be increment
            var_name = script[curr][:-2]
            if var_name not in vars:
                vars[var_name] = 0
            vars[var_name] += math.prod(stack)
        curr += 1
    return vars


n = int(input())
for _ in range(n):
    l = int(input())
    var_dict = parse_uwpl([input() for _ in range(l)])
    print(*var_dict.keys())
    print(*var_dict.values())