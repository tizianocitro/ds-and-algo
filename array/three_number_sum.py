# !difficulty: medium

# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
# The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets.
# The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.
# If no three numbers sum up to the target sum, the function should return an empty array.

# Input:
# array = [12, 3, 1, 2, -6, 5, -8, 6]
# targetSum = 0
# Output:
# [-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

# solution one in Quick Sort style
# Complexity
# O(n^2) time - where n is the length of the input array
# O(n) space - where n is the length of the input array
def threeNumberSum(array, targetSum):
    array.sort()
    length = len(array)
    triplets = []
    for i in range(length - 2):
        left = i + 1
        right = length - 1
        while left < right:
            first = array[i]
            second = array[left]
            third = array[right]
            currentSum = first + second + third
            if currentSum == targetSum:
                triplets.append([first, second, third])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return triplets

# solution two using three for loops
# Complexity
# O(n^3) time - where n is the length of the input array
# O(n) space - where n is the length of the input array
def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array)):
        first = array[i]
        for j in range(i, len(array)):
            second = array[j]
            if first != second:
                for k in range(j, len(array)):
                    third = array[k]
                    if third != first and third != second:
                        if first + second + third == targetSum:
                            triplets.append([first, second, third])
    return triplets
