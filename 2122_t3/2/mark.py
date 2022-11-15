#!/usr/bin/env python3

from sys import stdin

def upper_bound(test_case):
    return 13 * max(len(test_case[0]), len(test_case[1]))

def letter_shifts(word):
    # All possible words resulting from a letter shift up or down
    shifts = []
    for i in range(len(word)):
        if ord(word[i]) > 65:
            l_down = chr(ord(word[i]) - 1)
        else:
            l_down = "Z"
        if ord(word[i]) < 90:
            l_up = chr(ord(word[i]) + 1)
        else:
            l_up = "A"
        shifts.append(word[:i] + l_down + word[i+1:])
        shifts.append(word[:i] + l_up + word[i+1:])
    return shifts

t = int(input())

test_cases = [input().split() for _ in range(t)]

sequences = [s.split() for s in stdin.read().split("\n")]

score = 0
n_valid = 0

for test_case, sequence in zip(test_cases, sequences):
    # Check that starting words match up
    if len(sequence) == 0 or sequence[0] != test_case[0] or sequence[-1] != test_case[1]:
        continue

    # Check that subsequent words follow on from each other
    for j, word in enumerate(sequence[:-1]):

        # Start with letter shifts
        possible = set(letter_shifts(word))
        # Add shift left/right
        possible.add(word[-1] + word[:-1])
        possible.add(word[1:] + word[0])
        # Add letter duplication and deletion
        possible.add(word[0] + word)
        possible.add(word[1:])

        if sequence[j+1] not in possible:
            break

    else:  # Never hit break statement
        n_valid += 1
        score += max(0, upper_bound(test_case) - len(sequence) + 1)

n_cases = len(test_cases)
# Apply score penalty
score -= 100 * (n_cases - n_valid)

print(n_cases, n_valid, score)