# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63923e6de4cb724ea719007a

'''Problem:
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Input: intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].

Input: intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].
'''

# solution one
# Complexity:
# O(nlogn) time - because we are sorting the intervals
# O(n) space - to store the sorted intervals
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals

        # sort to ensure the we can make the check at line 25 to verify overlapping
        intervals.sort(key=lambda x: x.start)

        mergedIntervals = []
        current = intervals[0]

        for i in range(1, len(intervals)):      
            interval = intervals[i]

            # intervals do not overlap, so we add the current interval
            if interval.start >= current.end:
                mergedIntervals.append(current)
                # move to the current interval to the interval that did not overlap
                current = interval
                continue

            # if they overlap we just need to update the right element
            # with the highest among the two right elements
            current.end = max(interval.end, current.end)

        # add the last interval
        mergedIntervals.append(current)
        
        return mergedIntervals

# solution two
# Complexity:
# O(nlogn) time - because we are sorting the intervals
# O(n) space - to store the sorted intervals

class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals

        # sort the intervals on the start time
        intervals.sort(key=lambda x: x.start)

        mergedIntervals = []
        start = intervals[0].start
        end = intervals[0].end

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval.start <= end:  # overlapping intervals, adjust the 'end'
                end = max(interval.end, end)
            else:  # non-overlapping interval, add the previous interval and reset
                mergedIntervals.append(Interval(start, end))
                start = interval.start
                end = interval.end

        # add the last interval
        mergedIntervals.append(Interval(start, end))

        return mergedIntervals