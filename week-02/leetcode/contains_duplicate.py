def hasDuplicate(nums: list[int]) -> bool:
    unique = set(nums) # O(n)
    print(len(unique) != len(nums))
    return len(unique) != len(nums)

nums = [1, 2, 3, 3]
hasDuplicate(nums)

