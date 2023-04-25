from random import choices, randint, choice

N_CASES = 50
L_BOUND = 30
U_BOUND = 80
STEP_FREQ = 1
UPPERCASE = "QWERTYUOPASDFGHJZXCVBN"
MILK = "MILK"

print(N_CASES)

for i in range(N_CASES):
    rand_letters = choices(UPPERCASE, k=randint(L_BOUND, U_BOUND))

    for _ in range(STEP_FREQ * (i // 5) + 4):
        rand_letters.insert(randint(0, len(rand_letters)), choice(MILK))

    for letter in MILK:
        if letter not in rand_letters:
            rand_letters.append(letter)

    # idxs = list(range(len(rand_letters)))
    # for i in sample(idxs, 4):



    print("".join(rand_letters))