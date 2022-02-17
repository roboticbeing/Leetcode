import collections
from typing import List


class Solution:

    # Brute Force O(nlogn)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        newlist = [i ** 2 for i in nums]
        newlist.sort()
        return newlist

    # Two Pointer Solution O(n) is the best solution
    def sortedSquares2Pointer(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        newlist = []
        while l <= r:
            if nums[l] ** 2 < nums[r] ** 2:
                newlist.insert(0, nums[r] ** 2)
                r -= 1
            else:
                newlist.insert(0, nums[l] ** 2)
                l += 1
        return newlist

    # Deque Solution O(n) - does not work with large loads of data - is faster than a list when inserting/popping items
    def sortedSquaresDeque(self, nums: List[int]) -> List[int]:
        deque_nums = collections.deque(nums)
        reverse_sorted_list = []
        while deque_nums:
            left_square = deque_nums[0] ** 2
            right_square = deque_nums[-1] ** 2
            if left_square < right_square:
                reverse_sorted_list.append(right_square)
                deque_nums.pop()
            else:
                reverse_sorted_list.append(left_square)
                deque_nums.popleft()
        return reverse_sorted_list[::-1]

debug = Solution()

print(debug.sortedSquares([-4,-1,0,3,10]))
print(debug.sortedSquares2Pointer([-4,-1,0,3,10]))
print(debug.sortedSquaresDeque([-4,-1,0,3,10]))