# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/639b62040dbaa5118a4b5e96

'''Problem:
Given a binary tree, find the length of its diameter.
The diameter of a tree is the number of nodes on the longest path between any two leaf nodes.
The diameter of a tree may or may not pass through the root.

Note: You can always assume that there are at least two leaf nodes in the given tree.

Input: [1, 2, 3, 4, None, 5, 6]
Output: 5
Explanation: The diameter of the tree is: [4, 2, 1, 3, 6]
'''

# solution one with class level variable
# Complexity:
# O(n) time - where n is the number of nodes in the tree
# O(n) space - where n is the number of nodes in the tree
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # instance variable to store the diameter of the tree
    def __init__(self):
        self.tree_diameter = 0

    def findDiameter(self, root):
        # instead of using __init__ method to initialize the instance variable,
        # we can initialize it here:
        # self.treeDiameter = 0
        self.dfsDiameter(root)
        return self.tree_diameter

    def dfsDiameter(self, root):
        if root is None:
            return 0

        left_longest = self.dfsDiameter(root.left)
        right_longest = self.dfsDiameter(root.right)

        # calculate the diameter at the current node
        diameter = left_longest + right_longest + 1

        # get the longest diameter
        self.tree_diameter = max(self.tree_diameter, diameter)

        # get the longest path that exists from the current node to a leave
        # to do so we get the longst path to a leave from the subtree that have the current node's children as roots
        longest = max(left_longest, right_longest) + 1

        return longest

# solution two without class level variable
# Complexity:
# O(n) time - where n is the number of nodes in the tree
# O(n) space - where n is the number of nodes in the tree
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDiameter(self, root):
        tree_diameter = 0
        tree_diameter, _ = self.dfsDiameter(root)
        return tree_diameter

    def dfsDiameter(self, root):
        # this happens when recursive call is performed on a leave,
        # just return 0 as the diameter and longest path to a leave
        if root is None:
            return 0, 0

        # left_diameter is the longest diameter in the subtree that has root.left as root
        # left_longest is the longest path to a leave in the subtree that has root.left as root
        # the same is true for the right subtree
        left_diameter, left_longest = self.dfsDiameter(root.left)
        right_diameter, right_longest = self.dfsDiameter(root.right)

        # calculate the diameter at the current node
        diameter = left_longest + right_longest + 1
        # get the longest diameter from the subtree that have the current node's children as roots
        longest_child_diameter = max(left_diameter, right_diameter)
        # get the longest diameter
        longest_diameter = max(diameter, longest_child_diameter)

        # get the longest path that exists from the current node to a leave
        # to do so we get the longst path to a leave from the subtree that have the current node's children as roots
        longest = max(left_longest, right_longest) + 1

        return longest_diameter, longest