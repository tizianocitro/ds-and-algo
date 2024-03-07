# !difficulty: medium

''' Problem:
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

Input: [4, 1, 2, -1, 1, -3], target = 1
Output: [[-3, -1, 1, 4], [-3, 1, 1, 2]]
'''

# solution one
# Complexity:
# O(n^3) time - where n is the length of the input array
# O(n) space - for sorting
class Solution:
    def searchQuadruplets(self, arr, target):
        arr.sort()
        quadruplets = []
        for i in range(len(arr) - 3):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
        for j in range(i + 1, len(arr) - 2):
            if arr[j] == arr[j - 1]:
                continue
            self.searchPair(arr, quadruplets, target, i, j)
        return quadruplets

    def searchPair(self, arr, quadruplets, target, i, j):
        left = j + 1
        right = len(arr) - 1
        sum = arr[i] + arr[j]
        while left < right:
            sum = arr[i] + arr[j] + arr[left] + arr[right]
            if sum == target:
                quadruplets.append([arr[i], arr[j], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            if sum > target:
                right -= 1
            else:
                left += 1

