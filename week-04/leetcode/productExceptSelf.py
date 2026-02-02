# need to do in 0(n)
# - storing results in new array would work and then divide by nums[i]
# - possible to solve without division?
# naive solution would be O(n^2)

import math

def productExceptSelf(nums: list[int]) -> list[int]:
    total_prod = math.prod(nums)
    new_nums = [total_prod] * len(nums)

    for i in range(len(nums)):
        new_nums[i] = new_nums[i]/nums[i]

    print(new_nums)
    
    return []

# example test case
nums = [1,2,3,4]
productExceptSelf(nums)