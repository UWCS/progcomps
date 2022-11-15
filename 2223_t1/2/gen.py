from random import sample, randint, choice

n_tests = int(input())  # Max: 100
n_nums = int(input())  # Max: 30000
max_int = int(input())  # Max: 1000000

possible_nums = [x for x in range(1, max_int+1)]

print(n_tests)
for _ in range(n_tests):
    print(n_nums)

    pos_unique = sample(possible_nums, n_nums)
    if randint(1, 50) == 50:
        pos_unique[randint(0, n_nums-1)] = 0
    if randint(1, 5) == 5:
        idx1 = randint(0, n_nums-1)
        idx2 = randint(0, n_nums-1)
        pos_unique[idx1] = pos_unique[idx2]
    if randint(1, 2) == 2:
        idx1 = randint(0, n_nums-1)
        idx2 = randint(0, n_nums-1)
        pos_unique[idx1] = pos_unique[idx2]
    
    nums = [num * choice([-1, 1]) for num in pos_unique]
    print(*nums)
