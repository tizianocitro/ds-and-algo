# !code: 621, !difficulty: medium, !from: https://leetcode.com/problems/task-scheduler/

'''Problem:
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n.
Each CPU interval can be idle or allow the completion of one task.
Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

Constraints:
- 1 <= tasks.length <= 104
- tasks[i] is an uppercase English letter
- 0 <= n <= 100

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
With a cooling interval of 1, you can repeat a task after just one other task.

Input: tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10
Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.
'''

# solution one using hash map and heap
# Complexity:
# O(m) time - where m is the number of tasks because we need to iterate over the tasks to build the frequency map
# it would be O(mlogk) time, where k is the number of unique tasks, because we use heap's operations
# but given that k is limited to 26, we can consider the time complexity of these operations as O(1)
# O(1) space - because tasks are limited to 26 (uppercase english letters) and all structures are limited to
# contain at most 26 elements (heap, counter, executed array)
from collections import Counter
from heapq import *

class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        # counts how many times each task appears
        freqs = Counter(tasks)

        # build a heap to start with the most frequent task
        freq_max_heap = [(-freq, task) for task, freq in freqs.items()]
        heapify(freq_max_heap)

        intervals = 0

        # we executed until all the occurrences of each task have been executed
        while freq_max_heap:
            # keeps track of the tasks that have been executed already
            executed = []

            # keeps track of the number of tasks processed in the current cycle
            cycle = n + 1

            # keeps track of the number of tasks processed in the current cycle
            task_count = 0

            # until we execute all tasks in the heap or
            # we complete a full n + 1 cycle of task execution
            while cycle > 0 and freq_max_heap:
                freq, task = heappop(freq_max_heap)
                # if the task can still be executed at least once
                if -freq > 1:
                    executed.append((freq + 1, task))
                task_count += 1
                cycle -= 1

            # restore updated frequencies to the heap
            for freq, task in executed:
                heappush(freq_max_heap, (freq, task))

            # if there are no more occurrences of tasks we just add the ones that
            # we could execute in this iteration, otherwise we add n + 1 because
            # we need to complete a full n + 1 cycle including the idles
            intervals += task_count if not freq_max_heap else n + 1

        return intervals

# solution two using hash map, heap, and queue
# Complexity:
# O(m) time - where m is the number of tasks because we need to iterate over the tasks to build the frequency map
# it would be O(mlogk) time, where k is the number of unique tasks, because we use heap's operations
# but given that k is limited to 26, we can consider the time complexity of these operations as O(1)
# O(n) space - because tasks are limited to 26 (uppercase english letters) but we if n > 26, we need to store the idle tasks
from collections import Counter, deque
from heapq import *

class Solution:
    def __init__(self):
        self.IDLE = 'idle'

    def leastInterval(self, tasks, n: int) -> int:
        # counts how many times each task appears
        freqs = Counter(tasks)

        # build a heap to start with the most frequent task
        freq_max_heap = [(-freq, task) for task, freq in freqs.items()]
        heapify(freq_max_heap)

        # keeps track of the tasks that have been executed already
        # until we execute n + 1 of them
        q = deque()

        executed = intervals = 0

        # we executed until all the occurrences of each task have been executed
        while executed < len(freqs):
            freq, task = heappop(freq_max_heap) if freq_max_heap else (0, self.IDLE)

            # if the task is not idle, we decrement its frequency
            # and if it becomes zero, we increment the executed counter
            # because we have executed all the occurrences of the task
            if task != self.IDLE:
                freq += 1
                if freq == 0:
                    executed += 1

            # add the currently executed task to the queue
            q.append((freq, task))

            # if we have executed n + 1 tasks, we can add the first of them to
            # heap again because we executed n tasks and we can execute the same task again
            if len(q) > n:
                nth_task = q.popleft()
                # only add the task back if it is not idle or
                # if it has more occurrences that need to be executed
                if -nth_task[0] > 0:
                    heappush(freq_max_heap, nth_task)

            intervals += 1

        return intervals
