# !code: 257, !difficulty: easy, !from: https://leetcode.com/problems/binary-tree-paths/

'''Problem:
Given a binary tree, return all root-to-leaf paths.

Input: [1,2,3,null,5]
Output: ["1->2->5","1->3"]
'''

# solution one
# Complexity:
# O(nlogn) time - where n is the number of nodes in the tree and logn is the max length of a path
# O(nlogn) space - where n is the number of nodes in the tree and logn is the max length of a path
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
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
            allPaths.append("->".join([str(n) for n in currentPath]))
        else:
            self.dfsPaths(root.left, allPaths, currentPath)
            self.dfsPaths(root.right, allPaths, currentPath)

        del currentPath[-1]
