# global dict and handle base cases
def __init__(self):
    self.memo = {1: 1, 2: 2}


def climbStairs(self, n):
    if n not in self.memo:
        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
    return self.memo[n]
