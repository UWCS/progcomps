#!/usr/bin/env python3

from sys import stdin

def to_mins(hour_minute):
    return int(hour_minute[:2]) * 60 + int(hour_minute[-2:])

t = int(input())

journeys_groups = []

for _ in range(t):
    n, m = [int(s) for s in input().split()]
    
    stations = [input().split() for _ in range(n)]
    stations = {a: int(b) for a, b in stations}

    journeys = [input().split() for _ in range(m)]

    # Clean journey data
    journeys = [((stations[p1], to_mins(t1)), (stations[p2], to_mins(t2))) for p1, p2, t1, t2 in journeys]
    
    journeys_groups.append(journeys)

for i in range(t):
    allowed = [int(s) for s in input().split()]
    print(allowed)

    journeys = journeys_groups[i]
    print(journeys)