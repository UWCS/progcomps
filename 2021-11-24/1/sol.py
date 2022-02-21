t = int(input())

for _ in range(t):
    n = int(input())

    persistence = 0
    while n >= 10:
        n = sum([int(k) for k in str(n)])
        persistence += 1

    print(persistence)