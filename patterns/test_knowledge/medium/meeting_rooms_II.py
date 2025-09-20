# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/meeting-rooms-ii-medium

'''Problem:
Given a list of time intervals during which meetings are scheduled, determine the minimum number of meeting
rooms that are required to ensure that none of the meetings overlap in time.

Input: [[10, 15], [20, 25], [30, 35]]
Output: 1
Explanation: There are no overlapping intervals in the given list. So, only 1 meeting room is enough for all the meetings.

Input: [[10, 20], [15, 25], [24, 30]]
Output: 2
Explanation: The first and second intervals overlap, and the second and third intervals overlap as well. So, we need 2 rooms.

Input: [[10, 20], [20, 30]]
Output: 1
Explanation: The end time of the first meeting is the same as the start time of the second meeting.
So, one meeting can be scheduled right after the other in the same room.
'''

# solution one using min heap
# Complexity:
# O(nlogn) time - where n is the number of intervals
# O(n) space - where n is the number of intervals
from heapq import *

class Solution:
    def minMeetingRooms(self, intervals) -> int:
        rooms = 0

        # if there are no intervals, return 0 because no rooms are needed
        if len(intervals) < 1:
            return rooms

        # sort the intervals by start time
        intervals.sort(key=lambda interval: interval[0])

        min_heap = []
        for start, end in intervals:
            # while the min heap is not empty and the first element in the min heap is less
            # than or equal to the start time of the current interval, pop the first element
            # because a room is available again as that meeting has ended
            while min_heap and min_heap[0] <= start:
                heappop(min_heap)

            # add a room for the current meeting
            heappush(min_heap, end)
            # update the number of rooms needed
            rooms = max(rooms, len(min_heap))

        return rooms

# solution two using the count of free rooms
# Complexity:
# O(nlogn) time - where n is the number of intervals
# O(n) space - where n is the number of intervals
import heapq

class Solution:
    def minMeetingRooms(self, intervals) -> int:
        if not intervals:
            return 0

        free_rooms = []

        # sort the meetings in increasing order of their start time.
        intervals.sort(key=lambda x: x[0])

        # add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # for all the remaining meeting rooms
        for interval in intervals[1:]:
            # if the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= interval[0]:
                heapq.heappop(free_rooms)

            # if a new room is to be assigned, then also we add to the heap
            heapq.heappush(free_rooms, interval[1])

        # the size of the heap tells us the minimum rooms required for all the meetings
        return len(free_rooms)