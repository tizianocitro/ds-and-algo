# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/651a85ec58fd4e18cd6e4fe3

'''Problem:
Given a directed acyclic graph with n nodes labeled from 0 to n-1,
determine the smallest number of initial nodes such that you can access all the nodes by traversing edges.
Return these nodes.

Input: n = 6, edges = [[0,1], [0,2], [2,5], [3,4], [4,2]]
Expected Output: [0,3]
Explaination: Starting from nodes 0 and 3, you can reach all other nodes in the graph.
Starting from node 0, you can reach nodes 1, 2, and 5.
Starting from node 3, you can reach nodes 4 and 2 (and by extension 5).
'''

'''Solution:
To solve the problem, we focus on in-degrees which represent the number of incoming edges to a node.
In a directed graph, if a node doesn't have any incoming edges (in-degree of 0), then it means that the node cannot be reached from any other node.
Hence, such nodes are mandatory starting points to ensure that every node in the graph can be reached.
Our algorithm thus identifies all nodes with an in-degree of 0 as they are potential starting points to traverse the entire graph.
Starting from them, we will be able to reach all other nodes in the graph. This is because the graph is acyclic, so there are no cycles to prevent us from reaching all nodes.
'''

# solution one with one set
# Complexity:
# O(v + e) time - where v is the number of nodes and e is the number of edges
# O(v) space - where n is the number of nodes
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges):
        nodes_with_incoming_edges = set()
        # traverse the edges and add the destination nodes to the set,
        # because it has incoming edges -- O(e) time
        for _, dest in edges:
            nodes_with_incoming_edges.add(dest)
        # traverse all nodes to find the ones with no incoming edges -- O(v) time
        return [node for node in range(n) if node not in nodes_with_incoming_edges]

# solution two with two arrays
# Complexity:
# O(v + e) time - where v is the number of nodes and e is the number of edges
# O(v) space - where n is the number of nodes
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges):
        in_degrees = [0] * n
        # traverse the edges and add the destination nodes to the set,
        # because it has incoming edges -- O(e) time
        for _, dest in edges:
            in_degrees[dest] += 1

        # traverse all nodes to find the ones with no incoming edges -- O(v) time
        starting_nodes = []
        for node in range(n):
            if in_degrees[node] == 0:
                starting_nodes.append(node)

        return starting_nodes

