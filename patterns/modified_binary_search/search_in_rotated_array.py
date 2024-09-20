# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f9a0cd239f7cde26dde2b

'''Problem:
Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, find if a given key is present in it.

Write a function to return the index of the key in the rotated array. If the key is not present, return -1.
You can assume that the given array does not have any duplicates.

Input: [10, 15, 1, 3, 8], key = 15
Output: 1
Explanation: '15' is present in the array at index '1'.

Input: [4, 5, 7, 9, 10, -1, 2], key = 10
Output: 4
Explanation: '10' is present in the array at index '4'.
'''

# solution one with find peak index
# Complexity:
# O(logn) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def search(self, arr, key):
        peak_index = self.findPeakIndex(arr)
        left_index = self.binarySearch(arr, key, 0, peak_index)
        if left_index != -1:
            return left_index
        return self.binarySearch(arr, key, peak_index + 1, len(arr) - 1)

    def findPeakIndex(self, arr):
        left, right = 0, len(arr) - 1
        while left < right:
            middle = (left + right) // 2
            if arr[middle] > arr[middle + 1]:
                return middle
            # if the middle is bigger than the right,
            # then we are ascending side of the array
            if arr[middle] > arr[right]:
                left = middle + 1
            else: # we are in the descending side of the array
                right = middle
        return left

    def binarySearch(self, arr, key, left, right):
        while left <= right:
            middle = (left + right) // 2
            if arr[middle] == key:
                return middle
            if arr[middle] < key:
                left = middle + 1
            else:
                right = middle - 1
        return -1

'''Solution two idea:
After calculating the middle, we can compare the numbers at indices start and middle. This will give us two options:
1. If arr[start] <= arr[middle], the numbers from start to middle are sorted in ascending order.
2. Else, the numbers from middle + 1 to end are sorted in ascending order.

Once we know which part of the array is sorted, it is easy to adjust our ranges.
For example, if option-1 is true, we have two choices:
1. By comparing the key with the numbers at index start and middle we can easily find out
   if the key lies between indices start and middle; if it does, we can skip the second part => end = middle - 1.
2. Else, we can skip the first part => start = middle + 1.
'''

# solution two with direction
# Complexity:
# O(logn) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def search(self, arr, key):
        # left -> start, right -> end
        left, right = 0, len(arr) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if arr[middle] == key:
                return middle

            if arr[left] <= arr[middle]: # left side is sorted in ascending order
                if key >= arr[left] and key < arr[middle]:
                    right = middle - 1
                else: # key > arr[mid]
                    left = middle + 1
            else: # right side is sorted in ascending order
                if key > arr[middle] and key <= arr[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        # we are not able to find the element in the given array
        return -1
