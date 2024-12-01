# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6397aabd009f4ccc0648b8ca

'''Problem:
Given a binary tree, populate an array to represent the averages of all of its levels.

Input: [12, 7, 1, 9, 2, 10, 5]
Output: [12.0, 4.0, 6.5]
'''

'''Similar Problem:
Problem: Find the largest value on each level of a binary tree.
Solution: We will follow a similar approach, but instead of having a running sum we will track the maximum value of each level.
Snippets:
- maxValue = max(maxValue, currentNode.val)
- result.append(maxValue)
'''

# solution one
# Complexity:
# O(n) time - where n is the number of nodes in the tree
# O(n + w) space - where w is the number of levels in the tree and n is the number of nodes in the tree
# n is bigger than w, so the space complexity is O(n)
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def findLevelAverages(self, root):
        result = []
        if not root:
            return result

        q = deque()
        q.append(root)

        while q:
            node_at_level = len(q)
            total = 0

            for _ in range(node_at_level):
                node = q.popleft()
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(total / node_at_level)

        return result
