from typing import List


class Solution:
    # takes up more space
    def rob(self, nums: List[int]) -> int:
        # empty list base case
        if not nums:
            return 0
        # list of 1 or 2
        if len(nums) <= 2:
            return max(nums)

        # dynamic programming array
        dp = [0] * len(nums)

        # if we start with the first value
        dp[0] = nums[0]
        # if we start with the second value
        dp[1] = max(nums[0], nums[1])

        # start at 2 and go up to length of nums
        for n in range(2, len(nums)):
            # compare cumulative sum and prev sum
            dp[n] = max(dp[n - 1], nums[n] + dp[n - 2])

        # return last
        return dp[-1]

    def better_rob(self, nums: List[int]) -> int:
        prev = curr = 0

        for num in nums:
            temp = prev
            prev = curr
            curr = max(num + temp, prev)

        return curr

