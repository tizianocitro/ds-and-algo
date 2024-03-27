# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/6399dbf40d7254be596612d2

'''Problem:
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.

Input: [1, 7, 9, None, None, 2, 9], [1, 9, 9]
Output: True
Explanation: The tree has a path 1 -> 9 -> 9.
'''

# solution one using the sequence index to match the current node value
# Complexity:
# O(n) time - where n is the number of nodes in the tree
# O(n) space - where n is the number of nodes in the tree
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findPath(self, root, sequence):
        return self.dfsPath(root, sequence, 0)

    def dfsPath(self, root, sequence, index):
        if root is None:
            return False

        length = len(sequence)
        if index >= length or root.val != sequence[index]:
            return False

        if root.left is None and root.right is None:
            # check if the current node is the last node in the sequence
            # by checking if we reached the last index in the sequence
            # the check at line 62 excludes the possibility that the current node
            # is different from the last element in the sequence
            return index == length - 1

        return self.dfsPath(root.left, sequence, index + 1) or self.dfsPath(root.right, sequence, index + 1)

# solution two with reverse of the input sequence to use pop() method
# Complexity:
# O(n) time - where n is the number of nodes in the tree
# O(n) space - where n is the number of nodes in the tree
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findPath(self, root, sequence):
        sequence.reverse()
        return self.dfsPath(root, sequence)

    def dfsPath(self, root, sequence):
        if root is None or len(sequence) < 1:
            return False

        is_path = root.val == sequence[-1]
        if not is_path:
            return False

        if root.left is None and root.right is None:
            # check if the current node is the same as last node in the sequence
            return root.val == sequence[-1]
        else:
            current = sequence.pop()
            is_path = self.dfsPath(root.left, sequence) or self.dfsPath(root.right, sequence)

            # append the last node again because we need to move back to the parent node
            sequence.append(current)

        return is_path