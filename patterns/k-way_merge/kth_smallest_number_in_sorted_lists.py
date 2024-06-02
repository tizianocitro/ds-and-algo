# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a376b4a41249d4abecb716

'''Problem:
Given M sorted arrays, find the K’th smallest number among all the arrays.

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, this can be verified from 
the merged list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]

Input: L1=[5, 8, 9], L2=[1, 7], K=3
Output: 7
Explanation: The 3rd smallest number among all the arrays is 7.
'''

# solution one
# Complexity:
# O(mlogm + klogm) time - where m is the number of lists and k is the input k
# however, since m <= k, the time complexity can be simplified to O(klogm)
# O(m) space - to store the min heap
from heapq import *

class Solution:
    def findKthSmallest(self, lists, k):
        min_heap = []
        # push the first element of each list into the heap
        # each element of the heap is a tuple of (number, list_index, next_element_index)
        for i, l in enumerate(lists):
            # if the list is not empty, push the first element of the list
            if len(l) > 0:
                heappush(min_heap, (l[0], i, 1))

        # take the smallest (top) element from the min heap,
        # at the end of the kth iteration, kth_min_num will be
        # the kth smallest element in all the lists
        kth_min_num = 0
        for i in range(k):
            # if there are no more elements, return -1
            # because we have less than k elements in all the lists
            if not min_heap:
                return -1

            # pop the ith smallest element from the min heap
            # if the next element exists, push it to the heap
            ith_min_num, ith_list, ith_ix = heappop(min_heap)
            if ith_ix < len(lists[ith_list]):
                next_num = lists[ith_list][ith_ix]
                heappush(min_heap, (next_num, ith_list, ith_ix + 1))

            # update the kth smallest number
            kth_min_num = ith_min_num

        return kth_min_num

# solution two
# Complexity:
# O(mlogm + klogm) time - where m is the number of lists and k is the input k
# however, since m <= k, the time complexity can be simplified to O(klogm)
# O(m) space - to store the min heap
from heapq import *

class Solution:
    def findKthSmallest(self, lists, k):
        min_heap = []
        # push the first element of each list into the heap
        # each element of the heap is a tuple of (number, list_index, next_element_index)
        for i, l in enumerate(lists):
            # if the list is not empty, push the first element of the list
            if len(l) > 0:
                heappush(min_heap, (l[0], i, 1))

        # take the smallest (top) element from the min heap,
        # at the end of the kth iteration, the top of the heap
        # will be the kth smallest element in all the lists
        for i in range(k):
            # if there are no more elements, return -1
            # because we have less than k elements in all the lists
            if not min_heap:
                return -1

            # pop the ith smallest element from the min heap
            # if the next element exists, push it to the heap
            _, ith_list, ith_ix = heappop(min_heap)
            if ith_ix < len(lists[ith_list]):
                next_num = lists[ith_list][ith_ix]
                heappush(min_heap, (next_num, ith_list, ith_ix + 1))

        # return min_heap[0][0] if min_heap else -1 is another way
        # to return the kth smallest number at the top of the heap
        return heappop(min_heap)[0] if min_heap else -1

# solution three
# Complexity:
# O(mlogm + klogm) time - where m is the number of lists and k is the input k
# however, since m <= k, the time complexity can be simplified to O(klogm)
# O(m) space - to store the min heap
from heapq import *

class Solution:
    def findKthSmallest(self, lists, k):
        min_heap = []

        # put the 1st element of each list in the min heap
        for i in range(len(lists)):
            heappush(min_heap, (lists[i][0], 0, lists[i]))

        # take the smallest (top) element form the min heap,
        # if the running count is equal to k, return the number
        number_count, kth_min_num = 0, 0
        while min_heap:
            kth_min_num, i, list = heappop(min_heap)
            number_count += 1
            if number_count == k:
                break

            # if the array of the top element has more elements,
            # add the next element to the heap
            if len(list) > i+1:
                heappush(min_heap, (list[i+1], i+1, list))

        return kth_min_num