# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6397900a721fdbdbc77e92ad

'''Problem:
Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first.
You should populate the values of all nodes in each level from left to right in separate sub-arrays.

Input: [12, 7, 1, 9, None, 10, 5]
Output: [[9, 10, 5], [7, 1], [12]]
'''

# solution one using python's deque
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
        if root is None:
            return []

        # initialize the result as a deque to allow for appending to the front of the list
        result, deq = deque(), deque()
        deq.append(root)

        while deq:
            node_at_level = len(deq)
            current_level = []
            for _ in range(node_at_level):
                current_node = deq.popleft()
                current_level.append(current_node.val)

                if current_node.left:
                    deq.append(current_node.left)
                if current_node.right:
                    deq.append(current_node.right)

            # with deque appendleft costs O(1) time because deques are implemented as doubly linked lists
            # prepend the current level to the result, adding it to the front of the list
            result.appendleft(current_level)

        # convert the deque to a list
        return [list(level) for level in result]
