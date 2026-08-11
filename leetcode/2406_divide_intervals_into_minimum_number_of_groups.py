# !code: 2406, !difficulty: medium, !from: https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

'''Problem:
You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].
You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.

Return the minimum number of groups you need to make.

Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.

Constraints:
- 1 <= intervals.length <= 10^5
- intervals[i].length == 2
- 1 <= lefti <= righti <= 10^6

Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
Output: 3
Explanation: We can divide the intervals into the following groups:
- Group 1: [1, 5], [6, 8].
- Group 2: [2, 3], [5, 10].
- Group 3: [1, 10].
It can be proven that it is not possible to divide the intervals into fewer than 3 groups.

Input: intervals = [[1,3],[5,6],[8,10],[11,13]]
Output: 1
Explanation: None of the intervals overlap, so we can put all of them in one group.
'''

# solution one using heap
# Complexity:
# O(nlogn) time - where n is the length of the input intervals
# O(n) space - for the heap
from heapq import *

class Solution:
    def minGroups(self, intervals) -> int:
        intervals.sort(key=lambda interval: interval[0])

        min_num_groups = 0
        end_times_min_heap = []

        for start, end in intervals:
            while end_times_min_heap and start > end_times_min_heap[0]:
                heappop(end_times_min_heap)

            heappush(end_times_min_heap, end)

            min_num_groups = max(min_num_groups, len(end_times_min_heap))

        return min_num_groups

# solution two using line sweep
# Complexity:
# O(nk) time - where n is the length of the input intervals and k is the range (range_start, range_end)
# O(k) space - for the point_to_count array which contains at most k elements
class Solution:
    def minGroups(self, intervals) -> int:
        # find the minimum starting point and maximum ending point of all intervals
        range_start = float("inf")
        range_end = float("-inf")
        for interval in intervals:
            range_start = min(range_start, interval[0])
            range_end = max(range_end, interval[1])

        # create an array to keep track of interval starts and ends within the range
        # add 2 to the length to avoid index issues with marking the end of intervals
        point_to_count = [0] * (range_end + 2)

        # iterate through intervals to mark the start and end of each
        for interval in intervals:
            # increment at the start point of the interval
            point_to_count[interval[0]] += 1
            # decrement right after the interval's end point
            point_to_count[interval[1] + 1] -= 1

        # keeps track of the number of intervals active at a given point
        concurrent_intervals = 0
        # stores the maximum overlap found during the iteration
        max_concurrent_intervals = 0

        # iterate from the minimum start to maximum end to calculate overlaps
        for i in range(range_start, range_end + 1):
            # update active intervals by the start/end marks
            concurrent_intervals += point_to_count[i]
            max_concurrent_intervals = max(max_concurrent_intervals, concurrent_intervals)

        # return the maximum number of overlapping intervals found,
        # which is the minimum group count needed
        return max_concurrent_intervals