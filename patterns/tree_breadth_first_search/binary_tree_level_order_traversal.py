# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6394fcd622692a384ae7dbdd

'''Problem:
Given a binary tree, populate an array to represent its level-by-level traversal.
You should populate the values of all nodes of each level from left to right in separate sub-arrays.

Input: [12, 7, 1, 9, None, 10, 5]
Output: [[12], [7, 1], [9, 10, 5]]
'''

'''Solution:
We can use a Queue to efficiently traverse in BFS fashion. Here are the steps of our algorithm:

1. Start by pushing the root node to the queue.
2. Keep iterating until the queue is empty.
3. In each iteration, first count the elements in the queue (let’s call it levelSize). We will have these many nodes in the current level.
4. Next, remove levelSize (it is the length of the queue at the current step) nodes from the queue and push their value in an array to represent the current level.
5. After removing each node from the queue, insert both of its children into the queue.
6. If the queue is not empty, repeat from step 3 for the next level.
'''

# solution one with array simulating a queue
# Complexity:
# O(n) time - where n is the number of nodes in the binary tree
# O(n) space - where n is the number of nodes in the binary tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def traverse(self, root):
        if root is None:
            return []
        result, queue = [], [root]

        while queue:
            current_level = []
            node_at_level = len(queue)
            for _ in range(node_at_level):
                current_node = queue.pop(0)

                current_level.append(current_node.val)

                # insert the children of current node in the queue
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)

            result.append(current_level)

        return result

# solution one with python's deque
# Complexity:
# O(n) time - where n is the number of nodes in the binary tree
# O(n) space - where n is the number of nodes in the binary tree
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def traverse(self, root):
        result = []
        if root is None:
            return result

        queue = deque()
        queue.append(root)
        while queue:
            node_at_level = len(queue)
            current_level = []
            for _ in range(node_at_level):
                current_node = queue.popleft()
                
                # add the node to the current level
                current_level.append(current_node.val)
                
                # insert the children of current node in the queue
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            result.append(current_level)

        return result