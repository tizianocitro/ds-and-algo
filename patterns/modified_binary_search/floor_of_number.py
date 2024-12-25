# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63dd6c9cbe2006431cea7d90

'''Problem:
Given an array of numbers sorted in ascending order, find the floor of a given number key.
The floor of the key will be the biggest element in the given array smaller than or equal to the key.

Write a function to return the index of the floor of the key. If there isn’t a floor, return -1.

Input: [4, 6, 10], key = 6
Output: 1
Explanation: The biggest number smaller than or equal to 6 is 6 having index 1.
'''


# solution one with a floor variable
# Complexity:
# O(logn) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def searchFloorOfANumber(self, arr, key):
        floor = -1

        left, right = 0, len(arr) - 1
        while left <= right:
            middle = (left + right) // 2
            current = arr[middle]

            if current == key:
                return middle

            if current < key:
                floor = middle
                left = middle + 1
            else:
                right = middle - 1

        return floor

# solution two using right pointer position
# it is based on the fact that since the loop is running until 'start <= end',
# so at the end of the while loop, 'start == end + 1' we are not able to find the element in the given array,
# so the next smaller number will be arr[end]
# Complexity:
# O(logn) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def searchFloorOfANumber(self, arr, key):
        # if the key is smaller than the smallest element
        # it is no part of the array, so just return -1
        if key < arr[0]:
            return -1

        start, end = 0, len(arr) - 1
        while start <= end:
            middle = start + (end - start) // 2
            if key < arr[middle]:
                end = middle - 1
            elif key > arr[middle]:
                start = middle + 1
            else: # found the key
                return middle

        # since the loop is running until 'start <= end', so at the end of the while loop, 
        # 'start == end + 1' we are not able to find the element in the given array,
        # so the next smaller number will be arr[end]
        return end

