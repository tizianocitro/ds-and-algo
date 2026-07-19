# !code: 133, !difficulty: medium, !from: https://leetcode.com/problems/clone-graph, https://neetcode.io/problems/clone-graph

'''Problem:
Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors:

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on.
The graph is represented in the test case using an adjacency list. An adjacency list is a collection of unordered lists used to represent a finite graph.
Each list describes the set of neighbors of a node in the graph. The given node will always be the first node with val = 1.

You must return the copy of the given node as a reference to the cloned graph.

Constraints:
- The number of nodes in the graph is in the range [0, 100]
- 1 <= Node.val <= 100
- Node.val is unique for each node
- There are no repeated edges and no self-loops in the graph
- The Graph is connected and all nodes can be visited starting from the given node

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
'''

# solution one using bfs
# Complexity:
# O(v + e) time - where v is the number of vertices and e is the number of edges in the graph, since we visit each vertex and edge once
# O(v) space - since we store a clone of each vertex in the graph, and the queue can hold at most v vertices at a time
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return None

        # we can use a dict to keep track of the nodes we've already cloned, using the node's value as the key
        # it also allows us to keep track of visited nodes, since we only add a node to the queue the first time we encounter it
        id_to_node = {1: Node(node.val)}

        q = deque([node])
        while q:
            original_node = q.popleft()

            # the node will already be in the id_to_node dict since we add it
            # when we first encounter it as a neighbor of another node
            clone_node = id_to_node[original_node.val]

            for original_child in original_node.neighbors:
                # if the node is not in id_to_node, we haven't visited it before
                if original_child.val not in id_to_node:
                    # so, we clone it
                    clone_child = Node(original_child.val)
                    id_to_node[original_child.val] = clone_child
                    # and add it to the queue so we can visit its neighbors later
                    q.append(original_child)

                # add the cloned child to the neighbors of the cloned node
                clone_child = id_to_node[original_child.val]
                clone_node.neighbors.append(clone_child)

        return id_to_node[1]
