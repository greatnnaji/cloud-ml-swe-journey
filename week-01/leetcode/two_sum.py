def twoSum(nums: list[int], target: int) -> list[int]:
    index_to_value_map = {}
    return_list = []
    for index, value in enumerate(nums):
        index_to_value_map[value] = index
    
    for index, value in enumerate(nums):
        difference = target - value
        if difference in index_to_value_map and index_to_value_map[difference] != index:
            return_list.append(index)
            return_list.append(index_to_value_map[difference])
            print(return_list)
            return return_list
    
    print("The value you are looking for is not contained in list")

    return []

twoSum([5,5], 10)
