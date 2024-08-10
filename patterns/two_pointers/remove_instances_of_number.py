# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63dda4ad488110f74a93371d

''' Problem:
Given an unsorted array of numbers and a target key,
remove all instances of key in-place and return the new length of the array.

Input: [3, 2, 3, 6, 3, 10, 9, 3], key = 3
Output: 4 // The first four elements after removing every instance of key will be [2, 6, 10, 9]
'''

# solution one
# Complexity:
# O(n) time - where n is the size of the array
# O(1) space
class Solution:
    def remove(self, arr, key):
        nextElement = 0

        for i in range(len(arr)):
            if arr[i] != key:
                arr[nextElement] = arr[i]
                nextElement += 1

        return nextElement