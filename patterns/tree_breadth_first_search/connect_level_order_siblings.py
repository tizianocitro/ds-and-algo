# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63989951eb898f72291da2c7

'''Problem:
Given a binary tree, connect each node with its level order successor.
The last node of each level should point to a null node.

Input: [12, 7, 1, 9, 10, 5]
Output:
    12 -> None
    7 -> 1 -> None
    9 -> 10 -> 5 -> None
'''

# solution one
# Complexity:
# O(n) time - where n is the number of nodes in the tree
# O(n) space - where n is the number of nodes in the tree
from collections import deque

# level order traversal using 'next' pointer in nodes
def print_level_order(root):
    next_level_root = root
    while next_level_root:
        current = next_level_root
        next_level_root = None
        while current:
            print(str(current.val) + " ", end='')
            if not next_level_root:
                if current.left:
                    next_level_root = current.left
                elif current.right:
                    next_level_root = current.right
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
        
        while q:
            node_at_level = len(q)
            prev = None
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

