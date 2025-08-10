# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/subtree-of-another-tree-easy

# solution one without assuming the tree contains only one node
# with the same value as the root of the subtree
# Complexity:
# O(n * m) time - where n is the number of nodes in the tree s and m is the number of nodes in the tree t
# O(n) space - for the recursive call, when the tree s is skewed (like a linked list)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def areTheSame(self, s, t):
        # if they are both leaf nodes, return True
        if not s and not t:
            return True

        # if one is a leaf node and the other is not, return False
        if not s or not t:
            return False

        # if the values of the nodes are different, return False
        if s.val != t.val:
            return False

        # compare left and right subtrees
        return self.areTheSame(s.left, t.left) and self.areTheSame(s.right, t.right)

    def isSubtree(self, s, t):
        # if tree s is empty, t can't be its subtree
        if not s:
            return False

        # check if tree rooted at current node matches t
        if self.areTheSame(s, t):
            return True

        # check if t is a subtree of the left or right subtree of s
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

# solution two assuming the tree contains only one node
# with the same value as the root of the subtree
# Complexity:
# O(n) time - where n is the number of nodes in the tree s
# O(n) space - for the recursive call, when the tree s is skewed (like a linked list)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, s, t):
        # find the root of the subtree t in s
        root = self.findSubtreeRoot(s, t)
        # if the root of the subtree t is not found in s, return False
        if not root:
            return False
        # check if the subtree rooted at the found root is the same as t
        return self.areTheSame(root, t)

    def findSubtreeRoot(self, s, t):
        # if s is empty or we reach a leaf node, return None
        if not s:
            return None

        # found the root of the subtree t in s
        if s.val == t.val:
            return s

        # search in the left and right subtrees of s
        left = self.findSubtreeRoot(s.left, t)
        return left if left else self.findSubtreeRoot(s.right, t)

    def areTheSame(self, s, t):
        # if they are both leaf nodes, return True
        if not s and not t:
            return True

        # if one is a leaf node and the other is not, return False
        if not s or not t:
            return False

        # if the values of the nodes are different, return False
        if s.val != t.val:
            return False

        # check if the left and right subtrees are the same
        return self.areTheSame(s.left, t.left) and self.areTheSame(s.right, t.right)

