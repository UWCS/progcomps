from random import randint, normalvariate
from sys import argv

# Set dataset parameters
match (argv[1] if len(argv) > 1 else ""):
    case "a":
        n_tests, size_per_test = 100, 20
        damp_time, damp_rate = 1.5, 150
        thresh = 5000
    case "b":
        n_tests, size_per_test = 10, 10000
        damp_time, damp_rate = 5, 5000
        thresh = 100000
    case "c":
        n_tests, size_per_test = 1, 1000000
        damp_time, damp_rate = 10, 300000
        thresh = 36000000
    case _:
        exit()

def clamp(num: int, low: int, high: int):
    return min(high, max(low, num))

print(n_tests)
for _ in range(n_tests):
    print(thresh, size_per_test)
    center = randint(thresh, 4 * thresh)

    clocks = []
    for _ in range(size_per_test):

        std_time = thresh / (3 * damp_time) # 99.7% within 3 SD of mean
        time = int(normalvariate(center, std_time))
        clock_time = clamp(time, center - thresh, center + thresh)

        std_rate = thresh / (3 * damp_rate)
        rate = int(normalvariate(0, std_rate))
        clock_rate = clamp(rate, -thresh, thresh)

        clocks.append((clock_time, clock_rate))
    min_clock = min(clocks)
    clocks = [(t - min_clock[0], d) for t, d in clocks]
    [print(*clock) for clock in clocks]