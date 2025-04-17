# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63a1e905b231098e09f3ca44

'''Problem:
You are given a list of tasks that need to be run, in any order, on a server.
Each task will take one CPU interval to execute but once a task has finished,
it has a cooling period during which it can’t be run again.
If the cooling period for all tasks is K intervals, find the minimum number of CPU
intervals that the server needs to finish all tasks.

If at any time the server can’t execute any task then it must stay idle.

Input: [a, a, a, b, c, c], K=2
Output: 7
Explanation: a -> c -> b -> a -> c -> idle -> a

Input: [a, b, a], K=3
Output: 5
Explanation: a -> b -> idle -> idle -> a
'''

# solution one
# Complexity:
# O(nlogn) time - where n is the number of tasks
# O(n) space - where n is the number of tasks for the map and heap
from heapq import *
from collections import deque

class Solution:
    def scheduleTasks(self, tasks, k):
        if k < 1 or len(tasks) < 2:
            return len(tasks)

        # count the frequency of each task
        frequencies = {}
        for task in tasks:
            frequencies[task] = frequencies.get(task, 0) + 1

        # insert the tasks into a max heap based on their frequency
        max_heap = []
        for task, frequency in frequencies.items():
            heappush(max_heap, (-frequency, task))

        # executed indicates the number of tasks that have been fully executed,
        # meaning that their frequency has reached 0, so if a task 'a' has a frequency of 3,
        # it will be fully executed when it has been executed 3 times
        interval_count, executed = 0, 0

        # k_repeats is a queue that will hold the tasks that have been executed
        k_repeats = deque()

        # while we have not fully executed all the tasks
        while executed < len(frequencies):
            # if there are no tasks in the max heap, we will have to idle
            frequency, task = heappop(max_heap) if max_heap else (-1, 'idle')

            # increment the interval count and if the task is not idle,
            # decrement its frequency in the frequencies map and, in case,
            # the frequency reaches 0, increment the executed count
            interval_count += 1
            if task != 'idle':
                frequencies[task] -= 1
                if frequencies[task] == 0:
                    executed += 1

            # append the task to the k_repeats queue
            k_repeats.append((frequency + 1, task))

            # if the queue has k elements, we can start executing again the tasks
            # that have been executed k intervals ago, unless their frequency is 0
            if len(k_repeats) > k:
                first_repeated = k_repeats.popleft()
                if first_repeated[0] != 0:
                    heappush(max_heap, first_repeated)

        return interval_count

# solution two
# Complexity:
# O(nlogn) time - where n is the number of tasks
# O(n) space - where n is the number of tasks for the map and heap
from heapq import *

class Solution:
    def scheduleTasks(self, tasks, k):
        interval_count = 0

        frequencies = {}
        for char in tasks:
            frequencies[char] = frequencies.get(char, 0) + 1

        max_heap = []
        for char, frequency in frequencies.items():
            heappush(max_heap, (-frequency, char))

        while max_heap:
            wait_list = []

            # try to execute as many as k + 1 tasks from the max-heap
            # because there need to be at least k intervals before
            # the same task can be executed again, so we have to execute k + 1 tasks
            n = k + 1
            while n > 0 and max_heap:
                # we execute a task so we can increment the interval count
                interval_count += 1

                frequency, char = heappop(max_heap)
                if -frequency > 1:
                    # decrement the frequency and add the task to the wait list
                    wait_list.append((frequency + 1, char))
                    # decrement the number of tasks that we can execute
                    n -= 1

            # put all the waiting list back on the heap for the next iteration
            for frequency, char in wait_list:
                heappush(max_heap, (frequency, char))

            # if there are still tasks left in the heap, it means we need to
            # idle for the next n remaining intervals before we can start executing tasks again
            if max_heap:
                interval_count += n

        return interval_count