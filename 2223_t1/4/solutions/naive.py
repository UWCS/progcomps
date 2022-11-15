from math import ceil, inf

class Clock:
    def __init__(self, time, drift_rate) -> None:
        self.t: int = time
        self.dr: int = drift_rate
    
    def __repr__(self) -> str:
        return f"Time: {self.t}, Drift Rate: {self.dr}"
    
    def simulate(self, ticks: int) -> int:
        return self.t + (self.dr * ticks)

t = int(input())

for _ in range(t):
    # Get data
    threshold, n = [int(x) for x in input().split()]
    clocks = []
    for i in range(n):
        clocks.append(Clock(*[int(x) for x in input().split()]))

    # Check that it's not already drifted
    lt_clock = min(clocks, key=lambda x: x.t)
    ht_clock = max(clocks, key=lambda x: x.t)
    if ht_clock.t - lt_clock.t > threshold:
        print(0)
        continue
    
    # Find max and min drift rates to get a bound, find lowest
    x = inf
    for i in range(len(clocks)):
        for j in range(i, len(clocks)):
            if clocks[i].dr == clocks[j].dr:
                continue
            if clocks[i].dr < clocks[j].dr:
                ldr_clock, hdr_clock = clocks[i], clocks[j]
            else:
                ldr_clock, hdr_clock = clocks[j], clocks[i]
            
            x = min(x, ceil((threshold - (hdr_clock.t - ldr_clock.t)) / abs(ldr_clock.dr - hdr_clock.dr)))

    print(x)
    