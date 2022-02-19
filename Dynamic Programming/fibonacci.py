memo = {}

def fib(n):
    if n <= 2:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n]


print(fib(50))
