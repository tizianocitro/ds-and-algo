# !code: 56, !difficulty: medium, !from: https://leetcode.com/problems/merge-intervals/

'''Problem:
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

# solution one
# Complexity:
# O(nlogn) time - where n is the number of intervals (for sorting)
# O(n) space - where n is the number of intervals (for storing the merged intervals)
# in the worst case, all intervals are non overlapping
class Solution:
    def merge(self, intervals):
        # sort by start time to identify overlapping intervals
        intervals.sort(key=lambda interval: interval[0])

        merged_intervals = [] 
        current_interval = intervals[0]

        for i in range(1, len(intervals)):
            interval = intervals[i]

            # if the current interval overlaps with the interval we are
            # processing (current interval), we merge the intervals
            if interval[0] <= current_interval[1]:
                # this is actually not needed because the intervals are sorted by start time
                # so current_interval[0] <= interval[0] always, but it's good to be explicit
                current_interval[0] = min(interval[0], current_interval[0])
                current_interval[1] = max(interval[1], current_interval[1])
            else:
                # otherwise, we add current_interval to the list of merged intervals
                # and update current_interval to the interval we are processing
                merged_intervals.append(current_interval)
                current_interval = interval

        # add the last interval to the list of merged intervals
        # because it won't be added in the loop
        merged_intervals.append(current_interval)

        return merged_intervals