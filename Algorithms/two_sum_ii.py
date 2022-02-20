from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        memo = {}

        for n in range(len(numbers)):
            if numbers[n] in memo:
                return [memo[numbers[n]], n + 1]
            else:
                memo[target - numbers[n]] = n+1

debug = Solution()

print(debug.twoSum([2,3,4], 6))