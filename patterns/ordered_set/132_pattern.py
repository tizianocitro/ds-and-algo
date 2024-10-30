# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/132-pattern-medium

'''Problem:
Given an array nums, containing N integers. A 132 pattern consists of three numbers, say x, y, and z, where x < z and z < y.
This is often referred to as a '132' pattern because if we represent x, y, and z as 1, 3, and 2, respectively, it mimics the positional pattern in '132'.
Return true if such a pattern exists within any sequence of given numbers nums. Otherwise, return false.

Note that the it says sequence so it wants a subsequence and not a subarray, meaning the numbers can be non-contiguous.

Input: nums = [3, 5, 0, 3, 4]
Output: True
Explanation: Here, 3 < 4 and 4 < 5, forming a '132' pattern with the numbers 3, 5, and 4.

Input: nums = [1, 2, 3, 4]
Output: False
Explanation: The sequence is in ascending order, and no '132' pattern is present.

Input: nums = [9, 11, 8, 9, 10, 7, 9]
Output: True
Explanation: The pattern is formed with 8 < 9 and 9 < 10 in sequence 8, 10, 9.
'''

'''Solution:
The 132 Pattern problem requires finding a sequence of three numbers in an array such that the first number is smaller than the third number, which is in turn smaller than the second number. In other words, for indices i, j, and k, we need to find a pattern where nums[i] < nums[k] < nums[j] with i < j < k.

To solve this problem efficiently, we use a combination of a stack and a set to track potential candidates for the 132 pattern as we iterate through the array from the end to the beginning. This approach ensures that we can quickly identify and verify the necessary conditions for the pattern.
'''

# solution using monotonic stack
# Complexity:
# O(n) time - where n is the length of the input array nums
# O(n) space - for the stack
class Solution:
    def find132pattern(self, nums):
        # initialize z to the smallest possible value
        z = float('-inf')
        # use a stakc to keep track of the potential candidates for the third number
        stack = []

        # iterate backwards through the list
        for num in reversed(nums):
            if num < z:
                # a 132 pattern is found
                return True
            while stack and stack[-1] < num:
                # update z to the largest smaller element
                z = stack.pop()
            # add the current number to the set
            stack.append(num)

        # no 132 pattern found
        return False

# solution one using stack and set
# Complexity:
# O(nlogn) time - where n is the length of the input array nums. The time complexity is O(nlogn) because we iterate
# through the array once, and for each element, we perform a binary search operation on the set of potential candidates
# O(n) space - for the stack and the set of potential candidates
import bisect

class Solution:
    def find132pattern(self, nums):
        # also, the combination of stack and set allows to keep the second set sorted
        # list to store potential candidates for the second number (nums[j])
        second = []
        # stack to manage the numbers, this will maintain the third number (nums[k])
        stack = []

        # iterate through the array from the end to the beginning
        # this reverse iteration helps us to maintain the
        # potential third element (nums[k]) in the stack
        for i in range(len(nums) - 1, -1, -1):
            # pop elements from the stack that are smaller than the current number
            while stack and stack[-1] < nums[i]:
                # and push them as potential candidate for the second number (nums[j])
                second.append(stack.pop())

            # if there are candidates for both third and second number,
            # check if the current number can be part of a 132 pattern
            if stack and second:
                # bisect_right() finds the position of the smallest
                # number in the list greater than nums[i]
                pos = bisect.bisect_right(second, nums[i])
                if pos < len(second):
                    # if such a number exists, we found a 132 pattern
                    return True

            # push the current number onto the stack as a potential third number (nums[k])
            stack.append(nums[i])

        # no 132 pattern found
        return False