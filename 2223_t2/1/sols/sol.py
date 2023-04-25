# Find the start and end index of the shortest substring containing all of the letters "M", "I", "L" and "K"
def find_milk(string: str) -> tuple[int, int]:
    indices = (0, len(string) - 1)
    milk = {"M": -1, "I": -1, "L": -1, "K": -1}
    for i, c in enumerate(string):
        if c in milk:
            milk[c] = i
        if -1 not in milk.values():
            min_idx = min(milk.values())
            max_idx = max(milk.values())
            if max_idx - min_idx < indices[1] - indices[0]:
                indices = (min_idx, max_idx)
    return indices
    

n = int(input())
for _ in range(n):
    print(*find_milk(input()))