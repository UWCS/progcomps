from random import sample, choices, shuffle, choice, randint
from itertools import product

n_tests = int(input()) #50
test_size = int(input()) #10000

# Strings of length 5 w/ no vowels, 21^5 > 10^5
letter_combs = list(product("qwrtypsdfghjklzxcvbnm", repeat=5))
rule_pool = ["".join(letters) for letters in letter_combs]

sample(rule_pool, test_size)

possible_nums = [i+1 for i in range(test_size)]

print(n_tests + 20)

# Ignoramus
for i in range(n_tests):
    print(test_size)
    
    non_ignore = [
        choice(["don't ", ""]) + s for s in sample(rule_pool, i * 10)
    ]
    unique_ignore = [
        f"ignore rule {s}" for s in sample(possible_nums, test_size // 2)
    ]
    random_ignore = [
        f"ignore rule {s}" for s in choices(possible_nums, k=test_size // 2)
    ]
    ignoramus = non_ignore + unique_ignore + random_ignore
    shuffle(ignoramus)
    [print(i+1, ignoramus[i]) for i in range(test_size)]

# Generate longest possible chain
for _ in range(10):
    print(test_size)
    shuffle(possible_nums)

    rules = [[possible_nums[0], "don't ignore me"]]
    for i in range(len(possible_nums)-1):
        rules.append([possible_nums[i+1], f"ignore rule {possible_nums[i]}"])
    
    # Randomly force an even or odd chain
    if randint(0, 1):
        rules[-1][1] = f"ignore rule {rules[-1][0]}"
    rules = sorted(rules)
    [print(*rule) for rule in rules]

# n/2 chain, n/2 singleton branches
for _ in range(10):
    print(test_size)
    shuffle(possible_nums)

    rules = [[possible_nums[0], "ignore me"]]
    halfway = len(possible_nums)//2 - 1
    for i in range(halfway):
        rules.append([possible_nums[i+1], f"ignore rule {possible_nums[i]}"])
    for i in range(halfway, len(possible_nums)- 1):
        rules.append([possible_nums[i+1], f"ignore rule {possible_nums[halfway]}"])
    
    # Randomly force the existence of an even chain
    if randint(0, 1):
        rules[-1][1] = f"ignore rule {rules[-2][0]}"
    rules = sorted(rules)
    [print(*rule) for rule in rules]
    


