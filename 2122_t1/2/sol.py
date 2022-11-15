tests = int(input())

for _ in range(tests):
    x1, y1, x2, y2, ax, ay, bx, by = [int(s) for s in input().split()]
    blocked = [(ax, ay), (bx, by)]

    x_dist = abs(x1 - x2)
    y_dist = abs(y1 - y2)

    dist = abs(x1 - x2) + abs(y1 - y2) # taxicab distance

    if x_dist == 0:
        # If a or b in between shortest path
        if (ax == x1 and min(y1, y2) < ay < max(y1, y2)) or (bx == x1 and min(y1, y2) < by < max(y1, y2)):
            dist += 2  # add 2 to taxicab distance

    elif y_dist == 0:
        # If a or b in between shortest path
        if (ay == y1 and min(x1, x2) < ax < max(x1, x2)) or (by == y1 and min(x1, x2) < bx < max(x1, x2)):
            dist += 2  # add 2 to taxicab distance

    if x_dist >= 2 and y_dist >= 2:
        # only need to check adjacent tiles of start and end
        pass

    print(dist)

    
    