# !code: 4, !difficulty: hard, !from: https://leetcode.com/problems/median-of-two-sorted-arrays/description/

'''Problem:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Constraints:
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -106 <= nums1[i], nums2[i] <= 106

Follow Up Question:
What if the overall time complexity should be O(log (m+n))?

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''

'''Notes:
Useful explanation at https://www.youtube.com/watch?v=q6IEA26hvXc (neetcode yt).
'''

# solution one using binary search
# Complexity:
# O(log(min(m, n))) time - where m and n are the lengths of the two lists
# O(1) space
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        a, b = nums1, nums2
        # the total is needed because we need to check whether we have to
        # calculate the median for an even or an odd number of elements
        total = len(a) + len(b)
        # half is needed to efficiently calculate the index equivalent
        # to the middle element in array 'a' but in the array 'b'
        half = total // 2

        # always do binary search on the shortest of the two array
        # of it b is shorter than a, swap them
        if len(b) < len(a):
            a, b = b, a

        # left and right are the pointers for the binary search in array 'a'
        left, right = 0, len(a) - 1

        # there will always be a median so we will always return
        while True:
            a_middle = (left + right) // 2
            # - 2 because a_middle starts from zero and also b_middle should
            # start from 0, but half starts from 1 since it comes from the len()
            b_middle = half - a_middle - 2

            # get the right-most element of the left partition
            # and the left-most element of the right partition
            # but ensure they are not out of bounds, otherwise use infinity
            a_left = a[a_middle] if a_middle >= 0 else float('-inf')
            a_right = a[a_middle + 1] if a_middle + 1 < len(a) else float('inf')
            b_left = b[b_middle] if b_middle >= 0 else float('-inf')
            b_right = b[b_middle + 1] if b_middle + 1 < len(b) else float('inf')

            if a_left <= b_right and b_left <= a_right:
                # if the total number of elements is odd,
                # return the smaller of the two right-most elements
                if total % 2 != 0:
                    return min(a_right, b_right)
                # otherwise, return the average of the smaller of the two right-most elements
                # and the larger of the two left-most elements
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                # the partition is too far to the right in array 'a', so move left
                right = a_middle - 1
            else: # b_left > a_right
                # the partition is too far to the left in array 'a', so move right
                left = a_middle + 1

# solution two using k-way merge with min heap
# Complexity:
# O(nlogk) tiem - where k is the total number of elements in the two lists and n is the median position
# O(k) space - for the min heap
from heapq import *

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        min_heap = []

        # create a list of the two lists
        lists = [nums1, nums2]

        # push the first element of each list into the heap
        # each element of the heap is a tuple of (number, list_index, next_element_index)
        for i, l in enumerate(lists):
            # if the list is not empty, push the first element of the list
            if len(l) > 0:
                heappush(min_heap, (l[0], i, 1))

        # find median position and if the total number of elements is even
        total_elements = len(nums1) + len(nums2)
        median_pos = total_elements // 2
        is_even_len = total_elements % 2 == 0

        median = 0
        for i in range(median_pos + 1):
            # pop the ith element from the min heap and
            # if the next element exists, push it to the heap
            ith_num, ith_list, next_num_ix = heappop(min_heap)
            if next_num_ix < len(lists[ith_list]):
                next_num = lists[ith_list][next_num_ix]
                heappush(min_heap, (next_num, ith_list, next_num_ix + 1))

            # if it is even length and i (current iteration) is the median position
            # then calculate the median as the average of the ith number and
            # the previous median (which is the (i-1)th number)
            # otherwise, the median is the ith number
            if is_even_len and i == median_pos:
                median = (median + ith_num) / 2
            else:
                median = ith_num

        return median