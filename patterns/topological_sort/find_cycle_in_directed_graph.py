# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/solution-topological-sort

'''Problem:
Find if a given Directed Graph has a cycle in it or not.
'''

# solution one
# Complexity:
# O(v + e) time - where v is the number of vertices and e is the number of edges
# O(v + e) space - to store the graph and in-degrees
from collections import deque

class Solution:
    def findCycle(self, vertices, edges):
        if vertices < 1:
            return False

        # count of incoming edges and graph
        in_degress = {node: 0 for node in range(vertices)}
        graph = {node: [] for node in range(vertices)}

        # build the graph
        for parent, child in edges:
            graph[parent].append(child)
            in_degress[child] += 1

        # find all sources, i.e., all vertices with 0 in-degrees
        sources = deque()
        for node in in_degress:
            if in_degress[node] == 0:
                sources.append(node)

        visited = 0

        while sources:
            node = sources.popleft()
            # increment the visited nodes
            visited += 1

            # decrement the in-degrees of the children
            for child in graph[node]:
                in_degress[child] -= 1
                if in_degress[child] == 0:
                    sources.append(child)

        # if visited is not equal to vertices, then there is a cycle
        # because there is a cycle if there is a node that is not visited
        if visited != vertices:
            return True

        return False