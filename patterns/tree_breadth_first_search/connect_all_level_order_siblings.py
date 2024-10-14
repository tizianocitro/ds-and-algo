# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63989c048d812da0aa12bff7

'''Problem:
Given a binary tree, connect each node with its level order successor.
The last node of each level should point to the first node of the next level.

Input: [12, 7, 1, 9, 10, 5]
Output: 12 -> 7 -> 1 -> 9 -> 10 -> 5 -> None
'''

# solution one
# Complexity:
# O(n) time - where n is the number of nodes in the tree
# O(n) space - where n is the number of nodes in the tree
from collections import deque

# level order traversal using 'next' pointer in nodes
def print_level_order(root):
    nextLevelRoot = root
    while nextLevelRoot:
        current = nextLevelRoot
        nextLevelRoot = None
        while current:
            print(str(current.val) + " ", end='')
            if not nextLevelRoot:
                if current.left:
                    nextLevelRoot = current.left
                elif current.right:
                    nextLevelRoot = current.right
            current = current.next
    print()

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = self.next = None

class Solution:
    def connect(self, root):
        if not root:
            return None

        q = deque()
        q.append(root)
        prev = None

        while q:
            node_at_level = len(q)
            for i in range(node_at_level):
                current = q.popleft()
                if prev:
                    prev.next = current
                prev = current

                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)

        return root

