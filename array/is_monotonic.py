# Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.
# An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.
# Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase.
# Similarly, non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.
# Note that empty arrays and arrays of one element are monotonic.

# Input: array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
# Output: True

# solutions one and two are the same, the only difference id the way we manage boolean variables,
# which leads to a change in the for loop condition
# Complexity
# O(n) time - where n is the length of the input array
# O(1) space
def isMonotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(len(array) - 1):
        isNonDecreasing = isNonDecreasing and array[i] >= array[i + 1]
        isNonIncreasing = isNonIncreasing and array[i] <= array[i + 1]
    return isNonDecreasing or isNonIncreasing

def isMonotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isNonDecreasing = False
        if array[i] > array[i - 1]:
            isNonIncreasing = False
    return isNonDecreasing or isNonIncreasing

# solution three with direction
# Complexity
# O(n) time - where n is the length of the input array
# O(1) space
def isMonotonic(array):
    if len(array) < 2:
        return True
    direction = array [1] - array [0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue
        if breaksDirection(direction, array[i - 1], array[i]):
            return False
    return True

def breaksDirection(direction, previousInt, currentInt):
    difference = currentInt - previousInt
    if direction > 0:
        return difference < 0
    return difference > 0

# solution four using two pointers
# Complexity
# O(n) time - where n is the length of the input array
# O(1) space
def isMonotonic(array):
    if len(array) < 2:
        return True
    isMonotonic = True
    i = k = 0
    j = l = len(array) - 1

    while i <= j:
        if array[i] > array[i + 1] or array[j - 1] > array[j]:
            isMonotonic = False
            break
        else:
            i += 1
            j -= 1

    if isMonotonic:
        return True

    while k <= l:
        if array[k] >= array[k + 1] and array[l - 1] >= array[l]:
            k += 1
            l -= 1
        else:
            return False

    return True