from random import sample, choices, choice
from itertools import product

n_tests = int(input())
test_size = int(input())

# Strings of length 4 w/ no vowels, 10^4
letter_combs = list(product("aeiouAEIOU", repeat=4))
rule_pool = ["".join(letters) for letters in letter_combs]

sample(rule_pool, test_size)

possible_nums = [i+1 for i in range(test_size)]

# Merge
print(n_tests)
for i in range(n_tests):
    print(test_size)
    
    to_merge = [
        choice(["don't ", ""]) + s for s in choices(rule_pool, k=test_size)
    ]
    [print(i+1, to_merge[i]) for i in range(test_size)]



# print(n_tests)
# for i in range(n_tests):
#     print(test_size)

#     random.shuffle(possible_rules)
#     for j in range(size_per_test):
        
#         rule = random.choice(possible_rules)
#         match random.randint(0, 2):
#             case 0:
#                 rule = "don't " + rule
#             case 1:
#                 rule = f"ignore rule {random.randint(1, size_per_test)}"
#         print(f"{j+1}. {rule}")