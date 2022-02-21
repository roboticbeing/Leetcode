class Solution:
    def firstUniqChar(self, s: str) -> int:
        memo = {}

        for c in range(len(s)):
            if s[c] not in memo:
                memo[s[c]] = 1
            else:
                memo[s[c]] += 1

        for c in range(len(s)):
            if memo[s[c]] == 1:
                return c

        return -1

