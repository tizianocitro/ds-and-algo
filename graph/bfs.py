# !difficulty: medium

# You're given a Node class that has a name and an array of optional children nodes. When put together, nodes form an acyclic tree-like structure.
# Implement the breadthfirstSearch method on the Node class, which takes in an empty array, traverses the tree using the Breadth-first Search approach (specifically navigating the tree from left to right),
# stores all of the nodes' names in the input array, and returns it.

# Complexity
# O(V + E) time - where V is the number of vertixes and E is the number of edges
# O(V) space - where V is the number of vertixes

# Each vertex is visited once, and all its adjacent vertices are processed.
# Therefore, the time complexity of BFS is proportional to the sum of the number of vertices and the number of edges in the graph.
# Since each vertex and each edge is processed once, the time complexity is O(V + E).
# The space complexity of BFS is influenced by the queue used to store the vertices during traversal.
# At any given time, the queue can store at most the vertices of the current level.
# In the worst case, when all vertices are enqueued at the same level, the maximum number of vertices in the queue can be equal to the number of vertices (V).
# Therefore, the space complexity is O(V).
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            node = queue.pop(0)
            array.append(node.name)
            for child in node.children:
                queue.append(child)
        return array