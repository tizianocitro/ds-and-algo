# !difficulty: medium

''' Problem:
Also called the 'three-way partitioning' problem.

Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects,
hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue;
and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]
'''

# solution one
# Complexity:
# O(n) time - where n is the length of the array,
# because the first for loop iterates only three times, thus it's constant time
# O(1) space
class Solution:
    def sort(self, arr):
        nums = [0, 1, 2]
        i = 0
        for n in nums:
            while i < len(arr) and arr[i] == n:
                i += 1
            for j in range(i, len(arr)):
                if arr[j] == n:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
        return arr

# solution two
# Complexity:
# O(n) time - where n is the length of the array,
# O(1) space
'''
We use two pointers called low and high, which are pointing to the first and the last element of the array respectively.
While iterating, we move all 0s before low and all 2s after high so that in the end,
all 1s will be between low and high. In the end, all 0s are on the left, all 1s are in the middle, and all 2s are on the right.
'''
class Solution:
    def sort(self, arr):
        low, high = 0, len(arr) - 1
        i = low
        while i <= high:
            current = arr[i]
            if current == 2:
                arr[i], arr[high] = arr[high], arr[i]
                high -= 1 
                continue
            if current == 0:
                arr[i], arr[low] = arr[low], arr[i]
                low += 1
            i += 1
        return arr
