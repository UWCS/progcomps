from random import randint

print(5000)

print(1, 9)
print(1, 100)
print(4, 13)
print(0, 100)
print(1000, 0)

for i in range(5000, 9995):
    print(randint(0, (i // 10) + 5), randint(0, (i // 100) + 5))