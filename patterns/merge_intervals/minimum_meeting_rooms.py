# !difficulty: hard

'''Problem:
Given a list of intervals representing the start and end time of N meetings,
find the minimum number of rooms required to hold all the meetings.

Input: meetings = [[1,4], [2,5], [7,9]]
Output: 2
Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can occur in any of the two rooms later.

Input: meetings: [[6,7], [2,4], [8,12]]
Output: 1
Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.

Input: meetings: [[4,5], [2,3], [2,4], [3,5]]
Output: 2
Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].
'''

# solution one with cleaner code
# Complexity:
# O(nlogn) time - because we are sorting the meetings,
# also each push and pop from the heap is O(logn) and in worst case we do it n times
# O(n) space - for the heap, because we can have all the meetings overlapping
import heapq

class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def findMinimumMeetingRooms(self, meetings):
        if not meetings:
            return 0

        # sort the meetings by start time
        meetings.sort(key=lambda x: x.start)

        min_rooms = 0
        min_heap = []

        for meeting in meetings:
            # remove all meetings that have ended from the min_heap
            while min_heap and meeting.start >= min_heap[0].end:
                heapq.heappop(min_heap)

            # add the current meeting into the min_heap
            heapq.heappush(min_heap, meeting)
            # all active meetings are in the min_heap, so we need rooms for all of them
            min_rooms = max(min_rooms, len(min_heap))

        return min_rooms

# solution two
# Complexity:
# O(nlogn) time - because we are sorting the meetings,
# also each push and pop from the heap is O(logn) and in worst case we do it n times
# O(n) space - for the heap, because we can have all the meetings overlapping
import heapq

class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def findMinimumMeetingRooms(self, meetings):
        if len(meetings) < 1:
            return 0

        meetings.sort(key=lambda x: x.start)

        # the number of max concurrent meetings indicates the minimum required rooms
        # because they cannot happen in the same room
        max_concurrent_meetings = 1
        concurrent_meetings = []
        heapq.heappush(concurrent_meetings, meetings[0].end)

        for i in range(1, len(meetings)):
            meeting = meetings[i]

            # this if can also be removed, because we are adding the meeting.end to the heap
            # and afterward we are removing the finished meetingsx
            if meeting.start < meetings[i - 1].end:
                heapq.heappush(concurrent_meetings, meeting.end)

            # we have to remove them even if they end in a time that is equal to the current meeting.start
            # because they are not overlapping in this case,
            # the previous one finishes just when this new one starts
            while concurrent_meetings and concurrent_meetings[0] <= meeting.start:
                heapq.heappop(concurrent_meetings)
            
            # we do it here because we have to consider newly added meetings,
            # but also remove the finished ones that now do not occupy the room anymore
            max_concurrent_meetings = max(max_concurrent_meetings, len(concurrent_meetings))

        return max_concurrent_meetings

# solution three without the if
# Complexity:
# O(nlogn) time - because we are sorting the meetings,
# also each push and pop from the heap is O(logn) and in worst case we do it n times
# O(n) space - for the heap, because we can have all the meetings overlapping
import heapq

class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def findMinimumMeetingRooms(self, meetings):
        if len(meetings) < 1:
            return 0

        meetings.sort(key=lambda x: x.start)

        # the number of max concurrent meetings indicates the minimum required rooms
        # because they cannot happen in the same room
        max_concurrent_meetings = 1
        concurrent_meetings = []
        heapq.heappush(concurrent_meetings, meetings[0].end)

        for i in range(1, len(meetings)):
            meeting = meetings[i]
            heapq.heappush(concurrent_meetings, meeting.end)

            # we have to remove them even if they end in a time that is equal to the current meeting.start
            # because they are not overlapping in this case,
            # the previous one finishes just when this new one starts
            while concurrent_meetings and concurrent_meetings[0] <= meeting.start:
                heapq.heappop(concurrent_meetings)
            
            # we do it here because we have to consider newly added meetings,
            # but also remove the finished ones that now do not occupy the room anymore
            max_concurrent_meetings = max(max_concurrent_meetings, len(concurrent_meetings))

        return max_concurrent_meetings
