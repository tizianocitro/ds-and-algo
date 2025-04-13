# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/tasks-scheduling-order-medium

'''Problem:
There are N tasks, labeled from 0 to N-1. Each task can have some prerequisite
tasks which need to be completed before it can be scheduled.

Given the number of tasks and a list of prerequisite pairs, write a method to find the
ordering of tasks we should pick to finish all tasks.

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: [0 1 4 3 2 5] 
Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5] 

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2] 

Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: []
Explanation: The tasks have a cyclic dependency, therefore they cannot be scheduled.
'''

'''Similar Problems:
Course Schedule:
    There are N courses, labeled from 0 to N-1. Each course has some prerequisite courses which need to be completed before it can be taken.
    Given the number of courses and a list of prerequisite pairs, write a method to find
    the best ordering of the courses that a student can take in order to finish all courses.
Solution:
    This problem is exactly similar to the parent problem. In this problem, we have courses instead of tasks.
'''

# solution one
# Complexity:
# O(v + e) time - where v is the number of tasks and e is the number of prerequisites
# O(v + e) space - to store the graph and in-degrees
from collections import deque

class Solution:
    def findOrder(self, tasks, prerequisites):
        order_of_execution = []
        if tasks < 1:
            return order_of_execution

        in_degrees = [0 for _ in range(tasks)]
        graph = [[] for _ in range(tasks)]

        for parent, child in prerequisites:
            graph[parent].append(child)
            in_degrees[child] += 1

        sources = deque()
        for node in range(len(in_degrees)):
            if in_degrees[node] == 0:
                sources.append(node)

        while sources:
            node = sources.popleft()
            order_of_execution.append(node)

            for child in graph[node]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    sources.append(child)

        if len(order_of_execution) != tasks:
            return []

        return order_of_execution
