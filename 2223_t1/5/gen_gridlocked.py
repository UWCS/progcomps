from random import shuffle, randint

n_red, n_blue = 45000, 45000
print(n_red, n_blue)

flat = [i for i in range(90000)]
shuffle(flat)
bandits = []
for i in range(n_red + n_blue):
    x = flat[i] // 300
    y = flat[i] % 300
    r = 45 * randint(0, 3)
    bandits.append((x+1, y+1, r))
bandits = sorted(bandits)
[print(*bandit) for bandit in bandits]
