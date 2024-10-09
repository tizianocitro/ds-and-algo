# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f977fa24c2a2e65e84c02

'''Problem:
Find the maximum value in a given Bitonic array.
An array is considered bitonic if it is monotonically increasing and then monotonically decreasing.
Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

Input: [1, 3, 8, 12, 4, 2]
Output: 12
Explanation: The maximum number in the input bitonic array is 12.

Input: [3, 8, 3, 1]
Output: 8

Input: [1, 3, 8, 12]
Output: 12

Input: [10, 9, 8]
Output: 10
'''

# solution one
# Complexity:
# O(logn) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def findMax(self, arr):
        left, right = 0, len(arr) - 1
        while left <= right:
            middle = (left + right) // 2
            current = arr[middle]

            # if the element is smaller than its right neighbor,
            # then the maximum element must be on the right
            if middle < len(arr) - 1 and current < arr[middle + 1]:
                left = middle + 1
            # if the element is smaller than its left neighbor,
            # then the maximum element must be on the left
            elif middle > 0 and current < arr[middle - 1]:
                right = middle - 1
            # if the element is greater than both of its neighbors,
            # then we are in the maximum element
            else:
                return current

        return -1

# solution two
# Complexity:
# O(logn) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def findMax(self, arr):
        start, end = 0, len(arr) - 1

        # we break when start == end due to both start and end pointers
        # being equals when pointing at the maximum number of the bitonic array
        while start < end:
            # when we calculate the middle, we can compare the numbers pointed out by the indexs
            # middle and middle + 1 to find if we are in the ascending or the descending part
            middle = start + (end - start) // 2

            # if arr[middle] > arr[middle + 1], we are in the second (descending) part of the bitonic array,
            # therefore, our required number could either be pointed out by middle or will be before middle
            # this is why we do end = middle
            if arr[middle] > arr[middle + 1]:
                end = middle
            # if arr[middle] < arr[middle + 1], we are in the first (ascending) part of the bitonic array,
            # therefore, the required number will be after middle, so we do: start = middle + 1
            else:
                start = middle + 1

        # at the end of the while loop, 'start == end'
        return arr[start]
