# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/find-minimum-in-rotated-sorted-array-medium

'''Problem:
You have an array of length n, which was initially sorted in ascending order. This array was then rotated x times. It is given that 1 <= x <= n.
For example, if you rotate [1, 2, 3, 4] array 3 times, resultant array is [2, 3, 4, 1].
Your task is to find the minimum element from this array. Note that the array contains unique elements.

You must write an algorithm that runs in O(log n) time.

Input: [8, 1, 3, 4, 5]
Output: 1
Explanation: The smallest number in the array is 1.

Input: [4, 5, 7, 8, 0, 2, 3]
Output: 0
Explanation: The smallest number in the array is 0.

Input: [7, 9, 12, 3, 4, 5]
Output: 3
Explanation: In this rotated array, the smallest number present is 3.
'''

# solution one by finding the the peak and returning its next element
# Complexity:
# O(logn) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def findMin(self, nums) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) // 2
            if middle < len(nums) - 1 and nums[middle] > nums[middle + 1]:
                return nums[middle + 1]

            # if the middle is bigger than the right, then we are in the rotated part
            # of the array, so higher numbers are on the right, otherwise, we are in the
            # non-rotated side of the array, so higher numbers are on the left
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        # if we don't find the peak, the smallest number is the first one
        # because not finding the peak means the array is sorted in ascending order
        return nums[0]

# solution two
# Complexity:
# O(logn) time - where n is the number of elements in the input array
# O(1) space
class Solution:
    def findMin(self, nums) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            # if mid element is greater than the rightmost element, the minimum is on the right
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                # otherwise, the minimum is on the left or at mid
                right = middle

        # at the end of the loop, left == right, so we return nums[left]
        return nums[left]
