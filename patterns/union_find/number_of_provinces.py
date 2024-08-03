# !difficulty: medium, !from:

'''Problem:
There are n cities. Some of them are connected in a network.
If City A is directly connected to City B, and City B is directly connected to City C, city A is directly connected to City C.
If a group of cities are connected directly or indirectly, they form a province.

Given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, 
and isConnected[i][j] = 0 otherwise, determine the total number of provinces.

Constraints:
- 1 <= n <= 200
- n == isConnected.length
- n == isConnected[i].length
- isConnected[i][j] is 1 or 0
- isConnected[i][i] == 1
- isConnected[i][j] == isConnected[j][i]

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Explanation: Here, city 1 and 2 form a single provenance, and city 3 is one provenance itself.

Input: isConnected = [1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: In this scenario, no cities are connected to each other, so each city forms its own province.

Input: isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,0],[1,0,0,1]]
Output: 2
Explanation: Cities 1 and 4 form a province, and cities 2 and 3 form another province, resulting in a total of 2 provinces.
'''


'''Other solutions:
Look at the patterns/graph/number_of_provinces.py file for other solutions to this problem.
'''

# solutione one using union find
# Complexity:
# O(n^2) time - to iterate over the n x n matrix where n is the number of cities
# O(n) space - to store the parent and rank arrays
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
    def findProvinces(self, is_connected):
        n = len(is_connected)
        uf = UnionFind(n)

        # initially each node is a province
        num_provinces = n

        # matrix is nxn
        for i in range(n):
            for j in range(n):
                # if i and j are pointing to the same the node
                # or if the two nodes are already in the same province,
                # just skip them 
                if i == j or uf.find(i) == uf.find(j):
                    continue

                # everytime you reach two nodes that are connected
                # but they are not in the same province, merge them
                # and decrease the number of provinces
                if is_connected[i][j] == 1:
                    # merge connected nodes that are not in the same province yet
                    uf.union(i, j)
                    # decrease the number of provinces
                    num_provinces -= 1

                # the body of the two for loop can also be written in the following way
                # if i != j and uf.find(i) != uf.find(j) and is_connected[i][j] == 1:
                #     # merge connected nodes that are not in the same province yet
                #     uf.union(i, j)
                #     # decrease the number of provinces
                #     num_provinces -= 1

        return num_provinces
