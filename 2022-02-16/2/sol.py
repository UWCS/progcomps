def num_printers(printers, days):
    if days < 2:
        return printers
    if days == 2:
        return 2 * printers
    
    prev_totals = [printers, printers, 2*printers]

    for _ in range(days - 2):
        curr_total = prev_totals[0] + prev_totals[1]
        prev_totals = prev_totals[1:] + [curr_total]
    
    return curr_total

t = int(input())

for _ in range(t):
    print(num_printers(*[int(s) for s in input().split()]))