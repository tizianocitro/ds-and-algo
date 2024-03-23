# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6399d8d20d7254be596610f4

'''Problem:
Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number.
Find the total sum of all the numbers represented by all paths.

Input: [1, 7, 9, None, None, 2, 9]
Output: 408
Explanation: The sum of all path numbers: 17 + 192 + 199 = 408
'''

# solution one with level multiplier for summing up the path values
# Complexity:
# O(n) time - where n is the number of nodes in the tree
# O(n) space - where n is the number of nodes in the tree
# the worst case for space complexity will happen when the given tree is a linked list (i.e., every node has only one child)
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSumOfPathNumbers(self, root):
        return self.sumPathValues(root, 0)

    def sumPathValues(self, root, sum):
        if root is None:
            return 0
        
        sum = (10 * sum) + root.val 

        if root.left is None and root.right is None:
            return sum
        else:
            return self.sumPathValues(root.left, sum) + self.sumPathValues(root.right, sum)

# solution two keeping track of the current path to a leave
# Complexity:
# O(nlogn) time - where n is the number of nodes in the tree and logn is the max length of a path
# O(nlogn) space - where n is the number of nodes in the tree and logn is the max length of a path
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSumOfPathNumbers(self, root):
        pathValues = []
        self.findPathValues(root, pathValues, [])
        return sum(pathValues)

    def findPathValues(self, root, pathValues, path):
        if root is None:
            return pathValues

        val = root.val
        path.append(val)

        if root.left is None and root.right is None:
            pathValues.append(int(''.join([str(n) for n in path])))
        else:
            self.findPathValues(root.left, pathValues, path)
            self.findPathValues(root.right, pathValues, path)

        del path[-1]
