from collections import Counter
def topKfrequentElements(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    
    bucket = []
    for _ in range(len(nums) + 1): # need +1 cause index starts at 0
        bucket.append([])
    
    # print(bucket)

    for num, freq in count.items():
        bucket[freq].append(num)
    
    # for index, value in enumerate(bucket):
    #     print(index, value)

    result = []
    for i in range(len(bucket) - 1, 0, -1): # start len(bucket)-1, stop at 0, count down -1 (step), stop = 0 same as while i > 0
        for num in bucket[i]:
            result.append(num)
            if len(result) == k:
                return result
    
    return result

# this ex. helps see clearly why we need len(nums) + 1 for bucket size
nums = [7,7] 
k = 1
print(topKfrequentElements(nums, k))