# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639f2d925efa22c27557acf2

'''Problem:
Given an infinite sorted array (or an array with unknown size), find if a given number key is present in the array.
Write a function to return the index of the key if it is present in the array, otherwise return -1.

Since it is not possible to define an array with infinite (unknown) size,
you will be provided with an interface ArrayReader to read elements of the array.
ArrayReader.get(index) will return the number at index;
if the array’s size is smaller than the index, it will return Integer.MAX_VALUE.

Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 16
Output: 6
Explanation: The key is present at index 6 in the array.

Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 11
Output: -1
Explanation: The key is not present in the array.
'''

'''Solution:
Since Binary Search helps us find a number in a sorted array efficiently,
we can use a modified version of the Binary Search to find the key in an infinite sorted array.

The only issue with applying binary search in this problem is that we don’t know the bounds of the array.
To handle this situation, we will first find the proper bounds of the array where we can perform a binary search.

An efficient way to find the proper bounds is to start at the beginning of the array with the bound’s size as 1
and exponentially increase the bound’s size (i.e., double it) until we find the bounds that can have the key.
'''

# solution one - find the bounds and then do binary search
# Complexity:
# O(logn + logn) time - where n is the number of elements in the array
# There are two parts of the algorithm. In the first part, we keep increasing the bound’s size exponentially (double it every time)
# while searching for the proper bounds. Therefore, this step will take O(logn) assuming that the array will have maximum n numbers.
# In the second step, we perform the binary search which will take O(logn) as well
# O(1) space
import math

class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]

class Solution:
    def searchInfiniteSortedArray(self, reader, key):
        left, right = 0, 1

        # we are finding the bounds by doubling the right index each time,
        # so the time complexity of this loop is O(logn)
        while reader.get(right) < key:
            next_left = right + 1
            right += (right - left + 1) * 2
            left = next_left

        return self.binarySearch(reader, key, left, right)

    def binarySearch(self, reader, key, left, right):
        while left <= right:
            middle = (left + right) // 2
            current = reader.get(middle)

            if current == key:
                return middle
            
            if current > key:
                right = middle - 1
            else:
                left = middle + 1

        return -1

# solution two
# Complexity:
# O(n) time - where n is the number of elements in the array
# O(1) space
import math

class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]

class Solution:
    def searchInfiniteSortedArray(self, reader, key):
        i = 0

        while True:
            current = reader.get(i)
            if current == math.inf:
                break

            if current == key:
                return i

            if current > key:
                break

            i += 1

        return -1
