'''
Write a function that takes in a sorted array of integers as well as a target integer.
The function should use the Binary Search algorithm to determine if the target integer is contained in the array
and should return its index if it is, otherwise -1
'''

# solution one iterative
# Complexity:
# O(log(n)) time - where n is the length of the input array because we are cutting the array in half every time
# O(1) space
def binarySearch(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        el = array[middle]
        if el == target:
            return middle

        if el < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1

# solution two recursive
# Complexity:
# O(log(n)) time - where n is the length of the input array
# O(log(n)) space - because we are using recursion
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)
    
def binarySearchHelper(array, target, left, right):
    if left > right:
        return - 1
    
    middle = (left + right) // 2
    el = array[middle]
    if el == target:
        return middle

    if el < target:
        return binarySearchHelper(array, target, middle + 1, right)
    else:
        return binarySearchHelper(array, target, left, middle - 1)