# difficulty: medium, !from: https://www.designgurus.io/course-play/grokking-the-coding-interview/doc/same-tree-medium

'''Problem:
Given the roots of two binary trees 'p' and 'q', write a function to check if they are the same or not.
Two binary trees are considered the same if they met following two conditions:
- Both tree are structurally identical.
- Each corresponding node on both the trees have the same value.

Input: [1,2,3], [1,2,3]
Output: true

Input: [1,2], [1,null,2]
Output: false

Input: [1,2,1], [1,1,2]
Output: false
'''

# solution one multi-threaded version of solution three
# Complexity:
# O(v) time - where v is the number of nodes in the tree
# O(h) space - where h is the height of the tree, where h = v is the tree is a linked list
import os
import threading

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.isSame = True

    def isSameTree(self, p, q):
        num_threads = os.cpu_count()
        return self.isSameTreeMultiThreaded(p, q, num_threads)

    def isSameTreeMultiThreaded(self, p, q, num_threads):
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not p or not q:
            return False
        # one of p and q has a different value
        if p.val != q.val:
            return False

        # if we can start more threads, we will spawn a new thread to check the
        # right subtree, otherwise we will do everything in the current thread
        # notice that we halve the number of threads available for each sub-tree
        # to avoid overloading the system with threads
        if num_threads > 0:

            # function to check the right sub-tree in a separate thread
            def checkRightSubtree():
                # nonlocal is used to indicate that the variables p, q, and num_threads are not local
                # to checkRightSubtree, these variables are defined in an enclosing scope (the function or
                # block that contains checkRightSubtree()), but not as global variables
                nonlocal p, q, num_threads
                self.isSame &= self.isSameTreeMultiThreaded(p.right, q.right, num_threads // 2)

            # spawn a separate thread for checking the right sub-tree
            # by executing the checkRightSubtree function
            t1 = threading.Thread(target=checkRightSubtree)
            t1.start()

            # check the left sub-tree in the current thread
            self.isSame &= self.isSameTreeMultiThreaded(p.left, q.left, num_threads // 2)

            # wait for the thread checking the right sub-tree to finish
            t1.join()
        else:
            # in case we have only one thread available,
            # we will do everything in the current thread
            self.isSame &= self.isSameTreeMultiThreaded(p.right, q.right, 0) \
                and self.isSameTreeMultiThreaded(p.left, q.left, 0)

        return self.isSame

# solution two non multi-threaded
# Complexity:
# O(v) time - where v is the number of nodes in the tree
# O(h) space - where h is the height of the tree, where h = v is the tree is a linked list
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        # if one is None and the other is not, it means they are different
        # because one three has more nodes than the other
        if (p is not None and q is None) or (p is None and q is not None):
            return False

        # in this case it means both p and q are None,
        # so we can return True because we reached leaves
        if p is None:
            return True

        # if the nodes have different values
        if p.val != q.val:
            return False

        # check if left and right trees are the same
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# solution three slightly different than solution one
# Complexity:
# O(v) time - where v is the number of nodes in the tree
# O(h) space - where h is the height of the tree, where h = v is the tree is a linked list
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not p or not q:
            return False
        # one of p and q has a different value
        if p.val != q.val:
            return False

        # check left and right subtree recursively
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
