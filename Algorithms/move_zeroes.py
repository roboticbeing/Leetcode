from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for n in range(len(nums) - 1, -1, -1):
            if nums[n] == 0:
                del nums[n]
                nums.append(0)

debug = Solution()

debug.moveZeroes([0,0,1])