# !difficulty: hard, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63936a049634a0fa11c91b2b

'''Problem:
We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running.
Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

Input: jobs = [[1,4,3], [2,5,4], [7,9,6]]
Output: 7
Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the jobs are running at the same time i.e., during the time interval (2,4).

Input: jobs = [[6,7,10], [2,4,11], [8,12,15]]
Output: 15
Explanation: None of the jobs overlap, therefore we will take the maximum load of any job which is 15.
'''

# solution one
# Complexity:
# O(nlogn) time - because we are sorting the jobs,
# also each push and pop from the heap is O(logn) and in worst case we do it n times
# O(n) space - for the heap, because we can have all the jobs overlapping

# doing this instead of import heapq allows to use functions without heapq
# e.g., heapq.heappop() as heappop()
from heapq import *

class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpuLoad = cpu_load

class Solution:
    def findMaxCPULoad(self, jobs):
        # equivalent to if len(jobs) == 0 or if len(jobs) < 1
        if not jobs:
            return 0

        jobs.sort(key=lambda j: j.start)

        max_cpu_load, cpu_load = 0, 0
        concurrent_jobs = []

        for job in jobs:
            # concurrent_jobs[0][0] will contain the end of the first job in the heap
            while concurrent_jobs and concurrent_jobs[0][0] <= job.start:
                completed_job = heappop(concurrent_jobs)
                # completed_job[1] will contain the cpuLoad of the job
                cpu_load -= completed_job[1]

            # heap in python can accept tuples where the first element is the key
            heappush(concurrent_jobs, (job.end, job.cpuLoad))
            cpu_load += job.cpuLoad

            max_cpu_load = max(max_cpu_load, cpu_load)

        return max_cpu_load
