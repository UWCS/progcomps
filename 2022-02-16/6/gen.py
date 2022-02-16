from random import shuffle, randint, sample

def hours(mins: int):
    div, mod = divmod(mins, 60)
    return f"{div:02}:{mod:02}"

with open("stations.txt") as file:
    names = file.read().split("\n")

print(100)

with open("example.txt") as file:
    file.readline()
    print(file.read())

for t in range(3, 101):
    n = (t + 1) // 2
    m = 20 * n
    print(n, m)

    shuffle(names)

    used_names = names[:n]
    dist = 0
    for name in used_names:
        print(name, dist)
        dist += randint(20, 150)
    
    for i in range(m):
        a, b, = sample(used_names, 2)

        sec_a = randint(0, 1438)
        sec_b = randint(sec_a + 1, 1439)
        print(a, b, hours(sec_a), hours(sec_b))
    