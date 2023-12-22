# Given an array of integers between 1 and n, inclusive, where n is the length of the array, write a function
# that returns the first integer that appears more than once (when the array is read from left to right).
# In other words, out of all the integers that might occur more than once in the input array,
# the function should return the one whose first duplicate value has the minimum index.
# If no integer appears more than once, the function should return -1 .
# Note that you're allowed to mutate the input array.

# solution one with set
# Complexity
# O(n) time - where n is the length of the input array
# O(n) space - where n is the length of the input array
def firstDuplicateValue(array):
    s = set()
    for n in array:
        if n in s:
            return n
        s.add(n)
    return - 1

# solution two with no extra space
# Complexity
# O(n) time - where n is the length of the input array
# O(1) space
# This is solution only works because values in the array are guaranteed to be in the ragne 1...n and because we can mutate the array.
# The range 1...n is important because we can map numbers to their index by just subtracting 1 from their absolute value.
# Then we mark the number in the mapped index as negative to signify that we've seen it before.
def firstDuplicateValue(array):
    for n in array:
        # convert to absolute value because we're going to use it as an index and we don't want negative indexes
        absN = abs(n)
        # if it's < 0 it means we've already seen and set it to the negative version of itself
        if array[absN - 1] < 0:
            return absN
        # set it to the negative version of itself to signify that we've seen it
        array[absN - 1] *= -1
    return -1
