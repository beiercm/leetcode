def subarraySum(nums, k):
    start_index = 0
    window_index = 0
    count = 0

    while start_index < len(nums):
        window_index = start_index
        while window_index < len(nums):
            if sum(nums[start_index:window_index + 1]) == k:
                count += 1
                break
            window_index += 1
        start_index += 1

    return count

input = [1,2,3]
target = 3
print(subarraySum(input, target))