if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        variables = {}
        stack = []
        multiple = 1
        for _ in range(N):
            line = input()
            if line.endswith('++'):
                var = line.rstrip('++')
                if var not in variables:
                    variables[var] = 0
                variables[var] += multiple
            elif line.startswith('repeat'):
                mul = int(line.split(' ')[1])
                stack.append(mul)
                multiple *= mul
            elif line == '}':
                multiple //= stack[-1]
                stack.pop()
        vals = list(variables.items())
        print(*[key for key, _ in vals])
        print(*[val for _, val in vals])
