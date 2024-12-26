# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a096ffba30a80b3d62a94c

'''Problem:
Given an array of numbers which is sorted in ascending order and is rotated k times around a pivot, find k.

You can assume that the array does not have any duplicates.

Keep in mind that k can be 0, so the given array is an ascending array that is possibly rotated.

Input: [10, 15, 1, 3, 8]
Output: 2
Explanation: The array has been rotated 2 times.

Input: [4, 5, 7, 9, 10, -1, 2]
Output: 5
Explanation: The array has been rotated 5 times.

Input: [1, 3, 8, 10]
Output: 0
Explanation: The array has not been rotated.
'''

# solution oen by finding the peak
# Complexity:
# O(logn) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def countRotations(self, arr):
        peak_index = self.findPeakIndex(arr)
        return peak_index + 1

    def findPeakIndex(self, arr):
        left, right = 0, len(arr) - 1
        while left < right:
            middle = (left + right) // 2
            current = arr[middle]
            if current > arr[middle + 1]:
                return middle
            elif current > arr[right]:
                left = middle + 1
            else:
                right = middle
        return -1

# solution two by comparing the left and right
# Complexity:
# O(logn) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def countRotations(self, arr):
        left, right = 0, len(arr) - 1
        while left < right:
            middle = left + (right - left) // 2

            # if middle is greater than the next element
            if middle < right and arr[middle] > arr[middle + 1]:
                return middle + 1

            # if middle is smaller than the previous element
            if middle > left and arr[middle - 1] > arr[middle]:
                return middle

            # left side is sorted, so the pivot is on right side
            if arr[left] < arr[middle]:
                left = middle + 1
            else: # right side is sorted, so the pivot is on the left side
                right = middle - 1

        # the array has not been rotated
        return 0