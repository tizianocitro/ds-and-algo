# !difficulty: medium, !from: 

'''Problem:
Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.

Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
Output: 23
Explanation: The 3rd smallest number is 5 and 6th smallest number 15. The sum of numbers coming
between 5 and 15 is 23 (11+12).

Input: [3, 5, 8, 7], and K1=1, K2=4
Output: 12
Explanation: The sum of the numbers between the 1st smallest number (3) and the 4th smallest 
number (8) is 12 (5+7).
'''

# solution one
# Complexity:
# O(k2logk2) time - where k2 is the input parameter
# O(k2) space - because we keep k2 elements in the heap
from heapq import *

class Solution:
    def findSumOfElements(self, nums, k1, k2):
        max_heap = []
        # we keep k2 smallest numbers in the max heap,
        # this will require us to remove the top of the heap
        # before starting to pop the elements between k1 and k2
        for i in range(k2):
            heappush(max_heap, -nums[i])

        for i in range(k2, len(nums)):
            num = nums[i]
            if num < -max_heap[0]:
                heappop(max_heap)
                heappush(max_heap, -num)

        element_sum = 0
        # we need to remove the top of the heap because it is 
        # the k2th smallest number and we do not want to count it
        heappop(max_heap)
        # get the sum of numbers between k1 and k2 indices
        # these numbers will be at the top of the max heap
        for _ in range(k2 - k1 - 1):
            num = heappop(max_heap)
            element_sum += -num

        return element_sum

# solution two identical to solution one but
# with k - 1 elements in the heap to avoid the heappop() call
# that is made before starting to pop the elements between k1 and k2
# Complexity:
# O(k2logk2) time - where k2 is the input parameter
# O(k2) space - because we keep k2 - 1 elements in the heap
from heapq import *

class Solution:
    def findSumOfElements(self, nums, k1, k2):
        max_heap = []

        # keep smallest k2 - 1 numbers in the max heap,
        # this allows to avoid a call to heappop() before
        # starting to pop the elements between k1 and k2
        for i in range(k2 - 1):
            heappush(max_heap, -nums[i])

        # since we are keeping k2 - 1 elements in the heap
        # we need to start looping elements from k2 - 1 index
        for i in range(k2 - 1, len(nums)):
            num = nums[i]
            if num < -max_heap[0]:
                heappop(max_heap)
                heappush(max_heap, -num)

        element_sum = 0
        # get the sum of numbers between k1 and k2 indices
        # these numbers will be at the top of the max heap
        for _ in range(k2 - k1 - 1):
            num = heappop(max_heap)
            element_sum += -num

        return element_sum

# solution three identical to solution two but
# with a slightly different approach when building the heap
# Complexity:
# Complexity:
# O(k2logk2) time - where k2 is the input parameter
# O(k2) space - because we keep k2 - 1 elements in the heap
from heapq import *

class Solution:
    def findSumOfElements(self, nums, k1, k2):
        maxHeap = []
        # keep smallest k2 - 1 numbers in the max heap
        # this is an equivalent way to using two loops
        # like seen in the previous two solutions
        for i in range(len(nums)):
            if i < k2 - 1:
                heappush(maxHeap, -nums[i])
            elif nums[i] < -maxHeap[0]:
                heappop(maxHeap)
                heappush(maxHeap, -nums[i])

            # get the sum of numbers between k1 and k2 indices
            # these numbers will be at the top of the max heap
            element_sum = 0
            for _ in range(k2 - k1 - 1):
                element_sum += -heappop(maxHeap)

        return element_sum

# solution four using a min heap
# this has worse time and space complexity than the previous solutions
# Complexity:
# O(nlogn) time - where n is the length of the input array
# O(n) space - because we keep all elements in the heap
from heapq import *

class Solution:
    def findSumOfElements(self, nums, k1, k2):
        min_heap = []
        # insert all numbers to the min heap
        for num in nums:
            heappush(min_heap, num)

        # remove k1 small numbers from the min heap
        # so the next k2 - k1 - 1 numbers will be the ones
        # between k1th and k2th smallest numbers
        for _ in range(k1):
            heappop(min_heap)

        element_sum = 0
        # sum next k2 - k1 - 1 numbers
        for _ in range(k2 - k1 - 1):
            element_sum += heappop(min_heap)

        return element_sum
