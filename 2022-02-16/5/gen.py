import random

i = 1

lines = []
for _ in range(30000):
    s = input().split()[0]
    if s.isalpha():
        lines.append(s.upper())

words = [w.upper() for w in lines]

print(1000)

for a in range(4, 14):
    x = list(filter(lambda s: len(s) == a, words))
    for b in range(4, 14):
        y = list(filter(lambda s: len(s) == b, words))
        for _ in range(10):
            w1 = random.choice(x)
            w2 = random.choice(y)
            print(w1, w2)