# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63dd79528dcac62aa5cc1372

'''Problem:
Given a binary tree, find its maximum depth (or height).

Input: [1, 2, 3, 4, 5]
Output: 3

Input: [1, 2, 3, 4, 5, 6, 7]
Output: 3

Input: [12]
Output: 1
'''

# solution one
# Complexity:
# O(n) time - where n is the number of nodes in the tree
# O(n) space - where n is the number of levels in the tree
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def findDepth(self, root):
        maximumTreeDepth = 0
        if not root:
            return maximumTreeDepth

        q = deque()
        q.append(root)

        while q:
            maximumTreeDepth += 1
            node_at_level = len(q)

            for _ in range(node_at_level):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return maximumTreeDepth
