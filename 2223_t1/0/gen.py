from random import randint

print(100)
for i in range(100):
    rand_chrs = [chr(randint(97, 122)) for _ in range(100)]
    print("".join(rand_chrs))
