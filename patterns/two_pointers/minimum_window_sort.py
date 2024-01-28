# !difficulty: medium

''' Problem:
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5

Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5 // We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted because the minimum is -1.
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the array
# O(1) space
class Solution:
    def sort(self, arr):
        low, high = 0, len(arr) - 1
        while low < len(arr) - 1 and arr[low] <= arr[low + 1]:
            low += 1
            if low == len(arr) - 1: # the array is already sorted
                return 0
        while high > 0 and arr[high] >= arr[high - 1]:
            high -= 1

        min, max = low, high
        for k in range(low, high + 1):
            if arr[k] < arr[min]:
                min = k
            if arr[k] > arr[max]:
                max = k

        # this s an alternative to the while with the low var
        # but your have to use return high - low at the end
        # i = 0
        # while i < low and arr[i] < arr[min]:
        #    i += 1
        while low > 0 and arr[low - 1] > arr[min]:
            low -= 1
        while high <= len(arr) - 1 and arr[high] < arr[max]:
            high += 1
        
        return high - low
    

