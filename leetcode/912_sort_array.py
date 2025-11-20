# !code: 912, !difficulty: medium, !from: https://leetcode.com/problems/sort-an-array/

'''Problem:
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in
O(nlog(n)) time complexity and with the smallest space complexity possible.

Constraints:
- 1 <= nums.length <= 5 * 10^4
- -5 * 10^4 <= nums[i] <= 5 * 10^4

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3),
while the positions of other numbers are changed (for example, 1 and 5).

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
'''

# solution one using merge sort
# Complexity:
# O(nlogn) time - where n is the length of the input list
# O(n) space - because we are creating a new list to store the sorted list
class Solution:
    def sortArray(self, nums):
        cloned_nums = nums[:]
        self.mergeSort(nums, cloned_nums, 0, len(nums))
        return cloned_nums

    def mergeSort(self, main_nums, cloned_nums, low, high):
        if high - low <= 1:
            return

        middle = (low + high) // 2
        self.mergeSort(cloned_nums, main_nums, low, middle)
        self.mergeSort(cloned_nums, main_nums, middle, high)

        i = low
        j = middle
        k = low
        while i < middle and j < high:
            if main_nums[i] < main_nums[j]:
                cloned_nums[k] = main_nums[i]
                i += 1
            else:
                cloned_nums[k] = main_nums[j]
                j += 1
            k += 1

        while i < middle:
            cloned_nums[k] = main_nums[i]
            i += 1
            k += 1

        while j < high:
            cloned_nums[k] = main_nums[j]
            j += 1
            k += 1

# solution two using quick sort
# Complexity:
# O(nlogn) time - where n is the length of the input list
# O(n) space - because we are creating a new list to store the sorted list
class Solution:
    def sortArray(self, nums):
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, low, high):
        if low >= high:
            return

        pivot_ix = self.partition(nums, low, high)

        # the pivot is already in the right place, so
        # we don't need to include it in the next calls
        self.quickSort(nums, low, pivot_ix - 1)
        self.quickSort(nums, pivot_ix + 1, high)

    def partition(self, nums, low, high):
        if low >= high:
            return low

        # here you could use different approaches to select the pivot
        # e.g., median of medians, random pivot, etc.
        # for more information, check the solutions in sorting/quick_sort.py
        pivot = nums[high]

        for i in range(low, high):
            if nums[i] < pivot:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1

        # put the pivot in its right place, which is at the index 'low'
        nums[high], nums[low] = nums[low], nums[high]
        return low
