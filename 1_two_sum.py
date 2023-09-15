from collections import defaultdict

class Solution:
    def twoSum(self, nums, target):
        hashmap = defaultdict()

        for index, num in enumerate(nums):

            diff = target - num

            if diff in hashmap:
                return [index, hashmap[diff]]

            hashmap[num] = index


                
              



_input = [3,2,4]
target = 6
s = Solution()
print(s.twoSum(_input, target))