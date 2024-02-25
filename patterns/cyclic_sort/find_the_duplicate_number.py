# !difficulty: easy

'''Problem:
We are given an unsorted array containing n + 1 numbers taken from the range 1 to n.
The array has only one duplicate but it can be repeated multiple times.
Find that duplicate number without using any extra space and with the possibility to modify the input array.

Input: [1, 4, 4, 3, 2]
Output: 4
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the input array
# O(1) space
class Solution:
    def findNumber(self, nums):
        i = 0
        while i in range(len(nums)):
            num = nums[i]
            j = num - 1
            if num != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                continue

            # the two numbers are the same, otherwise we would have swapped them and moved to the next index
            # the indexes are different, so we have found the duplicate number because the number is the same at two different indexes
            if i != j:
                return num
            
            i += 1
        return -1