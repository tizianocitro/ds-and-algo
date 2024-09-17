# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f98b9d239f7cde26ddcaf

'''Problem:
Given a Bitonic array, find if a given key is present in it.
An array is considered bitonic if it is monotonically increasing and then monotonically decreasing.
Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

Write a function to return the index of the key.
If the key appears more than once, return the smaller index.
If the key is not present, return -1.

Input: [1, 3, 8, 4, 3], key=4
Output: 3

Input: [3, 8, 3, 1], key=8
Output: 1

Input: [1, 3, 8, 12], key=12
Output: 3

Input: [10, 9, 8], key=10
Output: 0
'''

# solution one
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

    # find index of the maximum value in a bitonic array
    def findPeakIndex(self, arr):
        left, right = 0, len(arr) - 1
        while left < right:
            middle = (left + right) // 2
            if arr[middle] > arr[middle + 1]:
                right = middle
            else:
                left = middle + 1

        # at the end of the while loop, 'left == right'
        # and they will point to the maximum value in the array
        return left

    # order-agnostic binary search
    def binarySearch(self, arr, key, left, right):
        while left <= right:
            middle = (left + right) // 2
            current = arr[middle]

            if key == current:
                return middle

            # ascending order
            if arr[left] < arr[right]:
                if key < current:
                    right = middle - 1
                else: # key > arr[mid]
                    left = middle + 1
            else: # descending order
                if key > current:
                    right = middle - 1
                else: # key < arr[mid]
                    left = middle + 1

        # element is not found
        return -1

# solution two
# Complexity:
# O(logn) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def search(self, arr, key):
        return self.binarySearch(arr, key, 0, len(arr) - 1)

    def binarySearch(self, arr, key, left, right):
        min_index = -1

        while left <= right:
            middle = (left + right) // 2
            current = arr[middle]

            # if the current element is the key, we update the min_index
            # and we search the left side because we want the smaller index
            if current == key:
                min_index = middle
                right = middle - 1
                continue

            # identify if the current element is a peak and the direction of the peak
            isDesc = current > arr[middle + 1]
            isAsc = current > arr[middle - 1]
            isPeak = isDesc and isAsc

            # if it is a peak, we can search both sides
            if isPeak:
                left_index = self.binarySearch(arr, key, left, middle - 1)
                right_index = self.binarySearch(arr, key, middle + 1, right)
                # if left size does not return -1, we returns it
                # because the index will surely be smaller than the right side
                if left_index != - 1:
                    return left_index
                # if left side returns -1, we return the right side,
                # even if it is -1 because the key is not in the array
                else:
                    return right_index

            # if it is not a peak, we can search only one side
            if current > key:
                # if it is descending, we search the right side
                if isDesc:
                    left = middle + 1
                else: # if it is ascending, we search the left side
                    right = middle - 1
            else: # if current < key, we search only one side because it is not a peak
                if isDesc: # if it is descending, we search the left side
                    right = middle - 1
                else: # if it is ascending, we search the right side
                    left = middle + 1

        return min_index
