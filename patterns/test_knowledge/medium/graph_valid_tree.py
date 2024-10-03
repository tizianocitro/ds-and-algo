# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/graph-valid-tree-medium

'''Problem:
Given a number n, which indicates the number of nodes numbered from 0 to n-1,
and a list of undirected edges for the graph, determine if the graph is a valid tree.

A graph qualifies as a valid tree if it meets the following criteria:
- It has no cycles
- It is fully connected

Constraints:
- 1 <= n <= 2000
- 0 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai <= bi < n
- ai != bi
- There are no self-loops or repeated edges

Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Explanation: There are no cycles in the graph, and all nodes are connected, forming a valid tree.

Input: n = 4, edges = [[0,1],[1,2],[2,3],[3,0]]]]
Output: false
Explanation: There is a cycle in the graph (0-1-2-3-0), thus it's not a valid tree.

Input: n = 5, edges = [[0,1],[1,2],[2,3]]
Output: false
Explanation: TNode 4 is not connected to any other node, making the graph not fully connected.
'''

# solution one using union find
# Complexity:
# O((e + v) * a(v)) time - where e is the number of edges, v is the number of vertices, and a(v) is the
# inverse Ackermann function, a(v) is nearly constant, so the time complexity could be considered O(e + v)
# also in the worst case, we work with e = v - 1, so the time complexity could be considered O(v)
# O(v) space - to store the parent and rank arrays in the union find
class UnionFind:
    def __init__(self, n):
        self.parent = [u for u in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        # you could also use the following check to return False
        # if pu == pv because it means that there is a cycle, so
        # if you return True at the end of the union() method, then
        # in the validTree() method, you could return False if
        # the union operation fails (because it fails because of a cycle)
        # e.g., if not uf.union(u, v): return False
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
    def validTree(self, n, edges):
        # it works also without this because in the worst case we would process all the n - 1 valid edges
        # but on the n-th edge we would return False because it would create a cycle
        # to be a valid tree, the graph should have n - 1 edges, if less
        # than not all nodes are connected, if more, then there is a cycle
        if len(edges) != n - 1:
            return False

        uf = UnionFind(n)

        # for each edge, union the nodes, this will reduce the number of components
        # however, this will not give the correct number of unique connected components
        # this takes O(e * a(v)) time where e is the number of edges and a(v) is the inverse Ackermann function
        for u, v in edges:
            # cycle detected, so return False
            # because the graph is a valid tree if there are no cycles
            if uf.find(u) == uf.find(v):
                return False

            # reduce the number of components if two nodes are connected
            # by updating the parent of one of the two nodes and (union operation)
            uf.union(u, v)

        # to get the number of unique components, we need to find the number of
        # unique parents, so we find the parent of each node and add it to a set
        # this takes O(n * a(v)) time where n is the number of nodes and a(v) is the inverse Ackermann function
        components = set(uf.find(u) for u in range(n))

        # the graph is valid if there is only one connected component
        return len(components) == 1

        # if you use the strategy of returning True/False in the union() method
        # then here you can just return True because if you arrive here than the graph is a valid trees
        # so no need for the lines above that check the number of components
        # return True

# solution two using union find but with a different approach
# O((e * a(v)) + v) time - where e is the number of edges, v is the number of vertices, and a(v) is the
# inverse Ackermann function, a(v) is nearly constant, so the time complexity could be considered O(e + v)
# also in the worst case, we work with e = v - 1, so the time complexity could be considered O(v)
# O(v) space - to store the parent array in the union find
class Solution:
    def __init__(self):
        self.parent = []

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def validTree(self, n, edges):
        # it works also without this because in the worst case we would process all the n - 1 valid edges
        # but on the n-th edge we would return False because it would create a cycle
        # to be a valid tree, the graph should have n - 1 edges, if less
        # than not all nodes are connected, if more, then there is a cycle
        if len(edges) != n - 1:
            return False

        # initially, each node is a component
        self.parent = [u for u in range(n)]

        components = n
        for u, v in edges:
            pu = self.find(u)
            pv = self.find(v)

            # cycle detected, so return False
            # because the graph is a valid tree if there are no cycles
            if pv == pu:
                return False

            # reduce the number of components if two nodes are connected
            # by updating the parent of one of the two nodes and
            # decrementing the number of components
            self.parent[pu] = pv
            components -= 1

        # the graph is valid if there is only one connected component
        return components == 1

# solution three using dfs
# Complexity:
# O(e + v) time - where e is the number of edges and v is the number of vertices
# also in the worst case, we work with e = v - 1, so the time complexity could be considered O(v)
# O(e + v) space - to store the adjacency list
# also in the worst case, we work with e = v - 1, so the space complexity could be considered O(v)
from collections import defaultdict

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = set()

    def validTree(self, n, edges):
        # it works also without this because in the worst case we would process all the n - 1 valid edges
        # but on the n-th edge we would return False because it would create a cycle
        # to be a valid tree, the graph should have n - 1 edges, if less
        # than not all nodes are connected, if more, then there is a cycle
        if len(edges) != n - 1:
            return False

        # build the adjacency list for the graph
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)

        # checking for cycle, if there is a cycle, return False
        # because the graph is a valid tree if there are no cycles
        # -1 is just a value to indicate that the parent of the first node is None
        # because we are starting from that node, so no parent yet for it
        if self.hasCycle(-1, 0):
            return False

        # checking for connectivity, all nodes should be visited
        return len(self.visited) == n

    def hasCycle(self, parent, node):
        # mark the node as visited
        self.visited.add(node)

        for neighbor in self.graph[node]:
            if neighbor == parent:
                continue

            # if the neighbor is already visited, then there is a cycle
            # or if there is a cycle in the neighbor's subtree, retun True
            # meaning that the graph is not a valid tree because there is a cycle
            if neighbor in self.visited or self.hasCycle(node, neighbor):
                return True

        return False