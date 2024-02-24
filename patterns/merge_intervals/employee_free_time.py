# !difficulty: hard

'''Problem:
For K employees, we are given a list of intervals representing each employee’s working hours.
Our goal is to determine if there is a free interval which is common to all employees.
You can assume that each list of employee working hours is sorted on the start time.

Input: employeeWorkingHours = [[[1,3], [5,6]], [[2,3], [6,8]]]
Output: [3,5]
Explanation: All the employees are free between [3,5].
'''

# solution one with only array
# Complexity:
# O(nlogn) time - because of sorting
# O(n) space - for storing the result and the array of all intervals
class Solution:
    def findEmployeeFreeTime(self, schedule):
        result = []
        
        all_intervals = []
        for intervals in schedule:
            all_intervals.extend(intervals)

        all_intervals.sort(key=lambda interval:interval.start)

        for i in range(1, len(all_intervals)):
            if all_intervals[i].start > all_intervals[i - 1].end:
                start = min(all_intervals[i].end, all_intervals[i - 1].end)
                end = max(all_intervals[i].start, all_intervals[i - 1].start)
                result.append([start, end])

        return result

'''Solution with heap:
This leverages the fact that each employee list is individually sorted!
We take the first interval of each employee and insert it in a Min Heap.
This Min Heap can always give us the interval with the smallest start time.
Once we have the smallest start-time interval, we can then compare it with the next smallest start-time interval (again from the Heap) to find the gap.
Whenever we take an interval out of the Min Heap, we can insert the same employee’s next interval in the heap.
This also means that we need to know which interval belongs to which employee.
'''
# solution two with heap
# Complexity:
# O(nlogk) time - where n is the total number of intervals and k is the number of employees
# this is because we are iterating through the intervals only once (which will take O(n)),
# and every time we process an interval, we remove (and can insert) one interval in the Min Heap, (which will take O(logk)).
# O(k) space - the heap will not have more than k elements.
from heapq import *

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class EmployeeInterval:
    def __init__(self, interval, employeeIndex, intervalIndex):
        # interval representing employee's working hours
        self.interval = interval
        # index of the list containing working hours of this employee
        self.employeeIndex = employeeIndex
        # index of the interval in the employee list
        self.intervalIndex = intervalIndex

    def __lt__(self, other):
        # min heap based on meeting.start
        return self.interval.start < other.interval.start

class Solution:
    def findEmployeeFreeTime(self, schedule):
        if schedule is None:
            return []

        n = len(schedule)
        result, minHeap = [], []

        # insert the first interval of each employee to the queue
        for i in range(n):
            heappush(minHeap, EmployeeInterval(schedule[i][0], i, 0))

        previousInterval = minHeap[0].interval
        while minHeap:
            queueTop = heappop(minHeap)
            # if previousInterval is not overlapping with the next interval, insert a free interval
            if previousInterval.end < queueTop.interval.start:
                result.append(Interval(previousInterval.end, queueTop.interval.start))
                previousInterval = queueTop.interval
            else: # overlapping intervals, update the previousInterval if needed
                if previousInterval.end < queueTop.interval.end:
                    previousInterval = queueTop.interval

            # if there are more intervals available for the same employee, add their next interval
            employeeSchedule = schedule[queueTop.employeeIndex]
            # len will be 2, which will be less than 0 + 1 in case of the two intervals we have
            # so if so far we have only considered the first of the two intervals for the employee, we will add the second interval
            if len(employeeSchedule) > queueTop.intervalIndex + 1:
                heappush(minHeap, EmployeeInterval(
                    employeeSchedule[queueTop.intervalIndex + 1],
                    queueTop.employeeIndex,
                    queueTop.intervalIndex + 1))

        return result