# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639894f2e4cab4072de783e2

'''Problem:
Given a binary tree and a node, find the level order successor of the given node in the tree.
The level order successor is the node that appears right after the given node in the level order traversal.

Input: [12, 7, 1, 9, 10, 5, 6], 12
Output: 7
'''

# solution one with one node traversal at each iteration
# Complexity:
# O(n) time - where n is the number of nodes in the tree
# O(n) space - where n is the number of nodes in the tree,
# each level has at most n/2 nodes and this will happen at the lowest level of the tree
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def findSuccessor(self, root, key):
        if not root:
            return None

        queue = deque()
        queue.append(root)

        while queue:
            current_node = queue.popleft()
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

            # when we find the key, the next node in front of the queue is the successor
            # so we break the loop, but it is important that we already added the children of the current node
            if current_node.val == key:
                break

        return queue.popleft()


# solution two with level traversal at each iteration
# Complexity:
# O(n) time - where n is the number of nodes in the tree
# O(n) space - where n is the number of nodes in the tree,
# each level has at most n/2 nodes and this will happen at the lowest level of the tree
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def findSuccessor(self, root, key):
        if not root:
            return None

        queue = deque()
        queue.append(root)
        is_next_succ = False

        while queue:
            node_at_level = len(queue)
            for _ in range(node_at_level):
                current_node = queue.popleft()

                if is_next_succ:
                    return current_node
                if current_node.val == key:
                    is_next_succ = True

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

        return root
