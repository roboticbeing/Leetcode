from typing import List


class Solution:
    # This is Kadane's algorithm. It is O(n).
    # This problem can be applied to Computer Vision when trying to find the brightest area in an image.
    def maxSubArray(self, nums: List[int]) -> int:
        # empty list case
        if not nums:
            return 0

        max_sum = curr_sum = nums[0]

        for i in nums:
            # having this line actually takes up less memory and runs faster
            curr_sum += i
            curr_sum = max(i, curr_sum)
            max_sum = max(curr_sum, max_sum)
        return max_sum


debug = Solution()

print(debug.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(debug.maxSubArray([-2]))
print(debug.maxSubArray([]))
