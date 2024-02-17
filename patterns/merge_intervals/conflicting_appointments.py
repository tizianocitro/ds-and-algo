# !difficulty: medium

'''Problem:
Given an array of intervals representing N appointments, find out if a person can attend all the appointments.

Input appointments = [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.

Input: appointments = [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.
'''

# solution one
# O(nlogn) time - where n is the number of appointments, because we are sorting the appointments
# O(1) space
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

class Solution:
    def canAttendAllAppointments(self, intervals):
        if len(intervals) < 2:
            return True
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            # the comparison is "<" and not "<=" because
            # while merging we needed "<=" comparison, as we will be merging the two
            # intervals having condition "intervals[i][start] == intervals[i - 1][end]",
            # but such intervals don't represent conflicting appointments as one starts right after the other
            if intervals[i].start < intervals[i - 1].end:
                return False
        return True
