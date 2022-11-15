from math import ceil

class Clock:
    def __init__(self, time, drift_rate) -> None:
        self.t: int = time
        self.dr: int = drift_rate
    
    def simulate(self, ticks: int) -> int:
        return self.t + (self.dr * ticks)

# Binary search for where we first satisfy the condition
def find_boundary(clocks, threshold, lower, upper):
    # Base case
    if lower == upper:
        return upper
    
    # Check if synchronised at midpoint time
    mid = (lower + upper) // 2
    lt_clock = min(clocks, key=lambda x: x.simulate(mid))
    ht_clock = max(clocks, key=lambda x: x.simulate(mid))

    # Adjust boundaries 
    if ht_clock.simulate(mid) - lt_clock.simulate(mid) > threshold:
        upper = mid
    else:
        lower = mid + 1
    
    # Recursive step
    return find_boundary(clocks, threshold, lower, upper)

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

    print(find_boundary(clocks, threshold, 1, bound))
    