# !code: 57, !difficulty: medium, !from: https://leetcode.com/problems/insert-interval/description, https://neetcode.io/problems/insert-new-interval/

'''Problem:
You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i]
represent the start and the end of the ith interval and intervals is sorted in ascending order by start_i.

You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i <= end_i <= 10^5
- intervals is sorted by start_i in ascending order
- newInterval.length == 2
- 0 <= start <= end <= 10^5

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''

# solution one with while loop
# Complexity:
# O(n) time - because we are iterating over the intervals
# O(n) space - to store the merged intervals
class Solution:
    def insert(self, intervals, newInterval):
        merged = []

        # to iterate over the intervals in separate loops
        i = 0

        # skip (and add to output) all intervals that come before the 'newInterval'
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # merge all intervals that overlap with the newInterval,
        # meaning the start of the interval is less than or equal to the end of the newInterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            # merge the intervals
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        # insert the newInterval because following intervals do not overlap,
        # they come after the newInterval
        merged.append(newInterval)

        # add all the remaining intervals to the output, the ones that come after the newInterval
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1

        return merged
