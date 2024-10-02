# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/number-of-connected-components-in-an-undirected-graph

'''Problem:
Given an undirected graph represented by 'n' nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes),
determine the number of connected components in the graph. A connected component is a group of nodes that are directly or indirectly linked to each other through the edges.

Constraints:
- 1 <= n <= 2000
- 1 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai <= bi < n
- ai != bi
- There are no repeated edges

Input: n = 5, edges = [[0,1], [2,3], [3,4]]
Output: 2
Explanation: Two components are: 0-1, and 2-3-4.

Input: n = 4, edges = [[0,1], [1,2], [2,3]]
Output: 1
Explanation: All the nodes are connected in a single chain: 0-1-2-3.

Input: n = 3, edges = [[0,1]]
Output: 2
Explanation: Two connected components exist: 0-1 and an isolated node 2.
'''

# solution one using union find
# Complexity:
# O((e + v) * a(v)) time - where e is the number of edges, v is the number of vertices, and a(v) is the
# inverse Ackermann function, a(v) is nearly constant, so the time complexity could be considered O(e + v)
# O(v) space - to store the parent and rank arrays in the union find
class UnionFind:
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        self.rank = [0] * n

    def find (self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pv == pu:
            return

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1

class Solution:
    def countComponents(self, n, edges):
        uf = UnionFind(n)

        # for each edge, union the nodes, this will reduce the number of components
        # however, this will not give the correct number of unique connected components
        # this takes O(e * a(v)) time where e is the number of edges and a(v) is the inverse Ackermann function
        for u, v in edges:
            uf.union(u, v)

        # to get the number of unique components, we need to find the number of
        # unique parents, so we find the parent of each node and add it to a set
        # this takes O(n * a(v)) time where n is the number of nodes and a(v) is the inverse Ackermann function
        parents = set(uf.find(i) for i in range(n))

        # the number of connected components is the length of the set
        return len(parents)

# solution two using union find but with a slightly different approach
# Complexity:
# O((e * a(v)) + n) time - where e is the number of edges, v is the number of vertices, and a(v) is the
# inverse Ackermann function, a(v) is nearly constant, so the time complexity could be considered O(e + v)
# O(v) space - to store the parent array in the union find
class Solution:
    def __init__(self):
        self.parents = []

    def find(self, u):
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def countComponents(self, n, edges):
        # initially, each node is a component
        components = n

        # this takes O(n) time where n is the number of nodes
        self.parents = [i for i in range(n)]

        # this takes O(e * a(v)) time where e is the number of edges
        # and a(v) is the inverse Ackermann function
        for u, v in edges:
            pu = self.find(u)
            pv = self.find(v)

            # if the nodes are not in the same component
            if pu != pv:
                # merge the two components
                self.parents[pu] = pv
                # and decrease the component count
                components -= 1

        return components