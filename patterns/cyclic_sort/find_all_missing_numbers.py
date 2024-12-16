# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63dd93fe61dc5307bdb75cd6

'''Problem:
We are given an unsorted array containing numbers taken from the range 1 to n.
The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input array
# O(n) space - where n is the length of the input array
class Solution:
    def findNumbers(self, nums):
        missingNumbers = []
        i, n = 0, len(nums)

        while i < n:
            # current number
            num = nums[i]
            # the index num should be
            j = nums[i] - 1

            if num != nums[j]:
                nums[j], nums[i] = nums[i], nums[j]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                missingNumbers.append(i + 1)

        return missingNumbers

# solution two
# Complexity:
# O(n) time - where n is the length of the input array
# O(n) space - where n is the length of the input array
class Solution:
    def findNumbers(self, nums):
        missingNumbers = []
        i, n = 0, len(nums)

        while i < n:
            # current number
            num = nums[i]
            # the index num should be
            j = nums[i] - 1

            # if the number is the number is not at the index it should be
            # and the number is not a duplicate, meaning that at the correct index
            # there is a different number
            if num != nums[j] and i != j:
                nums[j], nums[i] = nums[i], nums[j]
            else:
                i += 1

        for i in range(n):
            # identify elements that are not in their correct positions, where are missing numbers
            if nums[i] != i + 1:
                missingNumbers.append(i + 1)

        return missingNumbers
