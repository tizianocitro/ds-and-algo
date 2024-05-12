# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a1cc3eccf84a14e3c8ec6f

'''Problem:
Given an unsorted array of numbers, find Kth smallest number in it.

Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

Input: [1, 5, 12, 2, 11, 5], K = 4
Output: 5
Explanation: The 4th smallest number is '5', as the first three small numbers are [1, 2, 5].

Input: [5, 12, 11, -1, 12], K = 3
Output: 11
Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].
'''

'''Note:
For a detailed discussion about different approaches to solve this problem,
take a look here: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63dc97ea680533006222f650,
but it will also be solved in a dedicated entry that will then be added here as a reference.
'''

# solution one
# Complexity:
# O(nlogk) time - where n is the length of the input array and k is the input k
# O(k) space - to store the heap
from heapq import *

class Solution:
    def findKthSmallestNumber(self, nums, k):
        max_heap = []
        # it takes O(klogk)
        for i in range(k):
            heappush(max_heap, -nums[i])

        # it takes (n-k)logk
        for i in range(k, len(nums)):
            num = nums[i]
            # since we want to keep track of the k smallest numbers,
            # we can compare every number with the top of the heap
            # while iterating through all numbers, and if it is smaller than the top,
            # we’ll take the top out and insert the smaller number,
            # this way the top of the heap will always have the kth smallest number
            if num <= -max_heap[0]:
                heappop(max_heap)
                heappush(max_heap, -num)      

        return -max_heap[0]

# solution two
# Complexity:
# O(n + klogn) time - where n is the length of the input array and k is the input k
# O(n) space - to store the heap
from heapq import *

class Solution:
    # insert all the numbers in the min-heap and then extract
    # the top k numbers from the heap to find the Kth smallest number
    def findKthSmallestNumber(self, nums, k):
        min_heap = nums

        heapify(min_heap)

        kth_min = heappop(min_heap)
        for _ in range(k - 1):
            kth_min = heappop(min_heap)

        return kth_min

# solution three
# Complexity:
# O(nlogn) time - where n is the length of the input array and k is the input k
# O(n) space - to store the heap
from heapq import *

class Solution:
    def findKthSmallestNumber(self, nums, k):
        min_heap = []
        # this takes O(nlogn)
        for n in nums:
            heappush(min_heap, n)

        # this takes O(klogn)
        kth_min = heappop(min_heap)
        for _ in range(k - 1):
            kth_min = heappop(min_heap)

        return kth_min
