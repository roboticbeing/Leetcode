from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]

    def reverseString2Pointer(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]

            left, right = left + 1, right - 1

    def reverseStringRecursive(self, s):
        l = len(s)
        if l < 2:
            return s
        return self.reverseStringRecursive(s[l / 2:]) + self.reverseStringRecursive(s[:l / 2])