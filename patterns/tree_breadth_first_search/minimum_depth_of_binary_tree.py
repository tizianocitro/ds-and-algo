# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6397ac3f197fbea348eb0f04

'''Problem:
Find the minimum depth of a binary tree.
The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.

Input: [1, 2, 3, 4, 5]
Output: 2

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
        minimumTreeDepth = 0
        if not root:
            return minimumTreeDepth

        q = deque()
        q.append(root)

        while q:
            minimumTreeDepth += 1
            node_at_level = len(q)

            for _ in range(node_at_level):
                node = q.popleft()
                if not node.left and not node.right:
                    return minimumTreeDepth

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return minimumTreeDepth
