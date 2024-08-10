# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6393b0a334689e585e94a29a

'''Problem:
We are given an unsorted array containing n numbers taken from the range 1 to n.
The array has some numbers appearing twice, find all these duplicate numbers
using constant space (the space for the duplicatedNumbers list is not considered).

Input: [3, 4, 4, 5, 5]
Output: [4, 5]
'''

# solution one with one loop
# Complexity:
# O(n) time - where n is the length of the input array
# O(1) space
class Solution:
    def findNumbers(self, nums):
        duplicateNumbers = []
        i = 0
        while i < len(nums):
            num = nums[i]
            j = num - 1
            if num != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                continue
            
            if i != j:
                duplicateNumbers.append(num)
            
            i += 1
        return duplicateNumbers

# solution two with two loops
# Complexity:
# O(n) time - where n is the length of the input array
# O(1) space
class Solution:
    def findNumbers(self, nums):
        i = 0
        while i < len(nums):
            # calculate the index where the current element should be if it's not a duplicate
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        duplicateNumbers = []

        for i in range(len(nums)):
            # identify elements that are not in their correct positions, which are duplicates.
            if nums[i] != i + 1:
                duplicateNumbers.append(nums[i])

        return duplicateNumbers