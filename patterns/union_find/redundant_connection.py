# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/redundant-connection-medium

'''Problem:
Given an undirected graph containing 1  to n nodes.
The graph is represented by a 2D array of edges, where edges[i] = [ai, bi], represents an edge between ai, and bi.

Identify one edge that, if removed, will turn the graph into a tree.
A tree is a graph that is connected and has no cycles.
Assume that the graph is always reducible to a tree by removing just one edge.
If there are multiple answers, return the edge that occurs last in the input.

Constraints:
- n == edges.length
- 3 <= n <= 1000
- edges[i].length == 2
- 1 <= ai < bi <= edges.length
- ai != bi
- There are no repeated edges.
- The given graph is connected.


Input: [[1,2], [1,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The edge [1,4] is redundant because removing it will eliminate the cycle 1-3-4-1 while keeping the graph connected.

Input: [[1,2], [2,3], [3,1], [3,4]]
Output: [3,1]
Explanation: The edge [3,1] creates a cycle 1-2-3-1. Removing it leaves a tree with no cycles.

Input: [[1,2], [2,3], [3,4], [4,2], [5,6]]
Output: [4,2]
Explanation: The edge [4,2] adds a cycle 2-3-4-2 in one part of the graph. Removing this edge breaks the cycle, and the remaining graph is a tree.
'''

# solution one with union find as a class
# Complexity:
# O(na(n)) - where n is the number of nodes (and also edges) and a is the inverse Ackermann function (nearly constant)
# O(n) space - to store the parent and rank arrays
class UnionFind:
    def __init__(self, num_of_nodes):
        # the + 1 is because nodes are 1-indexed and we need
        # to include the last node in the position with the same index
        self.parent = [u for u in range(num_of_nodes + 1)]
        self.rank = [0 for _ in range(num_of_nodes + 1)]

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        uset = self.find(u)
        vset = self.find(v)

        if self.rank[uset] < self.rank[vset]:
            self.parent[uset] = vset
        elif self.rank[uset] > self.rank[vset]:
            self.parent[vset] = uset
        else:
            self.parent[uset] = vset
            self.rank[uset] += 1

class Solution:
    def findRedundantConnection(self, edges):
        # the + 1 is because nodes are 1-indexed
        num_of_nodes = len(edges) + 1
        uf = UnionFind(num_of_nodes)

        last_redundant_edge = []
        for u, v in edges:
            # redundant connection found
            if uf.find(u) == uf.find(v):
                last_redundant_edge = [u, v]
            else:
                uf.union(u, v)

        return last_redundant_edge

    # it can be written also in this way,
    # where we return the first redundant edge found
    # def findRedundantConnection(self, edges):
    #     num_of_nodes = len(edges) + 1
    #     uf = UnionFind(num_of_nodes)
    #     for u, v in edges:
    #         if uf.find(u) == uf.find(v):
    #             return [u, v]
    #         uf.union(u, v)
    #     return []

# solution two with union find as a functions
# Complexity:
# O(na(n)) - where n is the number of nodes (and also edges) and a is the inverse Ackermann function (nearly constant)
# O(n) space - to store the parent and rank arrays
class Solution:
    def findRedundantConnection(self, edges):
        # the + 1 is because nodes are 1-indexed
        parent = [i for i in range(len(edges) + 1)]

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            parent[find(u)] = find(v)

        for edge in edges:
            u, v = edge
            # redundant connection found
            if find(u) == find(v):
                return edge
            union(u, v)

        return []