from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}

        for i in range(len(nums)):
            if nums[i] in memo:
                return [memo[nums[i]], i]
            else:
                memo[target - nums[i]] = i

debug = Solution()

print(debug.twoSum([2,7,11,15,19], 9))