# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
# If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order.
# If no two numbers sum up to the target sum, the function should return an empty array.
# Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum.
# You can assume that there will be at most one pair of numbers summing up to the target sum.

# Input:
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# target_sum = 10
# Output: [-1, 11]

# solution one with set
# Complexity
# O(n) time - where n is the number of elements in the array
# O(n) space - because we create a set which in the worst case will contain n numbers where n is the number of elements in the array
def two_number_sum(array, target_sum):
    complements = set()
    for n in array:
        complement = target_sum - n
        if n in complements:
            return [n, complement]
        complements.add(complement)
    return []

# solution two with the use of two pointers
# Complexity
# O(n) time - where n is the number of elements in the array
# O(1) space
def two_number_sum(array, target_sum):
    array.sort()
    left = 0
    right = len(array) - 1
    # Maybe it should be right > left to avoid summing numbers on the same index
    # (e.g. at index 4 there is 5 with 5 + 5 = 10 == target_sum)
    while right >= left:
        sum = array[left] + array[right]
        if sum == target_sum:
            return [array[left], array[right]]
        if sum < target_sum:
            left += 1
        if sum > target_sum:
            right -= 1
    return []
