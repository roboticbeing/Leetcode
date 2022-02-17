# Test Input
n = 5
result = 0

# Brute Force
for i in range(0, n+1):
    result += i
print(result)

# Math Trick
print(n * (n + 1) / 2)

# Sum function
print(sum(range(0, n+1)))
