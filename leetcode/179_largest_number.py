# !code: 179, !difficulty: medium, !from: https://leetcode.com/problems/largest-number/

'''Problem:
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Input: nums = [10,2]
Output: "210"

Input: nums = [3,30,34,5,9]
Output: "9534330"

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 10^9
'''

# solution one using custom comparator
# Complexity:
# O(nlogn) time - where n is the length of the array because we sort the array
# O(n + s) space - where n is the length of the array because we create a new array of strings
# and also s is the length of the result string
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums) -> str:
        # convert the numbers to strings because we need it
        # for comparison and also to join them at the end
        num_strings = [str(num) for num in nums]

        # sort with the custom comparator
        num_strings.sort(key=cmp_to_key(self.highest_combination))

        result = ''.join(num_strings)

        # if the result is only zeros, we don't want to return '00...0' but '0'
        return '0' if result[0] == '0' else result

    # sort the numbers based on whether their combination is higher
    # in one verse or the other, e.g. num1 = 3 and num2 = 30,
    # 3 should come before 30 because 330 > 303
    def highest_combination(self, num1, num2):
        if num1 + num2 > num2 + num1:
            # num1 should come before num2
            return -1
        else:
            # num2 should come before num1
            return 1

# solution two using quick sort and custom comparator
# Complexity:
# O(nlogn) time - where n is the length of the array because we sort the array
# complexity of quick sort is O(nlogn) in the average case, and O(n^2) in the worst case
# O(n + s) space - where n is the length of the array because we create a new array of strings
# and also s is the length of the result string
class Solution:
    def largestNumber(self, nums) -> str:
        self.quickSort(nums, 0, len(nums) - 1)

        result = ''.join([str(num) for num in nums])

        # if the result is only zeros, we don't want to return '00...0' but '0'
        return '0' if result[0] == '0' else result

    def quickSort(self, nums, low, high):
        if low >= high:
            return

        pivot_ix = self.partition(nums, low, high)
        self.quickSort(nums, low, pivot_ix - 1)
        self.quickSort(nums, pivot_ix + 1, high)

    def partition(self, nums, low, high):
        if low == high:
            return low

        # the pivot here is chosen using lamuto partition scheme
        pivot = nums[high]
        for i in range(low, high):
            # sort using the custom comparator
            if self.highest_combination(nums[i], pivot):
                nums[i], nums[low] = nums[low], nums[i]
                low += 1

        nums[high], nums[low] = nums[low], nums[high]
        return low

    # custom comparator: we want num1 to come before the pivot
    # if num1 + pivot > pivot + num1
    def highest_combination(self, num1, num2):
        num1_str, num2_str = str(num1), str(num2)
        return num1_str + num2_str > num2_str + num1_str
