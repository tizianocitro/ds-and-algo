# !difficulty: medium, !from: https://www.algoexpert.io/questions/three-number-sort

# You're given an array of integers and another array of three distinct integers.
# The first array is guaranteed to only contain integers that are in the second array, and the second array represents a desired order for the integers in the first array.
# For example, a second array of [x, y, z] represents a desired order of [x, x, ..., x, y, y, ..., y, z, z, ..., z] in the first array.
# Write a function that sorts the first array according to the desired order in the second array.
# The function should perform this in place (i.e., it should mutate the input array), and it shouldn't use any auxiliary space (i.e., it should run with constant space: 0(1) space).
# Note that the desired order won't necessarily be ascending or descending
# and that the first array won't necessarily contain all three integers found in the second array it might only contain one or two.

# Sample Input
# array = [1, 0, 0, -1, -1, 0, 1, 1]
# order = [0, 1, -1]
# Sample Output
# [O, 0, 0, 1, 1, 1, -1, -1]

# Complexity
# O(n) time | O(1) space - where n is the length of the array

# solution one
# swaps elements starting from left to right whenever it finds an element matching the order element
def threeNumberSort(array, order):
    i = 0
    for n in order:
        for j in range(i, len(array)):
            if array[j] == n:
                array[i], array[j] = array[j], array[i]
                i += 1
    return array

# solution two
# swaps elements starting from left and whenever it finds an element matching the order element,
# it switches the element with the element at position j, where j starts at the end of the array
# and is decremented every time an element is swapped because we are sure it is not equals to the order element.
def threeNumberSort(array, order):
    i = 0
    for n in order:
        j = len(array) - 1
        while i <= j:
            if array[i] == n:
                i += 1
            else:
                array[i], array[j] = array[j], array[i]
                j -= 1
    return array