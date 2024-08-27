# !difficulty: medium, !from:https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/is-graph-bipartite-medium

'''Problem:
Given a 2D array graph[][], representing the undirected graph, where graph[u] is an array of nodes that are connected with node u.

Determine whether a given undirected graph is a bipartite graph.

The graph is a bipartite graph, if we can split the set of nodes into two distinct subsets such that no two nodes within
the same subset are adjacent (i.e., no edge exists between any two nodes within a single subset).

Constraints:
- graph.length == n
- 0 <= graph[u].length < n
- 0 <= graph[u][i] <= n - 1
- graph[u] does not contain u
- All the values of graph[u] are unique
- If graph[u] contains v, then graph[v] contains u

Input: graph = [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: The nodes can be divided into two groups: {0, 2} and {1, 3}. No two nodes within each group are adjacent, thus the graph is bipartite.

Input: graph =[[1], [0], [3], [2]]
Output: true
Explanation: The graph is a simple chain of 4 nodes. It's clearly bipartite as we can have {0, 2} and {1, 3} as the two subsets.

Input: graph =[[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: We found that edges (1, 2), (0, 3), and (2, 3) connect nodes within the same set, which violates the condition
for a bipartite graph where each edge must connect nodes in different subsets. Thus, there's no way to divide
this graph into two subsets that satisfy the bipartite condition.
'''

# solution one using union find
# Complexity:
# O((v + e) * a(n)) time - to iterate over the graph where v is the number of vertices,
# e is the number of edges, and a(n) is the inverse Ackermann function which is nearly constant
# O(v) space - to store the parent and rank arrays
class UnionFind:
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        uset = self.find(u)
        vset = self.find(v)

        if uset == vset:
            return

        if self.rank[uset] < self.rank[vset]:
            self.parent[uset] = vset
        elif self.rank[uset] > self.rank[vset]:
            self.parent[vset] = uset
        else:
            self.parent[uset] = vset
            self.rank[vset] += 1

class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        uf = UnionFind(n)

        for u in range(n):
            # no edges to check for this node
            if not graph[u]:
                continue

            parent_u = uf.find(u)

            # take the first neighbor of u because we will use it
            # as the parent for the set that u should no be part of
            # the idea is that for each neighbor v of u,
            # u and v shoud never be in the same set
            first_neighbor = graph[u][0]

            # union the rest of u's neighbors to the first neighbor's set
            for v in graph[u]:
                # if u and v belong to the same set,
                # the graph is not bipartite
                if parent_u == uf.find(v):
                    return False
                uf.union(first_neighbor, v)

        return True