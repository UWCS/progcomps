from math import ceil

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
    
    # Find max and min drift rates to get a bound
    ldr_clock = min(clocks, key=lambda x: x.dr)
    hdr_clock = max(clocks, key=lambda x: x.dr)
    if ldr_clock.dr == hdr_clock.dr:
        print(-1)
        continue
    bound = ceil((threshold - (hdr_clock.t - ldr_clock.t)) / abs(ldr_clock.dr - hdr_clock.dr))

    # Simulate up until at most we reach the bound (worst when it's something like 9/10ths of the way or more)
    i = 0
    while i < bound:
        i += 1
        times = [c.simulate(i) for c in clocks]
        if max(times) - min(times) > threshold:
            print(i)
            break
    else:
        print(bound)
    