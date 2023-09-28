# Write a function that takes in two non-empty arrays of integers,
# finds the pair of numbers (one from each array) whose absolute difference is closest to zero,
# and returns an array containing these two numbers, with the number from the first array in the first position.
# Note that the absolute difference of two integers is the distance between them on the real number line.
# For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.
# You can assume that there will onlv be one pair of numbers with the smallest difference.

# Input:
# arrayOne = [-1, 5, 10, 20, 28, 3]
# arrayTwo = [26, 134, 135, 15, 17]

# Output: [28, 26]

# Complexity
# O(nlog(n) + mlog(m)) time - where n is the length of the first input array and m is the length of the second input array
# O(1) space
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    smallestPair = []
    smallest = float("inf")
    current = float("inf")
    i, j = 0, 0
    while i < len(arrayOne) and j < len(arrayTwo):
        first = arrayOne[i]
        second = arrayTwo[j]
        if first < second:
            current = second - first
            i += 1
        elif second < first:
            current = first - second
            j += 1
        else:
            return [first, second]
        if smallest > current:
            smallest = current
            smallestPair = [first, second]
    return smallestPair
