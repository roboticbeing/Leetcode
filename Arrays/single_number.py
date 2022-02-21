from typing import List


class Solution:
    # O(1) space solution
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num

        return xor
