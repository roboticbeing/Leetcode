class Solution:
    def hammingWeight(self, n: int) -> int:
        n = str(n)
        count = 0
        for character in n:
            if character == '1':
                count += 1
        return count

    # built in function
    def hammingWeightBin(self, n: int) -> int:
        return bin(n).count('1')

    #bitwise ops
    def hammingWeightBin(self, n: int) -> int:
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c


debug = Solution()

debug.hammingWeight(1011)