from typing import Optional

def find_zero(nums, k) -> Optional[tuple[int, int]]:
    # Multiply (x, y=0)
    if 0 in nums and k > 1:
        if nums[0] == 0:
            return nums[1], 0
        else:
            return nums[0], 0
    
    # Subtract (x, x)
    nums = sorted(nums)
    for i in range(k - 1):
        if nums[i] == nums[i+1]:
            return nums[i], nums[i+1]
    
    # Add (x, -x)
    nums = sorted(nums, key=lambda x: abs(x))
    for i in range(k - 1):
        if abs(nums[i]) == abs(nums[i+1]):
            return nums[i], nums[i+1]


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
