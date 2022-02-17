from typing import List


class Solution:
    # First Brute-Force Solution O(n)
    def search(self, nums: List[int], target: int) -> int:
        for index, value in enumerate(nums):
            if value == target:
                return index
        # if it's not in the list
        return -1

    # Binary Search Solution O(logn)
    def binary_search(self, nums: List[int], target: int) -> int:
        # declare our lower and upper bounds
        low = 0
        high = len(nums)
        # loop through our list
        while low < high:
            # declare our mid point and round down
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            # trying to find the first false
            # search the right side
            # increase the lower bound
            elif nums[mid] < target:
                # if it's true, check against the next number in the sequence
                low = mid + 1
            # search the left side
            # decrease the upper bound
            else:
                high = mid
        return -1

    def validate(self, rc: int):
        print(rc)


debug = Solution()
test1 = debug.search([-1, 0, 3, 5, 9, 12], 9)
test2 = debug.search([-1, 0, 3, 5, 9, 12], 2)
test3 = debug.search([], 2)
test4 = debug.binary_search([-1, 0, 3, 5, 9, 12], 9)
test5 = debug.binary_search([-1, 0, 3, 5, 9, 12], 2)
# what if it shows up more than once?
# what if my array is empty?

debug.validate(test1)
debug.validate(test2)
debug.validate(test3)
debug.validate(test4)
debug.validate(test5)
