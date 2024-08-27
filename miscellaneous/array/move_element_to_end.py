# !difficulty: medium

# You're given an array of integers and an integer.
# Write a function that moves all instances of that integer in the array to the end of the array and returns the array.
# The function should perform this in place (i.e., it should mutate the input array) and doesn't need to maintain the order of the other integers.

# Input:
# array = [2, 1, 2, 2, 2, 3, 4, 2]
# toMove = 2

# Output: [1, 3, 4, 2, 2, 2, 2, 2], the numbers 1, 3, and 4 could be ordered differently

# solution one with better if management
# Complexity
# O(n) time - where n is the length of the input array
# O(1) space
def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while i < j:
        if array[j] == toMove:
            j -= 1
            continue
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        else:
            i +=1
    return array

# solution two
# Complexity
# O(n) time - where n is the length of the input array
# O(1) space
def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while i < j:
        if array[i] == toMove and array[j] != toMove:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        elif array[i] == toMove and array[j] == toMove:
            j -= 1
        else:
            i +=1
    return array

# solution three in selection sort style
# Complexity
# O(n^2) time - where n is the length of the input array
# O(1) space
def moveElementToEnd(array, toMove):
    for i in range(len(array)):
        if array[i] != toMove:
            continue
        for j in range(i, len(array)):
            if array[j] != toMove:
                array[i], array[j] = array[j], array[i]
    return array
