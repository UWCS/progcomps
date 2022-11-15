#!/usr/bin/env python

t = int(input())  # Get number of test cases

for _ in range(t):
    # Get the two words
    w1, w2 = input().split()

    # Convert to sorted character arrays
    s1 = sorted(w1)
    s2 = sorted(w2)

    # Compare the arrays
    if s1 == s2:
        print("Yes")
    else:
        print("No")
