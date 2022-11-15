from random import randint

n_tests = 10000

print(n_tests)

for len in range(2, 10):
    for _ in range(1250):
        char_list = [chr(randint(48, 57)) for _ in range(len)]
        print(int("".join(char_list)))