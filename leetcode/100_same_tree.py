# !code: 100, !difficulty: easy, !from: https://leetcode.com/problems/same-tree/

'''Problem:
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Constraints:
- The number of nodes in both trees is in the range [0, 100]
- -104 <= Node.val <= 104

Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Input: p = [1,2,1], q = [1,1,2]
Output: false
'''

# solution one using recursion
# Complexity:
# O(n) time - where n is the number of nodes in the tree
# O(n) space - for the recursive call stack, when the tree is skewed
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# solution two iterative
# Complexity:
# O(n) time - where n is the number of nodes in the tree
# O(n) space - for the recursive call stack, when the tree is complete and balanced
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # the queue to store the nodes of the two trees
        # that we will compare in the next iteration in a bfs manner
        queue = deque([(p, q)])

        while queue:
            node1, node2 = queue.popleft()

            # if the nodes are not equal, return False
            if not self.areNodeEquals(node1, node2):
                return False

            # if both nodes are not None, add their children to the queue
            if node1 and node2:
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))

        return True

    def areNodeEquals(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return True
