import random

limit = 2 * (10 ** 9)

print(10000)

# Example test cases
print(2, 4, 1, 5, 0, 3, 7, 10)
print(5, 0, 2, 1, 4)
print(2, 7, 3, 6, 0, 3, 4, 5)

# Permutations of [n]
for i in range(2497):
    nums = [j for j in range(random.randint(1, 4 * i + 5))]
    random.shuffle(nums)
    print(*nums)

# Permutations with added sinks
for i in range(2500):
    r_num = random.randint(1, 4 * i + 5)
    nums = [j for j in range(r_num)]
    random.shuffle(nums)

    # Create random sinks
    for _ in range(len(nums) // 16):
        idx = random.randint(0, r_num - 1)
        nums[idx] = random.randint(r_num, 4 * r_num)
    print(*nums)

# Allow duplicates, smaller size
for i in range(2500):
    r_num = random.randint(1, (i // 25) + 5)
    nums = [random.randint(0, r_num - 1) for _ in range(r_num)]
    print(*nums)

# Duplicates, smaller size, and sinks
for i in range(2500):
    r_num = random.randint(1, (i // 25) + 5)
    nums = [random.randint(0, r_num - 1) for _ in range(r_num)]

    # Create random sinks
    for _ in range(len(nums) // 10):
        idx = random.randint(0, r_num - 1)
        nums[idx] = random.randint(r_num, 4 * r_num)
    print(*nums)