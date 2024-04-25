# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f1a8b44223ca42ca4a723

'''Problem:
Given a sorted array of numbers, find if a given number key is present in the array.
Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order.
You should assume that the array can have duplicates.

Write a function to return the index of the key if it is present in the array, otherwise return -1.

Input: [4, 6, 10], key = 10
Output: 2

Input: [10, 6, 4], key = 10
Output: 0
'''

# solution one
# Complexity:
# O(logn) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def search(self, arr, key):
        left, right = 0, len(arr) - 1

        while left <= right:
            middle = (left + right) // 2
            current = arr[middle]

            # found element
            if current == key:
                return middle

            if current < key:
                # if asc order, then it's normal binaryb search
                if arr[left] <= arr[right]:
                    left = middle + 1
                else: # otherwise, we have to move in the opposite direction
                    right = middle - 1

            if current > key:
                # if asc order, then it's normal binaryb search
                if arr[left] <= arr[right]:
                    right = middle - 1
                else: # otherwise, we have to move in the opposite direction
                    left = middle + 1

        # element not found
        return -1

# solution two using a direction flag
# Complexity:
# O(logn) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def search(self, arr, key):
        left, right = 0, len(arr) - 1
        is_ascending = arr[left] < arr[right]
        
        while left <= right:
            # calculate the middle of the current range
            middle = left + (right - left) // 2

            if key == arr[middle]:
                return middle

        if is_ascending: # ascending order
            if key < arr[middle]:
                right = middle - 1 # the 'key' can be in the first half
            else: # key > arr[mid]
                left = middle + 1 # the 'key' can be in the second half
        else: # descending order
            if key > arr[middle]:
                right = middle - 1 # the 'key' can be in the first half
            else: # key < arr[mid]
                left = middle + 1 # the 'key' can be in the second half

        # element not found
        return -1
