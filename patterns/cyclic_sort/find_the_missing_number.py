# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6393ab5cd8a93f4bff961bc7

'''Problem:
We are given an array containing n distinct numbers taken from the range 0 to n.
Since the array has only n numbers out of the total n + 1 numbers, find the missing number.

Input: [4, 0, 3, 1]
Output: 2
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input array
# O(1) space
class Solution:
    def findMissingNumber(self, nums):
        n = len(nums)
        i, missingNumber = 0, n
        while i < n:
            num = nums[i]
            if num < n and i != num:
                nums[i], nums[num] = nums[num], nums[i]
                continue
            if num >= n:
                missingNumber = i
            i +=1
        return missingNumber

# solution two
# Complexity:
# O(n) time - where n is the length of the input array
# O(1) space
class Solution:
    def findMissingNumber(self, nums):
        i, n = 0, len(nums)
        while i < n:
            j = nums[i]
            if nums[i] < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        # find the first number missing from its index, that will be our required number
        for i in range(n):
            if nums[i] != i:
                return i

        return n