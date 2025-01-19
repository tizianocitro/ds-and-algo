# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/longest-continuous-subarray-medium

'''Problem:
Find the length of the longest contiguous subarray within an array of integers,
where the absolute difference between any two elements in this subarray does not exceed a specified limit.
The challenge lies in ensuring the subarray is continuous and the range
(difference between the maximum and minimum element in the subarray) fits within the given threshold.

Input: Array = [10, 1, 2, 4, 7], Limit = 5
Output: 3
Explanation: The longest subarray where the absolute difference between any two numbers is at most 5 is [1, 2, 4].

Input: Array = [4, 8, 5, 1, 7, 9], Limit = 3
Output: 2
Explanation: One possible longest subarray is [7, 9] where the difference between 7 and 9 is within the limit of 3.

Input: Array = [3, 3, 3, 3, 3], Limit = 0
Output: 5
Explanation: Since all elements are the same, the entire array is the longest subarray with differences of 0.
'''

# solution one using sliding window
# O(n^2) time - where n is the length of the input array, because we are iterating
# over all the elements of the array, and, in the worst case, we might need to shrink the
# size of the window for each two elements or for n - 1 elements if the last element fails the condition
# O(n) space - where n is the length of the input array, because in case all elements are unique and
# they meet the condition, we will have to store all of them in the window 
class Solution:
    def longestSubarray(self, nums, limit):
        max_length = 0
        # store the frequency of each number in the window
        # the map will also be the window itself
        freq = {}
        # start of the window for the next element to remove
        # and keep the window updated
        start = 0

        # for each number in the array along with its index
        for end, num in enumerate(nums):
            # increment the frequency of the number
            freq[num] = freq.get(num, 0) + 1

            # while the difference between the maximum and minimum numbers
            # in the window (represented by the map) is greater than the limit
            # we need to shrink the window by removing the start element
            # we always move the start to the right because we want to delete
            # the leftmost element in the window every time
            while max(freq.keys()) - min(freq.keys()) > limit:
                # decrease the frequency of the start element
                # and remove it from the freq map if it becomes zero
                freq[nums[start]] -= 1
                if freq[nums[start]] == 0:
                    del freq[nums[start]]
                # always delete the leftmost element in the window
                start += 1

            # update the maximum length of the window
            max_length = max(max_length, end - start + 1)

        return max_length
