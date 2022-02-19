# The Grid Traveler can only travel horizontally and vertically.

# memo needs to be outside of the function because it can't be passed as an arg
memo = {}


def gridTraveler(row, col):
    key = str(row) + ',' + str(col)
    # Base cases
    if key in memo:
        return memo[key]
    if row == 0 or col == 0:
        return 0
    if row == 1 and col == 1:
        return 1
    memo[key] = gridTraveler(row - 1, col) + gridTraveler(row, col - 1)
    return memo[key]


print(gridTraveler(18, 18))
