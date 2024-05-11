# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a1c9d019e6a3ce13cedb21

'''Problem:
Given an unsorted array of numbers, find the k largest numbers in it.
Consider that k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Input: [3, 1, 5, 12, 2, 11], k = 3
Output: [5, 12, 11]

Input: [5, 12, 11, -1, 12], k = 3
Output: [12, 11, 12]
'''

# solution one
# Complexity:
# O(nlogk) - where n is the number of numbers in nums
# it is O(klogk + (n-k)logk) but n > k, so O(nlogk)
# O(k) space - where k is the number of numbers we will keep in the heap
from heapq import *

class Solution:
    def findKLargestNumbers(self, nums, k):
        min_heap = []

        # put first k numbers in the min heap
        for i in range(k):
            heappush(min_heap, nums[i])

        # go through the remaining numbers of the array, if the number from the array
        # is bigger than the top (i.e., the smallest) number of the min-heap,
        # remove the top number from heap and add the number from the array
        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, nums[i])

        # the heap has the top k numbers
        return min_heap

# solution two
# Complexity:
# O(nlogn) - where n is the number of numbers in nums
# it is O(nlogn + klogn) but n > k, so O(nlogn)
# O(n) space - where n is the number of numbers in nums
from heapq import *

class Solution :
    def findKLargestNumbers(self, nums, k):
        max_heap = []

        # this takes O(nlogn) because we need to push all the n numbers
        # in the heap, which will take O(nlogn) because heappush takes O(logn)
        for num in nums:
            heappush(max_heap, -num)

        # this takes O(klogn) because we need to get the top of the heap,
        # which takes O(logn) since the heap contains n numbers,
        # and we need to get the top k times, so O(klogn)
        return [-heappop(max_heap) for _ in range(k)]
