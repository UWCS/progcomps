from random import sample, randint

n_players = int(input())  # Max 1000
n_rounds = int(input())  # Max 10000

# Assign up to 1000 unique player names sourced from:
# Top 500 Male/Female 2004 baby names in the UK (ONS)
with open("names_1000.txt") as file:
    names = file.read().split("\n")
player_names = sample(names, n_players)
# print(player_names)

def generate_nums() -> list[list[int]]:
    round_info = []
    rounds_won = [0] * n_players
    for k in range(n_rounds):
        best_idx = randint(0, n_players - 1)
        rounds_won[best_idx] += 1
        best_num = randint(1, 100)
        round = [
            randint(0, best_num - 1) if i != best_idx 
            else best_num
            for i in range(n_players)
        ]
        round_info.append(round)
    
    # The data the player would recieve
    transpose = [
        [round_info[i][j] for i in range(n_rounds)]
        for j in range(n_players)
    ]

    m = max(rounds_won)
    tied = [
        idx for idx in range(n_players) if rounds_won[idx] == m
    ]

    if len(tied) == 1:
        return transpose

    # Regenerate data if the scores are tied.
    seen = {}
    for idx in tied:
        p_tot = 0
        for j in range(n_rounds):
            p_tot += round_info[j][idx]
        if p_tot not in seen:
            seen[p_tot] = True
        else:
            return generate_nums()
    return transpose

player_scores = generate_nums()

player_info = [
    [player_names[i]] + player_scores[i] for i in range(n_players)
]

# Write input data
#
print(n_players, n_rounds)
for i in range(n_players):
    print(*player_info[i])
# print(player_info)