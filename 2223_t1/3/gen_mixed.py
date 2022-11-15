from random import sample, choices, shuffle, choice, randint
from itertools import product

n_tests = int(input())
test_size = int(input())

# 100 text-based rules
with open("rules.txt") as file:
    rule_pool = file.read().split("\n")

possible_nums = [i+1 for i in range(test_size)]

# Mixed
print(n_tests)
for i in range(n_tests):
    print(test_size)
    
    pos_neg = [
        choice(["don't ", ""]) + s for s in choices(rule_pool, k=test_size)
    ]
    for j in range(test_size):
        if randint(1, 5) >= 4:
            idx1 = randint(1, len(pos_neg))
            idx2 = randint(1, len(pos_neg))
            pos_neg[idx1-1] = f"ignore rule {idx2}"
    [print(i+1, pos_neg[i]) for i in range(test_size)]



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