# !difficulty: medium

'''Problem:
Given a binary tree, populate an array to represent its zigzag level order traversal.
You should populate the values of all nodes of the first level from left to right,
then right to left for the next level and keep alternating in the same manner for the following levels.

Input: [12, 7, 1, 9, None, 10, 5, 20, 17, None, None]
Output: [[12], [1, 7], [9, 10, 5], [17, 20]]
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
        if not root:
            return []

        add_from_right = False
        result, q = [], deque()
        q.append(root)

        while q:
            node_at_level = len(q)
            current_level = deque()

            for _ in range(node_at_level):
                current_node = q.popleft()

                if add_from_right:
                    current_level.appendleft(current_node.val)
                else:
                    current_level.append(current_node.val)
                
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
            
            result.append(list(current_level))
            add_from_right = not add_from_right

        return result

# solution two using python's list
# Complexity:
# O(n) time - where n is the number of nodes in the binary tree
# O(n) space - where n is the number of nodes in the binary tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def traverse(self, root):
        if not root:
            return []

        add_from_right = False
        result, q = [], []
        q.append(root)

        while q:
            node_at_level = len(q)
            current_level = []

            for _ in range(node_at_level):
                # equivalent to deque.popleft()
                current_node = q.pop(0)

                if add_from_right:
                    # equivalent to deque.appendleft(current_node.val)
                    current_level.insert(0, current_node.val)
                else:
                    current_level.append(current_node.val)
                
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
            
            result.append(current_level)
            add_from_right = not add_from_right

        return result
