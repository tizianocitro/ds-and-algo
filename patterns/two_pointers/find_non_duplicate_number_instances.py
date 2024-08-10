# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/638e33feac0cc8a9358a25ac

''' Problem:
Given an array of sorted numbers, move all non-duplicate number instances at the beginning of the array in-place.
The relative order of the elements should be kept the same and you should not use any extra space so that the solution has constant space complexity i.e., O(1).
Move all the unique number instances at the beginning of the array and after moving return the length of the subarray that has no duplicate in it.

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4 // The first four elements after removing the duplicates will be [2, 3, 6, 9]
'''

# solution one
# Complexity:
# O(n) time - where n is the size of the array
# O(1) space
class Solution:
    def remove(self, arr):
        next_non_duplicate, i = 1, 1

        while i < len(arr):
            # Check if the current element is different from the previous element
            if arr[next_non_duplicate - 1] != arr[i]:
                # If different, update the next_non_duplicate element and copy the current element
                # and then update the next_non_duplicate element index
                arr[next_non_duplicate] = arr[i]
                next_non_duplicate += 1
            i += 1

        return next_non_duplicate
