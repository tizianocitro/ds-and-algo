# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6398a0a974c44bdc88129966

'''Problem:
Given a binary tree and a number S, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals S.

Input: [12, 7, 1, 9, None, 10, 5], S = 23
Output: True
Explanation: There is a path from the root to the leaf with a sum of 23 (12 -> 1 -> 10).
'''

# solition one with recursion and no sum variable value change
# Complexity:
# O(n) time - where n is the number of nodes in the tree
# O(n) space - where n is the number of nodes in the tree because,
# in the worst case, the recursive call stack will be equal to the height of the tree
# the worst case will happen when the given tree is a linked list (i.e., every node has only one child)
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPath(self, root, sum):
        if root is None:
            return False
        
        # if the current node is a leaf and its value is equal to the sum, we've found a path
        if root.val == sum and root.left is None and root.right is None:
            return True

        # recursively call to traverse the left and right sub-tree
        # return true if any of the two recursive call return true
        return self.hasPath(root.left, sum - root.val) or self.hasPath(root.right, sum - root.val)

# solition two with recursion and sum variable value change
# Complexity:
# O(n) time - where n is the number of nodes in the tree
# O(n) space - where n is the number of nodes in the tree because,
# in the worst case, the recursive call stack will be equal to the height of the tree
# the worst case will happen when the given tree is a linked list (i.e., every node has only one child)
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPath(self, root, sum):
        if root is None:
            return False
        
        # if the current node is a leaf and its value is equal to the sum, we've found a path
        if root.val == sum and root.left is None and root.right is None:
            return True

        # subtract the value of the current node from the sum,
        # in this way, it will be reduced fro when it reaches a leaf
        sum -= root.val

        # recursively call to traverse the left and right sub-tree
        # return true if any of the two recursive call return true
        return self.hasPath(root.left, sum) or self.hasPath(root.right, sum)
