# difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/topological-sort-medium

'''Problem:
Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices
such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.

Given a directed graph, find the topological ordering of its vertices.
If the graph is cyclic, return an empty array.

Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
Output: Following are the two valid topological sorts for the given graph:
1) 3, 2, 0, 1
2) 3, 2, 1, 0

Input: Vertices=5, Edges=[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]
Output: Following are all valid topological sorts for the given graph:
1) 4, 2, 3, 0, 1
2) 4, 3, 2, 0, 1
3) 4, 3, 2, 1, 0
4) 4, 2, 3, 1, 0
5) 4, 2, 0, 3, 1

Input: Vertices=7, Edges=[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]
Output: Following are all valid topological sorts for the given graph:
1) 5, 6, 3, 4, 0, 1, 2
2) 6, 5, 3, 4, 0, 1, 2
3) 5, 6, 4, 3, 0, 2, 1
4) 6, 5, 4, 3, 0, 1, 2
5) 5, 6, 3, 4, 0, 2, 1
6) 5, 6, 3, 4, 1, 2, 0

There are other valid topological ordering of the graph too.
'''

# solution one
# Complexity:
# O(v + e) time - where v is the number of vertices and e is the number of edges
# O(v + e) space - to store the graph and in-degrees
from collections import deque

class Solution:
    def sort(self, vertices, edges):
        sorted_order = []

        # equivalent to if vertices <= 0:
        if vertices < 1:
            return sorted_order

        # count of incoming edges
        # it can also be a dictionary
        # in_degrees = {i: 0 for i in range(vertices)}
        in_degrees = [0 for _ in range(vertices)]

        # adjacency list graph
        # it can also be a dictionary
        # graph = {i: [] for i in range(vertices)}
        graph = [[] for _ in range(vertices)]

        # build the graph in O(e)
        for edge in edges:
            parent, child = edge
            # put the child into it's parent's list
            graph[parent].append(child)
            # increment child's in degree
            in_degrees[child] += 1

        # find all sources, i.e., all vertices with 0 in-degrees
        sources = deque()

        # build the sources in o(v)
        # alternatively:
        # for node in range(len(in_degrees)):
        # if in_degrees is a map:
        # for node in in_degrees:
        # for node in in_degrees.keys():
        for node in range(vertices):
            if in_degrees[node] == 0:
                # vertice with 0 in degree, so it is a source
                sources.append(node)

        # this takes O(v + e)
        # for each source, add it to the sorted_order and subtract '1'
        # from all of its children's in-degrees, if a child's in-degree
        # becomes zero, add it to the sources queue for next iteration
        while sources:
            # get a current source, the first in the queue
            node = sources.popleft()
            sorted_order.append(node)

            # get the node's children to decrement their in-degrees
            for child in graph[node]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    # the child's in-degree is now zero, so add it to the sources
                    sources.append(child)

        # topological sort is not possible as the graph has a cycle
        # if sorted_order is not equal to the number of vertices, this means
        # that the graph has a cycle because there are nodes that are not visited
        if len(sorted_order) != vertices:
            # print('no topological sort', len(sorted_order), vertices)
            return []

        return sorted_order