# !difficulty: easy

# Given an array of positive integers representing the values of coins in your possession,
# write a function that returns the minimum amount of change (the minimum sum of money) that you cannot create.
# The given coins can have any positive integer value and aren't necessarily unique (i.e., you can have multiple coins of the same value).
# For example, if you're given coins = [1, 2, 5], the minimum amount of change that you can't create is 4.
# If you're given no coins, the minimum amount of change that you can't create is 1.

# Input: [5, 7, 1, 1, 2, 3, 22]
# Output: 20

# solution one with sorting
# Complexity
# O(nlogn) time where n is the number of coins because we have to sort
# Always ask if you can sort the array in place because if you can the space is O(1),
# otherwise O(n) because you have to create a new array
def nonConstructibleChange(coins):
    coins.sort()
    current = 0
    for coin in coins:
        if coin > current + 1:
            # Return the first value I cannot construct, which is current + 1
            return current + 1
        current += coin
    # If it's empty or if the array contains no coin with a value greater than the current + 1
    # Return the first value I cannot construct, which is current + 1    
    return current + 1

# solution two whith while loop
# Complexity
# O(nm) time where n is the number of time we increase the rest and m is the number of coins
# O(1) space
def nonConstructibleChange(coins):
    current = 1
    rest = 0
    while rest <= 0:
        rest = current
        for coin in coins:
            if coin > current:
                continue
            rest -= coin
        if rest > 0:
            return current
        current += 1
    return 1