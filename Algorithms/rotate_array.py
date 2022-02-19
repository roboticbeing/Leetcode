import collections
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        im_a_cheater_that_uses_a_deque = collections.deque(nums)
        im_a_cheater_that_uses_a_deque.rotate(k)
        nums[:] = list(im_a_cheater_that_uses_a_deque)
        print(nums)


debug = Solution()

debug.rotate([1, 2, 3, 4, 5, 6, 7], 3)
