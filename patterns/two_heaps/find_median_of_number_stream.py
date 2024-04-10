# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639b685c5cda0fa79d72b471

'''Problem:
Design a class to calculate the median of a number stream.
The class should have the following two methods:
    1. insertNum(int num): stores the number in the class
    2. findMedian(): returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

Example:
    1. insertNum(3)
    2. insertNum(1)
    3. findMedian() -> output: 2
    4. insertNum(5)
    5. findMedian() -> output: 3
    6. insertNum(4)
    7. findMedian() -> output: 3.5
'''

# solutione one using two heaps
# Complexity:
# O(logn) time - where n is the number of elements in the stream, due to the insertion in the heap
# O(n) space - where n is the number of elements in the stream, to store the numbers in the heaps
from heapq import *

class Solution:

    def __init__(self):
        # containing first half of numbers
        self.maxHeap = []
        # containing second half of numbers
        self.minHeap = []

    def insertNum(self, num):
        # if the top of the maxHeap is greater than the top of the number,
        # then we need to push the number to the maxHeap, because it will be
        # in the first half of the numbers, which contains the smaller numbers
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        # either both the heaps will have equal number of elements or max-heap
        # will have one more element than the min-heap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
            # we have even number of elements, take the average of middle two elements
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0

        # because max-heap will have one more element than the min-heap
        return -self.maxHeap[0] / 1.0

