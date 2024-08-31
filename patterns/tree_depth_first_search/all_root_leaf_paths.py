# !difficulty: easy, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/63dd748dc496b56f43554c4e

'''Problem:
Given a binary tree, return all root-to-leaf paths.

Input: [1, 2, 3, None, 5]
Output: ["1->2->5", "1->3"]
'''

# solution one
# Complexity:
# O(nlogn) time - where n is the number of nodes in the tree and logn is the max length of a path
# O(nlogn) space - where n is the number of nodes in the tree and logn is the max length of a path
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findPaths(self, root):
        allPaths = []
        self.dfsPaths(root, allPaths, [])
        return allPaths

    def dfsPaths(self, root, allPaths, currentPath):
        if root is None:
            return

        # since lists in Python are mutable objects, when currentPath changes in subsequent recursive calls,
        # it also affects the values stored in allPaths, thus we need to make a copy of the currentPath
        currentPath.append(root.val)

        if root.left is None and root.right is None:
            allPaths.append(list(currentPath))
        else:
            self.dfsPaths(root.left, allPaths, currentPath)
            self.dfsPaths(root.right, allPaths, currentPath)

        del currentPath[-1]