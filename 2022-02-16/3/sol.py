t = int(input())

for _ in range(t):
    nums = [int(n) for n in input().split()]

    history = {}
    max_length = 0

    for start in range(len(nums)):

        if start in history:
            continue

        this_history = {}

        # Jump around adding things to this_history and history
        idx = start
        while idx < len(nums) and idx not in history and idx not in this_history:
            history[idx] = True
            this_history[idx] = True
            idx = nums[idx]
        
        # If jumped outside array bounds or part of previous loop
        if idx >= len(nums) or (idx in history and idx not in this_history):
            continue

        # Go around loop section again and count
        loop_point = idx
        length = 1
        idx = nums[idx]

        while idx != loop_point:
            length += 1
            idx = nums[idx]
        
        # print(length)
        max_length = max(max_length, length)
    
    print(max_length)
