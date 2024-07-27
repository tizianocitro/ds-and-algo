# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/tasks-scheduling-medium

'''Problem:
There are N tasks, labeled from 0 to N-1. Each task can have some prerequisite tasks which need to be completed before it can be scheduled.

Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: true
Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5] 

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: true
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish before '2' can be scheduled. One possible scheduling of tasks is: [0, 1, 2] 

Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: false
Explanation: The tasks have a cyclic dependency, therefore they cannot be scheduled.
'''

'''Similar Problems:
Course Schedule:
    There are N courses, labeled from 0 to N-1. Each course can have some prerequisite courses
    which need to be completed before it can be taken. Given the number of courses and a list of
    prerequisite pairs, find if it is possible for a studentto take all the courses.
Solution:
    This problem is exactly similar to the tasks scheduling problem.
    In this problem, we just have courses instead of tasks.
'''

# solution one
# Complexity:
# O(v + e) time - where v is the number of tasks and e is the number of prerequisites
# O(v + e) space - to store the graph and in-degrees
from collections import deque

class Solution:
    def isSchedulingPossible(self, tasks, prerequisites):
        if tasks < 1:
            return True

        # build the graph
        in_degrees = [0 for _ in range(tasks)]
        graph = [[] for _ in range(tasks)]
        for parent, child in prerequisites:
            graph[parent].append(child)
            in_degrees[child] += 1

        sources = deque()
        for node in range(len(in_degrees)):
            if in_degrees[node] == 0:
                sources.append(node)

        executed_tasks = []
        while sources:
            node = sources.popleft()
            executed_tasks.append(node)
            for child in graph[node]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    sources.append(child)

        # if sorted_order doesn't contain all tasks, there is a cyclic dependency
        # between tasks, therefore, we will not be able to schedule all tasks
        if len(executed_tasks) != tasks:
            return False

        return True

# solution two
# Complexity:
# O(v + e) time - where v is the number of tasks and e is the number of prerequisites
# O(v + e) space - to store the graph and in-degrees
from collections import deque

class Solution:
    def isSchedulingPossible(self, tasks, prerequisites):
        sorted_order = []
        if tasks <= 0:
            return False

        in_degrees = {i: 0 for i in range(tasks)}
        graph = {i: [] for i in range(tasks)}

        # build the graph
        for prerequisite in prerequisites:
            parent, child = prerequisite[0], prerequisite[1]
            graph[parent].append(child)
            in_degrees[child] += 1

        # find all sources i.e., all vertices with 0 in-degrees
        sources = deque()
        for node in in_degrees:
            if in_degrees[node] == 0:
                sources.append(node)

        # for each source, add it to the sorted_order and subtract one from all of its 
        # children's in-degrees if a child's in-degree becomes zero, add it to sources queue
        while sources:
            node = sources.popleft()
            sorted_order.append(node)

            # get the node's children to decrement their in-degrees
            for child in graph[node]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    sources.append(child)

        # if sorted_order doesn't contain all tasks, there is a cyclic dependency
        # between tasks, therefore, we will not be able to schedule all tasks
        return len(sorted_order) == tasks
