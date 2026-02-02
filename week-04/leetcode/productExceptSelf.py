# naive solution would be O(n^2)
# need to do in 0(n)
# - storing results in new array would work and then divide by nums[i] (with division)


import numpy as np

def productExceptSelf(nums: list[int]) -> list[int]:
    left = []
    left.append(1)
    right = []
    right.append(1)

    for i, value in enumerate(nums[:-1]):
        left.append(value * left[-1])

    for i,value in reversed(list(enumerate(nums[1:]))): # reversed to go from right to left excluding last element
        right.insert(0, value * right[0])
    
    arr1 = np.array(left)
    arr2 = np.array(right)

    result_arr = np.multiply(arr1,arr2)

    print(result_arr)

    return result_arr

# example test case
nums = [1,2,3,4]
productExceptSelf(nums)