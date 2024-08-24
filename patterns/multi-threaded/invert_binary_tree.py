# !difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/invert-binary-tree-medium

'''Problem:
Given the root of a binary tree, invert it.
To invert a binary tree means to swap the left and right children for each node in the tree.

Input: [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Input: [2,1,3]
Output: [2,3,1]

Input: [1,2]
Output: [1,2]
'''

# solution one multi-threaded version of solution three
# Complexity:
# O(v) time - where v is the number of nodes in the binary tree
# O(h) space - where h is the height of the binary tree, in the worst case,
# the height of the binary tree is O(v), when it is like a linked list
import os
import threading

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        num_threads = os.cpu_count()
        self.invert(root, num_threads)
        return root

    def invert(self, node, num_threads):
        if node is not None:
            # swap left subtree with right subtree
            node.left, node.right = node.right, node.left

            # notice that we halve the number of threads available for each sub-tree
            # to avoid overloading the system with threads
            if num_threads > 0:
                def invertRightSubTree():
                    nonlocal node, num_threads
                    self.invert(node.right, num_threads // 2)

                # spawn a separate thread to invert the right subtree
                # using the invertRightSubTree function
                t1 = threading.Thread(target=invertRightSubTree)
                t1.start()

                self.invert(node.left, num_threads // 2)

                t1.join()
            else:
                self.invert(node.left, 0)
                self.invert(node.right, 0)

# solution two multi-threaded version of solution three
# using multiprocessing module instead of os module
# and different way of creating threads
# Complexity:
# O(v) time - where v is the number of nodes in the binary tree
# O(h) space - where h is the height of the binary tree, in the worst case,
# the height of the binary tree is O(v), when it is like a linked list
import threading
import multiprocessing

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        num_threads = multiprocessing.cpu_count()
        return self.invert(root, num_threads)

    def invert(self, node, num_threads):
        if node is None:
            return None

        # swap left subtree with right subtree
        node.left, node.right = node.right, node.left

        # notice that we halve the number of threads available for each sub-tree
        # to avoid overloading the system with threads
        if num_threads > 0:
            # spawn a separate thread to invert the left subtree
            t1 = threading.Thread(target=self.invert, args=(node.left, num_threads // 2))
            t1.start()

            self.invert(node.right, num_threads // 2)

            t1.join()
        else:
            self.invert(node.left, 0)
            self.invert(node.right, 0)

        return node

# solution three
# Complexity:
# O(v) time - where v is the number of nodes in the binary tree
# O(h) space - where h is the height of the binary tree, in the worst case,
# the height of the binary tree is O(v), when it is like a linked list
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        self.invert(root)
        return root

    def invert(self, node):
        if node is not None:
            # swap left subtree with right subtree
            node.left, node.right = node.right, node.left

            # recursively invert left and right subtrees
            self.invert(node.left)
            self.invert(node.right)
