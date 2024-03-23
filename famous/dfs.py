# !difficulty: easy

# You're given a Node class that has a name and an array of optional children nodes. 
# When put together, nodes form an acyclic tree-like structure.
# Implement the depthFirstSearch method on the Node class, which takes in an empty array,
# traverses the tree using the Depth-first Search approach (specifically navigating the tree from left to right), 
# stores all of the nodes' names in the input array, and returns it.

# Complexity
# O(V + E) time - where V is the number of vertixes and E is the number of edges
# O(V) space - where V is the number of vertixes

# iterative solution
# Itvisits each vertex once and explores all its adjacent vertices.
# For each visited vertex, it pushes its unvisited neighbors onto the stack.
# This process continues until the stack becomes empty.
# Since each vertex and each edge is processed once, the time complexity is O(V + E).
# The space complexity is influenced by the maximum size of the stack.
# It can be expressed as O(V) in the worst-case scenario, where V is the number of vertices.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        stack = [self]
        while len(stack) > 0:
            node = stack.pop()
            array.append(node.name)
            for i in range(len(node.children) - 1, -1, -1):
                stack.append(node.children[i])
        return array

# recursive solution
# It visits each vertex once and recursively explores its adjacent vertices.
# It backtracks when it reaches a leaf node or when there are no unvisited neighbors.
# Each vertex and each edge is visited once, resulting in a time complexity of O(V + E).
# The space complexity is influenced by the maximum depth of the recursion.
# It can be expressed as O(V) in the worst-case scenario, where V is the number of vertices.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
