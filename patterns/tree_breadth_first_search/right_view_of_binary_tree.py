# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63989ddfa1cb64009de121d1

'''Problem:
Given a binary tree, return an array containing nodes in its right view.
The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.

Input: [12, 7, 1, 9, 10, 5]
Output: [12, 1, 5]
'''

'''Similar problems:
Problem: Given a binary tree, return an array containing nodes in its left view. The left view of a binary tree is the set of nodes visible when the tree is seen from the left side.
Solution: We will be following a similar approach, but instead of appending the last element of each level, we will be appending the first element of each level to the output array.
'''

# solution one
# Complexity:
# O(n) time - where n is the number of nodes in the tree
# O(n) space - where n is the number of nodes in the tree
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def traverse(self, root):
        result = []
        if not root:
            return result

        q = deque()
        q.append(root)

        while q:
            node_at_level = len(q)
            for i in range(node_at_level):
                node = q.popleft()
                if i == node_at_level - 1:
                    result.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return result
