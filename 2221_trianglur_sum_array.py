from typing import List

def triangularSum(nums: List[int]) -> int:
    _nums = [0] * 2

    if len(nums) == 1:
        return nums[0]

    while len(_nums) > 1:
        _nums = [0] * (len(nums) - 1)
        
        for index, num in enumerate(_nums):
            _nums[index] = (nums[index] + nums[index + 1]) % 10

        nums = _nums

    return nums[0]

_input = [1,1]
print(triangularSum(_input))