from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memo = {}
        for i in nums:
            if i in memo:
                return True
            memo[i] = i
        return False

