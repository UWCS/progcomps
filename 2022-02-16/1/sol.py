
def letter_dist(letter_a, letter_b):
    x = abs(ord(letter_a) - ord(letter_b))
    return 13 - abs(x - 13)

def word_dist(word_a: str, word_b: str):
    return sum(letter_dist(word_a[i], word_b[i]) for i in range(len(word_a)))

t = int(input())

for _ in range(t):
    start, end = input().split()
    # calculate distance between individual letters

    dists = []
    for i in range(len(start)):
        d = word_dist(start, end)

        # Add on penalty for shifting left/right
        if i < (len(start) + 1) // 2:
            d += i
        else:
            d += len(start) - i
        dists.append(d)

        # Shift starting word
        start = start[-1] + start[:-1]

    # print(dists)
    print(min(dists))