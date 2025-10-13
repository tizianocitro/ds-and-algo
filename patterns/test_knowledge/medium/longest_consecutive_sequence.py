# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/longest-consecutive-sequence-medium

'''Problem:
Given an unsorted array of integers, find the length of the longest consecutive sequence of numbers in it.
A consecutive sequence means the numbers in the sequence are contiguous without any gaps.
For instance, 1, 2, 3, 4 is a consecutive sequence, but 1, 3, 4, 5 is not.

Input: [10, 11, 14, 12, 13]
Output: 5
Explanation: The entire array forms a consecutive sequence from 10 to 14.

Input: [3, 6, 4, 100, 101, 102]
Output: 3
Explanation: There are two consecutive sequences, [3, 4] and [100,101,102]. The latter has a maximum length of 3.

Input: [4, 3, 6, 2, 5, 8, 4, 7, 0, 1]
Output: 9
Explanation: The longest consecutive sequences here are [0, 1, 2,, 3, 4, 5, 6, 7, 8].

Input: [7, 8, 10, 11, 15]
Output: 2
Explanation: The longest consecutive sequences here are [7,8] and [10,11], both of length 2.
'''

# solution one using a set
# Complexity:
# O(n) time - where n is the length of the input list
# O(n) space - where n is the length of the input list (for the set)
class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        # we store number in a set for O(1) lookups
        num_set = set(nums)

        longest_sequence = count = 0

        # this loop will run for each number in the input list
        # but the time complexity is O(n) because we are not
        # looping (while loop) through the entire list for each number
        # we are only looping if the current number is the start of a sequence,
        # however, for the other numbers we are not doing anything
        for num in nums:
            # if the current number is the start of a sequence
            # meaning num - 1 is not in the set
            if num - 1 not in num_set:
                # start a new sequence
                count = 1

                # for each number that comes after the current number
                # increment the count by 1 if the number is in the set
                next_num = num + 1
                while next_num in num_set:
                    count += 1
                    next_num += 1

            longest_sequence = max(longest_sequence, count)

        return longest_sequence

# solution two using sorting
# Complexity:
# O(nlogn) time - where n is the length of the input list (for sorting)
# O(1) space
class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        # this is needed only if you set longest_sequence = 0
        # instead of longest_sequence = 1
        # if len(nums) == 1:
        #     return 1

        # sort the array first
        nums.sort()

        # check for the longest sequence where the current number is
        # equal to the previous number but incremented by 1
        longest_sequence = count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += 1
            else:
                # if the current number is not equal to the previous number
                # but incremented by 1, reset the count to 1
                count = 1

            longest_sequence = max(longest_sequence, count)

        return longest_sequence

