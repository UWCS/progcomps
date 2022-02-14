import random

i = 1

lines = []
for _ in range(30000):
    s = input().split()[0]
    if s.isalpha():
        lines.append(s.upper())

words = [w.upper() for w in lines]

print(10000)

for k in range(4, 14):
    x = list(filter(lambda s: len(s) == k, words))
    for _ in range(1000):
        w1 = random.choice(x)
        w2 = random.choice(x)
        print(w1, w2)