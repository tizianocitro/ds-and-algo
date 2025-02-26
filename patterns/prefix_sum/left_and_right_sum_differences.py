# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/left-and-right-sum-differences-easy

'''Problem:
Given an input array of integers nums, find an integer array, let's call it differenceArray, of the same length as an input integer array.

Each element of differenceArray, i.e., differenceArray[i], should be calculated as follows:
take the sum of all elements to the left of index i in array nums (let's call it leftSumi), and subtract it from the sum of all elements
to the right of index i in array nums (let's call it rightSumi), taking the absolute value of the result: differenceArray[i] = |leftSumi - rightSumi|

If there are no elements to the left or right of i, the corresponding sum should be taken as 0.

Input: nums = [2, 5, 1, 6, 1]
Output: [13, 6, 0, 7, 14]
Explanation:
    For i=0: |(0) - (5+1+6+1)| = |0 - 13| = 13
    For i=1: |(2) - (1+6+1)| = |2 - 8| = 6
    For i=2: |(2+5) - (6+1)| = |7 - 7| = 0
    For i=3: |(2+5+1) - (1)| = |8 - 1| = 7
    For i=4: |(2+5+1+6) - (1)| = |14 - 0| = 14

Input: nums = [3, 3, 3]
Output: [6, 0, 6]
Explanation:
    For i=0: |(0) - (3+3)| = 6
    For i=1: |(3) - (3)| = 0
    For i=2: |(3+3) - (0)| = 6

Input: nums = [1, 2, 3, 4, 5]
Output: [14, 11, 6, 1, 10]
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input array
# O(n) space - for the difference_array
class Solution:
    def findDifferenceArray(self, nums):
        difference_array = [0] * len(nums)

        total_sum = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            right_sum = total_sum - left_sum - num
            difference_array[i] = abs(right_sum - left_sum)
            left_sum += num

        return difference_array

# solution two
# Complexity:
# O(n) time - where n is the length of the input array
# O(n) space - for the difference_array
class Solution:
    def findDifferenceArray(self, nums):
        difference_array = [0] * len(nums)

        left_sum = 0
        right_sum = sum(nums)
        for i, num in enumerate(nums):
            # to keep the right_sum updated we can just subtract the
            # current number from the right_sum
            right_sum -= num
            difference_array[i] = abs(right_sum - left_sum)
            left_sum += num

        return difference_array