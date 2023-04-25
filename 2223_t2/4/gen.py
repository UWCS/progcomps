from random import choices, randint, choice
from string import ascii_lowercase

N_CASES = 100
BASE_VARS = 1000
VAR_STEP = 0
L_VARS = 1
U_VARS = 10000
# low vals, many vars

print(N_CASES)
for i in range(N_CASES):
    n_vars = BASE_VARS + i * VAR_STEP
    names = list(set(["".join(choices(ascii_lowercase, k=4)) for _ in range(n_vars)]))
    # vals = [2 ** randint(0, 19) + randint(0, 5) for _ in range(len(names))]
    # multi = randint(1, 100)
    vals = [randint(L_VARS, U_VARS) for _ in range(len(names))]
    print(len(names))
    print(*names)
    print(*vals)