p, r = [int(i) for i in input().split()]

# Extract both the names and player scores
names = []
player_scores = []
for _ in range(p):
    line = input().split()
    names.append(line[0])
    player_scores.append([int(i) for i in line[1:]])

# Transpose the player scores into individual round results
round_results = [[player_scores[i][j] for i in range(p)] for j in range(r)]

# Calculate the number of rounds each player won
rounds_won = [0] * p
for round in round_results:
    idx = round.index(max(round))
    rounds_won[idx] += 1

# Find the indices of the players who tied, if any
m = max(rounds_won)
win_candidates = [idx for idx in range(p) if rounds_won[idx] == m]

if len(win_candidates) == 1:
    print(names[win_candidates[0]])
else:
    # Find name of player with highest total (who tied for round wins)
    win_cand_scores = [sum(player_scores[idx]) for idx in win_candidates]
    idx = win_cand_scores.index(max(win_cand_scores))
    name_idx = win_candidates[idx]
    print(names[name_idx])