# !difficulty: easy

# Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order.
# Input:
# array = [1, 2, 3, 5, 6, 8, 9]
# Output:
# [1, 4, 9, 25, 36, 64, 81]

# solution with the creation of a new array but in O(n) time
# O(n) time - where n is the length of the input array
# O(n) space - where n is the length of the input array
def sortedSquaredArray (array):
    sortedSquares = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    for idx in range(len(array) - 1, -1, -1):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largerValue * largerValue
            largerValueIdx -= 1

    return sortedSquares

# solution with the creation of a new array
# Complexity
# O(nlog(n)) time - where n is the number of the array
# O(n) space - because we create a new array and n is the number of elements in the array
def sortedSquaredArray(array):
    sortedSquares = []
    for i in range(len(array)):
        sortedSquares.append(array[i] * array[i])
        for j in range(i, 0, -1):
            if sortedSquares[j] >= sortedSquares[j - 1]:
                break
            sortedSquares[j], sortedSquares[j - 1] = sortedSquares[j - 1], sortedSquares[j]
    return sortedSquares

# solution with no new array and sort() method
# Complexity
# O(nlog(n)) time - where n is the number of the array (cost to order numbers)
# O(1) space
def sortedSquaredArray(array):
    for i in range(len(array)):
        array[i] *= array[i]
    array.sort()
    return array

# solution with no new array and insertion sort style of ordering
# Complexity
# O(nlog(n)) time - where n is the number of the array (cost to order numbers)
# O(1) space
def sortedSquaredArray(array):
    for i in range(len(array)):
        array[i] *= array[i]
        for j in range(i, 0, -1):
            if array[j] >= array[j - 1]:
                break
            array[j], array[j - 1] = array[j - 1], array[j]
    return array
