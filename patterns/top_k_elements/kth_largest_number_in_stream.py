# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a1d25873a7d4466d4608f3

'''Problem:
Design a class to efficiently find the Kth largest element in a stream of numbers.

The class should have the following two things:
1. The constructor of the class should accept an integer array containing initial numbers from the stream and an integer k.
2. The class should expose a function add(int num) which will store the given number and return the Kth largest number.

It is guaranteed that there will be at least k elements in the array when you search for the kth element.

Input: [3, 1, 5, 12, 2, 11], k = 4
1. Calling add(6) should return '5'.
2. Calling add(13) should return '6'.
2. Calling add(4) should still return '6'.
'''

# solution one without assuming that k < len(nums) is always true
# Complexity:
# __init__() will take O(nlogk) time - as we have to add n elements to the heap
# add() will take O(logk) time - when we have to update the heap containing k elements
# _init_() will take O(k) space - where k is the input parameter as the heap will store k elements
# add() will take O(1) space
from heapq import *

class Solution:

    def __init__(self, nums, k):
        self.min_heap = []
        self.k = k

        # add the numbers in the min heap
        for num in nums:
            self.add(num)

    def add(self, num):
        # add the new number in the min heap
        heappush(self.min_heap, num)

        # if heap has more than k numbers, remove one number
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)

        # return the kth largest number
        return self.min_heap[0]

# solution two assuming that k < len(nums) is always true compared to solution one
# Complexity:
# __init__() will take O(nlogk) time - as we have to add n elements to the heap
# add() will take O(logk) time - when we have to update the heap containing k elements
# _init_() will take O(k) space - where k is the input parameter as the heap will store k elements
# add() will take O(1) space
from heapq import *

class Solution:

    def __init__(self, nums, k):
        # this min hap will store the kth largest numbers
        # so it will always have k elements and the top
        # element will be the kth largest number
        self.min_heap = []

        for i in range(k):
            heappush(self.min_heap, nums[i])

        for i in range(k, len(nums)):
            self.add(nums[i])

    def add(self, num):
        # update the min heap if the incoming number is larger than
        # the smallest number in the heap, which means we have
        # to update the kth largest number at the top of the heap
        if num > self.min_heap[0]:
            heappop(self.min_heap)
            heappush(self.min_heap, num)

        # the top element will always be the kth largest number
        return self.min_heap[0]