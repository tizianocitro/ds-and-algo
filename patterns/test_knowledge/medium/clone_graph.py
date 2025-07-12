# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/clone-graph-medium

'''Problem:
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

Constraints:
- node.val is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The graph is connected and all nodes can be visited starting from the given node.

Input:
    1--2
    |  |
    4--3
Expected Output:
    1--2
    |  |
    4--3
Explanation: The graph has four nodes with the following connections:
    Node 1 is connected to nodes 2 and 4.
    Node 2 is connected to nodes 1 and 3.
    Node 3 is connected to nodes 2 and 4.
    Node 4 is connected to nodes 1 and 3.

Input:
    1--2
   /    \
  5      3
         |
         4
Expected Output:
    1--2
   /    \
  5      3
         |
         4
Explanation: The graph consists of five nodes with these connections:
    Node 1 is connected to nodes 2 and 5.
    Node 2 is connected to nodes 1 and 3.
    Node 3 is connected to nodes 2 and 4.
    Node 4 is connected to node 3.
    Node 5 is connected to node 

Input:
    1--2
   /    \
  4      3
   \    /
    5--6
Expected Output:
    1--2
   /    \
  4      3
   \    /
    5--6
Explanation: The graph has six nodes with the following connections:
    Node 1 is connected to nodes 2 and 4.
    Node 2 is connected to nodes 1 and 3.
    Node 3 is connected to nodes 2 and 6.
    Node 4 is connected to nodes 1 and 5.
    Node 5 is connected to nodes 4 and 6.
    Node 6 is connected to nodes 3 and 5.
'''

# solution one using dfs
# O(v + e) time - where v is the number of vertices and e is the number of edges
# O(v) space - for the cloned graph and the visited nodes
class GraphNode:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        return self.dfs(node, {})

        # if you want to see the visited nodes
        # visited = {}
        # cloned_node = self.dfs(node, visited)
        # for k, v in visited.items():
        #    print(k, '--->', [node.val for node in v.neighbors])
        # return cloned_node

    def dfs(self, node, visited):
        # if the node has already been visited, return the cloned node
        # so that it can be added to the parent without further recursion
        if node.val in visited:
            return visited[node.val]

        # clone the node and add it to the visited nodes
        cloned_node = GraphNode(node.val, [])
        visited[cloned_node.val] = cloned_node

        # visit the neighbors of the node
        for neighbor in node.neighbors:
            cloned_neighbor = self.dfs(neighbor, visited)
            cloned_node.neighbors.append(cloned_neighbor)

        return cloned_node

    def printGraph(self, node):
        # Use bfs to print the graph
        from collections import deque

        printed = set()
        queue = deque([node])
        while queue:
            current = queue.popleft()
            if current not in printed:
                print(current.val, '-->', [n.val for n in current.neighbors])
                for n in current.neighbors:
                    queue.append(n)
                printed.add(current)