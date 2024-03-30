# !difficulty: easy

'''Problem:
Given an undirected graph, represented as a list of edges.
Each edge is illustrated as a pair of integers [u, v], signifying that there's a mutual connection between node u and node v.

Given the number of nodes n, the edges, a starting node start, and a destination node end, your task is to ascertain if a path exists between the starting node and the destination node.

Input: n = 4, edges = [[0,1],[1,2],[2,3]], start = 0, end = 3
Expected Output: true
Justification: There's a path from node 0 -> 1 -> 2 -> 3.
'''

# solution one iterative
# Complexity:
# O(v + e) time - where v is the number of vertices and e is the number of edges for the dfs
# O(v + e) space - where v is the number of vertices and e is the number of edges for the dfs
# the graph dict as adjacency list is O(v + e) space
class Solution:
    def validPath(self, n: int, edges, start: int, end: int) -> bool:
        graph = {i: [] for i in range(n)}

        # since it is undirected graph, we need to add the edges in both directions
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        return self.dfs(graph, start, end)

    def dfs(self, graph, start, end):
        stack, visited = [], set()
        stack.append(start)

        while stack:
            current = stack.pop()
            visited.add(current)
            if current == end:
                return True

            for neighbor in reversed(graph[current]):
                if neighbor not in visited:
                    stack.append(neighbor)

        return False;

# solution one recursive
# Complexity:
# O(v + e) time - where v is the number of vertices and e is the number of edges for the dfs
# O(v + e) space - where v is the number of vertices and e is the number of edges for the dfs
# the graph dict as adjacency list is O(v + e) space
from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges, start: int, end: int) -> bool:
        graph = defaultdict(list)

        # create graph from edges
        for u, v in edges:
            graph[u].append(v)
            # undirected graph
            graph[v].append(u)

        visited = set()

        # inner function definition
        def dfs(node):
            # found the path
            if node == end:
                return True

            visited.add(node)

            # traverse neighbors
            for neighbor in graph[node]:
                if neighbor not in visited and dfs(neighbor):
                    # return true because the above if is true only if the dfs returns true,
                    # which means the path is found
                    return True

            # path not found
            return False

        return dfs(start)