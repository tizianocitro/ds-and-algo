# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a38552b33a04fe1cc698a5

'''Problem:
Given two sorted arrays in descending order, find K pairs with the largest sum where each pair consists of numbers from both the arrays.
Given k <= nums1.length * nums2.length.

Input: nums1=[9, 8, 2], nums2=[6, 3, 1], K=3
Output: [9, 3], [9, 6], [8, 6] 
Explanation: These 3 pairs have the largest sum. No other pair has a sum larger than any of these.

Input: nums1=[5, 2, 1], nums2=[2, -1], K=3
Output: [5, 2], [5, -1], [2, 2]
'''

'''Solution:
We can go through all the numbers of the two input arrays to create pairs
and initially insert them all in the heap until we have K pairs in min heap
after that, if a pair is bigger than the top (smallest) pair in the heap,
we can remove the smallest pair and insert this pair in the heap

We can optimize our algorithms in two ways:
1. Instead of iterating over all the numbers of both arrays,
   we can iterate only the first K numbers from both arrays.
   Since the arrays are sorted in descending order, the pairs with the maximum sum
   will be constituted by the first K numbers from both the arrays.
2. As soon as we encounter a pair with a sum that is smaller than
   the smallest (top) element of the heap, we don’t need to process the next elements of the array.
   Since the arrays are sorted in descending order,
   we won’t be able to find a pair with a higher sum moving forward
'''

# solution one
# Complexity:
# O(nmlogk) time or O(k^2logk) - where n and m are the total number of elements in both arrays
# and k is the input parameter. However, since k <= n and k <= m, we can say that 
# if both arrays have at least k elements, the time complexity can be simplified to O(k^2logk)
# O(k) space - where k is the input parameter for the heap
from heapq import *

class Solution:
    def findKLargestPairs(self, nums1, nums2, k):
        min_heap = []

        # instead of iterating over all the numbers of both arrays, we can iterate
        # only the first K numbers from both arrays. Since the arrays are sorted in descending order,
        # the pairs with the maximum sum will be constituted by the first K numbers from both the arrays
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                # fill the heap with the first k pairs
                if len(min_heap) < k:
                    heappush(min_heap, (nums1[i] + nums2[j], i, j))
                else:
                    # if the sum of the two numbers from the two arrays is smaller than the 
                    # smallest(top) element of the heap, we can 'break' here. Since the arrays are 
                    # sorted in the descending order, we'll not be able to find a pair with a higher 
                    # sum moving forward
                    if nums1[i] + nums2[j] < min_heap[0][0]:
                        break
                    else: # we've a pair with a larger sum, remove top and insert this pair in heap
                        heappop(min_heap)
                        heappush(min_heap, (nums1[i] + nums2[j], i, j))

        result = []
        for (_, i, j) in min_heap:
            result.append([nums1[i], nums2[j]])
        return result