# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/638f6ff2ae53511bdc36490d

''' Problem:
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
'''

# solution one
# Complexity:
# O(n^2) time - where n is the size of the array
# O(n) space - where n is the size of the array
class Solution:
    def searchTriplets(self, arr):
        triplets = []
        arr.sort()
        for i, n in enumerate(arr):
            if i > 0 and n == arr[i - 1]:
                continue
            self.searchPair(arr, triplets, i + 1, len(arr) - 1, -n)
        return triplets

    def searchPair(self, arr, triplets, left, right, target):
        while left <= right:
            l, r = arr[left], arr[right]
            sum = l + r
            if sum == target:
                triplets.append([l, r, -target])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1  # skip same element to avoid duplicate triplets
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1  # skip same element to avoid duplicate triplets
            if sum > target:
                right -= 1
            else:
                left += 1