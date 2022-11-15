from typing import Optional, Tuple

def find_zero(nums, k) -> Optional[Tuple[int, int]]:
    # Multiply
    if 0 in nums and k > 1:
        if nums[0] == 0:
            return nums[1], 0
        else:
            return nums[0], 0

    # Add or Subtract
    for i, n1 in enumerate(nums):
        for n2 in nums[i+1:]:
            if abs(n1) == abs(n2):
                return n1, n2
    
    if 0 in nums and k > 1:
        if nums[0] == 0:
            return nums[1], 0
        else:
            return nums[0], 0


n = int(input())
for _ in range(n):
    k = int(input())
    nums = [int(i) for i in input().split()]
    pair = find_zero(nums, k)
    if pair is None:
        print("Not Found")
    else:
        x, y = pair
        print(x, y)