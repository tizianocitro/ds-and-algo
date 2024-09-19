# !code: 207, !difficulty: medium, !from: https://leetcode.com/problems/course-schedule/

'''Problem:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs prerequisites[i] are unique

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
'''

# solution one using topological sort
# Complexity:
# O(n + m) time, where n is the number of courses and m is the number of prerequisites
# O(n + m) space, where n is the number of courses and m is the number of prerequisites
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # if there are no courses or only one, return True
        if numCourses < 2:
            return True

        # create a list to store the in-degrees of each course
        in_degrees = [0] * numCourses
        # create a graph to store the courses that depend on each course
        graph = [[] for _ in range(numCourses)]
        # calculate the in-degrees of each course and store the
        # courses that depend on each in the graph
        for course, prereq in prerequisites:
            # increment the in-degree of the course that has a prerequisite
            in_degrees[course] += 1
            # add the node that has a prerequisite to the neighbors of the prerequisite
            graph[prereq].append(course)

        # create a queue to store the courses that have no prerequisites
        # because they can work as starting points
        sources = deque()
        for course in range(len(in_degrees)):
            if in_degrees[course] == 0:
                sources.append(course)

        # count the number of scheduled courses
        scheduled = 0
        while sources:
            # count the current node as part of the scheduled courses
            course = sources.popleft()
            scheduled += 1

            # decrement the in-degree of the courses that depend on the current course
            # and add them to the queue if they have no prerequisites anymore
            for prereq in graph[course]:
                in_degrees[prereq] -= 1
                if in_degrees[prereq] == 0:
                    sources.append(prereq)

        # return True if all courses could be scheduled
        return scheduled == numCourses

# solution two using dfs
# Complexity:
# O(n + m) time, where n is the number of courses and m is the number of prerequisites
# O(n + m) space, where n is the number of courses and m is the number of prerequisites
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        # build the graph using an adjacency list
        graph = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])

        visit = [False] * numCourses
        in_stack = [False] * numCourses
        for i in range(numCourses):
            if self.dfs(i, graph, visit, in_stack):
                return False

        return True

    def dfs(self, node, graph, visit, in_stack):
        # if the node is already in the stack, we have a cycle
        if in_stack[node]:
            return True

        # if the node has already been visited, we have a cycle
        if visit[node]:
            return False

        # mark the current node as visited and part of current recursion stack
        visit[node] = True
        in_stack[node] = True
        for neighbor in graph[node]:
            if self.dfs(neighbor, graph, visit, in_stack):
                return True

        # remove the node from the stack
        in_stack[node] = False

        return False
